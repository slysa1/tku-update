from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
sys.path.insert(0, str(TOOLS_ROOT))
sys.path.insert(0, str(TOOLS_ROOT / "tku_reference_audit"))

from extract_asset_strings import strings_from_payload  # noqa: E402
from mw5_pak import iter_entries, resolve_data_offset  # noqa: E402

SCAN_EXTENSIONS = {".uasset", ".uexp", ".umap"}

TOKENS = [
    "CareerMode_Davion_Start",
    "CareerMode",
    "Davion",
    "Haynesville",
    "StartingLocation",
    "StartCondition",
    "CampaignArc",
    "CampaignArcs",
    "AllStarMapBorderChanges",
    "Borders3015",
    "BaseStarMapBorderActor",
    "StarMapBorderActor",
    "StarMapBordersUpdate_Action",
    "StarMapActor",
    "StarMapPawn",
    "StarSystemBody",
    "MW5_InnerSphereData",
    "EmployerInfoData",
    "SystemFactionChanges",
    "PersonaAnonymousEmployer",
    "Lyran",
    "Steiner",
    "Clan",
    "PlaceClusterToi",
    "CustomContent",
    "ModOverride",
    "/Game/UI/FrontEnd/Starmap",
    "/Game/Campaign/CampaignArcs/BorderChanges",
    "/Plugins/TheKnownUniverse/Content/Regions",
]

ROOT_GAME_PREFIXES = (
    "/Game/Levels/FrontEnd/",
    "/Game/UI/FrontEnd/",
    "/Game/Campaign/CampaignArcs/",
    "/Game/InnerSphereData/",
    "/Game/Employers/",
    "/Game/Factions/",
    "/Game/Campaign/Personas/",
    "/Game/Libraries/",
)

HIGH_RISK_BASES = {
    "/Game/Levels/FrontEnd/StarMap",
    "/Game/UI/FrontEnd/Starmap/StarMapActor",
    "/Game/UI/FrontEnd/StarMapPawn",
    "/Game/UI/FrontEnd/Starmap/StarSystemBody",
    "/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor",
    "/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges",
    "/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015",
    "/Game/InnerSphereData/MW5_InnerSphereData",
    "/Game/InnerSphereData/Updated/EmployerInfoData",
    "/Game/InnerSphereData/Updated/SystemFactionChanges",
    "/Game/Campaign/Personas/ProcMissionPersonas/PersonaAnonymousEmployer",
    "/Game/Campaign/Personas/ProcMissionPersonas/PersonaAnonymousEmployer2",
}


def token_hits(strings: list[str]) -> dict[str, list[str]]:
    hits: dict[str, list[str]] = {}
    for token in TOKENS:
        values = [value for value in strings if token.lower() in value.lower()]
        if values:
            hits[token] = values[:80]
    return hits


def classify_asset(path: str) -> str:
    if any(path.startswith(prefix) for prefix in ROOT_GAME_PREFIXES):
        return "root_game_override"
    if path.startswith("/Plugins/TheKnownUniverse/Content/Regions/"):
        return "plugin_region_or_campaign"
    if path.startswith("/Plugins/TheKnownUniverse/Content/") and re.search(r"/\d{4}-\d{2}-\d{2}/", path):
        return "plugin_timeline_border"
    if path.startswith("/Plugins/TheKnownUniverse/Content/"):
        return "plugin_support"
    return "other"


def read_asset_strings(pak_path: Path, entries) -> list[dict]:
    assets = []
    with pak_path.open("rb") as handle:
        grouped: dict[str, list] = {}
        for entry in entries:
            if entry.extension not in SCAN_EXTENSIONS:
                continue
            grouped.setdefault(entry.base_game_path, []).append(entry)

        for base_path, sidecars in sorted(grouped.items(), key=lambda item: item[0].lower()):
            strings: set[str] = set()
            files = []
            sizes = 0
            for entry in sidecars:
                files.append(entry.game_path)
                sizes += entry.size
                if entry.encrypted or entry.compression_method_index:
                    continue
                data_offset = resolve_data_offset(handle, entry.offset)
                handle.seek(data_offset)
                strings.update(strings_from_payload(handle.read(entry.size)))
            hits = token_hits(sorted(strings, key=str.lower))
            if hits or base_path in HIGH_RISK_BASES:
                assets.append(
                    {
                        "base_path": base_path,
                        "class": classify_asset(base_path),
                        "files": files,
                        "total_size": sizes,
                        "string_count": len(strings),
                        "token_hits": hits,
                    }
                )
    return assets


