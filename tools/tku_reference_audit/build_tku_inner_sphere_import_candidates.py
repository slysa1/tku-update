from __future__ import annotations

import csv
import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
EDITOR_ROOT = Path(r"E:\Games\MechWarrior5Editor")
CURRENT_RUNTIME_CSV = EDITOR_ROOT / "MW5Mercs" / "Content" / "InnerSphereData" / "MW5_InnerSphereData.csv"
OUT_DIR = REPORTS_DIR / "tku_editor_first"
TKU_PARSED_CSV = OUT_DIR / "original_tku_inner_sphere_datatable_rows_20260510.csv"

RAW_UTF16 = OUT_DIR / "tku_inner_sphere_raw_original_current_schema_20260510.csv"
RAW_UTF8 = OUT_DIR / "tku_inner_sphere_raw_original_current_schema_20260510.utf8.csv"
MERGED_UTF16 = OUT_DIR / "tku_inner_sphere_merged_current_plus_tku_additions_20260510.csv"
MERGED_UTF8 = OUT_DIR / "tku_inner_sphere_merged_current_plus_tku_additions_20260510.utf8.csv"
OUT_JSON = OUT_DIR / "tku_inner_sphere_import_candidates_20260510.json"
OUT_MD = OUT_DIR / "tku_inner_sphere_import_candidates_20260510.md"


NULL_VALUES = {"", "None", "none", "NULL", "null", "(Id=\"\")"}
ROW_FIELD = "---"


def read_csv(path: Path, encoding: str) -> list[dict[str, str]]:
    with path.open("r", encoding=encoding, newline="") as handle:
        return list(csv.DictReader(handle))


def current_fieldnames() -> list[str]:
    with CURRENT_RUNTIME_CSV.open("r", encoding="utf-16", newline="") as handle:
        reader = csv.reader(handle)
        return next(reader)


def row_id(row: dict[str, Any]) -> int | None:
    for key in (ROW_FIELD, "Name", "row_name"):
        value = row.get(key)
        try:
            return int(str(value).strip())
        except (TypeError, ValueError):
            continue
    return None


def format_cluster(value: Any) -> str:
    text = str(value or "").strip()
    if text in NULL_VALUES:
        return '(Id="")'
    match = re.fullmatch(r'\(Id="([^"]*)"\)', text)
    if match:
        return text
    if text.startswith("MWFactionAsset:"):
        return f'(Id="{text}")'
    return f'(Id="MWFactionAsset:{text}")'


def format_asset(value: Any) -> str:
    text = str(value or "").strip()
    return "None" if text in NULL_VALUES else text


def tku_row_to_current_schema(row: dict[str, str], fieldnames: list[str]) -> dict[str, str]:
    out = {field: "" for field in fieldnames}
    ident = row.get("row_name") or row.get("Name") or ""
    out[ROW_FIELD] = ident
    for field in fieldnames:
        if field in (ROW_FIELD, "Description", "Cluster", "ClusterOverlay", "ClusterConstellation"):
            continue
        out[field] = row.get(field, "")
    out["Name"] = row.get("Name") or ident
    out["Description"] = ""
    out["Cluster"] = format_cluster(row.get("Cluster"))
    out["ClusterOverlay"] = format_asset(row.get("ClusterOverlay"))
    out["ClusterConstellation"] = format_asset(row.get("ClusterConstellation"))
    return out


