from __future__ import annotations

import json
import os
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import unreal


REPORT_STEM = "ue4_starsystem_generator_refs_probe"
ASSET_PATHS = (
    "/Game/InnerSphereData/StarSystemGenerator",
    "/ModOverride/TKUCompatEditorPatch/InnerSphereData/StarSystemGenerator",
)
TABLE_PATHS = (
    "/Game/InnerSphereData/MW5_InnerSphereData",
    "/ModOverride/TKUCompatEditorPatch/InnerSphereData/MW5_InnerSphereData",
)
PROPERTY_CANDIDATES = (
    "inner_sphere_excel_table",
    "InnerSphereExcelTable",
    "innerSphereExcelTable",
    "mw5_inner_sphere_data",
    "MW5_InnerSphereData",
    "data_table",
    "DataTable",
)


def resolve_project_root() -> Path:
    raw = os.environ.get("TKU_PROJECT_ROOT")
    if raw:
        return Path(raw).resolve()
    script_path = globals().get("__file__")
    if script_path:
        return Path(script_path).resolve().parents[2]
    return Path(r"D:\Downloads\OneDrive\Documents\code\tku-update")


PROJECT_ROOT = resolve_project_root()
REPORT_DIR = PROJECT_ROOT / "reports" / "tku_editor_first"
OUT_JSON = REPORT_DIR / f"{REPORT_STEM}.json"
OUT_MD = REPORT_DIR / f"{REPORT_STEM}.md"


def text(value: Any) -> str:
    try:
        return str(value)
    except Exception:
        return repr(value)


