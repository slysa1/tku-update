from __future__ import annotations

import csv
import json
import math
import re
import traceback
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import unreal


from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
EDITOR_ROOT = Path(r"E:\Games\MechWarrior5Editor")
PROJECT_CONTENT = EDITOR_ROOT / "MW5Mercs" / "Content"
OUT_DIR = REPORTS_DIR / "tku_editor_first"
OUT_JSON = OUT_DIR / "starmap_generation_trace_20260510.json"
OUT_MD = OUT_DIR / "starmap_generation_trace_20260510.md"

STARMAP_LEVEL = "/Game/Levels/FrontEnd/StarMap"
CURRENT_DATA_TABLE = "/Game/InnerSphereData/MW5_InnerSphereData"
RUNTIME_CSV = PROJECT_CONTENT / "InnerSphereData" / "MW5_InnerSphereData.csv"
WIDE_JSON = PROJECT_CONTENT / "Data" / "InnerSphereMap" / "MW5_InnerSphereData.json"

ASSET_PATHS = (
    "/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets",
    "/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction",
    "/Game/Campaign/CampaignArcActions/MissionActions/MissionConfigs/PlaceClusterToi_Config",
    "/Game/Campaign/CampaignArcActions/MissionActions/MissionConfigs/PlaceClusterToi_Markups",
    "/Game/Campaign/_common/ClusterToiDataFragment",
    "/Game/InnerSphereData/StarSystemGenerator",
    "/Game/InnerSphereData/StarMapBP_UTILS",
    CURRENT_DATA_TABLE,
    STARMAP_LEVEL,
    "/Game/UI/FrontEnd/Starmap/StarMapActor",
    "/Game/UI/FrontEnd/Starmap/StarSystemBody",
    "/Game/UI/FrontEnd/StarMapPawn",
)

SEARCH_ROOTS = (
    "/Game/UI/Editor",
    "/Game/InnerSphereData",
    "/Game/UI/FrontEnd/Starmap",
    "/Game/UI/FrontEnd",
    "/Game/Campaign/Clusters",
)

KEYWORDS = (
    "Cluster",
    "ClusterDataAsset",
    "DataAsset",
    "InnerSphere",
    "MW5_InnerSphereData",
    "DataTable",
    "StarSystem",
    "StarSystemBody",
    "StarSystemGenerator",
    "StarMap",
    "Border",
    "Overlay",
    "Constellation",
    "Faction",
    "PlaceCluster",
    "TOI",
    "CreateAsset",
    "Duplicate",
    "Save",
    "SetCluster",
    "SystemIds",
    "SpawnActor",
    "Generate",
    "PosX",
    "PosY",
    "PanBounds",
    "Zoom",
)

DATA_TABLE_COLUMNS = (
    "Name",
    "StarSystemName",
    "PosX",
    "PosY",
    "Cluster",
    "ClusterOverlay",
    "ClusterConstellation",
)


def text(value) -> str:
    try:
        return str(value)
    except Exception:
        return repr(value)


