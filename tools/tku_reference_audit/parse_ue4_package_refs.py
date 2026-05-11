from __future__ import annotations

import argparse
import json
import struct
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
sys.path.insert(0, str(TOOLS_ROOT))

from mw5_pak import extract_exact_paths, iter_entries  # noqa: E402

UE_ASSET_MAGIC = 0x9E2A83C1

SOURCE_PAKS = {
    "vanilla_game": WORKSPACE / "MW5Mercs" / "Content" / "Paks" / "MW5Mercs-WindowsNoEditor.pak",
    "required_loose_override": WORKSPACE / "MW5Mercs" / "Content" / "Paks" / "MW5Mercs-zKnownUniverseStarmap.pak",
    "original_tku_mod": WORKSPACE / "MW5Mercs" / "Mods" / "TheKnownUniverse" / "Paks" / "TheKnownUniverse.pak",
}

TARGET_BASES = [
    "/Game/Levels/FrontEnd/StarMap",
    "/Game/UI/FrontEnd/Starmap/StarMapActor",
    "/Game/UI/FrontEnd/StarMapPawn",
    "/Game/UI/FrontEnd/Starmap/StarSystemBody",
    "/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor",
    "/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges",
    "/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015",
    "/Game/InnerSphereData/MW5_InnerSphereData",
    "/Game/InnerSphereData/Updated/EmployerInfoData",
    "/Game/InnerSphereData/Updated/SystemFactionChanges",
    "/Game/Campaign/Personas/ProcMissionPersonas/PersonaAnonymousEmployer",
    "/Game/Campaign/Personas/ProcMissionPersonas/PersonaAnonymousEmployer2",
]

HIGH_SIGNAL_PREFIXES = (
    "/Game/Levels/FrontEnd",
    "/Game/UI/FrontEnd/Starmap",
    "/Game/UI/FrontEnd/StarMapPawn",
    "/Game/InnerSphereData",
    "/Game/Campaign/CampaignArcs/BorderChanges",
    "/Game/Campaign/Clusters",
    "/Game/Campaign/Personas/ProcMissionPersonas",
    "/Game/Employers",
    "/Game/Factions",
    "/Plugins/TheKnownUniverse",
    "/ModOverride/TheKnownUniverse",
    "/Script/MechWarrior",
)

NATIVE_CLASS_NAMES = {
    "MWInnerSphereData",
    "MWStarMap",
    "MWStarMapPawn",
    "MWStarSystemBody",
    "MWStarMapBorderActor",
    "MWStarMapBorderAsset",
    "MWStarMapModel",
    "MWClusterDataAsset",
    "MWEmployerData",
    "MWFactionData",
}


class PackageParseError(ValueError):
    pass


@dataclass(frozen=True)
class FName:
    name: str
    number: int = 0

    def display(self) -> str:
        if self.number:
            return f"{self.name}#{self.number}"
        return self.name


@dataclass(frozen=True)
class PackageImport:
    index: int
    class_package: FName
    class_name: FName
    outer_index: int
    object_name: FName


@dataclass(frozen=True)
class PackageExport:
    index: int
    class_index: int
    super_index: int
    template_index: int
    outer_index: int
    object_name: FName
    object_flags: int
    serial_size: int
    serial_offset: int


class Reader:
    def __init__(self, data: bytes) -> None:
        self.data = data

    def _check(self, pos: int, size: int) -> None:
        if pos < 0 or pos + size > len(self.data):
            raise PackageParseError(f"read outside payload at {pos}+{size} / {len(self.data)}")

    def i32(self, pos: int) -> int:
        self._check(pos, 4)
        return struct.unpack_from("<i", self.data, pos)[0]

    def u32(self, pos: int) -> int:
        self._check(pos, 4)
        return struct.unpack_from("<I", self.data, pos)[0]

    def i64(self, pos: int) -> int:
        self._check(pos, 8)
        return struct.unpack_from("<q", self.data, pos)[0]

    def fstr(self, pos: int) -> tuple[str, int]:
        length = self.i32(pos)
        pos += 4
        if length == 0:
            return "", pos
        if length > 0:
            byte_count = length
            self._check(pos, byte_count)
            raw = self.data[pos : pos + byte_count]
            return raw.rstrip(b"\x00").decode("utf-8", "replace"), pos + byte_count
        byte_count = -length * 2
        self._check(pos, byte_count)
        raw = self.data[pos : pos + byte_count]
        return raw.rstrip(b"\x00").decode("utf-16-le", "replace"), pos + byte_count


