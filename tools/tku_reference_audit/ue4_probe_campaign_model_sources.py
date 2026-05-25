from __future__ import annotations

import json
import os
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import unreal


REPORT_STEM = "ue4_campaign_model_sources_probe"
TARGET_MOD_NAME = os.environ.get("TKU_CAMPAIGN_MODEL_MOD_NAME", "TKUCompatEditorPatch").strip()

FIXED_ASSETS = (
    "/Game/Modes/MW5GameMode",
    "/Game/Modes/CampaignMode",
    "/Game/Campaign/_common/DefaultSystemGenerator",
    "/Game/InnerSphereData/StarSystemGenerator",
    "/Game/InnerSphereData/MW5_InnerSphereData",
    "/Game/DLC1/CareerMode/StartConditions/CareerMode",
    "/Game/DLC1/CareerMode/StartConditions/CareerMode_Davion_Start",
    "/Game/DLC1/CareerMode/StartConditions/CareerMode_Start",
    "/Game/DLC1/CareerMode/StartConditions/FRR_CareerMode_Start",
    "/Game/DLC1/CareerMode/CareerModeCoreCampaign",
    f"/ModOverride/{TARGET_MOD_NAME}/Modes/MW5GameMode",
    f"/ModOverride/{TARGET_MOD_NAME}/Modes/CampaignMode",
    f"/ModOverride/{TARGET_MOD_NAME}/InnerSphereData/StarSystemGenerator",
    f"/ModOverride/{TARGET_MOD_NAME}/InnerSphereData/MW5_InnerSphereData",
)

DISCOVERY_PATHS = (
    "/Game/DLC1/CareerMode/StartConditions",
    "/Game/DLC1/CareerMode/StartConditions/Arcs",
    "/Game/DLC1/CareerMode/StartConditions/StartingMechs",
    "/Game/DLC1/CareerMode",
    "/Game/Campaign/_common",
    f"/ModOverride/{TARGET_MOD_NAME}",
)

KEYWORDS = (
    "career",
    "campaign",
    "cluster",
    "data",
    "default",
    "faction",
    "generate",
    "generator",
    "inner",
    "map",
    "model",
    "persistent",
    "scenario",
    "sphere",
    "star",
    "start",
    "system",
)

IMPORTANT_PATH_MARKERS = (
    "DefaultSystemGenerator",
    "StarSystemGenerator",
    "MW5_InnerSphereData",
    "CareerMode",
    "StartConditions",
    "MWStarMapModel",
    "InnerSphereMapInfo",
    "TKUCompatEditorPatch",
    "ModOverride",
)

KNOWN_PROPERTIES = (
    "campaign_system_generator_class",
    "default_inner_sphere_class",
    "inner_sphere_class",
    "inner_sphere_data",
    "inner_sphere_map_info",
    "map_info",
    "persistent_model",
    "scenario_specification",
    "star_map_model",
    "star_system_generator",
    "star_system_generator_class",
    "star_system_id",
    "start_condition",
    "start_conditions",
    "starting_location",
    "startup_scenario",
    "system_blackboard",
    "system_generator",
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


def path_name(value: Any) -> str | None:
    try:
        return text(value.get_path_name())
    except Exception:
        return None


def class_path(value: Any) -> str | None:
    try:
        return text(value.get_class().get_path_name())
    except Exception:
        return None


def class_name(value: Any) -> str | None:
    try:
        return text(value.get_class().get_name())
    except Exception:
        return None


def jsonable(value: Any, depth: int = 0) -> Any:
    if depth > 5:
        return text(value)
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Path):
        return str(value)
    if hasattr(value, "x") and hasattr(value, "y") and hasattr(value, "z"):
        return {"x": float(value.x), "y": float(value.y), "z": float(value.z)}
    if hasattr(value, "roll") and hasattr(value, "pitch") and hasattr(value, "yaw"):
        return {"roll": float(value.roll), "pitch": float(value.pitch), "yaw": float(value.yaw)}
    if isinstance(value, dict):
        items = list(value.items())
        return {
            "kind": "dict",
            "count": len(items),
            "sample": [
                {"key": jsonable(key, depth + 1), "value": jsonable(val, depth + 1)}
                for key, val in items[:40]
            ],
        }
    if isinstance(value, (list, tuple, set)):
        values = list(value)
        return {
            "kind": type(value).__name__,
            "count": len(values),
            "sample": [jsonable(item, depth + 1) for item in values[:40]],
            "tail_sample": [jsonable(item, depth + 1) for item in values[-20:]],
        }
    try:
        if hasattr(value, "__iter__") and not isinstance(value, (str, bytes)):
            values = list(value)
            return {
                "kind": type(value).__name__,
                "count": len(values),
                "sample": [jsonable(item, depth + 1) for item in values[:40]],
                "tail_sample": [jsonable(item, depth + 1) for item in values[-20:]],
            }
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


