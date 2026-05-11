from __future__ import annotations

import csv
import json
import math
import struct
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
EDITOR_ROOT = Path(r"E:\Games\MechWarrior5Editor")
OUT_DIR = REPORTS_DIR / "tku_editor_first"
OUT_JSON = OUT_DIR / "original_tku_inner_sphere_datatable_rows_20260510.json"
OUT_MD = OUT_DIR / "original_tku_inner_sphere_datatable_rows_20260510.md"
OUT_CSV = OUT_DIR / "original_tku_inner_sphere_datatable_rows_20260510.csv"

ORIGINAL_TKU_PAK = WORKSPACE / "MW5Mercs" / "Mods" / "TheKnownUniverse" / "Paks" / "TheKnownUniverse.pak"
CURRENT_RUNTIME_CSV = EDITOR_ROOT / "MW5Mercs" / "Content" / "InnerSphereData" / "MW5_InnerSphereData.csv"
WIDE_SOURCE_JSON = EDITOR_ROOT / "MW5Mercs" / "Content" / "Data" / "InnerSphereMap" / "MW5_InnerSphereData.json"
TARGET_UASSET = "/Game/InnerSphereData/MW5_InnerSphereData.uasset"
TARGET_UEXP = "/Game/InnerSphereData/MW5_InnerSphereData.uexp"

sys.path.insert(0, str(TOOLS_ROOT))
sys.path.insert(0, str(TOOLS_ROOT / "tku_reference_audit"))

from mw5_pak import extract_exact_paths  # noqa: E402
from parse_ue4_package_refs import Reader, parse_exports, parse_imports, parse_names, parse_summary  # noqa: E402


class RowParseError(ValueError):
    pass


def read_i32(data: bytes, pos: int) -> int:
    if pos < 0 or pos + 4 > len(data):
        raise RowParseError(f"i32 outside payload at {pos}")
    return struct.unpack_from("<i", data, pos)[0]


def read_f32(data: bytes, pos: int) -> float:
    if pos < 0 or pos + 4 > len(data):
        raise RowParseError(f"f32 outside payload at {pos}")
    return struct.unpack_from("<f", data, pos)[0]


def read_fname(data: bytes, pos: int, names: list[str]) -> tuple[str, int, int]:
    index = read_i32(data, pos)
    number = read_i32(data, pos + 4)
    if 0 <= index < len(names):
        name = names[index]
    else:
        name = f"<bad-name-index:{index}>"
    return name, number, pos + 8


def display_fname(name: str, number: int) -> str:
    # UE4 stores FName instance numbers as one-based values; the displayed name
    # uses zero-based suffixes such as C_8.
    if number > 0:
        return f"{name}_{number - 1}"
    return name


def read_fstring(data: bytes, pos: int) -> tuple[str, int]:
    length = read_i32(data, pos)
    pos += 4
    if length == 0:
        return "", pos
    if length > 0:
        end = pos + length
        if end > len(data):
            raise RowParseError(f"fstring outside payload at {pos}+{length}")
        return data[pos:end].rstrip(b"\x00").decode("utf-8", "replace"), end
    byte_count = -length * 2
    end = pos + byte_count
    if end > len(data):
        raise RowParseError(f"wide fstring outside payload at {pos}+{byte_count}")
    return data[pos:end].rstrip(b"\x00").decode("utf-16-le", "replace"), end


def parse_soft_object_path(payload: bytes, names: list[str]) -> str:
    if len(payload) < 12:
        return "None"
    asset_path, _, pos = read_fname(payload, 0, names)
    try:
        subpath, _ = read_fstring(payload, pos)
    except Exception:
        subpath = ""
    if asset_path in ("None", ""):
        return "None"
    return asset_path + ((f":{subpath}") if subpath else "")