def read_fname(reader: Reader, names: list[str], pos: int) -> FName:
    index = reader.i32(pos)
    number = reader.i32(pos + 4)
    if 0 <= index < len(names):
        name = names[index]
    else:
        name = f"<bad-name-index:{index}>"
    return FName(name, number)


def parse_summary(reader: Reader) -> dict[str, Any]:
    if reader.u32(0) != UE_ASSET_MAGIC:
        raise PackageParseError("missing UE asset magic")
    pos = 4
    legacy_file_version = reader.i32(pos)
    pos += 4
    legacy_ue3_version = reader.i32(pos)
    pos += 4
    file_version_ue4 = reader.i32(pos)
    pos += 4
    file_version_licensee_ue4 = reader.i32(pos)
    pos += 4
    custom_version_count = reader.i32(pos)
    pos += 4
    if custom_version_count < 0 or custom_version_count > 512:
        raise PackageParseError(f"implausible custom version count: {custom_version_count}")
    pos += custom_version_count * 20
    total_header_size = reader.i32(pos)
    pos += 4
    package_name, pos = reader.fstr(pos)
    package_flags = reader.u32(pos)
    pos += 4

    fields: dict[str, int] = {}
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
        fields[name] = reader.i32(pos)
        pos += 4

    guid = reader.data[pos : pos + 16].hex()
    pos += 16
    generation_count = reader.i32(pos)
    pos += 4
    generations: list[dict[str, int]] = []
    if 0 <= generation_count <= 1024:
        for _ in range(generation_count):
            generations.append({"export_count": reader.i32(pos), "name_count": reader.i32(pos + 4)})
            pos += 8

    return {
        "legacy_file_version": legacy_file_version,
        "legacy_ue3_version": legacy_ue3_version,
        "file_version_ue4": file_version_ue4,
        "file_version_licensee_ue4": file_version_licensee_ue4,
        "custom_version_count": custom_version_count,
        "total_header_size": total_header_size,
        "package_name": package_name,
        "package_flags_hex": f"0x{package_flags:08x}",
        "guid": guid,
        "generation_count": generation_count,
        "generations": generations,
        **fields,
    }


def parse_names(reader: Reader, summary: dict[str, Any]) -> list[str]:
    names: list[str] = []
    pos = int(summary["name_offset"])
    for _ in range(int(summary["name_count"])):
        name, pos = reader.fstr(pos)
        pos += 4
        names.append(name)
    return names


def parse_imports(reader: Reader, names: list[str], summary: dict[str, Any]) -> list[PackageImport]:
    imports: list[PackageImport] = []
    pos = int(summary["import_offset"])
    for index in range(int(summary["import_count"])):
        imports.append(
            PackageImport(
                index=index,
                class_package=read_fname(reader, names, pos),
                class_name=read_fname(reader, names, pos + 8),
                outer_index=reader.i32(pos + 16),
                object_name=read_fname(reader, names, pos + 20),
            )
        )
        pos += 28
    return imports


def parse_exports(reader: Reader, names: list[str], summary: dict[str, Any]) -> list[PackageExport]:
    exports: list[PackageExport] = []
    export_count = int(summary["export_count"])
    if export_count <= 0:
        return exports
    export_offset = int(summary["export_offset"])
    depends_offset = int(summary["depends_offset"])
    if depends_offset <= export_offset:
        raise PackageParseError("depends offset does not follow export map")
    stride = (depends_offset - export_offset) // export_count
    if stride < 44:
        raise PackageParseError(f"implausible export stride: {stride}")
    pos = export_offset
    for index in range(export_count):
        exports.append(
            PackageExport(
                index=index,
                class_index=reader.i32(pos),
                super_index=reader.i32(pos + 4),
                template_index=reader.i32(pos + 8),
                outer_index=reader.i32(pos + 12),
                object_name=read_fname(reader, names, pos + 16),
                object_flags=reader.u32(pos + 24),
                serial_size=reader.i64(pos + 28),
                serial_offset=reader.i64(pos + 36),
            )
        )
        pos += stride
    return exports


def ref_kind(index: int) -> str:
    if index == 0:
        return "null"
    if index < 0:
        return "import"
    return "export"


