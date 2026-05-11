# Workspace Notes

This workspace is the TKU update project root, intentionally separate from the live MechWarrior 5 install.

## Project And Runtime Paths

- Project root: `D:\Downloads\OneDrive\Documents\code\tku-update`
- Game install root: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries`
- Local MW5 mod root: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods`
- Game content pak root: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks`
- Steam Workshop MW5 mods: `E:\SteamLibrary\steamapps\workshop\content\784080`
- Path config: `config\tku_paths.local.json`; fallback example: `config\tku_paths.example.json`.
- Path helper for scripts: `tools\tku_project_paths.py`.

## Available Tooling

- MW5 Mod Editor is available at `E:\Games\MechWarrior5Editor`; use it as the preferred source for Blueprint parents, asset references, schemas, editor-authored overrides, and package/build behavior.
- UEViewer/umodel is available at `C:\Program Files\umodel`; its use is encouraged for cooked asset inspection, export checks, package contents, and reference evidence.
- FModel is available at `C:\Program Files\fmodel`; its use is encouraged for pak browsing, cooked asset review, string searches, and reference evidence.
- Blender 5.1 is available at `C:\Program Files\Blender Foundation\Blender 5.1` with the Unreal PSK/PSA addon installed; use it where appropriate for mesh, animation, import/export, and visual inspection work.
- UAssetAPI/MW5AssetTool is available at `D:\Downloads\OneDrive\Documents\code\tku-update\tools\MW5AssetTool`; use it where appropriate for structured UAsset inspection or automation, while keeping editor-authored fixes in the MW5 Mod Editor unless a workflow is explicitly proven safe.
- UAssetGUI is available at `C:\Program Files\UassetGUI`; use it where appropriate for asset inspection and comparison.
- `zDEV-UE4SS_v3.0.1.zip` has been extracted into `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Binaries\Win64`; use that UE4SS install where appropriate for runtime instrumentation, Lua/mod hooks, or evidence gathering.
- Keep evidence outputs under `reports\tku_editor_first\`, helper scripts under `tools\tku_reference_audit\`, or a clearly named staging directory in this project.

## Safety

- Treat FModel, umodel, Blender, UAssetAPI/MW5AssetTool, and UAssetGUI output as supporting evidence unless the workflow has been separately validated. Prefer MW5 Mod Editor behavior and UE4.27 documentation for final compatibility decisions and authored asset changes.
- Treat UE4SS runtime observations as supporting runtime evidence. Prefer MW5 Mod Editor behavior for asset repair decisions, and do not remove or re-extract UE4SS without an explicit reason.
- Do not install duplicate asset-inspection tools unless the user explicitly asks for it.
- Do not overwrite original TKU paks or loose required override paks in place.
- Do not treat this project folder as the game install folder. Use the configured paths for all live mod, pak, and Workshop locations.
