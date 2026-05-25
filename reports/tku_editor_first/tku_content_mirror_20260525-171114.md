# TKU Content Mirror - 20260525-171114

Purpose: stage a late-loading `Content\Paks` mirror of the current editor-authored TKU compat package so root `/Game` assets can win over the legacy loose TKU starmap pak during a controlled runtime test.

- Apply requested: `True`
- Source pak: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch\Paks\TKUCompatEditorPatch.pak`
- Source pak candidates: `4`
- Staged mirror pak: `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\staging\MW5Mercs-zzzzTKUCompatEditorPatch-20260525-171114.pak`
- Live mirror pak: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak`
- Disabled live mirror sibling: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak.disabled-by-tku-isolation`
- Mirror pak SHA256: `4414AC6DA60FD9D04E5BCB9098E0D716A689912AF4C484288AD54680537860DC`
- Files mirrored: `8`

## Safety

- No safety failures.

## Conflicting Content Paks

- `MW5Mercs-WindowsNoEditor.pak` target entries `8` mount `../../../` sha `None`

## Actions

- staged UnrealPak-built content-root mirror pak at D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\staging\MW5Mercs-zzzzTKUCompatEditorPatch-20260525-171114.pak
- moved stale disabled mirror sibling to D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\backups\content_mirror_20260525-171114\MW5Mercs-zzzzTKUCompatEditorPatch.pak.disabled-by-tku-isolation
- deployed live mirror pak to E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak

## Disabled Mirror Backup

- Moved stale disabled mirror sibling to `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\backups\content_mirror_20260525-171114\MW5Mercs-zzzzTKUCompatEditorPatch.pak.disabled-by-tku-isolation`.

## Rollback

- Remove only the staged live mirror pak `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak` to return to the previous content-pak set.