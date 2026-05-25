from __future__ import annotations

import json
import os
import re
import traceback
from collections import Counter, deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import unreal


REPORT_STEM = "ue4_active_campaign_actions_probe"
TARGET_MOD_NAME = os.environ.get("TKU_ACTIVE_ACTIONS_MOD_NAME", "TKUCompatEditorPatch").strip()
TARGET_PREFIX = f"/ModOverride/{TARGET_MOD_NAME}"

ROOT_ASSET_PATHS = (
    "/Game/DLC1/CareerMode/StartConditions/CareerMode_Start",
    "/Game/DLC1/CareerMode/StartConditions/FRR_CareerMode_Start",
    "/Game/DLC1/CareerMode/CareerModeCoreCampaign",
    "/Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters",
    "/Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones",
    "/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges",
    "/Game/DLC7/CampaignData/DLC7_CoreCampaign",
    "/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors",
    "/Game/DLC7/CampaignData/DLC7_ShowUnchartedSystems",
    "/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague",
    f"{TARGET_PREFIX}/DLC1/CareerMode/CareerModeCoreCampaign",
    f"{TARGET_PREFIX}/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters",
    f"{TARGET_PREFIX}/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones",
)

DISCOVERY_ROOTS = (
    "/Game/DLC7/CampaignData",
    "/Game/DLC7/PlaceClusterActions",
    f"{TARGET_PREFIX}/Campaign/Clusters",
    f"{TARGET_PREFIX}/DLC1/CareerMode/Clusters",
    f"{TARGET_PREFIX}/DLC7",
)

PROPERTY_CANDIDATES = (
    "campaign_arc",
    "campaign_arc_action_id",
    "campaign_arc_script",
    "campaign_event_list",
    "ClusterDataAsset",
    "ClusterDataAssetId",
    "cluster_constellation",
    "cluster_data_asset",
    "cluster_data_asset_id",
    "cluster_faction_asset",
    "cluster_overlay",
    "initial_star_map_borders",
    "is_legacy_cluster",
    "run_campaign_arc_script_on_save",
    "sub_campaigns",
    "system_ids",
    "toi_data",
)

FOCUS_TERMS = (
    "action",
    "arc",
    "border",
    "campaign",
    "career",
    "cluster",
    "faction",
    "overlay",
    "safe",
    "star",
    "system",
    "toi",
)

FOLLOW_DEP_TERMS = (
    "ClusterAsset",
    "Cluster_",
    "PlaceCluster",
    "PlaceSafeZone",
    "SafeZone",
    "Border",
    "Faction",
)

MAX_WALK_ASSETS = int(os.environ.get("TKU_ACTIVE_ACTIONS_MAX_ASSETS", "800"))
MAX_WALK_DEPTH = int(os.environ.get("TKU_ACTIVE_ACTIONS_MAX_DEPTH", "4"))


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


ASSET_PATH_RE = re.compile(r"/(?:Game|ModOverride)/[A-Za-z0-9_./-]+(?:\.[A-Za-z0-9_]+(?:_C)?)?")


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


def class_name(value: Any) -> str | None:
    try:
        return text(value.get_class().get_name())
    except Exception:
        return None


def class_path(value: Any) -> str | None:
    try:
        return text(value.get_class().get_path_name())
    except Exception:
        return None


def package_path_from_object_path(raw_path: str) -> str:
    path = raw_path.strip(" \t\r\n'\"),]}>")
    if "." in path:
        path = path.split(".", 1)[0]
    if path.endswith("_C"):
        path = path[:-2]
    return path


def extract_asset_paths(value: Any) -> list[str]:
    raw = text(value)
    paths = {package_path_from_object_path(match.group(0)) for match in ASSET_PATH_RE.finditer(raw)}
    return sorted(path for path in paths if path.startswith(("/Game/", "/ModOverride/")))


def collect_asset_paths_deep(value: Any, depth: int = 0) -> list[str]:
    paths = set(extract_asset_paths(value))
    if depth >= 5:
        return sorted(paths)

    direct_path = path_name(value)
    if direct_path:
        paths.add(package_path_from_object_path(direct_path))

    for prop_name in ("campaign_events", "campaign_actions", "CampaignEvents", "CampaignActions"):
        try:
            child = value.get_editor_property(prop_name)
        except Exception:
            continue
        paths.update(collect_asset_paths_deep(child, depth + 1))

    try:
        if hasattr(value, "__iter__") and not isinstance(value, (str, bytes)):
            for item in list(value)[:300]:
                paths.update(collect_asset_paths_deep(item, depth + 1))
    except Exception:
        pass
    return sorted(path for path in paths if path.startswith(("/Game/", "/ModOverride/")))


