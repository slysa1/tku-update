from __future__ import annotations

import json
import shutil
from pathlib import Path

from mw5_pak import build_pak, extract_exact_paths, iter_entries

from tku_project_paths import GAME_ROOT as WORKSPACE_ROOT, REPORTS_DIR

ORIGINAL_MOD_NAME = "TheKnownUniverse"
PLUGIN_ONLY_MOD_NAME = "TheKnownUniverseCompatPluginOnly"
LEGACY_SOURCE_MOD_NAME = "TheKnownUniverseCompatSource"
COMPAT_PATCH_NAME = "TheKnownUniverseCompatPatch"

ORIGINAL_MOD_ROOT = WORKSPACE_ROOT / "MW5Mercs" / "Mods" / ORIGINAL_MOD_NAME
ORIGINAL_MOD_PAK = ORIGINAL_MOD_ROOT / "Paks" / "TheKnownUniverse.pak"
ORIGINAL_MOD_JSON = ORIGINAL_MOD_ROOT / "mod.json"
ORIGINAL_MOD_RESOURCES = ORIGINAL_MOD_ROOT / "Resources"

PLUGIN_ONLY_ROOT = WORKSPACE_ROOT / "MW5Mercs" / "Mods" / PLUGIN_ONLY_MOD_NAME
PLUGIN_ONLY_PAK = PLUGIN_ONLY_ROOT / "Paks" / f"{PLUGIN_ONLY_MOD_NAME}.pak"
PLUGIN_ONLY_MOD_JSON = PLUGIN_ONLY_ROOT / "mod.json"
PLUGIN_ONLY_RESOURCES = PLUGIN_ONLY_ROOT / "Resources"

CONTENT_PAKS_ROOT = WORKSPACE_ROOT / "MW5Mercs" / "Content" / "Paks"
OVERRIDE_PAK = CONTENT_PAKS_ROOT / "MW5Mercs-zKnownUniverseStarmap.pak"
OVERRIDE_BACKUP_PAK = CONTENT_PAKS_ROOT / "MW5Mercs-zKnownUniverseStarmap.original-20260506.pak"

REPORT_JSON = REPORTS_DIR / "tku_plugin_only_variant.json"
REPORT_MD = REPORTS_DIR / "tku_plugin_only_variant.md"

PROFILE_SOURCES = {
    "single": WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "modlist.profile-single-knownuniverse-compat-20260506.json",
    "named_local": WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "modlist.profile-named-local-with-compat-20260506.json",
    "full_stack": WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "modlist.profile-full-stack-with-tku-compat-20260506.json",
}

PROFILE_OUTPUTS = {
    "single": WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "modlist.profile-single-knownuniverse-plugin-only-compat-20260506.json",
    "named_local": WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "modlist.profile-named-local-plugin-only-compat-20260506.json",
    "full_stack": WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "modlist.profile-full-stack-plugin-only-compat-20260506.json",
}


def build_plugin_only_mod() -> dict[str, object]:
    if PLUGIN_ONLY_ROOT.exists():
        shutil.rmtree(PLUGIN_ONLY_ROOT)
    (PLUGIN_ONLY_ROOT / "Paks").mkdir(parents=True, exist_ok=True)

    _, mount_point, entries = iter_entries(ORIGINAL_MOD_PAK)
    keep_paths = [
        entry.game_path
        for entry in entries
        if not entry.game_path.startswith("/Game/")
    ]
    extracted = extract_exact_paths(ORIGINAL_MOD_PAK, set(keep_paths))
    missing = [path for path in keep_paths if path not in extracted]
    if missing:
        raise RuntimeError(f"missing extracted files from {ORIGINAL_MOD_PAK}: {missing}")

    loose_files = [(path, extracted[path]) for path in sorted(keep_paths)]
    size = build_pak(loose_files, PLUGIN_ONLY_PAK, mount_point=mount_point)

    if ORIGINAL_MOD_RESOURCES.exists():
        shutil.copytree(ORIGINAL_MOD_RESOURCES, PLUGIN_ONLY_RESOURCES, dirs_exist_ok=True)

    original_mod = json.loads(ORIGINAL_MOD_JSON.read_text(encoding="utf-8"))
    original_mod["displayName"] = "The Known Universe Compat Plugin Only"
    original_mod["description"] = (
        "Local plugin-only compatibility variant of TheKnownUniverse. "
        "All root /Game assets are removed from the TKU mod pak so only plugin content remains."
    )
    original_mod["author"] = "TePa / codex local repack"
    original_mod["buildNumber"] = 40
    original_mod["manifest"] = []
    PLUGIN_ONLY_MOD_JSON.write_text(json.dumps(original_mod, indent=3) + "\n", encoding="utf-8")

    return {
        "mod_root": str(PLUGIN_ONLY_ROOT),
        "mod_json": str(PLUGIN_ONLY_MOD_JSON),
        "pak": str(PLUGIN_ONLY_PAK),
        "pak_size": size,
        "plugin_entry_count": sum(1 for entry in entries if entry.game_path.startswith("/Plugins/")),
        "game_entry_count_removed": sum(1 for entry in entries if entry.game_path.startswith("/Game/")),
        "other_entry_count": sum(1 for entry in entries if not (entry.game_path.startswith("/Game/") or entry.game_path.startswith("/Plugins/"))),
    }