def ref_display(index: int, imports: list[PackageImport], exports: list[PackageExport]) -> str:
    if index == 0:
        return "None"
    if index < 0:
        import_index = -index - 1
        if 0 <= import_index < len(imports):
            item = imports[import_index]
            return f"Import[{import_index}] {item.object_name.display()} ({item.class_package.display()}::{item.class_name.display()})"
        return f"Import[bad:{import_index}]"
    export_index = index - 1
    if 0 <= export_index < len(exports):
        item = exports[export_index]
        return f"Export[{export_index}] {item.object_name.display()}"
    return f"Export[bad:{export_index}]"


def resolve_import_path(index: int, imports: list[PackageImport], depth: int = 0) -> str:
    if depth > 20 or index < 0 or index >= len(imports):
        return ""
    item = imports[index]
    outer = item.outer_index
    if outer < 0:
        outer_path = resolve_import_path(-outer - 1, imports, depth + 1)
        if outer_path:
            separator = "." if outer_path.startswith("/") else "/"
            return f"{outer_path}{separator}{item.object_name.display()}"
    if outer == 0:
        return item.object_name.display()
    return item.object_name.display()


def import_to_dict(item: PackageImport, imports: list[PackageImport]) -> dict[str, Any]:
    return {
        "index": item.index,
        "class_package": item.class_package.display(),
        "class_name": item.class_name.display(),
        "outer_index": item.outer_index,
        "outer_kind": ref_kind(item.outer_index),
        "object_name": item.object_name.display(),
        "resolved_path": resolve_import_path(item.index, imports),
    }


def export_to_dict(item: PackageExport, imports: list[PackageImport], exports: list[PackageExport]) -> dict[str, Any]:
    return {
        "index": item.index,
        "object_name": item.object_name.display(),
        "class": ref_display(item.class_index, imports, exports),
        "super": ref_display(item.super_index, imports, exports),
        "template": ref_display(item.template_index, imports, exports),
        "outer": ref_display(item.outer_index, imports, exports),
        "object_flags_hex": f"0x{item.object_flags:08x}",
        "serial_size": item.serial_size,
        "serial_offset": item.serial_offset,
    }


def package_refs(imports: list[PackageImport]) -> list[str]:
    refs: set[str] = set()
    for item in imports:
        for value in (item.class_package.display(), item.object_name.display(), resolve_import_path(item.index, imports)):
            if value.startswith(("/Game/", "/Plugins/", "/Script/", "/ModOverride/")):
                refs.add(value)
    return sorted(refs, key=str.lower)


def high_signal_refs(refs: list[str]) -> list[str]:
    return [ref for ref in refs if ref.startswith(HIGH_SIGNAL_PREFIXES)]


def native_class_refs(imports: list[PackageImport], exports: list[PackageExport]) -> list[str]:
    refs: set[str] = set()
    for item in imports:
        if item.class_package.display() == "/Script/MechWarrior" or item.object_name.name in NATIVE_CLASS_NAMES:
            refs.add(f"Import[{item.index}] {item.object_name.display()} ({item.class_package.display()}::{item.class_name.display()})")
    for item in exports:
        rendered = export_to_dict(item, imports, exports)
        if any(token in rendered["class"] or token in rendered["super"] or token in rendered["template"] for token in NATIVE_CLASS_NAMES):
            refs.add(
                f"Export[{item.index}] {item.object_name.display()} class={rendered['class']} super={rendered['super']} template={rendered['template']}"
            )
    return sorted(refs, key=str.lower)


def key_exports(exports: list[PackageExport], imports: list[PackageImport]) -> list[dict[str, Any]]:
    selected: list[PackageExport] = []
    for item in exports:
        name = item.object_name.name
        class_text = ref_display(item.class_index, imports, exports)
        super_text = ref_display(item.super_index, imports, exports)
        if (
            name.endswith("_C")
            or name.startswith("Default__")
            or "StarMap" in name
            or "Border" in name
            or "Faction" in name
            or "Career" in name
            or "MW" in class_text
            or "MW" in super_text
        ):
            selected.append(item)
    return [export_to_dict(item, imports, exports) for item in selected[:120]]


