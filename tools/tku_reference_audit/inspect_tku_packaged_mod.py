from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPORT_STEM = "tku_packaged_mod_inspection_20260511"
DEFAULT_MOD_NAME = "TKUCompatEditorPatch"
EXPECTED_PAK_FRAGMENTS = [
    "Content/InnerSphereData/MW5_InnerSphereData.uasset",
    "Content/InnerSphereData/MW5_InnerSphereData.uexp",
    "Content/InnerSphereData/StarSystemGenerator.uasset",
    "Content/InnerSphereData/StarSystemGenerator.uexp",
    "Content/Levels/FrontEnd/StarMap.umap",
    "Content/Levels/FrontEnd/StarMap.uexp",
    "Content/UI/FrontEnd/StarMapPawn.uasset",
    "Content/UI/FrontEnd/StarMapPawn.uexp",
    "Content/Modes/MW5GameMode.uasset",
    "Content/Modes/MW5GameMode.uexp",
    "Content/Modes/CampaignMode.uasset",
    "Content/Modes/CampaignMode.uexp",
    "Content/Campaign/_common/DefaultSystemGenerator.uasset",
    "Content/Campaign/_common/DefaultSystemGenerator.uexp",
    "Content/DLC1/CareerMode/StartConditions/CareerMode.uasset",
    "Content/DLC1/CareerMode/StartConditions/CareerMode.uexp",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Davion_Start.uasset",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Davion_Start.uexp",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Davion_Start_Tutorial.uasset",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Davion_Start_Tutorial.uexp",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_FRR_Start.uasset",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_FRR_Start.uexp",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_FRR_Start_Tutorial.uasset",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_FRR_Start_Tutorial.uexp",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Kurita_Start.uasset",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Kurita_Start.uexp",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Kurita_Start_Tutorial.uasset",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Kurita_Start_Tutorial.uexp",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Liao_Start.uasset",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Liao_Start.uexp",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Liao_Start_Tutorial.uasset",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Liao_Start_Tutorial.uexp",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Marik_Start.uasset",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Marik_Start.uexp",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Marik_Start_Tutorial.uasset",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Marik_Start_Tutorial.uexp",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Steiner_Start.uasset",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Steiner_Start.uexp",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Steiner_Start_Tutorial.uasset",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Steiner_Start_Tutorial.uexp",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Start.uasset",
    "Content/DLC1/CareerMode/StartConditions/CareerMode_Start.uexp",
    "Content/DLC1/CareerMode/StartConditions/FRR_CareerMode_Start.uasset",
    "Content/DLC1/CareerMode/StartConditions/FRR_CareerMode_Start.uexp",
    "Content/DLC1/CareerMode/CareerModeCoreCampaign.uasset",
    "Content/DLC1/CareerMode/CareerModeCoreCampaign.uexp",
    "Content/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters.uasset",
    "Content/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters.uexp",
    "Content/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones.uasset",
    "Content/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones.uexp",
    "Content/Campaign/Clusters/TKU_ClanConflict/ClanConflict.uasset",
    "Content/Campaign/Clusters/TKU_ClanConflict/TKU_ClanConflict_NoOverlay_ClusterAsset.uasset",
    "Content/Campaign/Clusters/TKU_ClanConflict_Zones_ClanConf_1/TKU_ClanConflict_Zones_ClanConf_1_ClusterAsset.uasset",
    "Content/Campaign/Clusters/TKU_ClanConflict_Zones_ClanConf_2/TKU_ClanConflict_Zones_ClanConf_2_ClusterAsset.uasset",
    "Content/Campaign/Clusters/TKU_ClanConflict_Zones_ClanConf_3/TKU_ClanConflict_Zones_ClanConf_3_ClusterAsset.uasset",
    "Content/Campaign/Clusters/TKU_ClanConflict_Zones_ClanConf_4/TKU_ClanConflict_Zones_ClanConf_4_ClusterAsset.uasset",
    "Content/Campaign/Clusters/TKU_RepairSystem_Clan/RepairSystem_Clan.uasset",
    "Content/Campaign/Clusters/TKU_RepairSystem_Clan/TKU_RepairSystem_Clan_NoOverlay_ClusterAsset.uasset",
    "Content/Campaign/Clusters/TKU_RepairSystem_Clan_Zones_Clan_Safezone_1/TKU_RepairSystem_Clan_Zones_Clan_Safezone_1_ClusterAsset.uasset",
    "Content/Campaign/Clusters/TKU_RepairSystem_Clan_Zones_Clan_Safezone_2/TKU_RepairSystem_Clan_Zones_Clan_Safezone_2_ClusterAsset.uasset",
]
FOCUS_TERMS = [
    "TKUCompatEditorPatch",
    "ModOverride",
    "InnerSphereData",
    "MW5_InnerSphereData",
    "StarSystemGenerator",
    "Levels/FrontEnd/StarMap",
    "Levels\\FrontEnd\\StarMap",
    "UI/FrontEnd/StarMapPawn",
    "UI\\FrontEnd\\StarMapPawn",
    "Modes/MW5GameMode",
    "Modes\\MW5GameMode",
    "Modes/CampaignMode",
    "Modes\\CampaignMode",
    "Campaign/_common/DefaultSystemGenerator",
    "Campaign\\_common\\DefaultSystemGenerator",
    "Campaign/Clusters/TKU_",
    "Campaign\\Clusters\\TKU_",
    "ClanConflict",
    "RepairSystem_Clan",
    "DLC1/CareerMode/StartConditions/CareerMode",
    "DLC1\\CareerMode\\StartConditions\\CareerMode",
    "DLC1/CareerMode/CareerModeCoreCampaign",
    "DLC1\\CareerMode\\CareerModeCoreCampaign",
    "DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters",
    "DLC1\\CareerMode\\StartConditions\\Arcs\\CareerModeClusters",
    "DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones",
    "DLC1\\CareerMode\\StartConditions\\Arcs\\CareerMode_SafeZones",
]


