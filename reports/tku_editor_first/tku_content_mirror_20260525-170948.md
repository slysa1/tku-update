# TKU Content Mirror - 20260525-170948

Purpose: stage a late-loading `Content\Paks` mirror of the current editor-authored TKU compat package so root `/Game` assets can win over the legacy loose TKU starmap pak during a controlled runtime test.

- Apply requested: `False`
- Source pak: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch\Paks\TKUCompatEditorPatch.pak`
- Source pak candidates: `4`
- Staged mirror pak: `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\staging\MW5Mercs-zzzzTKUCompatEditorPatch-20260525-170948.pak`
- Live mirror pak: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak`
- Disabled live mirror sibling: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak.disabled-by-tku-isolation`
- Mirror pak SHA256: `CD28346527E769B8174E650677F76B6B9F3DD1ED106AC541033F5252373A8B36`
- Files mirrored: `8`

## Safety

- No safety failures.

## Conflicting Content Paks

- `MW5Mercs-WindowsNoEditor.pak` target entries `8` mount `../../../` sha `None`

## Actions

- staged UnrealPak-built content-root mirror pak at D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\staging\MW5Mercs-zzzzTKUCompatEditorPatch-20260525-170948.pak

## Rollback

- Remove only the staged live mirror pak `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak` to return to the previous content-pak set.