from __future__ import annotations

import argparse
import json
import os
import re
import struct
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from tku_project_paths import TKU_EDITOR_FIRST_REPORTS_DIR


DEFAULT_SAMPLE_IDS = (1, 3501, 3502, 4001, 4110, 5000, 6000, 7000, 7912, 7921)
MARKERS = (
    "StarMapModel",
    "MWStarMapModel",
    "InnerSphereMapInfo",
    "InnerSphereClass",
    "StarSystemGenerator",
    "HiddenStarSystems",
    "CurrentStarSystemId",
    "StarSystemId",
    "MWClusterDataAsset",
    "ClusterAsset",
    "TaurianConcordat",
    "MagistracyOfCanopus",
    "Clan",
    "RimWorldsRepublic",
    "OutworldsAlliance",
    "Periphery",
)
SEGMENT_END_MARKERS = (
    "TravelModel",
    "InventoryModel",
    "FinanceModel",
    "UnitProgressionModel",
    "RosterModel",
)
TOKEN_RE = re.compile(rb"[\x20-\x7e]{4,}")
FOCUS_TOKEN_RE = re.compile(
    r"(star|sphere|cluster|faction|generator|map|inner|hidden|current|taurian|canopus|clan|periphery|rim)",
    re.IGNORECASE,
)


def read_bytes(path: Path) -> bytes:
    return path.read_bytes()


def sha256_file(path: Path) -> str:
    import hashlib

    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def default_save_root() -> Path:
    local = os.environ.get("LOCALAPPDATA")
    if local:
        return Path(local) / "MW5Mercs" / "Saved" / "SaveGames"
    return Path.home() / "AppData" / "Local" / "MW5Mercs" / "Saved" / "SaveGames"


def find_latest_campaign(save_root: Path) -> Path:
    campaigns = sorted(save_root.glob("*/Campaign.json"), key=lambda item: item.stat().st_mtime, reverse=True)
    if not campaigns:
        raise FileNotFoundError(f"no Campaign.json found under {save_root}")
    return campaigns[0]


def offsets_of(data: bytes, marker: str) -> list[int]:
    needle = marker.encode("utf-8")
    offsets: list[int] = []
    start = 0
    while True:
        found = data.find(needle, start)
        if found == -1:
            break
        offsets.append(found)
        start = found + 1
    return offsets


def token_scan(data: bytes, start: int = 0, end: int | None = None, limit: int = 160) -> list[dict[str, Any]]:
    end = len(data) if end is None else min(end, len(data))
    tokens = []
    for match in TOKEN_RE.finditer(data[start:end]):
        token = match.group().decode("utf-8", "replace")
        if not FOCUS_TOKEN_RE.search(token):
            continue
        tokens.append({"offset": start + match.start(), "text": token})
        if len(tokens) >= limit:
            break
    return tokens


def int_offsets(data: bytes, value: int, *, start: int = 0, end: int | None = None, limit: int = 80) -> list[int]:
    end = len(data) if end is None else min(end, len(data))
    needle = struct.pack("<i", value)
    offsets: list[int] = []
    pos = start
    while pos < end:
        found = data.find(needle, pos, end)
        if found == -1:
            break
        offsets.append(found)
        if len(offsets) >= limit:
            break
        pos = found + 1
    return offsets


def nearest_marker(marker_offsets: dict[str, list[int]], offset: int) -> dict[str, Any]:
    nearest: tuple[int, str, int] | None = None
    for marker, offsets in marker_offsets.items():
        for marker_offset in offsets:
            distance = abs(marker_offset - offset)
            if nearest is None or distance < nearest[0]:
                nearest = (distance, marker, marker_offset)
    if nearest is None:
        return {}
    return {"marker": nearest[1], "marker_offset": nearest[2], "distance": nearest[0]}


