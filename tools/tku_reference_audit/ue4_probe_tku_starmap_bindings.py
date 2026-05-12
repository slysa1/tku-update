from __future__ import annotations

import json
import os
import re
import traceback
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import unreal


REPORT_STEM = "ue4_starmap_binding_probe_20260512"
TARGET_MOD_NAME = os.environ.get("TKU_STARMAP_BINDING_MOD_NAME", "TKUCompatEditorPatch").strip()
MAP_ASSET_PATH = os.environ.get("TKU_STARMAP_BINDING_MAP", "/Game/Levels/FrontEnd/StarMap").strip()
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
    "body",
    "lookup",
    "inner",
    "sphere",
    "data",
    "generate",
    "spawn",
    "border",
    "cluster",
    "faction",
    "overlay",
    "constellation",
    "camera",
    "pawn",
)

PROPERTY_CANDIDATES = (
    "star_system_body_look_up",
    "StarSystemBodyLookUp",
    "star_system_body_lookup",
    "star_system_bodies",
    "StarSystemBodies",
    "star_system_body",
    "StarSystemBody",
    "star_system_body_class",
    "StarSystemBodyClass",
    "star_system_body_look_up_count",
    "inner_sphere_data",
    "InnerSphereData",
    "star_system_generator",
    "StarSystemGenerator",
    "star_map_actor",
    "StarMapActor",
    "starmap_actor",
    "StarmapActor",
    "star_map_root",
    "StarMapRoot",
    "star_map_camera",
    "StarMapCamera",
    "initial_camera_transform",
    "InitialCameraTransform",
    "border_actor",
    "BorderActor",
    "cluster_material",
    "ClusterMaterial",
    "procedural_border_mesh",
    "ProceduralBorderMesh",
    "cluster_overlay",
    "ClusterOverlay",
    "cluster_constellation",
    "ClusterConstellation",
    "cluster_faction_asset",
    "ClusterFactionAsset",
    "system_ids",
    "SystemIds",
    "star_system_id",
    "StarSystemId",
    "b_should_display_on_starmap",
    "bShouldDisplayOnStarmap",
    "b_is_star_system_hidden",
    "bIsStarSystemHidden",
    "desired_zoom_level",
    "DesiredZoomLevel",
)


def text(value: Any) -> str:
    try:
        return str(value)
    except Exception:
        return repr(value)


def path_name(obj: Any) -> str:
    try:
        return text(obj.get_path_name())
    except Exception:
        return text(obj)


def class_name(obj: Any) -> str:
    try:
        return text(obj.get_class().get_name())
    except Exception:
        return ""


