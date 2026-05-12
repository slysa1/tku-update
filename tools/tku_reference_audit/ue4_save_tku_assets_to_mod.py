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


REPORT_STEM = "ue4_save_assets_to_mod_20260512"
TARGET_MOD_NAME = os.environ.get("TKU_SAVE_ASSETS_MOD_NAME", "TKUCompatEditorPatch").strip()
APPLY = os.environ.get("TKU_SAVE_ASSETS_APPLY", "").strip().lower() in {"1", "true", "yes", "y", "on"}
DEFAULT_ASSETS = ["/Game/InnerSphereData/StarSystemGenerator"]


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
BACKUP_DIR = REPORT_DIR / "backups" / f"{TARGET_MOD_NAME}_assets_pre_save_20260512"


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


def parse_assets() -> list[str]:
    raw = os.environ.get("TKU_SAVE_ASSETS_LIST", "").strip()
    if not raw:
        return DEFAULT_ASSETS
    try:
        value = json.loads(raw)
        if isinstance(value, str):
            return [value]
        return [str(item) for item in value]
    except Exception:
        return [piece.strip() for piece in raw.split(";") if piece.strip()]


ASSET_PATHS = parse_assets()


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


def remove_prefix(value: str, prefix: str) -> str:
    if value.startswith(prefix):
        return value[len(prefix) :]
    return value


def source_physical_path(asset_path: str) -> Path | None:
    if not asset_path.startswith("/Game/"):
        return None
    rel = remove_prefix(asset_path, "/Game/")
    for suffix in (".uasset", ".umap"):
        candidate = EDITOR_PROJECT / "Content" / f"{rel}{suffix}"
        if candidate.is_file():
            return candidate
    return None


def target_asset_path(source_asset_path: str) -> str:
    if not source_asset_path.startswith("/Game/"):
        raise ValueError(f"source asset must be under /Game: {source_asset_path}")
    rel = remove_prefix(source_asset_path, "/Game/")
    return f"/ModOverride/{TARGET_MOD_NAME}/{rel}"


def target_physical_path(source_asset_path: str, target_path: str) -> Path | None:
    source_file = source_physical_path(source_asset_path)
    if source_file is None:
        return None
    rel = remove_prefix(target_path, f"/ModOverride/{TARGET_MOD_NAME}/")
    return PLUGIN_DIR / "ModOverride" / f"{rel}{source_file.suffix}"


def inspect_asset(source_asset_path: str) -> dict[str, Any]:
    target_path = target_asset_path(source_asset_path)
    source_file = source_physical_path(source_asset_path)
    target_file = target_physical_path(source_asset_path, target_path)
    target_exists_in_registry = bool(unreal.EditorAssetLibrary.does_asset_exist(target_path))
    return {
        "source_asset_path": source_asset_path,
        "target_asset_path": target_path,
        "source_file": str(source_file) if source_file else None,
        "source_file_exists": bool(source_file and source_file.is_file()),
        "source_sha256_before": sha256_file(source_file) if source_file else None,
        "target_file": str(target_file) if target_file else None,
        "target_file_exists_before": bool(target_file and target_file.is_file()),
        "target_sha256_before": sha256_file(target_file) if target_file else None,
        "target_asset_exists_before": target_exists_in_registry,
        "target_load_before": jsonable(unreal.EditorAssetLibrary.load_asset(target_path))
        if target_exists_in_registry
        else None,
    }


