from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import sys

from tku_project_paths import (
    CONTENT_PAKS_ROOT,
    MODS_ROOT,
    MW5_EDITOR_ROOT,
    PROJECT_ROOT,
    TKU_EDITOR_FIRST_REPORTS_DIR,
    TOOLS_ROOT,
)

sys.path.insert(0, str(TOOLS_ROOT))

from mw5_pak import SIDECAREXT, extract_exact_paths, iter_entries  # noqa: E402


MOD_NAME = "TKUCompatEditorPatch"
MIRROR_PAK_NAME = "MW5Mercs-zzzzTKUCompatEditorPatch.pak"
DISABLED_SUFFIX = ".disabled-by-tku-isolation"
TARGET_GAME_PATHS = (
    "/Game/InnerSphereData/MW5_InnerSphereData.uasset",
    "/Game/InnerSphereData/MW5_InnerSphereData.uexp",
    "/Game/InnerSphereData/StarSystemGenerator.uasset",
    "/Game/InnerSphereData/StarSystemGenerator.uexp",
    "/Game/Levels/FrontEnd/StarMap.umap",
    "/Game/Levels/FrontEnd/StarMap.uexp",
    "/Game/UI/FrontEnd/StarMapPawn.uasset",
    "/Game/UI/FrontEnd/StarMapPawn.uexp",
)
MIRROR_SCOPES = ("starmap-core", "all-game")
UNREALPAK_EXE = MW5_EDITOR_ROOT / "Engine" / "Binaries" / "Win64" / "UnrealPak.exe"


def sha256_file(path: Path) -> str | None:
    if not path.is_file():
        return None
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def source_pak_candidates() -> list[Path]:
    candidates: list[Path] = []
    editor_mod_root = MW5_EDITOR_ROOT / "MW5Mercs" / "Mods" / MOD_NAME
    if editor_mod_root.is_dir():
        candidates.extend(editor_mod_root.rglob(f"{MOD_NAME}.pak"))

    live_mod_pak = MODS_ROOT / MOD_NAME / "Paks" / f"{MOD_NAME}.pak"
    if live_mod_pak.is_file():
        candidates.append(live_mod_pak)

    unique: list[Path] = []
    seen: set[str] = set()
    for candidate in candidates:
        if not candidate.is_file():
            continue
        key = str(candidate.resolve()).lower()
        if key in seen:
            continue
        seen.add(key)
        unique.append(candidate)

    return sorted(unique, key=lambda item: (item.stat().st_mtime, str(item).lower()), reverse=True)


def default_source_pak() -> Path:
    candidates = source_pak_candidates()
    if candidates:
        return candidates[0]
    return MODS_ROOT / MOD_NAME / "Paks" / f"{MOD_NAME}.pak"


def file_summary(path: Path) -> dict[str, Any]:
    item: dict[str, Any] = {
        "path": str(path),
        "exists": path.is_file(),
    }
    if path.is_file():
        stat = path.stat()
        item["file_size"] = stat.st_size
        item["last_write_utc"] = datetime.fromtimestamp(stat.st_mtime, tz=timezone.utc).isoformat()
        item["sha256"] = sha256_file(path)
    return item


def pak_inventory(pak_path: Path, target_paths: set[str], *, hash_large_files: bool = True) -> dict[str, Any]:
    item: dict[str, Any] = {
        "path": str(pak_path),
        "exists": pak_path.is_file(),
        "sha256": None,
        "target_entries": {},
    }
    if not pak_path.is_file():
        return item
    file_size = pak_path.stat().st_size
    item["file_size"] = file_size
    if hash_large_files or file_size < 1024 * 1024 * 512:
        item["sha256"] = sha256_file(pak_path)
    else:
        item["sha256_skipped"] = "file is larger than 512 MiB"
    try:
        _, mount_point, entries = iter_entries(pak_path)
        item["mount_point"] = mount_point
        by_path = {entry.game_path: entry for entry in entries}
        for target_path in sorted(target_paths):
            entry = by_path.get(target_path)
            item["target_entries"][target_path] = (
                None
                if entry is None
                else {
                    "pak_path": entry.pak_path,
                    "size": entry.size,
                    "uncompressed_size": entry.uncompressed_size,
                    "compression_method_index": entry.compression_method_index,
                    "encrypted": entry.encrypted,
                }
            )
        item["target_entry_count"] = sum(1 for value in item["target_entries"].values() if value)
        item["entry_count"] = len(entries)
    except Exception as exc:  # noqa: BLE001 - report evidence, do not mask.
        item["error"] = f"{type(exc).__name__}: {exc}"
    return item


