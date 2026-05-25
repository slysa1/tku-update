from __future__ import annotations

import hashlib
import json
import os
import shutil
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import unreal


REPORT_STEM = "ue4_game_mode_inner_sphere_patch"
TARGET_MOD_NAME = os.environ.get("TKU_GAME_MODE_MOD_NAME", "TKUCompatEditorPatch").strip()
APPLY = os.environ.get("TKU_GAME_MODE_APPLY", "").strip().lower() in {"1", "true", "yes", "y", "on"}

SOURCE_ASSETS = (
    "/Game/Modes/MW5GameMode",
    "/Game/Modes/CampaignMode",
)
GENERATOR_SOURCE_ASSET = "/Game/InnerSphereData/StarSystemGenerator"
GENERATOR_EXPECTED_TARGET_ASSET = f"/ModOverride/{TARGET_MOD_NAME}/InnerSphereData/StarSystemGenerator"
TARGET_PREFIX = f"/ModOverride/{TARGET_MOD_NAME}/"


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
BACKUP_DIR = REPORT_DIR / "backups" / f"{TARGET_MOD_NAME}_game_modes_pre_inner_sphere_patch"


def read_config() -> dict[str, Any]:
    for candidate in CONFIG_PATHS:
        if candidate and candidate.is_file():
            return json.loads(candidate.read_text(encoding="utf-8"))
    return {}


CONFIG = read_config()
EDITOR_ROOT = Path(os.environ.get("TKU_MW5_EDITOR_ROOT") or CONFIG.get("mw5_editor_root") or r"E:\Games\MechWarrior5Editor")
EDITOR_PROJECT = EDITOR_ROOT / "MW5Mercs"
PLUGIN_DIR = EDITOR_PROJECT / "Plugins" / TARGET_MOD_NAME


def text(value: Any) -> str:
    try:
        return str(value)
    except Exception:
        return repr(value)