def build_safety(asset_report: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    source = asset_report["source_asset_path"]
    target = asset_report["target_asset_path"]
    target_file_raw = asset_report.get("target_file")
    target_file = Path(target_file_raw) if target_file_raw else None
    if TARGET_MOD_NAME != "TKUCompatEditorPatch":
        failures.append(f"unexpected target mod name: {TARGET_MOD_NAME}")
    if not source.startswith("/Game/"):
        failures.append(f"source is not a /Game asset: {source}")
    if not target.startswith("/ModOverride/TKUCompatEditorPatch/"):
        failures.append(f"target is not the expected ModOverride path: {target}")
    if not PLUGIN_DIR.is_dir():
        failures.append(f"target plugin dir missing: {PLUGIN_DIR}")
    if not (PLUGIN_DIR / f"{TARGET_MOD_NAME}.uplugin").is_file():
        failures.append(f"target plugin descriptor missing: {PLUGIN_DIR / (TARGET_MOD_NAME + '.uplugin')}")
    if not asset_report.get("source_file_exists"):
        failures.append(f"source physical file missing: {asset_report.get('source_file')}")
    if target_file is None:
        failures.append("could not resolve target physical file")
    elif not is_relative_to(target_file, PLUGIN_DIR):
        failures.append(f"target file is outside plugin dir: {target_file}")
    return failures


def save_asset_to_mod(asset_report: dict[str, Any]) -> None:
    source = asset_report["source_asset_path"]
    target = asset_report["target_asset_path"]
    target_file = Path(asset_report["target_file"])

    asset_report["result"] = {"attempted": False, "saved": False, "reason": None}
    asset_report["safety_failures"] = build_safety(asset_report)

    source_asset = unreal.EditorAssetLibrary.load_asset(source)
    asset_report["source_load"] = jsonable(source_asset)
    if source_asset is None:
        asset_report["safety_failures"].append(f"source asset failed to load: {source}")

    if asset_report["safety_failures"]:
        asset_report["result"]["reason"] = "safety failures"
        return
    if not APPLY:
        asset_report["result"]["reason"] = "dry run only"
        return

    if target_file.is_file():
        BACKUP_DIR.mkdir(parents=True, exist_ok=True)
        backup_target = BACKUP_DIR / target_file.relative_to(PLUGIN_DIR)
        backup_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(target_file, backup_target)
        asset_report["preexisting_target_backup"] = {
            "path": str(backup_target),
            "sha256": sha256_file(backup_target),
        }
        unreal.EditorAssetLibrary.delete_asset(target)

    target_dir = "/".join(target.split("/")[:-1])
    unreal.EditorAssetLibrary.make_directory(target_dir)
    asset_report["result"]["attempted"] = True
    duplicated = unreal.EditorAssetLibrary.duplicate_asset(source, target)
    asset_report["duplicate_result"] = jsonable(duplicated)
    if duplicated is None:
        asset_report["result"]["reason"] = "duplicate_asset returned None"
        return
    asset_report["result"]["saved"] = bool(unreal.EditorAssetLibrary.save_asset(target, only_if_is_dirty=False))
    if not asset_report["result"]["saved"]:
        asset_report["result"]["reason"] = "save_asset returned false"


def write_report(report: dict[str, Any]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")

    lines = [
        "# UE4 Save Assets To Mod - 2026-05-12",
        "",
        f"- Generated: `{report['generated_utc']}`",
        f"- Apply requested: `{report['apply_requested']}`",
        f"- Target mod: `{TARGET_MOD_NAME}`",
        "",
        "## Assets",
        "",
    ]
    for asset in report["assets"]:
        result = asset.get("result", {})
        lines.append(f"### `{asset['source_asset_path']}`")
        lines.append(f"- Target: `{asset['target_asset_path']}`")
        lines.append(f"- Source file: `{asset.get('source_file')}`")
        lines.append(f"- Target file: `{asset.get('target_file')}`")
        lines.append(f"- Safety failures: `{asset.get('safety_failures', [])}`")
        lines.append(f"- Attempted: `{result.get('attempted')}`")
        lines.append(f"- Saved: `{result.get('saved')}`")
        lines.append(f"- Reason: `{result.get('reason')}`")
        lines.append(f"- Target hash before: `{asset.get('target_sha256_before')}`")
        lines.append(f"- Target hash after: `{asset.get('target_sha256_after')}`")
        lines.append(f"- Reload after: `{asset.get('target_load_after')}`")
        lines.append("")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    report: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "apply_requested": APPLY,
        "target_mod_name": TARGET_MOD_NAME,
        "plugin_dir": str(PLUGIN_DIR),
        "assets": [],
        "errors": [],
    }
    try:
        for source_asset_path in ASSET_PATHS:
            asset_report = inspect_asset(source_asset_path)
            save_asset_to_mod(asset_report)
            target_file = Path(asset_report["target_file"]) if asset_report.get("target_file") else None
            asset_report["target_file_exists_after"] = bool(target_file and target_file.is_file())
            asset_report["target_sha256_after"] = sha256_file(target_file) if target_file else None
            if unreal.EditorAssetLibrary.does_asset_exist(asset_report["target_asset_path"]):
                asset_report["target_load_after"] = jsonable(
                    unreal.EditorAssetLibrary.load_asset(asset_report["target_asset_path"])
                )
            else:
                asset_report["target_load_after"] = None
            report["assets"].append(asset_report)
    except Exception:
        report["errors"].append(traceback.format_exc())
    write_report(report)


if __name__ == "__main__":
    main()