def select_target_paths(source_pak: Path, scope: str) -> set[str]:
    if scope == "starmap-core":
        return set(TARGET_GAME_PATHS)
    if scope != "all-game":
        raise ValueError(f"unsupported mirror scope: {scope}")
    if not source_pak.is_file():
        return set()
    _, _, entries = iter_entries(source_pak)
    return {
        entry.game_path
        for entry in entries
        if entry.game_path.startswith("/Game/") and entry.extension in SIDECAREXT
    }


def scan_content_conflicts(content_paks_root: Path, target_paths: set[str]) -> list[dict[str, Any]]:
    conflicts: list[dict[str, Any]] = []
    if not content_paks_root.is_dir():
        return conflicts
    for pak_path in sorted(content_paks_root.glob("*.pak"), key=lambda item: item.name.lower()):
        inventory = pak_inventory(pak_path, target_paths, hash_large_files=False)
        if inventory.get("target_entry_count"):
            conflicts.append(inventory)
    return conflicts


def game_path_to_content_rel(game_path: str) -> str:
    if not game_path.startswith("/Game/"):
        raise ValueError(f"expected /Game path: {game_path}")
    return game_path[len("/Game/") :]


def stage_payloads_for_unrealpak(
    payloads: dict[str, bytes],
    loose_root: Path,
    response_path: Path,
) -> list[str]:
    if loose_root.exists():
        shutil.rmtree(loose_root)
    loose_root.mkdir(parents=True, exist_ok=True)
    response_path.parent.mkdir(parents=True, exist_ok=True)

    mirrored_paths: list[str] = []
    response_lines: list[str] = []
    for game_path in sorted(payloads):
        rel = game_path_to_content_rel(game_path)
        source_path = loose_root / rel
        source_path.parent.mkdir(parents=True, exist_ok=True)
        source_path.write_bytes(payloads[game_path])
        dest_path = "../../../MW5Mercs/Content/" + rel.replace("\\", "/")
        response_lines.append(f'"{source_path}" "{dest_path}"')
        mirrored_paths.append(game_path)
    response_path.write_text("\n".join(response_lines) + "\n", encoding="utf-8")
    return mirrored_paths


def build_with_unrealpak(output_pak: Path, response_path: Path) -> dict[str, Any]:
    output_pak.parent.mkdir(parents=True, exist_ok=True)
    if output_pak.exists():
        output_pak.unlink()
    command = [str(UNREALPAK_EXE), str(output_pak), f"-Create={response_path}"]
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    return {
        "command": command,
        "returncode": result.returncode,
        "stdout_tail": result.stdout[-4000:],
        "stderr_tail": result.stderr[-4000:],
    }


