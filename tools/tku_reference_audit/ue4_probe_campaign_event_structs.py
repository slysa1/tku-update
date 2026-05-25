from __future__ import annotations

import json
import os
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import unreal


REPORT_STEM = "ue4_campaign_event_struct_probe"
TARGET_MOD_NAME = os.environ.get("TKU_EVENT_STRUCT_MOD_NAME", "TKUCompatEditorPatch").strip()
TARGET_PREFIX = f"/ModOverride/{TARGET_MOD_NAME}"

ASSET_PATHS = (
    f"{TARGET_PREFIX}/DLC1/CareerMode/CareerModeCoreCampaign",
    f"{TARGET_PREFIX}/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters",
    f"{TARGET_PREFIX}/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones",
    "/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors",
    "/Game/DLC7/CampaignData/DLC7_ShowUnchartedSystems",
    "/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceHiddenSystemsCluster",
    "/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Periphery_PlaceCluster_ArcAction",
)

SCAN_ROOTS = (
    f"{TARGET_PREFIX}/DLC1/CareerMode",
    f"{TARGET_PREFIX}/Campaign/Clusters",
    f"{TARGET_PREFIX}/InnerSphereData",
    "/Game/DLC7/CampaignData",
    "/Game/DLC7/PlaceClusterActions",
)

EVENT_FIELD_CANDIDATES = (
    "event_name",
    "EventName",
    "trigger_conditions",
    "TriggerConditions",
    "campaign_actions",
    "CampaignActions",
)

TRIGGER_FIELD_CANDIDATES = (
    "trigger_type",
    "TriggerType",
    "date",
    "Date",
    "dlc",
    "DLC",
    "objectives",
    "Objectives",
    "reputation_level",
    "ReputationLevel",
)