def resolve_project_root() -> Path:
    raw = os.environ.get("TKU_PROJECT_ROOT")
    if raw:
        return Path(raw).resolve()
    return Path(__file__).resolve().parents[2]


PROJECT_ROOT = resolve_project_root()
REPORT_DIR = PROJECT_ROOT / "reports" / "tku_editor_first"
CONFIG_PATHS = [
    Path(os.environ["TKU_PATHS_CONFIG"]) if os.environ.get("TKU_PATHS_CONFIG") else None,
    PROJECT_ROOT / "config" / "tku_paths.local.json",
    PROJECT_ROOT / "config" / "tku_paths.json",
    PROJECT_ROOT / "config" / "tku_paths.example.json",
]


def read_config() -> dict[str, Any]:
    for candidate in CONFIG_PATHS:
        if candidate and candidate.is_file():
            return json.loads(candidate.read_text(encoding="utf-8"))
    return {}


CONFIG = read_config()


def sha256_file(path: Path) -> str | None:
    if not path.is_file():
        return None
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def jsonable(value: Any) -> Any:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(k): jsonable(v) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [jsonable(item) for item in value]
    return str(value)


def default_editor_root() -> Path:
    return Path(os.environ.get("TKU_MW5_EDITOR_ROOT") or CONFIG.get("mw5_editor_root") or r"E:\Games\MechWarrior5Editor")


def default_package_root(editor_root: Path) -> Path:
    return Path(os.environ.get("TKU_PACKAGED_MOD_ROOT") or editor_root / "MW5Mercs" / "Mods")


def default_unrealpak(editor_root: Path) -> Path:
    return Path(os.environ.get("TKU_UNREALPAK") or editor_root / "Engine" / "Binaries" / "Win64" / "UnrealPak.exe")


