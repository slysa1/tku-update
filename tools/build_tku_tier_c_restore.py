from __future__ import annotations

import json
import shutil
from pathlib import Path

from mw5_pak import build_pak, extract_exact_paths, gather_sidecar_paths, iter_entries

from tku_project_paths import GAME_ROOT as WORKSPACE_ROOT, REPORTS_DIR

SOURCE_MOD_NAME = "TheKnownUniverseCompatPluginOnly"
COMPAT_PATCH_NAME = "TheKnownUniverseCompatPatch"
RESTORE_MOD_NAME = "TheKnownUniverseCompatTierCRestore"

ORIGINAL_TKU_PAK = WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "TheKnownUniverse" / "Paks" / "TheKnownUniverse.pak"
CONTENT_RESTORE_PAK = WORKSPACE_ROOT / "MW5Mercs" / "Content" / "Paks" / "MW5Mercs-zzzzKnownUniverseTierCRestore.pak"

RESTORE_ROOT = WORKSPACE_ROOT / "MW5Mercs" / "Mods" / RESTORE_MOD_NAME
RESTORE_PAK = RESTORE_ROOT / "Paks" / f"{RESTORE_MOD_NAME}.pak"
RESTORE_MOD_JSON = RESTORE_ROOT / "mod.json"

REPORT_JSON = REPORTS_DIR / "tku_tier_c_restore.json"
REPORT_MD = REPORTS_DIR / "tku_tier_c_restore.md"

PROFILE_SOURCES = {
    "single": WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "modlist.profile-single-knownuniverse-plugin-only-compat-20260506.json",
    "named_local": WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "modlist.profile-named-local-plugin-only-compat-20260506.json",
    "full_stack": WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "modlist.profile-full-stack-plugin-only-compat-20260506.json",
}

PROFILE_OUTPUTS = {
    "single": WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "modlist.profile-single-knownuniverse-plugin-tierc-compat-20260506.json",
    "named_local": WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "modlist.profile-named-local-plugin-tierc-compat-20260506.json",
    "full_stack": WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "modlist.profile-full-stack-plugin-tierc-compat-20260506.json",
}

RESTORE_BASES = {
    "/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015",
    "/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges",
    "/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor",
    "/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL",
    "/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF",
    "/Game/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL",
}


def primary_manifest_paths(exact_paths: list[str]) -> list[str]:
    return [path for path in exact_paths if path.endswith(".uasset") or path.endswith(".umap")]


def build_restore_mod() -> dict[str, object]:
    reuse_existing = False
    if RESTORE_ROOT.exists():
        try:
            shutil.rmtree(RESTORE_ROOT)
        except PermissionError:
            reuse_existing = RESTORE_PAK.exists() and RESTORE_MOD_JSON.exists()
            if not reuse_existing:
                raise
    if not reuse_existing:
        (RESTORE_ROOT / "Paks").mkdir(parents=True, exist_ok=True)

    _, mount_point, entries = iter_entries(ORIGINAL_TKU_PAK)
    exact_paths = sorted(gather_sidecar_paths(entries, RESTORE_BASES))
    extracted = extract_exact_paths(ORIGINAL_TKU_PAK, set(exact_paths))
    missing = [path for path in exact_paths if path not in extracted]
    if missing:
        raise RuntimeError(f"missing restore files: {missing}")

    loose_files = [(path, extracted[path]) for path in exact_paths]
    pak_size = RESTORE_PAK.stat().st_size if reuse_existing else build_pak(loose_files, RESTORE_PAK, mount_point=mount_point)
    content_pak_size = build_pak(loose_files, CONTENT_RESTORE_PAK, mount_point=mount_point)

    mod_json = {
        "displayName": "The Known Universe Compat Tier C Restore",
        "version": "0.1.0",
        "buildNumber": 1,
        "description": (
            "Local TKU compatibility helper that restores the original border root assets and starmap faction "
            "materials on top of the broad vanilla rescue patch."
        ),
        "author": "codex",
        "authorURL": "",
        "defaultLoadOrder": 1001,
        "gameVersion": "1.13.378",
        "manifest": primary_manifest_paths(exact_paths),
        "steamPublishedFileId": 0,
        "steamLastSubmittedBuildNumber": 0,
        "steamModVisibility": "Private",
    }
    if not reuse_existing:
        RESTORE_MOD_JSON.write_text(json.dumps(mod_json, indent=3) + "\n", encoding="utf-8")

    return {
        "restore_root": str(RESTORE_ROOT),
        "restore_pak": str(RESTORE_PAK),
        "content_restore_pak": str(CONTENT_RESTORE_PAK),
        "pak_size": pak_size,
        "content_pak_size": content_pak_size,
        "reused_existing_restore_mod": reuse_existing,
        "exact_paths": exact_paths,
        "manifest_paths": mod_json["manifest"],
    }


def rewrite_profile(source_path: Path, output_path: Path):
    data = json.loads(source_path.read_text(encoding="utf-8"))
    mod_status = data.setdefault("modStatus", {})
    mod_status.setdefault(SOURCE_MOD_NAME, {})
    mod_status[SOURCE_MOD_NAME]["bEnabled"] = True
    mod_status.setdefault(COMPAT_PATCH_NAME, {})
    mod_status[COMPAT_PATCH_NAME]["bEnabled"] = True
    mod_status.setdefault(RESTORE_MOD_NAME, {})
    mod_status[RESTORE_MOD_NAME]["bEnabled"] = True
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
        "# TKU Tier C Restore",
        "",
        "- Strategy: keep the plugin-only TKU source variant, keep the broad vanilla rescue patch, and restore only the original TKU border root assets and faction materials at a higher load order and as a later content pak mirror.",
        f"- Restore mod root: `{RESTORE_ROOT}`",
        f"- Content restore pak: `{CONTENT_RESTORE_PAK}`",
        "",
        "## Restored Bases",
        "",
    ]
    for base in sorted(RESTORE_BASES):
        lines.append(f"- `{base}`")
    lines.extend(["", "## Generated Profiles", ""])
    for key, path in report["profiles"].items():
        lines.append(f"- `{key}`: `{path}`")
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    restore_report = build_restore_mod()
    profiles_report = build_profiles()

    report = {
        "restore_mod_name": RESTORE_MOD_NAME,
        "source_mod_name": SOURCE_MOD_NAME,
        "compat_patch_name": COMPAT_PATCH_NAME,
        "restore": restore_report,
        "profiles": profiles_report,
    }
    write_report(report)

    print(f"Wrote {RESTORE_MOD_JSON}")
    print(f"Wrote {RESTORE_PAK}")
    print(f"Wrote {REPORT_JSON}")
    print(f"Wrote {REPORT_MD}")


if __name__ == "__main__":
    main()