def jsonable(value: Any, depth: int = 0) -> Any:
    if depth > 5:
        return text(value)
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
            "sample": [{"key": jsonable(k, depth + 1), "value": jsonable(v, depth + 1)} for k, v in items[:40]],
        }
    if isinstance(value, (list, tuple, set)):
        values = list(value)
        return {
            "kind": type(value).__name__,
            "count": len(values),
            "sample": [jsonable(item, depth + 1) for item in values[:45]],
            "tail_sample": [jsonable(item, depth + 1) for item in values[-18:]],
        }
    try:
        if hasattr(value, "__iter__") and not isinstance(value, (str, bytes)):
            values = list(value)
            return {
                "kind": type(value).__name__,
                "count": len(values),
                "sample": [jsonable(item, depth + 1) for item in values[:45]],
                "tail_sample": [jsonable(item, depth + 1) for item in values[-18:]],
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


def filtered_member_names(value: Any) -> list[str]:
    try:
        names = dir(value)
    except Exception:
        return []
    return sorted(
        name
        for name in names
        if not name.startswith("_") and any(term in name.lower() for term in FOCUS_TERMS)
    )


def read_properties(obj: Any) -> dict[str, Any]:
    names = set(PROPERTY_CANDIDATES)
    names.update(filtered_member_names(obj))
    props: dict[str, Any] = {}
    for name in sorted(names):
        try:
            raw = obj.get_editor_property(name)
            props[name] = {
                "value": jsonable(raw),
                "path": path_name(raw),
                "asset_paths": extract_asset_paths(raw),
                "repr": text(raw)[:4000],
            }
        except Exception:
            continue
    return props


def asset_data(asset_path: str) -> dict[str, Any]:
    try:
        data = unreal.EditorAssetLibrary.find_asset_data(asset_path)
        return {
            "is_valid": bool(data.is_valid()),
            "asset_class": text(data.asset_class),
            "asset_name": text(data.asset_name),
            "package_name": text(data.package_name),
            "package_path": text(data.package_path),
            "object_path": text(data.object_path),
        }
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}


def dependency_options() -> Any:
    return unreal.AssetRegistryDependencyOptions(True, True, True, True, True)


def package_dependencies(asset_path: str) -> dict[str, Any]:
    out: dict[str, Any] = {}
    try:
        registry = unreal.AssetRegistryHelpers.get_asset_registry()
        opts = dependency_options()
        for method_name in ("get_dependencies", "get_referencers"):
            try:
                values = sorted(text(item) for item in (getattr(registry, method_name)(asset_path, opts) or []))
                out[method_name] = {
                    "count": len(values),
                    "focused": [item for item in values if any(term in item for term in FOLLOW_DEP_TERMS)][:160],
                    "sample": values[:80],
                }
            except Exception as exc:
                out[method_name] = {"error": f"{type(exc).__name__}: {exc}"}
    except Exception as exc:
        out["error"] = f"{type(exc).__name__}: {exc}"
    return out


def direct_sub_campaign_paths(asset: Any) -> list[str]:
    try:
        raw = asset.get_editor_property("sub_campaigns")
    except Exception:
        return []
    paths = []
    try:
        iterable = list(raw)
    except Exception:
        iterable = []
    for item in iterable:
        path = path_name(item)
        if path:
            paths.append(package_path_from_object_path(path))
    paths.extend(extract_asset_paths(raw))
    return sorted(set(paths))


def direct_event_action_paths(asset: Any) -> list[str]:
    try:
        raw = asset.get_editor_property("campaign_event_list")
    except Exception:
        return []
    return sorted(set(collect_asset_paths_deep(raw)))


def inspect_loaded_object(label: str, obj: Any) -> dict[str, Any]:
    return {
        "label": label,
        "object": jsonable(obj),
        "path": path_name(obj),
        "class_name": class_name(obj),
        "class_path": class_path(obj),
        "members": filtered_member_names(obj)[:300],
        "properties": read_properties(obj),
    }