def get_class_lineage(value: Any) -> list[str]:
    out: list[str] = []
    try:
        cls = value.get_class()
        while cls:
            out.append(text(cls.get_path_name()))
            cls = cls.get_super_class()
    except Exception:
        pass
    return out[:20]


def filtered_member_names(value: Any) -> list[str]:
    try:
        names = dir(value)
    except Exception:
        return []
    return sorted(
        name
        for name in names
        if not name.startswith("_") and any(keyword in name.lower() for keyword in KEYWORDS)
    )


def try_read_properties(value: Any) -> dict[str, Any]:
    names = set(KNOWN_PROPERTIES)
    names.update(filtered_member_names(value))
    props: dict[str, Any] = {}
    for name in sorted(names):
        try:
            props[name] = jsonable(value.get_editor_property(name))
        except Exception:
            continue
    return props


def decode_fib(value: str) -> str:
    chars = []
    for ch in value:
        code = ord(ch)
        chars.append(chr(code - 1) if code > 1 else ch)
    return "".join(chars)


def clean_token_runs(value: str) -> list[str]:
    allowed_extra = set("_/:. -'()+,")
    runs: list[str] = []
    current: list[str] = []
    for ch in value:
        if ch.isalnum() or ch in allowed_extra:
            current.append(ch)
            continue
        if current:
            token = " ".join("".join(current).split())
            if len(token) >= 3:
                runs.append(token)
            current = []
    if current:
        token = " ".join("".join(current).split())
        if len(token) >= 3:
            runs.append(token)
    return runs


def focused_fib_tokens(asset_path: str) -> list[str]:
    try:
        tags = unreal.EditorAssetLibrary.get_tag_values(asset_path)
        fib = str(tags.get("FiBData", ""))
    except Exception:
        return []
    if not fib:
        return []
    decoded = decode_fib(fib)
    tokens = []
    seen = set()
    for token in clean_token_runs(decoded):
        if not any(keyword in token.lower() for keyword in KEYWORDS):
            continue
        if token in seen:
            continue
        tokens.append(token)
        seen.add(token)
        if len(tokens) >= 220:
            break
    return tokens


def asset_registry() -> Any:
    return unreal.AssetRegistryHelpers.get_asset_registry()


def asset_data_to_path(asset_data: Any) -> str:
    try:
        return text(asset_data.package_name)
    except Exception:
        return text(asset_data)


def discover_assets() -> dict[str, Any]:
    registry = asset_registry()
    by_path: dict[str, list[str]] = {}
    all_paths: set[str] = set(FIXED_ASSETS)
    for base_path in DISCOVERY_PATHS:
        try:
            assets = list(registry.get_assets_by_path(base_path, True))
        except Exception:
            assets = []
        paths = sorted(asset_data_to_path(asset) for asset in assets)
        by_path[base_path] = paths
        for path in paths:
            lowered = path.lower()
            if any(keyword in lowered for keyword in ("careermode", "start", "generator", "innersphere", "cluster")):
                all_paths.add(path)
    return {"by_path": by_path, "probe_paths": sorted(all_paths)}


