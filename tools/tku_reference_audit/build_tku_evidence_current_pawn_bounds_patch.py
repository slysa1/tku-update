from __future__ import annotations

import hashlib
import json
import shutil
import struct
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from mw5_pak import build_pak, extract_exact_paths
from parse_ue4_package_refs import Reader, parse_exports, parse_names, parse_summary


from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
VANILLA_PAK = WORKSPACE / "MW5Mercs" / "Content" / "Paks" / "MW5Mercs-WindowsNoEditor.pak"
ORIGINAL_TKU_PAK = WORKSPACE / "MW5Mercs" / "Mods" / "TheKnownUniverse" / "Paks" / "TheKnownUniverse.pak"

OUTPUT_MOD_NAME = "TKUEvidenceCurrentPawnBounds"
OUTPUT_ROOT = WORKSPACE / "MW5Mercs" / "Mods" / OUTPUT_MOD_NAME
OUTPUT_PAK = OUTPUT_ROOT / "Paks" / f"{OUTPUT_MOD_NAME}.pak"
OUTPUT_MOD_JSON = OUTPUT_ROOT / "mod.json"

REPORT_DIR = REPORTS_DIR / "tku_editor_first"
REPORT_MD = REPORT_DIR / "tku_evidence_current_pawn_bounds_20260510.md"
REPORT_JSON = REPORT_DIR / "tku_evidence_current_pawn_bounds_20260510.json"

BASE_PATH = "/Game/UI/FrontEnd/StarMapPawn"
TARGET_PATHS = {f"{BASE_PATH}.uasset", f"{BASE_PATH}.uexp"}

TKU_PAN_VERTICAL = 16000.0
TKU_PAN_HORIZONTAL = 8500.0
TKU_ZOOM_DISTANCES = [300.0, 600.0, 900.0, 1300.0, 1800.0, 2200.0, 2800.0, 3500.0, 5000.0, 7500.0, 9000.0]
TKU_ZOOM_THRESHOLDS = [3500, 1000]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def fstr_next(data: bytes, pos: int) -> int:
    length = struct.unpack_from("<i", data, pos)[0]
    pos += 4
    if length > 0:
        pos += length
    elif length < 0:
        pos += -length * 2
    return pos


def summary_positions(data: bytes) -> dict[str, int]:
    pos = 4 + 4 + 4 + 4 + 4
    custom_version_count = struct.unpack_from("<i", data, pos)[0]
    pos += 4 + custom_version_count * 20
    positions: dict[str, int] = {"total_header_size": pos}
    pos += 4
    pos = fstr_next(data, pos)
    positions["package_flags"] = pos
    pos += 4
    for name in (
        "name_count",
        "name_offset",
        "gatherable_text_data_count",
        "gatherable_text_data_offset",
        "export_count",
        "export_offset",
        "import_count",
        "import_offset",
        "depends_offset",
        "soft_package_references_count",
        "soft_package_references_offset",
        "searchable_names_offset",
        "thumbnail_table_offset",
    ):
        positions[name] = pos
        pos += 4
    positions["guid"] = pos
    pos += 16
    positions["generation_count"] = pos
    generation_count = struct.unpack_from("<i", data, pos)[0]
    pos += 4
    for index in range(generation_count):
        positions[f"generation_{index}_export_count"] = pos
        positions[f"generation_{index}_name_count"] = pos + 4
        pos += 8
    return positions


def name_entry_ranges(data: bytes, summary: dict[str, Any]) -> dict[str, tuple[int, int]]:
    ranges: dict[str, tuple[int, int]] = {}
    pos = int(summary["name_offset"])
    reader = Reader(data)
    names = parse_names(reader, summary)
    for name in names:
        start = pos
        pos = fstr_next(data, pos)
        pos += 4
        ranges[name] = (start, pos)
    return ranges


def read_fname(data: bytes, pos: int, names: list[str]) -> tuple[str, int, int, int]:
    index = struct.unpack_from("<i", data, pos)[0]
    number = struct.unpack_from("<i", data, pos + 4)[0]
    if 0 <= index < len(names):
        name = names[index]
    else:
        name = f"<bad-name-index:{index}>"
    return name, index, number, pos + 8


def write_fname(index: int, number: int = 0) -> bytes:
    return struct.pack("<ii", index, number)