DATE_FIELD_CANDIDATES = (
    "b_check",
    "bCheck",
    "value",
    "Value",
    "condition",
    "Condition",
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


def class_name(value: Any) -> str | None:
    try:
        return text(value.get_class().get_name())
    except Exception:
        return None


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
            "sample": [jsonable(item, depth + 1) for item in values[:30]],
        }
    try:
        if hasattr(value, "__iter__") and not isinstance(value, (str, bytes)):
            values = list(value)
            return {
                "kind": type(value).__name__,
                "count": len(values),
                "sample": [jsonable(item, depth + 1) for item in values[:30]],
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


def try_get_property(obj: Any, name: str) -> dict[str, Any]:
    try:
        value = obj.get_editor_property(name)
        return {
            "ok": True,
            "name": name,
            "value": jsonable(value),
            "path": path_name(value),
            "repr": text(value)[:3000],
        }
    except Exception as exc:
        return {"ok": False, "name": name, "error": f"{type(exc).__name__}: {exc}"}


def probe_fields(obj: Any, candidates: tuple[str, ...]) -> dict[str, Any]:
    return {name: try_get_property(obj, name) for name in candidates}


def package_path_from_object_path(raw_path: str) -> str:
    path = raw_path.strip(" \t\r\n'\"),]}>")
    if "." in path:
        path = path.split(".", 1)[0]
    if path.endswith("_C"):
        path = path[:-2]
    return path


def prime_asset_registry() -> list[dict[str, Any]]:
    primed: list[dict[str, Any]] = []
    for root in SCAN_ROOTS:
        item: dict[str, Any] = {"root": root, "exists": False, "asset_count": 0, "sample": []}
        try:
            item["exists"] = bool(unreal.EditorAssetLibrary.does_directory_exist(root))
            if item["exists"]:
                assets = sorted(
                    set(
                        package_path_from_object_path(path)
                        for path in unreal.EditorAssetLibrary.list_assets(root, True, False)
                    )
                )
                item["asset_count"] = len(assets)
                item["sample"] = assets[:40]
        except Exception as exc:
            item["error"] = f"{type(exc).__name__}: {exc}"
        primed.append(item)
    return primed


def list_iterable(value: Any, limit: int = 40) -> list[Any]:
    try:
        return list(value)[:limit]
    except Exception:
        return []


def describe_event(event: Any) -> dict[str, Any]:
    item: dict[str, Any] = {
        "repr": text(event)[:5000],
        "python_type": type(event).__name__,
        "dir_focus": sorted(
            name
            for name in dir(event)
            if not name.startswith("_")
            and any(term in name.lower() for term in ("action", "condition", "date", "event", "trigger"))
        )[:120],
        "fields": probe_fields(event, EVENT_FIELD_CANDIDATES),
    }
    trigger = None
    for field_name in ("trigger_conditions", "TriggerConditions"):
        result = item["fields"].get(field_name) or {}
        if result.get("ok"):
            try:
                trigger = event.get_editor_property(field_name)
            except Exception:
                trigger = None
            break
    if trigger is not None:
        item["trigger"] = {
            "repr": text(trigger)[:5000],
            "python_type": type(trigger).__name__,
            "dir_focus": sorted(
                name
                for name in dir(trigger)
                if not name.startswith("_")
                and any(term in name.lower() for term in ("date", "dlc", "objective", "reputation", "trigger"))
            )[:120],
            "fields": probe_fields(trigger, TRIGGER_FIELD_CANDIDATES),
        }
        for date_field_name in ("date", "Date"):
            date_result = item["trigger"]["fields"].get(date_field_name) or {}
            if not date_result.get("ok"):
                continue
            try:
                date_value = trigger.get_editor_property(date_field_name)
                item["trigger"]["date_field"] = {
                    "name": date_field_name,
                    "repr": text(date_value)[:3000],
                    "python_type": type(date_value).__name__,
                    "fields": probe_fields(date_value, DATE_FIELD_CANDIDATES),
                }
            except Exception as exc:
                item["trigger"]["date_field_error"] = f"{type(exc).__name__}: {exc}"
            break
    actions = None
    for field_name in ("campaign_actions", "CampaignActions"):
        result = item["fields"].get(field_name) or {}
        if result.get("ok"):
            try:
                actions = event.get_editor_property(field_name)
            except Exception:
                actions = None
            break
    if actions is not None:
        action_items = list_iterable(actions)
        item["campaign_actions"] = {
            "count": len(action_items),
            "items": [jsonable(action) for action in action_items[:30]],
            "paths": [path for path in (path_name(action) for action in action_items) if path],
        }
    return item


def describe_campaign_arc(asset_path: str) -> dict[str, Any]:
    item: dict[str, Any] = {
        "asset_path": asset_path,
        "exists": False,
        "class_name": None,
        "events": [],
        "errors": [],
    }
    try:
        item["exists"] = bool(unreal.EditorAssetLibrary.does_asset_exist(asset_path))
    except Exception as exc:
        item["errors"].append(f"exists check failed: {type(exc).__name__}: {exc}")
        return item
    if not item["exists"]:
        return item
    try:
        asset = unreal.EditorAssetLibrary.load_asset(asset_path)
        item["class_name"] = class_name(asset)
        item["asset"] = jsonable(asset)
        event_list = asset.get_editor_property("campaign_event_list")
        item["campaign_event_list"] = {
            "repr": text(event_list)[:6000],
            "python_type": type(event_list).__name__,
            "fields": probe_fields(event_list, ("campaign_events", "CampaignEvents")),
        }
        events = []
        for field_name in ("campaign_events", "CampaignEvents"):
            field = item["campaign_event_list"]["fields"].get(field_name) or {}
            if not field.get("ok"):
                continue
            events = list_iterable(event_list.get_editor_property(field_name), limit=80)
            item["campaign_event_list"]["event_field_name"] = field_name
            break
        item["event_count"] = len(events)
        item["events"] = [describe_event(event) for event in events]
    except Exception:
        item["errors"].append(traceback.format_exc())
    return item


def describe_blueprint(asset_path: str) -> dict[str, Any]:
    item: dict[str, Any] = {
        "asset_path": asset_path,
        "exists": False,
        "class_name": None,
        "cdo_properties": {},
        "errors": [],
    }
    try:
        item["exists"] = bool(unreal.EditorAssetLibrary.does_asset_exist(asset_path))
    except Exception as exc:
        item["errors"].append(f"exists check failed: {type(exc).__name__}: {exc}")
        return item
    if not item["exists"]:
        return item
    try:
        cls = unreal.EditorAssetLibrary.load_blueprint_class(asset_path)
        cdo = unreal.get_default_object(cls)
        item["class_name"] = class_name(cdo)
        item["blueprint_class"] = jsonable(cls)
        item["cdo"] = jsonable(cdo)
        item["cdo_properties"] = {
            name: try_get_property(cdo, name)
            for name in ("ClusterDataAsset", "ClusterDataAssetId", "campaign_arc_action_id")
        }
    except Exception:
        item["errors"].append(traceback.format_exc())
    return item


def write_markdown(report: dict[str, Any]) -> None:
    lines = [
        "# UE4 Campaign Event Struct Probe",
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
    lines.extend(["", "## Campaign Arcs", ""])
    for asset in report.get("campaign_arcs", []):
        lines.append(f"### `{asset['asset_path']}`")
        lines.append(f"- Exists: `{asset.get('exists')}`")
        lines.append(f"- Class: `{asset.get('class_name')}`")
        lines.append(f"- Event count: `{asset.get('event_count')}`")
        field_name = ((asset.get("campaign_event_list") or {}).get("event_field_name"))
        lines.append(f"- Event array field: `{field_name}`")
        for event in asset.get("events", [])[:12]:
            event_name = None
            for field in ("event_name", "EventName"):
                value = ((event.get("fields") or {}).get(field) or {})
                if value.get("ok"):
                    event_name = value.get("repr")
                    break
            action_paths = ((event.get("campaign_actions") or {}).get("paths") or [])
            lines.append(f"- Event `{event_name}` actions `{len(action_paths)}` paths `{action_paths[:10]}`")
            trigger = event.get("trigger") or {}
            date_field = trigger.get("date_field") or {}
            if date_field:
                lines.append(f"  - Date field `{date_field.get('name')}` `{date_field.get('repr')}`")
        if asset.get("errors"):
            lines.append(f"- Errors: `{asset['errors']}`")
        lines.append("")
    lines.extend(["## Blueprints", ""])
    for bp in report.get("blueprints", []):
        lines.append(f"### `{bp['asset_path']}`")
        lines.append(f"- Exists: `{bp.get('exists')}`")
        lines.append(f"- CDO class: `{bp.get('class_name')}`")
        props = bp.get("cdo_properties") or {}
        for name, value in props.items():
            lines.append(f"- {name}: `{value}`")
        if bp.get("errors"):
            lines.append(f"- Errors: `{bp['errors']}`")
        lines.append("")
    if report.get("errors"):
        lines.extend(["## Errors", ""])
        for error in report["errors"]:
            lines.append(f"- `{error}`")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def build_findings(report: dict[str, Any]) -> list[str]:
    findings: list[str] = []
    for asset in report.get("campaign_arcs", []):
        findings.append(
            f"{asset['asset_path']} events={asset.get('event_count')} event_field={((asset.get('campaign_event_list') or {}).get('event_field_name'))}."
        )
        for event in asset.get("events", [])[:8]:
            event_name = None
            for field in ("event_name", "EventName"):
                value = ((event.get("fields") or {}).get(field) or {})
                if value.get("ok"):
                    event_name = value.get("repr")
                    break
            trigger = event.get("trigger") or {}
            date_field = trigger.get("date_field") or {}
            actions = event.get("campaign_actions") or {}
            if date_field:
                findings.append(
                    f"Event {event_name} has date field {date_field.get('name')}={date_field.get('repr')} actions={actions.get('count')}."
                )
            elif actions:
                findings.append(f"Event {event_name} actions={actions.get('count')}.")
    return findings[:40]


def main() -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "target_mod_name": TARGET_MOD_NAME,
        "asset_paths": list(ASSET_PATHS),
        "scan_roots": list(SCAN_ROOTS),
        "primed_assets": [],
        "campaign_arcs": [],
        "blueprints": [],
        "findings": [],
        "errors": [],
    }
    try:
        report["primed_assets"] = prime_asset_registry()
        for path in ASSET_PATHS:
            if path.endswith("_ArcAction") or "CampaignArcActions" in path or "PlaceClusterActions" in path:
                report["blueprints"].append(describe_blueprint(path))
            else:
                report["campaign_arcs"].append(describe_campaign_arc(path))
        report["findings"] = build_findings(report)
    except Exception:
        report["errors"].append(traceback.format_exc())
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True, default=str), encoding="utf-8")
    write_markdown(report)
    unreal.log(f"TKU campaign event struct probe wrote {OUT_JSON}")


main()