def to_jsonable(value, depth: int = 0):
    if depth > 6:
        return text(value)
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Path):
        return str(value)
    if hasattr(value, "x") and hasattr(value, "y") and hasattr(value, "z"):
        return {"x": float(value.x), "y": float(value.y), "z": float(value.z)}
    if isinstance(value, dict):
        return {text(k): to_jsonable(v, depth + 1) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [to_jsonable(item, depth + 1) for item in value]
    try:
        if hasattr(value, "__iter__") and not isinstance(value, (str, bytes)):
            return [to_jsonable(item, depth + 1) for item in list(value)]
    except Exception:
        pass
    out = {"repr": text(value), "python_type": type(value).__name__}
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


def safe(label: str, func, *args):
    try:
        return {"ok": True, "value": to_jsonable(func(*args))}
    except Exception as exc:
        return {"ok": False, "error": f"{type(exc).__name__}: {exc}"}


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


def read_prop(obj, prop: str):
    try:
        return to_jsonable(obj.get_editor_property(prop))
    except Exception:
        return None


def dependency_options():
    return unreal.AssetRegistryDependencyOptions(True, True, True, True, True)


def asset_refs(asset_path: str) -> dict:
    out = {}
    try:
        reg = unreal.AssetRegistryHelpers.get_asset_registry()
        opts = dependency_options()
        for method in ("get_dependencies", "get_referencers"):
            try:
                out[method] = sorted(text(item) for item in (getattr(reg, method)(asset_path, opts) or []))
            except Exception as exc:
                out[method] = {"error": f"{type(exc).__name__}: {exc}"}
    except Exception as exc:
        out["error"] = f"{type(exc).__name__}: {exc}"
    return out


def package_to_disk(asset_path: str) -> Path | None:
    if not asset_path.startswith("/Game/"):
        return None
    rel = asset_path[len("/Game/") :]
    suffix = ".umap" if "/Levels/" in asset_path else ".uasset"
    return PROJECT_CONTENT / (rel + suffix)


def decode_fib(value: str) -> str:
    # Asset registry FiBData stores searchable Blueprint text shifted by +1.
    chars = []
    for ch in value:
        code = ord(ch)
        if code > 1:
            chars.append(chr(code - 1))
        else:
            chars.append(ch)
    return "".join(chars)


TOKEN_RE = re.compile(r"[A-Za-z0-9_./:'\[\]\(\)# -]{3,}")


def unique_ordered(items: list[str], limit: int = 300) -> list[str]:
    seen = set()
    out = []
    for item in items:
        cleaned = " ".join(item.split())
        if not cleaned or cleaned in seen:
            continue
        seen.add(cleaned)
        out.append(cleaned)
        if len(out) >= limit:
            break
    return out


def interesting_tokens(raw_text: str, limit: int = 300) -> list[str]:
    tokens = TOKEN_RE.findall(raw_text)
    focused = [
        token
        for token in tokens
        if any(keyword.lower() in token.lower() for keyword in KEYWORDS)
    ]
    return unique_ordered(focused, limit)


def raw_package_strings(asset_path: str) -> dict:
    path = package_to_disk(asset_path)
    out = {"path": str(path) if path else None, "exists": bool(path and path.exists())}
    if not path or not path.exists():
        return out
    try:
        data = path.read_bytes()
    except Exception as exc:
        out["error"] = f"{type(exc).__name__}: {exc}"
        return out
    ascii_strings = [match.decode("ascii", "ignore") for match in re.findall(rb"[\x20-\x7e]{4,}", data)]
    utf16_strings = [
        match.decode("utf-16le", "ignore")
        for match in re.findall(rb"(?:[\x20-\x7e]\x00){4,}", data)
    ]
    combined = unique_ordered(ascii_strings + utf16_strings, 10000)
    focused = [
        item for item in combined
        if any(keyword.lower() in item.lower() for keyword in KEYWORDS)
    ]
    out["string_count"] = len(combined)
    out["focused_strings"] = focused[:250]
    return out


def asset_tag_trace(asset_path: str) -> dict:
    out = {"asset_path": asset_path}
    out["references"] = asset_refs(asset_path)
    if asset_path == STARMAP_LEVEL:
        out["asset_data"] = {
            "asset_class": "World/Map",
            "note": "Map assets are inspected by EditorLoadingAndSavingUtils and raw package scanning, not EditorAssetLibrary.",
        }
    else:
        out["exists"] = safe("does_asset_exist", unreal.EditorAssetLibrary.does_asset_exist, asset_path)
        try:
            data = unreal.EditorAssetLibrary.find_asset_data(asset_path)
            out["asset_data"] = {
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
            out["asset_data_error"] = f"{type(exc).__name__}: {exc}"
        try:
            raw = unreal.EditorAssetLibrary.get_tag_values(asset_path)
            out["tag_keys"] = sorted(text(key) for key in raw.keys())
            selected = {}
            for key, value in raw.items():
                key_text = text(key)
                value_text = text(value)
                if key_text == "FiBData":
                    decoded = decode_fib(value_text)
                    selected["FiBData"] = {
                        "raw_length": len(value_text),
                        "decoded_focused_tokens": interesting_tokens(decoded, 400),
                    }
                elif key_text in ("GeneratedClass", "ParentClass", "NativeParentClass", "BlueprintType", "IsDataOnly"):
                    selected[key_text] = value_text
            out["selected_tags"] = selected
        except Exception as exc:
            out["tags_error"] = f"{type(exc).__name__}: {exc}"
    out["raw_package_strings"] = raw_package_strings(asset_path)
    return out


def discover_focus_assets() -> dict:
    out = {}
    for root in SEARCH_ROOTS:
        item = {"root": root}
        try:
            if not unreal.EditorAssetLibrary.does_directory_exist(root):
                item["exists"] = False
            else:
                assets = list(unreal.EditorAssetLibrary.list_assets(root, recursive=True, include_folder=False))
                matches = [
                    asset for asset in assets
                    if any(keyword.lower() in asset.lower() for keyword in KEYWORDS)
                ]
                item["exists"] = True
                item["asset_count"] = len(assets)
                item["matches"] = sorted(matches)[:500]
        except Exception as exc:
            item["error"] = f"{type(exc).__name__}: {exc}"
        out[root] = item
    return out


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-16", newline="") as handle:
        return list(csv.DictReader(handle))


def load_wide_json_rows(path: Path) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def row_id(row: dict) -> int | None:
    for key in ("---", "Name"):
        try:
            return int(str(row.get(key)))
        except Exception:
            pass
    return None


def float_field(row: dict, key: str) -> float | None:
    try:
        value = float(row.get(key))
    except Exception:
        return None
    return value if math.isfinite(value) else None


def range_2d(rows: list[dict], x_key: str = "PosX", y_key: str = "PosY") -> dict:
    points = []
    for row in rows:
        x = float_field(row, x_key)
        y = float_field(row, y_key)
        if x is not None and y is not None:
            points.append((x, y))
    if not points:
        return {"count": 0}
    xs = [x for x, _ in points]
    ys = [y for _, y in points]
    return {
        "count": len(points),
        "x": {"min": min(xs), "max": max(xs), "span": max(xs) - min(xs)},
        "y": {"min": min(ys), "max": max(ys), "span": max(ys) - min(ys)},
    }


def data_table_probe() -> dict:
    out = {"asset_path": CURRENT_DATA_TABLE}
    asset = None
    try:
        asset = unreal.EditorAssetLibrary.load_asset(CURRENT_DATA_TABLE)
        out["asset_class"] = get_class_name(asset)
        out["row_struct"] = get_path_name(asset.get_editor_property("row_struct"))
    except Exception as exc:
        out["load_error"] = f"{type(exc).__name__}: {exc}"
        return out
    try:
        rows = [text(row) for row in unreal.DataTableFunctionLibrary.get_data_table_row_names(asset)]
        out["row_count"] = len(rows)
        out["row_sample"] = rows[:20]
        out["row_tail_sample"] = rows[-20:]
    except Exception as exc:
        out["row_error"] = f"{type(exc).__name__}: {exc}"
    columns = {}
    for column in DATA_TABLE_COLUMNS:
        try:
            values = [text(value) for value in unreal.DataTableFunctionLibrary.get_data_table_column_as_string(asset, unreal.Name(column))]
            columns[column] = {
                "ok": True,
                "count": len(values),
                "sample": values[:10],
                "tail_sample": values[-10:],
            }
            if column in ("PosX", "PosY"):
                nums = []
                for value in values:
                    try:
                        nums.append(float(value))
                    except Exception:
                        pass
                if nums:
                    columns[column]["range"] = {"min": min(nums), "max": max(nums), "span": max(nums) - min(nums)}
            if column in ("Cluster", "ClusterOverlay", "ClusterConstellation"):
                columns[column]["non_empty_count"] = sum(
                    1 for value in values if value not in ("", "None", '(Id="")')
                )
        except Exception as exc:
            columns[column] = {"ok": False, "error": f"{type(exc).__name__}: {exc}"}
    out["columns"] = columns
    return out


def source_file_probe() -> dict:
    out = {
        "runtime_csv": {"path": str(RUNTIME_CSV), "exists": RUNTIME_CSV.exists()},
        "wide_json": {"path": str(WIDE_JSON), "exists": WIDE_JSON.exists()},
    }
    try:
        rows = load_csv_rows(RUNTIME_CSV)
        out["runtime_csv"].update(
            {
                "row_count": len(rows),
                "range": range_2d(rows),
                "id_min": min(row_id(row) for row in rows if row_id(row) is not None),
                "id_max": max(row_id(row) for row in rows if row_id(row) is not None),
                "cluster_rows": sum(1 for row in rows if row.get("Cluster") not in ("", "None", '(Id="")', None)),
                "sample": rows[:3],
                "tail_sample": rows[-3:],
            }
        )
    except Exception as exc:
        out["runtime_csv"]["error"] = f"{type(exc).__name__}: {exc}"
    try:
        rows = load_wide_json_rows(WIDE_JSON)
        out["wide_json"].update(
            {
                "row_count": len(rows),
                "range": range_2d(rows),
                "id_min": min(row_id(row) for row in rows if row_id(row) is not None),
                "id_max": max(row_id(row) for row in rows if row_id(row) is not None),
                "sample": rows[:3],
                "tail_sample": rows[-3:],
                "farthest": [
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
                ],
            }
        )
    except Exception as exc:
        out["wide_json"]["error"] = f"{type(exc).__name__}: {exc}"
    return out


def current_level_actor_probe() -> dict:
    out = {"level": STARMAP_LEVEL}
    load = safe("load_map", unreal.EditorLoadingAndSavingUtils.load_map, STARMAP_LEVEL)
    out["load_map"] = load
    if not load["ok"]:
        return out
    try:
        actors = list(unreal.EditorLevelLibrary.get_all_level_actors())
    except Exception as exc:
        out["actors_error"] = f"{type(exc).__name__}: {exc}"
        return out
    class_counts = Counter(get_class_name(actor) for actor in actors)
    system_rows = []
    special_actors = []
    for actor in actors:
        cls = get_class_name(actor)
        try:
            label = text(actor.get_actor_label())
        except Exception:
            label = text(actor)
        try:
            loc = actor.get_actor_location()
            loc_json = {"x": float(loc.x), "y": float(loc.y), "z": float(loc.z)}
        except Exception:
            loc_json = None
        joined = f"{label} {cls}".lower()
        if "starsystembody" in joined:
            system_rows.append(
                {
                    "label": label,
                    "class": cls,
                    "path": get_path_name(actor),
                    "star_system_id": read_prop(actor, "star_system_id"),
                    "desired_zoom_level": read_prop(actor, "desired_zoom_level"),
                    "location": loc_json,
                }
            )
        elif any(term in joined for term in ("starmap", "scene", "camera", "pawn", "border")):
            special_actors.append(
                {
                    "label": label,
                    "class": cls,
                    "path": get_path_name(actor),
                    "location": loc_json,
                    "properties": {
                        "star_system_body_look_up_count": len(read_prop(actor, "star_system_body_look_up") or []),
                        "cluster_material": read_prop(actor, "cluster_material"),
                        "procedural_border_mesh": read_prop(actor, "procedural_border_mesh"),
                    },
                }
            )
    out["actor_count"] = len(actors)
    out["class_counts_top"] = dict(class_counts.most_common(40))
    out["star_system_body_count"] = len(system_rows)
    out["star_system_body_id_range"] = {
        "min": min((row["star_system_id"] for row in system_rows if isinstance(row["star_system_id"], int)), default=None),
        "max": max((row["star_system_id"] for row in system_rows if isinstance(row["star_system_id"], int)), default=None),
    }
    ids = [row["star_system_id"] for row in system_rows if isinstance(row["star_system_id"], int)]
    out["duplicate_star_system_ids"] = sorted(item for item, count in Counter(ids).items() if count > 1)[:100]
    out["missing_ids_in_actor_sequence_0_to_max"] = [
        item for item in range(0, max(ids) + 1) if item not in set(ids)
    ][:250] if ids else []
    by_distance = sorted(
        system_rows,
        key=lambda row: abs(row["location"]["x"]) + abs(row["location"]["y"]) if row.get("location") else -1,
        reverse=True,
    )
    out["sample_systems"] = system_rows[:20]
    out["farthest_systems"] = by_distance[:20]
    out["star_system_bodies"] = system_rows
    out["special_actors"] = special_actors[:100]
    return out


def placement_join_probe(level: dict, source: dict) -> dict:
    out = {}
    try:
        csv_rows = load_csv_rows(RUNTIME_CSV)
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}
    by_id = {row_id(row): row for row in csv_rows if row_id(row) is not None}
    actors = level.get("star_system_bodies", []) or level.get("sample_systems", []) + level.get("farthest_systems", [])
    joined = []
    loc_x_from_pos_y = []
    loc_y_from_pos_x = []
    for actor in actors:
        sid = actor.get("star_system_id")
        row = by_id.get(sid)
        loc = actor.get("location") or {}
        if not row:
            joined.append({"actor": actor, "csv_row": None})
            continue
        px = float_field(row, "PosX")
        py = float_field(row, "PosY")
        lx = loc.get("x")
        ly = loc.get("y")
        if py is not None and lx is not None:
            loc_x_from_pos_y.append((py, lx, sid))
        if px is not None and ly is not None:
            loc_y_from_pos_x.append((px, ly, sid))
        joined.append(
            {
                "star_system_id": sid,
                "actor_label": actor.get("label"),
                "actor_location": loc,
                "csv_star_system_name": row.get("StarSystemName"),
                "csv_pos": {"x": px, "y": py},
            }
        )
    def linear_fit(points: list[tuple[float, float, int]]) -> dict:
        if not points:
            return {"count": 0}
        xs = [item[0] for item in points]
        ys = [item[1] for item in points]
        x_avg = sum(xs) / len(xs)
        y_avg = sum(ys) / len(ys)
        denom = sum((x - x_avg) ** 2 for x in xs)
        if denom == 0:
            return {"count": len(points), "error": "zero variance"}
        slope = sum((x - x_avg) * (y - y_avg) for x, y in zip(xs, ys)) / denom
        intercept = y_avg - slope * x_avg
        residuals = [
            {"sid": sid, "residual": y - (intercept + slope * x), "input": x, "actual": y}
            for x, y, sid in points
        ]
        max_abs = max(abs(item["residual"]) for item in residuals)
        return {
            "count": len(points),
            "slope": slope,
            "intercept": intercept,
            "max_abs_residual": max_abs,
            "worst_residuals": sorted(residuals, key=lambda item: abs(item["residual"]), reverse=True)[:10],
        }
    fit_x = linear_fit(loc_x_from_pos_y)
    fit_y = linear_fit(loc_y_from_pos_x)
    out["joined_samples"] = joined
    out["joined_sample_count"] = len(joined)
    out["placement_transform_current_csv"] = {
        "loc_x_from_csv_pos_y": fit_x,
        "loc_y_from_csv_pos_x": fit_y,
    }
    wide = source.get("wide_json", {}).get("range", {})
    if wide and fit_x.get("count") and fit_y.get("count"):
        x_from_y = fit_x["intercept"] + fit_x["slope"] * wide["y"]["min"]
        x_to_y = fit_x["intercept"] + fit_x["slope"] * wide["y"]["max"]
        y_from_x = fit_y["intercept"] + fit_y["slope"] * wide["x"]["min"]
        y_to_x = fit_y["intercept"] + fit_y["slope"] * wide["x"]["max"]
        out["projected_wide_json_level_bounds"] = {
            "x": {"min": min(x_from_y, x_to_y), "max": max(x_from_y, x_to_y)},
            "y": {"min": min(y_from_x, y_to_x), "max": max(y_from_x, y_to_x)},
        }
    out["csv_ids_without_actor_sample"] = [
        item for item in sorted(by_id)
        if item not in set(
            row.get("star_system_id") for row in actors
        )
    ][:25]
    out["joined_samples"] = joined[:60]
    return out


def cluster_system_membership_probe() -> dict:
    out = {"root": "/Game/Campaign/Clusters"}
    try:
        assets = sorted(set(path.split(".", 1)[0] for path in unreal.EditorAssetLibrary.list_assets(out["root"], True, False)))
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}
    rows = []
    membership = defaultdict(list)
    for asset_path in assets:
        try:
            data = unreal.EditorAssetLibrary.find_asset_data(asset_path)
            if text(data.asset_class) != "MWClusterDataAsset":
                continue
            asset = unreal.EditorAssetLibrary.load_asset(asset_path)
            ids = read_prop(asset, "system_ids") or []
            faction = read_prop(asset, "cluster_faction_asset")
            overlay = read_prop(asset, "cluster_overlay")
            constellation = read_prop(asset, "cluster_constellation")
            row = {
                "asset_path": asset_path,
                "system_count": len(ids),
                "system_ids_sample": list(ids)[:40],
                "faction": faction,
                "overlay": overlay,
                "constellation": constellation,
            }
            rows.append(row)
            for sid in ids:
                membership[int(sid)].append(asset_path)
        except Exception as exc:
            rows.append({"asset_path": asset_path, "error": f"{type(exc).__name__}: {exc}"})
    duplicate_memberships = {
        str(sid): paths for sid, paths in membership.items() if len(paths) > 1
    }
    out["asset_count"] = len(rows)
    out["total_system_memberships"] = sum(row.get("system_count", 0) for row in rows)
    out["with_overlay"] = sum(1 for row in rows if row.get("overlay"))
    out["with_constellation"] = sum(1 for row in rows if row.get("constellation"))
    out["duplicate_system_memberships_count"] = len(duplicate_memberships)
    out["duplicate_system_memberships_sample"] = dict(list(sorted(duplicate_memberships.items()))[:50])
    out["assets_sample"] = rows[:80]
    return out


