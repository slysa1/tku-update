from __future__ import annotations

import json
import os
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import unreal


REPORT_STEM = "ue4_starmap_model_probe_20260512"
MAP_ASSET_PATH = os.environ.get("TKU_STARMAP_MODEL_MAP", "/Game/Levels/FrontEnd/StarMap").strip()
DATA_TABLE_ASSET = "/Game/InnerSphereData/MW5_InnerSphereData"


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

KEYWORDS = (
    "star",
    "starmap",
    "system",
    "inner",
    "sphere",
    "cluster",
    "faction",
    "data",
    "generate",
    "retrieve",
    "edge",
    "model",
    "map",
)

BLUEPRINT_ASSETS = (
    "/Game/Modes/MW5GameMode",
    "/Game/Modes/CampaignMode",
    "/Game/Campaign/_common/DefaultSystemGenerator",
    "/Game/InnerSphereData/StarMapBP_UTILS",
    "/Game/InnerSphereData/StarSystemGenerator",
    "/Game/UI/FrontEnd/Starmap/StarMapActor",
    "/Game/UI/FrontEnd/Starmap/StarSystemBody",
    "/Game/Levels/FrontEnd/StarMapSceneManager",
    "/Game/Levels/FrontEnd/StarSystemSceneManager",
)

NATIVE_CLASS_CANDIDATES = (
    "MWStarMapModel",
    "MWStarMap",
    "MWStarSystem",
    "MWStarSystemBody",
    "MWInnerSphereData",
    "MWClusterDataAsset",
    "MWStarMapBorderAsset",
    "DataTableFunctionLibrary",
)

NO_ARG_METHOD_CANDIDATES = (
    "get_star_system_id_array",
    "generate_inner_sphere_data",
    "retrieve_star_system_edges",
    "get_unfogged_star_systems",
    "get_selected_star_system_id",
)

ID_ARG_METHOD_CANDIDATES = (
    "get_star_system_info_by_id",
    "get_star_system_info",
    "find_star_system_body_by_id",
    "get_star_map_border_asset_id",
)

SAMPLE_IDS = (1, 3501, 4001, 4110, 7921)

