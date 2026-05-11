from __future__ import annotations

import csv
import json
import math
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
EDITOR_ROOT = Path(r"E:\Games\MechWarrior5Editor")
EDITOR_CONTENT = EDITOR_ROOT / "MW5Mercs" / "Content"
OUT_DIR = REPORTS_DIR / "tku_editor_first"

TKU_ROWS_CSV = OUT_DIR / "original_tku_inner_sphere_datatable_rows_20260510.csv"
TKU_ROWS_JSON = OUT_DIR / "original_tku_inner_sphere_datatable_rows_20260510.json"
TRACE_JSON = OUT_DIR / "starmap_generation_trace_20260510.json"
CLUSTER_INPUTS_JSON = OUT_DIR / "cluster_migration_inputs.json"
PAWN_PROBE_JSON = OUT_DIR / "ue4_starmap_bounds_clusters_probe.json"

ORIGINAL_TKU_PAK = WORKSPACE / "MW5Mercs" / "Mods" / "TheKnownUniverse" / "Paks" / "TheKnownUniverse.pak"
CURRENT_BASE_GAME_PAK = WORKSPACE / "MW5Mercs" / "Content" / "Paks" / "MW5Mercs-WindowsNoEditor.pak"
MODLIST_JSON = WORKSPACE / "MW5Mercs" / "Mods" / "modlist.json"

OUT_JSON = OUT_DIR / "tku_editor_repair_candidate_manifest_20260510.json"
OUT_MD = OUT_DIR / "tku_editor_repair_candidate_manifest_20260510.md"

sys.path.insert(0, str(TOOLS_ROOT))
from mw5_pak import iter_entries  # noqa: E402


NULL_VALUES = {"", "None", "none", "NULL", "null", "(Id=\"\")"}
ASSET_EXTENSIONS = (".uasset", ".uexp", ".ubulk", ".umap")


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def read_csv_any(path: Path) -> list[dict[str, str]]:
    errors: list[str] = []
    for encoding in ("utf-8-sig", "utf-16", "utf-8"):
        try:
            with path.open("r", encoding=encoding, newline="") as handle:
                reader = csv.DictReader(handle)
                rows = list(reader)
            if reader.fieldnames:
                return rows
        except UnicodeError as exc:
            errors.append(f"{encoding}: {exc}")
    raise RuntimeError(f"could not parse csv {path}: {errors}")


def read_json_rows(path: Path) -> list[dict[str, Any]]:
    data = load_json(path)
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for key in ("rows", "Rows", "data"):
            rows = data.get(key)
            if isinstance(rows, list):
                return rows
    raise RuntimeError(f"unsupported json row container: {path}")