def jsonable(value: Any, depth: int = 0) -> Any:
    if depth > 5:
        return text(value)
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {text(k): jsonable(v, depth + 1) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [jsonable(item, depth + 1) for item in value]
    try:
        if hasattr(value, "__iter__") and not isinstance(value, (str, bytes)):
            return [jsonable(item, depth + 1) for item in list(value)]
    except Exception:
        pass
    out: dict[str, Any] = {"repr": text(value), "python_type": type(value).__name__}
    for attr in ("get_name", "get_path_name", "get_full_name"):
        try:
            out[attr] = text(getattr(value, attr)())
        except Exception:
            pass
    try:
        cls = value.get_class()
        out["unreal_class"] = text(cls.get_name())
        out["unreal_class_path"] = text(cls.get_path_name())
    except Exception:
        pass
    return out


def path_name(obj: Any) -> str | None:
    try:
        return text(obj.get_path_name())
    except Exception:
        return None


def safe(label: str, func, *args) -> dict[str, Any]:
    try:
        return {"ok": True, "value": jsonable(func(*args))}
    except Exception as exc:
        return {"ok": False, "error": f"{type(exc).__name__}: {exc}"}


def focused_members(obj: Any) -> list[str]:
    try:
        names = dir(obj)
    except Exception:
        return []
    terms = ("table", "data", "inner", "sphere", "excel", "system", "row")
    return sorted(name for name in names if any(term in name.lower() for term in terms))


def property_probe(obj: Any) -> dict[str, Any]:
    out: dict[str, Any] = {"focused_members": focused_members(obj), "candidate_reads": {}}
    names = set(PROPERTY_CANDIDATES)
    names.update(out["focused_members"])
    for name in sorted(names):
        try:
            value = obj.get_editor_property(name)
            out["candidate_reads"][name] = {"ok": True, "value": jsonable(value), "path": path_name(value)}
        except Exception as exc:
            if name in PROPERTY_CANDIDATES:
                out["candidate_reads"][name] = {"ok": False, "error": f"{type(exc).__name__}: {exc}"}
    return out


def asset_probe(asset_path: str) -> dict[str, Any]:
    out: dict[str, Any] = {"asset_path": asset_path}
    out["exists"] = safe("does_asset_exist", unreal.EditorAssetLibrary.does_asset_exist, asset_path)
    try:
        asset = unreal.EditorAssetLibrary.load_asset(asset_path)
        out["asset"] = jsonable(asset)
        out["asset_properties"] = property_probe(asset)
    except Exception as exc:
        out["asset_error"] = f"{type(exc).__name__}: {exc}"
    try:
        bp_class = unreal.EditorAssetLibrary.load_blueprint_class(asset_path)
        out["blueprint_class"] = jsonable(bp_class)
        if bp_class:
            cdo = unreal.get_default_object(bp_class)
            out["cdo"] = jsonable(cdo)
            out["cdo_properties"] = property_probe(cdo)
            calls = {}
            for method in ("generate_inner_sphere_data", "retrieve_star_system_edges", "retrieve_edge_index_list"):
                if hasattr(cdo, method):
                    calls[method] = safe(method, getattr(cdo, method))
            out["calls"] = calls
    except Exception as exc:
        out["blueprint_error"] = f"{type(exc).__name__}: {exc}"
    return out


def table_probe(table_path: str) -> dict[str, Any]:
    out: dict[str, Any] = {"table_path": table_path}
    out["exists"] = safe("does_asset_exist", unreal.EditorAssetLibrary.does_asset_exist, table_path)
    try:
        table = unreal.EditorAssetLibrary.load_asset(table_path)
        out["asset"] = jsonable(table)
        rows = [str(row) for row in unreal.DataTableFunctionLibrary.get_data_table_row_names(table)]
        row_set = set(rows)
        out["row_count"] = len(rows)
        out["sample_rows_present"] = {
            row: row in row_set for row in ("1", "3501", "3502", "4001", "4110", "7921")
        }
    except Exception as exc:
        out["error"] = f"{type(exc).__name__}: {exc}"
    return out


def build_findings(report: dict[str, Any]) -> list[str]:
    findings: list[str] = []
    for table in report.get("tables", []):
        findings.append(
            f"{table['table_path']} rows={table.get('row_count')} samples={table.get('sample_rows_present')}"
        )
    for asset in report.get("assets", []):
        cdo_reads = asset.get("cdo_properties", {}).get("candidate_reads", {})
        table_refs = []
        for name, info in cdo_reads.items():
            if not info.get("ok"):
                continue
            path = info.get("path") or json.dumps(info.get("value"), default=str)
            if path and ("InnerSphereData" in path or "DataTable" in path or "MW5_InnerSphereData" in path):
                table_refs.append(f"{name} -> {path}")
        if table_refs:
            findings.append(f"{asset['asset_path']} CDO refs: {'; '.join(table_refs)}")
        calls = asset.get("calls", {})
        for method, result in calls.items():
            value = result.get("value", {})
            if isinstance(value, dict) and "count" in value:
                findings.append(f"{asset['asset_path']}.{method} count={value.get('count')}")
    return findings


def write_markdown(report: dict[str, Any]) -> None:
    lines = [
        "# UE4 StarSystemGenerator Reference Probe",
        "",
        f"- Generated: `{report['generated_utc']}`",
        "- Safety: read-only commandlet; no assets saved.",
        "",
        "## Findings",
        "",
    ]
    for finding in report.get("findings", []):
        lines.append(f"- {finding}")
    lines.extend(["", "## Tables", ""])
    for table in report.get("tables", []):
        lines.append(f"- `{table['table_path']}` rows `{table.get('row_count')}` samples `{table.get('sample_rows_present')}` asset `{table.get('asset')}`")
    lines.extend(["", "## Generators", ""])
    for asset in report.get("assets", []):
        lines.append(f"### `{asset['asset_path']}`")
        lines.append(f"- Asset: `{asset.get('asset')}`")
        lines.append(f"- Blueprint class: `{asset.get('blueprint_class')}`")
        cdo_reads = asset.get("cdo_properties", {}).get("candidate_reads", {})
        for name, info in cdo_reads.items():
            if info.get("ok"):
                lines.append(f"- `{name}`: path `{info.get('path')}` value `{info.get('value')}`")
        for method, result in asset.get("calls", {}).items():
            value = result.get("value", {})
            if isinstance(value, dict):
                lines.append(f"- `{method}`: ok `{result.get('ok')}` count `{value.get('count')}` sample `{value.get('sample')}`")
            else:
                lines.append(f"- `{method}`: `{result}`")
        lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "assets": [],
        "tables": [],
        "errors": [],
    }
    for table_path in TABLE_PATHS:
        try:
            report["tables"].append(table_probe(table_path))
        except Exception:
            report["errors"].append({table_path: traceback.format_exc()})
    for asset_path in ASSET_PATHS:
        try:
            report["assets"].append(asset_probe(asset_path))
        except Exception:
            report["errors"].append({asset_path: traceback.format_exc()})
    report["findings"] = build_findings(report)
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True, default=str), encoding="utf-8")
    write_markdown(report)
    unreal.log(f"TKU StarSystemGenerator refs probe wrote {OUT_JSON}")


main()
