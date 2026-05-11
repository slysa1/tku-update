from __future__ import annotations

import json
import shutil
from pathlib import Path

from mw5_pak import build_pak, extract_exact_paths, iter_entries

from tku_project_paths import GAME_ROOT as WORKSPACE_ROOT, REPORTS_DIR

MOD_NAME = "TheKnownUniverse"
MOD_ROOT = WORKSPACE_ROOT / "MW5Mercs" / "Mods" / MOD_NAME
MOD_PAK = MOD_ROOT / "Paks" / "TheKnownUniverse.pak"
MOD_JSON = MOD_ROOT / "mod.json"
MOD_RESOURCES = MOD_ROOT / "Resources"

BACKUP_ROOT = WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "TheKnownUniverse.original-20260506"
BACKUP_PAK = BACKUP_ROOT / "Paks" / "TheKnownUniverse.pak"
BACKUP_JSON = BACKUP_ROOT / "mod.json"

LEGACY_STARMAP_PAK = WORKSPACE_ROOT / "MW5Mercs" / "Content" / "Paks" / "MW5Mercs-zKnownUniverseStarmap.pak"
LEGACY_STARMAP_PAK_BACKUP = WORKSPACE_ROOT / "MW5Mercs" / "Content" / "Paks" / "MW5Mercs-zKnownUniverseStarmap.original-20260506.pak"

DISABLE_CONTENT_PAKS = [
    LEGACY_STARMAP_PAK,
    WORKSPACE_ROOT / "MW5Mercs" / "Content" / "Paks" / "MW5Mercs-zzzKnownUniverseCompatPatch.pak",
    WORKSPACE_ROOT / "MW5Mercs" / "Content" / "Paks" / "MW5Mercs-zzzzKnownUniverseTierCRestore.pak",
]

DISABLE_CONTENT_PAK_GLOBS = [
    "MW5Mercs-zKnownUniverseStarmap.repacked*.tmp.pak",
]

REPORT_JSON = REPORTS_DIR / "tku_same_name_compat_source.json"
REPORT_MD = REPORTS_DIR / "tku_same_name_compat_source.md"
MERGE_LEGACY_CUSTOM_CONTENT = False
KEEP_ONLY_PLUGIN_CONTENT = True
ALLOWED_ROOT_BASES = {
    "/Game/Levels/FrontEnd/StarMap",
}

EXCLUDED_BASES = {
    "/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015",
    "/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges",
    "/Game/InnerSphereData/MW5_InnerSphereData",
    "/Game/InnerSphereData/Updated/EmployerInfoData",
    "/Game/InnerSphereData/Updated/SystemFactionChanges",
    "/Game/Libraries/MW5_TOI_Functions",
    "/Game/UI/FrontEnd/StarMapPawn",
    "/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL",
    "/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF",
    "/Game/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL",
    "/Game/UI/FrontEnd/Starmap/StarMapActor",
    "/Game/UI/FrontEnd/Starmap/StarSystemBody",
    "/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor",
}


def ensure_backup():
    if BACKUP_ROOT.exists():
        return
    shutil.copytree(MOD_ROOT, BACKUP_ROOT)


def manifest_base_path(path: str) -> str:
    if path.endswith(".uasset") or path.endswith(".umap"):
        path = path.rsplit(".", 1)[0]
    return "/" + path.lstrip("/").replace("\\", "/")


