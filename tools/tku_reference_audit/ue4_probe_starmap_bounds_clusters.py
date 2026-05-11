from __future__ import annotations

import csv
import json
import math
import traceback
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import unreal


from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
EDITOR_ROOT = Path(r"E:\Games\MechWarrior5Editor")
OUT_DIR = REPORTS_DIR / "tku_editor_first"
OUT_JSON = OUT_DIR / "ue4_starmap_bounds_clusters_probe.json"
OUT_MD = OUT_DIR / "ue4_starmap_bounds_clusters_probe.md"

STARMAP_LEVEL = "/Game/Levels/FrontEnd/StarMap"
STARMAP_BLUEPRINTS = (
    "/Game/UI/FrontEnd/StarMapPawn",
    "/Game/UI/FrontEnd/Starmap/StarMapActor",
    "/Game/UI/FrontEnd/Starmap/StarSystemBody",
)
MIGRATION_UTILITY = "/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets"
CLUSTER_ROOT = "/Game/Campaign/Clusters"
RUNTIME_CSV = EDITOR_ROOT / "MW5Mercs" / "Content" / "InnerSphereData" / "MW5_InnerSphereData.csv"
WIDE_JSON = EDITOR_ROOT / "MW5Mercs" / "Content" / "Data" / "InnerSphereMap" / "MW5_InnerSphereData.json"

PROPERTY_TERMS = (
    "bound",
    "pan",
    "zoom",
    "camera",
    "clamp",
    "limit",
    "movement",
    "starmap",
    "star_map",
    "cluster",
    "border",
    "faction",
    "system",
    "body",
    "overlay",
    "constellation",
    "distance",
    "scale",
)

KNOWN_PROPERTY_CANDIDATES = (
    "PanBoundsHorizontal",
    "PanBoundsVertical",
    "ZoomDistanceList",
    "ZoomLevelThresholds",
    "system_ids",
    "cluster_faction_asset",
    "cluster_overlay",
    "cluster_constellation",
    "ClusterDataAsset",
    "ClusterDataAssetId",
    "BorderActor",
    "BorderAsset",
    "AllStarMapBorderChanges",
)


