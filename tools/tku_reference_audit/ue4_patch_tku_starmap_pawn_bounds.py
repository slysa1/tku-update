from __future__ import annotations

import csv
import hashlib
import json
import os
import shutil
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import unreal
except ImportError:  # Allows syntax checks outside the editor.
    unreal = None


REPORT_STEM = "ue4_starmap_pawn_bounds_patch_20260512"
TARGET_MOD_NAME = os.environ.get("TKU_STARMAP_PAWN_MOD_NAME", "TKUCompatEditorPatch").strip()
ASSET_PATH = os.environ.get("TKU_STARMAP_PAWN_ASSET", "/Game/UI/FrontEnd/StarMapPawn").strip()
APPLY = os.environ.get("TKU_STARMAP_PAWN_APPLY", "").strip().lower() in {"1", "true", "yes", "y", "on"}
EXIT_EDITOR = os.environ.get("TKU_STARMAP_PAWN_EXIT_EDITOR", "").strip().lower() in {"1", "true", "yes", "y", "on"}

TARGET_PAN_HORIZONTAL = float(os.environ.get("TKU_STARMAP_PAWN_PAN_HORIZONTAL", "17500"))
TARGET_PAN_VERTICAL = float(os.environ.get("TKU_STARMAP_PAWN_PAN_VERTICAL", "17500"))
TARGET_ZOOM_DISTANCES = [
    float(value)
    for value in os.environ.get(
        "TKU_STARMAP_PAWN_ZOOM_DISTANCES",
        "300,600,900,1300,1800,2200,2800,3500,5000,7500,9000",
    ).split(",")
    if value.strip()
]
TARGET_ZOOM_THRESHOLDS = [
    int(value)
    for value in os.environ.get("TKU_STARMAP_PAWN_ZOOM_THRESHOLDS", "3500,1000").split(",")
    if value.strip()
]

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
TARGET_ASSET_FILE = PLUGIN_DIR / "ModOverride" / "UI" / "FrontEnd" / "StarMapPawn.uasset"
BASE_ASSET_FILE = EDITOR_PROJECT / "Content" / "UI" / "FrontEnd" / "StarMapPawn.uasset"
BACKUP_DIR = REPORT_DIR / "backups" / f"{TARGET_MOD_NAME}_starmap_pawn_pre_bounds_patch_20260512"


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


def get_path_name(obj: Any) -> str:
    try:
        return str(obj.get_path_name())
    except Exception:
        return str(obj)


def get_class_name(obj: Any) -> str:
    try:
        return str(obj.get_class().get_name())
    except Exception:
        return ""


def read_prop(obj: Any, prop: str) -> Any:
    try:
        return jsonable(obj.get_editor_property(prop))
    except Exception as exc:
        return {"error": f"{type(exc).__name__}: {exc}"}


def write_prop(obj: Any, prop: str, value: Any) -> dict[str, Any]:
    try:
        obj.set_editor_property(prop, value)
        return {"ok": True, "after": read_prop(obj, prop)}
    except Exception as exc:
        return {"ok": False, "error": f"{type(exc).__name__}: {exc}"}


def detect_csv_encoding(path: Path) -> str:
    start = path.read_bytes()[:4]
    if start.startswith((b"\xff\xfe", b"\xfe\xff")):
        return "utf-16"
    if start.startswith(b"\xef\xbb\xbf"):
        return "utf-8-sig"
    return "utf-8-sig"


