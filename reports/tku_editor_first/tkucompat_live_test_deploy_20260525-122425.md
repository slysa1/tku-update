# TKU Compat Live Test Deploy - 20260525-122425

- Apply requested: `True`
- Source package: `E:\Games\MechWarrior5Editor\MW5Mercs\Mods\TKUCompatEditorPatch\TKUCompatEditorPatch\TKUCompatEditorPatch`
- Destination mod: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch`
- Baseline mod: `TKUEvidenceCorePluginOnly`
- Load order: `95`
- Game version: `1.13.378`
- Game version source: `parameter/default`
- Live modlist backup: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260525-122425.json`
- Repo modlist backup: `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\modlist.backup-before-TKUCompatEditorPatch-20260525-122425.json`
- Destination mod backup: `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\backups\live_mod_before_deploy_TKUCompatEditorPatch_20260525-122425`
- Test profile: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.profile-TKUCompatEditorPatch-corepatch-20260525-122425.json`

## Safety

- No safety failures.

## Actions

- backed up live modlist to E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260525-122425.json
- backed up live modlist to D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\modlist.backup-before-TKUCompatEditorPatch-20260525-122425.json
- backed up existing destination mod folder to D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\backups\live_mod_before_deploy_TKUCompatEditorPatch_20260525-122425
- removed existing destination mod folder before redeploy
- copied packaged mod to E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch
- updated deployed TKUCompatEditorPatch mod.json defaultLoadOrder=95 gameVersion=1.13.378
- wrote isolated test profile E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.profile-TKUCompatEditorPatch-corepatch-20260525-122425.json
- activated isolated test profile in E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.json

## Hashes

- deployed_mod_json: `EF93133F1EC0B513F65FE6B390451387DA2988DA8C23FCA12230E4109FF86BB9`
- deployed_pak: `7B9EA432C7624E4AE045F90D5E4C81F91A744F94F285A75B57232BA12C0A6C4E`
- source_mod_json: `258931944B78E1215D44E94373BF67F3DE34D4AF5010A473B873621A65867DFD`
- source_pak: `7B9EA432C7624E4AE045F90D5E4C81F91A744F94F285A75B57232BA12C0A6C4E`
- live_modlist: `9A1B441FD6AE98BF5652F4FEC8253BF59A57635F62A030EEB8A014DCD7E039A4`

## Rollback

To restore the previous live modlist, copy `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260525-122425.json` back to `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.json`.
To restore the previous deployed mod folder, copy `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\backups\live_mod_before_deploy_TKUCompatEditorPatch_20260525-122425` back to `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch`.