def to_jsonable(value, depth: int = 0):
    if depth > 5:
        return str(value)
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Path):
        return str(value)
    if hasattr(value, "x") and hasattr(value, "y") and hasattr(value, "z"):
        return {"x": value.x, "y": value.y, "z": value.z}
    if isinstance(value, dict):
        return {str(k): to_jsonable(v, depth + 1) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [to_jsonable(item, depth + 1) for item in value]
    try:
        if hasattr(value, "__iter__") and not isinstance(value, (str, bytes)):
            return [to_jsonable(item, depth + 1) for item in list(value)]
    except Exception:
        pass
    out = {"repr": str(value), "python_type": type(value).__name__}
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


def safe(label: str, func, *args):
    try:
        return {"ok": True, "value": to_jsonable(func(*args))}
    except Exception as exc:
        return {"ok": False, "error": f"{type(exc).__name__}: {exc}"}


def public_members(obj) -> list[str]:
    try:
        return sorted(name for name in dir(obj) if not name.startswith("_"))
    except Exception:
        return []


def get_path_name(obj) -> str:
    try:
        return str(obj.get_path_name())
    except Exception:
        return str(obj)


def get_class_name(obj) -> str:
    try:
        return str(obj.get_class().get_name())
    except Exception:
        return ""


def read_editor_property(obj, name: str):
    try:
        return True, to_jsonable(obj.get_editor_property(name))
    except Exception as exc:
        return False, f"{type(exc).__name__}: {exc}"


def filtered_properties(obj, limit: int = 160) -> dict:
    names = set(KNOWN_PROPERTY_CANDIDATES)
    for member in public_members(obj):
        lowered = member.lower()
        if any(term in lowered for term in PROPERTY_TERMS):
            names.add(member)
    found = {}
    errors = {}
    for name in sorted(names):
        ok, value = read_editor_property(obj, name)
        if ok:
            found[name] = value
        elif name in KNOWN_PROPERTY_CANDIDATES:
            errors[name] = value
        if len(found) >= limit:
            break
    return {"readable": found, "known_candidate_errors": errors}


def class_chain(bp_class) -> list[str]:
    chain = []
    current = bp_class
    for _ in range(24):
        if not current:
            break
        chain.append(get_path_name(current))
        try:
            current = current.get_super_class()
        except Exception:
            break
    return chain


def blueprint_probe(asset_path: str) -> dict:
    out = {"asset_path": asset_path}
    out["asset_exists"] = safe("does_asset_exist", unreal.EditorAssetLibrary.does_asset_exist, asset_path)
    asset_result = safe("load_asset", unreal.EditorAssetLibrary.load_asset, asset_path)
    out["asset"] = asset_result
    if asset_result["ok"] and asset_result["value"]:
        asset = unreal.EditorAssetLibrary.load_asset(asset_path)
        out["asset_class"] = get_class_name(asset)
        out["asset_properties"] = filtered_properties(asset)
    try:
        bp_class = unreal.EditorAssetLibrary.load_blueprint_class(asset_path)
    except Exception as exc:
        out["blueprint_error"] = f"{type(exc).__name__}: {exc}"
        return out
    if not bp_class:
        out["blueprint_class"] = None
        return out
    out["blueprint_class"] = get_path_name(bp_class)
    out["class_chain"] = class_chain(bp_class)
    try:
        cdo = unreal.get_default_object(bp_class)
        out["cdo_path"] = get_path_name(cdo)
        out["cdo_class"] = get_class_name(cdo)
        out["cdo_properties"] = filtered_properties(cdo)
    except Exception as exc:
        out["cdo_error"] = f"{type(exc).__name__}: {exc}"
    return out


def actor_label(actor) -> str:
    try:
        return str(actor.get_actor_label())
    except Exception:
        try:
            return str(actor.get_name())
        except Exception:
            return str(actor)


def range_summary(points: list[dict]) -> dict:
    if not points:
        return {"count": 0}
    xs = [point["x"] for point in points]
    ys = [point["y"] for point in points]
    zs = [point["z"] for point in points]
    return {
        "count": len(points),
        "x": {"min": min(xs), "max": max(xs), "span": max(xs) - min(xs)},
        "y": {"min": min(ys), "max": max(ys), "span": max(ys) - min(ys)},
        "z": {"min": min(zs), "max": max(zs), "span": max(zs) - min(zs)},
    }


def inspect_starmap_level() -> dict:
    out = {"level": STARMAP_LEVEL}
    load_result = safe("load_map", unreal.EditorLoadingAndSavingUtils.load_map, STARMAP_LEVEL)
    out["load_map"] = load_result
    if not load_result["ok"]:
        return out
    try:
        actors = list(unreal.EditorLevelLibrary.get_all_level_actors())
    except Exception as exc:
        out["actors_error"] = f"{type(exc).__name__}: {exc}"
        return out

    class_counts = Counter()
    focus_actors = []
    system_points = []
    all_points = []
    for actor in actors:
        cls = get_class_name(actor)
        label = actor_label(actor)
        class_counts[cls] += 1
        try:
            loc = actor.get_actor_location()
            loc_json = {"x": float(loc.x), "y": float(loc.y), "z": float(loc.z)}
            all_points.append(loc_json)
        except Exception:
            loc_json = None
        joined = f"{cls} {label}".lower()
        if "starsystembody" in joined:
            if loc_json:
                system_points.append(loc_json)
        if any(term in joined for term in ("starmap", "star system", "starsystem", "camera", "pawn", "border")):
            focus_actors.append(
                {
                    "label": label,
                    "class": cls,
                    "path": get_path_name(actor),
                    "location": loc_json,
                }
            )
    out["actor_count"] = len(actors)
    out["class_counts_top"] = dict(class_counts.most_common(40))
    out["all_actor_location_range"] = range_summary(all_points)
    out["star_system_body_location_range"] = range_summary(system_points)
    out["focus_actor_count"] = len(focus_actors)
    out["focus_actors_sample"] = focus_actors[:250]
    out["world_settings"] = safe(
        "get_world_settings",
        lambda: unreal.EditorLevelLibrary.get_editor_world().get_world_settings(),
    )
    return out


def parse_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-16", newline="") as handle:
        return list(csv.DictReader(handle))


def numeric_range(rows: list[dict], x_key: str = "PosX", y_key: str = "PosY") -> dict:
    xs = []
    ys = []
    for row in rows:
        try:
            x = float(row.get(x_key, ""))
            y = float(row.get(y_key, ""))
        except Exception:
            continue
        if math.isfinite(x) and math.isfinite(y):
            xs.append(x)
            ys.append(y)
    if not xs:
        return {"count": 0}
    return {
        "count": len(xs),
        "x": {"min": min(xs), "max": max(xs), "span": max(xs) - min(xs)},
        "y": {"min": min(ys), "max": max(ys), "span": max(ys) - min(ys)},
    }


def source_data_probe() -> dict:
    out = {
        "runtime_csv": {"path": str(RUNTIME_CSV)},
        "wide_json": {"path": str(WIDE_JSON)},
    }
    try:
        csv_rows = parse_csv_rows(RUNTIME_CSV)
        out["runtime_csv"]["row_count"] = len(csv_rows)
        out["runtime_csv"]["pos_range"] = numeric_range(csv_rows)
        out["runtime_csv"]["cluster_rows"] = sum(
            1 for row in csv_rows if row.get("Cluster") not in ("", "None", '(Id="")', None)
        )
    except Exception as exc:
        out["runtime_csv"]["error"] = f"{type(exc).__name__}: {exc}"
    try:
        rows = json.loads(WIDE_JSON.read_text(encoding="utf-8-sig"))
        out["wide_json"]["row_count"] = len(rows)
        out["wide_json"]["pos_range"] = numeric_range(rows)
        out["wide_json"]["sample_far_systems"] = [
            {
                "Name": row.get("Name"),
                "StarSystemName": row.get("StarSystemName"),
                "PosX": row.get("PosX"),
                "PosY": row.get("PosY"),
            }
            for row in sorted(
                rows,
                key=lambda item: abs(float(item.get("PosX") or 0)) + abs(float(item.get("PosY") or 0)),
                reverse=True,
            )[:20]
        ]
    except Exception as exc:
        out["wide_json"]["error"] = f"{type(exc).__name__}: {exc}"
    return out


def dependency_options():
    return unreal.AssetRegistryDependencyOptions(True, True, True, True, True)


def asset_dependencies(asset_path: str) -> dict:
    try:
        reg = unreal.AssetRegistryHelpers.get_asset_registry()
        opts = dependency_options()
        return {
            "dependencies": sorted(str(item) for item in (reg.get_dependencies(asset_path, opts) or [])),
            "referencers": sorted(str(item) for item in (reg.get_referencers(asset_path, opts) or [])),
        }
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}


