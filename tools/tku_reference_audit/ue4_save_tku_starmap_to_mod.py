from __future__ import annotations

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


REPORT_STEM = "ue4_starmap_save_to_mod_20260511"
TARGET_MOD_NAME = os.environ.get("TKU_STARMAP_EXPECT_MOD_NAME", "TKUCompatEditorPatch").strip()
APPLY = os.environ.get("TKU_STARMAP_APPLY", "").strip().lower() in {"1", "true", "yes", "y", "on"}

BASE_MAP_ASSET = "/Game/Levels/FrontEnd/StarMap"
TARGET_MAP_ASSET = f"/ModOverride/{TARGET_MOD_NAME}/Levels/FrontEnd/StarMap"


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
BACKUP_DIR = REPORT_DIR / "backups" / f"{TARGET_MOD_NAME}_starmap_pre_save_20260511"


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
BASE_MAP_FILE = EDITOR_PROJECT / "Content" / "Levels" / "FrontEnd" / "StarMap.umap"
TARGET_MAP_FILE = PLUGIN_DIR / "ModOverride" / "Levels" / "FrontEnd" / "StarMap.umap"


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


def is_relative_to(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


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


def inspect_current_level() -> dict[str, Any]:
    out: dict[str, Any] = {}
    if unreal is None:
        out["error"] = "unreal module is not available; run through MW5 UE4Editor-Cmd."
        return out

    try:
        actors = list(unreal.EditorLevelLibrary.get_all_level_actors())
    except Exception as exc:
        out["actors_error"] = f"{type(exc).__name__}: {exc}"
        return out

    class_counts = Counter(get_class_name(actor) for actor in actors)
    star_ids: list[int] = []
    samples: list[dict[str, Any]] = []
    for actor in actors:
        cls = get_class_name(actor)
        label = actor_label(actor)
        joined = f"{label} {cls}".lower()
        if "starsystembody" not in joined:
            continue
        sid = read_prop(actor, "star_system_id")
        if isinstance(sid, int):
            star_ids.append(sid)
        if len(samples) < 10:
            try:
                loc = actor.get_actor_location()
                loc_json = {"x": float(loc.x), "y": float(loc.y), "z": float(loc.z)}
            except Exception:
                loc_json = None
            samples.append(
                {
                    "label": label,
                    "class": cls,
                    "path": get_path_name(actor),
                    "star_system_id": sid,
                    "desired_zoom_level": read_prop(actor, "desired_zoom_level"),
                    "location": loc_json,
                }
            )

    out.update(
        {
            "actor_count": len(actors),
            "class_counts_top": dict(class_counts.most_common(20)),
            "star_system_body_count": len(star_ids),
            "star_system_body_id_range": {
                "min": min(star_ids) if star_ids else None,
                "max": max(star_ids) if star_ids else None,
            },
            "duplicate_star_system_ids": sorted(
                sid for sid, count in Counter(star_ids).items() if count > 1
            )[:100],
            "sample_star_system_bodies": samples,
        }
    )
    return out


def mod_target_status() -> dict[str, Any]:
    plugin_file = PLUGIN_DIR / f"{TARGET_MOD_NAME}.uplugin"
    active_mod_file = PLUGIN_DIR / "ActiveMod.txt"
    return {
        "target_mod_name": TARGET_MOD_NAME,
        "plugin_dir": str(PLUGIN_DIR),
        "plugin_dir_exists": PLUGIN_DIR.is_dir(),
        "plugin_file": str(plugin_file),
        "plugin_file_exists": plugin_file.is_file(),
        "active_mod_file": str(active_mod_file),
        "active_mod_file_exists": active_mod_file.is_file(),
        "active_mod_text": active_mod_file.read_text(encoding="utf-8", errors="replace").strip()
        if active_mod_file.is_file()
        else None,
    }


def build_safety(report: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if unreal is None:
        failures.append("unreal module unavailable")
    if TARGET_MOD_NAME != "TKUCompatEditorPatch":
        failures.append(f"unexpected target mod name: {TARGET_MOD_NAME}")
    if TARGET_MAP_ASSET != "/ModOverride/TKUCompatEditorPatch/Levels/FrontEnd/StarMap":
        failures.append(f"unexpected target map asset path: {TARGET_MAP_ASSET}")
    if not PLUGIN_DIR.is_dir():
        failures.append(f"target plugin dir missing: {PLUGIN_DIR}")
    if not (PLUGIN_DIR / f"{TARGET_MOD_NAME}.uplugin").is_file():
        failures.append(f"target plugin descriptor missing: {PLUGIN_DIR / (TARGET_MOD_NAME + '.uplugin')}")
    if not BASE_MAP_FILE.is_file():
        failures.append(f"base StarMap file missing: {BASE_MAP_FILE}")
    if not is_relative_to(TARGET_MAP_FILE, PLUGIN_DIR):
        failures.append(f"target map file is outside plugin dir: {TARGET_MAP_FILE}")
    if report.get("base_map_hash_before") is None:
        failures.append("could not hash base StarMap before operation")
    return failures


def write_report(report: dict[str, Any]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True, default=str), encoding="utf-8")

    result = report.get("result", {})
    lines = [
        "# UE4 StarMap Save To Mod Gate - 2026-05-11",
        "",
        f"- Generated: `{report['generated_utc']}`",
        f"- Apply requested: `{report['apply_requested']}`",
        f"- Base map asset: `{BASE_MAP_ASSET}`",
        f"- Target map asset: `{TARGET_MAP_ASSET}`",
        f"- Target physical file: `{TARGET_MAP_FILE}`",
        "",
        "## Mod Target",
        "",
        f"- Found: `{report['mod_target'].get('plugin_file_exists')}`",
        f"- Filesystem: `{report['mod_target']}`",
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
            "## Probe",
            "",
            f"- Base hash before: `{report.get('base_map_hash_before')}`",
            f"- Target existed before: `{report.get('target_map_exists_before')}`",
            f"- Base load ok: `{report.get('base_load', {}).get('ok')}`",
            f"- Loaded level actors: `{report.get('loaded_level', {})}`",
            "",
            "## Result",
            "",
            f"- Attempted: `{result.get('attempted')}`",
            f"- Saved: `{result.get('saved')}`",
            f"- Reason: `{result.get('reason')}`",
            f"- Target exists after: `{report.get('target_map_exists_after')}`",
            f"- Target hash after: `{report.get('target_map_hash_after')}`",
            f"- Base hash after: `{report.get('base_map_hash_after')}`",
            f"- Base unchanged: `{report.get('base_map_unchanged')}`",
            f"- Reload target ok: `{report.get('target_reload', {}).get('ok')}`",
            f"- Target level actors: `{report.get('target_level', {})}`",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    report: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "apply_requested": APPLY,
        "target_mod_name": TARGET_MOD_NAME,
        "base_map_asset": BASE_MAP_ASSET,
        "target_map_asset": TARGET_MAP_ASSET,
        "base_map_file": str(BASE_MAP_FILE),
        "target_map_file": str(TARGET_MAP_FILE),
        "mod_target": mod_target_status(),
        "base_map_hash_before": sha256_file(BASE_MAP_FILE),
        "target_map_exists_before": TARGET_MAP_FILE.is_file(),
        "target_map_hash_before": sha256_file(TARGET_MAP_FILE),
    }
    report["safety_failures"] = build_safety(report)
    report["result"] = {
        "attempted": False,
        "saved": False,
        "reason": None,
    }

    if unreal is None:
        report["result"]["reason"] = "unreal module is unavailable"
        write_report(report)
        return

    try:
        report["base_load"] = safe_call(unreal.EditorLoadingAndSavingUtils.load_map, BASE_MAP_ASSET)
        if report["base_load"].get("ok"):
            report["loaded_level"] = inspect_current_level()
    except Exception:
        report["base_load_exception"] = traceback.format_exc()

    if report["safety_failures"]:
        report["result"]["reason"] = "safety failures"
    elif not report.get("base_load", {}).get("ok"):
        report["result"]["reason"] = "base map load failed"
    elif not APPLY:
        report["result"]["reason"] = "dry run only"
    else:
        try:
            if TARGET_MAP_FILE.is_file():
                BACKUP_DIR.mkdir(parents=True, exist_ok=True)
                backup_target = BACKUP_DIR / TARGET_MAP_FILE.name
                shutil.copy2(TARGET_MAP_FILE, backup_target)
                report["preexisting_target_backup"] = {
                    "path": str(backup_target),
                    "sha256": sha256_file(backup_target),
                }
            TARGET_MAP_FILE.parent.mkdir(parents=True, exist_ok=True)
            world = unreal.EditorLevelLibrary.get_editor_world()
            report["result"]["attempted"] = True
            report["result"]["saved"] = bool(
                unreal.EditorLoadingAndSavingUtils.save_map(world, TARGET_MAP_ASSET)
            )
        except Exception:
            report["result"]["exception"] = traceback.format_exc()

    report["target_map_exists_after"] = TARGET_MAP_FILE.is_file()
    report["target_map_hash_after"] = sha256_file(TARGET_MAP_FILE)
    report["base_map_hash_after"] = sha256_file(BASE_MAP_FILE)
    report["base_map_unchanged"] = (
        report.get("base_map_hash_before") is not None
        and report.get("base_map_hash_before") == report.get("base_map_hash_after")
    )

    if TARGET_MAP_FILE.is_file() and unreal is not None:
        try:
            report["target_reload"] = safe_call(unreal.EditorLoadingAndSavingUtils.load_map, TARGET_MAP_ASSET)
            if report["target_reload"].get("ok"):
                report["target_level"] = inspect_current_level()
        except Exception:
            report["target_reload_exception"] = traceback.format_exc()

    write_report(report)


if __name__ == "__main__":
    main()
