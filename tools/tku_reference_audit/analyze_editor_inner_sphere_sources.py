from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

EDITOR_ROOT = Path(r"E:\Games\MechWarrior5Editor")
from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
DATA_ROOT = EDITOR_ROOT / "MW5Mercs" / "Content" / "Data" / "InnerSphereMap"
RUNTIME_ROOT = EDITOR_ROOT / "MW5Mercs" / "Content" / "InnerSphereData"
OUT_DIR = REPORTS_DIR / "tku_editor_first"


def parse_utf16_json_with_line_ending_repair(path: Path) -> tuple[object, dict]:
    raw = path.read_bytes()
    repaired = raw.replace(b"\r\n\x00", b"\n\x00")
    repair_bytes_removed = len(raw) - len(repaired)
    text = repaired.decode("utf-16-le")
    if text.startswith("\ufeff"):
        text = text[1:]
    return json.loads(text), {
        "encoding": "utf-16-le",
        "line_ending_repair": "replace b'\\r\\n\\x00' with b'\\n\\x00'",
        "repair_bytes_removed": repair_bytes_removed,
    }


def parse_csv(path: Path, encoding: str) -> list[dict[str, str]]:
    with path.open("r", encoding=encoding, newline="") as handle:
        return list(csv.DictReader(handle))


def coordinate_range(rows: list[dict], x_key: str, y_key: str) -> dict:
    xs = [float(row[x_key]) for row in rows if row.get(x_key) not in (None, "")]
    ys = [float(row[y_key]) for row in rows if row.get(y_key) not in (None, "")]
    return {
        "min_x": min(xs) if xs else None,
        "max_x": max(xs) if xs else None,
        "min_y": min(ys) if ys else None,
        "max_y": max(ys) if ys else None,
    }


def contains(row: dict, term: str) -> bool:
    return term.lower() in json.dumps(row, ensure_ascii=False).lower()


def samples(rows: list[dict], keys: list[str], limit: int = 8) -> list[dict]:
    return [{key: row.get(key) for key in keys} for row in rows[:limit]]


def main() -> int:
    inner_json_path = DATA_ROOT / "MW5_InnerSphereData.json"
    source_employers_path = DATA_ROOT / "EmployerInfoData.csv"
    source_factions_path = DATA_ROOT / "SystemFactionChanges.json"
    runtime_inner_csv_path = RUNTIME_ROOT / "MW5_InnerSphereData.csv"

    inner_json = json.loads(inner_json_path.read_text(encoding="utf-8-sig"))
    source_employers = parse_csv(source_employers_path, "utf-8-sig")
    source_factions, faction_parse_info = parse_utf16_json_with_line_ending_repair(source_factions_path)
    runtime_inner_csv = parse_csv(runtime_inner_csv_path, "utf-16")

    source_terms = {}
    for term in ("Clan", "Lyran", "Steiner", "ComStar", "FederatedCommonwealth", "Wolf"):
        source_terms[term] = {
            "inner_json_count": sum(1 for row in inner_json if contains(row, term)),
            "employer_count": sum(1 for row in source_employers if contains(row, term)),
            "system_faction_count": sum(1 for row in source_factions if contains(row, term)),
            "runtime_inner_csv_count": sum(1 for row in runtime_inner_csv if contains(row, term)),
        }

    faction_code_counts = Counter()
    for row in source_factions:
        for change in row.get("FactionChange", []):
            faction_code_counts.update(str(change.get("Faction", "")).split(","))

    report = {
        "editor_root": str(EDITOR_ROOT),
        "source_files": {
            "inner_sphere_json": str(inner_json_path),
            "employer_info_csv": str(source_employers_path),
            "system_faction_changes_json": str(source_factions_path),
            "runtime_inner_sphere_csv": str(runtime_inner_csv_path),
        },
        "parse_notes": {
            "system_faction_changes_json": faction_parse_info,
            "runtime_inner_sphere_csv_encoding": "utf-16",
        },
        "counts": {
            "inner_sphere_json_rows": len(inner_json),
            "source_employer_rows": len(source_employers),
            "source_system_faction_rows": len(source_factions),
            "runtime_inner_sphere_csv_rows": len(runtime_inner_csv),
        },
        "coordinate_ranges": {
            "inner_sphere_json": coordinate_range(inner_json, "PosX", "PosY"),
            "runtime_inner_sphere_csv": coordinate_range(runtime_inner_csv, "PosX", "PosY"),
        },
        "term_counts": source_terms,
        "top_faction_codes": dict(faction_code_counts.most_common(40)),
        "samples": {
            "inner_json_clan": samples([row for row in inner_json if contains(row, "Clan")], ["Name", "StarSystemName", "PosX", "PosY", "SystemStatus"]),
            "source_employer_clan": samples([row for row in source_employers if contains(row, "Clan")], ["Short", "Employer"]),
            "source_employer_lyran": samples([row for row in source_employers if contains(row, "Lyran")], ["Short", "Employer"]),
            "system_faction_clan": samples([row for row in source_factions if contains(row, "Clan")], ["Name", "Primary", "FactionChange"], limit=5),
        },
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    json_path = OUT_DIR / "editor_inner_sphere_source_analysis.json"
    md_path = OUT_DIR / "editor_inner_sphere_source_analysis.md"
    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")

    lines = [
        "# Editor InnerSphere Source Analysis",
        "",
        "This report inspects source-style data included with the MW5 Mod Editor. It does not modify editor or game assets.",
        "",
        "## Counts",
        "",
    ]
    for key, value in report["counts"].items():
        lines.append(f"- `{key}`: {value}")
    lines.extend(["", "## Coordinate Ranges", ""])
    for key, value in report["coordinate_ranges"].items():
        lines.append(f"- `{key}`: X {value['min_x']} to {value['max_x']}, Y {value['min_y']} to {value['max_y']}")
    lines.extend(["", "## Parse Notes", ""])
    lines.append(f"- `SystemFactionChanges.json`: {faction_parse_info}")
    lines.append("- `MW5_InnerSphereData.csv`: parsed as UTF-16")
    lines.extend(["", "## Term Counts", ""])
    for term, counts in source_terms.items():
        lines.append(f"- `{term}`: {counts}")
    lines.extend(["", "## Top Faction Codes In Source SystemFactionChanges", ""])
    for key, value in report["top_faction_codes"].items():
        lines.append(f"- `{key}`: {value}")
    lines.extend(["", "## Key Samples", ""])
    for key, rows in report["samples"].items():
        lines.append(f"### `{key}`")
        lines.append("")
        for row in rows:
            lines.append(f"- `{json.dumps(row, ensure_ascii=False)}`")
        lines.append("")
    md_path.write_text("\n".join(lines), encoding="utf-8")
    print(json_path)
    print(md_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
