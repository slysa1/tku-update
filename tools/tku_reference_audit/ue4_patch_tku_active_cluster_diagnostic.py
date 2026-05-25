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


REPORT_STEM = "ue4_active_cluster_diagnostic_patch"
TARGET_MOD_NAME = os.environ.get("TKU_ACTIVE_CLUSTER_DIAG_MOD_NAME", "TKUCompatEditorPatch").strip()
APPLY = os.environ.get("TKU_ACTIVE_CLUSTER_DIAG_APPLY", "").strip().lower() in {
    "1",
    "true",
    "yes",
    "y",
    "on",
}

SOURCE_CLUSTER_ASSET = os.environ.get(
    "TKU_ACTIVE_CLUSTER_DIAG_SOURCE",
    "/Game/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset",
).strip()
DIAGNOSTIC_SYSTEM_IDS = tuple(
    int(value)
    for value in os.environ.get("TKU_ACTIVE_CLUSTER_DIAG_IDS", "4088,4089,4090").replace(";", ",").split(",")
    if value.strip()
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
BACKUP_DIR = REPORT_DIR / "backups" / f"{TARGET_MOD_NAME}_active_cluster_diagnostic_patch"


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
            "sample": [jsonable(item, depth + 1) for item in values[:40]],
            "tail_sample": [jsonable(item, depth + 1) for item in values[-20:]],
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


TARGET_CLUSTER_ASSET = target_asset_path(SOURCE_CLUSTER_ASSET)


def target_file_path(source_asset: str) -> Path:
    return PLUGIN_DIR / "ModOverride" / f"{strip_game_prefix(source_asset)}.uasset"


def manifest_asset_path(source_asset: str) -> str:
    return f"/Game/{strip_game_prefix(source_asset)}.uasset"


def backup_target_file(target_file: Path) -> dict[str, Any] | None:
    if not target_file.is_file():
        return None
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    backup_target = BACKUP_DIR / target_file.relative_to(PLUGIN_DIR)
    backup_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(target_file, backup_target)
    return {"path": str(backup_target), "sha256": sha256_file(backup_target)}


def asset_exists(path: str) -> bool:
    try:
        return bool(unreal.EditorAssetLibrary.does_asset_exist(path))
    except Exception:
        return False


def duplicate_or_load(source_asset: str, target_asset: str) -> Any:
    if asset_exists(target_asset):
        return unreal.EditorAssetLibrary.load_asset(target_asset)
    target_dir = "/".join(target_asset.split("/")[:-1])
    unreal.EditorAssetLibrary.make_directory(target_dir)
    return unreal.EditorAssetLibrary.duplicate_asset(source_asset, target_asset)


def read_cluster_properties(asset: Any) -> dict[str, Any]:
    props: dict[str, Any] = {}
    for name in ("system_ids", "cluster_faction_asset", "cluster_overlay", "cluster_constellation", "is_legacy_cluster", "toi_data"):
        try:
            props[name] = jsonable(asset.get_editor_property(name))
        except Exception as exc:
            props[name] = f"{type(exc).__name__}: {exc}"
    return props


def system_ids_from_asset(asset: Any) -> list[int]:
    raw = asset.get_editor_property("system_ids")
    return sorted(int(value) for value in list(raw))


def set_cluster_system_ids(asset: Any, system_ids: list[int]) -> dict[str, Any]:
    result: dict[str, Any] = {"method_result": None, "property_result": None}
    method = getattr(asset, "set_cluster_system_ids_editoronly", None)
    if method:
        try:
            result["method_result"] = {"ok": True, "value": jsonable(method(system_ids))}
        except Exception as exc:
            result["method_result"] = {"ok": False, "error": f"{type(exc).__name__}: {exc}"}
    else:
        result["method_result"] = {"ok": False, "error": "method unavailable"}
    try:
        result["property_result"] = {"ok": True, "value": jsonable(asset.set_editor_property("system_ids", system_ids))}
    except Exception as exc:
        result["property_result"] = {"ok": False, "error": f"{type(exc).__name__}: {exc}"}
    return result


def build_safety() -> list[str]:
    failures: list[str] = []
    if TARGET_MOD_NAME != "TKUCompatEditorPatch":
        failures.append(f"unexpected target mod name: {TARGET_MOD_NAME}")
    if not SOURCE_CLUSTER_ASSET.startswith("/Game/DLC1/CareerMode/Clusters/"):
        failures.append(f"source cluster outside expected active career cluster root: {SOURCE_CLUSTER_ASSET}")
    if not DIAGNOSTIC_SYSTEM_IDS:
        failures.append("no diagnostic system ids provided")
    if not PLUGIN_DIR.is_dir():
        failures.append(f"target plugin dir missing: {PLUGIN_DIR}")
    descriptor = PLUGIN_DIR / f"{TARGET_MOD_NAME}.uplugin"
    if not descriptor.is_file():
        failures.append(f"target plugin descriptor missing: {descriptor}")
    if not asset_exists(SOURCE_CLUSTER_ASSET):
        failures.append(f"source cluster asset missing: {SOURCE_CLUSTER_ASSET}")
    target_file = target_file_path(SOURCE_CLUSTER_ASSET)
    try:
        target_file.resolve().relative_to(PLUGIN_DIR.resolve())
    except ValueError:
        failures.append(f"target file outside plugin dir: {target_file}")
    return failures


def apply_patch(safety_failures: list[str]) -> dict[str, Any]:
    result: dict[str, Any] = {
        "attempted": False,
        "applied": False,
        "saved": False,
        "reason": None,
        "source_asset": SOURCE_CLUSTER_ASSET,
        "target_asset": TARGET_CLUSTER_ASSET,
        "target_file": str(target_file_path(SOURCE_CLUSTER_ASSET)),
        "manifest_asset": manifest_asset_path(SOURCE_CLUSTER_ASSET),
        "diagnostic_system_ids": list(DIAGNOSTIC_SYSTEM_IDS),
    }
    if safety_failures:
        result["reason"] = "safety failures"
        return result
    if not APPLY:
        result["reason"] = "dry run only"
        source_asset = unreal.EditorAssetLibrary.load_asset(SOURCE_CLUSTER_ASSET)
        result["source_properties"] = read_cluster_properties(source_asset)
        return result

    result["attempted"] = True
    target_file = target_file_path(SOURCE_CLUSTER_ASSET)
    result["backup"] = backup_target_file(target_file)

    asset = duplicate_or_load(SOURCE_CLUSTER_ASSET, TARGET_CLUSTER_ASSET)
    result["target_asset_object"] = jsonable(asset)
    if not asset:
        result["reason"] = "duplicate/load returned None"
        return result

    if hasattr(asset, "modify"):
        try:
            result["modify_result"] = jsonable(asset.modify(True))
        except Exception as exc:
            result["modify_result"] = f"{type(exc).__name__}: {exc}"

    before_ids = system_ids_from_asset(asset)
    result["before_system_ids"] = before_ids
    merged_ids = sorted(set(before_ids).union(DIAGNOSTIC_SYSTEM_IDS))
    result["after_system_ids_planned"] = merged_ids
    result["added_system_ids"] = sorted(set(merged_ids) - set(before_ids))
    result["before_properties"] = read_cluster_properties(asset)
    result["set_results"] = set_cluster_system_ids(asset, merged_ids)
    result["after_properties"] = read_cluster_properties(asset)
    result["saved"] = bool(unreal.EditorAssetLibrary.save_loaded_asset(asset, True))
    result["applied"] = bool(result["saved"] and set(DIAGNOSTIC_SYSTEM_IDS).issubset(set(system_ids_from_asset(asset))))
    return result


def write_report(report: dict[str, Any]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True, default=str), encoding="utf-8")

    result = report.get("result", {})
    lines = [
        "# UE4 Active Cluster Diagnostic Patch",
        "",
        f"- Generated: `{report['generated_utc']}`",
        f"- Apply requested: `{report['apply_requested']}`",
        f"- Target mod: `{TARGET_MOD_NAME}`",
        f"- Source cluster: `{SOURCE_CLUSTER_ASSET}`",
        f"- Target cluster: `{TARGET_CLUSTER_ASSET}`",
        f"- Manifest entry: `{manifest_asset_path(SOURCE_CLUSTER_ASSET)}`",
        f"- Diagnostic system IDs: `{list(DIAGNOSTIC_SYSTEM_IDS)}`",
        f"- Backup dir: `{BACKUP_DIR if APPLY else None}`",
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
            "## Result",
            "",
            f"- Attempted: `{result.get('attempted')}`",
            f"- Applied: `{result.get('applied')}`",
            f"- Saved: `{result.get('saved')}`",
            f"- Reason: `{result.get('reason')}`",
            f"- Added system IDs: `{result.get('added_system_ids')}`",
            f"- Before count: `{len(result.get('before_system_ids') or [])}`",
            f"- After planned count: `{len(result.get('after_system_ids_planned') or [])}`",
        ]
    )
    if result.get("backup"):
        lines.append(f"- Backup: `{result['backup'].get('path')}`")
    if report.get("errors"):
        lines.extend(["", "## Errors", ""])
        for error in report["errors"]:
            lines.append(f"- `{error}`")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    report: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "apply_requested": APPLY,
        "target_mod_name": TARGET_MOD_NAME,
        "source_cluster_asset": SOURCE_CLUSTER_ASSET,
        "target_cluster_asset": TARGET_CLUSTER_ASSET,
        "diagnostic_system_ids": list(DIAGNOSTIC_SYSTEM_IDS),
        "plugin_dir": str(PLUGIN_DIR),
        "safety_failures": [],
        "errors": [],
        "result": {"attempted": False, "applied": False, "saved": False, "reason": "not run"},
    }
    try:
        report["safety_failures"] = build_safety()
        report["result"] = apply_patch(report["safety_failures"])
    except Exception:
        report["errors"].append({"fatal": traceback.format_exc()})
        report["safety_failures"].append("fatal exception before completion; see errors")
        report["result"] = {"attempted": False, "applied": False, "saved": False, "reason": "fatal exception"}
    finally:
        write_report(report)
        unreal.log(f"TKU active cluster diagnostic patch wrote {OUT_JSON}")


main()
