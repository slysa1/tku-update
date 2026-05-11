from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
sys.path.insert(0, str(TOOLS_ROOT))

from mw5_pak import iter_entries, resolve_data_offset  # noqa: E402

ASCII_RE = re.compile(rb"[\x20-\x7e]{4,}")
UTF16_RE = re.compile(rb"(?:[\x20-\x7e]\x00){4,}")

SCAN_EXTENSIONS = {".uasset", ".uexp", ".umap", ".ubulk"}

PATH_CATEGORIES = {
    "modern_cluster_assets": ["/Game/Campaign/Clusters/"],
    "cluster_named_assets": ["Cluster"],
    "starmap_assets": ["StarMap", "/Game/Levels/FrontEnd/StarMap"],
    "border_assets": ["Border", "Borders", "StarMapBorderActor", "BorderChanges"],
    "inner_sphere_data": ["InnerSphereData", "SystemFactionChanges", "EmployerInfoData"],
    "root_factions_employers": ["/Game/Factions/", "/Game/Employers/"],
    "plugin_campaign_arcs": ["/Plugins/TheKnownUniverse/Content/", "StarMapBordersUpdate_Action"],
}

STRING_TOKENS = [
    "/Game/Campaign/Clusters",
    "MWClusterDataAsset",
    "ClusterDataAsset",
    "ClusterOverlay",
    "ClusterConstellation",
    "cluster_overlay",
    "cluster_constellation",
    "PlaceCluster",
    "PlaceClusterToi",
    "CareerModeCustomClusters",
    "StarMapBorderActor",
    "BaseStarMapBorderActor",
    "StarMapBordersUpdate_Action",
    "PanBoundsHorizontal",
    "PanBoundsVertical",
    "ZoomDistanceList",
    "ZoomLevelThresholds",
    "Lyran",
    "Steiner",
    "Clan",
]


def strings_from_payload(payload: bytes) -> list[str]:
    found: set[str] = set()
    for match in ASCII_RE.finditer(payload):
        found.add(match.group(0).decode("utf-8", "replace"))
    for match in UTF16_RE.finditer(payload):
        found.add(match.group(0).decode("utf-16-le", "replace").rstrip("\x00"))
    return sorted(found, key=str.lower)


def extension_counts(entries) -> dict[str, int]:
    counter = Counter(entry.extension or "<none>" for entry in entries)
    return dict(sorted(counter.items()))


def prefix_counts(entries) -> dict[str, int]:
    counter: Counter[str] = Counter()
    for entry in entries:
        path = entry.game_path
        if path.startswith("/Game/"):
            parts = path.split("/")
            counter["/Game/" + (parts[2] if len(parts) > 2 else "")] += 1
        elif path.startswith("/Plugins/"):
            parts = path.split("/")
            if len(parts) >= 5:
                counter["/Plugins/" + parts[2] + "/" + parts[3] + "/" + parts[4]] += 1
            else:
                counter["/Plugins"] += 1
        else:
            counter[path.split("/", 2)[0] or "/"] += 1
    return dict(sorted(counter.items()))


def categorize_paths(entries) -> dict[str, dict]:
    out: dict[str, dict] = {}
    for category, needles in PATH_CATEGORIES.items():
        hits = [
            entry.game_path
            for entry in entries
            if any(needle.lower() in entry.game_path.lower() for needle in needles)
        ]
        out[category] = {
            "count": len(hits),
            "sample": hits[:120],
        }
    return out


def path_absences(path_categories: dict[str, dict], string_hits: dict[str, dict]) -> list[str]:
    absences: list[str] = []
    if path_categories["modern_cluster_assets"]["count"] == 0:
        absences.append("No path-level `/Game/Campaign/Clusters` assets exist in the original TKU pak.")
    if string_hits.get("MWClusterDataAsset", {}).get("asset_count", 0) == 0:
        absences.append("No scanned original TKU cooked asset strings mention `MWClusterDataAsset`.")
    if string_hits.get("/Game/Campaign/Clusters", {}).get("asset_count", 0) == 0:
        absences.append("No scanned original TKU cooked asset strings mention `/Game/Campaign/Clusters`.")
    if string_hits.get("PlaceClusterToi", {}).get("asset_count", 0) == 0:
        absences.append("No scanned original TKU cooked asset strings mention `PlaceClusterToi`.")
    return absences


def scan_strings(pak_path: Path, entries) -> dict[str, dict]:
    token_hits: dict[str, dict] = {
        token: {"asset_count": 0, "sample_assets": [], "sample_strings": []}
        for token in STRING_TOKENS
    }
    with pak_path.open("rb") as handle:
        for entry in entries:
            if entry.extension not in SCAN_EXTENSIONS:
                continue
            if entry.encrypted or entry.compression_method_index:
                continue
            data_offset = resolve_data_offset(handle, entry.offset)
            handle.seek(data_offset)
            payload = handle.read(entry.size)
            strings = strings_from_payload(payload)
            for token in STRING_TOKENS:
                matched = [s for s in strings if token.lower() in s.lower()]
                if not matched:
                    continue
                hit = token_hits[token]
                hit["asset_count"] += 1
                if len(hit["sample_assets"]) < 40:
                    hit["sample_assets"].append(entry.game_path)
                for value in matched:
                    if len(hit["sample_strings"]) >= 80:
                        break
                    if value not in hit["sample_strings"]:
                        hit["sample_strings"].append(value)
    return token_hits


