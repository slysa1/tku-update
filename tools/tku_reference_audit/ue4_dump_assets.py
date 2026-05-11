from __future__ import annotations

from collections import Counter
import json
import traceback
from pathlib import Path

import unreal

from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
OUT_DIR = REPORTS_DIR / "tku_editor_first"
OUT_JSON = OUT_DIR / "ue4_editor_asset_dump.json"
OUT_MD = OUT_DIR / "ue4_editor_asset_dump.md"

SOURCE_NOTE = (
    "Editor dump of the MW5 Mod Editor project. TKU comparisons should use "
    "the restored Nexus build-38 live folder at MW5Mercs/Mods/TheKnownUniverse. "
    "Quarantined blind-build artifacts are not source evidence."
)

FOCUS_ASSET_PATHS = [
    "/Game/Levels/FrontEnd/StarMap",
    "/Game/Levels/FrontEnd/StarMapSceneManager",
    "/Game/UI/FrontEnd/Starmap/StarMapActor",
    "/Game/UI/FrontEnd/StarMapPawn",
    "/Game/UI/FrontEnd/Starmap/StarSystemBody",
    "/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor",
    "/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges",
    "/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015",
    "/Game/InnerSphereData/MW5_InnerSphereData",
    "/Game/InnerSphereData/Updated/EmployerInfoData",
    "/Game/InnerSphereData/Updated/SystemFactionChanges",
    "/Game/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL",
    "/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL",
    "/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF",
    "/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets",
]

LEVEL_ASSET_PATHS = {
    "/Game/Levels/FrontEnd/StarMap",
}

DISCOVERY_DIRS = [
    "/Game/Campaign/CampaignArcs/BorderChanges",
    "/Game/Campaign/Clusters",
    "/Game/UI/Editor/Utils",
    "/Game/UI/FrontEnd/Starmap",
]

PROPERTY_CANDIDATES = [
    "PanBoundsHorizontal",
    "pan_bounds_horizontal",
    "PanBoundsVertical",
    "pan_bounds_vertical",
    "ZoomDistanceList",
    "zoom_distance_list",
    "ZoomLevelThresholds",
    "zoom_level_thresholds",
    "StarMapActor",
    "star_map_actor",
    "StarSystemBody",
    "star_system_body",
    "StarMapCamera",
    "star_map_camera",
    "InitialCameraTransform",
    "initial_camera_transform",
    "Faction",
    "faction",
    "FactionChange",
    "faction_change",
    "BorderChanges",
    "border_changes",
    "StarMapBorders",
    "star_map_borders",
    "Material",
    "material",
    "RowStruct",
    "row_struct",
    "StartDate",
    "start_date",
    "EndDate",
    "end_date",
    "BorderActor",
    "border_actor",
    "ClusterFactionAsset",
    "cluster_faction_asset",
    "ClusterOverlay",
    "cluster_overlay",
    "ClusterConstellation",
    "cluster_constellation",
    "SystemIds",
    "system_ids",
    "IsLegacyCluster",
    "is_legacy_cluster",
    "ToiData",
    "toi_data",
]

TAG_CANDIDATES = [
    "GeneratedClass",
    "ParentClass",
    "NativeParentClass",
    "BlueprintType",
    "ClassFlags",
    "RowStructure",
    "NumRows",
]

FOCUS_LEVEL_CLASSES = {
    "CameraActor",
    "StarMapActor_C",
    "StarMapSceneManager_C",
    "StarSystemSceneManager_C",
    "StarSystem_C",
    "StarSystemBody_C",
}


def normalize_asset_path(asset_path: str) -> str:
    path = text(asset_path)
    last_slash = path.rfind("/")
    dot = path.find(".", last_slash + 1)
    if dot != -1:
        return path[:dot]
    return path


def text(value) -> str:
    try:
        return str(value)
    except Exception:
        return repr(value)


def plain(value, max_items: int = 80):
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if hasattr(value, "x") and hasattr(value, "y") and hasattr(value, "z"):
        return {"x": value.x, "y": value.y, "z": value.z}
    if hasattr(value, "roll") and hasattr(value, "pitch") and hasattr(value, "yaw"):
        return {"roll": value.roll, "pitch": value.pitch, "yaw": value.yaw}
    try:
        return {text(k): plain(v, max_items=max_items) for k, v in value.items()}
    except Exception:
        pass
    if not isinstance(value, (str, bytes)):
        try:
            out = []
            for index, item in enumerate(value):
                if index >= max_items:
                    out.append("... truncated ...")
                    break
                out.append(plain(item, max_items=max_items))
            return out
        except Exception:
            pass
    return text(value)


