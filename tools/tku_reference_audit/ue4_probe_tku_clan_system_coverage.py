from __future__ import annotations

import csv
import inspect
import json
import os
import re
import traceback
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import unreal


REPORT_STEM = "ue4_clan_system_coverage_probe"
DATA_TABLE_ASSET = "/Game/InnerSphereData/MW5_InnerSphereData"
GENERATOR_ASSET = "/Game/InnerSphereData/StarSystemGenerator"
TARGET_MOD_NAME = os.environ.get("TKU_CLAN_COVERAGE_MOD_NAME", "TKUCompatEditorPatch").strip()
CLUSTER_ROOT = "/Game/Campaign/Clusters"
MOD_CLUSTER_ROOT = f"/ModOverride/{TARGET_MOD_NAME}/Campaign/Clusters"
CLUSTER_ROOTS = (CLUSTER_ROOT, MOD_CLUSTER_ROOT)
MAP_ASSET_PATH = os.environ.get("TKU_CLAN_COVERAGE_MAP", "/Game/Levels/FrontEnd/StarMap").strip()
SOURCE_CSV_NAME = "tku_inner_sphere_merged_current_plus_tku_additions_20260510.utf8.csv"

CLAN_TERMS = (
    "clan",
    "clanconflict",
    "repairSystem_clan",
    "cgb_",
    "cjf_",
    "csj_",
    "cwf_",
    "ghost bear",
    "jade falcon",
    "smoke jaguar",
    "wolf",
    "kerensky",
    "strana",
)

TABLE_COLUMNS = (
    "Name",
    "StarSystemName",
    "PosX",
    "PosY",
    "SystemType",
    "SystemStatus",
    "Cluster",
    "ClusterOverlay",
    "ClusterConstellation",
)

STRUCT_PROPERTY_CANDIDATES = (
    "star_system_id",
    "star_system_name",
    "pos_x",
    "pos_y",
    "system_status",
    "cluster",
    "cluster_asset",
    "cluster_asset_id",
    "cluster_data_asset",
    "cluster_data_asset_id",
    "cluster_faction_asset",
    "system_ids",
    "star_system_ids",
    "edges",
)

BODY_PROPERTY_CANDIDATES = (
    "star_system_id",
    "desired_zoom_level",
    "b_should_display_on_starmap",
    "bShouldDisplayOnStarmap",
    "b_is_star_system_hidden",
    "bIsStarSystemHidden",
)

