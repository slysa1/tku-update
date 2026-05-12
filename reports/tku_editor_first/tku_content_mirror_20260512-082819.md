# TKU Content Mirror - 20260512-082819

Purpose: stage a late-loading `Content\Paks` mirror of the current editor-authored TKU compat package so root `/Game` assets can win over the legacy loose TKU starmap pak during a controlled runtime test.

- Apply requested: `True`
- Source pak: `E:\Games\MechWarrior5Editor\MW5Mercs\Mods\TKUCompatEditorPatch\Paks\TKUCompatEditorPatch.pak`
- Staged mirror pak: `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\staging\MW5Mercs-zzzzTKUCompatEditorPatch-20260512-082819.pak`
- Live mirror pak: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak`
- Mirror pak SHA256: `4E40BDBF396D776870896DCE890B23C8D834A357168FC80CDAC7E85CAD0D965A`
- Files mirrored: `6`

## Safety

- No safety failures.

## Conflicting Content Paks

- `MW5Mercs-WindowsNoEditor.pak` target entries `6` mount `../../../` sha `None`
- `MW5Mercs-zKnownUniverseStarmap.pak` target entries `4` mount `../../../MW5Mercs/Content/` sha `DFAC2CA2E1DEDCD96709A95A778DA1BB55EB02BB87E9E62B7DFC8320DD9F1FCB`

## Actions

- staged UnrealPak-built content-root mirror pak at D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\staging\MW5Mercs-zzzzTKUCompatEditorPatch-20260512-082819.pak
- deployed live mirror pak to E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak

## Rollback

- Remove only the staged live mirror pak `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak` to return to the previous content-pak set.