from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from mw5_pak import SIDECAREXT, iter_entries
from tku_compat_config import classify_path, tier_a_bases

from tku_project_paths import GAME_ROOT as WORKSPACE_ROOT, REPORTS_DIR

GAME_PAK = WORKSPACE_ROOT / "MW5Mercs" / "Content" / "Paks" / "MW5Mercs-WindowsNoEditor.pak"
TKU_PAK = WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "TheKnownUniverse" / "Paks" / "TheKnownUniverse.pak"
OVERRIDE_PAK = WORKSPACE_ROOT / "MW5Mercs" / "Content" / "Paks" / "MW5Mercs-zKnownUniverseStarmap.pak"
TKU_MOD_JSON = WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "TheKnownUniverse" / "mod.json"

SUMMARY_JSON = REPORTS_DIR / "tku_compat_inventory_summary.json"
MATRIX_JSON = REPORTS_DIR / "tku_compat_asset_matrix.json"
SUMMARY_MD = REPORTS_DIR / "tku_compat_inventory_summary.md"


def base_map(entries):
    grouped = defaultdict(list)
    for entry in entries:
        if entry.extension not in SIDECAREXT:
            continue
        grouped[entry.base_game_path].append(entry.extension)
    return {base: sorted(set(exts)) for base, exts in grouped.items()}


def pak_summary(label: str, pak_path: Path):
    footer, mount_point, entries = iter_entries(pak_path)
    return {
        "label": label,
        "path": str(pak_path),
        "mount_point": mount_point,
        "version": footer.version,
        "file_count": len(entries),
        "game_entry_count": sum(1 for item in entries if item.game_path.startswith("/Game/")),
        "plugin_entry_count": sum(1 for item in entries if item.game_path.startswith("/Plugins/")),
        "entries": entries,
    }


def load_manifest_bases():
    data = json.loads(TKU_MOD_JSON.read_text(encoding="utf-8"))
    bases = []
    for path in data["manifest"]:
        if path.endswith(".uasset"):
            bases.append(path[:-7])
        elif path.endswith(".umap"):
            bases.append(path[:-5])
        else:
            bases.append(path)
    return sorted(set(bases))


def format_list(values):
    if not values:
        return "-"
    return ", ".join(values)


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    game = pak_summary("game", GAME_PAK)
    tku = pak_summary("tku_mod", TKU_PAK)
    override = pak_summary("tku_override", OVERRIDE_PAK)

    manifest_bases = set(load_manifest_bases())
    game_bases = base_map(game["entries"])
    tku_bases = base_map(tku["entries"])
    override_bases = base_map(override["entries"])

    all_bases = sorted(set(tku_bases) | set(override_bases))
    matrix = []
    for base in all_bases:
        domain, patch_tier, proposed_action = classify_path(base)
        entry = {
            "base_path": base,
            "domain": domain,
            "patch_tier": patch_tier,
            "proposed_action": proposed_action,
            "in_tku_manifest": base in manifest_bases,
            "tku_extensions": tku_bases.get(base, []),
            "override_extensions": override_bases.get(base, []),
            "vanilla_extensions": game_bases.get(base, []),
            "has_vanilla_match": base in game_bases,
            "source_paks": [
                label
                for label, mapping in (
                    ("tku_mod", tku_bases),
                    ("tku_override", override_bases),
                    ("game", game_bases),
                )
                if base in mapping
            ],
        }
        matrix.append(entry)

    tier_counter = Counter(item["patch_tier"] for item in matrix)
    domain_counter = Counter(item["domain"] for item in matrix)
    tier_a = tier_a_bases([item["base_path"] for item in matrix])
    tier_a_missing_vanilla = [item["base_path"] for item in matrix if item["patch_tier"] == "A" and not item["has_vanilla_match"]]

    summary_json = {
        "pak_summaries": [
            {key: value for key, value in game.items() if key != "entries"},
            {key: value for key, value in tku.items() if key != "entries"},
            {key: value for key, value in override.items() if key != "entries"},
        ],
        "manifest_count": len(manifest_bases),
        "matrix_count": len(matrix),
        "tier_counts": dict(sorted(tier_counter.items())),
        "domain_counts": dict(sorted(domain_counter.items())),
        "tier_a_base_paths": tier_a,
        "tier_a_missing_vanilla": tier_a_missing_vanilla,
    }

    SUMMARY_JSON.write_text(json.dumps(summary_json, indent=2), encoding="utf-8")
    MATRIX_JSON.write_text(json.dumps(matrix, indent=2), encoding="utf-8")

    lines = [
        "# TKU Compatibility Inventory Summary",
        "",
        "## Pak Summary",
        "",
        "| Pak | Files | /Game | /Plugins | Mount |",
        "| --- | ---: | ---: | ---: | --- |",
    ]
    for item in summary_json["pak_summaries"]:
        lines.append(
            f"| {item['label']} | {item['file_count']} | {item['game_entry_count']} | "
            f"{item['plugin_entry_count']} | `{item['mount_point']}` |"
        )

    lines.extend(
        [
            "",
            "## Tier Counts",
            "",
            "| Tier | Base Paths |",
            "| --- | ---: |",
        ]
    )
    for tier, count in sorted(summary_json["tier_counts"].items()):
        lines.append(f"| {tier} | {count} |")

    lines.extend(
        [
            "",
            "## Domain Counts",
            "",
            "| Domain | Base Paths |",
            "| --- | ---: |",
        ]
    )
    for domain, count in sorted(summary_json["domain_counts"].items()):
        lines.append(f"| {domain} | {count} |")

    lines.extend(
        [
            "",
            "## Tier A Targets",
            "",
            "| Base Path | TKU | Override | Vanilla |",
            "| --- | --- | --- | --- |",
        ]
    )
    for item in matrix:
        if item["patch_tier"] != "A":
            continue
        lines.append(
            f"| `{item['base_path']}` | {format_list(item['tku_extensions'])} | "
            f"{format_list(item['override_extensions'])} | {format_list(item['vanilla_extensions'])} |"
        )

    if tier_a_missing_vanilla:
        lines.extend(["", "## Missing Vanilla Matches", ""])
        for base in tier_a_missing_vanilla:
            lines.append(f"- `{base}`")

    SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {SUMMARY_JSON}")
    print(f"Wrote {MATRIX_JSON}")
    print(f"Wrote {SUMMARY_MD}")


if __name__ == "__main__":
    main()
