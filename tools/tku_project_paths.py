from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = PROJECT_ROOT / "tools"
CONFIG_DIR = PROJECT_ROOT / "config"

_DEFAULTS = {
    "game_root": r"E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries",
    "steam_workshop_root": r"E:\SteamLibrary\steamapps\workshop\content\784080",
    "mw5_editor_root": r"E:\Games\MechWarrior5Editor",
    "umodel_root": r"C:\Program Files\umodel",
    "fmodel_root": r"C:\Program Files\fmodel",
    "blender_root": r"C:\Program Files\Blender Foundation\Blender 5.1",
    "uassetapi_root": PROJECT_ROOT / "tools" / "MW5AssetTool",
    "uassetgui_root": r"C:\Program Files\UassetGUI",
    "ue4ss_win64_root": r"E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Binaries\Win64",
}

_ENV_KEYS = {
    "game_root": "TKU_GAME_ROOT",
    "local_mods_root": "TKU_LOCAL_MODS_ROOT",
    "content_paks_root": "TKU_CONTENT_PAKS_ROOT",
    "steam_workshop_root": "TKU_STEAM_WORKSHOP_ROOT",
    "mw5_editor_root": "TKU_MW5_EDITOR_ROOT",
    "umodel_root": "TKU_UMODEL_ROOT",
    "fmodel_root": "TKU_FMODEL_ROOT",
    "blender_root": "TKU_BLENDER_ROOT",
    "uassetapi_root": "TKU_UASSETAPI_ROOT",
    "uassetgui_root": "TKU_UASSETGUI_ROOT",
    "ue4ss_win64_root": "TKU_UE4SS_WIN64_ROOT",
}


def _read_config() -> dict[str, Any]:
    candidates: list[Path] = []
    explicit = os.environ.get("TKU_PATHS_CONFIG")
    if explicit:
        candidates.append(Path(explicit))
    candidates.extend(
        [
            CONFIG_DIR / "tku_paths.local.json",
            CONFIG_DIR / "tku_paths.json",
            CONFIG_DIR / "tku_paths.example.json",
        ]
    )
    for candidate in candidates:
        if candidate.is_file():
            return json.loads(candidate.read_text(encoding="utf-8"))
    return {}


_CONFIG = _read_config()


def _configured_path(key: str, default: str | Path) -> Path:
    raw = os.environ.get(_ENV_KEYS.get(key, "")) or _CONFIG.get(key) or default
    return Path(str(raw)).expanduser()


GAME_ROOT = _configured_path("game_root", _DEFAULTS["game_root"])
MODS_ROOT = _configured_path("local_mods_root", GAME_ROOT / "MW5Mercs" / "Mods")
CONTENT_PAKS_ROOT = _configured_path("content_paks_root", GAME_ROOT / "MW5Mercs" / "Content" / "Paks")
STEAM_WORKSHOP_ROOT = _configured_path("steam_workshop_root", _DEFAULTS["steam_workshop_root"])
MW5_EDITOR_ROOT = _configured_path("mw5_editor_root", _DEFAULTS["mw5_editor_root"])
UMODEL_ROOT = _configured_path("umodel_root", _DEFAULTS["umodel_root"])
FMODEL_ROOT = _configured_path("fmodel_root", _DEFAULTS["fmodel_root"])
BLENDER_ROOT = _configured_path("blender_root", _DEFAULTS["blender_root"])
UASSETAPI_ROOT = _configured_path("uassetapi_root", _DEFAULTS["uassetapi_root"])
UASSETGUI_ROOT = _configured_path("uassetgui_root", _DEFAULTS["uassetgui_root"])
UE4SS_WIN64_ROOT = _configured_path("ue4ss_win64_root", _DEFAULTS["ue4ss_win64_root"])
REPORTS_DIR = PROJECT_ROOT / "reports"
TKU_EDITOR_FIRST_REPORTS_DIR = REPORTS_DIR / "tku_editor_first"

__all__ = [
    "PROJECT_ROOT",
    "TOOLS_ROOT",
    "CONFIG_DIR",
    "GAME_ROOT",
    "MODS_ROOT",
    "CONTENT_PAKS_ROOT",
    "STEAM_WORKSHOP_ROOT",
    "MW5_EDITOR_ROOT",
    "UMODEL_ROOT",
    "FMODEL_ROOT",
    "BLENDER_ROOT",
    "UASSETAPI_ROOT",
    "UASSETGUI_ROOT",
    "UE4SS_WIN64_ROOT",
    "REPORTS_DIR",
    "TKU_EDITOR_FIRST_REPORTS_DIR",
]
