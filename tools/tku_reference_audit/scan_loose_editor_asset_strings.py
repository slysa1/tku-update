from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path

ASCII_RE = re.compile(rb"[\x20-\x7e]{4,}")
UTF16_RE = re.compile(rb"(?:[\x20-\x7e]\x00){4,}")

TARGETS = {
    "/Game/Levels/FrontEnd/StarMap": [
        "MW5Mercs/Content/Levels/FrontEnd/StarMap.umap",
    ],
    "/Game/UI/FrontEnd/Starmap/StarMapActor": [
        "MW5Mercs/Content/UI/FrontEnd/Starmap/StarMapActor.uasset",
    ],
    "/Game/UI/FrontEnd/StarMapPawn": [
        "MW5Mercs/Content/UI/FrontEnd/StarMapPawn.uasset",
    ],
    "/Game/UI/FrontEnd/Starmap/StarSystemBody": [
        "MW5Mercs/Content/UI/FrontEnd/Starmap/StarSystemBody.uasset",
    ],
    "/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor": [
        "MW5Mercs/Content/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor.uasset",
    ],
    "/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges": [
        "MW5Mercs/Content/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges.uasset",
    ],
    "/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015": [
        "MW5Mercs/Content/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015.uasset",
    ],
    "/Game/InnerSphereData/MW5_InnerSphereData": [
        "MW5Mercs/Content/InnerSphereData/MW5_InnerSphereData.uasset",
        "MW5Mercs/Content/InnerSphereData/MW5_InnerSphereData.csv",
        "MW5Mercs/Content/Data/InnerSphereMap/MW5_InnerSphereData.json",
    ],
    "/Game/InnerSphereData/Updated/EmployerInfoData": [
        "MW5Mercs/Content/InnerSphereData/Updated/EmployerInfoData.uasset",
    ],
    "/Game/InnerSphereData/Updated/SystemFactionChanges": [
        "MW5Mercs/Content/InnerSphereData/Updated/SystemFactionChanges.uasset",
    ],
    "/Game/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL": [
        "MW5Mercs/Content/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL.uasset",
    ],
    "/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL": [
        "MW5Mercs/Content/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL.uasset",
    ],
    "/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF": [
        "MW5Mercs/Content/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF.uasset",
    ],
    "/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets": [
        "MW5Mercs/Content/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets.uasset",
    ],
}

IMPORTANT_TOKENS = [
    "/Game/",
    "/ModOverride/",
    "/Plugins/",
    "StarMap",
    "StarMapActor",
    "StarMapPawn",
    "StarSystemBody",
    "BaseStarMapBorderActor",
    "StarMapBorderActor",
    "Faction",
    "Employer",
    "Lyran",
    "Steiner",
    "Clan",
    "InnerSphere",
    "SystemFaction",
    "Bounds",
    "Camera",
    "Zoom",
    "MWClusterDataAsset",
    "PlaceClusterTOI",
    "EUW_MigratePlaceCluster",
    "OverridePath",
]


def strings_from_payload(payload: bytes) -> list[str]:
    found: set[str] = set()
    for match in ASCII_RE.finditer(payload):
        found.add(match.group(0).decode("utf-8", "replace"))
    for match in UTF16_RE.finditer(payload):
        found.add(match.group(0).decode("utf-16-le", "replace").rstrip("\x00"))
    return sorted(found, key=str.lower)


def classify(strings: list[str]) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for token in IMPORTANT_TOKENS:
        hits = [s for s in strings if token.lower() in s.lower()]
        if hits:
            out[token] = hits[:200]
    return out


def markdown(report: dict) -> str:
    lines = [
        "# Vanilla Editor Asset String Reference Scan",
        "",
        "This scans loose assets from the MW5 Mod Editor install. It is useful for package/reference comparison against cooked TKU assets.",
        "",
        f"- Editor root: `{report['editor_root']}`",
        "",
    ]
    for asset in report["assets"]:
        lines.append(f"### `{asset['base_path']}`")
        lines.append("")
        lines.append(f"- existing_files: {', '.join(asset['existing_files']) if asset['existing_files'] else 'none'}")
        lines.append(f"- missing_files: {', '.join(asset['missing_files']) if asset['missing_files'] else 'none'}")
        lines.append(f"- string_count: {asset['string_count']}")
        lines.append("- notable tokens: " + (", ".join(sorted(asset["important"].keys())) if asset["important"] else "none"))
        for key in ("/Game/", "/ModOverride/", "/Plugins/", "StarMapActor", "StarMapPawn", "StarSystemBody", "BaseStarMapBorderActor", "Lyran", "Steiner", "Clan", "Bounds", "Camera", "Zoom", "MWClusterDataAsset", "PlaceClusterTOI", "EUW_MigratePlaceCluster", "OverridePath"):
            values = asset["important"].get(key, [])
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
    parser.add_argument("--editor-root", type=Path, default=Path(r"E:\Games\MechWarrior5Editor"))
    parser.add_argument("--out-dir", type=Path, default=REPORTS_DIR / "tku_editor_first")
    args = parser.parse_args()

    assets = []
    token_counts: Counter[str] = Counter()
    for base_path, rels in TARGETS.items():
        strings: list[str] = []
        existing: list[str] = []
        missing: list[str] = []
        for rel in rels:
            path = args.editor_root / rel
            if path.exists():
                existing.append(str(path))
                strings.extend(strings_from_payload(path.read_bytes()))
            else:
                missing.append(str(path))
        strings = sorted(set(strings), key=str.lower)
        important = classify(strings)
        for token in important:
            token_counts[token] += 1
        assets.append(
            {
                "base_path": base_path,
                "existing_files": existing,
                "missing_files": missing,
                "string_count": len(strings),
                "important": important,
            }
        )

    report = {
        "editor_root": str(args.editor_root),
        "assets": assets,
        "token_counts": dict(sorted(token_counts.items())),
    }
    args.out_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.out_dir / "vanilla_editor_asset_string_scan.json"
    md_path = args.out_dir / "vanilla_editor_asset_string_scan.md"
    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    md_path.write_text(markdown(report), encoding="utf-8")
    print(json_path)
    print(md_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