def jsonable(value: Any, depth: int = 0) -> Any:
    if depth > 4:
        return text(value)
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {text(k): jsonable(v, depth + 1) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [jsonable(item, depth + 1) for item in value]
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


def safe(label: str, func, *args) -> dict[str, Any]:
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


def strip_game_prefix(asset_path: str) -> str:
    if not asset_path.startswith("/Game/"):
        raise ValueError(f"expected /Game asset path: {asset_path}")
    return asset_path[len("/Game/") :]


def target_asset_path(source_asset: str) -> str:
    return TARGET_PREFIX + strip_game_prefix(source_asset)


def target_file_path(source_asset: str) -> Path:
    rel = strip_game_prefix(source_asset)
    return PLUGIN_DIR / "ModOverride" / f"{rel}.uasset"


def path_name(obj: Any) -> str | None:
    try:
        return text(obj.get_path_name())
    except Exception:
        return None


def extracted_path(value: Any) -> str | None:
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        for key in ("get_path_name", "path", "resolved_class_path", "resolved_asset_path"):
            candidate = value.get(key)
            if isinstance(candidate, str):
                return candidate
    return None


def read_class_prop(cdo: Any, prop: str) -> dict[str, Any]:
    try:
        value = cdo.get_editor_property(prop)
        return {"ok": True, "value": jsonable(value), "path": path_name(value)}
    except Exception as exc:
        return {"ok": False, "error": f"{type(exc).__name__}: {exc}"}


def inspect_mode(asset_path: str) -> dict[str, Any]:
    out: dict[str, Any] = {"asset_path": asset_path}
    out["exists"] = safe("does_asset_exist", unreal.EditorAssetLibrary.does_asset_exist, asset_path)
    try:
        asset = unreal.EditorAssetLibrary.load_asset(asset_path)
        out["asset"] = jsonable(asset)
        bp_class = unreal.EditorAssetLibrary.load_blueprint_class(asset_path)
        out["blueprint_class"] = jsonable(bp_class)
        if bp_class:
            cdo = unreal.get_default_object(bp_class)
            out["cdo"] = jsonable(cdo)
            out["default_inner_sphere_class"] = read_class_prop(cdo, "default_inner_sphere_class")
            out["campaign_system_generator_class"] = read_class_prop(cdo, "campaign_system_generator_class")
    except Exception as exc:
        out["error"] = f"{type(exc).__name__}: {exc}"
    return out


def inspect_generator() -> dict[str, Any]:
    out: dict[str, Any] = {
        "source_asset": GENERATOR_SOURCE_ASSET,
        "expected_target_asset": GENERATOR_EXPECTED_TARGET_ASSET,
    }
    out["source_exists"] = safe("does_asset_exist", unreal.EditorAssetLibrary.does_asset_exist, GENERATOR_SOURCE_ASSET)
    try:
        asset = unreal.EditorAssetLibrary.load_asset(GENERATOR_SOURCE_ASSET)
        out["asset"] = jsonable(asset)
        out["resolved_asset_path"] = path_name(asset)
        bp_class = unreal.EditorAssetLibrary.load_blueprint_class(GENERATOR_SOURCE_ASSET)
        out["blueprint_class"] = jsonable(bp_class)
        out["resolved_class_path"] = path_name(bp_class)
    except Exception as exc:
        out["error"] = f"{type(exc).__name__}: {exc}"
    return out


def build_safety(report: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if TARGET_MOD_NAME != "TKUCompatEditorPatch":
        failures.append(f"unexpected target mod name: {TARGET_MOD_NAME}")
    if not PLUGIN_DIR.is_dir():
        failures.append(f"target plugin dir missing: {PLUGIN_DIR}")
    if not (PLUGIN_DIR / f"{TARGET_MOD_NAME}.uplugin").is_file():
        failures.append(f"target plugin descriptor missing: {PLUGIN_DIR / (TARGET_MOD_NAME + '.uplugin')}")
    gen = report.get("generator", {})
    gen_class_path = gen.get("resolved_class_path") or extracted_path(gen.get("blueprint_class") or {})
    if not gen_class_path:
        failures.append(f"generator class did not resolve: {gen}")
    elif not gen_class_path.startswith(TARGET_PREFIX):
        failures.append(f"generator class did not resolve to target mod override: {gen_class_path}")
    for mode in report.get("modes", []):
        source = mode["source_asset"]
        target = mode["target_asset"]
        target_file = Path(mode["target_file"])
        if not source.startswith("/Game/Modes/"):
            failures.append(f"unexpected source mode path: {source}")
        if not target.startswith(f"/ModOverride/{TARGET_MOD_NAME}/Modes/"):
            failures.append(f"unexpected target mode path: {target}")
        try:
            target_file.resolve().relative_to(PLUGIN_DIR.resolve())
        except ValueError:
            failures.append(f"target mode file is outside plugin dir: {target_file}")
    return failures


def duplicate_or_load_target(mode: dict[str, Any]) -> Any:
    target = mode["target_asset"]
    source = mode["source_asset"]
    if unreal.EditorAssetLibrary.does_asset_exist(target):
        return unreal.EditorAssetLibrary.load_asset(target)
    target_dir = "/".join(target.split("/")[:-1])
    unreal.EditorAssetLibrary.make_directory(target_dir)
    return unreal.EditorAssetLibrary.duplicate_asset(source, target)


def apply_patch(report: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {"attempted": False, "applied": False, "saved": False, "modes": []}
    if report["safety_failures"]:
        result["reason"] = "safety failures"
        return result
    if not APPLY:
        result["reason"] = "dry run only"
        return result

    generator_class = unreal.EditorAssetLibrary.load_blueprint_class(GENERATOR_SOURCE_ASSET)
    if not generator_class:
        result["reason"] = f"generator class failed to load: {GENERATOR_SOURCE_ASSET}"
        return result
    generator_class_path = path_name(generator_class)
    if not generator_class_path or not generator_class_path.startswith(TARGET_PREFIX):
        result["reason"] = f"generator class resolved outside target mod override: {generator_class_path}"
        return result
    result["generator_class_path"] = generator_class_path

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    result["attempted"] = True
    all_saved = True
    for mode in report["modes"]:
        mode_result: dict[str, Any] = {
            "source_asset": mode["source_asset"],
            "target_asset": mode["target_asset"],
            "target_file": mode["target_file"],
            "attempted": True,
            "saved": False,
        }
        target_file = Path(mode["target_file"])
        if target_file.is_file():
            backup_target = BACKUP_DIR / target_file.relative_to(PLUGIN_DIR)
            backup_target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(target_file, backup_target)
            mode_result["backup"] = {"path": str(backup_target), "sha256": sha256_file(backup_target)}
        asset = duplicate_or_load_target(mode)
        mode_result["asset"] = jsonable(asset)
        if not asset:
            mode_result["error"] = "duplicate_or_load_target returned None"
            all_saved = False
            result["modes"].append(mode_result)
            continue
        bp_class = unreal.EditorAssetLibrary.load_blueprint_class(mode["target_asset"])
        mode_result["blueprint_class"] = jsonable(bp_class)
        if not bp_class:
            mode_result["error"] = "target Blueprint class failed to load"
            all_saved = False
            result["modes"].append(mode_result)
            continue
        cdo = unreal.get_default_object(bp_class)
        mode_result["before_default_inner_sphere_class"] = read_class_prop(cdo, "default_inner_sphere_class")
        if hasattr(asset, "modify"):
            mode_result["modify_asset"] = safe("asset.modify", asset.modify, True)
        if hasattr(cdo, "modify"):
            mode_result["modify_cdo"] = safe("cdo.modify", cdo.modify, True)
        try:
            cdo.set_editor_property("default_inner_sphere_class", generator_class)
            mode_result["write_default_inner_sphere_class"] = read_class_prop(cdo, "default_inner_sphere_class")
            mode_result["campaign_system_generator_class_after"] = read_class_prop(cdo, "campaign_system_generator_class")
            mode_result["saved"] = bool(unreal.EditorAssetLibrary.save_loaded_asset(asset, True))
            all_saved = all_saved and mode_result["saved"]
        except Exception:
            mode_result["exception"] = traceback.format_exc()
            all_saved = False
        result["modes"].append(mode_result)
    result["applied"] = all(item.get("write_default_inner_sphere_class", {}).get("ok") for item in result["modes"])
    result["saved"] = all_saved
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
        "# UE4 Game Mode InnerSphereClass Patch",
        "",
        f"- Generated: `{clean['generated_utc']}`",
        f"- Apply requested: `{clean['apply_requested']}`",
        f"- Generator source asset: `{GENERATOR_SOURCE_ASSET}`",
        f"- Expected resolved target asset: `{GENERATOR_EXPECTED_TARGET_ASSET}`",
        f"- Resolved generator class: `{clean.get('generator', {}).get('resolved_class_path')}`",
        "",
        "## Safety",
        "",
    ]
    if clean["safety_failures"]:
        for failure in clean["safety_failures"]:
            lines.append(f"- FAIL: {failure}")
    else:
        lines.append("- No safety failures.")
    lines.extend(["", "## Result", ""])
    lines.append(f"- Attempted: `{result.get('attempted')}`")
    lines.append(f"- Applied: `{result.get('applied')}`")
    lines.append(f"- Saved: `{result.get('saved')}`")
    lines.append(f"- Reason: `{result.get('reason')}`")
    lines.extend(["", "## Modes", ""])
    for mode in clean.get("modes", []):
        source_before = mode.get("source_before") or {}
        target_before = mode.get("target_before") or {}
        target_after = mode.get("target_after") or {}
        lines.append(f"### `{mode['source_asset']}`")
        lines.append(f"- Target: `{mode['target_asset']}`")
        lines.append(f"- Source before default inner sphere: `{source_before.get('default_inner_sphere_class')}`")
        lines.append(f"- Target before: `{target_before.get('default_inner_sphere_class')}`")
        lines.append(f"- Target after: `{target_after.get('default_inner_sphere_class')}`")
        lines.append(f"- Target hash before: `{mode.get('target_hash_before')}`")
        lines.append(f"- Target hash after: `{mode.get('target_hash_after')}`")
    for mode_result in result.get("modes", []):
        lines.append(f"- Apply `{mode_result.get('target_asset')}` saved `{mode_result.get('saved')}` write `{mode_result.get('write_default_inner_sphere_class')}`")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    report: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "apply_requested": APPLY,
        "target_mod_name": TARGET_MOD_NAME,
        "plugin_dir": str(PLUGIN_DIR),
        "generator_source_asset": GENERATOR_SOURCE_ASSET,
        "generator_expected_target_asset": GENERATOR_EXPECTED_TARGET_ASSET,
        "generator": {},
        "modes": [],
        "errors": [],
        "safety_failures": [],
        "result": {"attempted": False, "applied": False, "saved": False, "reason": "not run"},
        "completed": False,
    }
    try:
        try:
            report["generator"] = inspect_generator()
        except Exception:
            report["errors"].append({"generator": traceback.format_exc()})

        for source in SOURCE_ASSETS:
            target = target_asset_path(source)
            target_file = target_file_path(source)
            mode_report: dict[str, Any] = {
                "source_asset": source,
                "target_asset": target,
                "target_file": str(target_file),
                "target_exists_before": unreal.EditorAssetLibrary.does_asset_exist(target),
                "target_file_exists_before": target_file.is_file(),
                "target_hash_before": sha256_file(target_file),
                "source_before": inspect_mode(source),
                "target_before": inspect_mode(target) if unreal.EditorAssetLibrary.does_asset_exist(target) else None,
            }
            report["modes"].append(mode_report)
        report["safety_failures"] = build_safety(report)
        report["result"] = apply_patch(report)
        for mode in report["modes"]:
            target_file = Path(mode["target_file"])
            mode["target_exists_after"] = unreal.EditorAssetLibrary.does_asset_exist(mode["target_asset"])
            mode["target_file_exists_after"] = target_file.is_file()
            mode["target_hash_after"] = sha256_file(target_file)
            mode["target_after"] = inspect_mode(mode["target_asset"]) if mode["target_exists_after"] else None
        report["completed"] = True
    except Exception:
        report["errors"].append({"fatal": traceback.format_exc()})
        report["safety_failures"] = report.get("safety_failures", []) + ["fatal exception before completion; see errors"]
        report["result"] = {"attempted": False, "applied": False, "saved": False, "reason": "fatal exception"}
    finally:
        write_report(report)
        unreal.log(f"TKU game mode InnerSphereClass patch wrote {OUT_JSON}")


main()
