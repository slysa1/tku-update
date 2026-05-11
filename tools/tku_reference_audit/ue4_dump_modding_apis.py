from __future__ import annotations

import json
from pathlib import Path

import unreal


from tku_project_paths import GAME_ROOT as WORKSPACE, PROJECT_ROOT, REPORTS_DIR, TOOLS_ROOT
OUT_DIR = REPORTS_DIR / "tku_editor_first"
OUT_JSON = OUT_DIR / "ue4_modding_api_probe.json"
OUT_MD = OUT_DIR / "ue4_modding_api_probe.md"

KEYWORDS = (
    "mod",
    "override",
    "plugin",
    "asset",
    "blueprint",
    "package",
    "save",
    "cook",
)


def public_members(obj) -> list[str]:
    try:
        return sorted(name for name in dir(obj) if not name.startswith("_"))
    except Exception as exc:
        return [f"<dir-error:{type(exc).__name__}:{exc}>"]


def selected_module_symbols() -> dict[str, list[str]]:
    symbols = {}
    for keyword in KEYWORDS:
        symbols[keyword] = sorted(name for name in dir(unreal) if keyword.lower() in name.lower())[:400]
    return symbols


def class_members(class_name: str) -> dict:
    cls = getattr(unreal, class_name, None)
    if cls is None:
        return {"exists": False}
    return {
        "exists": True,
        "members": public_members(cls),
    }


def object_members(class_name: str) -> dict:
    cls = getattr(unreal, class_name, None)
    if cls is None:
        return {"exists": False}
    try:
        obj = cls()
    except Exception as exc:
        return {"exists": True, "construct_error": f"{type(exc).__name__}: {exc}", "class_members": public_members(cls)}
    return {"exists": True, "members": public_members(obj), "class_members": public_members(cls)}


def asset_probe(asset_path: str) -> dict:
    out = {"asset_path": asset_path}
    try:
        out["exists"] = bool(unreal.EditorAssetLibrary.does_asset_exist(asset_path))
    except Exception as exc:
        out["exists_error"] = f"{type(exc).__name__}: {exc}"
    try:
        asset = unreal.EditorAssetLibrary.load_asset(asset_path)
        out["loaded"] = bool(asset)
        if asset:
            out["class"] = str(asset.get_class().get_name())
            out["object_path"] = str(asset.get_path_name())
    except Exception as exc:
        out["load_error"] = f"{type(exc).__name__}: {exc}"
    try:
        bp_class = unreal.EditorAssetLibrary.load_blueprint_class(asset_path)
        out["blueprint_class"] = str(bp_class.get_path_name()) if bp_class else None
        if bp_class:
            cdo = unreal.get_default_object(bp_class)
            out["cdo_path"] = str(cdo.get_path_name())
            out["cdo_class"] = str(cdo.get_class().get_name())
            out["cdo_properties"] = {}
            for prop in ("PanBoundsHorizontal", "PanBoundsVertical", "ZoomDistanceList", "ZoomLevelThresholds"):
                try:
                    value = cdo.get_editor_property(prop)
                    if not isinstance(value, (str, int, float, bool)):
                        try:
                            value = list(value)
                        except Exception:
                            value = str(value)
                    out["cdo_properties"][prop] = value
                except Exception as exc:
                    out["cdo_properties"][prop] = f"<error:{type(exc).__name__}:{exc}>"
    except Exception as exc:
        out["blueprint_error"] = f"{type(exc).__name__}: {exc}"
    return out


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    report = {
        "source_note": "Non-mutating probe of MW5 Mod Editor Python API names related to mod/plugin/asset authoring.",
        "module_symbols": selected_module_symbols(),
        "class_members": {
            name: class_members(name)
            for name in (
                "EditorAssetLibrary",
                "AssetToolsHelpers",
                "AssetTools",
                "BlueprintEditorLibrary",
                "EditorLoadingAndSavingUtils",
                "EditorLevelLibrary",
                "PluginBlueprintLibrary",
                "ProjectPackagingSettings",
            )
        },
        "object_members": {
            name: object_members(name)
            for name in (
                "AssetTools",
                "ProjectPackagingSettings",
            )
        },
        "asset_probe": asset_probe("/Game/UI/FrontEnd/StarMapPawn"),
    }
    OUT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")

    lines = [
        "# UE4 Modding API Probe",
        "",
        report["source_note"],
        "",
        "## Asset Probe",
        "",
    ]
    probe = report["asset_probe"]
    for key, value in probe.items():
        lines.append(f"- `{key}`: `{value}`")
    lines.extend(["", "## Useful Symbols", ""])
    for keyword, names in report["module_symbols"].items():
        lines.append(f"### `{keyword}`")
        for name in names[:80]:
            lines.append(f"- `{name}`")
        lines.append("")
    lines.extend(["## Class Members", ""])
    for name, info in report["class_members"].items():
        lines.append(f"### `{name}` exists `{info.get('exists')}`")
        for member in info.get("members", [])[:160]:
            lines.append(f"- `{member}`")
        if info.get("construct_error"):
            lines.append(f"- construct error: `{info['construct_error']}`")
        lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    unreal.log(f"TKU modding API probe written to {OUT_JSON}")


main()
