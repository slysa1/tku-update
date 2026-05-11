from __future__ import annotations

import csv
import json
import os
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import unreal
except ImportError:  # Allows normal Python syntax checks outside the editor.
    unreal = None


TARGET_MOD_NAME = os.environ.get("TKU_IMPORT_EXPECT_MOD_NAME", "TKUCompatEditorPatch").strip()
SOURCE_ASSET_PATH = "/Game/InnerSphereData/MW5_InnerSphereData"
EXPECTED_ROW_STRUCT = "/Script/MechWarrior.InnerSphereMapData"
EXPECTED_ROW_COUNT = int(os.environ.get("TKU_IMPORT_EXPECTED_ROW_COUNT", "3974"))
SAMPLE_ROWS = ["0", "1", "2", "3501", "4001", "4110", "7921"]
REPORT_STEM = "ue4_inner_sphere_import_20260511"


def env_flag(name: str) -> bool:
    return os.environ.get(name, "").strip().lower() in {"1", "true", "yes", "y", "on"}


APPLY = env_flag("TKU_IMPORT_APPLY")
ALLOW_ROOT_OVERRIDE = env_flag("TKU_ALLOW_ROOT_INNER_SPHERE_OVERRIDE")
TARGET_ASSET_PATH = os.environ.get("TKU_IMPORT_TARGET_ASSET", "").strip()


def resolve_project_root() -> Path:
    raw = os.environ.get("TKU_PROJECT_ROOT")
    if raw:
        return Path(raw).resolve()

    script_path = globals().get("__file__")
    if script_path:
        return Path(script_path).resolve().parents[2]

    return Path(r"D:\Downloads\OneDrive\Documents\code\tku-update")


PROJECT_ROOT = resolve_project_root()
CONFIG_PATHS = [
    Path(os.environ["TKU_PATHS_CONFIG"]) if os.environ.get("TKU_PATHS_CONFIG") else None,
    PROJECT_ROOT / "config" / "tku_paths.local.json",
    PROJECT_ROOT / "config" / "tku_paths.json",
    PROJECT_ROOT / "config" / "tku_paths.example.json",
]
REPORT_DIR = PROJECT_ROOT / "reports" / "tku_editor_first"
OUT_JSON = REPORT_DIR / f"{REPORT_STEM}.json"
OUT_MD = REPORT_DIR / f"{REPORT_STEM}.md"
DEFAULT_CSV = REPORT_DIR / "tku_inner_sphere_merged_current_plus_tku_additions_20260510.csv"
CSV_PATH = Path(os.environ.get("TKU_IMPORT_CSV_PATH", str(DEFAULT_CSV))).resolve()


def read_config() -> dict[str, Any]:
    for candidate in CONFIG_PATHS:
        if candidate and candidate.is_file():
            return json.loads(candidate.read_text(encoding="utf-8"))
    return {}


CONFIG = read_config()
EDITOR_ROOT = Path(
    os.environ.get("TKU_MW5_EDITOR_ROOT")
    or CONFIG.get("mw5_editor_root")
    or r"E:\Games\MechWarrior5Editor"
)
EDITOR_PROJECT = EDITOR_ROOT / "MW5Mercs"


