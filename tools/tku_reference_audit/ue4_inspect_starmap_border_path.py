from __future__ import annotations

from collections import Counter
import json
import traceback
from pathlib import Path

import unreal


from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
OUT_DIR = REPORTS_DIR / "tku_editor_first"
OUT_JSON = OUT_DIR / "ue4_starmap_border_path_inspection.json"
OUT_MD = OUT_DIR / "ue4_starmap_border_path_inspection.md"

FOCUS_ASSETS = [
    "/Game/Campaign/Dialogue/HoloTable/StarMapActor_2570",
    "/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor",
    "/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015",
    "/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/StarMapBorderActor3015",
    "/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges",
    "/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction",
    "/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets",
    "/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction",
    "/Game/Campaign/Clusters/Steiner-KuritaBorder/Steiner-KuritaBorder_ClusterAsset",
    "/Game/Campaign/Clusters/Taurian/Taurian_ClusterAsset",
    "/Game/Campaign/Clusters/OutworldsAlliance/OutworldsAlliance_ClusterAsset",
    "/Game/Campaign/Clusters/IndustrialHub_1/IndustrialHub_1_ClusterAsset",
    "/Game/UI/FrontEnd/StarMapPawn",
    "/Game/UI/FrontEnd/Starmap/StarMapActor",
    "/Game/UI/FrontEnd/Starmap/StarSystemBody",
]

DISCOVERY_DIRS = [
    "/Game/Campaign/CampaignArcs/BorderChanges",
    "/Game/Campaign/Dialogue/HoloTable",
    "/Game/Campaign/Clusters",
]

PROPERTY_CANDIDATES = [
    "BorderActor",
    "border_actor",
    "BorderAsset",
    "border_asset",
    "BorderChanges",
    "border_changes",
    "StarMapBorders",
    "star_map_borders",
    "CampaignArcEventList",
    "campaign_arc_event_list",
    "CampaignArcEvents",
    "campaign_arc_events",
    "Actions",
    "actions",
    "Action",
    "action",
    "Config",
    "config",
    "PlaceClusterToi_Config",
    "place_cluster_toi_config",
    "ClusterDataAsset",
    "cluster_data_asset",
    "ClusterDataAssetId",
    "cluster_data_asset_id",
    "ClusterFactionAsset",
    "cluster_faction_asset",
    "ClusterOverlay",
    "cluster_overlay",
    "ClusterConstellation",
    "cluster_constellation",
    "SystemIds",
    "system_ids",
    "SystemID",
    "system_id",
    "SystemName",
    "system_name",
    "Faction",
    "faction",
    "Employer",
    "employer",
    "StartDate",
    "start_date",
    "EndDate",
    "end_date",
    "PanBoundsHorizontal",
    "pan_bounds_horizontal",
    "PanBoundsVertical",
    "pan_bounds_vertical",
    "ZoomDistanceList",
    "zoom_distance_list",
    "ZoomLevelThresholds",
    "zoom_level_thresholds",
    "StarMapCamera",
    "star_map_camera",
    "InitialCameraTransform",
    "initial_camera_transform",
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


def text(value) -> str:
    try:
        return str(value)
    except Exception:
        return repr(value)


def plain(value, max_items: int = 120):
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


def clipped(value, limit: int = 1200) -> str:
    value_text = text(value)
    if len(value_text) > limit:
        return value_text[:limit] + "... truncated ..."
    return value_text


def normalize_asset_path(asset_path: str) -> str:
    path = text(asset_path)
    last_slash = path.rfind("/")
    dot = path.find(".", last_slash + 1)
    if dot != -1:
        return path[:dot]
    return path


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


def dependency_options():
    return unreal.AssetRegistryDependencyOptions(True, True, True, True, True)


def asset_registry_refs(asset_registry, package_name: str) -> dict:
    out = {}
    opts = dependency_options()
    for method_name in ("get_dependencies", "get_referencers"):
        try:
            value = getattr(asset_registry, method_name)(package_name, opts)
            out[method_name] = sorted(text(item) for item in (value or []))
        except Exception as exc:
            out[method_name] = {"error": f"{type(exc).__name__}: {exc}"}
    return out


def asset_data(asset_path: str) -> dict:
    try:
        data = unreal.EditorAssetLibrary.find_asset_data(asset_path)
        return {
            "is_valid": bool(data.is_valid()),
            "asset_class": text(data.asset_class),
            "asset_name": text(data.asset_name),
            "package_name": text(data.package_name),
            "package_path": text(data.package_path),
            "object_path": text(data.object_path),
            "full_name": text(data.get_full_name()),
            "export_text_name": text(data.get_export_text_name()),
        }
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}


