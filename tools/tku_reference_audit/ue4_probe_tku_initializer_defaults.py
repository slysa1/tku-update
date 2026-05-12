from __future__ import annotations

import json
import os
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import unreal


REPORT_STEM = "ue4_initializer_defaults_probe_20260512"

ASSETS = (
    "/Game/Modes/MW5GameMode",
    "/Game/Modes/CampaignMode",
    "/Game/Campaign/_common/DefaultSystemGenerator",
    "/Game/InnerSphereData/StarSystemGenerator",
    "/Game/UI/FrontEnd/Starmap/StarMapActor",
)

PROPERTIES = (
    "default_inner_sphere_class",
    "campaign_system_generator_class",
    "persistent_model",
    "system_blackboard",
    "star_map_model",
    "travel_path_model",
    "star_system_body_look_up",
    "inner_sphere_data",
    "star_system_generator",
    "star_system_generator_class",
)

CALLS = {
    "/Game/InnerSphereData/StarSystemGenerator": (
        "generate_inner_sphere_data",
        "retrieve_star_system_edges",
        "retrieve_edge_index_list",
        "retrieve_star_system_clusters",
    ),
}


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


def jsonable(value: Any, depth: int = 0) -> Any:
    if depth > 5:
        return str(value)
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Path):
        return str(value)
    if hasattr(value, "x") and hasattr(value, "y") and hasattr(value, "z"):
        return {"x": float(value.x), "y": float(value.y), "z": float(value.z)}
    if isinstance(value, dict):
        items = list(value.items())
        return {
            "kind": "dict",
            "count": len(items),
            "sample": [
                {"key": jsonable(key, depth + 1), "value": jsonable(val, depth + 1)}
                for key, val in items[:20]
            ],
        }
    if isinstance(value, (list, tuple, set)):
        items = list(value)
        return {
            "kind": type(value).__name__,
            "count": len(items),
            "sample": [jsonable(item, depth + 1) for item in items[:20]],
            "tail_sample": [jsonable(item, depth + 1) for item in items[-10:]],
        }
    try:
        if hasattr(value, "__iter__") and not isinstance(value, (str, bytes)):
            items = list(value)
            return {
                "kind": type(value).__name__,
                "count": len(items),
                "sample": [jsonable(item, depth + 1) for item in items[:20]],
                "tail_sample": [jsonable(item, depth + 1) for item in items[-10:]],
            }
    except Exception:
        pass

    out: dict[str, Any] = {"repr": str(value), "python_type": type(value).__name__}
    for attr in ("get_name", "get_path_name", "get_full_name"):
        try:
            out[attr] = str(getattr(value, attr)())
        except Exception:
            pass
    try:
        cls = value.get_class()
        out["unreal_class"] = str(cls.get_name())
        out["unreal_class_path"] = str(cls.get_path_name())
    except Exception:
        pass
    return out


def safe_get_property(obj: Any, prop_name: str) -> dict[str, Any]:
    try:
        return {"ok": True, "value": jsonable(obj.get_editor_property(prop_name))}
    except Exception as exc:
        return {"ok": False, "error": f"{type(exc).__name__}: {exc}"}


def safe_call(obj: Any, method_name: str) -> dict[str, Any]:
    try:
        method = getattr(obj, method_name)
        return {"ok": True, "value": jsonable(method())}
    except Exception as exc:
        return {"ok": False, "error": f"{type(exc).__name__}: {exc}"}


def cdo_for_asset(asset_path: str) -> tuple[Any | None, dict[str, Any]]:
    asset = unreal.EditorAssetLibrary.load_asset(asset_path)
    info: dict[str, Any] = {"asset": jsonable(asset)}
    if asset is None:
        info["error"] = "asset did not load"
        return None, info

    generated_class = unreal.EditorAssetLibrary.load_blueprint_class(asset_path)
    info["generated_class"] = jsonable(generated_class)

    if generated_class is None:
        info["error"] = "could not resolve generated class"
        return None, info

    try:
        cdo = unreal.get_default_object(generated_class)
    except Exception as exc:
        info["error"] = f"{type(exc).__name__}: {exc}"
        return None, info

    info["cdo"] = jsonable(cdo)
    try:
        info["members"] = sorted(
            name for name in dir(cdo) if any(token in name.lower() for token in ("sphere", "system", "star", "model", "data", "edge", "cluster"))
        )
    except Exception as exc:
        info["members_error"] = f"{type(exc).__name__}: {exc}"
    return cdo, info


def probe_asset(asset_path: str) -> dict[str, Any]:
    cdo, info = cdo_for_asset(asset_path)
    if cdo is None:
        return info
    info["properties"] = {
        prop_name: result
        for prop_name in PROPERTIES
        for result in (safe_get_property(cdo, prop_name),)
        if result.get("ok")
    }
    info["property_errors"] = {
        prop_name: result["error"]
        for prop_name in PROPERTIES
        for result in (safe_get_property(cdo, prop_name),)
        if not result.get("ok")
    }
    info["calls"] = {method_name: safe_call(cdo, method_name) for method_name in CALLS.get(asset_path, ())}
    return info


def write_report(report: dict[str, Any]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")

    lines = [
        "# UE4 Initializer Defaults Probe - 2026-05-12",
        "",
        f"- Generated: `{report['generated_utc']}`",
        "",
        "## Findings",
        "",
    ]
    for finding in report.get("findings", []):
        lines.append(f"- {finding}")

    lines.extend(["", "## Assets", ""])
    for asset_path, info in report["assets"].items():
        cdo_path = (info.get("cdo") or {}).get("get_path_name")
        lines.append(f"### `{asset_path}`")
        lines.append(f"- CDO: `{cdo_path}`")
        for prop_name, result in (info.get("properties") or {}).items():
            value = result.get("value")
            if isinstance(value, dict):
                value = value.get("get_path_name") or value.get("repr") or value
            lines.append(f"- `{prop_name}`: `{value}`")
        for method_name, result in (info.get("calls") or {}).items():
            value = result.get("value")
            if isinstance(value, dict):
                value = f"{value.get('kind')} count={value.get('count')} sample={value.get('sample')} tail={value.get('tail_sample')}"
            lines.append(f"- call `{method_name}` ok=`{result.get('ok')}` value=`{value}`")
        lines.append("")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    report: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "assets": {},
        "findings": [],
        "errors": [],
    }
    try:
        for asset_path in ASSETS:
            report["assets"][asset_path] = probe_asset(asset_path)

        for asset_path, info in report["assets"].items():
            for prop_name, result in (info.get("properties") or {}).items():
                value = result.get("value")
                if isinstance(value, dict):
                    path = value.get("get_path_name") or value.get("repr")
                else:
                    path = value
                report["findings"].append(f"{asset_path}.{prop_name} -> {path}")

        gen_info = report["assets"].get("/Game/InnerSphereData/StarSystemGenerator", {})
        generate_result = (gen_info.get("calls") or {}).get("generate_inner_sphere_data", {})
        count = ((generate_result.get("value") or {}).get("count") if generate_result.get("ok") else None)
        report["findings"].append(f"StarSystemGenerator.generate_inner_sphere_data count -> {count}")
    except Exception:
        report["errors"].append(traceback.format_exc())
    write_report(report)


if __name__ == "__main__":
    main()