def find_starmap_segments(data: bytes) -> list[dict[str, int]]:
    anchors = sorted(set(offsets_of(data, "MWStarMapModel") + offsets_of(data, "StarMapModel")))
    segments: list[dict[str, int]] = []
    for anchor in anchors:
        start = max(0, anchor - 160)
        end_candidates = []
        for marker in SEGMENT_END_MARKERS:
            found = data.find(marker.encode("utf-8"), anchor + 1)
            if found != -1:
                end_candidates.append(found)
        end = min(end_candidates) if end_candidates else min(len(data), anchor + 8192)
        if end <= start:
            continue
        if segments and start <= segments[-1]["end"]:
            segments[-1]["end"] = max(segments[-1]["end"], end)
            continue
        segments.append({"start": start, "anchor": anchor, "end": end, "length": end - start})
    return segments


def scan_sav(path: Path, sample_ids: tuple[int, ...]) -> dict[str, Any]:
    data = read_bytes(path)
    marker_offsets = {marker: offsets_of(data, marker)[:80] for marker in MARKERS}
    segments = find_starmap_segments(data)
    segment_reports = []
    for segment in segments[:8]:
        start = segment["start"]
        end = segment["end"]
        segment_reports.append(
            {
                **segment,
                "focused_tokens": token_scan(data, start, end),
                "sample_id_occurrences": {
                    str(value): int_offsets(data, value, start=start, end=end, limit=20)
                    for value in sample_ids
                },
            }
        )
    global_id_offsets = {
        str(value): int_offsets(data, value, limit=50)
        for value in sample_ids
    }
    global_id_context = {
        value: [nearest_marker(marker_offsets, offset) for offset in offsets[:10]]
        for value, offsets in global_id_offsets.items()
    }
    return {
        "path": str(path),
        "size": path.stat().st_size,
        "last_write_time": datetime.fromtimestamp(path.stat().st_mtime).isoformat(),
        "sha256": sha256_file(path),
        "marker_offsets": marker_offsets,
        "focused_tokens_sample": token_scan(data, limit=240),
        "starmap_segments": segment_reports,
        "global_sample_id_occurrences": global_id_offsets,
        "global_sample_id_nearest_markers": global_id_context,
    }