def inspect_asset(asset_path: str, reason: str) -> dict[str, Any]:
    normalized = package_path_from_object_path(asset_path)
    out: dict[str, Any] = {
        "asset_path": normalized,
        "reason": reason,
        "asset_data": asset_data(normalized),
        "dependencies": package_dependencies(normalized),
        "exists": False,
        "sub_campaign_paths": [],
        "event_action_paths": [],
        "referenced_asset_paths": [],
        "referenced_cluster_paths": [],
    }
    try:
        out["exists"] = bool(unreal.EditorAssetLibrary.does_asset_exist(normalized))
    except Exception as exc:
        out["exists_error"] = f"{type(exc).__name__}: {exc}"
        return out
    if not out["exists"]:
        return out

    try:
        asset = unreal.EditorAssetLibrary.load_asset(normalized)
        out["asset"] = inspect_loaded_object("asset", asset)
        out["sub_campaign_paths"] = direct_sub_campaign_paths(asset)
        out["event_action_paths"] = direct_event_action_paths(asset)
    except Exception as exc:
        out["load_error"] = f"{type(exc).__name__}: {exc}"
        return out

    if (out.get("asset_data") or {}).get("asset_class") == "Blueprint":
        try:
            bp_class = unreal.EditorAssetLibrary.load_blueprint_class(normalized)
            out["blueprint_class"] = jsonable(bp_class)
            if bp_class:
                cdo = unreal.get_default_object(bp_class)
                out["cdo"] = inspect_loaded_object("cdo", cdo)
        except Exception as exc:
            out["blueprint_error"] = f"{type(exc).__name__}: {exc}"

    references: set[str] = set(out.get("sub_campaign_paths") or [])
    references.update(out.get("event_action_paths") or [])
    for section in ("asset", "cdo"):
        for prop in ((out.get(section) or {}).get("properties") or {}).values():
            references.update(prop.get("asset_paths") or [])
            path = prop.get("path")
            if path:
                references.add(package_path_from_object_path(path))
    for method_name in ("get_dependencies", "get_referencers"):
        dep_info = (out.get("dependencies") or {}).get(method_name) or {}
        for dep in dep_info.get("focused") or []:
            references.add(package_path_from_object_path(dep))
    out["referenced_asset_paths"] = sorted(path for path in references if path.startswith(("/Game/", "/ModOverride/")))
    out["referenced_cluster_paths"] = [
        path
        for path in out["referenced_asset_paths"]
        if any(term in path for term in ("ClusterAsset", "CampaignCluster", "ConflictCluster"))
    ]
    return out


def discover_dlc7_arcs() -> list[str]:
    paths: set[str] = set()
    try:
        registry = unreal.AssetRegistryHelpers.get_asset_registry()
        for data in list(registry.get_assets_by_path("/Game/DLC7/CampaignData", True)):
            package_name = text(data.package_name)
            asset_class = text(data.asset_class)
            if asset_class == "MWCampaignArcAsset" or package_name.rsplit("/", 1)[-1].startswith("DLC7_"):
                paths.add(package_name)
    except Exception:
        pass
    return sorted(paths)


def discovery_inventory() -> dict[str, Any]:
    inventory: dict[str, Any] = {}
    for root in DISCOVERY_ROOTS:
        item: dict[str, Any] = {"exists": False, "asset_count": 0, "focused_count": 0, "focused_sample": []}
        try:
            if unreal.EditorAssetLibrary.does_directory_exist(root):
                raw_paths = sorted(set(package_path_from_object_path(path) for path in unreal.EditorAssetLibrary.list_assets(root, True, False)))
                focused = [
                    path
                    for path in raw_paths
                    if any(term.lower() in path.lower() for term in FOCUS_TERMS + FOLLOW_DEP_TERMS)
                ]
                item.update(
                    {
                        "exists": True,
                        "asset_count": len(raw_paths),
                        "focused_count": len(focused),
                        "focused_sample": focused[:180],
                    }
                )
        except Exception as exc:
            item["error"] = f"{type(exc).__name__}: {exc}"
        inventory[root] = item
    inventory["dlc7_arc_assets"] = discover_dlc7_arcs()
    return inventory


def should_follow(path: str, depth: int, source_info: dict[str, Any]) -> bool:
    if depth >= MAX_WALK_DEPTH:
        return False
    if path.startswith(TARGET_PREFIX):
        return True
    if any(term in path for term in ("CareerMode", "DLC7_", "PlaceCluster", "PlaceSafeZone", "BorderChanges")):
        return True
    asset_class = (source_info.get("asset_data") or {}).get("asset_class")
    if asset_class in {"MWCampaignArcAsset", "Blueprint"}:
        return any(term in path for term in FOLLOW_DEP_TERMS + ("ArcAction", "Campaign"))
    return any(term in path for term in FOLLOW_DEP_TERMS)