def norm_text(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def norm_cluster(value: Any) -> str:
    text = norm_text(value)
    if text in NULL_VALUES:
        return ""
    match = re.fullmatch(r'\(Id="([^"]*)"\)', text)
    if match:
        text = match.group(1)
    if text.startswith("MWFactionAsset:"):
        text = text.split(":", 1)[1]
    return text


def norm_asset_path(value: Any) -> str:
    text = norm_text(value)
    if text in NULL_VALUES:
        return ""
    return text


def parse_float(value: Any) -> float | None:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if math.isnan(number):
        return None
    return number


def parse_int(value: Any) -> int | None:
    try:
        return int(str(value).strip())
    except (TypeError, ValueError):
        return None


def row_id(row: dict[str, Any]) -> int | None:
    return parse_int(row.get("Name") or row.get("name") or row.get("---") or row.get("row_name"))


def pos_xy(row: dict[str, Any]) -> tuple[float | None, float | None]:
    return parse_float(row.get("PosX") or row.get("pos_x")), parse_float(row.get("PosY") or row.get("pos_y"))


def coord_range(rows: list[dict[str, Any]]) -> dict[str, Any]:
    xs: list[float] = []
    ys: list[float] = []
    for row in rows:
        x, y = pos_xy(row)
        if x is not None and y is not None:
            xs.append(x)
            ys.append(y)
    if not xs or not ys:
        return {"count": 0}
    return {
        "count": len(xs),
        "x": {"min": min(xs), "max": max(xs), "span": max(xs) - min(xs)},
        "y": {"min": min(ys), "max": max(ys), "span": max(ys) - min(ys)},
    }


def projected_level_bounds(rows: list[dict[str, Any]]) -> dict[str, Any]:
    projected: list[dict[str, float]] = []
    for row in rows:
        x, y = pos_xy(row)
        if x is None or y is None:
            continue
        projected.append(
            {
                "level_x": 51336.0 + 8.0 * y,
                "level_y": 51039.0 + 8.0 * x,
            }
        )
    xs = [item["level_x"] for item in projected]
    ys = [item["level_y"] for item in projected]
    if not xs or not ys:
        return {"count": 0}
    return {
        "count": len(projected),
        "x": {
            "min": min(xs),
            "max": max(xs),
            "span": max(xs) - min(xs),
            "center": (min(xs) + max(xs)) / 2.0,
            "half_span": (max(xs) - min(xs)) / 2.0,
        },
        "y": {
            "min": min(ys),
            "max": max(ys),
            "span": max(ys) - min(ys),
            "center": (min(ys) + max(ys)) / 2.0,
            "half_span": (max(ys) - min(ys)) / 2.0,
        },
        "formula": {
            "level_x": "51336 + 8 * PosY",
            "level_y": "51039 + 8 * PosX",
        },
    }


def bounds_from_actor_trace(trace: dict[str, Any]) -> dict[str, Any]:
    bodies = trace.get("current_level", {}).get("star_system_bodies", [])
    xs: list[float] = []
    ys: list[float] = []
    for body in bodies:
        loc = body.get("location") or {}
        x = parse_float(loc.get("x"))
        y = parse_float(loc.get("y"))
        if x is not None and y is not None:
            xs.append(x)
            ys.append(y)
    if not xs or not ys:
        return {"count": 0}
    return {
        "count": len(xs),
        "x": {
            "min": min(xs),
            "max": max(xs),
            "span": max(xs) - min(xs),
            "center": (min(xs) + max(xs)) / 2.0,
            "half_span": (max(xs) - min(xs)) / 2.0,
        },
        "y": {
            "min": min(ys),
            "max": max(ys),
            "span": max(ys) - min(ys),
            "center": (min(ys) + max(ys)) / 2.0,
            "half_span": (max(ys) - min(ys)) / 2.0,
        },
    }


def extract_pawn_defaults(pawn_probe: dict[str, Any]) -> dict[str, Any]:
    for item in pawn_probe.get("blueprints", []):
        if item.get("asset_path") != "/Game/UI/FrontEnd/StarMapPawn":
            continue
        readable = item.get("cdo_properties", {}).get("readable", {})
        return {
            "PanBoundsHorizontal": readable.get("PanBoundsHorizontal") or readable.get("pan_bounds_horizontal"),
            "PanBoundsVertical": readable.get("PanBoundsVertical") or readable.get("pan_bounds_vertical"),
            "ZoomDistanceList": readable.get("ZoomDistanceList"),
            "ZoomLevelThresholds": readable.get("ZoomLevelThresholds"),
        }
    return {}


def id_set(rows: list[dict[str, Any]]) -> set[int]:
    values: set[int] = set()
    for row in rows:
        ident = row_id(row)
        if ident is not None:
            values.add(ident)
    return values


def sample_ints(values: set[int], limit: int = 25) -> list[int]:
    return sorted(values)[:limit]


def compare_ids(left_name: str, left: set[int], right_name: str, right: set[int]) -> dict[str, Any]:
    return {
        "left": left_name,
        "right": right_name,
        f"{left_name}_count": len(left),
        f"{right_name}_count": len(right),
        f"{left_name}_missing_from_{right_name}": len(left - right),
        f"{right_name}_missing_from_{left_name}": len(right - left),
        f"{left_name}_missing_from_{right_name}_sample": sample_ints(left - right),
        f"{right_name}_missing_from_{left_name}_sample": sample_ints(right - left),
    }


def package_from_object_path(asset_path: str) -> str:
    path = asset_path.strip()
    if not path:
        return ""
    slash = path.rfind("/")
    dot = path.find(".", slash + 1)
    if dot != -1:
        return path[:dot]
    return path


def package_to_editor_candidates(package_path: str) -> list[Path]:
    if not package_path.startswith("/Game/"):
        return []
    rel = package_path[len("/Game/") :].replace("/", "\\")
    return [EDITOR_CONTENT / f"{rel}{ext}" for ext in (".uasset", ".umap")]


def summarize_asset_path(path: str, original_tku_game_paths: set[str], base_game_paths: set[str]) -> dict[str, Any]:
    package_path = package_from_object_path(path)
    editor_candidates = package_to_editor_candidates(package_path)
    editor_existing = [str(candidate) for candidate in editor_candidates if candidate.exists()]
    original_tku_existing = sorted(
        f"{package_path}{ext}" for ext in ASSET_EXTENSIONS if f"{package_path}{ext}" in original_tku_game_paths
    )
    base_game_existing = sorted(
        f"{package_path}{ext}" for ext in ASSET_EXTENSIONS if f"{package_path}{ext}" in base_game_paths
    )
    if editor_existing:
        availability = "editor_loose"
    elif base_game_existing:
        availability = "current_base_game_pak"
    elif original_tku_existing:
        availability = "original_tku_pak_only"
    else:
        availability = "missing_from_editor_base_game_and_original_tku_pak"
    return {
        "object_path": path,
        "package_path": package_path,
        "editor_loose_exists": bool(editor_existing),
        "editor_loose_files": editor_existing,
        "current_base_game_pak_exists": bool(base_game_existing),
        "current_base_game_pak_files": base_game_existing,
        "original_tku_pak_exists": bool(original_tku_existing),
        "original_tku_pak_files": original_tku_existing,
        "availability": availability,
    }


def cluster_summary(rows: list[dict[str, Any]]) -> dict[str, Any]:
    by_cluster: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_variant: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)

    for row in rows:
        cluster = norm_cluster(row.get("Cluster"))
        if not cluster:
            continue
        overlay = norm_asset_path(row.get("ClusterOverlay"))
        constellation = norm_asset_path(row.get("ClusterConstellation"))
        by_cluster[cluster].append(row)
        by_variant[(cluster, overlay, constellation)].append(row)

    top_clusters = [
        {"cluster": cluster, "row_count": len(items)}
        for cluster, items in sorted(by_cluster.items(), key=lambda item: (-len(item[1]), item[0]))
    ]

    variants_by_cluster: dict[str, Counter[tuple[str, str]]] = defaultdict(Counter)
    for (cluster, overlay, constellation), items in by_variant.items():
        variants_by_cluster[cluster][(overlay, constellation)] += len(items)

    cluster_details: list[dict[str, Any]] = []
    for cluster in sorted(by_cluster):
        variants = variants_by_cluster[cluster]
        non_empty_variants = [
            (overlay, constellation, count)
            for (overlay, constellation), count in variants.items()
            if overlay or constellation
        ]
        ids = [row_id(row) for row in by_cluster[cluster]]
        ids = [ident for ident in ids if ident is not None]
        detail = {
            "cluster": cluster,
            "row_count": len(by_cluster[cluster]),
            "system_ids_sample": sorted(ids)[:30],
            "variant_count": len(variants),
            "non_empty_overlay_variant_count": len(non_empty_variants),
            "top_variants": [
                {
                    "overlay": overlay or "None",
                    "constellation": constellation or "None",
                    "row_count": count,
                }
                for (overlay, constellation), count in variants.most_common(10)
            ],
            "risk": "normal",
        }
        if cluster in {"RepairSystem", "CareerCluster"}:
            detail["risk"] = "generic_legacy_cluster_id"
        elif len(variants) > 8:
            detail["risk"] = "many_overlay_variants"
        cluster_details.append(detail)

    non_empty_variant_count = sum(1 for (_cluster, overlay, constellation) in by_variant if overlay or constellation)
    return {
        "cluster_row_count": sum(len(items) for items in by_cluster.values()),
        "unique_cluster_ids": len(by_cluster),
        "cluster_asset_count_if_grouped_by_cluster_id": len(by_cluster),
        "cluster_asset_count_if_grouped_by_cluster_overlay_constellation": len(by_variant),
        "non_empty_overlay_constellation_variant_count": non_empty_variant_count,
        "top_clusters": top_clusters[:40],
        "generic_or_high_variant_clusters": [item for item in cluster_details if item["risk"] != "normal"],
        "cluster_details": cluster_details,
    }