def jsonable(value: Any, depth: int = 0) -> Any:
    if depth > 4:
        return str(value)
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, dict):
        return {str(k): jsonable(v, depth + 1) for k, v in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [jsonable(item, depth + 1) for item in value]
    try:
        if hasattr(value, "__iter__") and not isinstance(value, (str, bytes)):
            return [jsonable(item, depth + 1) for item in list(value)]
    except Exception:
        pass

    out: dict[str, Any] = {"repr": str(value), "python_type": type(value).__name__}
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


def safe_call(func, *args) -> dict[str, Any]:
    try:
        return {"ok": True, "value": jsonable(func(*args))}
    except Exception as exc:
        return {"ok": False, "error": f"{type(exc).__name__}: {exc}"}


def get_path_name(obj: Any) -> str:
    try:
        return str(obj.get_path_name())
    except Exception:
        return str(obj)


def get_class_name(obj: Any) -> str:
    try:
        return str(obj.get_class().get_name())
    except Exception:
        return ""


def normalize_asset_path(path: str) -> str:
    path = path.strip()
    slash_index = path.rfind("/")
    dot_index = path.find(".", slash_index + 1)
    if dot_index != -1:
        return path[:dot_index]
    return path


def detect_csv_encoding(path: Path) -> str:
    start = path.read_bytes()[:4]
    if start.startswith((b"\xff\xfe", b"\xfe\xff")):
        return "utf-16"
    if start.startswith(b"\xef\xbb\xbf"):
        return "utf-8-sig"
    return "utf-8-sig"


def csv_summary(path: Path) -> dict[str, Any]:
    out: dict[str, Any] = {"path": str(path), "exists": path.is_file()}
    if not path.is_file():
        return out

    try:
        encoding = detect_csv_encoding(path)
        row_ids: list[str] = []
        rows_preview: list[list[str]] = []
        with path.open("r", encoding=encoding, newline="") as handle:
            reader = csv.reader(handle)
            header = next(reader)
            for index, row in enumerate(reader):
                if not row or not any(cell.strip() for cell in row):
                    continue
                row_ids.append(row[0].strip())
                if index < 5:
                    rows_preview.append(row[:8])
        out.update(
            {
                "encoding": encoding,
                "header": header,
                "row_count": len(row_ids),
                "sample_rows_present": {row_id: row_id in set(row_ids) for row_id in SAMPLE_ROWS},
                "preview": rows_preview,
            }
        )
    except Exception as exc:
        out["error"] = f"{type(exc).__name__}: {exc}"
    return out


def mod_target_status() -> dict[str, Any]:
    mods_dir = EDITOR_PROJECT / "Mods" / TARGET_MOD_NAME
    plugins_dir = EDITOR_PROJECT / "Plugins" / TARGET_MOD_NAME
    plugin_file = plugins_dir / f"{TARGET_MOD_NAME}.uplugin"
    filesystem = {
        "mods_dir": str(mods_dir),
        "mods_dir_exists": mods_dir.exists(),
        "plugins_dir": str(plugins_dir),
        "plugins_dir_exists": plugins_dir.exists(),
        "plugin_file": str(plugin_file),
        "plugin_file_exists": plugin_file.exists(),
    }

    mwmodutils: dict[str, Any] = {"available": False}
    if unreal is not None and hasattr(unreal, "MWModUtils"):
        mwmodutils["available"] = True
        for name, args in (
            ("get_mods_install_path", ()),
            ("get_mod_plugin_names", ()),
            ("get_active_mod_plugin", ()),
            ("get_active_mod_entry", ()),
        ):
            mwmodutils[name] = safe_call(getattr(unreal.MWModUtils, name), *args)

    plugin_names = []
    names_result = mwmodutils.get("get_mod_plugin_names", {})
    if names_result.get("ok"):
        plugin_names = [str(name) for name in names_result.get("value", [])]

    found = (
        filesystem["mods_dir_exists"]
        or filesystem["plugins_dir_exists"]
        or filesystem["plugin_file_exists"]
        or TARGET_MOD_NAME in plugin_names
    )
    return {
        "target_mod_name": TARGET_MOD_NAME,
        "filesystem": filesystem,
        "mwmodutils": mwmodutils,
        "found": found,
    }


def data_table_info(asset_path: str) -> dict[str, Any]:
    out: dict[str, Any] = {"asset_path": asset_path, "exists": False}
    if unreal is None:
        out["error"] = "unreal module is not available; run through MW5 UE4Editor-Cmd."
        return out
    if not asset_path:
        out["error"] = "No target asset path supplied."
        return out

    asset_path = normalize_asset_path(asset_path)
    out["asset_path"] = asset_path
    exists_result = safe_call(unreal.EditorAssetLibrary.does_asset_exist, asset_path)
    out["exists_call"] = exists_result
    out["exists"] = bool(exists_result.get("ok") and exists_result.get("value"))
    if not out["exists"]:
        return out

    asset_result = safe_call(unreal.EditorAssetLibrary.load_asset, asset_path)
    out["load_call"] = asset_result
    if not asset_result.get("ok"):
        return out

    asset = unreal.EditorAssetLibrary.load_asset(asset_path)
    out["class"] = get_class_name(asset)
    out["object_path"] = get_path_name(asset)

    try:
        row_struct = asset.get_editor_property("row_struct")
        out["row_struct"] = get_path_name(row_struct)
    except Exception as exc:
        out["row_struct_error"] = f"{type(exc).__name__}: {exc}"

    try:
        rows = [str(row) for row in unreal.DataTableFunctionLibrary.get_data_table_row_names(asset)]
        row_set = set(rows)
        out["row_count"] = len(rows)
        out["sample_rows_present"] = {row_id: row_id in row_set for row_id in SAMPLE_ROWS}
        out["first_rows"] = rows[:20]
    except Exception as exc:
        out["row_error"] = f"{type(exc).__name__}: {exc}"
    return out


def root_override_active_mod_check(mod_status: dict[str, Any]) -> dict[str, Any]:
    active_text = json.dumps(mod_status.get("mwmodutils", {}), ensure_ascii=False, default=str)
    return {
        "active_mod_mentions_target": TARGET_MOD_NAME.lower() in active_text.lower(),
        "active_mod_raw": mod_status.get("mwmodutils", {}),
    }


def build_safety_failures(report: dict[str, Any]) -> list[str]:
    failures: list[str] = []
    target_asset = normalize_asset_path(TARGET_ASSET_PATH)

    if unreal is None:
        failures.append("This script must run inside MW5 UE4Editor-Cmd; the unreal module is unavailable.")
    if not report["mod_target"]["found"]:
        failures.append(f"Editor mod target {TARGET_MOD_NAME} was not found.")
    if not target_asset:
        failures.append("TKU_IMPORT_TARGET_ASSET is required before applying.")
    if not report["csv"].get("exists"):
        failures.append(f"CSV import file does not exist: {CSV_PATH}")
    if report["csv"].get("row_count") != EXPECTED_ROW_COUNT:
        failures.append(
            f"CSV row count is {report['csv'].get('row_count')}; expected {EXPECTED_ROW_COUNT}."
        )

    if target_asset == SOURCE_ASSET_PATH and not ALLOW_ROOT_OVERRIDE:
        failures.append(
            "Target asset is the root /Game DataTable. Set TKU_ALLOW_ROOT_INNER_SPHERE_OVERRIDE=1 "
            "only after using the MW5 editor Save To Mod workflow for the active mod."
        )
    if target_asset == SOURCE_ASSET_PATH and ALLOW_ROOT_OVERRIDE:
        active = root_override_active_mod_check(report["mod_target"])
        report["root_override_active_mod_check"] = active
        if not active["active_mod_mentions_target"]:
            failures.append(
                "Root override mode was requested, but MWModUtils active-mod state does not mention "
                f"{TARGET_MOD_NAME}."
            )
    if target_asset and target_asset != SOURCE_ASSET_PATH and TARGET_MOD_NAME.lower() not in target_asset.lower():
        failures.append(
            f"Target asset path does not include {TARGET_MOD_NAME}; refusing to write outside the mod target."
        )

    target_info = report.get("target_data_table", {})
    if target_asset and not target_info.get("exists"):
        failures.append(f"Target DataTable asset does not exist: {target_asset}")
    if target_info.get("class") and target_info.get("class") != "DataTable":
        failures.append(f"Target asset class is {target_info.get('class')}; expected DataTable.")
    if target_info.get("row_struct") and target_info.get("row_struct") != EXPECTED_ROW_STRUCT:
        failures.append(
            f"Target row struct is {target_info.get('row_struct')}; expected {EXPECTED_ROW_STRUCT}."
        )
    return failures


def apply_import(report: dict[str, Any]) -> None:
    target_asset = normalize_asset_path(TARGET_ASSET_PATH)
    failures = build_safety_failures(report)
    report["safety_failures"] = failures
    if failures:
        report["apply_result"] = {"attempted": False, "applied": False, "reason": "safety_failures"}
        return
    if not APPLY:
        report["apply_result"] = {"attempted": False, "applied": False, "reason": "dry_run"}
        return

    try:
        asset = unreal.EditorAssetLibrary.load_asset(target_asset)
        before = data_table_info(target_asset)
        imported = bool(unreal.DataTableFunctionLibrary.fill_data_table_from_csv_file(asset, str(CSV_PATH)))
        after = data_table_info(target_asset)
        samples_ok = all(after.get("sample_rows_present", {}).values())
        row_count_ok = after.get("row_count") == EXPECTED_ROW_COUNT
        saved = False
        if imported and samples_ok and row_count_ok:
            saved = bool(unreal.EditorAssetLibrary.save_loaded_asset(asset, True))
        report["apply_result"] = {
            "attempted": True,
            "applied": imported,
            "saved": saved,
            "row_count_ok": row_count_ok,
            "sample_rows_ok": samples_ok,
            "before": before,
            "after": after,
        }
    except Exception as exc:
        report["apply_result"] = {
            "attempted": True,
            "applied": False,
            "error": f"{type(exc).__name__}: {exc}",
            "traceback": traceback.format_exc(),
        }


def write_report(report: dict[str, Any]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True, default=str), encoding="utf-8")

    lines = [
        "# UE4 InnerSphere DataTable Import Gate - 2026-05-11",
        "",
        f"- Generated: `{report['generated_utc']}`",
        f"- Apply requested: `{report['apply_requested']}`",
        f"- Target mod: `{TARGET_MOD_NAME}`",
        f"- Target asset: `{TARGET_ASSET_PATH or '<not supplied>'}`",
        f"- CSV: `{CSV_PATH}`",
        "",
        "## Mod Target",
        "",
        f"- Found: `{report['mod_target']['found']}`",
        f"- Filesystem: `{report['mod_target']['filesystem']}`",
        "",
        "## CSV",
        "",
        f"- Exists: `{report['csv'].get('exists')}`",
        f"- Encoding: `{report['csv'].get('encoding')}`",
        f"- Row count: `{report['csv'].get('row_count')}`",
        f"- Sample rows present: `{report['csv'].get('sample_rows_present')}`",
        "",
        "## Target DataTable",
        "",
        f"- Exists: `{report.get('target_data_table', {}).get('exists')}`",
        f"- Class: `{report.get('target_data_table', {}).get('class')}`",
        f"- Row struct: `{report.get('target_data_table', {}).get('row_struct')}`",
        f"- Row count: `{report.get('target_data_table', {}).get('row_count')}`",
        "",
        "## Safety",
        "",
    ]
    failures = report.get("safety_failures") or []
    if failures:
        for failure in failures:
            lines.append(f"- {failure}")
    else:
        lines.append("- No safety failures.")

    result = report.get("apply_result", {})
    lines.extend(
        [
            "",
            "## Result",
            "",
            f"- Attempted: `{result.get('attempted')}`",
            f"- Applied: `{result.get('applied')}`",
            f"- Saved: `{result.get('saved')}`",
            f"- Reason: `{result.get('reason')}`",
            f"- Row count OK: `{result.get('row_count_ok')}`",
            f"- Sample rows OK: `{result.get('sample_rows_ok')}`",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    report: dict[str, Any] = {
        "generated_utc": datetime.now(timezone.utc).isoformat(),
        "script": str(Path(globals().get("__file__", "")).resolve()) if globals().get("__file__") else None,
        "project_root": str(PROJECT_ROOT),
        "editor_root": str(EDITOR_ROOT),
        "editor_project": str(EDITOR_PROJECT),
        "target_mod_name": TARGET_MOD_NAME,
        "source_asset_path": SOURCE_ASSET_PATH,
        "target_asset_path": TARGET_ASSET_PATH,
        "csv_path": str(CSV_PATH),
        "apply_requested": APPLY,
        "allow_root_override": ALLOW_ROOT_OVERRIDE,
        "expected_row_struct": EXPECTED_ROW_STRUCT,
        "expected_row_count": EXPECTED_ROW_COUNT,
        "sample_rows": SAMPLE_ROWS,
        "csv": csv_summary(CSV_PATH),
        "mod_target": mod_target_status(),
    }
    report["target_data_table"] = data_table_info(TARGET_ASSET_PATH) if TARGET_ASSET_PATH else {
        "asset_path": "",
        "exists": False,
        "error": "No TKU_IMPORT_TARGET_ASSET supplied.",
    }
    apply_import(report)
    write_report(report)
    if unreal is not None:
        unreal.log(f"TKU InnerSphere import gate wrote {OUT_JSON}")
    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")

main()