def clipped(value, limit: int = 1000) -> str:
    value_text = text(value)
    if len(value_text) > limit:
        return value_text[:limit] + "... truncated ..."
    return value_text


def get_path_name(obj) -> str:
    try:
        return text(obj.get_path_name())
    except Exception:
        return text(obj)


def get_class_name(obj) -> str:
    try:
        return text(obj.get_class().get_name())
    except Exception:
        return ""


def make_dependency_options():
    return unreal.AssetRegistryDependencyOptions(
        True,   # include_soft_package_references
        True,   # include_hard_package_references
        True,   # include_searchable_names
        True,   # include_soft_management_references
        True,   # include_hard_management_references
    )


def get_dependencies(asset_registry, package_name: str) -> dict:
    deps = {}
    options = make_dependency_options()
    for method_name in ("get_dependencies", "get_referencers"):
        try:
            method = getattr(asset_registry, method_name)
            value = method(package_name, options)
            deps[method_name] = sorted(text(item) for item in (value or []))
        except Exception as exc:
            deps[method_name] = {"error": f"{type(exc).__name__}: {exc}"}
    return deps


def get_known_properties(obj) -> dict:
    out = {}
    for prop in PROPERTY_CANDIDATES:
        try:
            value = obj.get_editor_property(prop)
        except Exception:
            continue
        out[prop] = plain(value)
    return out


def get_asset_tags(asset_path: str) -> dict:
    out = {"all": {}, "all_keys": [], "selected": {}}
    try:
        raw_tags = unreal.EditorAssetLibrary.get_tag_values(asset_path)
        out["all"] = {text(k): clipped(v) for k, v in raw_tags.items()}
        out["all_keys"] = sorted(out["all"])
    except Exception as exc:
        out["all_error"] = f"{type(exc).__name__}: {exc}"
    try:
        data = unreal.EditorAssetLibrary.find_asset_data(asset_path)
        for tag in TAG_CANDIDATES:
            try:
                value = data.get_tag_value(tag)
            except Exception:
                continue
            if value not in (None, ""):
                out["selected"][tag] = text(value)
    except Exception as exc:
        out["selected_error"] = f"{type(exc).__name__}: {exc}"
    return out


def get_asset_data_info(asset_path: str) -> dict:
    try:
        data = unreal.EditorAssetLibrary.find_asset_data(asset_path)
        return {
            "is_valid": bool(data.is_valid()),
            "is_u_asset": bool(data.is_u_asset()),
            "is_redirector": bool(data.is_redirector()),
            "is_asset_loaded": bool(data.is_asset_loaded()),
            "asset_class": text(data.asset_class),
            "asset_name": text(data.asset_name),
            "object_path": text(data.object_path),
            "package_name": text(data.package_name),
            "package_path": text(data.package_path),
            "full_name": text(data.get_full_name()),
            "export_text_name": text(data.get_export_text_name()),
        }
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}


def get_blueprint_info(asset_path: str) -> dict:
    out = {}
    try:
        bp_class = unreal.EditorAssetLibrary.load_blueprint_class(asset_path)
    except Exception as exc:
        out["load_blueprint_class_error"] = f"{type(exc).__name__}: {exc}"
        return out
    if not bp_class:
        out["load_blueprint_class"] = None
        return out
    out["class_name"] = text(bp_class.get_name())
    out["class_path"] = get_path_name(bp_class)
    out["class_text"] = text(bp_class)
    try:
        cdo = unreal.get_default_object(bp_class)
        out["default_object_path"] = get_path_name(cdo)
        out["default_object_class"] = get_class_name(cdo)
        out["default_object_known_properties"] = get_known_properties(cdo)
    except Exception as exc:
        out["default_object_error"] = f"{type(exc).__name__}: {exc}"
    return out


def get_data_table_info(asset) -> dict:
    out = {}
    try:
        rows = [text(row) for row in unreal.DataTableFunctionLibrary.get_data_table_row_names(asset)]
        out["row_count"] = len(rows)
        out["sample_rows"] = rows[:40]
    except Exception as exc:
        out["row_error"] = f"{type(exc).__name__}: {exc}"
    try:
        row_struct = asset.get_editor_property("row_struct")
        out["row_struct"] = get_path_name(row_struct)
    except Exception:
        pass
    return out


