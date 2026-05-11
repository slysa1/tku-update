from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path


from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
EDITOR_ROOT = Path(r"E:\Games\MechWarrior5Editor")
EDITOR_PROJECT = EDITOR_ROOT / "MW5Mercs"
OUT_DIR = REPORTS_DIR / "tku_editor_first"
OUT_JSON = OUT_DIR / "editor_mod_target_status_20260510.json"
OUT_MD = OUT_DIR / "editor_mod_target_status_20260510.md"


def list_dir(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        return []
    items: list[dict[str, object]] = []
    for child in sorted(path.iterdir(), key=lambda item: item.name.lower()):
        items.append(
            {
                "name": child.name,
                "path": str(child),
                "is_dir": child.is_dir(),
                "size": child.stat().st_size if child.is_file() else None,
                "mtime": datetime.fromtimestamp(child.stat().st_mtime, timezone.utc).isoformat(),
            }
        )
    return items


def find_files(root: Path, patterns: tuple[str, ...]) -> list[str]:
    if not root.exists():
        return []
    found: list[str] = []
    for pattern in patterns:
        found.extend(str(path) for path in root.rglob(pattern))
    return sorted(set(found), key=str.lower)


def main() -> None:
    mods_dir = EDITOR_PROJECT / "Mods"
    plugins_dir = EDITOR_PROJECT / "Plugins"
    mod_targets = [
        path
        for path in find_files(EDITOR_PROJECT, ("*.uplugin", "*.mod", "mod.json", "modinfo.json"))
        if any(token in path.lower() for token in ("tku", "known", "compat", "evidence", "theknownuniverse"))
    ]
    data = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "non_mutating": True,
        "editor_root": str(EDITOR_ROOT),
        "editor_project": str(EDITOR_PROJECT),
        "mods_dir": {
            "path": str(mods_dir),
            "exists": mods_dir.exists(),
            "items": list_dir(mods_dir),
        },
        "plugins_dir": {
            "path": str(plugins_dir),
            "exists": plugins_dir.exists(),
            "items": list_dir(plugins_dir),
        },
        "candidate_tku_related_mod_targets": mod_targets,
        "decision": {
            "existing_editor_compat_mod_found": bool(mod_targets),
            "manual_create_mod_required": not bool(mod_targets),
            "build_authorized": False,
            "reason": "No dedicated TKU compatibility mod target exists in the MW5 Mod Editor project.",
        },
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")

    lines = [
        "# Editor Mod Target Status - 2026-05-10",
        "",
        f"- Generated: `{data['generated_utc']}`",
        "- Method: local filesystem inspection only.",
        "- Safety: no editor files, game files, or paks were modified.",
        "",
        "## Findings",
        "",
        f"- Editor project: `{EDITOR_PROJECT}`",
        f"- Mods directory exists: `{mods_dir.exists()}`",
        f"- Mods directory items: `{[item['name'] for item in data['mods_dir']['items']]}`",
        f"- Project plugin items: `{[item['name'] for item in data['plugins_dir']['items']]}`",
        f"- TKU/compat candidate mod targets: `{mod_targets}`",
        "",
        "## Decision",
        "",
        f"- Existing editor compatibility mod found: `{data['decision']['existing_editor_compat_mod_found']}`",
        f"- Manual Create Mod required: `{data['decision']['manual_create_mod_required']}`",
        f"- Build authorized: `{data['decision']['build_authorized']}`",
        f"- Reason: {data['decision']['reason']}",
        "",
        "Next gate: create the dedicated compatibility mod through the MW5 Mod Editor UI, then save copied/current-compatible assets to that mod before any package/build attempt.",
        "",
    ]
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")


if __name__ == "__main__":
    main()