def parse_primary_asset_id(payload: bytes, names: list[str]) -> str:
    if len(payload) < 16:
        return ""
    asset_type, _, _ = read_fname(payload, 0, names)
    asset_name, _, _ = read_fname(payload, 8, names)
    if asset_type in ("None", "") or asset_name in ("None", ""):
        return ""
    return f"{asset_type}:{asset_name}"


def decode_text_payload(payload: bytes) -> str:
    # FText is version-dependent and not needed for the repair gate. Keep a compact string hint.
    strings: list[str] = []
    for encoding in ("utf-8", "utf-16-le"):
        try:
            decoded = payload.decode(encoding, "ignore")
        except Exception:
            continue
        cleaned = "".join(ch if ch.isprintable() else " " for ch in decoded)
        cleaned = " ".join(cleaned.split())
        if cleaned:
            strings.append(cleaned[:240])
    return strings[0] if strings else ""


def parse_tagged_properties(data: bytes, pos: int, names: list[str], stop_at: int | None = None) -> tuple[dict[str, Any], int]:
    props: dict[str, Any] = {}
    end = len(data) if stop_at is None else stop_at
    while pos + 8 <= end:
        prop_name, _, pos = read_fname(data, pos, names)
        if prop_name == "None":
            return props, pos
        prop_type, _, pos = read_fname(data, pos, names)
        size = read_i32(data, pos)
        array_index = read_i32(data, pos + 4)
        pos += 8

        type_meta: dict[str, Any] = {"type": prop_type, "size": size, "array_index": array_index}
        if prop_type == "StructProperty":
            struct_name, _, pos = read_fname(data, pos, names)
            guid = data[pos : pos + 16].hex()
            pos += 16
            type_meta["struct_name"] = struct_name
            type_meta["struct_guid"] = guid
            has_guid = data[pos]
            pos += 1
            if has_guid:
                type_meta["property_guid"] = data[pos : pos + 16].hex()
                pos += 16
            value_pos = pos
            value = parse_struct_value(struct_name, data[value_pos : value_pos + size], names)
            pos += size
        elif prop_type == "EnumProperty":
            enum_name, _, pos = read_fname(data, pos, names)
            has_guid = data[pos]
            pos += 1
            if has_guid:
                type_meta["property_guid"] = data[pos : pos + 16].hex()
                pos += 16
            value_name, value_number, pos = read_fname(data, pos, names)
            type_meta["enum_name"] = enum_name
            value = display_fname(value_name, value_number).split("::", 1)[-1]
        else:
            has_guid = data[pos]
            pos += 1
            if has_guid:
                type_meta["property_guid"] = data[pos : pos + 16].hex()
                pos += 16
            value_pos = pos
            value_payload = data[value_pos : value_pos + size]
            value = parse_simple_value(prop_type, value_payload, names)
            pos += size
        props[prop_name] = value
        props[f"__meta_{prop_name}"] = type_meta
    raise RowParseError(f"property list did not terminate before {end}")


def parse_struct_value(struct_name: str, payload: bytes, names: list[str]) -> Any:
    if struct_name == "PrimaryAssetId":
        try:
            nested, _ = parse_tagged_properties(payload, 0, names)
            asset_type = nested.get("PrimaryAssetType") or nested.get("Type") or ""
            asset_name = nested.get("PrimaryAssetName") or nested.get("Name") or ""
            if isinstance(asset_type, dict):
                asset_type = asset_type.get("Name") or asset_type.get("PrimaryAssetType") or ""
            if isinstance(asset_name, dict):
                asset_name = asset_name.get("Name") or asset_name.get("PrimaryAssetName") or ""
            if asset_type in ("None", "") or asset_name in ("None", ""):
                return ""
            return f"{asset_type}:{asset_name}"
        except Exception:
            return parse_primary_asset_id(payload, names)
    try:
        nested, end_pos = parse_tagged_properties(payload, 0, names)
        if struct_name == "FactionAssetId":
            value = nested.get("Id", "")
            return value if isinstance(value, str) else ""
        return nested
    except Exception:
        if struct_name == "FactionAssetId" and len(payload) >= 16:
            return parse_primary_asset_id(payload[-16:], names)
        return {"struct_name": struct_name, "raw_hex_prefix": payload[:48].hex(), "size": len(payload)}