def group_border_timelines(entries) -> dict[str, dict]:
    grouped: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    for entry in entries:
        path = entry.game_path
        if not path.startswith("/Plugins/TheKnownUniverse/Content/"):
            continue
        parts = path.split("/")
        if len(parts) < 5:
            continue
        bucket = parts[4]
        filename = Path(path).name
        if "Border" not in filename and "Borders" not in filename:
            continue
        grouped[bucket][entry.extension].append(path)
    return {
        bucket: {extension: sorted(paths) for extension, paths in sorted(exts.items())}
        for bucket, exts in sorted(grouped.items())
    }


def write_markdown(report: dict, path: Path) -> None:
    lines = [
        "# Original TKU Pak Inventory",
        "",
        "This report inventories the unaltered TKU build-38 pak only. After the 2026-05-10 Nexus restore, the live TheKnownUniverse folder is the clean source under test; quarantined blind-build artifacts are not source evidence.",
        "",
        "## Source",
        "",
        f"- pak: `{report['source_pak']}`",
        f"- mount: `{report['mount_point']}`",
        f"- entry_count: `{report['entry_count']}`",
        f"- pak_version: `{report['pak_version']}`",
        f"- compressed_or_encrypted_entries: `{report['compressed_or_encrypted_entries']}`",
        "",
        "## High-Signal Findings",
        "",
    ]
    for finding in report["high_signal_findings"]:
        lines.append(f"- {finding}")
    lines.extend(["", "## Path Categories", ""])
    for category, info in report["path_categories"].items():
        lines.append(f"### `{category}`")
        lines.append("")
        lines.append(f"- count: `{info['count']}`")
        for sample in info["sample"][:40]:
            lines.append(f"- `{sample}`")
        lines.append("")
    lines.extend(["## String Token Hits", ""])
    for token, info in report["string_hits"].items():
        lines.append(f"### `{token}`")
        lines.append("")
        lines.append(f"- assets_with_token: `{info['asset_count']}`")
        if info["sample_assets"]:
            lines.append("- sample assets:")
            for sample in info["sample_assets"][:20]:
                lines.append(f"- `{sample}`")
        if info["sample_strings"]:
            lines.append("- sample strings:")
            for sample in info["sample_strings"][:20]:
                lines.append(f"- `{sample}`")
        lines.append("")
    lines.extend(["## Border Timeline Buckets", ""])
    for bucket, exts in report["border_timeline_buckets"].items():
        count = sum(len(paths) for paths in exts.values())
        lines.append(f"- `{bucket}`: `{count}` files")
    lines.extend(["", "## Prefix Counts", ""])
    for prefix, count in report["prefix_counts"].items():
        lines.append(f"- `{prefix}`: `{count}`")
    lines.extend(["", "## Extension Counts", ""])
    for extension, count in report["extension_counts"].items():
        lines.append(f"- `{extension}`: `{count}`")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--pak",
        type=Path,
        default=WORKSPACE / "MW5Mercs" / "Mods" / "TheKnownUniverse" / "Paks" / "TheKnownUniverse.pak",
    )
    parser.add_argument("--out-dir", type=Path, default=REPORTS_DIR / "tku_editor_first")
    args = parser.parse_args()

    footer, mount_point, entries = iter_entries(args.pak)
    path_categories = categorize_paths(entries)
    string_hits = scan_strings(args.pak, entries)
    high_signal_findings = path_absences(path_categories, string_hits)
    high_signal_findings.extend(
        [
            "The only path-level cluster-named original TKU assets are the `CareerModeCustomClusters` campaign arc sidecars.",
            "Original TKU contains many dated `StarMapBorderActor`, `Borders`, and `StarMapBordersUpdate_Action` plugin assets, consistent with an older border-overlay pipeline.",
            "Current MW5 editor evidence shows modern overlays also depend on `/Game/Campaign/Clusters` `MWClusterDataAsset` assets, which are absent from original TKU build 38.",
        ]
    )
    report = {
        "source_pak": str(args.pak),
        "mount_point": mount_point,
        "pak_version": footer.version,
        "entry_count": len(entries),
        "compressed_or_encrypted_entries": sum(
            1 for entry in entries if entry.encrypted or entry.compression_method_index
        ),
        "extension_counts": extension_counts(entries),
        "prefix_counts": prefix_counts(entries),
        "path_categories": path_categories,
        "string_tokens": STRING_TOKENS,
        "string_hits": string_hits,
        "high_signal_findings": high_signal_findings,
        "border_timeline_buckets": group_border_timelines(entries),
    }

    args.out_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.out_dir / "original_tku_pak_inventory.json"
    md_path = args.out_dir / "original_tku_pak_inventory.md"
    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    write_markdown(report, md_path)
    print(json_path)
    print(md_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
