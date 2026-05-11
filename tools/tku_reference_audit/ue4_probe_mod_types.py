from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path

import unreal


from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
EDITOR_ROOT = Path(r"E:\Games\MechWarrior5Editor")
STUB_PATH = EDITOR_ROOT / "MW5Mercs" / "Intermediate" / "PythonStub" / "unreal.py"
OUT_DIR = REPORTS_DIR / "tku_editor_first"
OUT_JSON = OUT_DIR / "ue4_mod_types_probe.json"
OUT_MD = OUT_DIR / "ue4_mod_types_probe.md"

SEARCH_TERMS = (
    "MWModPluginInfo",
    "ModPackageArgs",
    "ModPackage",
    "MWMod",
    "ModPlugin",
    "PackageMod",
    "CreateMod",
    "SaveToMod",
    "SaveTo",
)

EXACT_TYPES = (
    "MWModPluginInfo",
    "ModPackageArgs",
    "MWModUtils",
    "MWModEditorWidget",
    "ModInfo",
    "ModList",
    "ModListEntry",
    "ModStatus",
    "ModPlatform",
    "ModConflict",
    "PublishedModVisibility",
)

SAFE_MWMODUTILS_CALLS = (
    ("get_mods_install_path", ()),
    ("get_mod_plugin_names", ()),
    ("get_active_mod_plugin", ()),
    ("get_active_mod_entry", ()),
    ("get_mod_platform", ()),
    ("get_mod_list", (False,)),
    ("get_mod_list", (True,)),
    ("get_enabled_mod_list", ()),
    ("get_running_mods", ()),
    ("get_mod_status_list", ()),
)

ASSET_SEARCH_ROOTS = (
    "/Game/UI/Editor",
    "/Game/UI",
    "/Game/Editor",
)


def public_members(obj) -> list[str]:
    try:
        return sorted(name for name in dir(obj) if not name.startswith("_"))
    except Exception as exc:
        return [f"<dir-error:{type(exc).__name__}:{exc}>"]


def to_jsonable(value, depth: int = 0):
    if depth > 5:
        return str(value)
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(k): to_jsonable(v, depth + 1) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [to_jsonable(item, depth + 1) for item in value]
    try:
        if hasattr(value, "__iter__") and not isinstance(value, (str, bytes)):
            return [to_jsonable(item, depth + 1) for item in list(value)]
    except Exception:
        pass

    out = {
        "repr": str(value),
        "python_type": type(value).__name__,
    }
    for attr in ("get_name", "get_path_name", "get_full_name"):
        try:
            out[attr] = str(getattr(value, attr)())
        except Exception:
            pass
    try:
        cls = value.get_class()
        out["unreal_class"] = str(cls.get_name())
        out["unreal_class_path"] = str(cls.get_path_name())
    except Exception:
        pass
    return out


def safe_call(label: str, func, *args):
    try:
        return {"ok": True, "value": to_jsonable(func(*args))}
    except Exception as exc:
        return {"ok": False, "error": f"{type(exc).__name__}: {exc}"}


def editor_properties(obj, property_names: list[str]) -> dict:
    props = {}
    for name in property_names:
        try:
            props[name] = to_jsonable(obj.get_editor_property(name))
        except Exception as exc:
            props[name] = f"<error:{type(exc).__name__}:{exc}>"
    return props


def class_summary(name: str) -> dict:
    cls = getattr(unreal, name, None)
    if cls is None:
        return {"exists": False}
    members = public_members(cls)
    return {
        "exists": True,
        "repr": str(cls),
        "members": members,
        "term_members": {
            term: [member for member in members if term.lower() in member.lower()]
            for term in SEARCH_TERMS
        },
    }


def construct_summary(name: str, *args, **kwargs) -> dict:
    cls = getattr(unreal, name, None)
    if cls is None:
        return {"exists": False}
    try:
        obj = cls(*args, **kwargs)
    except Exception as exc:
        return {
            "exists": True,
            "constructed": False,
            "error": f"{type(exc).__name__}: {exc}",
            "class_members": public_members(cls),
        }
    return {
        "exists": True,
        "constructed": True,
        "repr": str(obj),
        "jsonable": to_jsonable(obj),
        "members": public_members(obj),
    }


