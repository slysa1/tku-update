from __future__ import annotations

import json
import shutil
from pathlib import Path

from mw5_pak import build_pak, extract_exact_paths, iter_entries

from tku_project_paths import GAME_ROOT as WORKSPACE_ROOT, REPORTS_DIR

ORIGINAL_MOD_NAME = "TheKnownUniverse"
SOURCE_COMPAT_MOD_NAME = "TheKnownUniverseCompatSource"
COMPAT_PATCH_NAME = "TheKnownUniverseCompatPatch"

ORIGINAL_MOD_ROOT = WORKSPACE_ROOT / "MW5Mercs" / "Mods" / ORIGINAL_MOD_NAME
ORIGINAL_MOD_PAK = ORIGINAL_MOD_ROOT / "Paks" / "TheKnownUniverse.pak"
ORIGINAL_MOD_JSON = ORIGINAL_MOD_ROOT / "mod.json"
ORIGINAL_MOD_RESOURCES = ORIGINAL_MOD_ROOT / "Resources"

SOURCE_COMPAT_ROOT = WORKSPACE_ROOT / "MW5Mercs" / "Mods" / SOURCE_COMPAT_MOD_NAME
SOURCE_COMPAT_PAK = SOURCE_COMPAT_ROOT / "Paks" / f"{SOURCE_COMPAT_MOD_NAME}.pak"
SOURCE_COMPAT_MOD_JSON = SOURCE_COMPAT_ROOT / "mod.json"
SOURCE_COMPAT_RESOURCES = SOURCE_COMPAT_ROOT / "Resources"

CONTENT_PAKS_ROOT = WORKSPACE_ROOT / "MW5Mercs" / "Content" / "Paks"
OVERRIDE_PAK = CONTENT_PAKS_ROOT / "MW5Mercs-zKnownUniverseStarmap.pak"
OVERRIDE_BACKUP_PAK = CONTENT_PAKS_ROOT / "MW5Mercs-zKnownUniverseStarmap.original-20260506.pak"

REPORT_JSON = REPORTS_DIR / "tku_source_strip_variant.json"
REPORT_MD = REPORTS_DIR / "tku_source_strip_variant.md"

PROFILE_SOURCES = {
    "single": WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "modlist.profile-single-knownuniverse-compat-20260506.json",
    "named_local": WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "modlist.profile-named-local-with-compat-20260506.json",
    "full_stack": WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "modlist.profile-full-stack-with-tku-compat-20260506.json",
}

PROFILE_OUTPUTS = {
    "single": WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "modlist.profile-single-knownuniverse-source-compat-20260506.json",
    "named_local": WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "modlist.profile-named-local-source-compat-20260506.json",
    "full_stack": WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "modlist.profile-full-stack-source-compat-20260506.json",
}

OVERRIDE_CONFLICT_BASES = {
    "/Game/InnerSphereData/MW5_InnerSphereData",
    "/Game/Levels/FrontEnd/StarMap",
}


def manifest_base_path(path: str) -> str:
    if path.endswith(".uasset") or path.endswith(".umap"):
        path = path.rsplit(".", 1)[0]
    return "/" + path.lstrip("/").replace("\\", "/")


def filtered_paths(pak_path: Path, excluded_bases: set[str]) -> tuple[str, list[str], list[str]]:
    _, mount_point, entries = iter_entries(pak_path)
    keep_paths = [entry.game_path for entry in entries if entry.base_game_path not in excluded_bases]
    excluded_paths = [entry.game_path for entry in entries if entry.base_game_path in excluded_bases]
    return mount_point, keep_paths, excluded_paths


def game_only_bases(pak_path: Path) -> set[str]:
    _, _, entries = iter_entries(pak_path)
    return {entry.base_game_path for entry in entries if entry.game_path.startswith("/Game/")}


def override_conflict_bases(pak_path: Path) -> set[str]:
    _, _, entries = iter_entries(pak_path)
    return {entry.base_game_path for entry in entries if entry.base_game_path in OVERRIDE_CONFLICT_BASES}


def unique_override_temp_pak() -> Path:
    candidate = CONTENT_PAKS_ROOT / "MW5Mercs-zKnownUniverseStarmap.repacked.tmp.pak"
    if not candidate.exists():
        return candidate
    counter = 2
    while True:
        candidate = CONTENT_PAKS_ROOT / f"MW5Mercs-zKnownUniverseStarmap.repacked.{counter}.tmp.pak"
        if not candidate.exists():
            return candidate
        counter += 1


def build_filtered_pak(source_pak: Path, output_pak: Path, excluded_bases: set[str]) -> dict[str, object]:
    mount_point, keep_paths, excluded_paths = filtered_paths(source_pak, excluded_bases)
    extracted = extract_exact_paths(source_pak, set(keep_paths))
    missing = [path for path in keep_paths if path not in extracted]
    if missing:
        raise RuntimeError(f"missing extracted files from {source_pak}: {missing}")
    loose_files = [(path, extracted[path]) for path in sorted(keep_paths)]
    size = build_pak(loose_files, output_pak, mount_point=mount_point)
    return {
        "source_pak": str(source_pak),
        "output_pak": str(output_pak),
        "mount_point": mount_point,
        "kept_exact_paths": keep_paths,
        "excluded_exact_paths": excluded_paths,
        "output_size": size,
    }