VISIBILITY_METHOD_CANDIDATES = (
    "is_hidden_ed_at_startup",
    "get_star_system_info_by_id",
    "get_star_system_info",
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
SOURCE_CSV = REPORT_DIR / SOURCE_CSV_NAME
OUT_JSON = REPORT_DIR / f"{REPORT_STEM}.json"
OUT_MD = REPORT_DIR / f"{REPORT_STEM}.md"


def text(value: Any) -> str:
    try:
        return str(value)
    except Exception:
        return repr(value)


def path_name(value: Any) -> str:
    try:
        return text(value.get_path_name())
    except Exception:
        return text(value)


def class_name(value: Any) -> str:
    try:
        return text(value.get_class().get_name())
    except Exception:
        return type(value).__name__


def read_prop(value: Any, prop_name: str) -> Any:
    try:
        return value.get_editor_property(prop_name)
    except Exception:
        return None


def read_struct_properties(value: Any, names: tuple[str, ...] = STRUCT_PROPERTY_CANDIDATES) -> dict[str, Any]:
    props: dict[str, Any] = {}
    for name in names:
        prop_value = read_prop(value, name)
        if prop_value is not None:
            props[name] = jsonable(prop_value)
    return props


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
            "sample": [
                {"key": jsonable(key, depth + 1), "value": jsonable(val, depth + 1)}
                for key, val in items[:40]
            ],
        }
    map_items = unreal_map_items(value)
    if map_items is not None:
        return {
            "kind": type(value).__name__,
            "count": len(map_items),
            "sample": [
                {"key": jsonable(key, depth + 1), "value": jsonable(val, depth + 1)}
                for key, val in map_items[:30]
            ],
            "tail_sample": [
                {"key": jsonable(key, depth + 1), "value": jsonable(val, depth + 1)}
                for key, val in map_items[-12:]
            ],
        }
    if isinstance(value, (list, tuple, set)):
        values = list(value)
        return {
            "kind": type(value).__name__,
            "count": len(values),
            "sample": [jsonable(item, depth + 1) for item in values[:40]],
            "tail_sample": [jsonable(item, depth + 1) for item in values[-12:]],
        }
    try:
        if hasattr(value, "__iter__") and not isinstance(value, (str, bytes)):
            values = list(value)
            return {
                "kind": type(value).__name__,
                "count": len(values),
                "sample": [jsonable(item, depth + 1) for item in values[:40]],
                "tail_sample": [jsonable(item, depth + 1) for item in values[-12:]],
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


def unreal_map_keys(value: Any) -> list[Any] | None:
    for attr in ("keys",):
        try:
            keys = list(getattr(value, attr)())
            return keys
        except Exception:
            pass
    try:
        if hasattr(value, "__iter__") and not isinstance(value, (str, bytes, list, tuple, set, dict)):
            return list(value)
    except Exception:
        pass
    return None


def unreal_map_get(value: Any, key: Any) -> Any:
    try:
        return value[key]
    except Exception:
        pass
    try:
        return value.get(key)
    except Exception:
        pass
    return None


def unreal_map_items(value: Any) -> list[tuple[Any, Any]] | None:
    try:
        return list(value.items())
    except Exception:
        pass
    keys = unreal_map_keys(value)
    if keys is None:
        return None
    return [(key, unreal_map_get(value, key)) for key in keys]


def to_int(value: Any) -> int | None:
    if isinstance(value, int):
        return value
    try:
        raw = text(value).strip()
        if re.fullmatch(r"-?\d+", raw):
            return int(raw)
    except Exception:
        pass
    return None


def extract_ints(value: Any, depth: int = 0) -> set[int]:
    if depth > 6:
        return set()
    direct = to_int(value)
    if direct is not None:
        return {direct}
    if value is None or isinstance(value, (float, bool)):
        return set()
    if isinstance(value, str):
        return {int(item) for item in re.findall(r"(?<![\d.-])\d{1,5}(?![\d.])", value)}
    if isinstance(value, dict):
        out: set[int] = set()
        for key, item in value.items():
            out.update(extract_ints(key, depth + 1))
            out.update(extract_ints(item, depth + 1))
        return out
    map_items = unreal_map_items(value)
    if map_items is not None:
        out: set[int] = set()
        for key, item in map_items:
            out.update(extract_ints(key, depth + 1))
            out.update(extract_ints(item, depth + 1))
        return out
    if isinstance(value, (list, tuple, set)):
        out: set[int] = set()
        for item in value:
            out.update(extract_ints(item, depth + 1))
        return out
    try:
        if hasattr(value, "__iter__") and not isinstance(value, (str, bytes)):
            out: set[int] = set()
            for item in list(value):
                out.update(extract_ints(item, depth + 1))
            return out
    except Exception:
        pass
    return extract_ints(text(value), depth + 1)


def method_signature(obj: Any, method_name: str) -> str | None:
    try:
        return str(inspect.signature(getattr(obj, method_name)))
    except Exception:
        return None


def safe_method_call(obj: Any, method_name: str, *args: Any) -> dict[str, Any]:
    try:
        value = getattr(obj, method_name)(*args)
        return {"ok": True, "value": jsonable(value)}
    except Exception as exc:
        return {"ok": False, "error": f"{type(exc).__name__}: {exc}"}


def star_system_info_summary(value: Any) -> dict[str, Any]:
    props = read_struct_properties(
        value,
        ("star_system_id", "star_system_name", "pos_x", "pos_y", "system_status", "star_map_stencil_id"),
    )
    if props:
        return props
    raw = text(value)
    item: dict[str, Any] = {"repr": raw[:900], "python_type": type(value).__name__}
    match = re.search(
        r"star_system_id:\s*(?P<id>\d+).*?star_system_name:\s*\"(?P<name>[^\"]*)\".*?pos_x:\s*(?P<x>-?[\d.]+).*?pos_y:\s*(?P<y>-?[\d.]+)",
        raw,
        re.DOTALL,
    )
    if match:
        item.update(
            {
                "star_system_id": int(match.group("id")),
                "star_system_name": match.group("name"),
                "pos_x": float(match.group("x")),
                "pos_y": float(match.group("y")),
            }
        )
    return item


def row_matches_clan(row: dict[str, str]) -> bool:
    combined = " ".join(str(value) for value in row.values()).lower()
    return any(term.lower() in combined for term in CLAN_TERMS)


def load_source_rows() -> dict[str, Any]:
    out: dict[str, Any] = {"path": str(SOURCE_CSV), "exists": SOURCE_CSV.is_file()}
    if not SOURCE_CSV.is_file():
        return out
    with SOURCE_CSV.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    clan_rows = [row for row in rows if row_matches_clan(row)]
    out["row_count"] = len(rows)
    out["clan_candidate_count"] = len(clan_rows)
    out["clan_candidate_ids"] = [int(row["Name"]) for row in clan_rows if row.get("Name", "").isdigit()]
    out["clan_candidate_sample"] = clan_rows[:80]
    out["cluster_counts"] = dict(Counter(row.get("Cluster", "") for row in clan_rows).most_common())
    return out


def load_data_table_rows() -> dict[str, Any]:
    out: dict[str, Any] = {"asset_path": DATA_TABLE_ASSET}
    asset = unreal.EditorAssetLibrary.load_asset(DATA_TABLE_ASSET)
    out["loaded"] = bool(asset)
    out["object_path"] = path_name(asset)
    out["class"] = class_name(asset)
    if not asset:
        return out
    try:
        out["row_struct"] = path_name(asset.get_editor_property("row_struct"))
    except Exception as exc:
        out["row_struct_error"] = f"{type(exc).__name__}: {exc}"
    row_names = [str(row) for row in unreal.DataTableFunctionLibrary.get_data_table_row_names(asset)]
    out["row_count"] = len(row_names)
    out["tail_rows"] = row_names[-30:]
    columns: dict[str, list[str]] = {}
    column_errors: dict[str, str] = {}
    for column in TABLE_COLUMNS:
        try:
            values = list(unreal.DataTableFunctionLibrary.get_data_table_column_as_string(asset, column))
            columns[column] = [text(value) for value in values]
        except Exception as exc:
            column_errors[column] = f"{type(exc).__name__}: {exc}"
    rows: list[dict[str, str]] = []
    for idx, row_name in enumerate(row_names):
        item: dict[str, str] = {"row_name": row_name}
        for column, values in columns.items():
            if idx < len(values):
                item[column] = values[idx]
        rows.append(item)
    clan_rows = [row for row in rows if row_matches_clan(row)]
    out["column_lengths"] = {column: len(values) for column, values in columns.items()}
    out["column_errors"] = column_errors
    out["clan_candidate_count"] = len(clan_rows)
    out["clan_candidate_ids"] = [
        int(row["row_name"])
        for row in clan_rows
        if row.get("row_name", "").isdigit()
    ]
    out["clan_candidate_sample"] = clan_rows[:80]
    return out


def generator_cdo() -> tuple[Any | None, dict[str, Any]]:
    info: dict[str, Any] = {"asset_path": GENERATOR_ASSET}
    asset = unreal.EditorAssetLibrary.load_asset(GENERATOR_ASSET)
    info["asset"] = jsonable(asset)
    try:
        cls = unreal.EditorAssetLibrary.load_blueprint_class(GENERATOR_ASSET)
        info["blueprint_class"] = jsonable(cls)
        if cls:
            cdo = unreal.get_default_object(cls)
            info["cdo"] = jsonable(cdo)
            return cdo, info
    except Exception as exc:
        info["error"] = f"{type(exc).__name__}: {exc}"
    return None, info


def call_generator(cdo: Any, method_name: str) -> dict[str, Any]:
    try:
        value = getattr(cdo, method_name)()
        items = unreal_map_items(value)
        keys = [key for key, _item in items] if items is not None else unreal_map_keys(value)
        return {
            "ok": True,
            "shape": {
                "type": type(value).__name__,
                "count": len(keys) if keys is not None else None,
                "sample_keys": [jsonable(key) for key in (keys or [])[:20]],
                "tail_keys": [jsonable(key) for key in (keys or [])[-20:]],
                "sample_items": [
                    {"key": jsonable(key), "value": jsonable(item)}
                    for key, item in (items or [])[:12]
                ],
                "tail_items": [
                    {"key": jsonable(key), "value": jsonable(item)}
                    for key, item in (items or [])[-8:]
                ],
            },
            "value": value,
        }
    except Exception as exc:
        return {"ok": False, "error": f"{type(exc).__name__}: {exc}"}


def map_key_ints(value: Any) -> set[int]:
    keys = unreal_map_keys(value) or []
    return {item for item in (to_int(key) for key in keys) if item is not None}


def inspect_generator(candidate_ids: list[int]) -> dict[str, Any]:
    cdo, info = generator_cdo()
    out: dict[str, Any] = {"cdo_info": info, "calls": {}, "coverage": {}}
    if cdo is None:
        return out
    calls = {
        name: call_generator(cdo, name)
        for name in (
            "generate_inner_sphere_data",
            "retrieve_star_system_edges",
            "retrieve_edge_index_list",
            "retrieve_star_system_clusters",
        )
    }
    out["calls"] = {name: {key: value for key, value in result.items() if key != "value"} for name, result in calls.items()}

    generated_value = calls["generate_inner_sphere_data"].get("value")
    edges_value = calls["retrieve_star_system_edges"].get("value")
    clusters_value = calls["retrieve_star_system_clusters"].get("value")
    generated_keys = map_key_ints(generated_value)
    edge_keys = map_key_ints(edges_value)

    edge_mentions: dict[int, int] = {system_id: 0 for system_id in candidate_ids}
    for key, value in unreal_map_items(edges_value) or []:
        ints = extract_ints(key) | extract_ints(value)
        for system_id in candidate_ids:
            if system_id in ints:
                edge_mentions[system_id] += 1

    cluster_memberships: dict[int, list[str]] = {system_id: [] for system_id in candidate_ids}
    clan_cluster_keys: list[str] = []
    for key, value in unreal_map_items(clusters_value) or []:
        key_text = text(key)
        if "clan" in key_text.lower() or any(prefix in key_text for prefix in ("CGB_", "CJF_", "CSJ_", "CWF_")):
            clan_cluster_keys.append(key_text)
        ints = extract_ints(value)
        for system_id in candidate_ids:
            if system_id in ints:
                cluster_memberships[system_id].append(key_text)

    out["clan_cluster_keys"] = clan_cluster_keys[:120]
    out["visibility_methods"] = inspect_visibility_methods(cdo, candidate_ids)
    for system_id in candidate_ids:
        generated_item = None
        if generated_value is not None and system_id in generated_keys:
            generated_item = unreal_map_get(generated_value, system_id)
        out["coverage"][str(system_id)] = {
            "generated_present": system_id in generated_keys,
            "generated_info": star_system_info_summary(generated_item),
            "edge_key_present": system_id in edge_keys,
            "edge_mention_count": edge_mentions.get(system_id, 0),
            "cluster_memberships": cluster_memberships.get(system_id, []),
        }
    return out


def inspect_visibility_methods(obj: Any, candidate_ids: list[int]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    sample_ids = candidate_ids[:8] + [system_id for system_id in (4110, 4120, 4132, 4143, 6979) if system_id in candidate_ids]
    sample_ids = list(dict.fromkeys(sample_ids))
    for method_name in VISIBILITY_METHOD_CANDIDATES:
        if not hasattr(obj, method_name):
            continue
        method: dict[str, Any] = {"signature": method_signature(obj, method_name)}
        method["no_arg"] = safe_method_call(obj, method_name)
        method["by_id"] = {
            str(system_id): safe_method_call(obj, method_name, system_id)
            for system_id in sample_ids
        }
        out[method_name] = method
    return out


def inspect_cluster_assets(candidate_ids: list[int]) -> dict[str, Any]:
    out: dict[str, Any] = {"roots": list(CLUSTER_ROOTS), "root_results": {}}
    candidate_set = set(candidate_ids)
    paths: list[str] = []
    for root in CLUSTER_ROOTS:
        try:
            root_paths = sorted(set(path.split(".", 1)[0] for path in unreal.EditorAssetLibrary.list_assets(root, True, False)))
            out["root_results"][root] = {"ok": True, "asset_path_count": len(root_paths)}
            paths.extend(root_paths)
        except Exception as exc:
            out["root_results"][root] = {"ok": False, "error": f"{type(exc).__name__}: {exc}"}
    paths = sorted(set(paths))
    rows: list[dict[str, Any]] = []
    memberships: dict[int, list[str]] = {system_id: [] for system_id in candidate_ids}
    for asset_path in paths:
        try:
            data = unreal.EditorAssetLibrary.find_asset_data(asset_path)
            if text(data.asset_class) != "MWClusterDataAsset":
                continue
            asset = unreal.EditorAssetLibrary.load_asset(asset_path)
            ids_raw = read_prop(asset, "system_ids") or []
            ids = sorted(item for item in (to_int(value) for value in ids_raw) if item is not None)
            row = {
                "asset_path": asset_path,
                "system_count": len(ids),
                "candidate_system_ids": sorted(candidate_set.intersection(ids)),
                "cluster_faction_asset": jsonable(read_prop(asset, "cluster_faction_asset")),
                "cluster_overlay": jsonable(read_prop(asset, "cluster_overlay")),
                "cluster_constellation": jsonable(read_prop(asset, "cluster_constellation")),
                "is_legacy_cluster": jsonable(read_prop(asset, "is_legacy_cluster")),
                "system_ids_sample": ids[:40],
            }
            rows.append(row)
            for system_id in candidate_set.intersection(ids):
                memberships[system_id].append(asset_path)
        except Exception as exc:
            rows.append({"asset_path": asset_path, "error": f"{type(exc).__name__}: {exc}"})
    out["asset_count"] = len(rows)
    out["total_system_memberships"] = sum(row.get("system_count", 0) for row in rows)
    out["with_overlay"] = sum(1 for row in rows if row.get("cluster_overlay"))
    out["with_constellation"] = sum(1 for row in rows if row.get("cluster_constellation"))
    out["candidate_memberships"] = {str(system_id): paths for system_id, paths in memberships.items()}
    out["candidate_assets"] = [row for row in rows if row.get("candidate_system_ids")]
    out["clan_named_assets"] = [
        row
        for row in rows
        if "clan" in row.get("asset_path", "").lower()
        or any(prefix in text(row.get("cluster_faction_asset")) for prefix in ("CGB_", "CJF_", "CSJ_", "CWF_"))
    ]
    out["asset_sample"] = rows[:120]
    return out


def actor_star_system_id(actor: Any) -> int | None:
    for prop in ("star_system_id", "StarSystemId", "star_system_ID"):
        try:
            value = actor.get_editor_property(prop)
            parsed = to_int(value)
            if parsed is not None:
                return parsed
        except Exception:
            continue
    return None


def inspect_level(candidate_ids: list[int]) -> dict[str, Any]:
    out: dict[str, Any] = {"map_asset_path": MAP_ASSET_PATH}
    try:
        out["load_map"] = jsonable(unreal.EditorLoadingAndSavingUtils.load_map(MAP_ASSET_PATH))
    except Exception as exc:
        out["load_error"] = f"{type(exc).__name__}: {exc}"
        return out
    actors = list(unreal.EditorLevelLibrary.get_all_level_actors())
    body_ids: list[int] = []
    body_samples: list[dict[str, Any]] = []
    for actor in actors:
        label = ""
        try:
            label = text(actor.get_actor_label())
        except Exception:
            label = text(actor)
        if "starsystembody" not in f"{class_name(actor)} {label}".lower():
            continue
        system_id = actor_star_system_id(actor)
        if system_id is not None:
            body_ids.append(system_id)
        if system_id in candidate_ids:
            body_samples.append(
                {
                    "label": label,
                    "class": class_name(actor),
                    "path": path_name(actor),
                    "star_system_id": system_id,
                    "location": jsonable(actor.get_actor_location()),
                    "properties": read_struct_properties(actor, BODY_PROPERTY_CANDIDATES),
                }
            )
    body_id_set = set(body_ids)
    out["actor_count"] = len(actors)
    out["star_system_body_count"] = len(body_ids)
    out["star_system_body_id_range"] = {
        "min": min(body_ids) if body_ids else None,
        "max": max(body_ids) if body_ids else None,
    }
    out["candidate_body_presence"] = {str(system_id): system_id in body_id_set for system_id in candidate_ids}
    out["candidate_body_samples"] = body_samples[:80]
    return out


def candidate_ids_from(report: dict[str, Any]) -> list[int]:
    ids: set[int] = set()
    for section in ("source_csv", "data_table"):
        ids.update(report.get(section, {}).get("clan_candidate_ids") or [])
    return sorted(ids)


def summarize(report: dict[str, Any]) -> list[str]:
    findings: list[str] = []
    source = report.get("source_csv", {})
    table = report.get("data_table", {})
    generator = report.get("generator", {})
    clusters = report.get("cluster_assets", {})
    level = report.get("level", {})
    ids = report.get("candidate_ids", [])
    findings.append(
        f"Source CSV clan candidate rows: {source.get('clan_candidate_count')} "
        f"(id range {min(ids) if ids else None}..{max(ids) if ids else None})."
    )
    findings.append(
        f"Editor DataTable rows: {table.get('row_count')}; DataTable clan candidate rows: {table.get('clan_candidate_count')}."
    )
    calls = generator.get("calls", {})
    for name, result in calls.items():
        shape = result.get("shape") or {}
        findings.append(f"StarSystemGenerator.{name} -> ok={result.get('ok')} count={shape.get('count')}.")
    coverage = generator.get("coverage", {})
    if coverage:
        generated_missing = [system_id for system_id, item in coverage.items() if not item.get("generated_present")]
        edge_missing = [
            system_id
            for system_id, item in coverage.items()
            if not item.get("edge_key_present") and not item.get("edge_mention_count")
        ]
        cluster_missing = [system_id for system_id, item in coverage.items() if not item.get("cluster_memberships")]
        findings.append(f"Clan candidates missing from generated map: {len(generated_missing)}.")
        findings.append(f"Clan candidates with no edge evidence: {len(edge_missing)}.")
        findings.append(f"Clan candidates with no cluster membership evidence: {len(cluster_missing)}.")
    if clusters:
        candidate_memberships = clusters.get("candidate_memberships") or {}
        missing_cluster_assets = [system_id for system_id, paths in candidate_memberships.items() if not paths]
        findings.append(
            f"Current MWClusterDataAsset count: {clusters.get('asset_count')} "
            f"(candidate IDs missing from cluster assets: {len(missing_cluster_assets)})."
        )
    if level:
        presence = level.get("candidate_body_presence") or {}
        missing_bodies = [system_id for system_id, present in presence.items() if not present]
        findings.append(
            f"StarMap level StarSystemBody actors: {level.get('star_system_body_count')} "
            f"(candidate bodies missing: {len(missing_bodies)})."
        )
    return findings


def write_markdown(report: dict[str, Any]) -> None:
    lines = [
        "# UE4 Clan System Coverage Probe",
        "",
        f"- Generated: `{report['generated_utc']}`",
        f"- DataTable: `{DATA_TABLE_ASSET}`",
        f"- Generator: `{GENERATOR_ASSET}`",
        f"- Map: `{MAP_ASSET_PATH}`",
        "- Safety: read-only commandlet; no assets saved.",
        "",
        "## Findings",
        "",
    ]
    for finding in report.get("findings", []):
        lines.append(f"- {finding}")

    ids = report.get("candidate_ids", [])
    lines.extend(["", "## Candidate IDs", ""])
    lines.append(f"- Count: `{len(ids)}`")
    lines.append(f"- IDs: `{ids}`")

    source = report.get("source_csv", {})
    lines.extend(["", "## Source CSV", ""])
    lines.append(f"- Path: `{source.get('path')}`")
    lines.append(f"- Rows: `{source.get('row_count')}`")
    lines.append(f"- Clan candidate rows: `{source.get('clan_candidate_count')}`")
    lines.append(f"- Clan cluster counts: `{source.get('cluster_counts')}`")
    for row in source.get("clan_candidate_sample", [])[:50]:
        lines.append(f"- `{row}`")

    table = report.get("data_table", {})
    lines.extend(["", "## DataTable", ""])
    for key in ("object_path", "class", "row_struct", "row_count", "column_lengths", "column_errors", "tail_rows"):
        lines.append(f"- `{key}`: `{table.get(key)}`")
    for row in table.get("clan_candidate_sample", [])[:50]:
        lines.append(f"- `{row}`")

    generator = report.get("generator", {})
    lines.extend(["", "## Generator Calls", ""])
    for name, result in (generator.get("calls") or {}).items():
        lines.append(f"### `{name}`")
        lines.append(f"- ok: `{result.get('ok')}`")
        if result.get("error"):
            lines.append(f"- error: `{result.get('error')}`")
        shape = result.get("shape") or {}
        lines.append(f"- shape: `{shape}`")

    lines.extend(["", "## Generator Visibility Methods", ""])
    for method_name, result in (generator.get("visibility_methods") or {}).items():
        lines.append(f"### `{method_name}`")
        lines.append(f"- signature: `{result.get('signature')}`")
        lines.append(f"- no_arg: `{result.get('no_arg')}`")
        lines.append(f"- by_id: `{result.get('by_id')}`")

    lines.extend(["", "## Generator Coverage", ""])
    for system_id, item in (generator.get("coverage") or {}).items():
        lines.append(f"### `{system_id}`")
        lines.append(f"- generated_present: `{item.get('generated_present')}`")
        lines.append(f"- edge_key_present: `{item.get('edge_key_present')}`")
        lines.append(f"- edge_mention_count: `{item.get('edge_mention_count')}`")
        lines.append(f"- cluster_memberships: `{item.get('cluster_memberships')}`")
        lines.append(f"- generated_info: `{item.get('generated_info')}`")

    clusters = report.get("cluster_assets", {})
    lines.extend(["", "## Current Cluster Assets", ""])
    lines.append(f"- roots: `{clusters.get('roots')}`")
    lines.append(f"- root_results: `{clusters.get('root_results')}`")
    for key in (
        "asset_count",
        "total_system_memberships",
        "with_overlay",
        "with_constellation",
    ):
        lines.append(f"- `{key}`: `{clusters.get(key)}`")
    lines.append(f"- candidate_memberships: `{clusters.get('candidate_memberships')}`")
    lines.append(f"- candidate_assets: `{clusters.get('candidate_assets')}`")
    for item in clusters.get("clan_named_assets", [])[:80]:
        lines.append(f"- clan-named asset: `{item}`")

    level = report.get("level", {})
    lines.extend(["", "## StarMap Level", ""])
    for key in ("load_map", "load_error", "actor_count", "star_system_body_count", "star_system_body_id_range"):
        lines.append(f"- `{key}`: `{level.get(key)}`")
    lines.append(f"- candidate_body_presence: `{level.get('candidate_body_presence')}`")
    for item in level.get("candidate_body_samples", [])[:80]:
        lines.append(f"- `{item}`")

    if report.get("errors"):
        lines.extend(["", "## Errors", ""])
        for error in report["errors"]:
            lines.append(f"- `{error}`")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "source_csv": {},
        "data_table": {},
        "candidate_ids": [],
        "generator": {},
        "cluster_assets": {},
        "level": {},
        "errors": [],
    }
    try:
        report["source_csv"] = load_source_rows()
    except Exception:
        report["errors"].append({"source_csv": traceback.format_exc()})
    try:
        report["data_table"] = load_data_table_rows()
    except Exception:
        report["errors"].append({"data_table": traceback.format_exc()})
    report["candidate_ids"] = candidate_ids_from(report)
    try:
        report["generator"] = inspect_generator(report["candidate_ids"])
    except Exception:
        report["errors"].append({"generator": traceback.format_exc()})
    try:
        report["cluster_assets"] = inspect_cluster_assets(report["candidate_ids"])
    except Exception:
        report["errors"].append({"cluster_assets": traceback.format_exc()})
    try:
        report["level"] = inspect_level(report["candidate_ids"])
    except Exception:
        report["errors"].append({"level": traceback.format_exc()})
    report["findings"] = summarize(report)
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True, default=str), encoding="utf-8")
    write_markdown(report)
    unreal.log(f"TKU clan system coverage probe wrote {OUT_JSON}")


main()