def parse_simple_value(prop_type: str, payload: bytes, names: list[str]) -> Any:
    if prop_type == "StrProperty":
        value, _ = read_fstring(payload, 0)
        return value
    if prop_type == "FloatProperty":
        return read_f32(payload, 0)
    if prop_type == "IntProperty":
        return read_i32(payload, 0)
    if prop_type == "NameProperty":
        value, _, _ = read_fname(payload, 0, names)
        return value
    if prop_type == "SoftObjectProperty":
        return parse_soft_object_path(payload, names)
    if prop_type == "ObjectProperty":
        return read_i32(payload, 0)
    if prop_type == "BoolProperty":
        return bool(payload[0]) if payload else False
    if prop_type == "TextProperty":
        return decode_text_payload(payload)
    return {"type": prop_type, "raw_hex_prefix": payload[:48].hex(), "size": len(payload)}


def find_row_map_start(data: bytes, names: list[str]) -> tuple[int, int, dict[str, Any]]:
    props, pos = parse_tagged_properties(data, 0, names)
    candidates = []
    for delta in (0, 4, 8, 12):
        if pos + delta + 4 <= len(data):
            count = read_i32(data, pos + delta)
            if 0 < count < 10000:
                candidates.append({"pos": pos + delta, "row_count": count, "skipped_bytes_after_properties": delta})
    if not candidates:
        raise RowParseError(f"could not find plausible row count after top-level properties at {pos}")
    chosen = candidates[0]
    return chosen["pos"] + 4, chosen["row_count"], {"top_level_properties": props, **chosen}


def parse_rows(uasset: bytes, uexp: bytes) -> dict[str, Any]:
    reader = Reader(uasset)
    summary = parse_summary(reader)
    names = parse_names(reader, summary)
    imports = parse_imports(reader, names, summary)
    exports = parse_exports(reader, names, summary)
    if not exports:
        raise RowParseError("no exports in DataTable package")
    export = exports[0]
    start = export.serial_offset - len(uasset)
    end = start + export.serial_size
    if start < 0 or end > len(uexp):
        raise RowParseError(f"export serial range outside uexp: {start}..{end} / {len(uexp)}")
    serial = uexp[start:end]
    pos, row_count, row_map_info = find_row_map_start(serial, names)
    rows = []
    errors = []
    for row_index in range(row_count):
        row_start = pos
        try:
            row_name, _, pos = read_fname(serial, pos, names)
            props, pos = parse_tagged_properties(serial, pos, names)
            row = {"row_index": row_index, "row_name": row_name}
            for key, value in props.items():
                if not key.startswith("__meta_"):
                    row[key] = value
            rows.append(row)
        except Exception as exc:
            errors.append({"row_index": row_index, "row_start": row_start, "error": f"{type(exc).__name__}: {exc}"})
            break
    return {
        "summary": summary,
        "export": {
            "object_name": export.object_name.display(),
            "serial_size": export.serial_size,
            "serial_offset": export.serial_offset,
        },
        "name_count": len(names),
        "import_count": len(imports),
        "row_map_info": row_map_info,
        "expected_row_count": row_count,
        "parsed_row_count": len(rows),
        "parse_errors": errors,
        "rows": rows,
    }


def load_current_csv_rows() -> list[dict[str, str]]:
    with CURRENT_RUNTIME_CSV.open("r", encoding="utf-16", newline="") as handle:
        return list(csv.DictReader(handle))


def load_wide_json_rows() -> list[dict]:
    return json.loads(WIDE_SOURCE_JSON.read_text(encoding="utf-8-sig"))


def row_id(row: dict) -> int | None:
    for key in ("row_name", "---", "Name"):
        try:
            return int(str(row.get(key)))
        except Exception:
            pass
    return None