def legacy_cluster_mapping(tku_rows: list[dict[str, Any]], current_rows: list[dict[str, Any]]) -> dict[str, Any]:
    current_by_id = {ident: row for row in current_rows if (ident := row_id(row)) is not None}
    mapping: dict[str, Counter[str]] = defaultdict(Counter)
    samples: dict[str, list[dict[str, Any]]] = defaultdict(list)
    missing_current_by_cluster: Counter[str] = Counter()

    for tku_row in tku_rows:
        tku_cluster = norm_cluster(tku_row.get("Cluster"))
        if not tku_cluster:
            continue
        ident = row_id(tku_row)
        current_row = current_by_id.get(ident)
        if current_row is None:
            mapping[tku_cluster]["__no_current_row__"] += 1
            missing_current_by_cluster[tku_cluster] += 1
            continue
        current_cluster = norm_cluster(current_row.get("Cluster")) or "__current_no_cluster__"
        mapping[tku_cluster][current_cluster] += 1
        if len(samples[tku_cluster]) < 12:
            samples[tku_cluster].append(
                {
                    "system_id": ident,
                    "system_name": tku_row.get("StarSystemName"),
                    "tku_cluster": tku_cluster,
                    "current_cluster": current_cluster,
                    "tku_overlay": norm_asset_path(tku_row.get("ClusterOverlay")) or "None",
                    "current_overlay": norm_asset_path(current_row.get("ClusterOverlay")) or "None",
                }
            )

    cluster_maps = []
    for tku_cluster, counter in sorted(mapping.items()):
        top_current = [
            {"current_cluster": cluster, "overlap_count": count}
            for cluster, count in counter.most_common(20)
        ]
        cluster_maps.append(
            {
                "tku_cluster": tku_cluster,
                "matched_or_missing_count": sum(counter.values()),
                "distinct_current_cluster_targets": len(counter),
                "no_current_row_count": counter.get("__no_current_row__", 0),
                "top_current_clusters": top_current,
                "samples": samples.get(tku_cluster, []),
            }
        )

    return {
        "mapped_tku_cluster_count": len(cluster_maps),
        "clusters_with_missing_current_rows": [
            {"tku_cluster": cluster, "missing_current_rows": count}
            for cluster, count in missing_current_by_cluster.most_common()
        ],
        "high_split_clusters": [
            item
            for item in cluster_maps
            if item["distinct_current_cluster_targets"] > 8 or item["tku_cluster"] in {"RepairSystem", "CareerCluster"}
        ],
        "cluster_maps": cluster_maps,
    }