def discover_mod_dir(package_root: Path, mod_name: str, explicit: str | None) -> tuple[Path, list[str]]:
    notes: list[str] = []
    if explicit:
        return Path(explicit).resolve(), notes

    direct = package_root / mod_name
    if direct.is_dir():
        return direct, notes

    candidates = []
    if package_root.is_dir():
        for child in package_root.iterdir():
            if not child.is_dir():
                continue
            mod_json = child / "mod.json"
            if child.name.lower() == mod_name.lower() or mod_json.is_file():
                candidates.append(child)
    notes.append(f"direct package folder not found: {direct}")
    if len(candidates) == 1:
        notes.append(f"using single candidate under package root: {candidates[0]}")
        return candidates[0], notes
    if candidates:
        notes.append("multiple candidate mod folders found; using name match if possible")
        for candidate in candidates:
            if candidate.name.lower() == mod_name.lower():
                return candidate, notes
    return direct, notes


def load_json(path: Path) -> dict[str, Any] | None:
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except UnicodeDecodeError:
        return json.loads(path.read_text(encoding="utf-16"))


def run_unrealpak_list(unrealpak: Path, pak: Path, list_out: Path) -> dict[str, Any]:
    result: dict[str, Any] = {
        "pak": str(pak),
        "unrealpak": str(unrealpak),
        "attempted": False,
        "returncode": None,
        "list_output": str(list_out),
        "focused_entries": [],
        "expected_fragments_present": {},
    }
    if not unrealpak.is_file():
        result["error"] = f"UnrealPak.exe not found: {unrealpak}"
        return result

    proc = subprocess.run(
        [str(unrealpak), str(pak), "-List"],
        cwd=str(unrealpak.parent),
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=180,
        check=False,
    )
    result["attempted"] = True
    result["returncode"] = proc.returncode
    list_out.write_text(proc.stdout, encoding="utf-8")

    normalized = proc.stdout.replace("\\", "/")
    result["expected_fragments_present"] = {
        fragment: fragment.replace("\\", "/") in normalized for fragment in EXPECTED_PAK_FRAGMENTS
    }
    focused = []
    for line in proc.stdout.splitlines():
        comparable = line.replace("\\", "/").lower()
        if any(term.replace("\\", "/").lower() in comparable for term in FOCUS_TERMS):
            focused.append(line.strip())
    result["focused_entries"] = focused[:200]
    result["focused_entry_count"] = len(focused)
    return result


