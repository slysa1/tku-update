from __future__ import annotations

import argparse
import json
from pathlib import Path

from mw5_pak import build_pak, extract_exact_paths, gather_sidecar_paths, iter_entries
from tku_compat_config import (
    PATCH_BUILD_NUMBER,
    PATCH_DISPLAY_NAME,
    PATCH_GAME_VERSION,
    PATCH_LOAD_ORDER,
    PATCH_NAME,
    PATCH_VERSION,
    patch_description,
    tier_bases,
)

from tku_project_paths import GAME_ROOT as WORKSPACE_ROOT, REPORTS_DIR

GAME_PAK = WORKSPACE_ROOT / "MW5Mercs" / "Content" / "Paks" / "MW5Mercs-WindowsNoEditor.pak"
TKU_PAK = WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "TheKnownUniverse" / "Paks" / "TheKnownUniverse.pak"
OVERRIDE_PAK = WORKSPACE_ROOT / "MW5Mercs" / "Content" / "Paks" / "MW5Mercs-zKnownUniverseStarmap.pak"
CONTENT_PATCH_PAK = WORKSPACE_ROOT / "MW5Mercs" / "Content" / "Paks" / "MW5Mercs-zzzKnownUniverseCompatPatch.pak"

PATCH_ROOT = WORKSPACE_ROOT / "MW5Mercs" / "Mods" / PATCH_NAME
PATCH_PAK = PATCH_ROOT / "Paks" / f"{PATCH_NAME}.pak"
PATCH_MOD_JSON = PATCH_ROOT / "mod.json"
PATCH_RESOURCES = PATCH_ROOT / "Resources"
PATCH_STAGING_ROOT = PATCH_ROOT / "Staging"

def group_base_map(entries):
    grouped = {}
    for entry in entries:
        grouped.setdefault(entry.base_game_path, []).append(entry)
    return grouped


def staging_content_root(max_tier: str) -> Path:
    return PATCH_STAGING_ROOT / f"Tier{max_tier}" / "MW5Mercs" / "Content"


def unique_staging_content_root(max_tier: str) -> Path:
    base_root = staging_content_root(max_tier)
    if not base_root.exists():
        return base_root
    counter = 2
    while True:
        candidate = PATCH_STAGING_ROOT / f"Tier{max_tier}_{counter}" / "MW5Mercs" / "Content"
        if not candidate.exists():
            return candidate
        counter += 1


def to_staging_path(game_path: str, content_root: Path) -> Path:
    stripped = game_path.removeprefix("/Game/")
    return content_root / Path(stripped.replace("/", "\\"))


def primary_manifest_paths(exact_paths: list[str]) -> list[str]:
    return [path for path in exact_paths if path.endswith(".uasset") or path.endswith(".umap")]


def all_vanilla_root_bases(base_paths: list[str], game_entries) -> list[str]:
    vanilla_bases = {entry.base_game_path for entry in game_entries}
    return [base for base in base_paths if base.startswith("/Game/") and base in vanilla_bases]


def artifact_paths(max_tier: str, full_root_vanilla: bool) -> tuple[Path, Path, Path]:
    if full_root_vanilla:
        report_json = REPORTS_DIR / "tku_compat_patch_vanilla_root_rescue.json"
        report_md = REPORTS_DIR / "tku_compat_patch_vanilla_root_rescue.md"
        resource_manifest = PATCH_RESOURCES / "vanilla-root-rescue-manifest.json"
        return report_json, report_md, resource_manifest
    tier_slug = max_tier.lower()
    report_json = REPORTS_DIR / f"tku_compat_patch_tier_{tier_slug}.json"
    report_md = REPORTS_DIR / f"tku_compat_patch_tier_{tier_slug}.md"
    resource_manifest = PATCH_RESOURCES / f"tier-{tier_slug}-manifest.json"
    return report_json, report_md, resource_manifest


def parse_args():
    parser = argparse.ArgumentParser(description="Build TheKnownUniverse compatibility patch")
    parser.add_argument("--tier", choices=("A", "B", "C"), default="A")
    parser.add_argument("--all-vanilla-root", action="store_true")
    parser.add_argument("--mirror-content-pak", action="store_true")
    return parser.parse_args()


