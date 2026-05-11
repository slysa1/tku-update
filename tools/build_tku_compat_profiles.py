from __future__ import annotations

import json
from pathlib import Path

PATCH_ID = "TheKnownUniverseCompatPatch"

from tku_project_paths import GAME_ROOT as WORKSPACE_ROOT, REPORTS_DIR
MODS_ROOT = WORKSPACE_ROOT / "MW5Mercs" / "Mods"

SOURCES = {
    "single": MODS_ROOT / "modlist.profile-single-knownuniverse-20260506.json",
    "named_local": MODS_ROOT / "modlist.profile-named-local-20260506.json",
    "full_stack": MODS_ROOT / "modlist.pre-near-vanilla-backup-20260506.json",
}

OUTPUTS = {
    "single": MODS_ROOT / "modlist.profile-single-knownuniverse-compat-20260506.json",
    "named_local": MODS_ROOT / "modlist.profile-named-local-with-compat-20260506.json",
    "full_stack": MODS_ROOT / "modlist.profile-full-stack-with-tku-compat-20260506.json",
}


def enable_patch(profile_path: Path, output_path: Path):
    data = json.loads(profile_path.read_text(encoding="utf-8"))
    data.setdefault("modStatus", {})
    data["modStatus"].setdefault(PATCH_ID, {})
    data["modStatus"][PATCH_ID]["bEnabled"] = True
    output_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def main():
    for key, source in SOURCES.items():
        enable_patch(source, OUTPUTS[key])
        print(f"Wrote {OUTPUTS[key]}")


if __name__ == "__main__":
    main()