def collect_overlay_paths(rows: list[dict[str, Any]]) -> list[str]:
    paths: set[str] = set()
    for row in rows:
        for key in ("ClusterOverlay", "ClusterConstellation"):
            path = norm_asset_path(row.get(key))
            if path:
                paths.add(path)
    return sorted(paths)


def summarize_modlist() -> dict[str, Any]:
    if not MODLIST_JSON.exists():
        return {"exists": False}
    data = load_json(MODLIST_JSON)
    enabled = sorted(name for name, state in data.get("modStatus", {}).items() if state.get("bEnabled"))
    return {
        "exists": True,
        "gameVersion": data.get("gameVersion"),
        "enabled_mods": enabled,
        "stable_floor_ok": enabled == ["TKUEvidenceCorePluginOnly"],
    }


def pak_inventory(pak_path: Path, label: str) -> dict[str, Any]:
    _footer, mount, entries = iter_entries(pak_path)
    game_paths = {entry.game_path for entry in entries}
    custom_content = sorted(path for path in game_paths if path.startswith("/Game/CustomContent/"))
    campaign_clusters = sorted(path for path in game_paths if path.startswith("/Game/Campaign/Clusters/"))
    dlc1_career_clusters = sorted(path for path in game_paths if path.startswith("/Game/DLC1/CareerMode/Clusters/"))
    dlc1_career_warzones = sorted(path for path in game_paths if path.startswith("/Game/DLC1/CareerMode/Warzones/"))
    campaign_border_meshes = sorted(
        path
        for path in game_paths
        if path.startswith("/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/")
    )
    plugin_war = sorted(
        path
        for path in game_paths
        if path.startswith("/Plugins/TheKnownUniverse/Content/Regions/War/")
        or "ClanConflict" in path
        or "CustomConflict" in path
        or "CareerModeCustomClusters" in path
    )
    return {
        "label": label,
        "path": str(pak_path),
        "mount_point": mount,
        "entry_count": len(entries),
        "game_paths": game_paths,
        "summary": {
            "custom_content_entries": len(custom_content),
            "custom_content_sample": custom_content[:50],
            "campaign_clusters_entries": len(campaign_clusters),
            "campaign_clusters_sample": campaign_clusters[:50],
            "dlc1_career_clusters_entries": len(dlc1_career_clusters),
            "dlc1_career_clusters_sample": dlc1_career_clusters[:50],
            "dlc1_career_warzones_entries": len(dlc1_career_warzones),
            "dlc1_career_warzones_sample": dlc1_career_warzones[:50],
            "campaign_border_meshes_entries": len(campaign_border_meshes),
            "campaign_border_meshes_sample": campaign_border_meshes[:50],
            "plugin_war_entries": len(plugin_war),
            "plugin_war_sample": plugin_war[:80],
        },
    }