def parse_package(payload: bytes) -> dict[str, Any]:
    reader = Reader(payload)
    summary = parse_summary(reader)
    names = parse_names(reader, summary)
    imports = parse_imports(reader, names, summary)
    exports = parse_exports(reader, names, summary)
    refs = package_refs(imports)
    return {
        "summary": summary,
        "name_sample": names[:80],
        "package_refs": refs,
        "high_signal_refs": high_signal_refs(refs),
        "native_class_refs": native_class_refs(imports, exports),
        "imports": [import_to_dict(item, imports) for item in imports],
        "key_exports": key_exports(exports, imports),
        "export_names": [item.object_name.display() for item in exports],
    }


def find_asset_payloads(pak_path: Path, target_bases: list[str]) -> dict[str, dict[str, Any]]:
    _, _, entries = iter_entries(pak_path)
    wanted_paths: set[str] = set()
    base_to_payload_path: dict[str, str] = {}
    sidecars_by_base: dict[str, list[str]] = {base: [] for base in target_bases}
    for base in target_bases:
        for entry in entries:
            if entry.base_game_path.lower() != base.lower():
                continue
            sidecars_by_base[base].append(entry.game_path)
            if entry.extension in {".uasset", ".umap"}:
                wanted_paths.add(entry.game_path)
                base_to_payload_path[base] = entry.game_path
    extracted = extract_exact_paths(pak_path, wanted_paths)
    result: dict[str, dict[str, Any]] = {}
    for base in target_bases:
        payload_path = base_to_payload_path.get(base)
        result[base] = {
            "sidecars": sorted(sidecars_by_base.get(base, []), key=str.lower),
            "payload_path": payload_path,
            "payload": extracted.get(payload_path, b"") if payload_path else b"",
        }
    return result


def diff_list(left: list[str], right: list[str]) -> dict[str, list[str]]:
    left_set = set(left)
    right_set = set(right)
    return {
        "only_left": sorted(left_set - right_set, key=str.lower),
        "only_right": sorted(right_set - left_set, key=str.lower),
        "common": sorted(left_set & right_set, key=str.lower),
    }


def make_report(args: argparse.Namespace) -> dict[str, Any]:
    sources: dict[str, Any] = {}
    for source_name, pak_path in SOURCE_PAKS.items():
        if not pak_path.exists():
            sources[source_name] = {"pak_path": str(pak_path), "exists": False, "assets": {}}
            continue
        assets = find_asset_payloads(pak_path, TARGET_BASES)
        parsed_assets: dict[str, Any] = {}
        for base, item in assets.items():
            payload = item.pop("payload")
            asset_record: dict[str, Any] = {
                "sidecars": item["sidecars"],
                "payload_path": item["payload_path"],
                "status": "missing" if not payload else "parsed",
            }
            if payload:
                try:
                    parsed = parse_package(payload)
                    asset_record.update(parsed)
                except Exception as exc:  # noqa: BLE001 - report parse failures as evidence.
                    asset_record["status"] = "parse_error"
                    asset_record["error"] = str(exc)
            parsed_assets[base] = asset_record
        sources[source_name] = {"pak_path": str(pak_path), "exists": True, "assets": parsed_assets}

    comparisons: dict[str, Any] = {}
    vanilla_assets = sources.get("vanilla_game", {}).get("assets", {})
    tku_assets = sources.get("original_tku_mod", {}).get("assets", {})
    loose_assets = sources.get("required_loose_override", {}).get("assets", {})
    for base in TARGET_BASES:
        vanilla = vanilla_assets.get(base, {})
        tku = tku_assets.get(base, {})
        loose = loose_assets.get(base, {})
        comparisons[base] = {
            "vanilla_vs_tku_high_signal_refs": diff_list(
                vanilla.get("high_signal_refs", []), tku.get("high_signal_refs", [])
            ),
            "vanilla_vs_tku_export_names": diff_list(vanilla.get("export_names", []), tku.get("export_names", [])),
            "loose_vs_tku_high_signal_refs": diff_list(loose.get("high_signal_refs", []), tku.get("high_signal_refs", [])),
        }

    return {
        "source_note": (
            "Read-only UE4 cooked package reference parse. This inspects uasset/umap headers, name maps, imports, "
            "exports, and hard package references; it does not decode Blueprint bytecode or DataTable row payloads."
        ),
        "target_bases": TARGET_BASES,
        "sources": sources,
        "comparisons": comparisons,
    }