def decode_property_tags(cdo: bytes, names: list[str]) -> list[dict[str, Any]]:
    tags: list[dict[str, Any]] = []
    pos = 0
    while pos + 8 <= len(cdo):
        start = pos
        prop_name, prop_name_index, prop_number, pos = read_fname(cdo, pos, names)
        if prop_name == "None":
            tags.append({"name": "None", "name_index": prop_name_index, "start": start, "end": pos})
            break
        prop_type, prop_type_index, prop_type_number, pos = read_fname(cdo, pos, names)
        size = struct.unpack_from("<i", cdo, pos)[0]
        array_index = struct.unpack_from("<i", cdo, pos + 4)[0]
        pos += 8
        inner_type = None
        inner_type_index = None
        if prop_type == "ArrayProperty":
            inner_type, inner_type_index, _, pos = read_fname(cdo, pos, names)
        has_property_guid = cdo[pos]
        pos += 1
        value_start = pos
        value_end = value_start + size
        tags.append(
            {
                "name": prop_name,
                "name_index": prop_name_index,
                "name_number": prop_number,
                "type": prop_type,
                "type_index": prop_type_index,
                "type_number": prop_type_number,
                "size": size,
                "array_index": array_index,
                "inner_type": inner_type,
                "inner_type_index": inner_type_index,
                "has_property_guid": bool(has_property_guid),
                "start": start,
                "value_start": value_start,
                "value_end": value_end,
                "end": value_end,
            }
        )
        pos = value_end
    return tags


def array_property_tag(name_index: int, inner_type_index: int, values: list[float] | list[int], value_kind: str) -> bytes:
    if value_kind == "float":
        value_bytes = struct.pack("<i", len(values)) + b"".join(struct.pack("<f", float(value)) for value in values)
    elif value_kind == "int":
        value_bytes = struct.pack("<i", len(values)) + b"".join(struct.pack("<i", int(value)) for value in values)
    else:
        raise ValueError(value_kind)
    return (
        write_fname(name_index)
        + write_fname(NAME_INDEX["ArrayProperty"])
        + struct.pack("<ii", len(value_bytes), 0)
        + write_fname(inner_type_index)
        + b"\x00"
        + value_bytes
    )


def float_property_tag(name_index: int, value: float) -> bytes:
    return (
        write_fname(name_index)
        + write_fname(NAME_INDEX["FloatProperty"])
        + struct.pack("<ii", 4, 0)
        + b"\x00"
        + struct.pack("<f", value)
    )


NAME_INDEX: dict[str, int] = {}


