from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
sys.path.insert(0, str(TOOLS_ROOT))

from mw5_pak import build_pak, extract_exact_paths  # noqa: E402

GAME_PAK = WORKSPACE / "MW5Mercs" / "Content" / "Paks" / "MW5Mercs-WindowsNoEditor.pak"
MOD_ROOT = WORKSPACE / "MW5Mercs" / "Mods" / "TKUEvidenceStartBorderCompat"
PAK_PATH = MOD_ROOT / "Paks" / "TKUEvidenceStartBorderCompat.pak"
REPORT_DIR = REPORTS_DIR / "tku_editor_first"
REPORT_MD = REPORT_DIR / "tku_evidence_start_border_patch_20260510.md"
REPORT_JSON = REPORT_DIR / "tku_evidence_start_border_patch_20260510.json"

VANILLA_BORDER_PATHS = {
    "/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015.uasset",
    "/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015.uexp",
    "/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges.uasset",
    "/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges.uexp",
    "/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor.uasset",
    "/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor.uexp",
}


def write_mod_json(manifest: list[str]) -> None:
    payload = {
        "displayName": "TKUEvidenceStartBorderCompat",
        "version": "0.1",
        "buildNumber": 1,
        "description": (
            "Evidence-gated TKU start-border stabilizer: reasserts current vanilla 3015/all "
            "border assets and BaseStarMapBorderActor after TKU."
        ),
        "author": "Codex local compatibility build",
        "authorURL": "",
        "defaultLoadOrder": 100,
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
        "# TKU Evidence Start Border Compat Build - 2026-05-10",
        "",
        "## Purpose",
        "",
        "Create a narrow, reversible evidence build to test whether TKU's old career-start border chain is the remaining loading-stall trigger.",
        "",
        "## Evidence Gate",
        "",
        "- `TKUEvidenceStarmapCompat` changed the repeated post-loading `0x4C` fatal crash into a hard loading stall.",
        "- The active mix still leaves TKU `Borders3015`, `AllStarMapBorderChanges`, and `BaseStarMapBorderActor` overriding current assets.",
        "- Current editor evidence shows Davion career start conditions reference `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015`.",
        "- String/package evidence shows TKU `Borders3015` redirects `BorderActor` to `/TheKnownUniverse/2864-01-01/StarMapBorderActor2864-01-01`.",
        "- Package evidence shows that TKU 2864 border actor inherits through `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`.",
        "- Previous runtime history already produced a `BaseStarMapBorderActor_C` superstruct failure when old border actors were mixed into current starmap assets.",
        "",
        "## Build Contents",
        "",
        f"- Output mod: `{report['mod_root']}`",
        f"- Output pak: `{report['pak_path']}`",
        f"- Pak size: `{report['pak_size']}`",
        f"- File count: `{report['file_count']}`",
        "",
        "## Included From Current Vanilla",
        "",
    ]
    for path in report["included_from_vanilla"]:
        lines.append(f"- `{path}`")
    lines.extend(
        [
            "",
            "## Expected Result",
            "",
            "- If the old TKU start-border chain caused the hard stall, the profile `TheKnownUniverse` + `TKUEvidenceStarmapCompat` + this mod should progress past the Davion loading screen.",
            "- If it still stalls without a crash, the next evidence target moves to root data tables, `MW5_TOI_Functions`, and faction/employer assets.",
            "- If the old `0x4C` fatal returns, this border override changed mount interaction and should be disabled before further testing.",
            "",
            "## Known Limitation",
            "",
            "- This intentionally restores current vanilla start-border behavior, so it is not expected to restore TKU's full historical territory overlays.",
            "",
            "## Rollback",
            "",
            "- Disable `TKUEvidenceStartBorderCompat` in `modlist.json`, or remove only the new `MW5Mercs\\Mods\\TKUEvidenceStartBorderCompat` folder.",
            "- Original `TheKnownUniverse.pak`, `TKUEvidenceStarmapCompat`, and `MW5Mercs-zKnownUniverseStarmap.pak` are not edited.",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    if not GAME_PAK.exists():
        raise FileNotFoundError(GAME_PAK)

    vanilla_payloads = extract_exact_paths(GAME_PAK, VANILLA_BORDER_PATHS)
    missing = sorted(VANILLA_BORDER_PATHS - set(vanilla_payloads), key=str.lower)
    if missing:
        raise FileNotFoundError(f"Missing vanilla border payloads: {missing}")

    files = [(path, vanilla_payloads[path]) for path in sorted(vanilla_payloads, key=str.lower)]

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
        "sources": {"game_pak": str(GAME_PAK)},
        "included_from_vanilla": sorted(vanilla_payloads, key=str.lower),
        "expected_result": "Progress past Davion loading if TKU old start-border chain caused the hard stall.",
        "known_limit": "Full TKU historical territory overlays still require current-schema reconstruction.",
    }
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")
    REPORT_MD.write_text(markdown(report), encoding="utf-8")
    print(REPORT_MD)
    print(PAK_PATH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
