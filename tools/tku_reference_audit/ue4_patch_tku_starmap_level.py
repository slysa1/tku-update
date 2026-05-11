from __future__ import annotations

import csv
import hashlib
import json
import os
import shutil
import traceback
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import unreal
except ImportError:  # Allows normal Python syntax checks outside the editor.
    unreal = None


REPORT_STEM = "ue4_starmap_actor_patch_20260511"
TARGET_MOD_NAME = os.environ.get("TKU_STARMAP_PATCH_MOD_NAME", "TKUCompatEditorPatch").strip()
APPLY = os.environ.get("TKU_STARMAP_PATCH_APPLY", "").strip().lower() in {"1", "true", "yes", "y", "on"}
MAP_ASSET_PATH = os.environ.get("TKU_STARMAP_PATCH_MAP", "/Game/Levels/FrontEnd/StarMap").strip()
SPAWN_METHOD = os.environ.get("TKU_STARMAP_PATCH_SPAWN_METHOD", "object").strip().lower()
SPAWN_PROBE = os.environ.get("TKU_STARMAP_PATCH_SPAWN_PROBE", "").strip().lower() in {"1", "true", "yes", "y", "on"}
NO_SAVE = os.environ.get("TKU_STARMAP_PATCH_NO_SAVE", "").strip().lower() in {"1", "true", "yes", "y", "on"}
EXIT_EDITOR = os.environ.get("TKU_STARMAP_PATCH_EXIT_EDITOR", "").strip().lower() in {"1", "true", "yes", "y", "on"}
SPAWN_LIMIT = int(os.environ.get("TKU_STARMAP_PATCH_LIMIT", "0") or "0")

DATA_TABLE_ASSET = "/Game/InnerSphereData/MW5_InnerSphereData"
STAR_SYSTEM_BODY_BP = "/Game/UI/FrontEnd/Starmap/StarSystemBody"
EXPECTED_ROW_COUNT = int(os.environ.get("TKU_STARMAP_PATCH_EXPECTED_ROWS", "3974"))
EXPECTED_BODY_COUNT = EXPECTED_ROW_COUNT - 1
LEVEL_X_OFFSET = 51336.0
LEVEL_Y_OFFSET = 51039.0
LEVEL_SCALE = 8.0


def resolve_project_root() -> Path:
    raw = os.environ.get("TKU_PROJECT_ROOT")
    if raw:
        return Path(raw).resolve()

    script_path = globals().get("__file__")
    if script_path:
        return Path(script_path).resolve().parents[2]

    return Path(r"D:\Downloads\OneDrive\Documents\code\tku-update")


PROJECT_ROOT = resolve_project_root()
CONFIG_PATHS = [
    Path(os.environ["TKU_PATHS_CONFIG"]) if os.environ.get("TKU_PATHS_CONFIG") else None,
    PROJECT_ROOT / "config" / "tku_paths.local.json",
    PROJECT_ROOT / "config" / "tku_paths.json",
    PROJECT_ROOT / "config" / "tku_paths.example.json",
]
REPORT_DIR = PROJECT_ROOT / "reports" / "tku_editor_first"
OUT_JSON = REPORT_DIR / f"{REPORT_STEM}.json"
OUT_MD = REPORT_DIR / f"{REPORT_STEM}.md"
STATUS_JSON = REPORT_DIR / f"{REPORT_STEM}_status.json"
CSV_PATH = REPORT_DIR / "tku_inner_sphere_merged_current_plus_tku_additions_20260510.csv"


def read_config() -> dict[str, Any]:
    for candidate in CONFIG_PATHS:
        if candidate and candidate.is_file():
            return json.loads(candidate.read_text(encoding="utf-8"))
    return {}


CONFIG = read_config()
EDITOR_ROOT = Path(
    os.environ.get("TKU_MW5_EDITOR_ROOT")
    or CONFIG.get("mw5_editor_root")
    or r"E:\Games\MechWarrior5Editor"
)
EDITOR_PROJECT = EDITOR_ROOT / "MW5Mercs"
PLUGIN_DIR = EDITOR_PROJECT / "Plugins" / TARGET_MOD_NAME
TARGET_MAP_FILE = PLUGIN_DIR / "ModOverride" / "Levels" / "FrontEnd" / "StarMap.umap"
BASE_MAP_FILE = EDITOR_PROJECT / "Content" / "Levels" / "FrontEnd" / "StarMap.umap"
BACKUP_DIR = REPORT_DIR / "backups" / f"{TARGET_MOD_NAME}_starmap_pre_actor_patch_20260511"