def load_campaign(campaign_path: Path) -> dict[str, Any]:
    try:
        parsed = json.loads(campaign_path.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        return {"path": str(campaign_path), "error": f"{type(exc).__name__}: {exc}"}
    return {
        "path": str(campaign_path),
        "name": parsed.get("Name"),
        "game_date": parsed.get("GameDate"),
        "last_save_date": parsed.get("LastSaveDate"),
        "start_condition_id": parsed.get("StartConditionId"),
        "last_save_file_name": parsed.get("LastSaveFileName"),
        "save_count": len(parsed.get("Saves", [])),
        "saves": parsed.get("Saves", []),
    }


def build_findings(report: dict[str, Any]) -> list[str]:
    findings: list[str] = []
    campaign = report.get("campaign", {})
    dlc_tags = []
    for save in campaign.get("saves", []):
        for tag in save.get("DLCTags", []):
            if tag not in dlc_tags:
                dlc_tags.append(tag)
    if dlc_tags:
        findings.append(f"Latest campaign save advertises DLC tags: {', '.join(dlc_tags)}.")
    for sav in report.get("sav_files", []):
        segments = sav.get("starmap_segments", [])
        if segments:
            token_text = " | ".join(token["text"] for token in segments[0].get("focused_tokens", [])[:16])
            findings.append(
                f"{Path(sav['path']).name} serializes a StarMapModel segment of {segments[0]['length']} bytes; first focused tokens: {token_text}."
            )
            segment_counts = {
                sid: len(offsets)
                for sid, offsets in segments[0].get("sample_id_occurrences", {}).items()
            }
            findings.append(f"{Path(sav['path']).name} StarMapModel sample-id occurrences: {segment_counts}.")
        markers = sav.get("marker_offsets", {})
        class_count = len(markers.get("StarSystemGenerator", []))
        if class_count:
            findings.append(f"{Path(sav['path']).name} references StarSystemGenerator {class_count} time(s).")
        if markers.get("TaurianConcordat") or markers.get("MagistracyOfCanopus"):
            findings.append(f"{Path(sav['path']).name} contains Taurian/Canopus faction references.")
    return findings


def write_markdown(report: dict[str, Any], output_path: Path) -> None:
    lines = [
        f"# MW5 Save StarMap Scan - {report['timestamp']}",
        "",
        "- Method: read-only binary/string scan of the latest MW5 save directory.",
        "- Safety: no save files, game files, mod files, or editor assets were modified.",
        "",
        "## Findings",
        "",
    ]
    for finding in report.get("findings", []):
        lines.append(f"- {finding}")
    campaign = report.get("campaign", {})
    lines.extend(
        [
            "",
            "## Campaign",
            "",
            f"- Path: `{campaign.get('path')}`",
            f"- Name: `{campaign.get('name')}`",
            f"- Game date: `{campaign.get('game_date')}`",
            f"- Last save date: `{campaign.get('last_save_date')}`",
            f"- Start condition: `{campaign.get('start_condition_id')}`",
            f"- Last save file: `{campaign.get('last_save_file_name')}`",
            f"- Save count: `{campaign.get('save_count')}`",
        ]
    )
    for sav in report.get("sav_files", []):
        lines.extend(
            [
                "",
                f"## `{Path(sav['path']).name}`",
                "",
                f"- Size: `{sav.get('size')}`",
                f"- Last write: `{sav.get('last_write_time')}`",
                f"- SHA256: `{sav.get('sha256')}`",
                f"- StarMapModel segment count: `{len(sav.get('starmap_segments', []))}`",
            ]
        )
        for marker in MARKERS:
            offsets = sav.get("marker_offsets", {}).get(marker, [])
            if offsets:
                lines.append(f"- Marker `{marker}` count `{len(offsets)}` sample offsets `{offsets[:8]}`")
        for segment in sav.get("starmap_segments", [])[:4]:
            lines.append(
                f"- Segment start `{segment['start']}` end `{segment['end']}` length `{segment['length']}`"
            )
            for sid, offsets in segment.get("sample_id_occurrences", {}).items():
                if offsets:
                    lines.append(f"  - Segment int `{sid}` offsets `{offsets}`")
            for token in segment.get("focused_tokens", [])[:40]:
                lines.append(f"  - Token `{token['offset']}` `{token['text']}`")
        lines.append("- Global sample ID occurrence counts:")
        for sid, offsets in sav.get("global_sample_id_occurrences", {}).items():
            lines.append(f"  - `{sid}`: `{len(offsets)}`")
    output_path.write_text("\n".join(lines), encoding="utf-8")


def build_report(args: argparse.Namespace) -> dict[str, Any]:
    save_root = args.save_root or default_save_root()
    campaign_path = args.campaign or find_latest_campaign(save_root)
    save_dir = campaign_path.parent
    sample_ids = tuple(args.sample_ids or DEFAULT_SAMPLE_IDS)
    sav_paths = sorted(save_dir.glob("*.sav"), key=lambda item: item.stat().st_mtime, reverse=True)
    if args.latest_saves:
        sav_paths = sav_paths[: args.latest_saves]
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    report = {
        "timestamp": timestamp,
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "save_root": str(save_root),
        "save_dir": str(save_dir),
        "sample_ids": sample_ids,
        "campaign": load_campaign(campaign_path),
        "sav_files": [scan_sav(path, sample_ids) for path in sav_paths],
    }
    report["findings"] = build_findings(report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only MW5 save starmap/cache scanner.")
    parser.add_argument("--save-root", type=Path)
    parser.add_argument("--campaign", type=Path)
    parser.add_argument("--latest-saves", type=int, default=2)
    parser.add_argument("--sample-ids", type=int, nargs="*")
    args = parser.parse_args()
    report = build_report(args)
    out_dir = TKU_EDITOR_FIRST_REPORTS_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = out_dir / f"mw5_save_starmap_scan_{report['timestamp']}.json"
    md_path = out_dir / f"mw5_save_starmap_scan_{report['timestamp']}.md"
    json_path.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(report, md_path)
    print(json_path)
    print(md_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
