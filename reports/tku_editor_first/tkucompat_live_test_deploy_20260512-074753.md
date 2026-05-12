# TKU Compat Live Test Deploy - 20260512-074753

- Apply requested: `True`
- Source package: `E:\Games\MechWarrior5Editor\MW5Mercs\Mods\TKUCompatEditorPatch`
- Destination mod: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch`
- Baseline mod: `TKUEvidenceCorePluginOnly`
- Load order: `95`
- Game version: `1.13.378`
- Game version source: `live modlist`
- Live modlist backup: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260512-074753.json`
- Repo modlist backup: `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\modlist.backup-before-TKUCompatEditorPatch-20260512-074753.json`
- Destination mod backup: `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\backups\live_mod_before_deploy_TKUCompatEditorPatch_20260512-074753`
- Test profile: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.profile-TKUCompatEditorPatch-corepatch-20260512-074753.json`

## Safety

- No safety failures.

## Actions

- backed up live modlist to E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260512-074753.json
- backed up live modlist to D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\modlist.backup-before-TKUCompatEditorPatch-20260512-074753.json
- backed up existing destination mod folder to D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\backups\live_mod_before_deploy_TKUCompatEditorPatch_20260512-074753
- removed existing destination mod folder before redeploy
- copied packaged mod to E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch
- updated deployed TKUCompatEditorPatch mod.json defaultLoadOrder=95 gameVersion=1.13.378
- wrote isolated test profile E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.profile-TKUCompatEditorPatch-corepatch-20260512-074753.json
- activated isolated test profile in E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.json

## Hashes

- deployed_mod_json: `3274DFCA7E196BB35F38E61E2DAE40E63D7F1F641BF08748EF566061FDCAB65E`
- deployed_pak: `43F98D4D171E1F189D96E3D5D7DA5BF6F2355C603381ED3E05AD5649811DA30D`
- source_mod_json: `823F58AAD5328017B1D15A554B9E88A46BD0482EF0D8928056BB5E85003804FF`
- source_pak: `43F98D4D171E1F189D96E3D5D7DA5BF6F2355C603381ED3E05AD5649811DA30D`
- live_modlist: `9A1B441FD6AE98BF5652F4FEC8253BF59A57635F62A030EEB8A014DCD7E039A4`

## Rollback

To restore the previous live modlist, copy `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260512-074753.json` back to `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.json`.
To restore the previous deployed mod folder, copy `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\backups\live_mod_before_deploy_TKUCompatEditorPatch_20260512-074753` back to `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch`.