def jsonable(value: Any, depth: int = 0) -> Any:
    if depth > 4:
        return str(value)
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(k): jsonable(v, depth + 1) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [jsonable(item, depth + 1) for item in value]
    try:
        if hasattr(value, "__iter__") and not isinstance(value, (str, bytes)):
            return [jsonable(item, depth + 1) for item in list(value)]
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


def safe_call(func, *args) -> dict[str, Any]:
    try:
        return {"ok": True, "value": jsonable(func(*args))}
    except Exception as exc:
        return {"ok": False, "error": f"{type(exc).__name__}: {exc}"}


def sha256_file(path: Path) -> str | None:
    if not path.is_file():
        return None
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def log_status(step: str, **details: Any) -> None:
    payload = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "step": step,
        "details": jsonable(details),
    }
    try:
        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        STATUS_JSON.write_text(json.dumps(payload, indent=2, sort_keys=True, default=str), encoding="utf-8")
    except Exception:
        pass
    if unreal is not None:
        try:
            unreal.log(f"TKU StarMap patch: {step} {json.dumps(jsonable(details), sort_keys=True, default=str)}")
        except Exception:
            pass


def detect_csv_encoding(path: Path) -> str:
    start = path.read_bytes()[:4]
    if start.startswith((b"\xff\xfe", b"\xfe\xff")):
        return "utf-16"
    if start.startswith(b"\xef\xbb\xbf"):
        return "utf-8-sig"
    return "utf-8-sig"


