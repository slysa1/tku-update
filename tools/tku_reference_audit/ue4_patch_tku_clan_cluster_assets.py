from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import shutil
import traceback
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import unreal


REPORT_STEM = "ue4_tku_clan_cluster_assets_patch"
TARGET_MOD_NAME = os.environ.get("TKU_CLAN_CLUSTER_MOD_NAME", "TKUCompatEditorPatch").strip()
APPLY = os.environ.get("TKU_CLAN_CLUSTER_APPLY", "").strip().lower() in {"1", "true", "yes", "y", "on"}
USE_PLACEHOLDER_OVERLAYS = os.environ.get("TKU_CLAN_CLUSTER_PLACEHOLDER_OVERLAYS", "").strip().lower() in {
    "1",
    "true",
    "yes",
    "y",
    "on",
}

SOURCE_CSV_RELATIVE = Path("reports/tku_editor_first/tku_inner_sphere_merged_current_plus_tku_additions_20260510.utf8.csv")
CLUSTER_IDS = ("ClanConflict", "RepairSystem_Clan")
TARGET_PREFIX = f"/ModOverride/{TARGET_MOD_NAME}/"

SOURCE_ASSETS = {
    "cluster_conflict_template": "/Game/Campaign/Clusters/OutworldsAlliance/OutworldsAlliance_ClusterAsset",
    "cluster_repair_template": "/Game/Campaign/Clusters/IndustrialHub_25/IndustrialHub_25_ClusterAsset",
    "faction_conflict_template": "/Game/Campaign/Clusters/OutworldsAlliance/OutworldsBorder",
    "faction_repair_template": "/Game/Campaign/Clusters/IndustrialHub_25/RepairSystem_20",
    "conflict_overlay_placeholder": "/Game/Campaign/Clusters/OutworldsAlliance/15_1",
    "repair_overlay_placeholder": "/Game/Campaign/Clusters/IndustrialHub_25/Safezone1_Collision",
    "repair_constellation_placeholder": "/Game/Campaign/Clusters/IndustrialHub_25/Safezone1",
}


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
BACKUP_DIR = REPORT_DIR / "backups" / f"{TARGET_MOD_NAME}_clan_cluster_assets_patch"


def read_config() -> dict[str, Any]:
    for candidate in CONFIG_PATHS:
        if candidate and candidate.is_file():
            return json.loads(candidate.read_text(encoding="utf-8"))
    return {}


CONFIG = read_config()
EDITOR_ROOT = Path(os.environ.get("TKU_MW5_EDITOR_ROOT") or CONFIG.get("mw5_editor_root") or r"E:\Games\MechWarrior5Editor")
EDITOR_PROJECT = EDITOR_ROOT / "MW5Mercs"
PLUGIN_DIR = EDITOR_PROJECT / "Plugins" / TARGET_MOD_NAME
SOURCE_CSV = PROJECT_ROOT / SOURCE_CSV_RELATIVE


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