def build_source_compat_mod() -> dict[str, object]:
    excluded_mod_bases = game_only_bases(ORIGINAL_MOD_PAK)
    reuse_existing = False
    if SOURCE_COMPAT_ROOT.exists():
        try:
            shutil.rmtree(SOURCE_COMPAT_ROOT)
        except PermissionError:
            reuse_existing = SOURCE_COMPAT_PAK.exists() and SOURCE_COMPAT_MOD_JSON.exists()
            if not reuse_existing:
                raise
    original_mod = json.loads(ORIGINAL_MOD_JSON.read_text(encoding="utf-8"))
    manifest = []
    for path in original_mod.get("manifest", []):
        if manifest_base_path(path) in excluded_mod_bases:
            continue
        manifest.append(path)

    if not reuse_existing:
        (SOURCE_COMPAT_ROOT / "Paks").mkdir(parents=True, exist_ok=True)

        pak_report = build_filtered_pak(ORIGINAL_MOD_PAK, SOURCE_COMPAT_PAK, excluded_mod_bases)

        if ORIGINAL_MOD_RESOURCES.exists():
            shutil.copytree(ORIGINAL_MOD_RESOURCES, SOURCE_COMPAT_RESOURCES, dirs_exist_ok=True)
    else:
        pak_report = {
            "source_pak": str(ORIGINAL_MOD_PAK),
            "output_pak": str(SOURCE_COMPAT_PAK),
            "mount_point": "../../../MW5Mercs/",
            "kept_exact_paths": [],
            "excluded_exact_paths": [],
            "output_size": SOURCE_COMPAT_PAK.stat().st_size,
            "reused_existing": True,
        }

    original_mod["displayName"] = "The Known Universe Compat Source"
    original_mod["description"] = (
        "Local plugin-only compatibility variant of TheKnownUniverse. "
        "This build strips all root /Game assets from the TKU mod pak while preserving TKU plugin content."
    )
    original_mod["author"] = "TePa / codex local repack"
    original_mod["buildNumber"] = 39
    original_mod["manifest"] = manifest
    SOURCE_COMPAT_MOD_JSON.write_text(json.dumps(original_mod, indent=3) + "\n", encoding="utf-8")

    return {
        "mod_root": str(SOURCE_COMPAT_ROOT),
        "mod_json": str(SOURCE_COMPAT_MOD_JSON),
        "pak": pak_report,
        "manifest_count": len(manifest),
        "excluded_mod_bases": sorted(excluded_mod_bases),
    }


def replace_override_pak() -> dict[str, object]:
    source_pak = OVERRIDE_BACKUP_PAK if OVERRIDE_BACKUP_PAK.exists() else OVERRIDE_PAK
    temp_pak = unique_override_temp_pak()
    excluded_override_bases = override_conflict_bases(source_pak)
    if not OVERRIDE_BACKUP_PAK.exists():
        shutil.copy2(OVERRIDE_PAK, OVERRIDE_BACKUP_PAK)
    pak_report = build_filtered_pak(source_pak, temp_pak, excluded_override_bases)
    shutil.copy2(temp_pak, OVERRIDE_PAK)
    try:
        temp_pak.unlink(missing_ok=True)
    except PermissionError:
        pass
    pak_report["temp_pak"] = str(temp_pak)
    pak_report["backup_pak"] = str(OVERRIDE_BACKUP_PAK)
    pak_report["live_override_pak"] = str(OVERRIDE_PAK)
    pak_report["excluded_override_bases"] = sorted(excluded_override_bases)
    return pak_report


def rewrite_profile(source_path: Path, output_path: Path):
    data = json.loads(source_path.read_text(encoding="utf-8"))
    mod_status = data.setdefault("modStatus", {})
    mod_status.setdefault(ORIGINAL_MOD_NAME, {})
    mod_status[ORIGINAL_MOD_NAME]["bEnabled"] = False
    mod_status.setdefault(SOURCE_COMPAT_MOD_NAME, {})
    mod_status[SOURCE_COMPAT_MOD_NAME]["bEnabled"] = True
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
        "# TKU Source Strip Variant",
        "",
        "- Strategy: keep the original TKU download untouched, build a plugin-only TKU source mod, and replace the old content override with a backed-up customcontent-only copy.",
        f"- Source compat mod: `{SOURCE_COMPAT_ROOT}`",
        f"- Live override pak: `{OVERRIDE_PAK}`",
        f"- Override backup pak: `{OVERRIDE_BACKUP_PAK}`",
        "",
        "## Excluded Mod Bases",
        "",
    ]
    for base in report["source_mod"]["excluded_mod_bases"]:
        lines.append(f"- `{base}`")
    lines.extend(["", "## Excluded Override Bases", ""])
    for base in report["override"]["excluded_override_bases"]:
        lines.append(f"- `{base}`")
    lines.extend(["", "## Generated Profiles", ""])
    for key, path in report["profiles"].items():
        lines.append(f"- `{key}`: `{path}`")
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    source_mod_report = build_source_compat_mod()
    override_report = replace_override_pak()
    profiles_report = build_profiles()

    report = {
        "source_compat_mod_name": SOURCE_COMPAT_MOD_NAME,
        "compat_patch_name": COMPAT_PATCH_NAME,
        "source_mod": source_mod_report,
        "override": override_report,
        "profiles": profiles_report,
    }
    write_report(report)

    print(f"Wrote {SOURCE_COMPAT_MOD_JSON}")
    print(f"Wrote {SOURCE_COMPAT_PAK}")
    print(f"Updated {OVERRIDE_PAK}")
    print(f"Wrote {REPORT_JSON}")
    print(f"Wrote {REPORT_MD}")


if __name__ == "__main__":
    main()
