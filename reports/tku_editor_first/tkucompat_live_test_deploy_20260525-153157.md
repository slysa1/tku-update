# TKU Compat Live Test Deploy - 20260525-153157

- Apply requested: `True`
- Source package: `E:\Games\MechWarrior5Editor\MW5Mercs\Mods\TKUCompatEditorPatch\TKUCompatEditorPatch\TKUCompatEditorPatch`
- Destination mod: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch`
- Baseline mod: `TKUEvidenceCorePluginOnly`
- Load order: `95`
- Game version: `1.13.378`
- Game version source: `live modlist`
- Live modlist backup: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260525-153157.json`
- Repo modlist backup: `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\modlist.backup-before-TKUCompatEditorPatch-20260525-153157.json`
- Destination mod backup: `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\backups\live_mod_before_deploy_TKUCompatEditorPatch_20260525-153157`
- Test profile: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.profile-TKUCompatEditorPatch-corepatch-20260525-153157.json`

## Safety

- No safety failures.

## Actions

- backed up live modlist to E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260525-153157.json
- backed up live modlist to D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\modlist.backup-before-TKUCompatEditorPatch-20260525-153157.json
- backed up existing destination mod folder to D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\backups\live_mod_before_deploy_TKUCompatEditorPatch_20260525-153157
- removed existing destination mod folder before redeploy
- copied packaged mod to E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch
- updated deployed TKUCompatEditorPatch mod.json defaultLoadOrder=95 gameVersion=1.13.378
- wrote isolated test profile E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.profile-TKUCompatEditorPatch-corepatch-20260525-153157.json
- activated isolated test profile in E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.json

## Hashes

- deployed_mod_json: `26AF913E3DDE5416231BE6CB017805FBBC13E338C82A6D0E2947BF64652B8DE4`
- deployed_pak: `8E6DDE23C08CAC71988E93EE71014A6C0E67FB64FC81B1A560CCAEFB92439CC8`
- source_mod_json: `E17A255B85B4964F949EF3A1EA1C90E9FE5407752636083B9FCBCE583CE73C02`
- source_pak: `8E6DDE23C08CAC71988E93EE71014A6C0E67FB64FC81B1A560CCAEFB92439CC8`
- live_modlist: `9A1B441FD6AE98BF5652F4FEC8253BF59A57635F62A030EEB8A014DCD7E039A4`

## Rollback

To restore the previous live modlist, copy `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260525-153157.json` back to `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.json`.
To restore the previous deployed mod folder, copy `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\backups\live_mod_before_deploy_TKUCompatEditorPatch_20260525-153157` back to `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch`.
