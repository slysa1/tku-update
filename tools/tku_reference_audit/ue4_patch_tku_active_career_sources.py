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


REPORT_STEM = "ue4_active_career_sources_patch"
TARGET_MOD_NAME = os.environ.get("TKU_ACTIVE_CAREER_MOD_NAME", "TKUCompatEditorPatch").strip()
APPLY = os.environ.get("TKU_ACTIVE_CAREER_APPLY", "").strip().lower() in {"1", "true", "yes", "y", "on"}

START_CONDITIONS_PATH = "/Game/DLC1/CareerMode/StartConditions"
CORE_SOURCE_ASSETS = (
    "/Game/DLC1/CareerMode/StartConditions/CareerMode_Start",
    "/Game/DLC1/CareerMode/StartConditions/FRR_CareerMode_Start",
    "/Game/DLC1/CareerMode/CareerModeCoreCampaign",
    "/Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters",
    "/Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones",
)
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
BACKUP_DIR = REPORT_DIR / "backups" / f"{TARGET_MOD_NAME}_active_career_sources_patch"


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
        values = list(value)
        return {
            "kind": type(value).__name__,
            "count": len(values),
            "sample": [jsonable(item, depth + 1) for item in values[:20]],
            "tail_sample": [jsonable(item, depth + 1) for item in values[-10:]],
        }

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


def path_name(obj: Any) -> str | None:
    try:
        return text(obj.get_path_name())
    except Exception:
        return None


def class_name(obj: Any) -> str | None:
    try:
        return text(obj.get_class().get_name())
    except Exception:
        return None


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


def manifest_asset_path(source_asset: str) -> str:
    relative = strip_game_prefix(source_asset)
    suffix = ".umap" if relative.startswith("Levels/") else ".uasset"
    return f"/Game/{relative}{suffix}"


def safe_read_property(asset: Any, prop: str) -> dict[str, Any]:
    try:
        value = asset.get_editor_property(prop)
        return {"ok": True, "value": jsonable(value), "path": path_name(value)}
    except Exception as exc:
        return {"ok": False, "error": f"{type(exc).__name__}: {exc}"}


def focused_properties(asset: Any) -> dict[str, Any]:
    props: dict[str, Any] = {}
    for name in (
        "associated_faction_asset_id",
        "campaign_arc",
        "campaign_arc_script",
        "campaign_event_list",
        "initial_star_map_borders",
        "run_campaign_arc_script_on_save",
        "starting_date",
        "starting_system_id",
        "sub_campaigns",
    ):
        result = safe_read_property(asset, name)
        if result["ok"]:
            props[name] = result["value"]
    return props


def inspect_asset(asset_path: str) -> dict[str, Any]:
    out: dict[str, Any] = {
        "asset_path": asset_path,
        "target_asset": target_asset_path(asset_path) if asset_path.startswith("/Game/") else None,
        "manifest_asset": manifest_asset_path(asset_path) if asset_path.startswith("/Game/") else None,
    }
    try:
        out["exists"] = bool(unreal.EditorAssetLibrary.does_asset_exist(asset_path))
    except Exception as exc:
        out["exists"] = False
        out["exists_error"] = f"{type(exc).__name__}: {exc}"
        return out
    if not out["exists"]:
        return out
    try:
        asset = unreal.EditorAssetLibrary.load_asset(asset_path)
        out["asset"] = jsonable(asset)
        out["class_name"] = class_name(asset)
        out["path_name"] = path_name(asset)
        out["focused_properties"] = focused_properties(asset)
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


def discover_start_condition_assets() -> list[str]:
    registry = unreal.AssetRegistryHelpers.get_asset_registry()
    discovered: list[str] = []
    for asset_data in list(registry.get_assets_by_path(START_CONDITIONS_PATH, False)):
        package_name = text(asset_data.package_name)
        if not package_name.startswith(f"{START_CONDITIONS_PATH}/"):
            continue
        asset = unreal.EditorAssetLibrary.load_asset(package_name)
        if class_name(asset) == "MWStartConditionsAsset":
            discovered.append(package_name)
    return sorted(discovered)


def build_source_assets() -> list[str]:
    sources: list[str] = []
    seen: set[str] = set()
    for source in discover_start_condition_assets() + list(CORE_SOURCE_ASSETS):
        if source not in seen:
            sources.append(source)
            seen.add(source)
    return sources


