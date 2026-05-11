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
from parse_ue4_package_refs import (
    Reader,
    high_signal_refs,
    package_refs,
    parse_exports,
    parse_imports,
    parse_names,
    parse_summary,
)


from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
SOURCE_MOD = WORKSPACE / "MW5Mercs" / "Mods" / "TheKnownUniverse"
SOURCE_PAK = SOURCE_MOD / "Paks" / "TheKnownUniverse.pak"
SOURCE_MOD_JSON = SOURCE_MOD / "mod.json"
SOURCE_RESOURCES = SOURCE_MOD / "Resources"

OUTPUT_MOD_NAME = "TKUEvidenceBoundsPawn"
OUTPUT_ROOT = WORKSPACE / "MW5Mercs" / "Mods" / OUTPUT_MOD_NAME
OUTPUT_PAK = OUTPUT_ROOT / "Paks" / f"{OUTPUT_MOD_NAME}.pak"
OUTPUT_MOD_JSON = OUTPUT_ROOT / "mod.json"
OUTPUT_RESOURCES = OUTPUT_ROOT / "Resources"

REPORT_DIR = REPORTS_DIR / "tku_editor_first"
REPORT_MD = REPORT_DIR / "tku_evidence_bounds_pawn_20260510.md"
REPORT_JSON = REPORT_DIR / "tku_evidence_bounds_pawn_20260510.json"

