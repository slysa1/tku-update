from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
EDITOR_ROOT = Path(r"E:\Games\MechWarrior5Editor")
DATA_ROOT = EDITOR_ROOT / "MW5Mercs" / "Content" / "Data" / "InnerSphereMap"
RUNTIME_ROOT = EDITOR_ROOT / "MW5Mercs" / "Content" / "InnerSphereData"
OUT_DIR = REPORTS_DIR / "tku_editor_first"

sys.path.insert(0, str(TOOLS_ROOT))
sys.path.insert(0, str(TOOLS_ROOT / "tku_reference_audit"))

from extract_asset_strings import strings_from_payload  # noqa: E402
from mw5_pak import extract_exact_paths  # noqa: E402


def parse_csv(path: Path, encoding: str) -> list[dict[str, str]]:
    with path.open("r", encoding=encoding, newline="") as handle:
        return list(csv.DictReader(handle))


def cluster_id_from_csv(value: str) -> str:
    if not value or value in {"None", "(Id=\"\")"}:
        return ""
    marker = "MWFactionAsset:"
    if marker not in value:
        return value
    return value.split(marker, 1)[1].split('"', 1)[0].split(")", 1)[0]


def path_asset_name(path_or_object: object) -> str:
    text = str(path_or_object or "")
    match = re.search(r"'([^']+)'", text)
    if match:
        text = match.group(1)
    if "." in text:
        return text.rsplit(".", 1)[1]
    return Path(text).name


def load_editor_cluster_assets() -> list[dict]:
    dump_path = OUT_DIR / "ue4_editor_asset_dump.json"
    if not dump_path.exists():
        return []
    dump = json.loads(dump_path.read_text(encoding="utf-8"))
    assets = []
    for asset in dump.get("assets", []):
        if not asset.get("asset_path", "").startswith("/Game/Campaign/Clusters/"):
            continue
        if asset.get("asset_data", {}).get("asset_class") != "MWClusterDataAsset":
            continue
        props = asset.get("known_properties", {})
        system_ids = props.get("system_ids", [])
        assets.append(
            {
                "asset_path": asset["asset_path"],
                "system_count": len(system_ids) if isinstance(system_ids, list) else 0,
                "cluster_faction_asset": str(props.get("cluster_faction_asset") or ""),
                "cluster_faction_name": path_asset_name(props.get("cluster_faction_asset")),
                "cluster_overlay": str(props.get("cluster_overlay") or ""),
                "cluster_constellation": str(props.get("cluster_constellation") or ""),
            }
        )
    return sorted(assets, key=lambda item: item["asset_path"].lower())


def load_original_tku_inner_sphere_strings() -> list[str]:
    pak = WORKSPACE / "MW5Mercs" / "Mods" / "TheKnownUniverse" / "Paks" / "TheKnownUniverse.pak"
    paths = {
        "/Game/InnerSphereData/MW5_InnerSphereData.uasset",
        "/Game/InnerSphereData/MW5_InnerSphereData.uexp",
    }
    extracted = extract_exact_paths(pak, paths)
    strings: set[str] = set()
    for path in paths:
        payload = extracted.get(path, b"")
        strings.update(strings_from_payload(payload))
    return sorted(strings, key=str.lower)


def load_current_place_cluster_actions() -> list[dict]:
    regions_root = EDITOR_ROOT / "MW5Mercs" / "Content" / "Campaign" / "CampaignArcs" / "Regions"
    actions = []
    if not regions_root.exists():
        return actions
    for path in sorted(regions_root.rglob("Place*.uasset")):
        strings = strings_from_payload(path.read_bytes())
        cluster_refs = sorted(
            value
            for value in strings
            if value.startswith("/Game/Campaign/Clusters/")
            or "MWClusterDataAsset" in value
            or "ClusterDataAsset" in value
        )
        if not cluster_refs:
            continue
        rel = path.relative_to(EDITOR_ROOT).as_posix()
        game_path = "/" + rel
        game_path = game_path.replace("/MW5Mercs/Content/", "/Game/")
        if game_path.endswith(".uasset"):
            game_path = game_path[:-7]
        actions.append(
            {
                "asset_path": game_path,
                "file": str(path),
                "cluster_ref_count": len(cluster_refs),
                "cluster_refs": cluster_refs[:40],
                "cluster_name_strings": [
                    value for value in strings if "ClusterName" in value or "ClusterDescription" in value
                ][:20],
            }
        )
    return actions