def path_availability_summary(paths: list[str], original_tku_game_paths: set[str], base_game_paths: set[str]) -> dict[str, Any]:
    assets = [summarize_asset_path(path, original_tku_game_paths, base_game_paths) for path in paths]
    counter = Counter(item["availability"] for item in assets)
    missing = [item for item in assets if item["availability"] == "missing_from_editor_base_game_and_original_tku_pak"]
    pak_only = [item for item in assets if item["availability"] == "original_tku_pak_only"]
    base_game = [item for item in assets if item["availability"] == "current_base_game_pak"]
    return {
        "unique_overlay_or_constellation_paths": len(paths),
        "availability_counts": dict(sorted(counter.items())),
        "base_game_sample": base_game[:40],
        "pak_only_sample": pak_only[:40],
        "missing_sample": missing[:40],
        "assets": assets,
    }


def extract_current_cluster_asset_factions(cluster_inputs: dict[str, Any]) -> dict[str, Any]:
    assets = cluster_inputs.get("editor_cluster_assets", [])
    names = sorted({item.get("cluster_faction_name") for item in assets if item.get("cluster_faction_name")})
    return {
        "count": len(names),
        "names": names,
        "repair_system_names": [name for name in names if name.startswith("RepairSystem")],
        "career_cluster_names": [name for name in names if name.startswith("CareerCluster")],
    }