def table_probe(asset: Any) -> dict[str, Any]:
    out: dict[str, Any] = {}
    try:
        row_names = [str(row) for row in unreal.DataTableFunctionLibrary.get_data_table_row_names(asset)]
        out["row_count"] = len(row_names)
        out["sample_rows_present"] = {sid: sid in set(row_names) for sid in ("1", "3501", "3502", "4001", "4110", "7000", "7921")}
        out["tail_sample"] = row_names[-20:]
    except Exception as exc:
        out["error"] = f"{type(exc).__name__}: {exc}"
    return out


def object_probe(label: str, value: Any) -> dict[str, Any]:
    out: dict[str, Any] = {
        "label": label,
        "object": jsonable(value),
        "class_name": class_name(value),
        "class_path": class_path(value),
        "lineage": get_class_lineage(value),
        "members": filtered_member_names(value)[:260],
        "properties": try_read_properties(value),
    }
    return out


def asset_probe(asset_path: str) -> dict[str, Any]:
    out: dict[str, Any] = {"asset_path": asset_path}
    try:
        out["exists"] = bool(unreal.EditorAssetLibrary.does_asset_exist(asset_path))
    except Exception as exc:
        out["exists_error"] = f"{type(exc).__name__}: {exc}"
        out["exists"] = False
    if not out["exists"]:
        return out

    try:
        asset = unreal.EditorAssetLibrary.load_asset(asset_path)
        out["asset"] = object_probe("asset", asset)
        if class_name(asset) == "DataTable":
            out["data_table"] = table_probe(asset)
    except Exception as exc:
        out["asset_error"] = f"{type(exc).__name__}: {exc}"
        return out

    if class_name(asset) == "Blueprint":
        try:
            bp_class = unreal.EditorAssetLibrary.load_blueprint_class(asset_path)
            out["blueprint_class"] = jsonable(bp_class)
            if bp_class:
                cdo = unreal.get_default_object(bp_class)
                out["cdo"] = object_probe("cdo", cdo)
        except Exception as exc:
            out["blueprint_error"] = f"{type(exc).__name__}: {exc}"
    else:
        out["blueprint_skipped"] = f"asset class is {class_name(asset)}"

    out["fib_tokens"] = focused_fib_tokens(asset_path)
    try:
        refs = list(unreal.EditorAssetLibrary.find_package_referencers_for_asset(asset_path, True))
        out["referencers"] = {
            "count": len(refs),
            "focused": sorted(ref for ref in refs if any(marker in str(ref) for marker in IMPORTANT_PATH_MARKERS))[:80],
            "sample": sorted(str(ref) for ref in refs[:80]),
        }
    except Exception as exc:
        out["referencers_error"] = f"{type(exc).__name__}: {exc}"
    return out


def flatten_property_hits(asset_path: str, source_label: str, value: Any) -> list[dict[str, str]]:
    hits: list[dict[str, str]] = []
    if isinstance(value, dict):
        for key, item in value.items():
            hits.extend(flatten_property_hits(asset_path, f"{source_label}.{key}", item))
        return hits
    if isinstance(value, list):
        for idx, item in enumerate(value[:80]):
            hits.extend(flatten_property_hits(asset_path, f"{source_label}[{idx}]", item))
        return hits
    text_value = text(value)
    if any(marker.lower() in text_value.lower() for marker in IMPORTANT_PATH_MARKERS):
        hits.append({"asset_path": asset_path, "source": source_label, "value": text_value[:900]})
    return hits