def summarize_current_csv(rows: list[dict[str, str]]) -> dict:
    cluster_counts = Counter(cluster_id_from_csv(row.get("Cluster", "")) for row in rows)
    overlay_values = [row.get("ClusterOverlay", "") for row in rows if row.get("ClusterOverlay") not in {"", "None", None}]
    constellation_values = [
        row.get("ClusterConstellation", "")
        for row in rows
        if row.get("ClusterConstellation") not in {"", "None", None}
    ]
    nonempty_cluster_counts = Counter({key: value for key, value in cluster_counts.items() if key})
    return {
        "row_count": len(rows),
        "cluster_rows": sum(cluster_counts.values()),
        "nonempty_cluster_rows": sum(nonempty_cluster_counts.values()),
        "unique_nonempty_cluster_ids": len(nonempty_cluster_counts),
        "top_cluster_ids": dict(nonempty_cluster_counts.most_common(30)),
        "overlay_rows": len(overlay_values),
        "unique_overlay_values": len(set(overlay_values)),
        "constellation_rows": len(constellation_values),
        "unique_constellation_values": len(set(constellation_values)),
        "sample_overlay_values": sorted(set(overlay_values))[:30],
        "sample_constellation_values": sorted(set(constellation_values))[:30],
        "cluster_ids": sorted(nonempty_cluster_counts),
    }


def summarize_wide_json(rows: list[dict]) -> dict:
    keys = ("Cluster", "ClusterOverlay", "ClusterConstellation")
    counts = {}
    samples = {}
    for key in keys:
        values = [row.get(key) for row in rows if row.get(key) not in ("", "None", None)]
        counts[key] = {"rows": len(values), "unique_values": len({json.dumps(value, sort_keys=True) for value in values})}
        samples[key] = values[:20]
    return {
        "row_count": len(rows),
        "cluster_field_counts": counts,
        "cluster_field_samples": samples,
    }


def summarize_original_strings(strings: list[str], current_cluster_ids: list[str]) -> dict:
    paths = [value for value in strings if value.startswith("/Game/") or value.startswith("/ModOverride/")]
    interesting_terms = [
        "ClusterOverlay",
        "ClusterConstellation",
        "MWFactionAsset",
        "FactionBorderMeshes",
        "Regions/",
        "CustomContent/Zones_Clan",
        "Lyran",
        "Steiner",
        "Clan",
        "Taurian",
        "Outworlds",
        "Canopus",
    ]
    term_hits = {
        term: [value for value in strings if term.lower() in value.lower()][:80]
        for term in interesting_terms
    }
    current_ids_found = [
        cluster_id
        for cluster_id in current_cluster_ids
        if any(cluster_id.lower() in value.lower() for value in strings)
    ]
    return {
        "string_count": len(strings),
        "asset_path_string_count": len(paths),
        "sample_asset_paths": paths[:120],
        "current_cluster_ids_found_count": len(current_ids_found),
        "current_cluster_ids_found": current_ids_found,
        "term_hit_counts": {term: len(values) for term, values in term_hits.items()},
        "term_hit_samples": term_hits,
    }