def inspect_asset(asset_registry, asset_path: str) -> dict:
    asset_path = normalize_asset_path(asset_path)
    if asset_path in LEVEL_ASSET_PATHS:
        return {
            "asset_path": asset_path,
            "exists": True,
            "asset_data": {
                "asset_class": "World",
                "package_name": asset_path,
                "note": "Level asset inspected through EditorLevelLibrary to avoid EditorAssetLibrary map errors.",
            },
            "tags": {"all": {}, "all_keys": [], "selected": {}},
            "dependencies": get_dependencies(asset_registry, asset_path),
            "load_skipped": "EditorAssetLibrary.load_asset/find_asset_data does not support level assets.",
        }
    item = {
        "asset_path": asset_path,
        "asset_data": get_asset_data_info(asset_path),
        "tags": get_asset_tags(asset_path),
        "dependencies": get_dependencies(asset_registry, asset_path),
    }
    try:
        item["exists"] = bool(unreal.EditorAssetLibrary.does_asset_exist(asset_path))
    except Exception as exc:
        item["exists"] = False
        item["exists_error"] = f"{type(exc).__name__}: {exc}"
    if not item["exists"]:
        return item

    asset_class = str(item.get("asset_data", {}).get("asset_class", ""))
    if asset_class in {"World", "MapBuildDataRegistry"}:
        item["load_skipped"] = "EditorAssetLibrary.load_asset does not support level assets."
        return item

    try:
        asset = unreal.EditorAssetLibrary.load_asset(asset_path)
    except Exception as exc:
        item["load_error"] = f"{type(exc).__name__}: {exc}"
        asset = None
    item["loaded"] = asset is not None
    if asset is None:
        return item

    item["object_path"] = get_path_name(asset)
    item["class"] = get_class_name(asset)
    item["known_properties"] = get_known_properties(asset)

    class_name = item["class"].lower()
    if "blueprint" in class_name:
        item["blueprint"] = get_blueprint_info(asset_path)
    if item["class"] == "DataTable":
        item["data_table"] = get_data_table_info(asset)
    return item


def discover_assets() -> dict:
    discovered = {"directories": {}, "asset_paths": []}
    seen = set(FOCUS_ASSET_PATHS)
    for directory in DISCOVERY_DIRS:
        try:
            assets = [
                normalize_asset_path(path)
                for path in unreal.EditorAssetLibrary.list_assets(directory, True, False)
            ]
        except Exception as exc:
            discovered["directories"][directory] = {"error": f"{type(exc).__name__}: {exc}"}
            continue
        assets = sorted(set(assets))
        discovered["directories"][directory] = {
            "asset_count": len(assets),
            "sample_assets": assets[:60],
        }
        for asset_path in assets:
            if asset_path not in seen:
                seen.add(asset_path)
                discovered["asset_paths"].append(asset_path)
    return discovered


def summarize_points(points: list[dict]) -> dict:
    if not points:
        return {"count": 0}
    xs = [point["x"] for point in points]
    ys = [point["y"] for point in points]
    zs = [point["z"] for point in points]
    mean_x = sum(xs) / len(xs)
    mean_y = sum(ys) / len(ys)
    mean_z = sum(zs) / len(zs)
    return {
        "count": len(points),
        "min_x": min(xs),
        "max_x": max(xs),
        "span_x": max(xs) - min(xs),
        "mean_x": mean_x,
        "min_y": min(ys),
        "max_y": max(ys),
        "span_y": max(ys) - min(ys),
        "mean_y": mean_y,
        "min_z": min(zs),
        "max_z": max(zs),
        "span_z": max(zs) - min(zs),
        "mean_z": mean_z,
    }


def actor_info(actor) -> dict:
    info = {
        "label": text(actor.get_actor_label()),
        "class": get_class_name(actor),
        "path": get_path_name(actor),
    }
    try:
        loc = actor.get_actor_location()
        info["location"] = plain(loc)
    except Exception:
        pass
    props = get_known_properties(actor)
    if props:
        info["known_properties"] = props
    return info