def decision(report: dict) -> dict:
    level = report.get("current_level", {})
    table = report.get("data_table", {})
    source = report.get("source_files", {})
    clusters = report.get("cluster_assets", {})
    actor_count = level.get("star_system_body_count")
    table_rows = table.get("row_count")
    csv_rows = source.get("runtime_csv", {}).get("row_count")
    json_rows = source.get("wide_json", {}).get("row_count")
    findings = []
    if actor_count and json_rows and actor_count < json_rows:
        findings.append("Current StarMap level actor set is vanilla-sized relative to the wide source JSON.")
    if table_rows and csv_rows and table_rows == csv_rows:
        findings.append("Current editor DataTable row count matches the vanilla runtime CSV.")
    if csv_rows and json_rows and csv_rows < json_rows:
        findings.append("Wide source JSON has additional systems not present in the current cooked/editor DataTable.")
    if clusters.get("asset_count"):
        findings.append("Current territory overlays are represented by MWClusterDataAsset assets, not only deprecated DataTable cluster columns.")
    return {
        "build_authorized": False,
        "manual_editor_ui_required": True,
        "next_repair_candidate": "Editor-authored data/level/cluster migration candidate; no cooked direct substitution.",
        "evidence_gates": findings,
    }


def write_markdown(report: dict) -> None:
    lines = [
        "# Starmap Generation Trace - 2026-05-10",
        "",
        f"- Generated: `{report['generated_utc']}`",
        "- Method: non-mutating MW5 Mod Editor commandlet plus read-only package string scanning.",
        "- Safety: no assets were saved, duplicated, packaged, moved, or modified.",
        "",
        "## Decision",
        "",
        f"- Build authorized: `{report['decision']['build_authorized']}`",
        f"- Manual editor UI required for first authoring step: `{report['decision']['manual_editor_ui_required']}`",
        f"- Next repair candidate: {report['decision']['next_repair_candidate']}",
        "",
        "Evidence gates:",
    ]
    for item in report["decision"]["evidence_gates"]:
        lines.append(f"- {item}")

    source = report.get("source_files", {})
    table = report.get("data_table", {})
    level = report.get("current_level", {})
    placement = report.get("placement_join", {})
    clusters = report.get("cluster_assets", {})

    lines.extend(["", "## Data Sources", ""])
    lines.append(f"- Current DataTable rows: `{table.get('row_count')}` row struct `{table.get('row_struct')}`")
    lines.append(f"- Runtime CSV rows/range: `{source.get('runtime_csv', {}).get('row_count')}` `{source.get('runtime_csv', {}).get('range')}`")
    lines.append(f"- Wide JSON rows/range: `{source.get('wide_json', {}).get('row_count')}` `{source.get('wide_json', {}).get('range')}`")
    for column, info in table.get("columns", {}).items():
        lines.append(f"- DataTable `{column}`: `{info}`")

    lines.extend(["", "## Current Level Actors", ""])
    lines.append(f"- StarMap actors total: `{level.get('actor_count')}`")
    lines.append(f"- StarSystemBody count: `{level.get('star_system_body_count')}`")
    lines.append(f"- StarSystemBody id range: `{level.get('star_system_body_id_range')}`")
    lines.append(f"- Duplicate StarSystemBody ids: `{level.get('duplicate_star_system_ids')}`")
    lines.append(f"- Top classes: `{level.get('class_counts_top')}`")
    lines.append(f"- Placement transform: `{placement.get('placement_transform_current_csv')}`")
    lines.append(f"- Projected wide JSON level bounds: `{placement.get('projected_wide_json_level_bounds')}`")
    for row in placement.get("joined_samples", [])[:30]:
        lines.append(f"- Joined sample: `{row}`")

    lines.extend(["", "## Cluster Assets", ""])
    lines.append(f"- Cluster asset count: `{clusters.get('asset_count')}`")
    lines.append(f"- Total system memberships: `{clusters.get('total_system_memberships')}`")
    lines.append(f"- With overlay: `{clusters.get('with_overlay')}`")
    lines.append(f"- With constellation: `{clusters.get('with_constellation')}`")
    lines.append(f"- Duplicate memberships: `{clusters.get('duplicate_system_memberships_count')}`")

    lines.extend(["", "## Focus Asset Metadata", ""])
    for asset in report.get("assets", []):
        lines.append(f"### `{asset['asset_path']}`")
        data = asset.get("asset_data", {})
        lines.append(f"- Class: `{data.get('asset_class')}`")
        refs = asset.get("references", {})
        deps = refs.get("get_dependencies", [])
        rrefs = refs.get("get_referencers", [])
        lines.append(f"- Dependencies: `{len(deps) if isinstance(deps, list) else deps}`")
        if isinstance(deps, list):
            for dep in deps[:60]:
                lines.append(f"  - `{dep}`")
        lines.append(f"- Referencers: `{len(rrefs) if isinstance(rrefs, list) else rrefs}`")
        fib = asset.get("selected_tags", {}).get("FiBData", {})
        if fib:
            lines.append(f"- Decoded FiB focused token count: `{len(fib.get('decoded_focused_tokens', []))}`")
            for token in fib.get("decoded_focused_tokens", [])[:80]:
                lines.append(f"  - `{token}`")
        raw_strings = asset.get("raw_package_strings", {}).get("focused_strings", [])
        if raw_strings:
            lines.append(f"- Raw package focused strings: `{len(raw_strings)}`")
            for token in raw_strings[:80]:
                lines.append(f"  - `{token}`")
        lines.append("")

    lines.extend(["## Discovered Focus Assets", ""])
    for root, info in report.get("discovered_assets", {}).items():
        lines.append(f"### `{root}`")
        lines.append(f"- Exists: `{info.get('exists')}` count `{info.get('asset_count')}`")
        for match in info.get("matches", [])[:120]:
            lines.append(f"- `{match}`")
        lines.append("")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    report = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "non_mutating": True,
        "assets": [],
        "discovered_assets": {},
        "data_table": {},
        "source_files": {},
        "current_level": {},
        "placement_join": {},
        "cluster_assets": {},
        "errors": [],
    }
    try:
        report["discovered_assets"] = discover_focus_assets()
    except Exception:
        report["errors"].append({"discover_focus_assets": traceback.format_exc()})
    for asset_path in ASSET_PATHS:
        try:
            report["assets"].append(asset_tag_trace(asset_path))
        except Exception:
            report["errors"].append({asset_path: traceback.format_exc()})
    try:
        report["data_table"] = data_table_probe()
    except Exception:
        report["errors"].append({"data_table": traceback.format_exc()})
    try:
        report["source_files"] = source_file_probe()
    except Exception:
        report["errors"].append({"source_files": traceback.format_exc()})
    try:
        report["current_level"] = current_level_actor_probe()
    except Exception:
        report["errors"].append({"current_level": traceback.format_exc()})
    try:
        report["placement_join"] = placement_join_probe(report["current_level"], report["source_files"])
    except Exception:
        report["errors"].append({"placement_join": traceback.format_exc()})
    try:
        report["cluster_assets"] = cluster_system_membership_probe()
    except Exception:
        report["errors"].append({"cluster_assets": traceback.format_exc()})
    report["decision"] = decision(report)
    OUT_JSON.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    write_markdown(report)
    unreal.log(f"TKU starmap generation trace wrote {OUT_JSON} and {OUT_MD}")


main()