def csv_extent_summary(path: Path) -> dict[str, Any]:
    out: dict[str, Any] = {"path": str(path), "exists": path.is_file()}
    if not path.is_file():
        return out
    encoding = detect_csv_encoding(path)
    xs: list[float] = []
    ys: list[float] = []
    vanilla_xs: list[float] = []
    vanilla_ys: list[float] = []
    with path.open("r", encoding=encoding, newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if not row or not any(str(value).strip() for value in row.values()):
                continue
            try:
                sid = int((row.get("Name") or row.get("---") or "").strip())
                pos_x = float(row["PosX"])
                pos_y = float(row["PosY"])
            except (KeyError, TypeError, ValueError):
                continue
            if sid == 0:
                continue
            level_x = LEVEL_SCALE * pos_y
            level_y = LEVEL_SCALE * pos_x
            xs.append(level_x)
            ys.append(level_y)
            if sid <= 3501:
                vanilla_xs.append(level_x)
                vanilla_ys.append(level_y)

    def bounds(values: list[float]) -> dict[str, float | None]:
        if not values:
            return {"min": None, "max": None, "span": None, "half_span": None}
        min_value = min(values)
        max_value = max(values)
        span = max_value - min_value
        return {"min": min_value, "max": max_value, "span": span, "half_span": span / 2.0}

    out.update(
        {
            "encoding": encoding,
            "row_count_excluding_0": len(xs),
            "all_x": bounds(xs),
            "all_y": bounds(ys),
            "vanilla_subset_x": bounds(vanilla_xs),
            "vanilla_subset_y": bounds(vanilla_ys),
            "target_pan_horizontal": TARGET_PAN_HORIZONTAL,
            "target_pan_vertical": TARGET_PAN_VERTICAL,
        }
    )
    return out


def load_pawn() -> dict[str, Any]:
    out: dict[str, Any] = {"asset_path": ASSET_PATH}
    if unreal is None:
        out["error"] = "unreal module unavailable"
        return out
    out["asset_exists"] = safe_call(unreal.EditorAssetLibrary.does_asset_exist, ASSET_PATH)
    asset = unreal.EditorAssetLibrary.load_asset(ASSET_PATH)
    out["asset_loaded"] = bool(asset)
    if not asset:
        return out
    out["asset_object_path"] = get_path_name(asset)
    out["asset_class"] = get_class_name(asset)
    bp_class = unreal.EditorAssetLibrary.load_blueprint_class(ASSET_PATH)
    out["blueprint_class_loaded"] = bool(bp_class)
    if not bp_class:
        return out
    out["blueprint_class_path"] = get_path_name(bp_class)
    cdo = unreal.get_default_object(bp_class)
    out["cdo_path"] = get_path_name(cdo)
    out["cdo_class"] = get_class_name(cdo)
    out["defaults"] = {
        "pan_bounds_horizontal": read_prop(cdo, "pan_bounds_horizontal"),
        "pan_bounds_vertical": read_prop(cdo, "pan_bounds_vertical"),
        "zoom_distance_list": read_prop(cdo, "zoom_distance_list"),
        "zoom_level_thresholds": read_prop(cdo, "zoom_level_thresholds"),
    }
    out["_asset_ref"] = asset
    out["_cdo_ref"] = cdo
    return out


def build_safety(report: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if unreal is None:
        failures.append("unreal module unavailable")
    if TARGET_MOD_NAME != "TKUCompatEditorPatch":
        failures.append(f"unexpected target mod name: {TARGET_MOD_NAME}")
    if ASSET_PATH != "/Game/UI/FrontEnd/StarMapPawn":
        failures.append(f"unexpected asset path: {ASSET_PATH}")
    if not PLUGIN_DIR.is_dir():
        failures.append(f"target plugin dir missing: {PLUGIN_DIR}")
    if not TARGET_ASSET_FILE.is_file():
        failures.append(f"mod-owned StarMapPawn file missing; use MW5 Mod Editor Save To Mod first: {TARGET_ASSET_FILE}")
    if report.get("target_asset_hash_before") is None:
        failures.append("could not hash target StarMapPawn before operation")
    if report.get("base_asset_hash_before") is None:
        failures.append("could not hash base StarMapPawn before operation")
    pawn = report.get("pawn", {})
    for key in ("asset_object_path", "blueprint_class_path", "cdo_path"):
        value = pawn.get(key)
        if value and f"/ModOverride/{TARGET_MOD_NAME}/" not in value:
            failures.append(f"{key} is not resolving through mod override: {value}")
    if not pawn.get("asset_loaded"):
        failures.append(f"StarMapPawn asset did not load: {ASSET_PATH}")
    if not pawn.get("blueprint_class_loaded"):
        failures.append(f"StarMapPawn Blueprint class did not load: {ASSET_PATH}")
    if TARGET_PAN_HORIZONTAL < 10000 or TARGET_PAN_VERTICAL < 10000:
        failures.append("target pan bounds are unexpectedly small for TKU expanded map")
    if max(TARGET_ZOOM_DISTANCES or [0]) < 7500:
        failures.append("target zoom distance max is unexpectedly small for TKU expanded map")
    return failures


def apply_patch(report: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {"attempted": False, "applied": False, "saved": False}
    if report["safety_failures"]:
        result["reason"] = "safety failures"
        return result
    if not APPLY:
        result["reason"] = "dry run only"
        return result

    asset = report["pawn"].get("_asset_ref")
    cdo = report["pawn"].get("_cdo_ref")
    if not asset or not cdo:
        result["reason"] = "missing loaded asset or CDO ref"
        return result

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    backup_target = BACKUP_DIR / TARGET_ASSET_FILE.name
    shutil.copy2(TARGET_ASSET_FILE, backup_target)
    result["pre_patch_backup"] = {"path": str(backup_target), "sha256": sha256_file(backup_target)}

    result["attempted"] = True
    result["modify_asset"] = safe_call(asset.modify, True) if hasattr(asset, "modify") else {"ok": False, "error": "asset.modify unavailable"}
    result["modify_cdo"] = safe_call(cdo.modify, True) if hasattr(cdo, "modify") else {"ok": False, "error": "cdo.modify unavailable"}
    writes = {
        "pan_bounds_horizontal": write_prop(cdo, "pan_bounds_horizontal", TARGET_PAN_HORIZONTAL),
        "pan_bounds_vertical": write_prop(cdo, "pan_bounds_vertical", TARGET_PAN_VERTICAL),
        "zoom_distance_list": write_prop(cdo, "zoom_distance_list", TARGET_ZOOM_DISTANCES),
        "zoom_level_thresholds": write_prop(cdo, "zoom_level_thresholds", TARGET_ZOOM_THRESHOLDS),
    }
    result["writes"] = writes
    result["applied"] = all(item.get("ok") for item in writes.values())
    if result["applied"]:
        result["saved"] = bool(unreal.EditorAssetLibrary.save_loaded_asset(asset, True))
    return result


def strip_refs(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: strip_refs(item) for key, item in value.items() if not key.startswith("_")}
    if isinstance(value, list):
        return [strip_refs(item) for item in value]
    return value


def write_report(report: dict[str, Any]) -> None:
    clean = strip_refs(report)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(clean, indent=2, sort_keys=True, default=str), encoding="utf-8")

    result = clean.get("result", {})
    lines = [
        "# UE4 StarMapPawn Bounds Patch Gate - 2026-05-12",
        "",
        f"- Generated: `{clean['generated_utc']}`",
        f"- Apply requested: `{clean['apply_requested']}`",
        f"- Asset path: `{ASSET_PATH}`",
        f"- Target mod file: `{TARGET_ASSET_FILE}`",
        f"- Target pan horizontal: `{TARGET_PAN_HORIZONTAL}`",
        f"- Target pan vertical: `{TARGET_PAN_VERTICAL}`",
        f"- Target zoom distances: `{TARGET_ZOOM_DISTANCES}`",
        f"- Target zoom thresholds: `{TARGET_ZOOM_THRESHOLDS}`",
        "",
        "## Extents",
        "",
        f"- CSV extent summary: `{clean.get('csv_extents')}`",
        "",
        "## Pawn",
        "",
        f"- Asset object path: `{clean.get('pawn', {}).get('asset_object_path')}`",
        f"- Blueprint class: `{clean.get('pawn', {}).get('blueprint_class_path')}`",
        f"- CDO path: `{clean.get('pawn', {}).get('cdo_path')}`",
        f"- Defaults before: `{clean.get('pawn', {}).get('defaults')}`",
        "",
        "## Safety",
        "",
    ]
    if clean["safety_failures"]:
        for failure in clean["safety_failures"]:
            lines.append(f"- FAIL: {failure}")
    else:
        lines.append("- No safety failures.")

    lines.extend(
        [
            "",
            "## Result",
            "",
            f"- Attempted: `{result.get('attempted')}`",
            f"- Applied: `{result.get('applied')}`",
            f"- Saved: `{result.get('saved')}`",
            f"- Reason: `{result.get('reason')}`",
            f"- Writes: `{result.get('writes')}`",
            f"- Backup: `{result.get('pre_patch_backup')}`",
            "",
            "## Hashes",
            "",
            f"- Target before: `{clean.get('target_asset_hash_before')}`",
            f"- Target after: `{clean.get('target_asset_hash_after')}`",
            f"- Base unchanged: `{clean.get('base_asset_unchanged')}`",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    report: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "apply_requested": APPLY,
        "target_mod_name": TARGET_MOD_NAME,
        "asset_path": ASSET_PATH,
        "target_asset_file": str(TARGET_ASSET_FILE),
        "base_asset_file": str(BASE_ASSET_FILE),
        "target_asset_hash_before": sha256_file(TARGET_ASSET_FILE),
        "base_asset_hash_before": sha256_file(BASE_ASSET_FILE),
        "targets": {
            "pan_bounds_horizontal": TARGET_PAN_HORIZONTAL,
            "pan_bounds_vertical": TARGET_PAN_VERTICAL,
            "zoom_distance_list": TARGET_ZOOM_DISTANCES,
            "zoom_level_thresholds": TARGET_ZOOM_THRESHOLDS,
        },
        "csv_extents": csv_extent_summary(CSV_PATH),
        "pawn": {},
    }
    try:
        report["pawn"] = load_pawn()
    except Exception:
        report["pawn_exception"] = traceback.format_exc()
    report["safety_failures"] = build_safety(report)
    report["result"] = apply_patch(report)
    report["target_asset_hash_after"] = sha256_file(TARGET_ASSET_FILE)
    report["base_asset_hash_after"] = sha256_file(BASE_ASSET_FILE)
    report["base_asset_unchanged"] = (
        report.get("base_asset_hash_before") is not None
        and report.get("base_asset_hash_before") == report.get("base_asset_hash_after")
    )
    write_report(report)
    if unreal is not None:
        unreal.log(f"TKU StarMapPawn bounds patch gate wrote {OUT_JSON}")
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")
    if EXIT_EDITOR and unreal is not None:
        try:
            unreal.SystemLibrary.quit_editor()
        except Exception:
            pass


if __name__ == "__main__":
    main()