def walk_active_graph() -> dict[str, Any]:
    seeds = list(ROOT_ASSET_PATHS) + discover_dlc7_arcs()
    queue: deque[tuple[str, int, str]] = deque((package_path_from_object_path(path), 0, "root") for path in seeds)
    assets: dict[str, Any] = {}
    edges: list[dict[str, Any]] = []

    while queue and len(assets) < MAX_WALK_ASSETS:
        asset_path, depth, reason = queue.popleft()
        if asset_path in assets:
            continue
        info = inspect_asset(asset_path, reason)
        info["walk_depth"] = depth
        assets[asset_path] = info
        next_paths: set[str] = set(info.get("sub_campaign_paths") or [])
        next_paths.update(info.get("event_action_paths") or [])
        next_paths.update(info.get("referenced_asset_paths") or [])
        for ref in sorted(next_paths):
            edges.append({"from": asset_path, "to": ref, "depth": depth, "reason": "extracted-reference"})
            if ref not in assets and should_follow(ref, depth, info):
                queue.append((ref, depth + 1, f"referenced by {asset_path}"))
    return {"seeds": seeds, "assets": assets, "edges": edges, "walk_limit_hit": bool(queue)}


def collect_graph_summary(graph: dict[str, Any]) -> dict[str, Any]:
    assets = graph.get("assets") or {}
    class_counts = Counter((info.get("asset_data") or {}).get("asset_class") or "unknown" for info in assets.values())
    active_actions = sorted(
        path
        for path, info in assets.items()
        if (info.get("asset_data") or {}).get("asset_class") == "Blueprint"
        and any(term in path for term in ("ArcAction", "PlaceCluster", "PlaceSafeZone"))
    )
    place_cluster_actions = [path for path in active_actions if "PlaceCluster" in path or "PlaceHiddenSystemsCluster" in path]
    place_safezone_actions = [path for path in active_actions if "PlaceSafeZone" in path]
    cluster_refs: set[str] = set()
    mod_cluster_refs: set[str] = set()
    action_cluster_bindings: list[dict[str, str]] = []

    for path, info in assets.items():
        refs = set(info.get("referenced_cluster_paths") or [])
        cluster_refs.update(refs)
        mod_cluster_refs.update(ref for ref in refs if ref.startswith(TARGET_PREFIX))
        cdo_props = ((info.get("cdo") or {}).get("properties") or {})
        for prop_name in ("ClusterDataAsset", "cluster_data_asset", "ClusterDataAssetId", "cluster_data_asset_id"):
            prop = cdo_props.get(prop_name) or {}
            refs = prop.get("asset_paths") or []
            if refs:
                for ref in refs:
                    action_cluster_bindings.append({"action": path, "property": prop_name, "cluster_asset": ref})
                continue
            prop_repr = prop.get("repr")
            if prop_repr and "primary_asset_name" in prop_repr:
                action_cluster_bindings.append({"action": path, "property": prop_name, "cluster_asset": prop_repr[:500]})

    return {
        "asset_count": len(assets),
        "class_counts": dict(class_counts.most_common()),
        "action_count": len(active_actions),
        "active_actions_sample": active_actions[:120],
        "place_cluster_action_count": len(place_cluster_actions),
        "place_cluster_actions_sample": place_cluster_actions[:120],
        "place_safezone_action_count": len(place_safezone_actions),
        "place_safezone_actions_sample": place_safezone_actions[:80],
        "cluster_reference_count": len(cluster_refs),
        "cluster_references_sample": sorted(cluster_refs)[:160],
        "mod_cluster_reference_count": len(mod_cluster_refs),
        "mod_cluster_references_sample": sorted(mod_cluster_refs)[:160],
        "action_cluster_bindings_sample": action_cluster_bindings[:180],
    }


