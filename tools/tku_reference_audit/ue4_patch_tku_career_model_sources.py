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


REPORT_STEM = "ue4_career_model_sources_patch"
TARGET_MOD_NAME = os.environ.get("TKU_CAREER_MODEL_MOD_NAME", "TKUCompatEditorPatch").strip()
APPLY = os.environ.get("TKU_CAREER_MODEL_APPLY", "").strip().lower() in {"1", "true", "yes", "y", "on"}

MODE_SOURCE_ASSETS = (
    "/Game/Modes/MW5GameMode",
    "/Game/Modes/CampaignMode",
    "/Game/DLC1/CareerMode/StartConditions/CareerMode",
)
INNER_SPHERE_SOURCE_ASSET = "/Game/InnerSphereData/StarSystemGenerator"
CAMPAIGN_GENERATOR_SOURCE_ASSET = "/Game/Campaign/_common/DefaultSystemGenerator"
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
BACKUP_DIR = REPORT_DIR / "backups" / f"{TARGET_MOD_NAME}_career_model_sources_patch"


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
    return PLUGIN_DIR / "ModOverride" / f"{strip_game_prefix(source_asset)}.uasset"


def path_name(obj: Any) -> str | None:
    try:
        return text(obj.get_path_name())
    except Exception:
        return None


def read_class_prop(cdo: Any, prop: str) -> dict[str, Any]:
    try:
        value = cdo.get_editor_property(prop)
        return {"ok": True, "value": jsonable(value), "path": path_name(value)}
    except Exception as exc:
        return {"ok": False, "error": f"{type(exc).__name__}: {exc}"}


def inspect_blueprint(asset_path: str) -> dict[str, Any]:
    out: dict[str, Any] = {"asset_path": asset_path}
    try:
        out["exists"] = bool(unreal.EditorAssetLibrary.does_asset_exist(asset_path))
    except Exception as exc:
        out["exists_error"] = f"{type(exc).__name__}: {exc}"
        out["exists"] = False
    if not out["exists"]:
        return out
    try:
        asset = unreal.EditorAssetLibrary.load_asset(asset_path)
        out["asset"] = jsonable(asset)
        out["asset_class"] = path_name(asset.get_class()) if hasattr(asset, "get_class") else None
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


def backup_target_file(target_file: Path) -> dict[str, Any] | None:
    if not target_file.is_file():
        return None
    backup_target = BACKUP_DIR / target_file.relative_to(PLUGIN_DIR)
    backup_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(target_file, backup_target)
    return {"path": str(backup_target), "sha256": sha256_file(backup_target)}


def duplicate_or_load(source_asset: str, target_asset: str) -> Any:
    if unreal.EditorAssetLibrary.does_asset_exist(target_asset):
        return unreal.EditorAssetLibrary.load_asset(target_asset)
    target_dir = "/".join(target_asset.split("/")[:-1])
    unreal.EditorAssetLibrary.make_directory(target_dir)
    return unreal.EditorAssetLibrary.duplicate_asset(source_asset, target_asset)


