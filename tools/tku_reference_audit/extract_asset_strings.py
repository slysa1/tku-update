from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
sys.path.insert(0, str(TOOLS_ROOT))

from mw5_pak import extract_exact_paths, iter_entries  # noqa: E402

ASCII_RE = re.compile(rb"[\x20-\x7e]{4,}")
UTF16_RE = re.compile((rb"(?:[\x20-\x7e]\x00){4,}"))

TARGET_BASES = [
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
    "/Game/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL",
    "/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL",
    "/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF",
]

IMPORTANT_TOKENS = [
    "StarMap",
    "StarMapActor",
    "StarMapPawn",
    "StarSystemBody",
    "BaseStarMapBorderActor",
    "StarMapBorderActor",
    "StarMapBordersUpdate",
    "BorderChanges",
    "Faction",
    "Employer",
    "Lyran",
    "Steiner",
    "Clan",
    "TheKnownUniverse",
    "InnerSphere",
    "SystemFaction",
    "FactionColours",
    "FactionBorder",
    "Map",
    "Bounds",
    "Camera",
    "Zoom",
]


def strings_from_payload(payload: bytes) -> list[str]:
    found: set[str] = set()
    for match in ASCII_RE.finditer(payload):
        found.add(match.group(0).decode("utf-8", "replace"))
    for match in UTF16_RE.finditer(payload):
        found.add(match.group(0).decode("utf-16-le", "replace").rstrip("\x00"))
    return sorted(found, key=str.lower)


def classify_strings(strings: list[str]) -> dict[str, list[str]]:
    classes: dict[str, list[str]] = {}
    for token in IMPORTANT_TOKENS:
        hits = [s for s in strings if token.lower() in s.lower()]
        if hits:
            classes[token] = hits[:200]
    path_hits = [
        s
        for s in strings
        if s.startswith("/Game/")
        or s.startswith("/Plugins/")
        or s.startswith("BlueprintGeneratedClass")
        or s.startswith("Class'")
    ]
    if path_hits:
        classes["asset_paths"] = path_hits[:400]
    return classes


def markdown_summary(report: dict) -> str:
    lines = [
        "# TKU Cooked Asset String Reference Scan",
        "",
        "This is a terminal-only scan of strings embedded in selected cooked TKU assets. It is evidence for references and naming, not a substitute for MW5 Mod Editor inspection.",
        "",
        f"- Source pak: `{report['source_pak']}`",
        f"- Selected exact files: {report['selected_file_count']}",
        "",
        "## Selected Assets",
        "",
    ]
    for item in report["assets"]:
        lines.append(f"### `{item['base_path']}`")
        lines.append("")
        lines.append(f"- files: {', '.join(item['files'])}")
        lines.append(f"- string_count: {item['string_count']}")
        if item["important"]:
            lines.append("- notable tokens: " + ", ".join(sorted(item["important"].keys())))
        else:
            lines.append("- notable tokens: none")
        for key in ("asset_paths", "BaseStarMapBorderActor", "StarMapActor", "StarMapPawn", "StarSystemBody", "Lyran", "Steiner", "Clan", "Faction", "Bounds", "Camera", "Zoom"):
            values = item["important"].get(key, [])
            if values:
                lines.append("")
                lines.append(f"Key `{key}` examples:")
                for value in values[:20]:
                    lines.append(f"- `{value}`")
        lines.append("")
    lines.append("## Token Counts")
    lines.append("")
    for token, count in report["token_counts"].items():
        lines.append(f"- `{token}`: {count}")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pak", type=Path, default=WORKSPACE / "MW5Mercs" / "Mods" / "TheKnownUniverse" / "Paks" / "TheKnownUniverse.pak")
    parser.add_argument("--out-dir", type=Path, default=REPORTS_DIR / "tku_editor_first")
    args = parser.parse_args()

    _, _, entries = iter_entries(args.pak)
    wanted: set[str] = set()
    files_by_base: dict[str, list[str]] = {}
    for base in TARGET_BASES:
        files = [
            entry.game_path
            for entry in entries
            if entry.base_game_path.lower() == base.lower()
            and entry.extension in {".uasset", ".uexp", ".umap", ".ubulk"}
        ]
        files_by_base[base] = files
        wanted.update(files)

    extracted = extract_exact_paths(args.pak, wanted)
    assets = []
    token_counter: Counter[str] = Counter()
    for base, files in files_by_base.items():
        strings: list[str] = []
        for file_path in files:
            payload = extracted.get(file_path)
            if payload is not None:
                strings.extend(strings_from_payload(payload))
        strings = sorted(set(strings), key=str.lower)
        important = classify_strings(strings)
        for token in important:
            token_counter[token] += 1
        assets.append(
            {
                "base_path": base,
                "files": files,
                "string_count": len(strings),
                "important": important,
            }
        )

    report = {
        "source_pak": str(args.pak),
        "selected_file_count": len(wanted),
        "target_bases": TARGET_BASES,
        "assets": assets,
        "token_counts": dict(sorted(token_counter.items())),
    }

    args.out_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.out_dir / "tku_cooked_asset_string_scan.json"
    md_path = args.out_dir / "tku_cooked_asset_string_scan.md"
    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    md_path.write_text(markdown_summary(report), encoding="utf-8")
    print(json_path)
    print(md_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