def build_safety(source_assets: list[str]) -> list[str]:
    failures: list[str] = []
    if TARGET_MOD_NAME != "TKUCompatEditorPatch":
        failures.append(f"unexpected target mod name: {TARGET_MOD_NAME}")
    if not PLUGIN_DIR.is_dir():
        failures.append(f"target plugin dir missing: {PLUGIN_DIR}")
    descriptor = PLUGIN_DIR / f"{TARGET_MOD_NAME}.uplugin"
    if not descriptor.is_file():
        failures.append(f"target plugin descriptor missing: {descriptor}")
    if len([path for path in source_assets if path.startswith(f"{START_CONDITIONS_PATH}/")]) < 6:
        failures.append("too few CareerMode start-condition assets discovered")

    for source in source_assets:
        target = target_asset_path(source)
        target_file = target_file_path(source)
        if not source.startswith("/Game/"):
            failures.append(f"unexpected non-/Game source asset: {source}")
        if not target.startswith(TARGET_PREFIX):
            failures.append(f"unexpected target asset path: {target}")
        try:
            target_file.resolve().relative_to(PLUGIN_DIR.resolve())
        except ValueError:
            failures.append(f"target file outside plugin dir: {target_file}")
    return failures


def apply_patch(source_assets: list[str], safety_failures: list[str]) -> dict[str, Any]:
    result: dict[str, Any] = {
        "attempted": False,
        "applied": False,
        "saved": False,
        "reason": None,
        "assets": [],
    }
    if safety_failures:
        result["reason"] = "safety failures"
        return result
    if not APPLY:
        result["reason"] = "dry run only"
        return result

    result["attempted"] = True
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    all_saved = True
    for source in source_assets:
        target = target_asset_path(source)
        target_file = target_file_path(source)
        item: dict[str, Any] = {
            "source_asset": source,
            "target_asset": target,
            "target_file": str(target_file),
            "manifest_asset": manifest_asset_path(source),
            "source_before": inspect_asset(source),
            "target_before": inspect_asset(target) if unreal.EditorAssetLibrary.does_asset_exist(target) else None,
            "backup": backup_target_file(target_file),
        }
        try:
            asset = duplicate_or_load(source, target)
            item["asset"] = jsonable(asset)
            if hasattr(asset, "modify"):
                asset.modify(True)
            item["saved"] = bool(unreal.EditorAssetLibrary.save_loaded_asset(asset, True)) if asset else False
            item["target_after"] = inspect_asset(target)
            all_saved = all_saved and bool(item["saved"])
        except Exception:
            item["exception"] = traceback.format_exc()
            item["saved"] = False
            all_saved = False
        result["assets"].append(item)

    result["applied"] = all(item.get("saved") is True for item in result["assets"])
    result["saved"] = all_saved
    return result


def write_report(report: dict[str, Any]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True, default=str), encoding="utf-8")

    result = report.get("result", {})
    lines = [
        "# UE4 Active Career Sources Patch",
        "",
        f"- Generated: `{report['generated_utc']}`",
        f"- Apply requested: `{report['apply_requested']}`",
        f"- Source asset count: `{len(report.get('source_assets', []))}`",
        "- Scope: current-schema CareerMode start conditions plus active career root/cluster/safezone arcs.",
        "- Intent: create packageable `/Game` override sources for the assets the live Davion career start actually uses.",
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
        lines.append(f"- Manifest entry: `{item.get('manifest_asset')}`")
        lines.append(f"- File: `{item.get('target_file')}`")
        lines.append(f"- Saved: `{item.get('saved')}`")
        if item.get("backup"):
            lines.append(f"- Backup: `{item['backup'].get('path')}`")
        source_props = ((item.get("source_before") or {}).get("focused_properties") or {})
        target_props = ((item.get("target_after") or {}).get("focused_properties") or {})
        for prop in ("campaign_arc", "initial_star_map_borders", "starting_system_id", "sub_campaigns", "campaign_event_list"):
            if prop in source_props or prop in target_props:
                lines.append(f"- {prop}: source=`{text(source_props.get(prop))[:260]}` target=`{text(target_props.get(prop))[:260]}`")
        if item.get("exception"):
            lines.append("- Exception: see JSON report.")
        lines.append("")

    if report.get("errors"):
        lines.extend(["## Errors", ""])
        for error in report["errors"]:
            lines.append(f"- `{error}`")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    report: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "apply_requested": APPLY,
        "target_mod_name": TARGET_MOD_NAME,
        "plugin_dir": str(PLUGIN_DIR),
        "source_assets": [],
        "dry_run_assets": [],
        "safety_failures": [],
        "errors": [],
        "result": {"attempted": False, "applied": False, "saved": False, "reason": "not run"},
    }
    try:
        source_assets = build_source_assets()
        report["source_assets"] = source_assets
        report["dry_run_assets"] = [inspect_asset(asset_path) for asset_path in source_assets]
        report["safety_failures"] = build_safety(source_assets)
        report["result"] = apply_patch(source_assets, report["safety_failures"])
    except Exception:
        report["errors"].append({"fatal": traceback.format_exc()})
        report["safety_failures"].append("fatal exception before completion; see errors")
        report["result"] = {"attempted": False, "applied": False, "saved": False, "reason": "fatal exception"}
    finally:
        write_report(report)
        unreal.log(f"TKU active career sources patch wrote {OUT_JSON}")


main()