TARGET_PATHS = {
    "/Game/UI/FrontEnd/StarMapPawn.uasset",
    "/Game/UI/FrontEnd/StarMapPawn.uexp",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest().upper()


def read_fname_index(data: bytes, pos: int, names: list[str]) -> tuple[str, int, int]:
    name_index = struct.unpack_from("<i", data, pos)[0]
    number = struct.unpack_from("<i", data, pos + 4)[0]
    if 0 <= name_index < len(names):
        name = names[name_index]
    else:
        name = f"<bad-name-index:{name_index}>"
    return name, number, pos + 8


def recover_cdo_defaults(uasset: bytes, uexp: bytes) -> dict[str, Any]:
    reader = Reader(uasset)
    summary = parse_summary(reader)
    names = parse_names(reader, summary)
    imports = parse_imports(reader, names, summary)
    exports = parse_exports(reader, names, summary)
    default_export = next((item for item in exports if item.object_name.name == "Default__StarMapPawn_C"), None)
    if default_export is None:
        return {"error": "Default__StarMapPawn_C export not found"}

    start = default_export.serial_offset - len(uasset)
    end = start + default_export.serial_size
    if start < 0 or end > len(uexp):
        return {
            "error": "Default__StarMapPawn_C export serial range is outside uexp",
            "serial_offset": default_export.serial_offset,
            "serial_size": default_export.serial_size,
            "uasset_len": len(uasset),
            "uexp_len": len(uexp),
        }

    pos = start
    values: dict[str, Any] = {}
    tags: list[dict[str, Any]] = []
    while pos + 8 <= end:
        prop_name, prop_number, pos = read_fname_index(uexp, pos, names)
        if prop_name == "None":
            tags.append({"name": "None", "offset": pos - 8})
            break
        prop_type, prop_type_number, pos = read_fname_index(uexp, pos, names)
        if pos + 8 > end:
            tags.append({"name": prop_name, "error": "truncated property tag header"})
            break
        size = struct.unpack_from("<i", uexp, pos)[0]
        array_index = struct.unpack_from("<i", uexp, pos + 4)[0]
        inner_type = None
        if prop_type == "ArrayProperty":
            inner_type, _, after_inner_type = read_fname_index(uexp, pos + 8, names)
            has_property_guid = uexp[after_inner_type]
            value_pos = after_inner_type + 1
        else:
            has_property_guid = uexp[pos + 8]
            value_pos = pos + 9
        value_end = value_pos + size
        tag: dict[str, Any] = {
            "name": prop_name,
            "name_number": prop_number,
            "type": prop_type,
            "type_number": prop_type_number,
            "size": size,
            "array_index": array_index,
            "has_property_guid": bool(has_property_guid),
            "offset": pos - 16,
        }
        if inner_type:
            tag["inner_type"] = inner_type
        if value_end > end or size < 0:
            tag["error"] = "invalid property value range"
            tags.append(tag)
            break
        if prop_type == "FloatProperty" and size == 4:
            value = struct.unpack_from("<f", uexp, value_pos)[0]
            tag["value"] = value
            values[prop_name] = value
        elif prop_type == "ArrayProperty" and size >= 4:
            count = struct.unpack_from("<i", uexp, value_pos)[0]
            element_size = 4 + count * 4
            if count >= 0 and element_size == size and inner_type == "FloatProperty":
                array_values = [
                    struct.unpack_from("<f", uexp, value_pos + 4 + index * 4)[0]
                    for index in range(count)
                ]
                tag["value"] = array_values
                values[prop_name] = array_values
            elif count >= 0 and element_size == size and inner_type == "IntProperty":
                array_values = [
                    struct.unpack_from("<i", uexp, value_pos + 4 + index * 4)[0]
                    for index in range(count)
                ]
                tag["value"] = array_values
                values[prop_name] = array_values
            else:
                tag["array_count"] = count
        tags.append(tag)
        pos = value_end

    return {
        "summary": {
            "name_count": summary["name_count"],
            "import_count": summary["import_count"],
            "export_count": summary["export_count"],
            "package_flags_hex": summary["package_flags_hex"],
        },
        "high_signal_refs": high_signal_refs(package_refs(imports)),
        "exports": [
            {
                "object_name": item.object_name.display(),
                "serial_size": item.serial_size,
                "serial_offset": item.serial_offset,
            }
            for item in exports
        ],
        "recovered_default_values": values,
        "decoded_tags": tags,
    }


def build() -> dict[str, Any]:
    if not SOURCE_PAK.exists():
        raise FileNotFoundError(SOURCE_PAK)
    (OUTPUT_ROOT / "Paks").mkdir(parents=True, exist_ok=True)

    extracted = extract_exact_paths(SOURCE_PAK, TARGET_PATHS)
    missing = sorted(TARGET_PATHS - set(extracted))
    if missing:
        raise RuntimeError(f"missing StarMapPawn sidecars from original TKU pak: {missing}")

    if OUTPUT_PAK.exists():
        pak_size = OUTPUT_PAK.stat().st_size
    else:
        pak_size = build_pak(
            [(path, extracted[path]) for path in sorted(TARGET_PATHS)],
            OUTPUT_PAK,
        )

    if SOURCE_RESOURCES.exists():
        shutil.copytree(SOURCE_RESOURCES, OUTPUT_RESOURCES, dirs_exist_ok=True)

    original_mod_json = json.loads(SOURCE_MOD_JSON.read_text(encoding="utf-8"))
    mod_json = {
        "displayName": "TKU Evidence Bounds Pawn",
        "version": "0.1.0-evidence",
        "buildNumber": 1,
        "description": (
            "Narrow evidence patch that restores only TKU's cooked StarMapPawn defaults on top of "
            "the stable TKUEvidenceCorePluginOnly baseline. This tests expanded starmap pan/zoom "
            "bounds only; it does not attempt to restore territory overlay or border actors."
        ),
        "author": f"{original_mod_json.get('author', 'TePa')} / local evidence rebuild",
        "authorURL": original_mod_json.get("authorURL", ""),
        "defaultLoadOrder": 95,
        "gameVersion": "1.13.378",
        "manifest": [],
        "steamPublishedFileId": 0,
        "steamLastSubmittedBuildNumber": 0,
        "steamModVisibility": "Private",
    }
    OUTPUT_MOD_JSON.write_text(json.dumps(mod_json, indent=3) + "\n", encoding="utf-8")

    decoded_defaults = recover_cdo_defaults(
        extracted["/Game/UI/FrontEnd/StarMapPawn.uasset"],
        extracted["/Game/UI/FrontEnd/StarMapPawn.uexp"],
    )

    return {
        "output_mod_name": OUTPUT_MOD_NAME,
        "source_mod": str(SOURCE_MOD),
        "source_pak": str(SOURCE_PAK),
        "source_pak_sha256": sha256(SOURCE_PAK),
        "output_root": str(OUTPUT_ROOT),
        "output_pak": str(OUTPUT_PAK),
        "output_pak_sha256": sha256(OUTPUT_PAK),
        "output_pak_size": pak_size,
        "target_paths": sorted(TARGET_PATHS),
        "decoded_starmap_pawn_defaults": decoded_defaults,
        "expected_runtime_meaning": {
            "success": (
                "Career still loads and the starmap can pan/zoom beyond vanilla bounds. This validates "
                "StarMapPawn defaults as the bounds source and leaves overlay as a separate cluster-data problem."
            ),
            "no_bounds_change": (
                "Bounds are controlled elsewhere, likely StarMap level actors or StarMapActor logic, and "
                "StarMapPawn should be removed again."
            ),
            "crash_or_stall": (
                "Even though package tables looked compatible, the old cooked StarMapPawn is not safe; disable "
                "this patch and recreate the defaults in the editor/current asset pipeline."
            ),
        },
    }


def write_report(report: dict[str, Any]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")

    defaults = report["decoded_starmap_pawn_defaults"].get("recovered_default_values", {})
    zoom = defaults.get("ZoomDistanceList", [])
    thresholds = defaults.get("ZoomLevelThresholds", [])
    lines = [
        "# TKU Evidence Bounds Pawn Patch - 2026-05-10",
        "",
        "## Purpose",
        "",
        "Test exactly one remaining runtime symptom: the vanilla-width starmap bounds observed after the stable core-plugin-only run.",
        "",
        "This patch is deliberately narrow. It restores only original TKU build-38 `/Game/UI/FrontEnd/StarMapPawn.uasset` and `.uexp` on top of `TKUEvidenceCorePluginOnly`.",
        "",
        "## Evidence Gate",
        "",
        "- User runtime evidence: `TKUEvidenceCorePluginOnly` loads successfully, but starmap panning remains bounded by vanilla limits.",
        "- Current editor default evidence: vanilla `StarMapPawn` has `PanBoundsHorizontal=5500`, `PanBoundsVertical=4500`, and zoom distances ending at `3500`.",
        "- Cooked package-table evidence: original TKU `StarMapPawn` and current vanilla `StarMapPawn` have matching import/export structure and both inherit native `/Script/MechWarrior.MWStarMapPawn`.",
        "- Recovered cooked CDO values show TKU changes only the expected pan/zoom defaults for this hypothesis.",
        "- The patch does not restore TKU `StarMap.umap`, `StarMapActor`, `StarSystemBody`, `BaseStarMapBorderActor`, dated border actors, faction/employer data, or root data tables.",
        "",
        "## Recovered TKU Defaults",
        "",
        f"- `PanBoundsHorizontal`: `{defaults.get('PanBoundsHorizontal')}`",
        f"- `PanBoundsVertical`: `{defaults.get('PanBoundsVertical')}`",
        f"- `ZoomDistanceList`: `{zoom}`",
        f"- `ZoomLevelThresholds`: `{thresholds}`",
        "",
        "## Build Output",
        "",
        f"- Output mod: `{report['output_root']}`",
        f"- Output pak: `{report['output_pak']}`",
        f"- Output pak SHA256: `{report['output_pak_sha256']}`",
        f"- Source pak SHA256: `{report['source_pak_sha256']}`",
        f"- Pak entries: `{len(report['target_paths'])}`",
        "",
        "## Expected Runtime Meaning",
        "",
    ]
    for key, value in report["expected_runtime_meaning"].items():
        lines.append(f"- `{key}`: {value}")
    lines.extend(
        [
            "",
            "## What This Does Not Test",
            "",
            "- It does not fix the missing minor-power territory overlay.",
            "- It does not prove old TKU starmap classes are safe.",
            "- It does not authorize restoring old border actors or root faction/employer assets.",
            "",
            "## Rollback",
            "",
            "Disable `TKUEvidenceBoundsPawn` in `MW5Mercs\\Mods\\modlist.json`. `TKUEvidenceCorePluginOnly` remains the stable floor.",
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