def number_value(row: dict, key: str) -> float | None:
    try:
        value = float(row.get(key))
    except Exception:
        return None
    return value if math.isfinite(value) else None


def range_2d(rows: list[dict], x_key: str = "PosX", y_key: str = "PosY") -> dict:
    points = []
    for row in rows:
        x = number_value(row, x_key)
        y = number_value(row, y_key)
        if x is not None and y is not None:
            points.append((x, y))
    if not points:
        return {"count": 0}
    xs = [x for x, _ in points]
    ys = [y for _, y in points]
    return {
        "count": len(points),
        "x": {"min": min(xs), "max": max(xs), "span": max(xs) - min(xs)},
        "y": {"min": min(ys), "max": max(ys), "span": max(ys) - min(ys)},
    }


def normalize_cluster(value: Any) -> str:
    text = str(value or "")
    if text in ("", "None", '(Id="")'):
        return ""
    marker = "MWFactionAsset:"
    if marker in text:
        return text.split(marker, 1)[1].split('"', 1)[0].split(")", 1)[0]
    if ":" in text:
        return text.rsplit(":", 1)[1]
    return text


def summarize(rows: list[dict], current_rows: list[dict], wide_rows: list[dict]) -> dict:
    ids = [row_id(row) for row in rows if row_id(row) is not None]
    current_ids = {row_id(row) for row in current_rows if row_id(row) is not None}
    wide_ids = {row_id(row) for row in wide_rows if row_id(row) is not None}
    cluster_counts = Counter(normalize_cluster(row.get("Cluster")) for row in rows)
    nonempty_cluster_counts = Counter({key: value for key, value in cluster_counts.items() if key})
    overlay_rows = [row for row in rows if str(row.get("ClusterOverlay") or "") not in ("", "None")]
    constellation_rows = [row for row in rows if str(row.get("ClusterConstellation") or "") not in ("", "None")]
    return {
        "row_count": len(rows),
        "id_min": min(ids) if ids else None,
        "id_max": max(ids) if ids else None,
        "id_count": len(ids),
        "coordinate_range": range_2d(rows),
        "nonempty_cluster_rows": sum(nonempty_cluster_counts.values()),
        "unique_nonempty_cluster_ids": len(nonempty_cluster_counts),
        "top_cluster_ids": dict(nonempty_cluster_counts.most_common(60)),
        "overlay_rows": len(overlay_rows),
        "constellation_rows": len(constellation_rows),
        "sample_overlay_rows": [
            {
                "row_name": row.get("row_name"),
                "Name": row.get("Name"),
                "StarSystemName": row.get("StarSystemName"),
                "Cluster": row.get("Cluster"),
                "ClusterOverlay": row.get("ClusterOverlay"),
                "ClusterConstellation": row.get("ClusterConstellation"),
            }
            for row in overlay_rows[:40]
        ],
        "sample_far_systems": [
            {
                "row_name": row.get("row_name"),
                "Name": row.get("Name"),
                "StarSystemName": row.get("StarSystemName"),
                "PosX": row.get("PosX"),
                "PosY": row.get("PosY"),
                "Cluster": row.get("Cluster"),
            }
            for row in sorted(
                rows,
                key=lambda item: abs(float(item.get("PosX") or 0)) + abs(float(item.get("PosY") or 0)),
                reverse=True,
            )[:40]
        ],
        "ids_missing_from_current_csv_count": len(set(ids) - current_ids),
        "ids_missing_from_current_csv_sample": sorted(set(ids) - current_ids)[:120],
        "ids_missing_from_wide_source_json_count": len(set(ids) - wide_ids),
        "ids_missing_from_wide_source_json_sample": sorted(set(ids) - wide_ids)[:120],
        "current_csv_ids_missing_from_tku_count": len(current_ids - set(ids)),
        "wide_source_ids_missing_from_tku_count": len(wide_ids - set(ids)),
    }


