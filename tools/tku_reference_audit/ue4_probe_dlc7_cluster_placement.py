from __future__ import annotations

import json
import os
import re
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import unreal


REPORT_STEM = "ue4_dlc7_cluster_placement_probe"
TARGET_MOD_NAME = os.environ.get("TKU_DLC7_CLUSTER_MOD_NAME", "TKUCompatEditorPatch").strip()

DLC7_ROOTS = (
    "/Game/DLC7/CampaignData/Clusters",
    "/Game/DLC7/PlaceClusterActions",
    "/Game/DLC7/CampaignData/CampaignArcActions",
    "/Game/DLC7/CampaignData",
)

FOCUS_TERMS = (
    "Cluster",
    "PlaceCluster",
    "Wave",
    "Periphery",
    "CGB",
    "CJF",
    "CSJ",
    "CWF",
    "Hidden",
    "Rasalhague",
)

PROPERTY_CANDIDATES = (
    "campaign_arc_script",
    "campaign_event_list",
    "run_campaign_arc_script_on_save",
    "sub_campaigns",
    "campaign_arc_action_id",
    "cluster_data_asset",
    "cluster_data_asset_id",
    "ClusterDataAsset",
    "ClusterDataAssetId",
    "cluster_faction_asset",
    "cluster_overlay",
    "cluster_constellation",
    "system_ids",
    "is_legacy_cluster",
)


def resolve_project_root() -> Path:
    raw = os.environ.get("TKU_PROJECT_ROOT")
    if raw:
        return Path(raw).resolve()
    script_path = globals().get("__file__")
    if script_path:
        return Path(script_path).resolve().parents[2]
    return Path(r"D:\Downloads\OneDrive\Documents\code\tku-update")


PROJECT_ROOT = resolve_project_root()
REPORT_DIR = PROJECT_ROOT / "reports" / "tku_editor_first"
OUT_JSON = REPORT_DIR / f"{REPORT_STEM}.json"
OUT_MD = REPORT_DIR / f"{REPORT_STEM}.md"


def text(value: Any) -> str:
    try:
        return str(value)
    except Exception:
        return repr(value)


def path_name(value: Any) -> str | None:
    try:
        return text(value.get_path_name())
    except Exception:
        return None


def class_name(value: Any) -> str:
    try:
        return text(value.get_class().get_name())
    except Exception:
        return type(value).__name__


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
            "tail_sample": [jsonable(item, depth + 1) for item in values[-12:]],
        }
    try:
        if hasattr(value, "__iter__") and not isinstance(value, (str, bytes)):
            values = list(value)
            return {
                "kind": type(value).__name__,
                "count": len(values),
                "sample": [jsonable(item, depth + 1) for item in values[:40]],
                "tail_sample": [jsonable(item, depth + 1) for item in values[-12:]],
            }
    except Exception:
        pass

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


def dependency_options() -> Any:
    return unreal.AssetRegistryDependencyOptions(True, True, True, True, True)


def dependencies(asset_path: str) -> dict[str, Any]:
    out: dict[str, Any] = {}
    try:
        registry = unreal.AssetRegistryHelpers.get_asset_registry()
        options = dependency_options()
        for method_name in ("get_dependencies", "get_referencers"):
            try:
                values = list(getattr(registry, method_name)(asset_path, options) or [])
                out[method_name] = sorted(text(item) for item in values)
            except Exception as exc:
                out[method_name] = {"error": f"{type(exc).__name__}: {exc}"}
    except Exception as exc:
        out["error"] = f"{type(exc).__name__}: {exc}"
    return out


def read_properties(obj: Any) -> dict[str, Any]:
    props: dict[str, Any] = {}
    for prop in PROPERTY_CANDIDATES:
        try:
            value = obj.get_editor_property(prop)
            props[prop] = jsonable(value)
        except Exception:
            continue
    return props


def selected_tags(asset_path: str) -> dict[str, str]:
    tags: dict[str, str] = {}
    try:
        data = unreal.EditorAssetLibrary.find_asset_data(asset_path)
        for key in ("GeneratedClass", "ParentClass", "NativeParentClass", "BlueprintType", "ClassFlags"):
            try:
                value = data.get_tag_value(key)
            except Exception:
                value = None
            if value:
                tags[key] = text(value)
    except Exception:
        pass
    return tags


def inspect_asset(asset_path: str) -> dict[str, Any]:
    out: dict[str, Any] = {"asset_path": asset_path}
    try:
        data = unreal.EditorAssetLibrary.find_asset_data(asset_path)
        out["asset_data"] = {
            "is_valid": bool(data.is_valid()),
            "asset_class": text(data.asset_class),
            "asset_name": text(data.asset_name),
            "package_name": text(data.package_name),
            "package_path": text(data.package_path),
            "object_path": text(data.object_path),
        }
    except Exception as exc:
        out["asset_data_error"] = f"{type(exc).__name__}: {exc}"
    out["tags"] = selected_tags(asset_path)
    out["dependencies"] = dependencies(asset_path)
    try:
        out["exists"] = bool(unreal.EditorAssetLibrary.does_asset_exist(asset_path))
    except Exception as exc:
        out["exists"] = False
        out["exists_error"] = f"{type(exc).__name__}: {exc}"
    if not out.get("exists"):
        return out

    try:
        asset = unreal.EditorAssetLibrary.load_asset(asset_path)
        out["asset"] = {
            "object_path": path_name(asset),
            "class": class_name(asset),
            "properties": read_properties(asset),
        }
    except Exception as exc:
        out["load_error"] = f"{type(exc).__name__}: {exc}"
        return out

    asset_class = (out.get("asset_data") or {}).get("asset_class")
    if asset_class == "Blueprint":
        try:
            bp_class = unreal.EditorAssetLibrary.load_blueprint_class(asset_path)
            if bp_class:
                cdo = unreal.get_default_object(bp_class)
                out["blueprint"] = {
                    "class_path": path_name(bp_class),
                    "cdo_path": path_name(cdo),
                    "cdo_class": class_name(cdo),
                    "cdo_properties": read_properties(cdo),
                }
        except Exception as exc:
            out["blueprint_error"] = f"{type(exc).__name__}: {exc}"
    return out