def patch_current_starmap_pawn(vanilla_uasset: bytes, vanilla_uexp: bytes, tku_uasset: bytes) -> tuple[bytes, bytes, dict[str, Any]]:
    vanilla_reader = Reader(vanilla_uasset)
    vanilla_summary = parse_summary(vanilla_reader)
    vanilla_names = parse_names(vanilla_reader, vanilla_summary)
    vanilla_exports = parse_exports(vanilla_reader, vanilla_names, vanilla_summary)

    tku_reader = Reader(tku_uasset)
    tku_summary = parse_summary(tku_reader)
    tku_name_ranges = name_entry_ranges(tku_uasset, tku_summary)

    missing_names = [name for name in ("PanBoundsVertical", "PanBoundsHorizontal") if name not in vanilla_names]
    if missing_names != ["PanBoundsVertical", "PanBoundsHorizontal"]:
        raise RuntimeError(f"unexpected missing-name set: {missing_names}")
    for required in ("ArrayProperty", "FloatProperty", "IntProperty", "ZoomDistanceList", "ZoomLevelThresholds"):
        if required not in vanilla_names:
            raise RuntimeError(f"required current name missing: {required}")
    for required in missing_names:
        if required not in tku_name_ranges:
            raise RuntimeError(f"required TKU name entry missing: {required}")

    name_entries = b"".join(tku_uasset[start:end] for name in missing_names for start, end in [tku_name_ranges[name]])
    name_delta = len(name_entries)
    new_name_indices = {name: len(vanilla_names) + index for index, name in enumerate(missing_names)}

    global NAME_INDEX
    NAME_INDEX = {name: index for index, name in enumerate(vanilla_names)}

    default_export = next((item for item in vanilla_exports if item.object_name.name == "Default__StarMapPawn_C"), None)
    if default_export is None:
        raise RuntimeError("current Default__StarMapPawn_C export not found")
    cdo_start = default_export.serial_offset - len(vanilla_uasset)
    cdo_end = cdo_start + default_export.serial_size
    old_cdo = vanilla_uexp[cdo_start:cdo_end]
    tags = decode_property_tags(old_cdo, vanilla_names)

    pan_prefix = (
        float_property_tag(new_name_indices["PanBoundsVertical"], TKU_PAN_VERTICAL)
        + float_property_tag(new_name_indices["PanBoundsHorizontal"], TKU_PAN_HORIZONTAL)
    )
    rewritten = bytearray(pan_prefix)
    before_values: dict[str, Any] = {}
    after_values: dict[str, Any] = {
        "PanBoundsVertical": TKU_PAN_VERTICAL,
        "PanBoundsHorizontal": TKU_PAN_HORIZONTAL,
        "ZoomDistanceList": TKU_ZOOM_DISTANCES,
        "ZoomLevelThresholds": TKU_ZOOM_THRESHOLDS,
    }
    for tag in tags:
        if tag["name"] == "ZoomDistanceList":
            count = struct.unpack_from("<i", old_cdo, tag["value_start"])[0]
            before_values["ZoomDistanceList"] = [
                struct.unpack_from("<f", old_cdo, tag["value_start"] + 4 + index * 4)[0]
                for index in range(count)
            ]
            rewritten += array_property_tag(
                tag["name_index"],
                tag["inner_type_index"],
                TKU_ZOOM_DISTANCES,
                "float",
            )
        elif tag["name"] == "ZoomLevelThresholds":
            count = struct.unpack_from("<i", old_cdo, tag["value_start"])[0]
            before_values["ZoomLevelThresholds"] = [
                struct.unpack_from("<i", old_cdo, tag["value_start"] + 4 + index * 4)[0]
                for index in range(count)
            ]
            rewritten += array_property_tag(
                tag["name_index"],
                tag["inner_type_index"],
                TKU_ZOOM_THRESHOLDS,
                "int",
            )
        else:
            rewritten += old_cdo[tag["start"]:tag["end"]]
    new_cdo = bytes(rewritten)
    cdo_delta = len(new_cdo) - len(old_cdo)

    new_uasset = bytearray(vanilla_uasset)
    name_map_end = int(vanilla_summary["import_offset"])
    new_uasset[name_map_end:name_map_end] = name_entries

    positions = summary_positions(vanilla_uasset)
    patch_i32(new_uasset, positions["total_header_size"], int(vanilla_summary["total_header_size"]) + name_delta)
    patch_i32(new_uasset, positions["name_count"], int(vanilla_summary["name_count"]) + len(missing_names))
    patch_i32(new_uasset, positions["import_offset"], int(vanilla_summary["import_offset"]) + name_delta)
    patch_i32(new_uasset, positions["export_offset"], int(vanilla_summary["export_offset"]) + name_delta)
    patch_i32(new_uasset, positions["depends_offset"], int(vanilla_summary["depends_offset"]) + name_delta)
    patch_i32(new_uasset, positions["generation_0_name_count"], int(vanilla_summary["name_count"]) + len(missing_names))

    export_offset = int(vanilla_summary["export_offset"]) + name_delta
    export_count = int(vanilla_summary["export_count"])
    depends_offset = int(vanilla_summary["depends_offset"]) + name_delta
    stride = (depends_offset - export_offset) // export_count
    for export in vanilla_exports:
        export_pos = export_offset + export.index * stride
        new_serial_offset = export.serial_offset + name_delta
        new_serial_size = export.serial_size
        if export.index == default_export.index:
            new_serial_size += cdo_delta
        elif export.serial_offset > default_export.serial_offset:
            new_serial_offset += cdo_delta
        patch_i64(new_uasset, export_pos + 28, new_serial_size)
        patch_i64(new_uasset, export_pos + 36, new_serial_offset)

    new_uexp = vanilla_uexp[:cdo_start] + new_cdo + vanilla_uexp[cdo_end:]
    return bytes(new_uasset), new_uexp, {
        "name_delta": name_delta,
        "cdo_delta": cdo_delta,
        "added_names": missing_names,
        "new_name_indices": new_name_indices,
        "before_values": before_values,
        "after_values": after_values,
        "old_cdo_size": len(old_cdo),
        "new_cdo_size": len(new_cdo),
        "old_uasset_size": len(vanilla_uasset),
        "new_uasset_size": len(new_uasset),
        "old_uexp_size": len(vanilla_uexp),
        "new_uexp_size": len(new_uexp),
    }


def patch_i32(data: bytearray, pos: int, value: int) -> None:
    data[pos:pos + 4] = struct.pack("<i", value)


def patch_i64(data: bytearray, pos: int, value: int) -> None:
    data[pos:pos + 8] = struct.pack("<q", value)