def write_report(report: dict[str, Any], report_json: Path, report_md: Path) -> None:
    report_json.parent.mkdir(parents=True, exist_ok=True)
    report_json.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")

    lines = [
        f"# TKU Content Mirror - {report['timestamp']}",
        "",
        "Purpose: stage a late-loading `Content\\Paks` mirror of the current editor-authored TKU compat package so root `/Game` assets can win over the legacy loose TKU starmap pak during a controlled runtime test.",
        "",
        f"- Apply requested: `{report['apply_requested']}`",
        f"- Source pak: `{report['source_pak']}`",
        f"- Mirror scope: `{report['mirror_scope']}`",
        f"- Source pak candidates: `{len(report.get('source_pak_candidates', []))}`",
        f"- Staged mirror pak: `{report['staged_pak']}`",
        f"- Live mirror pak: `{report['live_pak']}`",
        f"- Disabled live mirror sibling: `{report['live_disabled_pak']}`",
        f"- Mirror pak SHA256: `{report.get('staged_sha256')}`",
        f"- Files mirrored: `{len(report.get('mirrored_paths', []))}`",
        "",
        "## Safety",
        "",
    ]
    if report["safety_failures"]:
        for failure in report["safety_failures"]:
            lines.append(f"- FAIL: {failure}")
    else:
        lines.append("- No safety failures.")
    lines.extend(["", "## Conflicting Content Paks", ""])
    for conflict in report.get("content_conflicts_before", []):
        lines.append(
            f"- `{Path(conflict['path']).name}` target entries `{conflict.get('target_entry_count')}` "
            f"mount `{conflict.get('mount_point')}` sha `{conflict.get('sha256')}`"
        )
    if not report.get("content_conflicts_before"):
        lines.append("- None found.")
    lines.extend(["", "## Actions", ""])
    for action in report.get("actions", []):
        lines.append(f"- {action}")
    if not report.get("actions"):
        lines.append("- Dry run/staging only; no live files changed.")
    if report.get("live_disabled_backup"):
        lines.extend(["", "## Disabled Mirror Backup", ""])
        lines.append(f"- Moved stale disabled mirror sibling to `{report['live_disabled_backup']}`.")
    if report.get("live_backup"):
        lines.extend(["", "## Rollback", ""])
        lines.append(f"- Replace `{report['live_pak']}` with backup `{report['live_backup']}`.")
    else:
        lines.extend(["", "## Rollback", ""])
        lines.append(f"- Remove only the staged live mirror pak `{report['live_pak']}` to return to the previous content-pak set.")
    lines.extend(["", "## Mirrored Path Sample", ""])
    for path in report.get("mirrored_paths", [])[:160]:
        lines.append(f"- `{path}`")
    report_md.write_text("\n".join(lines), encoding="utf-8")