def discover_assets() -> dict[str, Any]:
    out: dict[str, Any] = {"roots": {}, "paths": []}
    paths: set[str] = set()
    for root in DLC7_ROOTS:
        try:
            raw_paths = sorted(set(path.split(".", 1)[0] for path in unreal.EditorAssetLibrary.list_assets(root, True, False)))
            matches = [
                path
                for path in raw_paths
                if any(term.lower() in path.lower() for term in FOCUS_TERMS)
            ]
            out["roots"][root] = {"ok": True, "asset_path_count": len(raw_paths), "match_count": len(matches)}
            paths.update(matches)
        except Exception as exc:
            out["roots"][root] = {"ok": False, "error": f"{type(exc).__name__}: {exc}"}
    out["paths"] = sorted(paths)
    return out


def extract_asset_paths_from_text(value: Any) -> list[str]:
    raw = text(value)
    return sorted(set(re.findall(r"/Game/[A-Za-z0-9_./-]+", raw)))


def summarize(report: dict[str, Any]) -> list[str]:
    assets = report.get("assets", [])
    cluster_assets = [
        item for item in assets if (item.get("asset_data") or {}).get("asset_class") == "MWClusterDataAsset"
    ]
    place_actions = [
        item
        for item in assets
        if "PlaceCluster" in item.get("asset_path", "") or "PlaceHiddenSystemsCluster" in item.get("asset_path", "")
    ]
    campaign_arcs = [
        item for item in assets if (item.get("asset_data") or {}).get("asset_class") == "MWCampaignArcAsset"
    ]
    referenced_cluster_paths: set[str] = set()
    for item in place_actions + campaign_arcs:
        referenced_cluster_paths.update(extract_asset_paths_from_text(item))

    return [
        f"DLC7 focused asset paths discovered: {len(report.get('discovery', {}).get('paths', []))}.",
        f"DLC7 MWClusterDataAsset assets inspected: {len(cluster_assets)}.",
        f"DLC7 place-cluster action assets inspected: {len(place_actions)}.",
        f"DLC7 campaign arc assets inspected: {len(campaign_arcs)}.",
        f"Cluster paths mentioned by inspected actions/arcs: {len(referenced_cluster_paths)}.",
    ]


def write_markdown(report: dict[str, Any]) -> None:
    lines = [
        "# UE4 DLC7 Cluster Placement Probe",
        "",
        f"- Generated: `{report['generated_utc']}`",
        f"- Target mod: `{TARGET_MOD_NAME}`",
        "- Safety: read-only commandlet; no assets saved.",
        "",
        "## Findings",
        "",
    ]
    for finding in report.get("findings", []):
        lines.append(f"- {finding}")

    lines.extend(["", "## Roots", ""])
    for root, info in (report.get("discovery", {}).get("roots") or {}).items():
        lines.append(f"- `{root}`: `{info}`")

    lines.extend(["", "## Assets", ""])
    for item in report.get("assets", []):
        lines.append(f"### `{item.get('asset_path')}`")
        asset_data = item.get("asset_data") or {}
        lines.append(f"- class: `{asset_data.get('asset_class')}`")
        asset_props = ((item.get("asset") or {}).get("properties") or {})
        if asset_props:
            lines.append(f"- asset properties: `{asset_props}`")
        bp = item.get("blueprint") or {}
        cdo_props = bp.get("cdo_properties") or {}
        if bp:
            lines.append(f"- cdo: `{bp.get('cdo_path')}` class `{bp.get('cdo_class')}`")
        if cdo_props:
            lines.append(f"- cdo properties: `{cdo_props}`")
        deps = (item.get("dependencies") or {}).get("get_dependencies", [])
        refs = (item.get("dependencies") or {}).get("get_referencers", [])
        lines.append(f"- dependencies: `{len(deps) if isinstance(deps, list) else deps}`")
        if isinstance(deps, list):
            for dep in deps[:30]:
                lines.append(f"  - `{dep}`")
        lines.append(f"- referencers: `{len(refs) if isinstance(refs, list) else refs}`")
        if isinstance(refs, list):
            for ref in refs[:30]:
                lines.append(f"  - `{ref}`")
        lines.append("")

    if report.get("errors"):
        lines.extend(["## Errors", ""])
        for error in report["errors"]:
            lines.append(f"- `{error}`")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "target_mod_name": TARGET_MOD_NAME,
        "discovery": {},
        "assets": [],
        "errors": [],
    }
    try:
        report["discovery"] = discover_assets()
        for asset_path in report["discovery"].get("paths", []):
            report["assets"].append(inspect_asset(asset_path))
    except Exception:
        report["errors"].append(traceback.format_exc())
    report["findings"] = summarize(report)
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True, default=str), encoding="utf-8")
    write_markdown(report)
    unreal.log(f"TKU DLC7 cluster placement probe wrote {OUT_JSON}")


main()