def inspect_package(mod_dir: Path, mod_name: str, unrealpak: Path) -> dict[str, Any]:
    mod_json_path = mod_dir / "mod.json"
    mod_json = load_json(mod_json_path)
    files = []
    if mod_dir.is_dir():
        for path in sorted(item for item in mod_dir.rglob("*") if item.is_file()):
            files.append(
                {
                    "path": str(path),
                    "relative_path": str(path.relative_to(mod_dir)),
                    "size": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
            )

    paks = [Path(item["path"]) for item in files if str(item["relative_path"]).lower().endswith(".pak")]
    pak_reports = []
    for pak in paks:
        list_out = REPORT_DIR / f"{REPORT_STEM}_{pak.stem}_unrealpak_list.txt"
        pak_reports.append(run_unrealpak_list(unrealpak, pak, list_out))

    safety_failures = []
    if not mod_dir.is_dir():
        safety_failures.append(f"packaged mod folder not found: {mod_dir}")
    if not mod_json_path.is_file():
        safety_failures.append(f"mod.json not found: {mod_json_path}")
    if not paks:
        safety_failures.append("no .pak files found in packaged mod folder")
    if mod_json and str(mod_json.get("name") or mod_json.get("displayName") or mod_json.get("modName") or "").lower() not in {
        "",
        mod_name.lower(),
    }:
        safety_failures.append(f"mod.json name fields do not clearly match {mod_name}: {mod_json}")
    for fragment in EXPECTED_PAK_FRAGMENTS:
        if pak_reports and not any(report.get("expected_fragments_present", {}).get(fragment) for report in pak_reports):
            safety_failures.append(f"expected asset fragment not found in any pak listing: {fragment}")

    return {
        "mod_dir": str(mod_dir),
        "mod_dir_exists": mod_dir.is_dir(),
        "mod_json_path": str(mod_json_path),
        "mod_json": mod_json,
        "file_count": len(files),
        "files": files,
        "pak_count": len(paks),
        "paks": pak_reports,
        "safety_failures": safety_failures,
    }


def write_report(report: dict[str, Any]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    json_path = REPORT_DIR / f"{REPORT_STEM}.json"
    md_path = REPORT_DIR / f"{REPORT_STEM}.md"
    json_path.write_text(json.dumps(report, indent=2, sort_keys=True, default=str), encoding="utf-8")

    package = report["package"]
    lines = [
        "# TKU Packaged Mod Inspection - 2026-05-11",
        "",
        f"- Generated: `{report['generated_utc']}`",
        f"- Mod name: `{report['mod_name']}`",
        f"- Package root: `{report['package_root']}`",
        f"- Mod folder: `{package['mod_dir']}`",
        f"- UnrealPak: `{report['unrealpak']}`",
        "",
        "## Package Summary",
        "",
        f"- Folder exists: `{package['mod_dir_exists']}`",
        f"- File count: `{package['file_count']}`",
        f"- Pak count: `{package['pak_count']}`",
        f"- mod.json path: `{package['mod_json_path']}`",
        f"- mod.json: `{package['mod_json']}`",
        "",
        "## Safety",
        "",
    ]
    if package["safety_failures"]:
        for failure in package["safety_failures"]:
            lines.append(f"- FAIL: {failure}")
    else:
        lines.append("- No package inspection safety failures.")

    lines.extend(["", "## Files", ""])
    for item in package["files"]:
        lines.append(f"- `{item['relative_path']}` size `{item['size']}` sha256 `{item['sha256']}`")

    lines.extend(["", "## Pak Listings", ""])
    for pak in package["paks"]:
        lines.append(f"- Pak: `{pak['pak']}`")
        lines.append(f"  - Return code: `{pak.get('returncode')}`")
        lines.append(f"  - List output: `{pak.get('list_output')}`")
        lines.append(f"  - Expected fragments present: `{pak.get('expected_fragments_present')}`")
        lines.append(f"  - Focused entry count: `{pak.get('focused_entry_count')}`")
        for entry in (pak.get("focused_entries") or [])[:40]:
            lines.append(f"  - `{entry}`")
    lines.append("")
    md_path.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {json_path}")
    print(f"Wrote {md_path}")


def main() -> int:
    editor_root = default_editor_root()
    parser = argparse.ArgumentParser(description="Inspect a packaged MW5 TKU compatibility mod output.")
    parser.add_argument("--mod-name", default=DEFAULT_MOD_NAME)
    parser.add_argument("--package-root", default=str(default_package_root(editor_root)))
    parser.add_argument("--mod-dir", default=None)
    parser.add_argument("--unrealpak", default=str(default_unrealpak(editor_root)))
    args = parser.parse_args()

    package_root = Path(args.package_root).resolve()
    mod_dir, notes = discover_mod_dir(package_root, args.mod_name, args.mod_dir)
    report = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "project_root": str(PROJECT_ROOT),
        "mod_name": args.mod_name,
        "package_root": str(package_root),
        "unrealpak": str(Path(args.unrealpak).resolve()),
        "discovery_notes": notes,
        "expected_pak_fragments": EXPECTED_PAK_FRAGMENTS,
        "package": inspect_package(mod_dir, args.mod_name, Path(args.unrealpak).resolve()),
    }
    write_report(report)
    return 1 if report["package"]["safety_failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