def selected_tags(asset_path: str) -> dict:
    tags = {"all_keys": [], "selected": {}, "all": {}}
    try:
        raw = unreal.EditorAssetLibrary.get_tag_values(asset_path)
        tags["all"] = {text(k): clipped(v) for k, v in raw.items()}
        tags["all_keys"] = sorted(tags["all"])
    except Exception as exc:
        tags["all_error"] = f"{type(exc).__name__}: {exc}"
    try:
        data = unreal.EditorAssetLibrary.find_asset_data(asset_path)
        for tag in TAG_CANDIDATES:
            value = data.get_tag_value(tag)
            if value not in (None, ""):
                tags["selected"][tag] = text(value)
    except Exception as exc:
        tags["selected_error"] = f"{type(exc).__name__}: {exc}"
    return tags


def get_known_properties(obj) -> dict:
    props = {}
    for prop in PROPERTY_CANDIDATES:
        try:
            value = obj.get_editor_property(prop)
        except Exception:
            continue
        props[prop] = plain(value)
    return props


def class_chain(bp_class) -> list[str]:
    out = []
    current = bp_class
    for _ in range(16):
        if not current:
            break
        out.append(get_path_name(current))
        try:
            current = current.get_super_class()
        except Exception:
            break
    return out


def blueprint_info(asset_path: str) -> dict:
    info = {}
    try:
        bp_class = unreal.EditorAssetLibrary.load_blueprint_class(asset_path)
    except Exception as exc:
        info["load_blueprint_class_error"] = f"{type(exc).__name__}: {exc}"
        return info
    if not bp_class:
        info["load_blueprint_class"] = None
        return info
    info["class_name"] = text(bp_class.get_name())
    info["class_path"] = get_path_name(bp_class)
    info["class_chain"] = class_chain(bp_class)
    try:
        cdo = unreal.get_default_object(bp_class)
        info["default_object_path"] = get_path_name(cdo)
        info["default_object_class"] = get_class_name(cdo)
        info["default_object_known_properties"] = get_known_properties(cdo)
    except Exception as exc:
        info["default_object_error"] = f"{type(exc).__name__}: {exc}"
    return info


def inspect_asset(asset_registry, asset_path: str) -> dict:
    asset_path = normalize_asset_path(asset_path)
    item = {
        "asset_path": asset_path,
        "references": asset_registry_refs(asset_registry, asset_path),
    }
    try:
        item["exists"] = bool(unreal.EditorAssetLibrary.does_asset_exist(asset_path))
    except Exception as exc:
        item["exists"] = False
        item["exists_error"] = f"{type(exc).__name__}: {exc}"
    if not item["exists"]:
        item["asset_data"] = {"asset_class": None}
        item["tags"] = {"all_keys": [], "selected": {}, "all": {}}
        return item
    item["asset_data"] = asset_data(asset_path)
    item["tags"] = selected_tags(asset_path)
    try:
        asset = unreal.EditorAssetLibrary.load_asset(asset_path)
    except Exception as exc:
        item["load_error"] = f"{type(exc).__name__}: {exc}"
        asset = None
    item["loaded"] = asset is not None
    if asset is None:
        return item
    item["loaded_class"] = get_class_name(asset)
    item["known_properties"] = get_known_properties(asset)
    if item["asset_data"].get("asset_class") == "Blueprint" or item["loaded_class"] == "Blueprint":
        item["blueprint"] = blueprint_info(asset_path)
    return item


def discover_asset_paths() -> list[str]:
    seen = set(FOCUS_ASSETS)
    for directory in DISCOVERY_DIRS:
        try:
            paths = unreal.EditorAssetLibrary.list_assets(directory, True, False)
        except Exception:
            continue
        for path in paths:
            path = normalize_asset_path(path)
            name = path.rsplit("/", 1)[-1]
            if (
                "StarMapBorderActor" in name
                or "Borders" in name
                or "StarMapActor_2570" in name
                or path in FOCUS_ASSETS
            ):
                seen.add(path)
    return sorted(seen)


