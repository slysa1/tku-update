from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
sys.path.insert(0, str(TOOLS_ROOT))

from mw5_pak import build_pak, extract_exact_paths, iter_entries  # noqa: E402

GAME_PAK = WORKSPACE / "MW5Mercs" / "Content" / "Paks" / "MW5Mercs-WindowsNoEditor.pak"
LOOSE_TKU_STARMAP_PAK = WORKSPACE / "MW5Mercs" / "Content" / "Paks" / "MW5Mercs-zKnownUniverseStarmap.pak"
MOD_ROOT = WORKSPACE / "MW5Mercs" / "Mods" / "TKUEvidenceStarmapCompat"
PAK_PATH = MOD_ROOT / "Paks" / "TKUEvidenceStarmapCompat.pak"
REPORT_DIR = REPORTS_DIR / "tku_editor_first"
REPORT_MD = REPORT_DIR / "tku_evidence_starmap_class_patch_20260510.md"
REPORT_JSON = REPORT_DIR / "tku_evidence_starmap_class_patch_20260510.json"

VANILLA_CLASS_PATHS = {
    "/Game/UI/FrontEnd/Starmap/StarMapActor.uasset",
    "/Game/UI/FrontEnd/Starmap/StarMapActor.uexp",
    "/Game/UI/FrontEnd/Starmap/StarSystemBody.uasset",
    "/Game/UI/FrontEnd/Starmap/StarSystemBody.uexp",
}


def loose_override_paths() -> list[str]:
    _, _, entries = iter_entries(LOOSE_TKU_STARMAP_PAK)
    return [
        entry.game_path
        for entry in entries
        if entry.extension in {".uasset", ".uexp", ".umap", ".ubulk"}
    ]


def write_mod_json(manifest: list[str]) -> None:
    payload = {
        "displayName": "TKUEvidenceStarmapCompat",
        "version": "0.1",
        "buildNumber": 1,
        "description": (
            "Evidence-gated TKU stabilizer: reasserts the original loose TKU starmap override "
            "after TKU and replaces only StarMapActor/StarSystemBody with current vanilla class assets."
        ),
        "author": "Codex local compatibility build",
        "authorURL": "",
        "defaultLoadOrder": 99,
        "gameVersion": "1.13.378",
        "manifest": sorted(manifest, key=str.lower),
        "steamPublishedFileId": 0,
        "steamLastSubmittedBuildNumber": 0,
        "steamModVisibility": "Private",
    }
    MOD_ROOT.mkdir(parents=True, exist_ok=True)
    (MOD_ROOT / "mod.json").write_text(json.dumps(payload, indent=3), encoding="utf-8")


def markdown(report: dict) -> str:
    lines = [
        "# TKU Evidence Starmap Compat Build - 2026-05-10",
        "",
        "## Purpose",
        "",
        "Create a narrow, reversible evidence build to test the current fatal-crash hypothesis without editing original TKU files.",
        "",
        "## Evidence Gate",
        "",
        "- Runtime isolation pinned the repeated `0x4C` fatal crash to `TheKnownUniverse.pak`.",
        "- The loose `MW5Mercs-zKnownUniverseStarmap.pak` loaded a Davion career successfully with no enabled mods.",
        "- Structured package-table parsing shows the loose starmap binds to current `/Game` starmap classes.",
        "- Structured package-table parsing shows TKU's mod-pak starmap binds to `/ModOverride/TheKnownUniverse` starmap classes.",
        "- Structured package-table parsing shows current vanilla `StarSystemBody` imports `MWClusterDataAsset` and exports current cluster-mesh hooks that original TKU lacks.",
        "",
        "## Build Contents",
        "",
        f"- Output mod: `{report['mod_root']}`",
        f"- Output pak: `{report['pak_path']}`",
        f"- Pak size: `{report['pak_size']}`",
        f"- File count: `{report['file_count']}`",
        "",
        "## Source Groups",
        "",
        f"- Safe loose override source: `{report['sources']['loose_override_pak']}`",
        f"- Current vanilla class source: `{report['sources']['game_pak']}`",
        "",
        "## Included From Loose Override",
        "",
    ]
    for path in report["included_from_loose_override"]:
        lines.append(f"- `{path}`")
    lines.extend(["", "## Included From Current Vanilla", ""])
    for path in report["included_from_vanilla"]:
        lines.append(f"- `{path}`")
    lines.extend(
        [
            "",
            "## Expected Result",
            "",
            "- If the old TKU starmap class stack is the fatal cause, TKU plus this compat mod should reach career gameplay after Davion start.",
            "- If it still crashes with the same `0x4C` hash, the next suspect moves from starmap class assets to root data/campaign-start assets.",
            "- This build is not expected to fully restore all non-major territory overlays; cluster-data migration remains a separate task.",
            "",
            "## Rollback",
            "",
            "- Disable `TKUEvidenceStarmapCompat` in `modlist.json`, or remove only the new `MW5Mercs\\Mods\\TKUEvidenceStarmapCompat` folder.",
            "- Original `TheKnownUniverse.pak` and `MW5Mercs-zKnownUniverseStarmap.pak` were not edited.",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    if not GAME_PAK.exists():
        raise FileNotFoundError(GAME_PAK)
    if not LOOSE_TKU_STARMAP_PAK.exists():
        raise FileNotFoundError(LOOSE_TKU_STARMAP_PAK)

    loose_paths = loose_override_paths()
    loose_payloads = extract_exact_paths(LOOSE_TKU_STARMAP_PAK, set(loose_paths))
    vanilla_payloads = extract_exact_paths(GAME_PAK, VANILLA_CLASS_PATHS)

    files: list[tuple[str, bytes]] = []
    for path in sorted(loose_payloads, key=str.lower):
        files.append((path, loose_payloads[path]))
    for path in sorted(vanilla_payloads, key=str.lower):
        files.append((path, vanilla_payloads[path]))

    PAK_PATH.parent.mkdir(parents=True, exist_ok=True)
    pak_size = build_pak(files, PAK_PATH)

    manifest = [path for path, _ in files if path.endswith((".uasset", ".umap"))]
    write_mod_json(manifest)

    report = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "mod_root": str(MOD_ROOT),
        "pak_path": str(PAK_PATH),
        "pak_size": pak_size,
        "file_count": len(files),
        "sources": {
            "game_pak": str(GAME_PAK),
            "loose_override_pak": str(LOOSE_TKU_STARMAP_PAK),
        },
        "included_from_loose_override": sorted(loose_payloads, key=str.lower),
        "included_from_vanilla": sorted(vanilla_payloads, key=str.lower),
        "expected_result": "Fatal crash should clear if old TKU starmap class stack is the cause.",
        "known_limit": "Non-major territory overlays still require current MWClusterDataAsset migration.",
    }
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")
    REPORT_MD.write_text(markdown(report), encoding="utf-8")
    print(REPORT_MD)
    print(PAK_PATH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