def build_findings(report: dict[str, Any]) -> list[str]:
    summary = report.get("graph_summary") or {}
    graph = report.get("active_graph") or {}
    assets = graph.get("assets") or {}
    findings = [
        f"Active graph assets inspected: {summary.get('asset_count')} class counts {summary.get('class_counts')}.",
        f"Active ArcAction blueprints discovered from campaign-event lists/references: {summary.get('action_count')}.",
        f"PlaceCluster-like actions in walked graph: {summary.get('place_cluster_action_count')}.",
        f"PlaceSafeZone actions in walked graph: {summary.get('place_safezone_action_count')}.",
        f"Cluster references in walked graph: {summary.get('cluster_reference_count')}; mod-owned cluster references: {summary.get('mod_cluster_reference_count')}.",
    ]
    for target in (
        "/Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters",
        f"{TARGET_PREFIX}/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters",
        "/Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones",
        f"{TARGET_PREFIX}/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones",
    ):
        info = assets.get(target)
        if not info:
            continue
        findings.append(
            f"{target} subcampaigns={len(info.get('sub_campaign_paths') or [])} event_actions={len(info.get('event_action_paths') or [])}."
        )
    if summary.get("place_cluster_action_count") == 0:
        findings.append("No PlaceCluster action was reached from active roots; the next patch should target arc wiring, not cluster data alone.")
    elif summary.get("mod_cluster_reference_count") == 0:
        findings.append("PlaceCluster actions were reached, but none referenced mod-owned TKU cluster assets in this walk.")
    return findings


def write_markdown(report: dict[str, Any]) -> None:
    lines = [
        "# UE4 Active Campaign Actions Probe",
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

    summary = report.get("graph_summary") or {}
    lines.extend(["", "## Graph Summary", ""])
    for key in (
        "asset_count",
        "class_counts",
        "action_count",
        "place_cluster_action_count",
        "place_safezone_action_count",
        "cluster_reference_count",
        "mod_cluster_reference_count",
    ):
        lines.append(f"- {key}: `{summary.get(key)}`")

    lines.extend(["", "## Action Cluster Bindings", ""])
    for row in summary.get("action_cluster_bindings_sample", [])[:120]:
        lines.append(f"- `{row['action']}` `{row['property']}` -> `{row['cluster_asset']}`")

    lines.extend(["", "## Place Cluster Actions", ""])
    for path in summary.get("place_cluster_actions_sample", [])[:160]:
        lines.append(f"- `{path}`")

    lines.extend(["", "## Mod Cluster References", ""])
    for path in summary.get("mod_cluster_references_sample", [])[:160]:
        lines.append(f"- `{path}`")

    lines.extend(["", "## Discovery Inventory", ""])
    for root, info in (report.get("discovery") or {}).items():
        if root == "dlc7_arc_assets":
            lines.append(f"- `{root}`: `{len(info)}`")
        else:
            lines.append(f"- `{root}`: `{info}`")

    lines.extend(["", "## Walked Assets", ""])
    for asset_path, info in (report.get("active_graph", {}).get("assets") or {}).items():
        data = info.get("asset_data") or {}
        lines.append(f"### `{asset_path}`")
        lines.append(f"- depth/reason: `{info.get('walk_depth')}` / `{info.get('reason')}`")
        lines.append(f"- class: `{data.get('asset_class')}` exists `{info.get('exists')}`")
        if info.get("sub_campaign_paths"):
            lines.append(f"- subcampaigns: `{len(info.get('sub_campaign_paths') or [])}`")
            for path in info.get("sub_campaign_paths", [])[:50]:
                lines.append(f"  - `{path}`")
        if info.get("event_action_paths"):
            lines.append(f"- event actions: `{len(info.get('event_action_paths') or [])}`")
            for path in info.get("event_action_paths", [])[:80]:
                lines.append(f"  - `{path}`")
        if info.get("referenced_cluster_paths"):
            lines.append(f"- referenced clusters: `{info.get('referenced_cluster_paths')[:80]}`")
        cdo_props = ((info.get("cdo") or {}).get("properties") or {})
        focused_cdo_props = {
            key: value
            for key, value in cdo_props.items()
            if any(term.lower() in key.lower() for term in ("cluster", "campaign", "border", "faction"))
        }
        if focused_cdo_props:
            lines.append(f"- cdo focused properties: `{focused_cdo_props}`")
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
        "root_asset_paths": list(ROOT_ASSET_PATHS),
        "max_walk_assets": MAX_WALK_ASSETS,
        "max_walk_depth": MAX_WALK_DEPTH,
        "discovery": {},
        "active_graph": {},
        "graph_summary": {},
        "findings": [],
        "errors": [],
    }
    try:
        report["discovery"] = discovery_inventory()
    except Exception:
        report["errors"].append({"discovery": traceback.format_exc()})
    try:
        report["active_graph"] = walk_active_graph()
        report["graph_summary"] = collect_graph_summary(report["active_graph"])
        report["findings"] = build_findings(report)
    except Exception:
        report["errors"].append({"active_graph": traceback.format_exc()})
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True, default=str), encoding="utf-8")
    write_markdown(report)
    unreal.log(f"TKU active campaign actions probe wrote {OUT_JSON}")


main()