def inspect_level() -> dict:
    out = {"level_path": "/Game/Levels/FrontEnd/StarMap"}
    try:
        loaded = unreal.EditorLevelLibrary.load_level(out["level_path"])
        out["loaded"] = bool(loaded)
    except Exception as exc:
        out["loaded"] = False
        out["load_error"] = f"{type(exc).__name__}: {exc}"
        return out
    try:
        actors = unreal.EditorLevelLibrary.get_all_level_actors()
        out["actor_count"] = len(actors)
        class_counts = Counter()
        star_system_points = []
        out["focus_actors"] = []
        out["actors"] = []
        class_defaults = {}
        for actor in actors:
            info = actor_info(actor)
            class_name = info.get("class", "")
            class_counts[class_name] += 1
            if class_name == "StarSystemBody_C" and isinstance(info.get("location"), dict):
                star_system_points.append(info["location"])
            if class_name in FOCUS_LEVEL_CLASSES or "StarMap" in info.get("label", ""):
                out["focus_actors"].append(info)
            out["actors"].append(info)
            if class_name in FOCUS_LEVEL_CLASSES and class_name not in class_defaults:
                try:
                    cdo = unreal.get_default_object(actor.get_class())
                    class_defaults[class_name] = {
                        "default_object_path": get_path_name(cdo),
                        "default_object_class": get_class_name(cdo),
                        "default_object_known_properties": get_known_properties(cdo),
                    }
                except Exception as exc:
                    class_defaults[class_name] = {"error": f"{type(exc).__name__}: {exc}"}
        out["class_counts"] = dict(class_counts.most_common())
        out["star_system_body_bounds"] = summarize_points(star_system_points)
        out["focus_class_default_objects"] = class_defaults
    except Exception as exc:
        out["actor_error"] = f"{type(exc).__name__}: {exc}"
    try:
        world = unreal.EditorLevelLibrary.get_editor_world()
        out["world"] = get_path_name(world)
        settings = world.get_world_settings()
        out["world_settings_class"] = get_class_name(settings)
        out["world_settings_path"] = get_path_name(settings)
    except Exception as exc:
        out["world_error"] = f"{type(exc).__name__}: {exc}"
    return out


def append_dependency_summary(lines: list[str], asset: dict) -> None:
    deps = asset.get("dependencies", {})
    for key, value in deps.items():
        if isinstance(value, list):
            lines.append(f"- `{key}` count: {len(value)}")
            for dep in value[:25]:
                lines.append(f"- `{dep}`")
        elif isinstance(value, dict):
            lines.append(f"- `{key}`: `{value}`")


def write_asset_details(lines: list[str], asset: dict) -> None:
    lines.append(f"### `{asset['asset_path']}`")
    lines.append("")
    asset_data = asset.get("asset_data", {})
    lines.append(f"- exists: `{asset.get('exists')}`")
    lines.append(f"- asset_class: `{asset_data.get('asset_class', '')}`")
    if asset.get("class"):
        lines.append(f"- loaded class: `{asset.get('class')}`")
    if asset.get("load_skipped"):
        lines.append(f"- load skipped: {asset['load_skipped']}")
    tags = asset.get("tags", {}).get("selected", {})
    if tags:
        lines.append("- selected tags:")
        for key, value in tags.items():
            lines.append(f"- `{key}` = `{value}`")
    table = asset.get("data_table")
    if table:
        lines.append(f"- data table rows: `{table.get('row_count')}`")
        if table.get("row_struct"):
            lines.append(f"- row_struct: `{table.get('row_struct')}`")
        for row in table.get("sample_rows", [])[:20]:
            lines.append(f"- sample row `{row}`")
    props = asset.get("known_properties")
    if props:
        lines.append("- known properties:")
        for key, value in props.items():
            lines.append(f"- `{key}` = `{value}`")
    bp = asset.get("blueprint")
    if bp:
        lines.append("- blueprint:")
        for key in ("class_name", "class_path", "default_object_class", "default_object_path"):
            if key in bp:
                lines.append(f"- `{key}` = `{bp[key]}`")
        props = bp.get("default_object_known_properties")
        if props:
            lines.append("- default object known properties:")
            for key, value in props.items():
                lines.append(f"- `{key}` = `{value}`")
    append_dependency_summary(lines, asset)
    lines.append("")


