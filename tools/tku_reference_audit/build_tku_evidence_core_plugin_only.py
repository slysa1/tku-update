from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path

import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mw5_pak import build_pak, extract_exact_paths, iter_entries


from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
SOURCE_MOD = WORKSPACE / "MW5Mercs" / "Mods" / "TheKnownUniverse"
SOURCE_PAK = SOURCE_MOD / "Paks" / "TheKnownUniverse.pak"
SOURCE_MOD_JSON = SOURCE_MOD / "mod.json"
SOURCE_RESOURCES = SOURCE_MOD / "Resources"

OUTPUT_MOD_NAME = "TKUEvidenceCorePluginOnly"
OUTPUT_ROOT = WORKSPACE / "MW5Mercs" / "Mods" / OUTPUT_MOD_NAME
OUTPUT_PAK = OUTPUT_ROOT / "Paks" / f"{OUTPUT_MOD_NAME}.pak"
OUTPUT_MOD_JSON = OUTPUT_ROOT / "mod.json"
OUTPUT_RESOURCES = OUTPUT_ROOT / "Resources"

REPORT_DIR = REPORTS_DIR / "tku_editor_first"
REPORT_MD = REPORT_DIR / "tku_evidence_core_plugin_only_20260510.md"
REPORT_JSON = REPORT_DIR / "tku_evidence_core_plugin_only_20260510.json"

