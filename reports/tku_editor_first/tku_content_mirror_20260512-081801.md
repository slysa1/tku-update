# TKU Content Mirror - 20260512-081801

Purpose: stage a late-loading `Content\Paks` mirror of the current editor-authored TKU compat package so root `/Game` assets can win over the legacy loose TKU starmap pak during a controlled runtime test.

- Apply requested: `False`
- Source pak: `E:\Games\MechWarrior5Editor\MW5Mercs\Mods\TKUCompatEditorPatch\Paks\TKUCompatEditorPatch.pak`
- Staged mirror pak: `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\staging\MW5Mercs-zzzzTKUCompatEditorPatch.pak`
- Live mirror pak: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak`
- Mirror pak SHA256: `34A15D270F1041CEB315A26940DF026E603F2E04E44B6D2DE07BA2FDCF837C7D`
- Files mirrored: `6`

## Safety

- No safety failures.

## Conflicting Content Paks

- `MW5Mercs-WindowsNoEditor.pak` target entries `6` mount `../../../` sha `DE272882DD376AF73364D6960B6F12842FB2A03B26FC82571DF10A32AC079124`
- `MW5Mercs-zKnownUniverseStarmap.pak` target entries `4` mount `../../../MW5Mercs/Content/` sha `DFAC2CA2E1DEDCD96709A95A778DA1BB55EB02BB87E9E62B7DFC8320DD9F1FCB`

## Actions

- staged mirror pak at D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\staging\MW5Mercs-zzzzTKUCompatEditorPatch.pak

## Rollback

- Remove only the staged live mirror pak `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak` to return to the previous content-pak set.