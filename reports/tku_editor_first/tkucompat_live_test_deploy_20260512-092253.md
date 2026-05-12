# TKU Compat Live Test Deploy - 20260512-092253

- Apply requested: `True`
- Source package: `E:\Games\MechWarrior5Editor\MW5Mercs\Mods\TKUCompatEditorPatch`
- Destination mod: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch`
- Baseline mod: `TKUEvidenceCorePluginOnly`
- Load order: `95`
- Game version: `1.13.378`
- Game version source: `live modlist`
- Live modlist backup: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260512-092253.json`
- Repo modlist backup: `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\modlist.backup-before-TKUCompatEditorPatch-20260512-092253.json`
- Destination mod backup: `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\backups\live_mod_before_deploy_TKUCompatEditorPatch_20260512-092253`
- Test profile: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.profile-TKUCompatEditorPatch-corepatch-20260512-092253.json`

## Safety

- No safety failures.

## Actions

- backed up live modlist to E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260512-092253.json
- backed up live modlist to D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\modlist.backup-before-TKUCompatEditorPatch-20260512-092253.json
- backed up existing destination mod folder to D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\backups\live_mod_before_deploy_TKUCompatEditorPatch_20260512-092253
- removed existing destination mod folder before redeploy
- copied packaged mod to E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch
- updated deployed TKUCompatEditorPatch mod.json defaultLoadOrder=95 gameVersion=1.13.378
- wrote isolated test profile E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.profile-TKUCompatEditorPatch-corepatch-20260512-092253.json
- activated isolated test profile in E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.json

## Hashes

- deployed_mod_json: `D44214389A1C8AF11A369793308F88DC9CD5FA3601C245206FF82695A8E52A11`
- deployed_pak: `FB5F798061ADFF1DC78A4CD350541E530692C3C681061D639C24107895CB746C`
- source_mod_json: `A5894A7E6C77BD31D5C617BC26328E7F130F321C277A49D16A6357483AA90971`
- source_pak: `FB5F798061ADFF1DC78A4CD350541E530692C3C681061D639C24107895CB746C`
- live_modlist: `9A1B441FD6AE98BF5652F4FEC8253BF59A57635F62A030EEB8A014DCD7E039A4`

## Rollback

To restore the previous live modlist, copy `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260512-092253.json` back to `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.json`.
To restore the previous deployed mod folder, copy `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\backups\live_mod_before_deploy_TKUCompatEditorPatch_20260512-092253` back to `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch`.