def asset_brief(source_name: str, base: str, asset: dict[str, Any]) -> list[str]:
    lines: list[str] = []
    status = asset.get("status", "missing")
    lines.append(f"### `{source_name}` `{base}`")
    lines.append("")
    lines.append(f"- status: `{status}`")
    if asset.get("payload_path"):
        lines.append(f"- payload: `{asset['payload_path']}`")
    if asset.get("sidecars"):
        lines.append(f"- sidecars: `{', '.join(asset['sidecars'])}`")
    if status != "parsed":
        if asset.get("error"):
            lines.append(f"- error: `{asset['error']}`")
        lines.append("")
        return lines
    summary = asset["summary"]
    lines.append(
        "- summary: "
        f"names `{summary['name_count']}`, imports `{summary['import_count']}`, exports `{summary['export_count']}`, "
        f"package flags `{summary['package_flags_hex']}`"
    )
    if asset.get("native_class_refs"):
        lines.append("- native class refs:")
        for ref in asset["native_class_refs"][:16]:
            lines.append(f"- `{ref}`")
    if asset.get("high_signal_refs"):
        lines.append("- high-signal hard refs:")
        for ref in asset["high_signal_refs"][:40]:
            lines.append(f"- `{ref}`")
    if asset.get("key_exports"):
        lines.append("- key exports:")
        for export in asset["key_exports"][:30]:
            lines.append(f"- `{export['object_name']}` class `{export['class']}` super `{export['super']}`")
    lines.append("")
    return lines


def markdown(report: dict[str, Any]) -> str:
    lines = [
        "# TKU Cooked Package Reference Parse",
        "",
        report["source_note"],
        "",
        "## Key Interpretation",
        "",
        "- This report is stronger than string scanning because imports and exports come from UE package tables.",
        "- It still cannot prove Blueprint runtime control flow or decode DataTable rows; that remains editor/tool work.",
        "- Evidence here should gate any next rebuild. If a suspected replacement is not visible in import/export tables, do not build around that suspicion.",
        "",
        "## Source Paks",
        "",
    ]
    for source_name, source in report["sources"].items():
        lines.append(f"- `{source_name}`: `{source['pak_path']}` exists `{source['exists']}`")
    lines.extend(["", "## Highest Signal Assets", ""])

    focus = [
        "/Game/Levels/FrontEnd/StarMap",
        "/Game/UI/FrontEnd/Starmap/StarMapActor",
        "/Game/UI/FrontEnd/Starmap/StarSystemBody",
        "/Game/UI/FrontEnd/StarMapPawn",
        "/Game/InnerSphereData/MW5_InnerSphereData",
        "/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor",
    ]
    for base in focus:
        for source_name in ("required_loose_override", "original_tku_mod", "vanilla_game"):
            asset = report["sources"].get(source_name, {}).get("assets", {}).get(base, {})
            lines.extend(asset_brief(source_name, base, asset))

    lines.extend(["## Comparison Diffs", ""])
    for base, comparison in report["comparisons"].items():
        diff_refs = comparison["vanilla_vs_tku_high_signal_refs"]
        diff_exports = comparison["vanilla_vs_tku_export_names"]
        if not diff_refs["only_left"] and not diff_refs["only_right"] and not diff_exports["only_left"] and not diff_exports["only_right"]:
            continue
        lines.append(f"### `{base}`")
        lines.append("")
        if diff_refs["only_right"]:
            lines.append("- high-signal refs only in TKU:")
            for ref in diff_refs["only_right"][:50]:
                lines.append(f"- `{ref}`")
        if diff_refs["only_left"]:
            lines.append("- high-signal refs only in vanilla:")
            for ref in diff_refs["only_left"][:50]:
                lines.append(f"- `{ref}`")
        if diff_exports["only_right"]:
            lines.append("- export names only in TKU:")
            for ref in diff_exports["only_right"][:50]:
                lines.append(f"- `{ref}`")
        if diff_exports["only_left"]:
            lines.append("- export names only in vanilla:")
            for ref in diff_exports["only_left"][:50]:
                lines.append(f"- `{ref}`")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", type=Path, default=REPORTS_DIR / "tku_editor_first")
    args = parser.parse_args()

    report = make_report(args)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    json_path = args.out_dir / "tku_cooked_package_refs.json"
    md_path = args.out_dir / "tku_cooked_package_refs.md"
    json_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    md_path.write_text(markdown(report), encoding="utf-8")
    print(json_path)
    print(md_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