def write_markdown(report: dict) -> None:
    lines = [
        "# UE4 Editor Asset Dump",
        "",
        SOURCE_NOTE,
        "",
        "## Discovery",
        "",
    ]
    for directory, info in report.get("discovered", {}).get("directories", {}).items():
        lines.append(f"- `{directory}` asset_count: `{info.get('asset_count', 'error')}`")
        if info.get("error"):
            lines.append(f"- `{directory}` error: `{info['error']}`")
    lines.extend(["", "## Focus Assets", ""])

    assets_by_path = {asset["asset_path"]: asset for asset in report["assets"]}
    for asset_path in FOCUS_ASSET_PATHS:
        asset = assets_by_path.get(asset_path)
        if asset:
            write_asset_details(lines, asset)

    border_assets = [
        asset for asset in report["assets"]
        if asset["asset_path"].startswith("/Game/Campaign/CampaignArcs/BorderChanges/")
        and asset["asset_path"] not in set(FOCUS_ASSET_PATHS)
    ]
    if border_assets:
        lines.extend(["## Border Asset Summary", ""])
        for asset in border_assets:
            deps = asset.get("dependencies", {}).get("get_dependencies", [])
            refs = asset.get("dependencies", {}).get("get_referencers", [])
            lines.append(
                f"- `{asset['asset_path']}` class "
                f"`{asset.get('asset_data', {}).get('asset_class', '')}` "
                f"deps `{len(deps) if isinstance(deps, list) else 'error'}` "
                f"refs `{len(refs) if isinstance(refs, list) else 'error'}`"
            )
        lines.append("")

    cluster_assets = [
        asset for asset in report["assets"]
        if asset["asset_path"].startswith("/Game/Campaign/Clusters/")
    ]
    if cluster_assets:
        lines.extend(["## Cluster Asset Summary", ""])
        for asset in cluster_assets:
            props = asset.get("known_properties", {})
            system_ids = props.get("system_ids", props.get("SystemIds", []))
            system_count = len(system_ids) if isinstance(system_ids, list) else ""
            faction = props.get("cluster_faction_asset", props.get("ClusterFactionAsset", ""))
            overlay = props.get("cluster_overlay", props.get("ClusterOverlay", ""))
            constellation = props.get("cluster_constellation", props.get("ClusterConstellation", ""))
            lines.append(
                f"- `{asset['asset_path']}` class "
                f"`{asset.get('asset_data', {}).get('asset_class', '')}` "
                f"systems `{system_count}` faction `{faction}` "
                f"overlay `{overlay}` constellation `{constellation}`"
            )
        lines.append("")

    level = report.get("level", {})
    lines.extend(["## StarMap Level", ""])
    lines.append(f"- loaded: `{level.get('loaded')}`")
    lines.append(f"- actor_count: `{level.get('actor_count', '')}`")
    bounds = level.get("star_system_body_bounds", {})
    if bounds:
        lines.append(
            "- StarSystemBody bounds: "
            f"count `{bounds.get('count')}`, "
            f"x `{bounds.get('min_x')}`..`{bounds.get('max_x')}` "
            f"(span `{bounds.get('span_x')}`), "
            f"y `{bounds.get('min_y')}`..`{bounds.get('max_y')}` "
            f"(span `{bounds.get('span_y')}`)"
        )
    class_counts = level.get("class_counts", {})
    if class_counts:
        lines.append("- top actor classes:")
        for class_name, count in list(class_counts.items())[:25]:
            lines.append(f"- `{class_name}` = `{count}`")
    defaults = level.get("focus_class_default_objects", {})
    if defaults:
        lines.append("- focus class default objects:")
        for class_name, info in defaults.items():
            lines.append(f"- `{class_name}` CDO `{info.get('default_object_path', info.get('error', ''))}`")
            for key, value in info.get("default_object_known_properties", {}).items():
                lines.append(f"- `{class_name}.{key}` = `{value}`")
    lines.append("- focus actors:")
    for actor in level.get("focus_actors", [])[:80]:
        lines.append(
            f"- `{actor.get('label')}` class `{actor.get('class')}` "
            f"path `{actor.get('path')}` loc `{actor.get('location', '')}`"
        )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    report = {
        "source_note": SOURCE_NOTE,
        "focus_asset_paths": FOCUS_ASSET_PATHS,
        "discovery_dirs": DISCOVERY_DIRS,
        "assets": [],
        "level": {},
        "errors": [],
    }
    try:
        asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()
        discovered = discover_assets()
        report["discovered"] = discovered
        asset_paths = sorted(set(FOCUS_ASSET_PATHS + discovered.get("asset_paths", [])))
        report["asset_paths"] = asset_paths
        for asset_path in asset_paths:
            report["assets"].append(inspect_asset(asset_registry, asset_path))
        report["level"] = inspect_level()
    except Exception:
        report["errors"].append(traceback.format_exc())
    OUT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")
    write_markdown(report)
    unreal.log("TKU editor asset dump written to {}".format(OUT_JSON))


main()
