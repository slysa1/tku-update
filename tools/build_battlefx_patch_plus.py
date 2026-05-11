from __future__ import annotations

import json
import shutil
from pathlib import Path

from mw5_pak import build_pak, extract_exact_paths, gather_sidecar_paths, iter_entries

from tku_project_paths import GAME_ROOT as WORKSPACE_ROOT, REPORTS_DIR

GAME_PAK = WORKSPACE_ROOT / "MW5Mercs" / "Content" / "Paks" / "MW5Mercs-WindowsNoEditor.pak"
PATCH_ROOT = WORKSPACE_ROOT / "MW5Mercs" / "Mods" / "BattleFXPatch"
PATCH_PAK = PATCH_ROOT / "Paks" / "BattleFXPatch.pak"
PATCH_PAK_BAK = PATCH_ROOT / "Paks" / "BattleFXPatch.pak.bak"
PATCH_MOD_JSON = PATCH_ROOT / "mod.json"
PATCH_STAGING = PATCH_ROOT / "Staging_v41" / "MW5Mercs" / "Content"
PATCH_RESOURCES = PATCH_ROOT / "Resources"

REPORT_JSON = REPORTS_DIR / "battlefx_patch_extension_report.json"
REPORT_MD = REPORTS_DIR / "battlefx_patch_extension_report.md"

EXTRA_BASES = [
    "/Game/Objects/Projectiles/Missile/Particles/Missile_Impact_Dirt_PCL",
    "/Game/Objects/_common/Effects/ExplosionsMegaPack/Particles/Volataile/Explosion_Mech_Alt",
]


def to_staging_path(game_path: str) -> Path:
    stripped = game_path.removeprefix("/Game/")
    return PATCH_STAGING / Path(stripped.replace("/", "\\"))


def main():
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    PATCH_RESOURCES.mkdir(parents=True, exist_ok=True)

    _, _, patch_entries = iter_entries(PATCH_PAK)
    _, _, game_entries = iter_entries(GAME_PAK)

    current_exact_paths = sorted(entry.game_path for entry in patch_entries)
    extra_exact_paths = sorted(gather_sidecar_paths(game_entries, set(EXTRA_BASES)))

    patch_payloads = extract_exact_paths(PATCH_PAK, set(current_exact_paths))
    extra_payloads = extract_exact_paths(GAME_PAK, set(extra_exact_paths))

    all_payloads = dict(patch_payloads)
    all_payloads.update(extra_payloads)
    all_exact_paths = sorted(all_payloads)

    PATCH_STAGING.mkdir(parents=True, exist_ok=True)

    for game_path in all_exact_paths:
        out_path = to_staging_path(game_path)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_bytes(all_payloads[game_path])

    if PATCH_PAK.exists():
        shutil.copy2(PATCH_PAK, PATCH_PAK_BAK)

    pak_size = build_pak([(path, all_payloads[path]) for path in all_exact_paths], PATCH_PAK)

    mod_data = json.loads(PATCH_MOD_JSON.read_text(encoding="utf-8"))
    if extra_exact_paths:
        manifest = set(mod_data.get("manifest", []))
        if any(path.endswith("Missile_Impact_Dirt_PCL.uasset") for path in extra_exact_paths):
            manifest.add("/Game/Objects/Projectiles/Missile/Particles/Missile_Impact_Dirt_PCL.uasset")
        if any(path.endswith("Explosion_Mech_Alt.uasset") for path in extra_exact_paths):
            manifest.add("/Game/Objects/_common/Effects/ExplosionsMegaPack/Particles/Volataile/Explosion_Mech_Alt.uasset")
        mod_data["manifest"] = sorted(manifest)
        PATCH_MOD_JSON.write_text(json.dumps(mod_data, indent=3) + "\n", encoding="utf-8")

    report = {
        "patch_pak": str(PATCH_PAK),
        "patch_pak_size": pak_size,
        "added_base_paths": EXTRA_BASES,
        "added_exact_paths": extra_exact_paths,
        "status": "extended" if extra_exact_paths else "no_exact_vanilla_sources_found",
        "total_exact_paths": len(all_exact_paths),
        "version": mod_data["version"],
        "buildNumber": mod_data["buildNumber"],
    }
    REPORT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")

    lines = [
        "# BattleFXPatch Extension Report",
        "",
        f"- Patch pak: `{PATCH_PAK}`",
        f"- Current version: `{mod_data['version']}` build `{mod_data['buildNumber']}`",
        f"- Status: `{report['status']}`",
        f"- Total exact files packed: `{len(all_exact_paths)}`",
        f"- Pak size: `{pak_size}` bytes",
        "",
        "## Added Base Paths",
        "",
    ]
    for base in EXTRA_BASES:
        lines.append(f"- `{base}`")
    lines.extend(["", "## Added Exact Files", ""])
    for path in extra_exact_paths:
        lines.append(f"- `{path}`")
    if not extra_exact_paths:
        lines.extend(
            [
                "",
                "No exact modern vanilla files were found for those two BattleFX-only paths in `MW5Mercs-WindowsNoEditor.pak`.",
                "The compatibility patch therefore remains a 45-base-asset override, and these two paths stay unresolved.",
            ]
        )
    REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {PATCH_PAK}")
    print(f"Wrote {PATCH_MOD_JSON}")
    print(f"Wrote {REPORT_JSON}")
    print(f"Wrote {REPORT_MD}")


if __name__ == "__main__":
    main()