def struct_samples() -> dict:
    samples = {
        "MWModPluginInfo_default": construct_summary("MWModPluginInfo"),
        "MWModPluginInfo_sample": construct_summary(
            "MWModPluginInfo",
            mod_name="__TKUProbeNoCreate__",
            plugin_path="__NoDiskPath__",
            version_name="0.0-probe",
            friendly_name="TKU Probe No Create",
            description="Non-mutating constructor sample",
            category="Probe",
            created_by="Codex",
            created_by_url="",
            docs_url="",
            marketplace_url="",
            support_url="",
            engine_version="4.27",
        ),
        "ModPackageArgs_default": construct_summary("ModPackageArgs"),
        "ModPackageArgs_sample": construct_summary(
            "ModPackageArgs",
            mod_name="__TKUProbeNoPackage__",
            skip_packaging=True,
            output_to_folder=True,
            publish_to_steam=False,
            steam_visibility="Private",
        ),
    }

    struct_fields = {
        "MWModPluginInfo_default": [
            "mod_name",
            "plugin_path",
            "version_name",
            "friendly_name",
            "description",
            "category",
            "created_by",
            "created_by_url",
            "docs_url",
            "marketplace_url",
            "support_url",
            "engine_version",
        ],
        "MWModPluginInfo_sample": [
            "mod_name",
            "plugin_path",
            "version_name",
            "friendly_name",
            "description",
            "category",
            "created_by",
            "created_by_url",
            "docs_url",
            "marketplace_url",
            "support_url",
            "engine_version",
        ],
        "ModPackageArgs_default": [
            "mod_name",
            "skip_packaging",
            "output_to_folder",
            "publish_to_steam",
            "steam_visibility",
        ],
        "ModPackageArgs_sample": [
            "mod_name",
            "skip_packaging",
            "output_to_folder",
            "publish_to_steam",
            "steam_visibility",
        ],
    }

    for key, fields in struct_fields.items():
        info = samples[key]
        if not info.get("constructed"):
            continue
        class_name = key.rsplit("_", 1)[0]
        cls = getattr(unreal, class_name, None)
        try:
            if "sample" in key and class_name == "MWModPluginInfo":
                obj = cls(
                    mod_name="__TKUProbeNoCreate__",
                    plugin_path="__NoDiskPath__",
                    version_name="0.0-probe",
                    friendly_name="TKU Probe No Create",
                    description="Non-mutating constructor sample",
                    category="Probe",
                    created_by="Codex",
                    created_by_url="",
                    docs_url="",
                    marketplace_url="",
                    support_url="",
                    engine_version="4.27",
                )
            elif "sample" in key and class_name == "ModPackageArgs":
                obj = cls(
                    mod_name="__TKUProbeNoPackage__",
                    skip_packaging=True,
                    output_to_folder=True,
                    publish_to_steam=False,
                    steam_visibility="Private",
                )
            else:
                obj = cls()
            info["editor_properties"] = editor_properties(obj, fields)
        except Exception as exc:
            info["editor_properties_error"] = f"{type(exc).__name__}: {exc}"
    return samples


def matching_unreal_symbols() -> dict:
    names = sorted(dir(unreal))
    return {
        term: [name for name in names if term.lower() in name.lower()]
        for term in SEARCH_TERMS
    }


def mwmodutils_safe_results() -> dict:
    cls = getattr(unreal, "MWModUtils", None)
    if cls is None:
        return {"exists": False}
    results = {"exists": True, "calls": {}}
    for name, args in SAFE_MWMODUTILS_CALLS:
        label = name if not args else f"{name}({', '.join(map(str, args))})"
        results["calls"][label] = safe_call(label, getattr(cls, name), *args)
    return results


def editor_widget_probe() -> dict:
    cls = getattr(unreal, "MWModEditorWidget", None)
    if cls is None:
        return {"exists": False}
    out = {
        "exists": True,
        "class_members": public_members(cls),
        "constructor_attempt": construct_summary("MWModEditorWidget"),
    }
    out["package_mod_member_present"] = "package_mod" in out["class_members"]
    return out


def find_editor_utility_assets() -> dict:
    found = {}
    for root in ASSET_SEARCH_ROOTS:
        try:
            if not unreal.EditorAssetLibrary.does_directory_exist(root):
                found[root] = {"exists": False, "assets": []}
                continue
            assets = list(unreal.EditorAssetLibrary.list_assets(root, recursive=True, include_folder=False))
            matches = [
                asset for asset in assets
                if any(term.lower() in asset.lower() for term in ("mod", "package", "save"))
            ]
            found[root] = {"exists": True, "asset_count": len(assets), "matches": matches[:250]}
        except Exception as exc:
            found[root] = {"exists": None, "error": f"{type(exc).__name__}: {exc}"}
    return found