def write_csv(rows: list[dict]) -> None:
    fields = [
        "row_index",
        "row_name",
        "Name",
        "StarSystemName",
        "PosX",
        "PosY",
        "SystemType",
        "SpectralType",
        "Luminosity",
        "SubType",
        "SystemStatus",
        "ChargingStation",
        "Orbitals",
        "Habitable",
        "Description",
        "Cluster",
        "ClusterOverlay",
        "ClusterConstellation",
    ]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(report: dict) -> None:
    summary = report["summary_stats"]
    lines = [
        "# Original TKU InnerSphere DataTable Rows - 2026-05-10",
        "",
        f"- Generated: `{report['generated_utc']}`",
        f"- Source pak: `{ORIGINAL_TKU_PAK}`",
        f"- Source asset: `{TARGET_UASSET}` / `{TARGET_UEXP}`",
        "- Method: read-only local pak extraction plus UE4 package/DataTable row-map parsing.",
        "- Safety: no game, editor, or pak assets were modified.",
        "",
        "## Parse Result",
        "",
        f"- Expected row count: `{report['datatable']['expected_row_count']}`",
        f"- Parsed row count: `{report['datatable']['parsed_row_count']}`",
        f"- Parse errors: `{report['datatable']['parse_errors']}`",
        f"- Row-map info: `{report['datatable']['row_map_info']}`",
        f"- Derived CSV: `{OUT_CSV}`",
        "",
        "## Summary",
        "",
        f"- Row IDs: `{summary['id_min']}` to `{summary['id_max']}` across `{summary['id_count']}` rows",
        f"- Coordinate range: `{summary['coordinate_range']}`",
        f"- Non-empty cluster rows: `{summary['nonempty_cluster_rows']}`",
        f"- Unique cluster ids: `{summary['unique_nonempty_cluster_ids']}`",
        f"- Overlay rows: `{summary['overlay_rows']}`",
        f"- Constellation rows: `{summary['constellation_rows']}`",
        f"- IDs missing from current CSV: `{summary['ids_missing_from_current_csv_count']}`",
        f"- IDs missing from wide source JSON: `{summary['ids_missing_from_wide_source_json_count']}`",
        f"- Current CSV IDs missing from TKU: `{summary['current_csv_ids_missing_from_tku_count']}`",
        f"- Wide source IDs missing from TKU: `{summary['wide_source_ids_missing_from_tku_count']}`",
        "",
        "Top TKU cluster ids:",
    ]
    for key, value in summary["top_cluster_ids"].items():
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "## Sample Overlay Rows", ""])
    for row in summary["sample_overlay_rows"]:
        lines.append(f"- `{row}`")
    lines.extend(["", "## Farthest Systems", ""])
    for row in summary["sample_far_systems"]:
        lines.append(f"- `{row}`")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    payloads = extract_exact_paths(ORIGINAL_TKU_PAK, {TARGET_UASSET, TARGET_UEXP})
    datatable = parse_rows(payloads[TARGET_UASSET], payloads[TARGET_UEXP])
    rows = datatable["rows"]
    current_rows = load_current_csv_rows()
    wide_rows = load_wide_json_rows()
    report = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "source": {
            "original_tku_pak": str(ORIGINAL_TKU_PAK),
            "uasset": TARGET_UASSET,
            "uexp": TARGET_UEXP,
        },
        "datatable": {
            key: value
            for key, value in datatable.items()
            if key != "rows"
        },
        "summary_stats": summarize(rows, current_rows, wide_rows),
        "rows_sample": rows[:20],
        "rows_tail_sample": rows[-20:],
    }
    write_csv(rows)
    OUT_JSON.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    write_markdown(report)
    print(f"wrote {OUT_JSON}")
    print(f"wrote {OUT_MD}")
    print(f"wrote {OUT_CSV}")


if __name__ == "__main__":
    main()