EVIDENCE_REPORTS = [
    "reports\\tku_runtime_isolation_20260510.md",
    "reports\\tku_editor_first\\ue4_starmap_border_path_inspection.md",
    "reports\\tku_editor_first\\tku_cooked_package_refs.md",
    "reports\\tku_editor_first\\tku_structured_reference_findings_20260510.md",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def build() -> dict[str, object]:
    if not SOURCE_PAK.exists():
        raise FileNotFoundError(SOURCE_PAK)
    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    (OUTPUT_ROOT / "Paks").mkdir(parents=True, exist_ok=True)

    _, mount_point, entries = iter_entries(SOURCE_PAK)
    kept_paths = sorted(entry.game_path for entry in entries if not entry.game_path.startswith("/Game/"))
    removed_game_paths = sorted(entry.game_path for entry in entries if entry.game_path.startswith("/Game/"))
    extracted = extract_exact_paths(SOURCE_PAK, set(kept_paths))
    missing = [path for path in kept_paths if path not in extracted]
    if missing:
        raise RuntimeError(f"missing extracted files from original TKU pak: {missing[:20]}")

    pak_size = build_pak(
        [(path, extracted[path]) for path in kept_paths],
        OUTPUT_PAK,
        mount_point=mount_point,
    )

    if SOURCE_RESOURCES.exists():
        shutil.copytree(SOURCE_RESOURCES, OUTPUT_RESOURCES, dirs_exist_ok=True)

    original_mod_json = json.loads(SOURCE_MOD_JSON.read_text(encoding="utf-8"))
    mod_json = {
        "displayName": "TKU Evidence Core Plugin Only",
        "version": "0.1.0-evidence",
        "buildNumber": 1,
        "description": (
            "Evidence-backed local TKU baseline built from the restored original build-38 pak. "
            "Keeps only non-/Game TKU plugin content and excludes root starmap, border, data, employer, "
            "faction, persona, and material substitutions that are not current-schema safe."
        ),
        "author": f"{original_mod_json.get('author', 'TePa')} / local evidence rebuild",
        "authorURL": original_mod_json.get("authorURL", ""),
        "defaultLoadOrder": 90,
        "gameVersion": "1.13.378",
        "manifest": [],
        "steamPublishedFileId": 0,
        "steamLastSubmittedBuildNumber": 0,
        "steamModVisibility": "Private",
    }
    OUTPUT_MOD_JSON.write_text(json.dumps(mod_json, indent=3) + "\n", encoding="utf-8")

    removed_groups = {
        "/Game/Campaign/CampaignArcs/BorderChanges": 0,
        "/Game/UI/FrontEnd/Starmap": 0,
        "/Game/UI/FrontEnd/StarMapPawn": 0,
        "/Game/Levels/FrontEnd/StarMap": 0,
        "/Game/InnerSphereData": 0,
        "/Game/Employers": 0,
        "/Game/Factions": 0,
        "/Game/Campaign/Personas": 0,
        "/Game/Libraries/MW5_TOI_Functions": 0,
        "/Game/other": 0,
    }
    for path in removed_game_paths:
        matched = False
        for prefix in list(removed_groups):
            if prefix != "/Game/other" and path.startswith(prefix):
                removed_groups[prefix] += 1
                matched = True
                break
        if not matched:
            removed_groups["/Game/other"] += 1

    return {
        "output_mod_name": OUTPUT_MOD_NAME,
        "source_mod": str(SOURCE_MOD),
        "source_pak": str(SOURCE_PAK),
        "source_pak_sha256": sha256(SOURCE_PAK),
        "output_root": str(OUTPUT_ROOT),
        "output_pak": str(OUTPUT_PAK),
        "output_pak_sha256": sha256(OUTPUT_PAK),
        "output_pak_size": pak_size,
        "mount_point": mount_point,
        "total_source_entries": len(entries),
        "kept_entries": len(kept_paths),
        "removed_game_entries": len(removed_game_paths),
        "kept_plugin_entries": sum(1 for path in kept_paths if path.startswith("/Plugins/")),
        "kept_other_entries": sum(1 for path in kept_paths if not path.startswith("/Plugins/")),
        "removed_groups": removed_groups,
        "sample_removed_game_paths": removed_game_paths[:80],
        "sample_kept_paths": kept_paths[:80],
        "evidence_reports": EVIDENCE_REPORTS,
    }


def write_report(report: dict[str, object]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")
    lines = [
        "# TKU Evidence Core Plugin-Only Build - 2026-05-10",
        "",
        "## Purpose",
        "",
        "Create a clean-source TKU baseline from the restored original build-38 pak without loading the root `/Game` substitutions that current evidence has made unsafe.",
        "",
        "This is not a final compatibility patch. It is the next gated runtime baseline: prove that original TKU plugin content plus the original loose starmap override can load without the stale root border/starmap class stack.",
        "",
        "## Evidence Gate",
        "",
        "- Original `TheKnownUniverse.pak` alone is sufficient to reproduce the career-load fatal crash.",
        "- Editor inspection shows current `StarMapActor_2570_C` and all vanilla dated border actors inherit `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor_C`.",
        "- TKU cooked root `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor` is stale and caused the `Could not find SuperStruct BaseStarMapBorderActor_C to create StarMapActor_2570_C` crash family.",
        "- Original TKU `StarMapActor` / `StarSystemBody` lack current cluster-data hooks; replacing only those assets produced a loading stall rather than a fix.",
        "- Previous reduced testing showed plugin-only TKU content could load farther than the full root override set, but this build is regenerated from the restored original pak, not from failed blind artifacts.",
        "",
        "## Build Output",
        "",
        f"- Output mod: `{report['output_root']}`",
        f"- Output pak: `{report['output_pak']}`",
        f"- Output pak SHA256: `{report['output_pak_sha256']}`",
        f"- Source pak SHA256: `{report['source_pak_sha256']}`",
        f"- Source entries: `{report['total_source_entries']}`",
        f"- Kept entries: `{report['kept_entries']}`",
        f"- Removed root `/Game` entries: `{report['removed_game_entries']}`",
        "",
        "## Removed Root Groups",
        "",
    ]
    for group, count in report["removed_groups"].items():
        lines.append(f"- `{group}`: `{count}`")
    lines.extend(
        [
            "",
            "## Next Runtime Meaning",
            "",
            "- If this profile still crashes with the original `0x4C` hash, then plugin content or the always-loaded loose override still contains a fatal path and the plugin-only assumption is false.",
            "- If this profile loads, it becomes the safe baseline for editor-authored current-schema repairs: map bounds via current `StarMapPawn`, overlay via `MWClusterDataAsset`, and only recreated/reparented border assets if proven necessary.",
            "- If it loads but lacks expanded map bounds or non-major overlays, that is expected and should not be papered over by restoring old root assets.",
            "",
            "## What Not To Restore In This Build",
            "",
            "- Do not restore TKU root `BaseStarMapBorderActor`, `Borders3015`, or dated root border assets.",
            "- Do not restore TKU root `StarMapActor`, `StarSystemBody`, `StarMapPawn`, or `StarMap.umap` directly.",
            "- Do not restore TKU root employer/faction assets as a group; previous runtime evidence tied that pattern to ownership regressions.",
            "",
            "## Evidence Sources",
            "",
        ]
    )
    for path in report["evidence_reports"]:
        lines.append(f"- `{path}`")
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    report = build()
    write_report(report)
    print(f"Wrote {OUTPUT_MOD_JSON}")
    print(f"Wrote {OUTPUT_PAK}")
    print(f"Wrote {REPORT_MD}")
    print(f"Wrote {REPORT_JSON}")


if __name__ == "__main__":
    main()