def summarize_assets(assets: list[dict]) -> dict:
    class_counts = Counter()
    parent_counts = Counter()
    base_ref_assets = []
    for asset in assets:
        class_counts[asset.get("asset_data", {}).get("asset_class", "")] += 1
        parent = asset.get("tags", {}).get("selected", {}).get("ParentClass")
        if parent:
            parent_counts[parent] += 1
        refs = asset.get("references", {}).get("get_dependencies", [])
        if isinstance(refs, list) and any("BaseStarMapBorderActor" in ref for ref in refs):
            base_ref_assets.append(asset["asset_path"])
    return {
        "asset_count": len(assets),
        "asset_class_counts": dict(class_counts.most_common()),
        "parent_class_counts": dict(parent_counts.most_common()),
        "assets_depending_on_base_border": sorted(base_ref_assets),
    }


def write_markdown(report: dict) -> None:
    lines = [
        "# UE4 Starmap Border Path Inspection",
        "",
        "Focused MW5 Mod Editor dump for the crash family around `BaseStarMapBorderActor_C`, `StarMapActor_2570_C`, dated border actors, cluster assets, and starmap bounds.",
        "",
        "## Summary",
        "",
    ]
    summary = report.get("summary", {})
    lines.append(f"- inspected assets: `{summary.get('asset_count')}`")
    for parent, count in summary.get("parent_class_counts", {}).items():
        lines.append(f"- parent `{parent}` count `{count}`")
    if summary.get("assets_depending_on_base_border"):
        lines.append("- assets depending on `BaseStarMapBorderActor`:")
        for asset_path in summary["assets_depending_on_base_border"][:80]:
            lines.append(f"- `{asset_path}`")
    lines.extend(["", "## Focus Findings", ""])
    by_path = {asset["asset_path"]: asset for asset in report.get("assets", [])}
    for asset_path in FOCUS_ASSETS:
        asset = by_path.get(asset_path)
        if not asset:
            continue
        write_asset(lines, asset)
    lines.extend(["", "## Border Actor Parent Summary", ""])
    for asset in report.get("assets", []):
        path = asset.get("asset_path", "")
        name = path.rsplit("/", 1)[-1]
        if "StarMapBorderActor" not in name:
            continue
        tags = asset.get("tags", {}).get("selected", {})
        deps = asset.get("references", {}).get("get_dependencies", [])
        dep_count = len(deps) if isinstance(deps, list) else "error"
        lines.append(
            f"- `{path}` parent `{tags.get('ParentClass', '')}` native `{tags.get('NativeParentClass', '')}` deps `{dep_count}`"
        )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def write_asset(lines: list[str], asset: dict) -> None:
    lines.append(f"### `{asset['asset_path']}`")
    data = asset.get("asset_data", {})
    lines.append(f"- exists: `{asset.get('exists')}`")
    lines.append(f"- asset_class: `{data.get('asset_class', '')}`")
    tags = asset.get("tags", {}).get("selected", {})
    for key in ("GeneratedClass", "ParentClass", "NativeParentClass", "RowStructure"):
        if key in tags:
            lines.append(f"- {key}: `{tags[key]}`")
    props = asset.get("known_properties", {})
    if props:
        lines.append("- known properties:")
        for key, value in props.items():
            lines.append(f"- `{key}` = `{value}`")
    bp = asset.get("blueprint", {})
    if bp:
        lines.append("- class chain:")
        for item in bp.get("class_chain", []):
            lines.append(f"- `{item}`")
        bp_props = bp.get("default_object_known_properties", {})
        if bp_props:
            lines.append("- default object known properties:")
            for key, value in bp_props.items():
                lines.append(f"- `{key}` = `{value}`")
    refs = asset.get("references", {})
    for key in ("get_dependencies", "get_referencers"):
        value = refs.get(key, [])
        if isinstance(value, list):
            lines.append(f"- {key} count: `{len(value)}`")
            for ref in value[:35]:
                lines.append(f"- `{ref}`")
        else:
            lines.append(f"- {key}: `{value}`")
    lines.append("")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    report = {
        "source_note": "Editor-visible current MW5 assets only. Compare TKU cooked build-38 refs separately; do not infer cooked Blueprint graph safety from this report alone.",
        "focus_assets": FOCUS_ASSETS,
        "discovery_dirs": DISCOVERY_DIRS,
        "assets": [],
        "errors": [],
    }
    try:
        asset_registry = unreal.AssetRegistryHelpers.get_asset_registry()
        asset_paths = discover_asset_paths()
        report["asset_paths"] = asset_paths
        for asset_path in asset_paths:
            report["assets"].append(inspect_asset(asset_registry, asset_path))
        report["summary"] = summarize_assets(report["assets"])
    except Exception:
        report["errors"].append(traceback.format_exc())
    OUT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")
    write_markdown(report)
    unreal.log("TKU starmap border path inspection written to {}".format(OUT_JSON))


main()