def build_safety(report: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    if TARGET_MOD_NAME != "TKUCompatEditorPatch":
        failures.append(f"unexpected target mod name: {TARGET_MOD_NAME}")
    if not PLUGIN_DIR.is_dir():
        failures.append(f"target plugin dir missing: {PLUGIN_DIR}")
    descriptor = PLUGIN_DIR / f"{TARGET_MOD_NAME}.uplugin"
    if not descriptor.is_file():
        failures.append(f"target plugin descriptor missing: {descriptor}")

    inner_path = report.get("inner_sphere_class_path")
    if not inner_path or not inner_path.startswith(TARGET_PREFIX):
        failures.append(f"inner sphere class did not resolve to target mod override: {inner_path}")

    campaign_target = target_asset_path(CAMPAIGN_GENERATOR_SOURCE_ASSET)
    if not campaign_target.startswith(f"/ModOverride/{TARGET_MOD_NAME}/Campaign/_common/"):
        failures.append(f"unexpected campaign generator target: {campaign_target}")

    for source in MODE_SOURCE_ASSETS:
        target = target_asset_path(source)
        target_file = target_file_path(source)
        if not target.startswith(TARGET_PREFIX):
            failures.append(f"unexpected target asset path: {target}")
        try:
            target_file.resolve().relative_to(PLUGIN_DIR.resolve())
        except ValueError:
            failures.append(f"target file outside plugin dir: {target_file}")
    return failures


def apply_patch(report: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {"attempted": False, "applied": False, "saved": False, "reason": None, "assets": []}
    if report["safety_failures"]:
        result["reason"] = "safety failures"
        return result
    if not APPLY:
        result["reason"] = "dry run only"
        return result

    inner_class = unreal.EditorAssetLibrary.load_blueprint_class(INNER_SPHERE_SOURCE_ASSET)
    if not inner_class:
        result["reason"] = "inner sphere class failed to load"
        return result
    if not (path_name(inner_class) or "").startswith(TARGET_PREFIX):
        result["reason"] = f"inner sphere class resolved outside target mod: {path_name(inner_class)}"
        return result

    result["attempted"] = True
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    campaign_target = target_asset_path(CAMPAIGN_GENERATOR_SOURCE_ASSET)
    campaign_target_file = target_file_path(CAMPAIGN_GENERATOR_SOURCE_ASSET)
    campaign_result: dict[str, Any] = {
        "source_asset": CAMPAIGN_GENERATOR_SOURCE_ASSET,
        "target_asset": campaign_target,
        "target_file": str(campaign_target_file),
        "backup": backup_target_file(campaign_target_file),
    }
    campaign_asset = duplicate_or_load(CAMPAIGN_GENERATOR_SOURCE_ASSET, campaign_target)
    campaign_result["asset"] = jsonable(campaign_asset)
    campaign_result["saved"] = bool(unreal.EditorAssetLibrary.save_loaded_asset(campaign_asset, True)) if campaign_asset else False
    campaign_class = unreal.EditorAssetLibrary.load_blueprint_class(campaign_target)
    campaign_result["blueprint_class"] = jsonable(campaign_class)
    campaign_result["class_path"] = path_name(campaign_class)
    result["assets"].append(campaign_result)
    if not campaign_class:
        result["reason"] = "campaign generator class failed to load"
        return result

    all_saved = bool(campaign_result["saved"])
    for source in MODE_SOURCE_ASSETS:
        target = target_asset_path(source)
        target_file = target_file_path(source)
        asset_result: dict[str, Any] = {
            "source_asset": source,
            "target_asset": target,
            "target_file": str(target_file),
            "backup": backup_target_file(target_file),
        }
        asset = duplicate_or_load(source, target)
        asset_result["asset"] = jsonable(asset)
        if not asset:
            asset_result["error"] = "duplicate_or_load returned None"
            all_saved = False
            result["assets"].append(asset_result)
            continue
        bp_class = unreal.EditorAssetLibrary.load_blueprint_class(target)
        asset_result["blueprint_class"] = jsonable(bp_class)
        if not bp_class:
            asset_result["error"] = "target Blueprint class failed to load"
            all_saved = False
            result["assets"].append(asset_result)
            continue
        cdo = unreal.get_default_object(bp_class)
        if hasattr(asset, "modify"):
            asset_result["modify_asset"] = safe("asset.modify", asset.modify, True)
        if hasattr(cdo, "modify"):
            asset_result["modify_cdo"] = safe("cdo.modify", cdo.modify, True)
        asset_result["before_default_inner_sphere_class"] = read_class_prop(cdo, "default_inner_sphere_class")
        asset_result["before_campaign_system_generator_class"] = read_class_prop(cdo, "campaign_system_generator_class")
        try:
            cdo.set_editor_property("default_inner_sphere_class", inner_class)
            cdo.set_editor_property("campaign_system_generator_class", campaign_class)
            asset_result["after_default_inner_sphere_class"] = read_class_prop(cdo, "default_inner_sphere_class")
            asset_result["after_campaign_system_generator_class"] = read_class_prop(cdo, "campaign_system_generator_class")
            asset_result["saved"] = bool(unreal.EditorAssetLibrary.save_loaded_asset(asset, True))
            all_saved = all_saved and asset_result["saved"]
        except Exception:
            asset_result["exception"] = traceback.format_exc()
            all_saved = False
        result["assets"].append(asset_result)

    result["applied"] = all(
        item.get("saved") is True
        for item in result["assets"]
    )
    result["saved"] = all_saved
    return result


def write_report(report: dict[str, Any]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True, default=str), encoding="utf-8")

    result = report.get("result", {})
    lines = [
        "# UE4 Career Model Sources Patch",
        "",
        f"- Generated: `{report['generated_utc']}`",
        f"- Apply requested: `{report['apply_requested']}`",
        f"- InnerSphere class: `{report.get('inner_sphere_class_path')}`",
        f"- Campaign generator target: `{target_asset_path(CAMPAIGN_GENERATOR_SOURCE_ASSET)}`",
        "- Scope: MW5GameMode, CampaignMode, and DLC1 CareerMode class defaults.",
        "",
        "## Safety",
        "",
    ]
    if report["safety_failures"]:
        for failure in report["safety_failures"]:
            lines.append(f"- FAIL: {failure}")
    else:
        lines.append("- No safety failures.")
    lines.extend(["", "## Result", ""])
    lines.append(f"- Attempted: `{result.get('attempted')}`")
    lines.append(f"- Applied: `{result.get('applied')}`")
    lines.append(f"- Saved: `{result.get('saved')}`")
    lines.append(f"- Reason: `{result.get('reason')}`")

    lines.extend(["", "## Assets", ""])
    for item in result.get("assets", []):
        lines.append(f"### `{item.get('target_asset')}`")
        lines.append(f"- Source: `{item.get('source_asset')}`")
        lines.append(f"- File: `{item.get('target_file')}`")
        lines.append(f"- Saved: `{item.get('saved')}`")
        if item.get("backup"):
            lines.append(f"- Backup: `{item['backup'].get('path')}`")
        if item.get("after_default_inner_sphere_class"):
            lines.append(f"- DefaultInnerSphereClass: `{item['after_default_inner_sphere_class'].get('path')}`")
        if item.get("after_campaign_system_generator_class"):
            lines.append(f"- CampaignSystemGeneratorClass: `{item['after_campaign_system_generator_class'].get('path')}`")
        if item.get("error"):
            lines.append(f"- Error: `{item.get('error')}`")
        if item.get("exception"):
            lines.append("- Exception: see JSON report.")
        lines.append("")

    lines.extend(["## Before/After", ""])
    for mode in report.get("modes", []):
        lines.append(f"### `{mode['source_asset']}`")
        lines.append(f"- Target: `{mode['target_asset']}`")
        before = mode.get("target_before") or mode.get("source_before") or {}
        after = mode.get("target_after") or {}
        lines.append(f"- Before DefaultInnerSphereClass: `{(before.get('default_inner_sphere_class') or {}).get('path')}`")
        lines.append(f"- Before CampaignSystemGeneratorClass: `{(before.get('campaign_system_generator_class') or {}).get('path')}`")
        lines.append(f"- After DefaultInnerSphereClass: `{(after.get('default_inner_sphere_class') or {}).get('path')}`")
        lines.append(f"- After CampaignSystemGeneratorClass: `{(after.get('campaign_system_generator_class') or {}).get('path')}`")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    report: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "apply_requested": APPLY,
        "target_mod_name": TARGET_MOD_NAME,
        "plugin_dir": str(PLUGIN_DIR),
        "inner_sphere_source_asset": INNER_SPHERE_SOURCE_ASSET,
        "campaign_generator_source_asset": CAMPAIGN_GENERATOR_SOURCE_ASSET,
        "campaign_generator_target_asset": target_asset_path(CAMPAIGN_GENERATOR_SOURCE_ASSET),
        "modes": [],
        "errors": [],
        "safety_failures": [],
        "result": {"attempted": False, "applied": False, "saved": False, "reason": "not run"},
    }
    try:
        inner_class = unreal.EditorAssetLibrary.load_blueprint_class(INNER_SPHERE_SOURCE_ASSET)
        report["inner_sphere_class_path"] = path_name(inner_class)
        report["campaign_generator_before"] = inspect_blueprint(CAMPAIGN_GENERATOR_SOURCE_ASSET)
        campaign_target = target_asset_path(CAMPAIGN_GENERATOR_SOURCE_ASSET)
        report["campaign_generator_target_before"] = inspect_blueprint(campaign_target) if unreal.EditorAssetLibrary.does_asset_exist(campaign_target) else None
        for source in MODE_SOURCE_ASSETS:
            target = target_asset_path(source)
            mode: dict[str, Any] = {
                "source_asset": source,
                "target_asset": target,
                "target_file": str(target_file_path(source)),
                "source_before": inspect_blueprint(source),
                "target_before": inspect_blueprint(target) if unreal.EditorAssetLibrary.does_asset_exist(target) else None,
            }
            report["modes"].append(mode)
        report["safety_failures"] = build_safety(report)
        report["result"] = apply_patch(report)
        report["campaign_generator_target_after"] = inspect_blueprint(campaign_target) if unreal.EditorAssetLibrary.does_asset_exist(campaign_target) else None
        for mode in report["modes"]:
            mode["target_after"] = inspect_blueprint(mode["target_asset"]) if unreal.EditorAssetLibrary.does_asset_exist(mode["target_asset"]) else None
    except Exception:
        report["errors"].append({"fatal": traceback.format_exc()})
        report["safety_failures"].append("fatal exception before completion; see errors")
        report["result"] = {"attempted": False, "applied": False, "saved": False, "reason": "fatal exception"}
    finally:
        write_report(report)
        unreal.log(f"TKU career model sources patch wrote {OUT_JSON}")


main()
