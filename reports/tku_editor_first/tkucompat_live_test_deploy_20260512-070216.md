# TKU Compat Live Test Deploy - 20260512-070216

- Apply requested: `True`
- Source package: `E:\Games\MechWarrior5Editor\MW5Mercs\Mods\TKUCompatEditorPatch`
- Destination mod: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch`
- Baseline mod: `TKUEvidenceCorePluginOnly`
- Load order: `95`
- Game version: `1.1.380`
- Live modlist backup: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260512-070216.json`
- Repo modlist backup: `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\modlist.backup-before-TKUCompatEditorPatch-20260512-070216.json`
- Test profile: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.profile-TKUCompatEditorPatch-corepatch-20260512-070216.json`

## Safety

- No safety failures.

## Actions

- backed up live modlist to E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260512-070216.json
- backed up live modlist to D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\modlist.backup-before-TKUCompatEditorPatch-20260512-070216.json
- copied packaged mod to E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch
- updated deployed TKUCompatEditorPatch mod.json defaultLoadOrder=95 gameVersion=1.1.380
- wrote isolated test profile E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.profile-TKUCompatEditorPatch-corepatch-20260512-070216.json
- activated isolated test profile in E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.json

## Hashes

- deployed_mod_json: `469D22A8FD9A94F8CEA1045B147432272710F8FE155BA739366F0332C76305EA`
- deployed_pak: `3214395F1E9EDB88957903C88CE364A48AD634902A26EF461284E3D27BAAED0D`
- source_mod_json: `915029771DF2F0AD587F0A14D035FF6E1A1B93D13C65AF718388297455EC4CA9`
- source_pak: `3214395F1E9EDB88957903C88CE364A48AD634902A26EF461284E3D27BAAED0D`
- live_modlist: `337E2487793E061A6FF282130791978A964A8C5F42CAA28C07C6CC458587CCDE`

## Rollback

To restore the previous live modlist, copy `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260512-070216.json` back to `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.json`.