def label(actor: Any) -> str:
    try:
        return text(actor.get_actor_label())
    except Exception:
        try:
            return text(actor.get_name())
        except Exception:
            return text(actor)


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
                for key, val in items[:25]
            ],
        }
    if isinstance(value, (list, tuple, set)):
        values = list(value)
        return {
            "kind": type(value).__name__,
            "count": len(values),
            "sample": [jsonable(item, depth + 1) for item in values[:25]],
        }
    try:
        if hasattr(value, "__iter__") and not isinstance(value, (str, bytes)):
            values = list(value)
            return {
                "kind": type(value).__name__,
                "count": len(values),
                "sample": [jsonable(item, depth + 1) for item in values[:25]],
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


def read_property(obj: Any, prop: str) -> dict[str, Any] | None:
    try:
        value = obj.get_editor_property(prop)
    except Exception:
        return None
    return {"property": prop, "value": jsonable(value)}


def read_property_candidates(obj: Any) -> dict[str, Any]:
    found: dict[str, Any] = {}
    for prop in PROPERTY_CANDIDATES:
        item = read_property(obj, prop)
        if item is not None:
            found[prop] = item["value"]
    return found


def filtered_dir(obj: Any) -> list[str]:
    names = []
    try:
        names = dir(obj)
    except Exception:
        return []
    return sorted(
        name
        for name in names
        if any(keyword in name.lower() for keyword in KEYWORDS)
    )[:300]


def class_introspection(obj: Any) -> dict[str, Any]:
    out: dict[str, Any] = {}
    try:
        cls = obj.get_class()
        out["class_path"] = path_name(cls)
        out["class_dir_filtered"] = filtered_dir(cls)
        for method_name in ("get_properties", "get_fields", "properties"):
            try:
                method = getattr(cls, method_name)
                value = method() if callable(method) else method
                out[method_name] = jsonable(value)
            except Exception as exc:
                out[f"{method_name}_error"] = f"{type(exc).__name__}: {exc}"
    except Exception as exc:
        out["error"] = f"{type(exc).__name__}: {exc}"
    return out


def actor_summary(actor: Any) -> dict[str, Any]:
    item: dict[str, Any] = {
        "label": label(actor),
        "class": class_name(actor),
        "path": path_name(actor),
        "properties": read_property_candidates(actor),
        "dir_filtered": filtered_dir(actor),
        "class_introspection": class_introspection(actor),
    }
    try:
        item["location"] = jsonable(actor.get_actor_location())
    except Exception:
        pass
    try:
        cdo = unreal.get_default_object(actor.get_class())
        item["class_default_object"] = {
            "path": path_name(cdo),
            "properties": read_property_candidates(cdo),
            "dir_filtered": filtered_dir(cdo),
        }
    except Exception as exc:
        item["class_default_object_error"] = f"{type(exc).__name__}: {exc}"
    return item


def data_table_probe() -> dict[str, Any]:
    out: dict[str, Any] = {"asset_path": DATA_TABLE_ASSET}
    asset = unreal.EditorAssetLibrary.load_asset(DATA_TABLE_ASSET)
    out["loaded"] = bool(asset)
    if not asset:
        return out
    out["object_path"] = path_name(asset)
    out["class"] = class_name(asset)
    try:
        out["row_struct"] = path_name(asset.get_editor_property("row_struct"))
    except Exception as exc:
        out["row_struct_error"] = f"{type(exc).__name__}: {exc}"
    try:
        rows = [str(row) for row in unreal.DataTableFunctionLibrary.get_data_table_row_names(asset)]
        row_set = set(rows)
        out["row_count"] = len(rows)
        out["sample_rows_present"] = {
            row: row in row_set
            for row in ("0", "1", "2", "3501", "4001", "4110", "7921")
        }
        out["tail_rows"] = rows[-25:]
    except Exception as exc:
        out["row_error"] = f"{type(exc).__name__}: {exc}"
    return out


def inspect_level() -> dict[str, Any]:
    out: dict[str, Any] = {"map_asset_path": MAP_ASSET_PATH}
    load = None
    try:
        load = unreal.EditorLoadingAndSavingUtils.load_map(MAP_ASSET_PATH)
        out["load_map"] = jsonable(load)
    except Exception as exc:
        out["load_error"] = f"{type(exc).__name__}: {exc}"
        return out
    actors = list(unreal.EditorLevelLibrary.get_all_level_actors())
    out["actor_count"] = len(actors)
    out["class_counts_top"] = dict(Counter(class_name(actor) for actor in actors).most_common(40))

    body_rows = []
    focus_rows = []
    for actor in actors:
        cls = class_name(actor)
        name_text = f"{label(actor)} {cls}".lower()
        if "starsystembody" in name_text:
            body_rows.append(
                {
                    "label": label(actor),
                    "class": cls,
                    "path": path_name(actor),
                    "star_system_id": jsonable(
                        actor.get_editor_property("star_system_id")
                    )
                    if read_property(actor, "star_system_id") is not None
                    else None,
                    "properties": read_property_candidates(actor),
                    "dir_filtered": filtered_dir(actor),
                }
            )
        elif any(term in name_text for term in ("starmap", "starsystemscene", "scene", "camera")):
            focus_rows.append(actor_summary(actor))

    ids = [
        row["star_system_id"]
        for row in body_rows
        if isinstance(row.get("star_system_id"), int)
    ]
    out["star_system_body_count"] = len(body_rows)
    out["star_system_body_id_range"] = {
        "min": min(ids) if ids else None,
        "max": max(ids) if ids else None,
    }
    out["star_system_body_samples"] = body_rows[:15]
    out["star_system_body_tail_samples"] = body_rows[-15:]
    out["focus_actors"] = focus_rows
    try:
        world = unreal.EditorLevelLibrary.get_editor_world()
        out["world_path"] = path_name(world)
        out["world_outer"] = path_name(world.get_outer())
    except Exception as exc:
        out["world_error"] = f"{type(exc).__name__}: {exc}"
    return out


def decode_fib(value: str) -> str:
    chars = []
    for ch in value:
        code = ord(ch)
        chars.append(chr(code - 1) if code > 1 else ch)
    return "".join(chars)


def blueprint_fib(asset_path: str) -> dict[str, Any]:
    out: dict[str, Any] = {"asset_path": asset_path}
    try:
        tags = unreal.EditorAssetLibrary.get_tag_values(asset_path)
        fib = str(tags.get("FiBData", ""))
    except Exception as exc:
        out["error"] = f"{type(exc).__name__}: {exc}"
        return out
    decoded = decode_fib(fib) if fib else ""
    tokens = re.findall(r"[A-Za-z0-9_./:'\[\]\(\)# -]{3,}", decoded)
    focused = []
    seen = set()
    for token in tokens:
        clean = " ".join(token.split())
        if clean in seen:
            continue
        if any(keyword in clean.lower() for keyword in KEYWORDS):
            focused.append(clean)
            seen.add(clean)
        if len(focused) >= 500:
            break
    out["fib_raw_length"] = len(fib)
    out["focused_tokens"] = focused
    return out


def decision(report: dict[str, Any]) -> dict[str, Any]:
    level = report.get("level", {})
    table = report.get("data_table", {})
    findings = []
    if table.get("row_count") == 3974:
        findings.append("Editor DataTable override resolves with the merged TKU row count.")
    if level.get("star_system_body_count") == 3973:
        findings.append("Editor StarMap override resolves with the merged TKU StarSystemBody actor count.")
    for actor in level.get("focus_actors", []):
        if actor.get("class") == "StarMapActor_C":
            props = actor.get("properties", {})
            for prop_name, value in props.items():
                if "look" in prop_name.lower() or "inner" in prop_name.lower() or "generate" in prop_name.lower():
                    findings.append(f"StarMapActor property `{prop_name}` resolved as `{value}`.")
    return {"findings": findings}


def write_markdown(report: dict[str, Any]) -> None:
    lines = [
        "# UE4 StarMap Binding Probe - 2026-05-12",
        "",
        f"- Generated: `{report['generated_utc']}`",
        f"- Target mod: `{TARGET_MOD_NAME}`",
        f"- Map: `{MAP_ASSET_PATH}`",
        "- Safety: read-only commandlet; no assets saved.",
        "",
        "## Decision",
        "",
    ]
    for item in report.get("decision", {}).get("findings", []):
        lines.append(f"- {item}")
    level = report.get("level", {})
    table = report.get("data_table", {})
    lines.extend(
        [
            "",
            "## Counts",
            "",
            f"- DataTable object path: `{table.get('object_path')}`",
            f"- DataTable rows: `{table.get('row_count')}`",
            f"- DataTable sample rows present: `{table.get('sample_rows_present')}`",
            f"- World path: `{level.get('world_path')}`",
            f"- StarSystemBody actors: `{level.get('star_system_body_count')}`",
            f"- StarSystemBody id range: `{level.get('star_system_body_id_range')}`",
            "",
            "## Focus Actors",
            "",
        ]
    )
    for actor in level.get("focus_actors", []):
        lines.append(f"### `{actor.get('label')}` `{actor.get('class')}`")
        lines.append(f"- path: `{actor.get('path')}`")
        props = actor.get("properties", {})
        if props:
            lines.append("- matched properties:")
            for key, value in props.items():
                lines.append(f"- `{key}` = `{value}`")
        cdo = actor.get("class_default_object", {})
        cdo_props = cdo.get("properties", {})
        if cdo_props:
            lines.append("- CDO matched properties:")
            for key, value in cdo_props.items():
                lines.append(f"- `{key}` = `{value}`")
        dir_filtered = actor.get("dir_filtered", [])
        if dir_filtered:
            lines.append(f"- filtered dir sample: `{dir_filtered[:80]}`")
        lines.append("")
    lines.extend(["## Blueprint Token Focus", ""])
    for path, fib in report.get("blueprint_fib", {}).items():
        lines.append(f"### `{path}`")
        for token in fib.get("focused_tokens", [])[:120]:
            lines.append(f"- `{token}`")
        lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "target_mod_name": TARGET_MOD_NAME,
        "map_asset_path": MAP_ASSET_PATH,
        "data_table": {},
        "level": {},
        "blueprint_fib": {},
        "errors": [],
    }
    try:
        report["data_table"] = data_table_probe()
    except Exception:
        report["errors"].append({"data_table": traceback.format_exc()})
    try:
        report["level"] = inspect_level()
    except Exception:
        report["errors"].append({"level": traceback.format_exc()})
    for asset_path in (
        "/Game/UI/FrontEnd/Starmap/StarMapActor",
        "/Game/UI/FrontEnd/Starmap/StarSystemBody",
        "/Game/Levels/FrontEnd/StarMapSceneManager",
        "/Game/Levels/FrontEnd/StarSystemSceneManager",
        "/Game/InnerSphereData/StarSystemGenerator",
        "/Game/InnerSphereData/StarMapBP_UTILS",
    ):
        try:
            report["blueprint_fib"][asset_path] = blueprint_fib(asset_path)
        except Exception:
            report["errors"].append({asset_path: traceback.format_exc()})
    report["decision"] = decision(report)
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True, default=str), encoding="utf-8")
    write_markdown(report)
    unreal.log(f"TKU StarMap binding probe wrote {OUT_JSON}")


main()