def summarize(report: dict) -> str:
    lines = [
        "# TKU Crash Surface Scan",
        "",
        "This report scans strings across original TKU cooked assets to narrow the editor/tool inspection surface for the repeated Davion career-load `0x4C` crash. It is not proof of runtime execution by itself.",
        "",
        f"- Source pak: `{report['source_pak']}`",
        f"- Assets with relevant token hits or high-risk classification: `{len(report['assets'])}`",
        "",
        "## High-Signal Interpretation",
        "",
        "- The crash reproduces with TKU alone, so assets in this pak are sufficient to trigger it.",
        "- Any asset listed here still needs editor/tool inspection before a rebuild is justified.",
        "- Root `/Game` substitutions are higher risk than plugin-only content because reduced plugin-only builds previously loaded farther.",
        "",
        "## Token Coverage",
        "",
    ]
    for token, count in report["token_asset_counts"].items():
        lines.append(f"- `{token}`: `{count}` assets")
    lines.extend(["", "## Class Counts", ""])
    for class_name, count in report["class_counts"].items():
        lines.append(f"- `{class_name}`: `{count}`")
    lines.extend(["", "## High-Risk Root Assets", ""])
    for asset in report["assets"]:
        if asset["class"] != "root_game_override":
            continue
        lines.append(f"### `{asset['base_path']}`")
        lines.append("")
        lines.append(f"- files: {', '.join(asset['files'])}")
        lines.append(f"- strings: `{asset['string_count']}`")
        if asset["token_hits"]:
            lines.append("- tokens: " + ", ".join(f"`{token}`" for token in asset["token_hits"]))
        for token in ("CareerMode", "Davion", "Haynesville", "StartingLocation", "StartCondition", "StarMapActor", "StarSystemBody", "BaseStarMapBorderActor", "AllStarMapBorderChanges", "Borders3015", "EmployerInfoData", "SystemFactionChanges", "ModOverride"):
            values = asset["token_hits"].get(token, [])
            if values:
                lines.append(f"- `{token}` examples: " + "; ".join(f"`{value}`" for value in values[:8]))
        lines.append("")
    lines.extend(["## Plugin Region And Timeline Assets", ""])
    for asset in report["assets"]:
        if asset["class"] not in {"plugin_region_or_campaign", "plugin_timeline_border"}:
            continue
        lines.append(f"### `{asset['base_path']}`")
        lines.append("")
        lines.append("- tokens: " + ", ".join(f"`{token}`" for token in asset["token_hits"]))
        for token, values in asset["token_hits"].items():
            lines.append(f"- `{token}` examples: " + "; ".join(f"`{value}`" for value in values[:6]))
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--pak",
        type=Path,
        default=WORKSPACE / "MW5Mercs" / "Mods" / "TheKnownUniverse" / "Paks" / "TheKnownUniverse.pak",
    )
    parser.add_argument("--out-dir", type=Path, default=REPORTS_DIR / "tku_editor_first")
    args = parser.parse_args()

    _, _, entries = iter_entries(args.pak)
    assets = read_asset_strings(args.pak, entries)
    token_counts = Counter()
    class_counts = Counter(asset["class"] for asset in assets)
    for asset in assets:
        for token in asset["token_hits"]:
            token_counts[token] += 1
    report = {
        "source_pak": str(args.pak),
        "tokens": TOKENS,
        "token_asset_counts": dict(sorted(token_counts.items())),
        "class_counts": dict(class_counts.most_common()),
        "assets": assets,
    }
    args.out_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.out_dir / "tku_crash_surface_scan.json"
    md_path = args.out_dir / "tku_crash_surface_scan.md"
    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    md_path.write_text(summarize(report), encoding="utf-8")
    print(json_path)
    print(md_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
