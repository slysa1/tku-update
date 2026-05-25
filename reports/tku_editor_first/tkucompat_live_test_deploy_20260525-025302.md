# TKU Compat Live Test Deploy - 20260525-025302

- Apply requested: `True`
- Source package: `E:\Games\MechWarrior5Editor\MW5Mercs\Mods\TKUCompatEditorPatch\TKUCompatEditorPatch`
- Destination mod: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch`
- Baseline mod: `TKUEvidenceCorePluginOnly`
- Load order: `95`
- Game version: `1.13.378`
- Game version source: `live modlist`
- Live modlist backup: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260525-025302.json`
- Repo modlist backup: `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\modlist.backup-before-TKUCompatEditorPatch-20260525-025302.json`
- Destination mod backup: `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\backups\live_mod_before_deploy_TKUCompatEditorPatch_20260525-025302`
- Test profile: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.profile-TKUCompatEditorPatch-corepatch-20260525-025302.json`

## Safety

- No safety failures.

## Actions

- backed up live modlist to E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260525-025302.json
- backed up live modlist to D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\modlist.backup-before-TKUCompatEditorPatch-20260525-025302.json
- backed up existing destination mod folder to D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\backups\live_mod_before_deploy_TKUCompatEditorPatch_20260525-025302
- removed existing destination mod folder before redeploy
- copied packaged mod to E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch
- updated deployed TKUCompatEditorPatch mod.json defaultLoadOrder=95 gameVersion=1.13.378
- wrote isolated test profile E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.profile-TKUCompatEditorPatch-corepatch-20260525-025302.json
- activated isolated test profile in E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.json

## Hashes

- deployed_mod_json: `2E8AD50987C8929434774A6E0D58612F4209F332B284638919407FB5E09F4A82`
- deployed_pak: `4EFE99533ECB084EE69CF54B22302671EDBC5B57B520E6A3A823B2599629D687`
- source_mod_json: `9E5F9562C9FBE1922082CA69F4BDE1CEE82E612B485BCEA554D2F6215C7E1306`
- source_pak: `4EFE99533ECB084EE69CF54B22302671EDBC5B57B520E6A3A823B2599629D687`
- live_modlist: `9A1B441FD6AE98BF5652F4FEC8253BF59A57635F62A030EEB8A014DCD7E039A4`

## Rollback

To restore the previous live modlist, copy `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260525-025302.json` back to `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.json`.
To restore the previous deployed mod folder, copy `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\backups\live_mod_before_deploy_TKUCompatEditorPatch_20260525-025302` back to `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch`.