def asset_tags(asset_path: str) -> dict:
    try:
        data = unreal.EditorAssetLibrary.find_asset_data(asset_path)
        try:
            raw_tags = unreal.EditorAssetLibrary.get_tag_values(asset_path)
            keep = {
                "GeneratedClass",
                "ParentClass",
                "NativeParentClass",
                "BlueprintType",
                "IsDataOnly",
                "BlueprintPath",
                "TickFrequency",
                "TickPrediction",
                "TickPredictionReason",
                "NumReplicatedProperties",
            }
            tags = {str(k): str(v) for k, v in raw_tags.items() if str(k) in keep}
        except Exception as exc:
            tags = {"tag_read_error": f"{type(exc).__name__}: {exc}"}
        return {
            "is_valid": bool(data.is_valid()),
            "asset_class": str(data.asset_class),
            "package_name": str(data.package_name),
            "object_path": str(data.object_path),
            "tags": tags,
        }
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}


def cluster_asset_probe() -> dict:
    out = {"root": CLUSTER_ROOT}
    try:
        paths = [
            path.split(".", 1)[0]
            for path in unreal.EditorAssetLibrary.list_assets(CLUSTER_ROOT, True, False)
        ]
    except Exception as exc:
        out["error"] = f"{type(exc).__name__}: {exc}"
        return out
    rows = []
    for path in sorted(set(paths)):
        try:
            data = unreal.EditorAssetLibrary.find_asset_data(path)
            if str(data.asset_class) != "MWClusterDataAsset":
                continue
            asset = unreal.EditorAssetLibrary.load_asset(path)
        except Exception as exc:
            rows.append({"asset_path": path, "error": f"{type(exc).__name__}: {exc}"})
            continue
        props = filtered_properties(asset)["readable"]
        system_ids = props.get("system_ids", [])
        rows.append(
            {
                "asset_path": path,
                "system_count": len(system_ids) if isinstance(system_ids, list) else 0,
                "cluster_faction_asset": props.get("cluster_faction_asset"),
                "cluster_overlay": props.get("cluster_overlay"),
                "cluster_constellation": props.get("cluster_constellation"),
                "properties": props,
            }
        )
    out["asset_count"] = len(rows)
    out["total_system_memberships"] = sum(row.get("system_count", 0) for row in rows)
    out["with_overlay"] = sum(1 for row in rows if row.get("cluster_overlay"))
    out["with_constellation"] = sum(1 for row in rows if row.get("cluster_constellation"))
    out["assets"] = rows
    focus_terms = ("Taurian", "Outworlds", "Steiner", "Lyran", "IndustrialHub", "Rasalhague", "Canopus")
    out["focus_assets"] = [
        row for row in rows if any(term.lower() in row["asset_path"].lower() for term in focus_terms)
    ][:80]
    return out