def inspect_override() -> dict[str, object]:
    if not OVERRIDE_BACKUP_PAK.exists():
        raise RuntimeError(f"expected override backup missing: {OVERRIDE_BACKUP_PAK}")
    _, _, entries = iter_entries(OVERRIDE_PAK)
    return {
        "live_override_pak": str(OVERRIDE_PAK),
        "backup_override_pak": str(OVERRIDE_BACKUP_PAK),
        "entry_count": len(entries),
        "customcontent_entry_count": sum(1 for entry in entries if entry.game_path.startswith("/Game/CustomContent/")),
        "conflict_entry_count": sum(
            1
            for entry in entries
            if entry.base_game_path in {"/Game/InnerSphereData/MW5_InnerSphereData", "/Game/Levels/FrontEnd/StarMap"}
        ),
    }


def rewrite_profile(source_path: Path, output_path: Path):
    data = json.loads(source_path.read_text(encoding="utf-8"))
    mod_status = data.setdefault("modStatus", {})
    for mod_name in (ORIGINAL_MOD_NAME, LEGACY_SOURCE_MOD_NAME):
        mod_status.setdefault(mod_name, {})
        mod_status[mod_name]["bEnabled"] = False
    mod_status.setdefault(PLUGIN_ONLY_MOD_NAME, {})
    mod_status[PLUGIN_ONLY_MOD_NAME]["bEnabled"] = True
    mod_status.setdefault(COMPAT_PATCH_NAME, {})
    mod_status[COMPAT_PATCH_NAME]["bEnabled"] = True
    output_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def build_profiles() -> dict[str, str]:
    outputs: dict[str, str] = {}
    for key, source in PROFILE_SOURCES.items():
        output = PROFILE_OUTPUTS[key]
        rewrite_profile(source, output)
        outputs[key] = str(output)
    return outputs


def write_report(report: dict[str, object]):
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")

    lines = [
        "# TKU Plugin-Only Variant",
        "",
        "- Strategy: leave the original TKU download untouched, build a new plugin-only mod from the original pak, and pair it with the broad vanilla rescue patch plus the customcontent-only override pak.",
        f"- Plugin-only mod: `{PLUGIN_ONLY_ROOT}`",
        f"- Live override pak: `{OVERRIDE_PAK}`",
        f"- Backup override pak: `{OVERRIDE_BACKUP_PAK}`",
        "",
        "## Generated Profiles",
        "",
    ]
    for key, path in report["profiles"].items():
        lines.append(f"- `{key}`: `{path}`")
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    plugin_only_report = build_plugin_only_mod()
    override_report = inspect_override()
    profiles_report = build_profiles()

    report = {
        "plugin_only_mod_name": PLUGIN_ONLY_MOD_NAME,
        "compat_patch_name": COMPAT_PATCH_NAME,
        "plugin_only_mod": plugin_only_report,
        "override": override_report,
        "profiles": profiles_report,
    }
    write_report(report)

    print(f"Wrote {PLUGIN_ONLY_MOD_JSON}")
    print(f"Wrote {PLUGIN_ONLY_PAK}")
    print(f"Wrote {REPORT_JSON}")
    print(f"Wrote {REPORT_MD}")


if __name__ == "__main__":
    main()