def make_manifest() -> dict[str, Any]:
    tku_rows = read_csv_any(TKU_ROWS_CSV)
    tku_parse_summary = load_json(TKU_ROWS_JSON)
    trace = load_json(TRACE_JSON)
    cluster_inputs = load_json(CLUSTER_INPUTS_JSON)
    pawn_probe = load_json(PAWN_PROBE_JSON)

    runtime_csv_path = Path(trace["source_files"]["runtime_csv"]["path"])
    wide_json_path = Path(trace["source_files"]["wide_json"]["path"])
    current_rows = read_csv_any(runtime_csv_path)
    wide_rows = read_json_rows(wide_json_path)

    original_inventory = pak_inventory(ORIGINAL_TKU_PAK, "original_tku")
    base_game_inventory = pak_inventory(CURRENT_BASE_GAME_PAK, "current_base_game")
    original_tku_game_paths = original_inventory["game_paths"]
    base_game_paths = base_game_inventory["game_paths"]

    tku_ids = id_set(tku_rows)
    current_ids = id_set(current_rows)
    wide_ids = id_set(wide_rows)
    tku_bounds = projected_level_bounds(tku_rows)
    current_actor_bounds = bounds_from_actor_trace(trace)
    current_pawn_defaults = extract_pawn_defaults(pawn_probe)

    overlay_paths = collect_overlay_paths(tku_rows)
    overlays = path_availability_summary(overlay_paths, original_tku_game_paths, base_game_paths)
    clusters = cluster_summary(tku_rows)

    current_half_x = current_actor_bounds.get("x", {}).get("half_span")
    current_half_y = current_actor_bounds.get("y", {}).get("half_span")
    target_half_x = tku_bounds.get("x", {}).get("half_span")
    target_half_y = tku_bounds.get("y", {}).get("half_span")

    bounds_ratio = {}
    if current_half_x and target_half_x:
        bounds_ratio["x_half_span_ratio"] = target_half_x / current_half_x
    if current_half_y and target_half_y:
        bounds_ratio["y_half_span_ratio"] = target_half_y / current_half_y

    recommended_bounds_floor = {}
    if target_half_x:
        recommended_bounds_floor["world_x_half_span_plus_1000"] = math.ceil(target_half_x + 1000)
    if target_half_y:
        recommended_bounds_floor["world_y_half_span_plus_1000"] = math.ceil(target_half_y + 1000)

    manifest = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "non_mutating": True,
        "inputs": {
            "workspace": str(WORKSPACE),
            "editor_root": str(EDITOR_ROOT),
            "original_tku_pak": str(ORIGINAL_TKU_PAK),
            "current_base_game_pak": str(CURRENT_BASE_GAME_PAK),
            "original_tku_rows_csv": str(TKU_ROWS_CSV),
            "starmap_generation_trace": str(TRACE_JSON),
            "cluster_inputs": str(CLUSTER_INPUTS_JSON),
        },
        "live_floor": {
            "modlist": summarize_modlist(),
            "build_authorized": False,
            "runtime_pak_authorized": False,
        },
        "data_reconciliation": {
            "current_editor_datatable_rows": trace["data_table"]["row_count"],
            "current_runtime_csv_rows": len(current_rows),
            "wide_source_json_rows": len(wide_rows),
            "original_tku_rows": len(tku_rows),
            "original_tku_parse_summary": tku_parse_summary.get("summary_stats"),
            "id_compare_tku_vs_current_runtime_csv": compare_ids("tku", tku_ids, "current", current_ids),
            "id_compare_tku_vs_wide_source_json": compare_ids("tku", tku_ids, "wide", wide_ids),
            "coordinate_ranges": {
                "current_runtime_csv": coord_range(current_rows),
                "wide_source_json": coord_range(wide_rows),
                "original_tku": coord_range(tku_rows),
            },
        },
        "bounds_candidate": {
            "current_actor_bounds": current_actor_bounds,
            "original_tku_projected_level_bounds": tku_bounds,
            "placement_formula_evidence": trace["placement_join"]["placement_transform_current_csv"],
            "current_pawn_defaults": current_pawn_defaults,
            "bounds_ratio": bounds_ratio,
            "recommended_editor_authored_bounds_floor": recommended_bounds_floor,
            "decision": "Use current StarSystemBody/StarMapPawn classes and editor-authored data/level changes; do not restore old cooked pawn, body, actor, map, or border classes.",
        },
        "territory_candidate": {
            "cluster_summary": clusters,
            "legacy_cluster_mapping_to_current_csv": legacy_cluster_mapping(tku_rows, current_rows),
            "current_editor_cluster_asset_factions": extract_current_cluster_asset_factions(cluster_inputs),
            "overlay_constellation_asset_availability": overlays,
            "original_pak_relevant_inventory": original_inventory["summary"],
            "current_base_game_relevant_inventory": base_game_inventory["summary"],
            "decision": "Modern MWClusterDataAsset overlays must be editor-authored. Original TKU DataTable columns are evidence for membership and mesh references, not a direct cooked replacement.",
        },
        "editor_authoring_gate": {
            "manual_editor_ui_required": True,
            "python_commandlet_create_or_package_supported": False,
            "authorized_next_actions": [
                "Create a dedicated editor mod/project copy through the MW5 Mod Editor UI if one does not already exist.",
                "Import or fill an editor DataTable from the parsed original TKU rows only inside the compatibility mod.",
                "Regenerate or duplicate StarMap level actors using current StarSystemBody_C and the recovered placement formula.",
                "Create MWClusterDataAsset assets with editor-only setters/migration utility after resolving generic legacy cluster IDs.",
                "Save/package only after the authored assets and dependency manifest are reviewed.",
            ],
            "blocked_actions": [
                "Runtime pak build from cooked StarMap assets.",
                "Direct substitution of original root /Game cooked assets.",
                "Direct substitution of old StarMapPawn, StarMapActor, StarSystemBody, StarMap.umap, BaseStarMapBorderActor, or cooked border assets.",
            ],
        },
        "decision": {
            "build_authorized": False,
            "next_repair_candidate": "Editor-authored TKU data/map/cluster ModOverride candidate, prepared in MW5 Mod Editor UI from restored original TKU DataTable evidence.",
            "why_no_build_yet": [
                "Editor Python can inspect mod APIs but commandlet creation/packaging of MW5 mod assets is not proven.",
                "Original TKU cluster IDs contain legacy generic RepairSystem/CareerCluster groups that need editor-side migration policy before asset writes.",
                "Overlay mesh dependencies must be treated as current base-game dependencies where present, and copied/imported only where absent from current content and present in the original TKU pak.",
            ],
        },
    }
    manifest["territory_candidate"]["overlay_constellation_asset_availability_asset_details_path"] = str(OUT_JSON)
    return manifest