def is_relative_to(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except ValueError:
        return False


def cluster_id_from_value(value: str) -> str:
    if not value:
        return ""
    match = re.search(r"MWFactionAsset:([^\"\)]+)", value)
    return match.group(1) if match else ""


def sanitize_asset_piece(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_]+", "_", value).strip("_")
    return cleaned or "None"


def overlay_suffix(overlay: str, constellation: str) -> str:
    if overlay in ("", "None", None) and constellation in ("", "None", None):
        return "NoOverlay"
    base = Path(str(overlay).split(".", 1)[0]).name
    return sanitize_asset_piece(base)


def load_cluster_groups() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    groups: dict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    omitted: list[dict[str, Any]] = []
    with SOURCE_CSV.open("r", encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            try:
                system_id = int(row.get("---") or row.get("Name") or "")
            except ValueError:
                continue
            name = row.get("StarSystemName") or ""
            cluster_id = cluster_id_from_value(row.get("Cluster") or "")
            is_clan_candidate = "(Clan)" in name or cluster_id in CLUSTER_IDS or system_id in {4565, 5554, 6979}
            if not is_clan_candidate:
                continue
            if cluster_id not in CLUSTER_IDS:
                omitted.append(
                    {
                        "system_id": system_id,
                        "star_system_name": name,
                        "cluster_id": cluster_id,
                        "reason": "not one of the targeted current-schema clan cluster ids",
                    }
                )
                continue
            overlay = row.get("ClusterOverlay") or "None"
            constellation = row.get("ClusterConstellation") or "None"
            groups[(cluster_id, overlay, constellation)].append(
                {
                    "system_id": system_id,
                    "star_system_name": name,
                    "overlay": overlay,
                    "constellation": constellation,
                }
            )

    planned: list[dict[str, Any]] = []
    for (cluster_id, overlay, constellation), rows in sorted(groups.items()):
        suffix = overlay_suffix(overlay, constellation)
        target_dir = f"/ModOverride/{TARGET_MOD_NAME}/Campaign/Clusters/TKU_{cluster_id}"
        if suffix != "NoOverlay":
            target_dir += f"_{suffix}"
        planned.append(
            {
                "cluster_id": cluster_id,
                "overlay": overlay,
                "constellation": constellation,
                "system_ids": sorted(row["system_id"] for row in rows),
                "systems": sorted(rows, key=lambda item: item["system_id"]),
                "target_dir": target_dir,
                "target_cluster_asset": f"{target_dir}/TKU_{cluster_id}_{suffix}_ClusterAsset",
                "target_faction_asset": f"/ModOverride/{TARGET_MOD_NAME}/Campaign/Clusters/TKU_{cluster_id}/{cluster_id}",
                "source_cluster_asset": SOURCE_ASSETS[
                    "cluster_repair_template" if cluster_id == "RepairSystem_Clan" else "cluster_conflict_template"
                ],
                "source_faction_asset": SOURCE_ASSETS[
                    "faction_repair_template" if cluster_id == "RepairSystem_Clan" else "faction_conflict_template"
                ],
            }
        )
    return planned, omitted


def plugin_file_for_asset(asset_path: str) -> Path:
    if not asset_path.startswith(TARGET_PREFIX):
        raise ValueError(f"target asset is outside expected mod override: {asset_path}")
    relative = asset_path[len(TARGET_PREFIX) :]
    return PLUGIN_DIR / "ModOverride" / f"{relative}.uasset"


def backup_target(asset_path: str) -> dict[str, Any] | None:
    target_file = plugin_file_for_asset(asset_path)
    if not target_file.is_file():
        return None
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


def load_optional_asset(asset_path: str | None) -> Any:
    if not asset_path or asset_path == "None":
        return None
    return unreal.EditorAssetLibrary.load_asset(asset_path)


def placeholder_assets_for(group: dict[str, Any]) -> dict[str, str | None]:
    if not USE_PLACEHOLDER_OVERLAYS or group["overlay"] in ("", "None", None):
        return {"overlay_asset": None, "constellation_asset": None}
    if group["cluster_id"] == "RepairSystem_Clan":
        return {
            "overlay_asset": SOURCE_ASSETS["repair_overlay_placeholder"],
            "constellation_asset": SOURCE_ASSETS["repair_constellation_placeholder"],
        }
    return {
        "overlay_asset": SOURCE_ASSETS["conflict_overlay_placeholder"],
        "constellation_asset": None,
    }


def try_set_cluster_value(asset: Any, method_name: str, property_name: str, value: Any) -> dict[str, Any]:
    result: dict[str, Any] = {
        "method": method_name,
        "property": property_name,
        "method_result": None,
        "property_result": None,
    }
    method = getattr(asset, method_name, None)
    if method:
        result["method_result"] = safe(method_name, method, value)
    else:
        result["method_result"] = {"ok": False, "error": "method unavailable"}
    result["property_result"] = safe(f"set_editor_property:{property_name}", asset.set_editor_property, property_name, value)
    return result


def read_cluster_properties(asset: Any) -> dict[str, Any]:
    props: dict[str, Any] = {}
    for name in ("system_ids", "cluster_faction_asset", "cluster_overlay", "cluster_constellation", "is_legacy_cluster", "toi_data"):
        try:
            props[name] = jsonable(asset.get_editor_property(name))
        except Exception as exc:
            props[name] = f"{type(exc).__name__}: {exc}"
    return props


def build_safety(planned_groups: list[dict[str, Any]]) -> list[str]:
    failures: list[str] = []
    if TARGET_MOD_NAME != "TKUCompatEditorPatch":
        failures.append(f"unexpected target mod name: {TARGET_MOD_NAME}")
    if not SOURCE_CSV.is_file():
        failures.append(f"source CSV missing: {SOURCE_CSV}")
    if not PLUGIN_DIR.is_dir():
        failures.append(f"target plugin dir missing: {PLUGIN_DIR}")
    descriptor = PLUGIN_DIR / f"{TARGET_MOD_NAME}.uplugin"
    if not descriptor.is_file():
        failures.append(f"target plugin descriptor missing: {descriptor}")
    if not planned_groups:
        failures.append("no targeted clan cluster groups were discovered")
    for label, source in SOURCE_ASSETS.items():
        if label.endswith("_placeholder") and not USE_PLACEHOLDER_OVERLAYS:
            continue
        if not asset_exists(source):
            failures.append(f"source asset missing: {label} -> {source}")
    for group in planned_groups:
        for path_key in ("target_cluster_asset", "target_faction_asset"):
            target = group[path_key]
            if not target.startswith(TARGET_PREFIX):
                failures.append(f"target asset outside mod override: {target}")
                continue
            target_file = plugin_file_for_asset(target)
            if not is_relative_to(target_file, PLUGIN_DIR):
                failures.append(f"target file outside plugin dir: {target_file}")
    return failures


def apply_group(group: dict[str, Any]) -> dict[str, Any]:
    result: dict[str, Any] = {
        "cluster_id": group["cluster_id"],
        "target_cluster_asset": group["target_cluster_asset"],
        "target_faction_asset": group["target_faction_asset"],
        "system_ids": group["system_ids"],
        "system_count": len(group["system_ids"]),
        "placeholder_assets": placeholder_assets_for(group),
        "attempted": False,
        "saved": False,
        "backup": {},
        "errors": [],
    }
    if not APPLY:
        result["reason"] = "dry run only"
        return result

    result["attempted"] = True
    result["backup"]["cluster_asset"] = backup_target(group["target_cluster_asset"])
    result["backup"]["faction_asset"] = backup_target(group["target_faction_asset"])

    faction_asset = duplicate_or_load(group["source_faction_asset"], group["target_faction_asset"])
    result["faction_asset"] = jsonable(faction_asset)
    if not faction_asset:
        result["errors"].append("faction asset duplicate/load returned None")
        return result
    faction_saved = bool(unreal.EditorAssetLibrary.save_loaded_asset(faction_asset, True))
    result["faction_saved"] = faction_saved

    cluster_asset = duplicate_or_load(group["source_cluster_asset"], group["target_cluster_asset"])
    result["cluster_asset"] = jsonable(cluster_asset)
    if not cluster_asset:
        result["errors"].append("cluster asset duplicate/load returned None")
        return result

    overlay_path = result["placeholder_assets"]["overlay_asset"]
    constellation_path = result["placeholder_assets"]["constellation_asset"]
    overlay_asset = load_optional_asset(overlay_path)
    constellation_asset = load_optional_asset(constellation_path)
    if overlay_path and not overlay_asset:
        result["errors"].append(f"overlay placeholder failed to load: {overlay_path}")
    if constellation_path and not constellation_asset:
        result["errors"].append(f"constellation placeholder failed to load: {constellation_path}")
    if result["errors"]:
        return result

    if hasattr(cluster_asset, "modify"):
        result["modify_cluster"] = safe("cluster.modify", cluster_asset.modify, True)
    result["before_properties"] = read_cluster_properties(cluster_asset)
    result["set_results"] = {
        "system_ids": try_set_cluster_value(
            cluster_asset,
            "set_cluster_system_ids_editoronly",
            "system_ids",
            [int(item) for item in group["system_ids"]],
        ),
        "faction": try_set_cluster_value(
            cluster_asset,
            "set_cluster_faction_asset_editoronly",
            "cluster_faction_asset",
            faction_asset,
        ),
        "overlay": try_set_cluster_value(
            cluster_asset,
            "set_cluster_overlay_editoronly",
            "cluster_overlay",
            overlay_asset,
        ),
        "constellation": try_set_cluster_value(
            cluster_asset,
            "set_cluster_constellation_editoronly",
            "cluster_constellation",
            constellation_asset,
        ),
    }
    result["after_properties"] = read_cluster_properties(cluster_asset)
    result["cluster_saved"] = bool(unreal.EditorAssetLibrary.save_loaded_asset(cluster_asset, True))
    result["saved"] = bool(faction_saved and result["cluster_saved"])
    return result


def write_report(report: dict[str, Any]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True, default=str), encoding="utf-8")

    lines = [
        "# UE4 TKU Clan Cluster Assets Patch",
        "",
        f"- Generated: `{report['generated_utc']}`",
        f"- Apply requested: `{report['apply_requested']}`",
        f"- Placeholder overlays: `{report['use_placeholder_overlays']}`",
        f"- Target mod: `{TARGET_MOD_NAME}`",
        f"- Source CSV: `{SOURCE_CSV}`",
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

    lines.extend(["", "## Planned Groups", ""])
    for group in report["planned_groups"]:
        lines.append(
            f"- `{group['target_cluster_asset']}` cluster `{group['cluster_id']}` systems `{len(group['system_ids'])}` overlay `{group['overlay']}` constellation `{group['constellation']}`"
        )

    lines.extend(["", "## Results", ""])
    for result in report.get("results", []):
        lines.append(f"### `{result['target_cluster_asset']}`")
        lines.append(f"- Attempted: `{result.get('attempted')}`")
        lines.append(f"- Saved: `{result.get('saved')}`")
        lines.append(f"- System IDs: `{result.get('system_ids')}`")
        lines.append(f"- Placeholder assets: `{result.get('placeholder_assets')}`")
        lines.append(f"- Errors: `{result.get('errors')}`")
        after = result.get("after_properties") or {}
        lines.append(f"- After system count: `{len(after.get('system_ids', [])) if isinstance(after.get('system_ids'), list) else after.get('system_ids')}`")
        lines.append(f"- After faction: `{after.get('cluster_faction_asset')}`")
        lines.append(f"- After overlay: `{after.get('cluster_overlay')}`")
        lines.append(f"- After constellation: `{after.get('cluster_constellation')}`")
        lines.append("")

    lines.extend(["## Omitted Clan Candidates", ""])
    for item in report.get("omitted_candidates", []):
        lines.append(f"- `{item['system_id']}` `{item['star_system_name']}` cluster `{item['cluster_id']}`: {item['reason']}")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    report: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "apply_requested": APPLY,
        "use_placeholder_overlays": USE_PLACEHOLDER_OVERLAYS,
        "target_mod_name": TARGET_MOD_NAME,
        "plugin_dir": str(PLUGIN_DIR),
        "source_assets": SOURCE_ASSETS,
        "planned_groups": [],
        "omitted_candidates": [],
        "safety_failures": [],
        "results": [],
        "errors": [],
    }
    try:
        planned_groups, omitted = load_cluster_groups()
        report["planned_groups"] = planned_groups
        report["omitted_candidates"] = omitted
        report["safety_failures"] = build_safety(planned_groups)
        if not report["safety_failures"]:
            for group in planned_groups:
                report["results"].append(apply_group(group))
    except Exception:
        report["errors"].append({"fatal": traceback.format_exc()})
        report["safety_failures"].append("fatal exception before completion; see errors")
    finally:
        write_report(report)
        unreal.log(f"TKU clan cluster assets patch wrote {OUT_JSON}")


main()