PROPERTY_CANDIDATES = (
    "star_system_generator",
    "StarSystemGenerator",
    "star_system_generator_class",
    "StarSystemGeneratorClass",
    "default_system_generator",
    "DefaultSystemGenerator",
    "inner_sphere_data",
    "InnerSphereData",
    "star_map_model",
    "StarMapModel",
    "starmap_model",
    "StarmapModel",
    "star_map_model_class",
    "StarMapModelClass",
    "star_system_info",
    "StarSystemInfo",
    "star_system_data",
    "StarSystemData",
)


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
                for key, val in items[:20]
            ],
        }
    if isinstance(value, (list, tuple, set)):
        values = list(value)
        return {
            "kind": type(value).__name__,
            "count": len(values),
            "sample": [jsonable(item, depth + 1) for item in values[:20]],
            "tail_sample": [jsonable(item, depth + 1) for item in values[-10:]],
        }
    try:
        if hasattr(value, "__iter__") and not isinstance(value, (str, bytes)):
            values = list(value)
            return {
                "kind": type(value).__name__,
                "count": len(values),
                "sample": [jsonable(item, depth + 1) for item in values[:20]],
                "tail_sample": [jsonable(item, depth + 1) for item in values[-10:]],
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


def filtered_dir(obj: Any, limit: int = 260) -> list[str]:
    try:
        names = dir(obj)
    except Exception:
        return []
    return sorted(
        name
        for name in names
        if any(keyword in name.lower() for keyword in KEYWORDS)
    )[:limit]


def safe_call(label: str, func, *args) -> dict[str, Any]:
    try:
        value = func(*args)
        return {"ok": True, "value": jsonable(value)}
    except Exception as exc:
        return {"ok": False, "error": f"{type(exc).__name__}: {exc}"}


def path_name(obj: Any) -> str:
    try:
        return text(obj.get_path_name())
    except Exception:
        return text(obj)


def class_name(obj: Any) -> str:
    try:
        return text(obj.get_class().get_name())
    except Exception:
        return type(obj).__name__


def data_table_probe() -> dict[str, Any]:
    out: dict[str, Any] = {"asset_path": DATA_TABLE_ASSET}
    asset = unreal.EditorAssetLibrary.load_asset(DATA_TABLE_ASSET)
    out["object_path"] = path_name(asset)
    out["class"] = class_name(asset)
    rows = unreal.DataTableFunctionLibrary.get_data_table_row_names(asset)
    names = [str(row) for row in rows]
    out["row_count"] = len(names)
    out["sample_rows_present"] = {str(sid): str(sid) in set(names) for sid in SAMPLE_IDS}
    out["tail_sample"] = names[-12:]
    return out


def construct_native(class_name_: str) -> dict[str, Any]:
    out: dict[str, Any] = {"class_name": class_name_}
    cls = getattr(unreal, class_name_, None)
    if cls is None:
        out["exists"] = False
        return out
    out["exists"] = True
    out["class_members"] = filtered_dir(cls)
    attempts = []
    for label, builder in (
        ("constructor", lambda: cls()),
        ("new_object", lambda: unreal.new_object(cls)),
    ):
        try:
            obj = builder()
            attempts.append({"label": label, "ok": True, "object": jsonable(obj), "members": filtered_dir(obj)})
            out["object"] = obj
            break
        except Exception as exc:
            attempts.append({"label": label, "ok": False, "error": f"{type(exc).__name__}: {exc}"})
    out["construct_attempts"] = attempts
    return out


def call_method_matrix(obj: Any) -> dict[str, Any]:
    out: dict[str, Any] = {}
    if obj is None:
        return out
    for method in NO_ARG_METHOD_CANDIDATES:
        if hasattr(obj, method):
            out[method] = safe_call(method, getattr(obj, method))
    for method in ID_ARG_METHOD_CANDIDATES:
        if hasattr(obj, method):
            out[method] = {str(sid): safe_call(f"{method}({sid})", getattr(obj, method), sid) for sid in SAMPLE_IDS}
    return out


def read_properties(obj: Any) -> dict[str, Any]:
    out: dict[str, Any] = {}
    if obj is None:
        return out
    for prop in PROPERTY_CANDIDATES:
        try:
            out[prop] = jsonable(obj.get_editor_property(prop))
        except Exception:
            pass
    return out


def decode_fib(value: str) -> str:
    chars = []
    for ch in value:
        code = ord(ch)
        chars.append(chr(code - 1) if code > 1 else ch)
    return "".join(chars)


def focused_fib_tokens(asset_path: str) -> list[str]:
    try:
        tags = unreal.EditorAssetLibrary.get_tag_values(asset_path)
        fib = str(tags.get("FiBData", ""))
    except Exception:
        return []
    decoded = decode_fib(fib) if fib else ""
    tokens = []
    for raw in decoded.replace("\n", " ").split("\x00"):
        for piece in raw.split("  "):
            clean = " ".join(piece.split())
            if not clean:
                continue
            if any(keyword in clean.lower() for keyword in KEYWORDS):
                tokens.append(clean)
    seen = set()
    out = []
    for token in tokens:
        if token not in seen:
            out.append(token)
            seen.add(token)
        if len(out) >= 180:
            break
    return out


def blueprint_probe(asset_path: str) -> dict[str, Any]:
    out: dict[str, Any] = {"asset_path": asset_path}
    try:
        asset = unreal.EditorAssetLibrary.load_asset(asset_path)
        out["asset"] = jsonable(asset)
    except Exception as exc:
        out["asset_error"] = f"{type(exc).__name__}: {exc}"
    try:
        bp_class = unreal.EditorAssetLibrary.load_blueprint_class(asset_path)
        out["blueprint_class"] = jsonable(bp_class)
        if bp_class:
            cdo = unreal.get_default_object(bp_class)
            out["cdo"] = jsonable(cdo)
            out["members"] = filtered_dir(cdo)
            out["properties"] = read_properties(cdo)
            out["calls"] = call_method_matrix(cdo)
        out["fib_tokens"] = focused_fib_tokens(asset_path)
    except Exception as exc:
        out["blueprint_error"] = f"{type(exc).__name__}: {exc}"
    return out


def level_actor_probe() -> dict[str, Any]:
    out: dict[str, Any] = {"map_asset_path": MAP_ASSET_PATH}
    try:
        out["load_map"] = jsonable(unreal.EditorLoadingAndSavingUtils.load_map(MAP_ASSET_PATH))
    except Exception as exc:
        out["load_error"] = f"{type(exc).__name__}: {exc}"
        return out
    actors = list(unreal.EditorLevelLibrary.get_all_level_actors())
    focus = []
    for actor in actors:
        cls = class_name(actor)
        name = ""
        try:
            name = text(actor.get_actor_label())
        except Exception:
            name = text(actor)
        if any(token in cls.lower() or token in name.lower() for token in ("starmap", "star system", "starsystem")):
            focus.append(
                {
                    "label": name,
                    "class": cls,
                    "path": path_name(actor),
                    "members": filtered_dir(actor, limit=160),
                    "calls": call_method_matrix(actor),
                }
            )
    out["focus_actors"] = focus
    return out


def module_symbol_probe() -> dict[str, Any]:
    symbols = {}
    all_names = dir(unreal)
    for keyword in ("StarMap", "StarSystem", "InnerSphere", "Cluster", "Faction", "DataTable"):
        symbols[keyword] = sorted(name for name in all_names if keyword.lower() in name.lower())[:250]
    return symbols


def native_probe() -> dict[str, Any]:
    out: dict[str, Any] = {}
    for name in NATIVE_CLASS_CANDIDATES:
        info = construct_native(name)
        obj = info.pop("object", None)
        if obj is not None:
            info["calls"] = call_method_matrix(obj)
        out[name] = info
    return out


def summarize_model_result(report: dict[str, Any]) -> list[str]:
    findings: list[str] = []
    table = report.get("data_table", {})
    if table.get("row_count"):
        findings.append(f"Resolved DataTable row count: {table.get('row_count')}.")
    for class_name_, info in report.get("native_classes", {}).items():
        calls = info.get("calls", {})
        ids = calls.get("get_star_system_id_array")
        if ids:
            value = ids.get("value", {})
            findings.append(f"{class_name_}.get_star_system_id_array -> {value}.")
        info_by_id = calls.get("get_star_system_info_by_id")
        if info_by_id:
            present = {
                sid: result.get("ok")
                for sid, result in info_by_id.items()
            }
            findings.append(f"{class_name_}.get_star_system_info_by_id sample ok flags: {present}.")
    for asset_path, info in report.get("blueprints", {}).items():
        calls = info.get("calls", {})
        if calls:
            findings.append(f"{asset_path} exposed callable probe methods: {sorted(calls.keys())}.")
    return findings


def write_markdown(report: dict[str, Any]) -> None:
    lines = [
        "# UE4 StarMap Model Probe - 2026-05-12",
        "",
        f"- Generated: `{report['generated_utc']}`",
        f"- Map: `{MAP_ASSET_PATH}`",
        "- Safety: read-only commandlet; no assets saved.",
        "",
        "## Findings",
        "",
    ]
    for item in report.get("findings", []):
        lines.append(f"- {item}")
    lines.extend(["", "## DataTable", ""])
    table = report.get("data_table", {})
    for key in ("object_path", "class", "row_count", "sample_rows_present", "tail_sample"):
        lines.append(f"- `{key}`: `{table.get(key)}`")
    lines.extend(["", "## Native Classes", ""])
    for name, info in report.get("native_classes", {}).items():
        lines.append(f"### `{name}`")
        lines.append(f"- exists: `{info.get('exists')}`")
        if info.get("construct_attempts"):
            lines.append(f"- construct attempts: `{info.get('construct_attempts')}`")
        if info.get("calls"):
            for method, result in info["calls"].items():
                lines.append(f"- `{method}`: `{result}`")
        if info.get("class_members"):
            lines.append(f"- members: `{info.get('class_members')[:80]}`")
        lines.append("")
    lines.extend(["## Blueprint Classes", ""])
    for asset_path, info in report.get("blueprints", {}).items():
        lines.append(f"### `{asset_path}`")
        lines.append(f"- class: `{info.get('blueprint_class')}`")
        lines.append(f"- members: `{info.get('members', [])[:120]}`")
        if info.get("properties"):
            lines.append(f"- properties: `{info.get('properties')}`")
        if info.get("calls"):
            for method, result in info["calls"].items():
                lines.append(f"- `{method}`: `{result}`")
        if info.get("fib_tokens"):
            lines.append(f"- FiB tokens: `{info.get('fib_tokens')[:80]}`")
        lines.append("")
    lines.extend(["## Level Actors", ""])
    for actor in report.get("level", {}).get("focus_actors", [])[:12]:
        lines.append(f"### `{actor.get('label')}` `{actor.get('class')}`")
        lines.append(f"- path: `{actor.get('path')}`")
        lines.append(f"- members: `{actor.get('members')[:80]}`")
        if actor.get("calls"):
            for method, result in actor["calls"].items():
                lines.append(f"- `{method}`: `{result}`")
        lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "data_table": {},
        "native_symbols": {},
        "native_classes": {},
        "blueprints": {},
        "level": {},
        "errors": [],
    }
    for key, func in (
        ("data_table", data_table_probe),
        ("native_symbols", module_symbol_probe),
        ("native_classes", native_probe),
        ("level", level_actor_probe),
    ):
        try:
            report[key] = func()
        except Exception:
            report["errors"].append({key: traceback.format_exc()})
    for asset_path in BLUEPRINT_ASSETS:
        try:
            report["blueprints"][asset_path] = blueprint_probe(asset_path)
        except Exception:
            report["errors"].append({asset_path: traceback.format_exc()})
    report["findings"] = summarize_model_result(report)
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True, default=str), encoding="utf-8")
    write_markdown(report)
    unreal.log(f"TKU StarMap model probe wrote {OUT_JSON}")


main()