def build() -> dict[str, Any]:
    vanilla = extract_exact_paths(VANILLA_PAK, TARGET_PATHS)
    tku = extract_exact_paths(ORIGINAL_TKU_PAK, {f"{BASE_PATH}.uasset"})
    patched_uasset, patched_uexp, patch_report = patch_current_starmap_pawn(
        vanilla[f"{BASE_PATH}.uasset"],
        vanilla[f"{BASE_PATH}.uexp"],
        tku[f"{BASE_PATH}.uasset"],
    )

    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)
    (OUTPUT_ROOT / "Paks").mkdir(parents=True, exist_ok=True)
    output_files = [
        (f"{BASE_PATH}.uasset", patched_uasset),
        (f"{BASE_PATH}.uexp", patched_uexp),
    ]
    pak_size = build_pak(output_files, OUTPUT_PAK)
    OUTPUT_MOD_JSON.write_text(
        json.dumps(
            {
                "displayName": "TKU Evidence Current Pawn Bounds",
                "version": "0.1.0-evidence",
                "buildNumber": 1,
                "description": (
                    "Narrow evidence patch made from the current vanilla StarMapPawn. It preserves modern "
                    "widget/tooltip references and changes only serialized bounds/zoom defaults toward TKU values."
                ),
                "author": "local evidence rebuild",
                "authorURL": "",
                "defaultLoadOrder": 96,
                "gameVersion": "1.13.378",
                "manifest": [],
                "steamPublishedFileId": 0,
                "steamLastSubmittedBuildNumber": 0,
                "steamModVisibility": "Private",
            },
            indent=3,
        )
        + "\n",
        encoding="utf-8",
    )

    return {
        "output_mod_name": OUTPUT_MOD_NAME,
        "output_root": str(OUTPUT_ROOT),
        "output_pak": str(OUTPUT_PAK),
        "output_pak_sha256": sha256(OUTPUT_PAK),
        "output_pak_size": pak_size,
        "vanilla_pak": str(VANILLA_PAK),
        "vanilla_pak_sha256": sha256(VANILLA_PAK),
        "original_tku_pak": str(ORIGINAL_TKU_PAK),
        "original_tku_pak_sha256": sha256(ORIGINAL_TKU_PAK),
        "target_paths": sorted(TARGET_PATHS),
        "patch_report": patch_report,
        "expected_runtime_meaning": {
            "success": "Career loads, starmap opens normally, and map bounds/zoom expand.",
            "no_bounds_change": "Bounds are likely controlled outside StarMapPawn CDO defaults.",
            "crash_or_starmap_button_failure": "Manual current-package CDO patch is unsafe; disable this mod and return to core-only baseline.",
        },
    }


def write_report(report: dict[str, Any]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")
    patch = report["patch_report"]
    lines = [
        "# TKU Evidence Current Pawn Bounds Patch - 2026-05-10",
        "",
        "## Purpose",
        "",
        "Retest expanded map bounds without restoring old TKU `StarMapPawn` behavior.",
        "",
        "The prior `TKUEvidenceBoundsPawn` restored the old cooked TKU pawn wholesale. It let the career load, but pressing the starmap button dropped to first-person hangar view instead of opening the starmap. That rules out the old pawn as a safe runtime asset.",
        "",
        "This patch starts from the current vanilla `StarMapPawn` package and changes only serialized CDO defaults needed for the bounds hypothesis.",
        "",
        "## Changes",
        "",
        f"- Added current-package name-map entries: `{patch['added_names']}`",
        f"- Added `PanBoundsVertical`: `{patch['after_values']['PanBoundsVertical']}`",
        f"- Added `PanBoundsHorizontal`: `{patch['after_values']['PanBoundsHorizontal']}`",
        f"- Replaced `ZoomDistanceList`: `{patch['before_values']['ZoomDistanceList']}` -> `{patch['after_values']['ZoomDistanceList']}`",
        f"- Replaced `ZoomLevelThresholds`: `{patch['before_values']['ZoomLevelThresholds']}` -> `{patch['after_values']['ZoomLevelThresholds']}`",
        f"- Current package CDO byte delta: `{patch['cdo_delta']}`",
        f"- Current package name-map byte delta: `{patch['name_delta']}`",
        "",
        "## Safety Boundary",
        "",
        "- Keeps the current `/Game/UI/FrontEnd/StarMapPawn` package and current widget/tooltip references.",
        "- Does not restore TKU `StarMap.umap`, `StarMapActor`, `StarSystemBody`, `BaseStarMapBorderActor`, dated border actors, root data tables, employers, or factions.",
        "- Still a cooked-package evidence patch, not the final preferred editor-authored asset.",
        "",
        "## Build Output",
        "",
        f"- Output mod: `{report['output_root']}`",
        f"- Output pak: `{report['output_pak']}`",
        f"- Output pak SHA256: `{report['output_pak_sha256']}`",
        "",
        "## Expected Runtime Meaning",
        "",
    ]
    for key, value in report["expected_runtime_meaning"].items():
        lines.append(f"- `{key}`: {value}")
    lines.extend(
        [
            "",
            "## Rollback",
            "",
            "Disable `TKUEvidenceCurrentPawnBounds`. The stable floor remains `TKUEvidenceCorePluginOnly` alone.",
            "",
        ]
    )
    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    report = build()
    write_report(report)
    print(f"Wrote {OUTPUT_MOD_JSON}")
    print(f"Wrote {OUTPUT_PAK}")
    print(f"Wrote {REPORT_MD}")
    print(f"Wrote {REPORT_JSON}")


if __name__ == "__main__":
    main()