def migration_utility_probe() -> dict:
    out = {"asset_path": MIGRATION_UTILITY}
    out["asset"] = safe("load_asset", unreal.EditorAssetLibrary.load_asset, MIGRATION_UTILITY)
    out["tags"] = asset_tags(MIGRATION_UTILITY)
    out["references"] = asset_dependencies(MIGRATION_UTILITY)
    return out


def repair_track_decision(report: dict) -> dict:
    level = report.get("starmap_level", {})
    source = report.get("source_data", {})
    clusters = report.get("cluster_assets", {})
    star_count = level.get("star_system_body_location_range", {}).get("count")
    runtime_rows = source.get("runtime_csv", {}).get("row_count")
    wide_rows = source.get("wide_json", {}).get("row_count")
    current_cluster_count = clusters.get("asset_count")

    findings = []
    if star_count and wide_rows and star_count < wide_rows:
        findings.append(
            "Current StarMap level has fewer placed StarSystemBody actors than the wide source JSON has systems; expanded-map repair is not only a camera-bound value."
        )
    if runtime_rows and wide_rows and runtime_rows < wide_rows:
        findings.append(
            "Runtime InnerSphere CSV is vanilla-scale while source JSON is wider; data generation/import remains part of the bounds track."
        )
    if current_cluster_count:
        findings.append(
            "Current MW5 exposes territory overlays through explicit MWClusterDataAsset assets with system_ids, faction, overlay, and constellation fields."
        )

    return {
        "bounds_track": "Inspect StarMapActor, StarMap level generation/placement, and data import before authoring another pawn-only bounds patch.",
        "overlay_track": "Proceed toward current-schema MWClusterDataAsset migration; do not restore old cooked TKU border actors for overlays.",
        "authoring_gate": "Use commandlet Python only for inspection/export; use MW5 Mod Editor UI for first Create Mod / Save To Mod authoring unless a later scripted widget path is proven.",
        "findings": findings,
    }