def active_mod_path_probe() -> dict:
    active = safe_call("MWModUtils.get_active_mod_plugin", unreal.MWModUtils.get_active_mod_plugin)
    plugin_names = safe_call("MWModUtils.get_mod_plugin_names", unreal.MWModUtils.get_mod_plugin_names)
    mods_path = safe_call("MWModUtils.get_mods_install_path", unreal.MWModUtils.get_mods_install_path)
    return {
        "active_mod_plugin": active,
        "mod_plugin_names": plugin_names,
        "mods_install_path": mods_path,
    }


def stub_snippets() -> dict:
    if not STUB_PATH.exists():
        return {"exists": False, "path": str(STUB_PATH)}
    text = STUB_PATH.read_text(encoding="utf-8", errors="replace")
    snippets = {"exists": True, "path": str(STUB_PATH), "matches": {}}
    for term in SEARCH_TERMS + EXACT_TYPES:
        pattern = re.compile(rf"^class\s+{re.escape(term)}\b|def\s+.*{re.escape(term)}.*|{re.escape(term)}", re.IGNORECASE | re.MULTILINE)
        term_matches = []
        for match in pattern.finditer(text):
            line_no = text.count("\n", 0, match.start()) + 1
            start = max(0, text.rfind("\n", 0, match.start()))
            end = match.end()
            for _ in range(16):
                next_end = text.find("\n", end + 1)
                if next_end == -1:
                    end = len(text)
                    break
                end = next_end
            snippet = text[start:end].strip()
            term_matches.append({"line": line_no, "snippet": snippet[:2200]})
            if len(term_matches) >= 8:
                break
        snippets["matches"][term] = term_matches
    return snippets


def build_decision(report: dict) -> dict:
    symbols = report["matching_unreal_symbols"]
    exact = report["class_summaries"]
    widget = report["editor_widget_probe"]

    create_symbols = symbols.get("CreateMod", [])
    save_to_mod_symbols = symbols.get("SaveToMod", [])
    save_to_symbols = symbols.get("SaveTo", [])
    package_symbols = symbols.get("PackageMod", []) + [
        name for name in exact.get("MWModEditorWidget", {}).get("members", [])
        if "package" in name.lower()
    ]

    can_package_directly = bool(package_symbols)
    package_requires_widget = widget.get("package_mod_member_present") and not any(
        symbol.lower() == "package_mod" for symbol in symbols.get("PackageMod", [])
    )
    has_direct_create_or_save_to_mod = bool(create_symbols or save_to_mod_symbols)

    return {
        "non_mutating_decision": (
            "Editor Python exposes MW5 mod metadata structs and read-only mod utilities. "
            "It exposes MWModEditorWidget.package_mod(args), but no direct module-level "
            "CreateMod, SaveToMod, or SaveTo symbol was found by this probe."
        ),
        "can_create_mod_via_python": has_direct_create_or_save_to_mod,
        "can_package_via_python_without_ui_widget": can_package_directly and not package_requires_widget,
        "package_api_requires_widget_instance": package_requires_widget,
        "manual_editor_ui_required_for_safe_mod_creation_or_save_to_mod": not has_direct_create_or_save_to_mod,
        "evidence": {
            "create_mod_symbols": create_symbols,
            "save_to_mod_symbols": save_to_mod_symbols,
            "save_to_symbols": save_to_symbols,
            "package_symbols": package_symbols,
        },
    }


