from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import unreal


from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
EDITOR_PROJECT = Path(r"E:\Games\MechWarrior5Editor\MW5Mercs")
OUT_DIR = REPORTS_DIR / "tku_editor_first"
OUT_JSON = OUT_DIR / "ue4_mod_entry_creation_probe_20260510.json"
OUT_MD = OUT_DIR / "ue4_mod_entry_creation_probe_20260510.md"

PROBE_MOD_NAME = "__TKUProbeEntryOnly_NoDisk__"


def list_tree(path: Path) -> list[str]:
    if not path.exists():
        return []
    return sorted(str(item.relative_to(path)) for item in path.rglob("*"))


def describe(value):
    out = {
        "repr": repr(value),
        "python_type": type(value).__name__,
    }
    for attr in ("get_name", "get_path_name", "get_full_name"):
        fn = getattr(value, attr, None)
        if callable(fn):
            try:
                out[attr] = fn()
            except Exception as exc:
                out[f"{attr}_error"] = f"{type(exc).__name__}: {exc}"
    if hasattr(value, "get_editor_property"):
        props = {}
        for prop in (
            "mod_name",
            "plugin_path",
            "version_name",
            "friendly_name",
            "description",
            "category",
            "created_by",
            "load_order",
            "bEnabled",
            "enabled",
            "name",
            "display_name",
        ):
            try:
                props[prop] = value.get_editor_property(prop)
            except Exception as exc:
                props[f"{prop}__error"] = f"{type(exc).__name__}: {exc}"
        out["editor_properties"] = props
    return out


def main() -> None:
    mods_dir = EDITOR_PROJECT / "Mods"
    plugins_dir = EDITOR_PROJECT / "Plugins"
    before = {
        "mods": list_tree(mods_dir),
        "plugins": list_tree(plugins_dir),
    }
    result = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "non_mutating_intent": True,
        "called_functions": ["MWModUtils.create_mod_entry"],
        "explicitly_not_called": [
            "MWModUtils.set_active_mod",
            "MWModUtils.save_mod_info_to_file",
            "MWModEditorWidget.package_mod",
            "EditorAssetLibrary.save_asset",
            "EditorAssetLibrary.duplicate_asset",
        ],
        "probe_mod_name": PROBE_MOD_NAME,
        "before_counts": {key: len(value) for key, value in before.items()},
    }
    try:
        info = unreal.MWModPluginInfo(
            mod_name=PROBE_MOD_NAME,
            plugin_path="",
            version_name="0.0-probe",
            friendly_name="TKU Probe Entry Only",
            description="Non-mutating create_mod_entry probe",
            category="Probe",
            created_by="Codex",
            engine_version="4.27",
        )
        result["plugin_info"] = describe(info)
        entry = unreal.MWModUtils.create_mod_entry(info)
        result["create_mod_entry"] = {"ok": True, "value": describe(entry)}
    except Exception as exc:
        result["create_mod_entry"] = {"ok": False, "error": f"{type(exc).__name__}: {exc}"}

    after = {
        "mods": list_tree(mods_dir),
        "plugins": list_tree(plugins_dir),
    }
    result["after_counts"] = {key: len(value) for key, value in after.items()}
    result["filesystem_delta"] = {
        key: {
            "added": sorted(set(after[key]) - set(before[key])),
            "removed": sorted(set(before[key]) - set(after[key])),
        }
        for key in before
    }
    result["decision"] = {
        "created_editor_mod_target": False,
        "create_mod_entry_is_sufficient_for_mod_scaffold": False,
        "manual_create_mod_required": True,
        "build_authorized": False,
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(result, indent=2, sort_keys=True, default=str), encoding="utf-8")
    lines = [
        "# UE4 Mod Entry Creation Probe - 2026-05-10",
        "",
        f"- Generated: `{result['generated_utc']}`",
        "- Method: MW5 editor commandlet Python, in-memory mod-entry call only.",
        "- Safety: did not call set_active_mod, save_mod_info_to_file, package_mod, save_asset, or duplicate_asset.",
        "",
        "## Result",
        "",
        f"- create_mod_entry ok: `{result['create_mod_entry'].get('ok')}`",
        f"- filesystem delta: `{result['filesystem_delta']}`",
        f"- created editor mod target: `{result['decision']['created_editor_mod_target']}`",
        f"- manual Create Mod required: `{result['decision']['manual_create_mod_required']}`",
        f"- build authorized: `{result['decision']['build_authorized']}`",
        "",
    ]
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