def write_mod_json(manifest_paths: list[str], description: str):
    data = {
        "displayName": PATCH_DISPLAY_NAME,
        "version": PATCH_VERSION,
        "buildNumber": PATCH_BUILD_NUMBER,
        "description": description,
        "author": "codex",
        "authorURL": "",
        "defaultLoadOrder": PATCH_LOAD_ORDER,
        "gameVersion": PATCH_GAME_VERSION,
        "manifest": manifest_paths,
        "steamPublishedFileId": 0,
        "steamLastSubmittedBuildNumber": 0,
        "steamModVisibility": "Private",
    }
    PATCH_MOD_JSON.write_text(json.dumps(data, indent=3) + "\n", encoding="utf-8")


def main():
    args = parse_args()
    max_tier = args.tier
    full_root_vanilla = args.all_vanilla_root
    patch_report_json, patch_report_md, patch_resource_manifest = artifact_paths(max_tier, full_root_vanilla)
    patch_staging = unique_staging_content_root(max_tier)

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    PATCH_RESOURCES.mkdir(parents=True, exist_ok=True)

    _, _, tku_entries = iter_entries(TKU_PAK)
    _, _, override_entries = iter_entries(OVERRIDE_PAK)
    _, _, game_entries = iter_entries(GAME_PAK)

    combined_bases = sorted(set(group_base_map(tku_entries)) | set(group_base_map(override_entries)))
    if full_root_vanilla:
        selected_base_paths = sorted(all_vanilla_root_bases(combined_bases, game_entries))
    else:
        selected_base_paths = tier_bases(combined_bases, max_tier)
    exact_paths = sorted(gather_sidecar_paths(game_entries, set(selected_base_paths)))
    extracted = extract_exact_paths(GAME_PAK, set(exact_paths))

    missing = [path for path in exact_paths if path not in extracted]
    if missing:
        raise RuntimeError(f"missing extracted files: {missing}")

    patch_staging.mkdir(parents=True, exist_ok=True)

    for exact_path in exact_paths:
        out_path = to_staging_path(exact_path, patch_staging)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_bytes(extracted[exact_path])

    loose_files = []
    for exact_path in exact_paths:
        loose_files.append((exact_path, extracted[exact_path]))
    pak_size = build_pak(loose_files, PATCH_PAK)
    content_patch_pak_size = None
    if args.mirror_content_pak:
        content_patch_pak_size = build_pak(loose_files, CONTENT_PATCH_PAK)

    manifest_paths = primary_manifest_paths(exact_paths)
    write_mod_json(manifest_paths, patch_description(max_tier, full_root_vanilla=full_root_vanilla))

    report = {
        "patch_name": PATCH_NAME,
        "patch_root": str(PATCH_ROOT),
        "patch_pak": str(PATCH_PAK),
        "patch_pak_size": pak_size,
        "content_patch_pak": str(CONTENT_PATCH_PAK) if args.mirror_content_pak else None,
        "content_patch_pak_size": content_patch_pak_size,
        "staging_root": str(patch_staging),
        "tier": max_tier,
        "selection_mode": "all_vanilla_root" if full_root_vanilla else "tiered",
        "selected_base_paths": selected_base_paths,
        "exact_paths": exact_paths,
        "manifest_paths": manifest_paths,
        "load_order": PATCH_LOAD_ORDER,
        "game_version": PATCH_GAME_VERSION,
    }
    patch_report_json.write_text(json.dumps(report, indent=2), encoding="utf-8")
    patch_resource_manifest.write_text(json.dumps(report, indent=2), encoding="utf-8")

    lines = [
        "# TKU Compat Patch Vanilla-Root Rescue" if full_root_vanilla else f"# TKU Compat Patch Tier {max_tier}",
        "",
        f"- Patch root: `{PATCH_ROOT}`",
        f"- Patch pak: `{PATCH_PAK}`",
        f"- Pak size: `{pak_size}` bytes",
        f"- Content mirror pak: `{CONTENT_PATCH_PAK}`" if args.mirror_content_pak else "- Content mirror pak: `(not built)`",
        f"- Content mirror size: `{content_patch_pak_size}` bytes" if args.mirror_content_pak else "",
        f"- Load order: `{PATCH_LOAD_ORDER}`",
        f"- Selection mode: `{'all_vanilla_root' if full_root_vanilla else 'tiered'}`",
        f"- Selected base paths: `{len(selected_base_paths)}`",
        "",
        "## Base Paths",
        "",
    ]
    for base in selected_base_paths:
        lines.append(f"- `{base}`")
    lines.extend(["", "## Exact Files", ""])
    for path in exact_paths:
        lines.append(f"- `{path}`")
    patch_report_md.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {PATCH_MOD_JSON}")
    print(f"Wrote {PATCH_PAK}")
    print(f"Wrote {patch_report_json}")
    print(f"Wrote {patch_report_md}")


if __name__ == "__main__":
    main()