def summarize(report: dict[str, Any]) -> list[str]:
    findings: list[str] = []
    discovered = report.get("discovered_assets", {})
    start_assets = discovered.get("by_path", {}).get("/Game/DLC1/CareerMode/StartConditions", [])
    findings.append(f"Discovered {len(start_assets)} assets under DLC1 CareerMode StartConditions.")

    for asset_path, info in report.get("assets", {}).items():
        table = info.get("data_table")
        if table and table.get("row_count") is not None:
            findings.append(f"{asset_path} DataTable row count: {table.get('row_count')}.")
        for label in ("asset", "cdo"):
            props = (info.get(label) or {}).get("properties") or {}
            for prop_name, prop_value in props.items():
                prop_text = text(prop_value)
                if any(marker.lower() in prop_text.lower() for marker in IMPORTANT_PATH_MARKERS):
                    findings.append(f"{asset_path} {label}.{prop_name} references {prop_text[:240]}.")
        tokens = info.get("fib_tokens") or []
        focused_tokens = [
            token
            for token in tokens
            if any(marker.lower() in token.lower() for marker in IMPORTANT_PATH_MARKERS)
        ]
        if focused_tokens:
            findings.append(f"{asset_path} focused Blueprint tokens: {focused_tokens[:12]}.")
    return findings


def write_markdown(report: dict[str, Any]) -> None:
    lines = [
        "# UE4 Campaign Model Sources Probe",
        "",
        f"- Generated: `{report['generated_utc']}`",
        f"- Target mod: `{TARGET_MOD_NAME}`",
        "- Safety: read-only commandlet; no assets saved.",
        "",
        "## Findings",
        "",
    ]
    for finding in report.get("findings", []):
        lines.append(f"- {finding}")

    lines.extend(["", "## Discovered Assets", ""])
    for base_path, assets in (report.get("discovered_assets", {}).get("by_path") or {}).items():
        lines.append(f"- `{base_path}`: `{len(assets)}`")

    lines.extend(["", "## Property Hits", ""])
    for hit in report.get("property_hits", [])[:240]:
        lines.append(f"- `{hit['asset_path']}` `{hit['source']}`: `{hit['value']}`")

    lines.extend(["", "## Assets", ""])
    for asset_path, info in report.get("assets", {}).items():
        lines.append(f"### `{asset_path}`")
        lines.append(f"- Exists: `{info.get('exists')}`")
        for label in ("asset", "cdo"):
            obj = info.get(label) or {}
            if not obj:
                continue
            lines.append(f"- {label} class: `{obj.get('class_path')}`")
            lines.append(f"- {label} lineage: `{obj.get('lineage')}`")
            props = obj.get("properties") or {}
            if props:
                lines.append(f"- {label} focused properties: `{props}`")
        if info.get("data_table"):
            lines.append(f"- DataTable: `{info.get('data_table')}`")
        tokens = info.get("fib_tokens") or []
        if tokens:
            lines.append(f"- FiB tokens: `{tokens[:120]}`")
        refs = info.get("referencers") or {}
        if refs:
            lines.append(f"- Referencers: `{refs}`")
        lines.append("")

    if report.get("errors"):
        lines.extend(["## Errors", ""])
        for error in report["errors"]:
            lines.append(f"- `{error}`")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "target_mod_name": TARGET_MOD_NAME,
        "discovered_assets": {},
        "assets": {},
        "property_hits": [],
        "errors": [],
    }
    try:
        report["discovered_assets"] = discover_assets()
        for asset_path in report["discovered_assets"]["probe_paths"]:
            try:
                report["assets"][asset_path] = asset_probe(asset_path)
            except Exception:
                report["errors"].append({asset_path: traceback.format_exc()})
        for asset_path, info in report["assets"].items():
            for label in ("asset", "cdo"):
                props = (info.get(label) or {}).get("properties") or {}
                report["property_hits"].extend(flatten_property_hits(asset_path, label, props))
        report["findings"] = summarize(report)
    except Exception:
        report["errors"].append({"fatal": traceback.format_exc()})
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True, default=str), encoding="utf-8")
    write_markdown(report)
    unreal.log(f"TKU campaign model sources probe wrote {OUT_JSON}")


main()