def bullet(lines: list[str]) -> str:
    return "\n".join(f"- {line}" for line in lines)


def compact_asset_samples(items: list[dict[str, Any]], limit: int = 8) -> list[dict[str, Any]]:
    return [
        {
            "object_path": item.get("object_path"),
            "package_path": item.get("package_path"),
            "availability": item.get("availability"),
        }
        for item in items[:limit]
    ]


def render_md(manifest: dict[str, Any]) -> str:
    live = manifest["live_floor"]["modlist"]
    data = manifest["data_reconciliation"]
    bounds = manifest["bounds_candidate"]
    territory = manifest["territory_candidate"]
    overlays = territory["overlay_constellation_asset_availability"]
    clusters = territory["cluster_summary"]
    legacy_mapping = territory["legacy_cluster_mapping_to_current_csv"]

    high_risk = clusters["generic_or_high_variant_clusters"][:20]
    top_clusters = clusters["top_clusters"][:20]

    lines: list[str] = []
    lines.append("# TKU Editor Repair Candidate Manifest - 2026-05-10")
    lines.append("")
    lines.append(f"- Generated: `{manifest['generated_utc']}`")
    lines.append("- Method: local read-only reconciliation of editor traces, restored original TKU DataTable parse, and original TKU pak inventory.")
    lines.append("- Safety: no editor assets, original paks, modlist, or runtime paks were modified.")
    lines.append("")
    lines.append("## Live Floor")
    lines.append("")
    lines.append(f"- modlist exists: `{live.get('exists')}`")
    lines.append(f"- game version: `{live.get('gameVersion')}`")
    lines.append(f"- enabled mods: `{live.get('enabled_mods')}`")
    lines.append(f"- stable floor ok: `{live.get('stable_floor_ok')}`")
    lines.append(f"- runtime pak build authorized: `{manifest['live_floor']['runtime_pak_authorized']}`")
    lines.append("")
    lines.append("## Data Reconciliation")
    lines.append("")
    lines.append(f"- Current editor DataTable rows: `{data['current_editor_datatable_rows']}`")
    lines.append(f"- Current runtime CSV rows: `{data['current_runtime_csv_rows']}`")
    lines.append(f"- Wide editor source JSON rows: `{data['wide_source_json_rows']}`")
    lines.append(f"- Restored original TKU DataTable rows: `{data['original_tku_rows']}`")
    lines.append(f"- TKU vs current ID delta: `{data['id_compare_tku_vs_current_runtime_csv']}`")
    lines.append(f"- TKU vs wide source ID delta: `{data['id_compare_tku_vs_wide_source_json']}`")
    lines.append(f"- Coordinate ranges: `{data['coordinate_ranges']}`")
    lines.append("")
    lines.append("## Bounds Candidate")
    lines.append("")
    lines.append(f"- Current actor bounds: `{bounds['current_actor_bounds']}`")
    lines.append(f"- Original TKU projected level bounds: `{bounds['original_tku_projected_level_bounds']}`")
    lines.append(f"- Current pawn defaults: `{bounds['current_pawn_defaults']}`")
    lines.append(f"- Bounds half-span ratio TKU/current: `{bounds['bounds_ratio']}`")
    lines.append(f"- Estimated editor-authored bounds floor: `{bounds['recommended_editor_authored_bounds_floor']}`")
    lines.append(f"- Decision: {bounds['decision']}")
    lines.append("")
    lines.append("## Territory Candidate")
    lines.append("")
    lines.append(f"- TKU clustered rows: `{clusters['cluster_row_count']}`")
    lines.append(f"- Unique TKU cluster IDs: `{clusters['unique_cluster_ids']}`")
    lines.append(f"- Asset count if grouped by cluster ID: `{clusters['cluster_asset_count_if_grouped_by_cluster_id']}`")
    lines.append(f"- Asset count if grouped by cluster/overlay/constellation variant: `{clusters['cluster_asset_count_if_grouped_by_cluster_overlay_constellation']}`")
    lines.append(f"- Non-empty overlay/constellation variants: `{clusters['non_empty_overlay_constellation_variant_count']}`")
    lines.append("")
    lines.append("Top TKU clusters:")
    lines.append(bullet([f"`{item['cluster']}`: `{item['row_count']}`" for item in top_clusters]))
    lines.append("")
    lines.append("Generic or high-variant clusters that require explicit policy:")
    lines.append(bullet([f"`{item['cluster']}` rows `{item['row_count']}`, variants `{item['variant_count']}`, risk `{item['risk']}`" for item in high_risk]))
    lines.append("")
    lines.append("Legacy TKU cluster IDs that split across many current CSV clusters:")
    lines.append(
        bullet(
            [
                f"`{item['tku_cluster']}` targets `{item['distinct_current_cluster_targets']}`, no-current-row `{item['no_current_row_count']}`, top `{item['top_current_clusters'][:8]}`"
                for item in legacy_mapping["high_split_clusters"][:12]
            ]
        )
    )
    lines.append("")
    lines.append("Overlay/constellation availability:")
    lines.append(f"- unique paths: `{overlays['unique_overlay_or_constellation_paths']}`")
    lines.append(f"- availability counts: `{overlays['availability_counts']}`")
    lines.append(f"- current base-game sample: `{compact_asset_samples(overlays['base_game_sample'])}`")
    lines.append(f"- pak-only sample: `{compact_asset_samples(overlays['pak_only_sample'])}`")
    lines.append(f"- missing sample: `{compact_asset_samples(overlays['missing_sample'])}`")
    lines.append("")
    lines.append("Original TKU pak relevant inventory:")
    lines.append(f"- custom content entries: `{territory['original_pak_relevant_inventory']['custom_content_entries']}`")
    lines.append(f"- campaign cluster entries: `{territory['original_pak_relevant_inventory']['campaign_clusters_entries']}`")
    lines.append(f"- DLC1 career cluster entries: `{territory['original_pak_relevant_inventory']['dlc1_career_clusters_entries']}`")
    lines.append(f"- DLC1 career warzone entries: `{territory['original_pak_relevant_inventory']['dlc1_career_warzones_entries']}`")
    lines.append(f"- campaign border mesh entries: `{territory['original_pak_relevant_inventory']['campaign_border_meshes_entries']}`")
    lines.append(f"- plugin war entries: `{territory['original_pak_relevant_inventory']['plugin_war_entries']}`")
    lines.append("")
    lines.append("Current base-game relevant inventory:")
    lines.append(f"- custom content entries: `{territory['current_base_game_relevant_inventory']['custom_content_entries']}`")
    lines.append(f"- campaign cluster entries: `{territory['current_base_game_relevant_inventory']['campaign_clusters_entries']}`")
    lines.append(f"- DLC1 career cluster entries: `{territory['current_base_game_relevant_inventory']['dlc1_career_clusters_entries']}`")
    lines.append(f"- DLC1 career warzone entries: `{territory['current_base_game_relevant_inventory']['dlc1_career_warzones_entries']}`")
    lines.append(f"- campaign border mesh entries: `{territory['current_base_game_relevant_inventory']['campaign_border_meshes_entries']}`")
    lines.append(f"- plugin war entries: `{territory['current_base_game_relevant_inventory']['plugin_war_entries']}`")
    lines.append("")
    lines.append(f"Decision: {territory['decision']}")
    lines.append("")
    lines.append("## Editor Authoring Gate")
    lines.append("")
    lines.append(f"- Manual editor UI required: `{manifest['editor_authoring_gate']['manual_editor_ui_required']}`")
    lines.append(f"- Python commandlet create/package supported: `{manifest['editor_authoring_gate']['python_commandlet_create_or_package_supported']}`")
    lines.append("")
    lines.append("Authorized next actions:")
    lines.append(bullet(manifest["editor_authoring_gate"]["authorized_next_actions"]))
    lines.append("")
    lines.append("Blocked actions:")
    lines.append(bullet(manifest["editor_authoring_gate"]["blocked_actions"]))
    lines.append("")
    lines.append("## Decision")
    lines.append("")
    lines.append(f"- Build authorized: `{manifest['decision']['build_authorized']}`")
    lines.append(f"- Next repair candidate: {manifest['decision']['next_repair_candidate']}")
    lines.append("")
    lines.append("Why no build yet:")
    lines.append(bullet(manifest["decision"]["why_no_build_yet"]))
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    manifest = make_manifest()
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    with OUT_JSON.open("w", encoding="utf-8") as handle:
        json.dump(manifest, handle, indent=2, sort_keys=True)
    OUT_MD.write_text(render_md(manifest), encoding="utf-8")
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()