def write_markdown(report: dict, path: Path) -> None:
    current = report["current_runtime_csv"]
    editor_assets = report["editor_cluster_assets"]
    place_actions = report["current_place_cluster_actions"]
    comparison = report["csv_vs_editor_cluster_assets"]
    original = report["original_tku_cooked_inner_sphere_strings"]
    wide = report["wide_source_json"]

    lines = [
        "# Cluster Migration Inputs",
        "",
        "This report compares the current editor cluster pipeline against the original unaltered TKU cooked InnerSphere table. It does not modify the editor, game, or original TKU backup.",
        "",
        "## Current Editor Runtime CSV",
        "",
        f"- rows: `{current['row_count']}`",
        f"- nonempty cluster rows: `{current['nonempty_cluster_rows']}`",
        f"- unique nonempty cluster ids: `{current['unique_nonempty_cluster_ids']}`",
        f"- cluster overlay rows: `{current['overlay_rows']}`",
        f"- cluster constellation rows: `{current['constellation_rows']}`",
        "",
        "Top cluster ids:",
    ]
    for key, value in current["top_cluster_ids"].items():
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(
        [
            "",
            "## Current Editor Cluster Assets",
            "",
            f"- `MWClusterDataAsset` count: `{len(editor_assets)}`",
            f"- total system id memberships: `{sum(item['system_count'] for item in editor_assets)}`",
            f"- CSV cluster ids missing matching editor cluster faction names: `{len(comparison['csv_ids_missing_editor_faction_asset'])}`",
            f"- editor cluster faction names not found in CSV ids: `{len(comparison['editor_faction_assets_missing_csv_id'])}`",
            "",
        ]
    )
    for item in editor_assets[:40]:
        lines.append(
            f"- `{item['asset_path']}` systems `{item['system_count']}` faction `{item['cluster_faction_name']}`"
        )
    lines.extend(
        [
            "",
            "## Current Place Cluster Actions",
            "",
            f"- place assets with cluster refs: `{len(place_actions)}`",
            "",
        ]
    )
    for item in place_actions[:50]:
        refs = ", ".join(f"`{ref}`" for ref in item["cluster_refs"][:3])
        lines.append(f"- `{item['asset_path']}` refs {refs}")
    lines.extend(
        [
            "",
            "## Wide Source JSON",
            "",
            f"- rows: `{wide['row_count']}`",
        ]
    )
    for key, value in wide["cluster_field_counts"].items():
        lines.append(f"- `{key}` rows `{value['rows']}`, unique `{value['unique_values']}`")
    lines.extend(
        [
            "",
            "## Original TKU Cooked InnerSphere Strings",
            "",
            f"- string_count: `{original['string_count']}`",
            f"- asset path strings: `{original['asset_path_string_count']}`",
            f"- current editor cluster ids found in original cooked strings: `{original['current_cluster_ids_found_count']}`",
            "",
            "Original term hit counts:",
        ]
    )
    for key, value in original["term_hit_counts"].items():
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "Current cluster ids found in original TKU strings:"])
    for value in original["current_cluster_ids_found"][:100]:
        lines.append(f"- `{value}`")
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "- Current MW5 converts old `Cluster`, `ClusterOverlay`, and `ClusterConstellation` table fields into explicit `MWClusterDataAsset` assets.",
            "- Original TKU build 38 does not contain modern cluster assets, but its cooked InnerSphere table still exposes old cluster field names, faction-like cluster IDs, and overlay mesh paths as strings.",
            "- Terminal string extraction is not enough to reconstruct row-to-cluster mappings safely; the next evidence step is editor/tool inspection of the migration utility and a structured export path for original TKU `MW5_InnerSphereData`.",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    runtime_csv = parse_csv(RUNTIME_ROOT / "MW5_InnerSphereData.csv", "utf-16")
    wide_json = json.loads((DATA_ROOT / "MW5_InnerSphereData.json").read_text(encoding="utf-8-sig"))
    current_summary = summarize_current_csv(runtime_csv)
    editor_cluster_assets = load_editor_cluster_assets()
    place_cluster_actions = load_current_place_cluster_actions()
    editor_faction_names = sorted(
        {item["cluster_faction_name"] for item in editor_cluster_assets if item["cluster_faction_name"]}
    )
    csv_ids = current_summary["cluster_ids"]
    original_strings = load_original_tku_inner_sphere_strings()
    report = {
        "source_files": {
            "current_runtime_csv": str(RUNTIME_ROOT / "MW5_InnerSphereData.csv"),
            "wide_source_json": str(DATA_ROOT / "MW5_InnerSphereData.json"),
            "original_tku_pak": str(WORKSPACE / "MW5Mercs" / "Mods" / "TheKnownUniverse" / "Paks" / "TheKnownUniverse.pak"),
            "editor_asset_dump": str(OUT_DIR / "ue4_editor_asset_dump.json"),
        },
        "current_runtime_csv": current_summary,
        "wide_source_json": summarize_wide_json(wide_json),
        "editor_cluster_assets": editor_cluster_assets,
        "current_place_cluster_actions": place_cluster_actions,
        "csv_vs_editor_cluster_assets": {
            "csv_cluster_ids": csv_ids,
            "editor_cluster_faction_names": editor_faction_names,
            "csv_ids_missing_editor_faction_asset": sorted(set(csv_ids) - set(editor_faction_names)),
            "editor_faction_assets_missing_csv_id": sorted(set(editor_faction_names) - set(csv_ids)),
        },
        "original_tku_cooked_inner_sphere_strings": summarize_original_strings(original_strings, csv_ids),
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    json_path = OUT_DIR / "cluster_migration_inputs.json"
    md_path = OUT_DIR / "cluster_migration_inputs.md"
    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    write_markdown(report, md_path)
    print(json_path)
    print(md_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
