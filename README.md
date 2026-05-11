# TKU Update Workspace

This project lives outside the live MechWarrior 5 install so scripts, reports, and agent notes do not get mixed into the game directory.

## Important Paths

Default local paths are recorded in `config/tku_paths.local.json` and documented in `config/tku_paths.example.json`.

- Project root: `D:\Downloads\OneDrive\Documents\code\tku-update`
- Game install root: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries`
- Local MW5 mod root: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods`
- Game content pak root: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks`
- Steam Workshop MW5 mods: `E:\SteamLibrary\steamapps\workshop\content\784080`
- MW5 Mod Editor: `E:\Games\MechWarrior5Editor`
- UEViewer/umodel: `C:\Program Files\umodel`
- FModel: `C:\Program Files\fmodel`
- Blender 5.1 with Unreal PSK/PSA addon: `C:\Program Files\Blender Foundation\Blender 5.1`
- UAssetAPI/MW5AssetTool: `D:\Downloads\OneDrive\Documents\code\tku-update\tools\MW5AssetTool`
- UAssetGUI: `C:\Program Files\UassetGUI`
- UE4SS v3.0.1 dev extraction: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Binaries\Win64`

## Working Rules

Run future Codex/assistant sessions from this folder, not from the game install folder. The copied scripts use `tools/tku_project_paths.py` so project outputs stay under this workspace while live mod and pak operations still target the configured game paths.

Prefer `config/tku_paths.local.json` for this machine. For another machine, copy `config/tku_paths.example.json` to `config/tku_paths.local.json` and adjust the paths, or set these environment variables:

- `TKU_GAME_ROOT`
- `TKU_LOCAL_MODS_ROOT`
- `TKU_CONTENT_PAKS_ROOT`
- `TKU_STEAM_WORKSHOP_ROOT`
- `TKU_MW5_EDITOR_ROOT`
- `TKU_UMODEL_ROOT`
- `TKU_FMODEL_ROOT`
- `TKU_BLENDER_ROOT`
- `TKU_UASSETAPI_ROOT`
- `TKU_UASSETGUI_ROOT`
- `TKU_UE4SS_WIN64_ROOT`

Do not overwrite original TKU paks or loose required override paks in place. Put evidence under `reports\tku_editor_first\` and helper scripts under `tools\tku_reference_audit\`.