def parse_rows() -> dict[int, dict[str, Any]]:
    encoding = detect_csv_encoding(CSV_PATH)
    rows: dict[int, dict[str, Any]] = {}
    with CSV_PATH.open("r", encoding=encoding, newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if not row or not any(str(value).strip() for value in row.values()):
                continue
            raw_id = (row.get("Name") or row.get("---") or "").strip()
            try:
                sid = int(raw_id)
                pos_x = float(row["PosX"])
                pos_y = float(row["PosY"])
            except (KeyError, TypeError, ValueError):
                continue
            rows[sid] = {
                "id": sid,
                "name": row.get("StarSystemName") or "",
                "pos_x": pos_x,
                "pos_y": pos_y,
                "level_x": LEVEL_X_OFFSET + LEVEL_SCALE * pos_y,
                "level_y": LEVEL_Y_OFFSET + LEVEL_SCALE * pos_x,
                "level_z": 0.0,
            }
    return rows


def get_class_name(obj: Any) -> str:
    try:
        return str(obj.get_class().get_name())
    except Exception:
        return ""


def get_path_name(obj: Any) -> str:
    try:
        return str(obj.get_path_name())
    except Exception:
        return str(obj)


def actor_label(actor: Any) -> str:
    try:
        return str(actor.get_actor_label())
    except Exception:
        try:
            return str(actor.get_name())
        except Exception:
            return str(actor)


def read_prop(obj: Any, prop: str) -> Any:
    try:
        return jsonable(obj.get_editor_property(prop))
    except Exception:
        return None


def is_star_system_body(actor: Any) -> bool:
    joined = f"{actor_label(actor)} {get_class_name(actor)}".lower()
    return "starsystembody" in joined


def inspect_level(rows_by_id: dict[int, dict[str, Any]] | None = None) -> dict[str, Any]:
    out: dict[str, Any] = {}
    if unreal is None:
        out["error"] = "unreal module is not available; run through MW5 UE4Editor-Cmd."
        return out

    try:
        world = unreal.EditorLevelLibrary.get_editor_world()
        out["world_path"] = get_path_name(world)
        out["world_outer"] = get_path_name(world.get_outer())
    except Exception as exc:
        out["world_error"] = f"{type(exc).__name__}: {exc}"

    actors = list(unreal.EditorLevelLibrary.get_all_level_actors())
    class_counts = Counter(get_class_name(actor) for actor in actors)
    body_rows: list[dict[str, Any]] = []
    for actor in actors:
        if not is_star_system_body(actor):
            continue
        try:
            loc = actor.get_actor_location()
            loc_json = {"x": float(loc.x), "y": float(loc.y), "z": float(loc.z)}
        except Exception:
            loc_json = None
        sid = read_prop(actor, "star_system_id")
        row: dict[str, Any] = {
            "label": actor_label(actor),
            "class": get_class_name(actor),
            "path": get_path_name(actor),
            "star_system_id": sid,
            "desired_zoom_level": read_prop(actor, "desired_zoom_level"),
            "location": loc_json,
        }
        if isinstance(sid, int) and loc_json and rows_by_id and sid in rows_by_id:
            expected = rows_by_id[sid]
            row["placement_error"] = {
                "dx": loc_json["x"] - expected["level_x"],
                "dy": loc_json["y"] - expected["level_y"],
                "dz": loc_json["z"] - expected["level_z"],
            }
        body_rows.append(row)

    ids = [row["star_system_id"] for row in body_rows if isinstance(row.get("star_system_id"), int)]
    out.update(
        {
            "actor_count": len(actors),
            "class_counts_top": dict(class_counts.most_common(30)),
            "star_system_body_count": len(body_rows),
            "star_system_body_id_range": {
                "min": min(ids) if ids else None,
                "max": max(ids) if ids else None,
            },
            "duplicate_star_system_ids": sorted(sid for sid, count in Counter(ids).items() if count > 1)[:100],
            "sample_star_system_bodies": body_rows[:10],
            "tail_star_system_bodies": body_rows[-10:],
        }
    )
    if rows_by_id is not None:
        desired_ids = set(rows_by_id) - {0}
        out["desired_body_count"] = len(desired_ids)
        out["missing_desired_ids_count"] = len(desired_ids - set(ids))
        out["extra_actor_ids_count"] = len(set(ids) - desired_ids)
        out["missing_desired_ids_sample"] = sorted(desired_ids - set(ids))[:40]
        out["extra_actor_ids_sample"] = sorted(set(ids) - desired_ids)[:40]
        placement_errors = []
        for row in body_rows:
            err = row.get("placement_error")
            if not err:
                continue
            if abs(err["dx"]) > 0.01 or abs(err["dy"]) > 0.01 or abs(err["dz"]) > 0.01:
                placement_errors.append({"id": row["star_system_id"], "error": err})
        out["placement_errors_count"] = len(placement_errors)
        out["placement_errors_sample"] = placement_errors[:40]
    return out


def data_table_info() -> dict[str, Any]:
    out: dict[str, Any] = {"asset_path": DATA_TABLE_ASSET}
    if unreal is None:
        out["error"] = "unreal module is not available"
        return out
    asset = unreal.EditorAssetLibrary.load_asset(DATA_TABLE_ASSET)
    out["loaded"] = bool(asset)
    if not asset:
        return out
    out["object_path"] = get_path_name(asset)
    out["class"] = get_class_name(asset)
    try:
        out["row_struct"] = get_path_name(asset.get_editor_property("row_struct"))
    except Exception as exc:
        out["row_struct_error"] = f"{type(exc).__name__}: {exc}"
    try:
        rows = [str(row) for row in unreal.DataTableFunctionLibrary.get_data_table_row_names(asset)]
        out["row_count"] = len(rows)
        out["sample_rows_present"] = {row: row in set(rows) for row in ("0", "1", "3501", "4001", "4110", "7921")}
    except Exception as exc:
        out["row_error"] = f"{type(exc).__name__}: {exc}"
    return out


def build_safety(report: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if unreal is None:
        failures.append("unreal module unavailable")
    if TARGET_MOD_NAME != "TKUCompatEditorPatch":
        failures.append(f"unexpected target mod name: {TARGET_MOD_NAME}")
    if MAP_ASSET_PATH != "/Game/Levels/FrontEnd/StarMap":
        failures.append(f"unexpected map asset path: {MAP_ASSET_PATH}")
    if SPAWN_METHOD not in {"class", "object"}:
        failures.append(f"unexpected spawn method: {SPAWN_METHOD}")
    if not PLUGIN_DIR.is_dir():
        failures.append(f"target plugin dir missing: {PLUGIN_DIR}")
    if not TARGET_MAP_FILE.is_file():
        failures.append(f"mod-owned StarMap file missing: {TARGET_MAP_FILE}")
    if not CSV_PATH.is_file():
        failures.append(f"merged InnerSphere CSV missing: {CSV_PATH}")
    if report.get("csv", {}).get("row_count") != EXPECTED_ROW_COUNT:
        failures.append(f"unexpected CSV row count: {report.get('csv', {}).get('row_count')}")
    table = report.get("data_table", {})
    if table.get("row_count") != EXPECTED_ROW_COUNT:
        failures.append(f"active DataTable row count is not {EXPECTED_ROW_COUNT}: {table.get('row_count')}")
    if table.get("object_path") and f"/ModOverride/{TARGET_MOD_NAME}/" not in table["object_path"]:
        failures.append(f"active DataTable is not resolving through mod override: {table['object_path']}")
    level = report.get("before_level", {})
    if level.get("world_path") and f"/ModOverride/{TARGET_MOD_NAME}/" not in level["world_path"]:
        failures.append(f"loaded StarMap is not resolving through mod override: {level['world_path']}")
    if report.get("target_map_hash_before") is None:
        failures.append("could not hash target StarMap before operation")
    return failures


def load_spawn_source() -> tuple[Any, str | None]:
    if SPAWN_METHOD == "class":
        actor_class = unreal.EditorAssetLibrary.load_blueprint_class(STAR_SYSTEM_BODY_BP)
        if not actor_class:
            return None, f"could not load blueprint class: {STAR_SYSTEM_BODY_BP}"
        return actor_class, None

    blueprint_asset = unreal.EditorAssetLibrary.load_asset(STAR_SYSTEM_BODY_BP)
    if not blueprint_asset:
        try:
            blueprint_asset = unreal.load_asset(STAR_SYSTEM_BODY_BP)
        except Exception:
            blueprint_asset = None
    if not blueprint_asset:
        return None, f"could not load blueprint asset: {STAR_SYSTEM_BODY_BP}"
    return blueprint_asset, None


def spawn_one_actor(spawn_source: Any, row: dict[str, Any], label: str) -> Any:
    location = unreal.Vector(row["level_x"], row["level_y"], row["level_z"])
    rotation = unreal.Rotator(0.0, 0.0, 0.0)
    log_status("before_spawn_actor", method=SPAWN_METHOD, id=row["id"], label=label, location=row)
    if SPAWN_METHOD == "class":
        actor = unreal.EditorLevelLibrary.spawn_actor_from_class(spawn_source, location, rotation)
    else:
        actor = unreal.EditorLevelLibrary.spawn_actor_from_object(spawn_source, location, rotation)
    log_status("after_spawn_actor", method=SPAWN_METHOD, id=row["id"], actor=get_path_name(actor) if actor else None)
    if not actor:
        return None
    star_system_info = unreal.StarSystemInfo(
        star_system_id=int(row["id"]),
        star_system_name=str(row.get("name") or ""),
        pos_x=float(row["pos_x"]),
        pos_y=float(row["pos_y"]),
    )
    actor.setup_info(star_system_info)
    actor.set_actor_label(label, True)
    log_status(
        "after_configure_actor",
        method=SPAWN_METHOD,
        id=row["id"],
        actor=get_path_name(actor),
        star_system_id=read_prop(actor, "star_system_id"),
        desired_zoom_level=read_prop(actor, "desired_zoom_level"),
    )
    return actor


def probe_spawn(rows_by_id: dict[int, dict[str, Any]], before_level: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {
        "attempted": True,
        "probe": True,
        "method": SPAWN_METHOD,
        "spawned": 0,
        "destroyed": False,
        "saved": False,
        "errors": [],
    }
    spawn_source, error = load_spawn_source()
    if error:
        result["errors"].append(error)
        return result

    existing_ids = set()
    for actor in unreal.EditorLevelLibrary.get_all_level_actors():
        if is_star_system_body(actor):
            sid = read_prop(actor, "star_system_id")
            if isinstance(sid, int):
                existing_ids.add(sid)

    desired_ids = sorted(set(rows_by_id) - {0})
    missing_ids = [sid for sid in desired_ids if sid not in existing_ids]
    if not missing_ids:
        result["reason"] = "no missing StarSystemBody actors"
        return result

    sid = missing_ids[0]
    label = f"TKUProbe_StarSystemBody{int(before_level.get('star_system_body_count') or 0)}"
    actor = None
    try:
        actor = spawn_one_actor(spawn_source, rows_by_id[sid], label)
        if not actor:
            result["errors"].append(f"spawn returned None for id {sid}")
            return result
        result["spawned"] = 1
        result["spawned_id"] = sid
        result["spawned_actor"] = get_path_name(actor)
        result["star_system_id_after_setup"] = read_prop(actor, "star_system_id")
        result["desired_zoom_level_after_setup"] = read_prop(actor, "desired_zoom_level")
    except Exception:
        result["errors"].append(traceback.format_exc())
    finally:
        if actor:
            result["destroyed"] = bool(unreal.EditorLevelLibrary.destroy_actor(actor))
            log_status("after_probe_destroy", id=sid, destroyed=result["destroyed"])
    return result


def spawn_missing(rows_by_id: dict[int, dict[str, Any]], before_level: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {
        "attempted": True,
        "spawned": 0,
        "saved": False,
        "spawned_ids_sample": [],
        "errors": [],
    }
    result["method"] = SPAWN_METHOD
    spawn_source, error = load_spawn_source()
    if error:
        result["errors"].append(error)
        return result

    existing_ids = set()
    for actor in unreal.EditorLevelLibrary.get_all_level_actors():
        if is_star_system_body(actor):
            sid = read_prop(actor, "star_system_id")
            if isinstance(sid, int):
                existing_ids.add(sid)

    desired_ids = sorted(set(rows_by_id) - {0})
    missing_ids = [sid for sid in desired_ids if sid not in existing_ids]
    if SPAWN_LIMIT > 0:
        missing_ids = missing_ids[:SPAWN_LIMIT]
    result["missing_before_count"] = len(missing_ids)
    result["missing_before_sample"] = missing_ids[:40]

    next_label_index = int(before_level.get("star_system_body_count") or 0)
    for sid in missing_ids:
        row = rows_by_id[sid]
        try:
            actor = spawn_one_actor(spawn_source, row, f"StarSystemBody{next_label_index}")
            if not actor:
                result["errors"].append(f"spawn returned None for id {sid}")
                continue
            next_label_index += 1
            result["spawned"] += 1
            if len(result["spawned_ids_sample"]) < 80:
                result["spawned_ids_sample"].append(sid)
        except Exception:
            result["errors"].append(f"id {sid}: {traceback.format_exc()}")
            if len(result["errors"]) >= 20:
                break

    if NO_SAVE:
        result["saved"] = False
        result["reason"] = "no-save requested"
    else:
        log_status("before_save_current_level", spawned=result["spawned"], errors=len(result["errors"]))
        result["saved"] = bool(unreal.EditorLevelLibrary.save_current_level())
        log_status("after_save_current_level", saved=result["saved"])
    return result


def write_report(report: dict[str, Any]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True, default=str), encoding="utf-8")

    result = report.get("result", {})
    lines = [
        "# UE4 StarMap Actor Patch Gate - 2026-05-11",
        "",
        f"- Generated: `{report['generated_utc']}`",
        f"- Apply requested: `{report['apply_requested']}`",
        f"- Spawn probe: `{report['spawn_probe']}`",
        f"- Spawn method: `{report['spawn_method']}`",
        f"- Spawn limit: `{report['spawn_limit']}`",
        f"- No-save requested: `{report['no_save']}`",
        f"- Map asset: `{MAP_ASSET_PATH}`",
        f"- Target mod file: `{TARGET_MAP_FILE}`",
        f"- CSV: `{CSV_PATH}`",
        "",
        "## Inputs",
        "",
        f"- CSV rows: `{report.get('csv', {}).get('row_count')}`",
        f"- Active DataTable: `{report.get('data_table', {})}`",
        f"- Target map hash before: `{report.get('target_map_hash_before')}`",
        "",
        "## Safety",
        "",
    ]
    if report["safety_failures"]:
        for failure in report["safety_failures"]:
            lines.append(f"- FAIL: {failure}")
    else:
        lines.append("- No safety failures.")

    lines.extend(
        [
            "",
            "## Before",
            "",
            f"- Level: `{report.get('before_level', {})}`",
            "",
            "## Result",
            "",
            f"- Attempted: `{result.get('attempted')}`",
            f"- Reason: `{result.get('reason')}`",
            f"- Spawned: `{result.get('spawned')}`",
            f"- Saved: `{result.get('saved')}`",
            f"- Errors: `{len(result.get('errors') or [])}`",
            "",
            "## After",
            "",
            f"- Target map hash after: `{report.get('target_map_hash_after')}`",
            f"- Base map unchanged: `{report.get('base_map_unchanged')}`",
            f"- Level: `{report.get('after_level', {})}`",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    log_status("start", apply=APPLY, spawn_probe=SPAWN_PROBE, method=SPAWN_METHOD, limit=SPAWN_LIMIT, no_save=NO_SAVE)
    rows_by_id = parse_rows() if CSV_PATH.is_file() else {}
    report: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "apply_requested": APPLY,
        "spawn_probe": SPAWN_PROBE,
        "spawn_method": SPAWN_METHOD,
        "spawn_limit": SPAWN_LIMIT,
        "no_save": NO_SAVE,
        "target_mod_name": TARGET_MOD_NAME,
        "map_asset_path": MAP_ASSET_PATH,
        "target_map_file": str(TARGET_MAP_FILE),
        "base_map_file": str(BASE_MAP_FILE),
        "target_map_hash_before": sha256_file(TARGET_MAP_FILE),
        "base_map_hash_before": sha256_file(BASE_MAP_FILE),
        "csv": {
            "path": str(CSV_PATH),
            "exists": CSV_PATH.is_file(),
            "row_count": len(rows_by_id),
            "desired_actor_count": len(set(rows_by_id) - {0}),
            "sample_ids": sorted(rows_by_id)[:10],
            "tail_ids": sorted(rows_by_id)[-10:],
        },
        "data_table": {},
        "base_load": {},
        "before_level": {},
        "result": {
            "attempted": False,
            "spawned": 0,
            "saved": False,
            "reason": None,
        },
    }

    if unreal is not None:
        try:
            report["data_table"] = data_table_info()
            log_status("before_load_map", map=MAP_ASSET_PATH)
            report["base_load"] = safe_call(unreal.EditorLoadingAndSavingUtils.load_map, MAP_ASSET_PATH)
            log_status("after_load_map", result=report["base_load"])
            if report["base_load"].get("ok"):
                report["before_level"] = inspect_level(rows_by_id)
                log_status(
                    "after_before_level_inspection",
                    actor_count=report["before_level"].get("actor_count"),
                    body_count=report["before_level"].get("star_system_body_count"),
                    missing=report["before_level"].get("missing_desired_ids_count"),
                )
        except Exception:
            report["load_exception"] = traceback.format_exc()

    report["safety_failures"] = build_safety(report)

    if report["safety_failures"]:
        report["result"]["reason"] = "safety failures"
    elif not report["base_load"].get("ok"):
        report["result"]["reason"] = "map load failed"
    elif SPAWN_PROBE:
        report["result"] = probe_spawn(rows_by_id, report.get("before_level", {}))
    elif not APPLY:
        report["result"]["reason"] = "dry run only"
    elif report.get("before_level", {}).get("missing_desired_ids_count") == 0:
        report["result"]["reason"] = "no missing StarSystemBody actors"
    else:
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        backup_target = BACKUP_DIR / TARGET_MAP_FILE.name
        shutil.copy2(TARGET_MAP_FILE, backup_target)
        report["pre_patch_backup"] = {
            "path": str(backup_target),
            "sha256": sha256_file(backup_target),
        }
        report["result"] = spawn_missing(rows_by_id, report.get("before_level", {}))

    report["target_map_hash_after"] = sha256_file(TARGET_MAP_FILE)
    report["base_map_hash_after"] = sha256_file(BASE_MAP_FILE)
    report["base_map_unchanged"] = (
        report.get("base_map_hash_before") is not None
        and report.get("base_map_hash_before") == report.get("base_map_hash_after")
    )
    if unreal is not None and report.get("base_load", {}).get("ok"):
        try:
            report["after_level"] = inspect_level(rows_by_id)
        except Exception:
            report["after_exception"] = traceback.format_exc()

    write_report(report)
    log_status("report_written", report=str(OUT_JSON), result=report.get("result"))
    if EXIT_EDITOR and unreal is not None:
        try:
            unreal.SystemLibrary.quit_editor()
        except Exception:
            pass


if __name__ == "__main__":
    main()