def write_markdown(report: dict) -> None:
    decision = report["repair_track_decision"]
    level = report.get("starmap_level", {})
    source = report.get("source_data", {})
    clusters = report.get("cluster_assets", {})
    lines = [
        "# UE4 Starmap Bounds And Cluster Probe",
        "",
        f"- Generated: `{report['generated_utc']}`",
        "- Method: non-mutating MW5 Mod Editor commandlet inspection.",
        "- Safety: loaded assets and the current starmap level for inspection only; did not save, duplicate, package, or modify assets.",
        "",
        "## Repair Gate",
        "",
        f"- Bounds track: {decision['bounds_track']}",
        f"- Overlay track: {decision['overlay_track']}",
        f"- Authoring gate: {decision['authoring_gate']}",
        "",
        "Findings:",
    ]
    for item in decision["findings"]:
        lines.append(f"- {item}")

    lines.extend(["", "## Starmap Level", ""])
    lines.append(f"- Level: `{STARMAP_LEVEL}`")
    lines.append(f"- Actor count: `{level.get('actor_count')}`")
    lines.append(f"- Top classes: `{level.get('class_counts_top')}`")
    lines.append(f"- StarSystemBody range: `{level.get('star_system_body_location_range')}`")
    lines.append(f"- Focus actor count: `{level.get('focus_actor_count')}`")
    for actor in level.get("focus_actors_sample", [])[:80]:
        lines.append(f"- `{actor.get('label')}` class `{actor.get('class')}` loc `{actor.get('location')}`")

    lines.extend(["", "## Source Data Ranges", ""])
    lines.append(f"- Runtime CSV rows: `{source.get('runtime_csv', {}).get('row_count')}`")
    lines.append(f"- Runtime CSV range: `{source.get('runtime_csv', {}).get('pos_range')}`")
    lines.append(f"- Runtime CSV cluster rows: `{source.get('runtime_csv', {}).get('cluster_rows')}`")
    lines.append(f"- Wide JSON rows: `{source.get('wide_json', {}).get('row_count')}`")
    lines.append(f"- Wide JSON range: `{source.get('wide_json', {}).get('pos_range')}`")

    lines.extend(["", "## Blueprint CDOs", ""])
    for bp in report.get("blueprints", []):
        lines.append(f"### `{bp['asset_path']}`")
        lines.append(f"- Class: `{bp.get('blueprint_class')}`")
        lines.append(f"- Class chain: `{bp.get('class_chain')}`")
        readable = bp.get("cdo_properties", {}).get("readable", {})
        for key, value in readable.items():
            lines.append(f"- `{key}`: `{value}`")
        lines.append("")

    lines.extend(["## Cluster Assets", ""])
    lines.append(f"- Count: `{clusters.get('asset_count')}`")
    lines.append(f"- Total system memberships: `{clusters.get('total_system_memberships')}`")
    lines.append(f"- With overlay: `{clusters.get('with_overlay')}`")
    lines.append(f"- With constellation: `{clusters.get('with_constellation')}`")
    for row in clusters.get("focus_assets", [])[:80]:
        lines.append(
            f"- `{row['asset_path']}` systems `{row.get('system_count')}` faction `{row.get('cluster_faction_asset')}` overlay `{row.get('cluster_overlay')}` constellation `{row.get('cluster_constellation')}`"
        )

    lines.extend(["", "## Migration Utility", ""])
    util = report.get("migration_utility", {})
    lines.append(f"- Asset: `{MIGRATION_UTILITY}`")
    lines.append(f"- Tags: `{util.get('tags')}`")
    refs = util.get("references", {})
    lines.append(f"- Dependency count: `{len(refs.get('dependencies', [])) if isinstance(refs.get('dependencies'), list) else refs.get('dependencies')}`")
    for dep in refs.get("dependencies", [])[:80]:
        lines.append(f"- `{dep}`")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    report = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "non_mutating": True,
        "starmap_level": {},
        "blueprints": [],
        "source_data": {},
        "cluster_assets": {},
        "migration_utility": {},
        "errors": [],
    }
    try:
        report["starmap_level"] = inspect_starmap_level()
    except Exception:
        report["errors"].append({"starmap_level": traceback.format_exc()})
    for asset_path in STARMAP_BLUEPRINTS:
        try:
            report["blueprints"].append(blueprint_probe(asset_path))
        except Exception:
            report["errors"].append({asset_path: traceback.format_exc()})
    try:
        report["source_data"] = source_data_probe()
    except Exception:
        report["errors"].append({"source_data": traceback.format_exc()})
    try:
        report["cluster_assets"] = cluster_asset_probe()
    except Exception:
        report["errors"].append({"cluster_assets": traceback.format_exc()})
    try:
        report["migration_utility"] = migration_utility_probe()
    except Exception:
        report["errors"].append({"migration_utility": traceback.format_exc()})
    report["repair_track_decision"] = repair_track_decision(report)
    OUT_JSON.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    write_markdown(report)
    unreal.log(f"TKU starmap bounds and cluster probe wrote {OUT_JSON} and {OUT_MD}")


main()