def build_report(args: argparse.Namespace) -> dict[str, Any]:
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    report_dir = TKU_EDITOR_FIRST_REPORTS_DIR
    staging_dir = report_dir / "staging"
    loose_root = staging_dir / f"content_mirror_loose_{timestamp}"
    response_path = staging_dir / f"content_mirror_unrealpak_response_{timestamp}.txt"
    backup_dir = report_dir / "backups" / f"content_mirror_{timestamp}"
    candidates = source_pak_candidates()
    source_pak = args.source_pak or default_source_pak()
    staged_pak = args.staged_pak or staging_dir / f"MW5Mercs-zzzzTKUCompatEditorPatch-{timestamp}.pak"
    live_pak = args.live_pak or CONTENT_PAKS_ROOT / MIRROR_PAK_NAME
    live_disabled_pak = Path(str(live_pak) + DISABLED_SUFFIX)
    target_paths = select_target_paths(source_pak, args.scope)

    report: dict[str, Any] = {
        "timestamp": timestamp,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "apply_requested": bool(args.apply),
        "source_pak": str(source_pak),
        "mirror_scope": args.scope,
        "source_pak_candidates": [file_summary(candidate) for candidate in candidates],
        "staged_pak": str(staged_pak),
        "live_pak": str(live_pak),
        "live_disabled_pak": str(live_disabled_pak),
        "target_paths": sorted(target_paths),
        "mirrored_paths": [],
        "safety_failures": [],
        "actions": [],
        "live_backup": None,
        "live_disabled_backup": None,
        "unrealpak_exe": str(UNREALPAK_EXE),
        "unrealpak_response": str(response_path),
        "content_conflicts_before": scan_content_conflicts(CONTENT_PAKS_ROOT, target_paths),
    }

    if not source_pak.is_file():
        report["safety_failures"].append(f"source pak missing: {source_pak}")
    if not target_paths:
        report["safety_failures"].append(f"no target paths selected for scope {args.scope}")
    if not UNREALPAK_EXE.is_file():
        report["safety_failures"].append(f"UnrealPak.exe missing: {UNREALPAK_EXE}")
    if not CONTENT_PAKS_ROOT.is_dir():
        report["safety_failures"].append(f"content paks root missing: {CONTENT_PAKS_ROOT}")
    if live_pak.name != MIRROR_PAK_NAME:
        report["safety_failures"].append(f"unexpected live mirror pak name: {live_pak.name}")
    try:
        resolved_live = live_pak.resolve()
        resolved_content = CONTENT_PAKS_ROOT.resolve()
        if not str(resolved_live).lower().startswith(str(resolved_content).lower()):
            report["safety_failures"].append(f"live mirror pak is not under content paks root: {live_pak}")
    except Exception as exc:  # noqa: BLE001
        report["safety_failures"].append(f"could not resolve live/content paths: {type(exc).__name__}: {exc}")

    if not report["safety_failures"]:
        payloads = extract_exact_paths(source_pak, target_paths)
        missing = sorted(target_paths - set(payloads))
        if missing:
            report["safety_failures"].append(f"source pak missing target paths: {missing}")
        else:
            report["mirrored_paths"] = stage_payloads_for_unrealpak(payloads, loose_root, response_path)
            report["unrealpak_build"] = build_with_unrealpak(staged_pak, response_path)
            if report["unrealpak_build"].get("returncode") != 0:
                report["safety_failures"].append(
                    f"UnrealPak build failed with exit code {report['unrealpak_build'].get('returncode')}"
                )
            report["staged_size"] = staged_pak.stat().st_size if staged_pak.is_file() else None
            report["staged_sha256"] = sha256_file(staged_pak)
            report["staged_inventory"] = pak_inventory(staged_pak, target_paths)
            report["actions"].append(f"staged UnrealPak-built content-root mirror pak at {staged_pak}")

            staged_count = report["staged_inventory"].get("target_entry_count")
            if staged_count != len(target_paths):
                report["safety_failures"].append(
                    f"staged mirror pak target entry count mismatch: {staged_count} != {len(target_paths)}"
                )

    if not report["safety_failures"] and args.apply:
        backup_path = None
        if live_pak.is_file():
            backup_dir.mkdir(parents=True, exist_ok=True)
            backup_path = backup_dir / live_pak.name
            shutil.copy2(live_pak, backup_path)
            report["live_backup"] = str(backup_path)
            report["actions"].append(f"backed up existing live mirror pak to {backup_path}")
        if live_disabled_pak.is_file():
            backup_dir.mkdir(parents=True, exist_ok=True)
            disabled_backup_path = backup_dir / live_disabled_pak.name
            shutil.move(str(live_disabled_pak), str(disabled_backup_path))
            report["live_disabled_backup"] = str(disabled_backup_path)
            report["actions"].append(f"moved stale disabled mirror sibling to {disabled_backup_path}")
        live_pak.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(staged_pak, live_pak)
        report["actions"].append(f"deployed live mirror pak to {live_pak}")
        report["live_sha256_after"] = sha256_file(live_pak)
        report["live_disabled_exists_after"] = live_disabled_pak.is_file()
        report["content_conflicts_after"] = scan_content_conflicts(CONTENT_PAKS_ROOT, target_paths)

    report_json = report_dir / f"tku_content_mirror_{timestamp}.json"
    report_md = report_dir / f"tku_content_mirror_{timestamp}.md"
    report["report_json"] = str(report_json)
    report["report_md"] = str(report_md)
    write_report(report, report_json, report_md)
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--scope", choices=MIRROR_SCOPES, default="starmap-core")
    parser.add_argument("--source-pak", type=Path)
    parser.add_argument("--staged-pak", type=Path)
    parser.add_argument("--live-pak", type=Path)
    args = parser.parse_args()
    report = build_report(args)
    print(report["report_json"])
    print(report["report_md"])
    if report["safety_failures"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