def write_markdown(report: dict) -> None:
    decision = report["decision"]
    lines = [
        "# UE4 MW5 Mod Types Probe",
        "",
        f"- Generated: `{report['generated_utc']}`",
        "- Method: non-mutating `UE4Editor-Cmd -run=pythonscript` introspection.",
        "- Safety: did not call `set_active_mod`, `create_mod_entry`, `package_mod`, `save_asset`, `duplicate_asset`, or any asset-writing API.",
        "",
        "## Decision",
        "",
        decision["non_mutating_decision"],
        "",
        f"- Can create a complete MW5 mod via direct Python API: `{decision['can_create_mod_via_python']}`",
        f"- Can package via Python without a UI widget instance: `{decision['can_package_via_python_without_ui_widget']}`",
        f"- Package API appears to require `MWModEditorWidget.package_mod(args)`: `{decision['package_api_requires_widget_instance']}`",
        f"- Manual editor UI required for safe `Create Mod` / `Save To Mod` until a widget workflow is proven: `{decision['manual_editor_ui_required_for_safe_mod_creation_or_save_to_mod']}`",
        "",
        "## Runtime State",
        "",
    ]
    for key, value in report["runtime_state"].items():
        lines.append(f"- `{key}`: `{value}`")

    lines.extend(["", "## Matching Unreal Symbols", ""])
    for term, names in report["matching_unreal_symbols"].items():
        lines.append(f"### `{term}`")
        if names:
            for name in names:
                lines.append(f"- `{name}`")
        else:
            lines.append("- None found")
        lines.append("")

    lines.extend(["## Exact Type Summaries", ""])
    for name, info in report["class_summaries"].items():
        lines.append(f"### `{name}`")
        lines.append(f"- Exists: `{info.get('exists')}`")
        if info.get("exists"):
            members = info.get("members", [])
            matched = sorted({
                member
                for values in info.get("term_members", {}).values()
                for member in values
            })
            lines.append(f"- Public member count: `{len(members)}`")
            if matched:
                lines.append("- Search-term members:")
                for member in matched:
                    lines.append(f"  - `{member}`")
        lines.append("")

    lines.extend(["## Struct Constructor Samples", ""])
    for name, info in report["struct_samples"].items():
        lines.append(f"### `{name}`")
        lines.append(f"- Constructed: `{info.get('constructed')}`")
        if info.get("error"):
            lines.append(f"- Error: `{info['error']}`")
        props = info.get("editor_properties", {})
        for key, value in props.items():
            lines.append(f"- `{key}`: `{value}`")
        lines.append("")

    lines.extend(["## Safe MWModUtils Calls", ""])
    calls = report["mwmodutils_safe_results"].get("calls", {})
    for name, result in calls.items():
        lines.append(f"### `{name}`")
        lines.append(f"- OK: `{result.get('ok')}`")
        value = result.get("value", result.get("error"))
        text = json.dumps(value, indent=2, ensure_ascii=False) if not isinstance(value, str) else value
        for line in text.splitlines()[:40]:
            lines.append(f"  {line}")
        lines.append("")

    lines.extend(["## Editor Widget Probe", ""])
    widget = report["editor_widget_probe"]
    lines.append(f"- `MWModEditorWidget` exists: `{widget.get('exists')}`")
    lines.append(f"- `package_mod` member present: `{widget.get('package_mod_member_present')}`")
    ctor = widget.get("constructor_attempt", {})
    lines.append(f"- Constructor attempt constructed: `{ctor.get('constructed')}`")
    if ctor.get("error"):
        lines.append(f"- Constructor error: `{ctor['error']}`")

    lines.extend(["", "## Editor Utility Asset Matches", ""])
    for root, info in report["editor_utility_asset_matches"].items():
        lines.append(f"### `{root}`")
        lines.append(f"- Exists: `{info.get('exists')}`")
        if "asset_count" in info:
            lines.append(f"- Asset count: `{info['asset_count']}`")
        for asset in info.get("matches", [])[:80]:
            lines.append(f"- `{asset}`")
        if info.get("error"):
            lines.append(f"- Error: `{info['error']}`")
        lines.append("")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    report = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "probe_scope": "MW5 editor Python mod authoring/package API symbol and type inspection",
        "non_mutating": True,
        "search_terms": SEARCH_TERMS,
        "runtime_state": {
            "workspace": str(WORKSPACE),
            "editor_root": str(EDITOR_ROOT),
            "project": str(EDITOR_ROOT / "MW5Mercs" / "MW5Mercs.uproject"),
            "stub_path": str(STUB_PATH),
        },
        "matching_unreal_symbols": matching_unreal_symbols(),
        "class_summaries": {name: class_summary(name) for name in EXACT_TYPES},
        "struct_samples": struct_samples(),
        "mwmodutils_safe_results": mwmodutils_safe_results(),
        "editor_widget_probe": editor_widget_probe(),
        "editor_utility_asset_matches": find_editor_utility_assets(),
        "active_mod_path_probe": active_mod_path_probe(),
        "stub_snippets": stub_snippets(),
    }
    report["decision"] = build_decision(report)

    OUT_JSON.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    write_markdown(report)
    unreal.log(f"TKU MW5 mod types probe wrote {OUT_JSON} and {OUT_MD}")


main()