def write_candidate(path: Path, rows: list[dict[str, str]], fieldnames: list[str], encoding: str) -> None:
    with path.open("w", encoding=encoding, newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def norm_float(value: Any) -> float | None:
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def compare_shared(current_by_id: dict[int, dict[str, str]], tku_by_id: dict[int, dict[str, str]]) -> dict[str, Any]:
    shared = sorted(set(current_by_id) & set(tku_by_id))
    name_diffs = []
    position_diffs = []
    cluster_diffs = []
    for ident in shared:
        cur = current_by_id[ident]
        tku = tku_by_id[ident]
        if (cur.get("StarSystemName") or "") != (tku.get("StarSystemName") or ""):
            name_diffs.append(
                {
                    "id": ident,
                    "current": cur.get("StarSystemName"),
                    "tku": tku.get("StarSystemName"),
                }
            )
        cur_x, cur_y = norm_float(cur.get("PosX")), norm_float(cur.get("PosY"))
        tku_x, tku_y = norm_float(tku.get("PosX")), norm_float(tku.get("PosY"))
        if cur_x is not None and cur_y is not None and tku_x is not None and tku_y is not None:
            if abs(cur_x - tku_x) > 0.001 or abs(cur_y - tku_y) > 0.001:
                position_diffs.append(
                    {
                        "id": ident,
                        "name": tku.get("StarSystemName") or cur.get("StarSystemName"),
                        "current": {"x": cur_x, "y": cur_y},
                        "tku": {"x": tku_x, "y": tku_y},
                    }
                )
        if format_cluster(cur.get("Cluster")) != format_cluster(tku.get("Cluster")):
            cluster_diffs.append(
                {
                    "id": ident,
                    "name": tku.get("StarSystemName") or cur.get("StarSystemName"),
                    "current": cur.get("Cluster"),
                    "tku": format_cluster(tku.get("Cluster")),
                }
            )
    return {
        "shared_id_count": len(shared),
        "name_diff_count": len(name_diffs),
        "name_diff_sample": name_diffs[:40],
        "position_diff_count": len(position_diffs),
        "position_diff_sample": position_diffs[:40],
        "cluster_diff_count": len(cluster_diffs),
        "cluster_diff_sample": cluster_diffs[:40],
    }


def enum_value_summary(rows: list[dict[str, str]], fields: list[str]) -> dict[str, Any]:
    return {
        field: {
            "unique_count": len(values := sorted(set(row.get(field, "") for row in rows))),
            "values": values,
        }
        for field in fields
    }


def cluster_counts(rows: list[dict[str, str]]) -> dict[str, int]:
    counter = Counter(format_cluster(row.get("Cluster")) for row in rows)
    counter.pop('(Id="")', None)
    return dict(counter.most_common(80))


def main() -> None:
    fieldnames = current_fieldnames()
    current_rows = read_csv(CURRENT_RUNTIME_CSV, "utf-16")
    tku_rows = read_csv(TKU_PARSED_CSV, "utf-8-sig")
    current_by_id = {ident: row for row in current_rows if (ident := row_id(row)) is not None}
    tku_by_id = {ident: row for row in tku_rows if (ident := row_id(row)) is not None}

    raw_rows = [tku_row_to_current_schema(row, fieldnames) for row in tku_rows]
    tku_addition_ids = sorted(set(tku_by_id) - set(current_by_id))
    current_only_ids = sorted(set(current_by_id) - set(tku_by_id))
    merged_rows = [dict(row) for row in current_rows]
    merged_rows.extend(tku_row_to_current_schema(tku_by_id[ident], fieldnames) for ident in tku_addition_ids)
    merged_rows.sort(key=lambda row: row_id(row) if row_id(row) is not None else 10**9)

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_candidate(RAW_UTF16, raw_rows, fieldnames, "utf-16")
    write_candidate(RAW_UTF8, raw_rows, fieldnames, "utf-8")
    write_candidate(MERGED_UTF16, merged_rows, fieldnames, "utf-16")
    write_candidate(MERGED_UTF8, merged_rows, fieldnames, "utf-8")

    enum_fields = [
        "SystemType",
        "SpectralType",
        "Luminosity",
        "SystemStatus",
        "ChargingStation",
        "Orbitals",
        "Habitable",
    ]
    current_enums = enum_value_summary(current_rows, enum_fields)
    raw_enums = enum_value_summary(raw_rows, enum_fields)
    enum_compat = {
        field: {
            "tku_values_missing_from_current_observed_values": sorted(
                set(raw_enums[field]["values"]) - set(current_enums[field]["values"])
            ),
            "current_observed_values_missing_from_tku": sorted(
                set(current_enums[field]["values"]) - set(raw_enums[field]["values"])
            ),
        }
        for field in enum_fields
    }

    report = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "non_mutating": True,
        "inputs": {
            "current_runtime_csv": str(CURRENT_RUNTIME_CSV),
            "original_tku_parsed_csv": str(TKU_PARSED_CSV),
        },
        "outputs": {
            "raw_original_current_schema_utf16": str(RAW_UTF16),
            "raw_original_current_schema_utf8": str(RAW_UTF8),
            "merged_current_plus_tku_additions_utf16": str(MERGED_UTF16),
            "merged_current_plus_tku_additions_utf8": str(MERGED_UTF8),
        },
        "row_counts": {
            "current_rows": len(current_rows),
            "raw_original_tku_rows": len(raw_rows),
            "merged_rows": len(merged_rows),
            "tku_addition_rows": len(tku_addition_ids),
            "current_only_rows_retained_in_merged": len(current_only_ids),
            "shared_rows": len(set(current_by_id) & set(tku_by_id)),
        },
        "fieldnames": fieldnames,
        "shared_row_differences": compare_shared(current_by_id, tku_by_id),
        "enum_compatibility": enum_compat,
        "cluster_counts": {
            "current": cluster_counts(current_rows),
            "raw_original_tku": cluster_counts(raw_rows),
            "merged": cluster_counts(merged_rows),
        },
        "samples": {
            "tku_addition_ids": tku_addition_ids[:120],
            "current_only_ids": current_only_ids[:120],
            "raw_rows": raw_rows[:5],
            "merged_tku_additions": [tku_row_to_current_schema(tku_by_id[ident], fieldnames) for ident in tku_addition_ids[:10]],
        },
        "decision": {
            "build_authorized": False,
            "preferred_first_editor_data_candidate": "merged_current_plus_tku_additions",
            "reason": "The merged candidate preserves current 1.13 rows and descriptions while adding TKU-only systems; raw original TKU rows are retained only as clean-source reference.",
        },
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")

    lines = [
        "# TKU InnerSphere Import Candidates - 2026-05-10",
        "",
        f"- Generated: `{report['generated_utc']}`",
        "- Method: local CSV normalization only.",
        "- Safety: no editor assets, game assets, modlist, or paks were modified.",
        "",
        "## Outputs",
        "",
        f"- Raw original TKU, current schema UTF-16: `{RAW_UTF16}`",
        f"- Raw original TKU, current schema UTF-8: `{RAW_UTF8}`",
        f"- Merged current + TKU additions UTF-16: `{MERGED_UTF16}`",
        f"- Merged current + TKU additions UTF-8: `{MERGED_UTF8}`",
        "",
        "## Counts",
        "",
        f"- Current rows: `{len(current_rows)}`",
        f"- Raw original TKU rows: `{len(raw_rows)}`",
        f"- Merged rows: `{len(merged_rows)}`",
        f"- TKU-only addition rows: `{len(tku_addition_ids)}`",
        f"- Current-only rows retained in merged: `{len(current_only_ids)}`",
        f"- Shared rows: `{len(set(current_by_id) & set(tku_by_id))}`",
        "",
        "## Compatibility Notes",
        "",
        f"- Enum compatibility: `{enum_compat}`",
        f"- Shared row differences: `{report['shared_row_differences']}`",
        "",
        "## Decision",
        "",
        f"- Build authorized: `{report['decision']['build_authorized']}`",
        f"- Preferred first editor data candidate: `{report['decision']['preferred_first_editor_data_candidate']}`",
        f"- Reason: {report['decision']['reason']}",
        "",
    ]
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")
    print(f"Wrote {RAW_UTF16}")
    print(f"Wrote {MERGED_UTF16}")


if __name__ == "__main__":
    main()