def build_repacked_mod() -> dict[str, object]:
    source_pak = BACKUP_PAK if BACKUP_PAK.exists() else MOD_PAK
    source_json = BACKUP_JSON if BACKUP_JSON.exists() else MOD_JSON

    _, mount_point, entries = iter_entries(source_pak)
    keep_paths = []
    for entry in entries:
        if entry.base_game_path in EXCLUDED_BASES:
            continue
        if (
            KEEP_ONLY_PLUGIN_CONTENT
            and entry.game_path.startswith("/Game/")
            and entry.base_game_path not in ALLOWED_ROOT_BASES
        ):
            continue
        keep_paths.append(entry.game_path)
    extracted = extract_exact_paths(source_pak, set(keep_paths))
    missing = [path for path in keep_paths if path not in extracted]
    if missing:
        raise RuntimeError(f"missing files from {source_pak}: {missing}")

    legacy_custom_content_pak = LEGACY_STARMAP_PAK_BACKUP if LEGACY_STARMAP_PAK_BACKUP.exists() else LEGACY_STARMAP_PAK
    merged_custom_content_paths: list[str] = []
    if MERGE_LEGACY_CUSTOM_CONTENT and legacy_custom_content_pak.exists():
        _, _, legacy_entries = iter_entries(legacy_custom_content_pak)
        merged_custom_content_paths = sorted(
            entry.game_path for entry in legacy_entries if entry.game_path.startswith("/Game/CustomContent/")
        )
        if merged_custom_content_paths:
            legacy_extracted = extract_exact_paths(legacy_custom_content_pak, set(merged_custom_content_paths))
            missing_legacy = [path for path in merged_custom_content_paths if path not in legacy_extracted]
            if missing_legacy:
                raise RuntimeError(f"missing custom content files from {legacy_custom_content_pak}: {missing_legacy}")
            extracted.update(legacy_extracted)

    loose_paths = sorted(set(keep_paths) | set(merged_custom_content_paths))
    loose_files = [(path, extracted[path]) for path in loose_paths]
    pak_size = build_pak(loose_files, MOD_PAK, mount_point=mount_point)

    source_mod_json = json.loads(source_json.read_text(encoding="utf-8"))
    filtered_manifest = [
        path
        for path in source_mod_json.get("manifest", [])
        if manifest_base_path(path) not in EXCLUDED_BASES
        and not (
            KEEP_ONLY_PLUGIN_CONTENT
            and manifest_base_path(path).startswith("/Game/")
            and manifest_base_path(path) not in ALLOWED_ROOT_BASES
        )
    ]
    source_mod_json["description"] = (
        "Compatibility repack of TheKnownUniverse for local MW5 testing. "
        "Keeps TKU plugin content plus the TKU StarMap level under the original mod id, while "
        "the modern base game supplies the remaining root /Game starmap shell classes, faction, "
        "employer, border, data, and shared logic assets."
    )
    source_mod_json["author"] = "TePa / codex local repack"
    source_mod_json["buildNumber"] = 59
    source_mod_json["manifest"] = filtered_manifest
    MOD_JSON.write_text(json.dumps(source_mod_json, indent=3) + "\n", encoding="utf-8")

    return {
        "mod_root": str(MOD_ROOT),
        "source_pak": str(source_pak),
        "legacy_custom_content_pak": str(legacy_custom_content_pak) if legacy_custom_content_pak.exists() else None,
        "output_pak": str(MOD_PAK),
        "output_size": pak_size,
        "kept_entry_count": len(loose_paths),
        "merged_custom_content_entry_count": len(merged_custom_content_paths),
        "excluded_bases": sorted(EXCLUDED_BASES),
        "manifest_count": len(filtered_manifest),
    }


def disable_extra_content_paks() -> list[str]:
    disabled: list[str] = []
    pak_paths = list(DISABLE_CONTENT_PAKS)
    content_paks_dir = WORKSPACE_ROOT / "MW5Mercs" / "Content" / "Paks"
    for pattern in DISABLE_CONTENT_PAK_GLOBS:
        pak_paths.extend(sorted(content_paks_dir.glob(pattern)))

    for pak_path in pak_paths:
        if not pak_path.exists():
            continue
        disabled_path = pak_path.with_suffix(pak_path.suffix + ".disabled")
        if disabled_path.exists():
            disabled.append(str(disabled_path))
            continue
        pak_path.rename(disabled_path)
        disabled.append(str(disabled_path))
    return disabled


def write_report(report: dict[str, object]):
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")

    lines = [
        "# TKU Same-Name Compat Source",
        "",
        "- Strategy: preserve a full backup of the original `TheKnownUniverse` folder, then repack the live `TheKnownUniverse` mod under the same mod id with the stable TKU root substitutions, all original plugin content, and the legacy `CustomContent` starmap assets merged into the mod package.",
        f"- Live mod root: `{MOD_ROOT}`",
        f"- Backup mod root: `{BACKUP_ROOT}`",
        "",
        "## Merge Notes",
        "",
        f"- Merged legacy custom-content entries: `{report['repacked_mod']['merged_custom_content_entry_count']}`",
        f"- Legacy custom-content source pak: `{report['repacked_mod']['legacy_custom_content_pak']}`",
        "",
        "## Excluded Bases",
        "",
    ]
    for base in report["repacked_mod"]["excluded_bases"]:
        lines.append(f"- `{base}`")
    if report["disabled_content_paks"]:
        lines.extend(["", "## Disabled Content Paks", ""])
        for path in report["disabled_content_paks"]:
            lines.append(f"- `{path}`")
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    ensure_backup()
    repacked_mod = build_repacked_mod()
    disabled_content_paks = disable_extra_content_paks()

    report = {
        "mod_name": MOD_NAME,
        "backup_root": str(BACKUP_ROOT),
        "repacked_mod": repacked_mod,
        "disabled_content_paks": disabled_content_paks,
    }
    write_report(report)

    print(f"Wrote {MOD_JSON}")
    print(f"Wrote {MOD_PAK}")
    print(f"Wrote {REPORT_JSON}")
    print(f"Wrote {REPORT_MD}")


if __name__ == "__main__":
    main()
