# TKU Evidence Core Plugin-Only Build - 2026-05-10

## Purpose

Create a clean-source TKU baseline from the restored original build-38 pak without loading the root `/Game` substitutions that current evidence has made unsafe.

This is not a final compatibility patch. It is the next gated runtime baseline: prove that original TKU plugin content plus the original loose starmap override can load without the stale root border/starmap class stack.

## Evidence Gate

- Original `TheKnownUniverse.pak` alone is sufficient to reproduce the career-load fatal crash.
- Editor inspection shows current `StarMapActor_2570_C` and all vanilla dated border actors inherit `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor_C`.
- TKU cooked root `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor` is stale and caused the `Could not find SuperStruct BaseStarMapBorderActor_C to create StarMapActor_2570_C` crash family.
- Original TKU `StarMapActor` / `StarSystemBody` lack current cluster-data hooks; replacing only those assets produced a loading stall rather than a fix.
- Previous reduced testing showed plugin-only TKU content could load farther than the full root override set, but this build is regenerated from the restored original pak, not from failed blind artifacts.

## Build Output

- Output mod: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUEvidenceCorePluginOnly`
- Output pak: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUEvidenceCorePluginOnly\Paks\TKUEvidenceCorePluginOnly.pak`
- Output pak SHA256: `3669B40ED821BF1881BE45F3C57C16D7C2A9BA0EDDFD0845E46704DC105D222C`
- Source pak SHA256: `0F23FC683DEBEC27D07FF6739137BA1E4069934082D5AFFF6B3F2161CC64C678`
- Source entries: `2709`
- Kept entries: `2427`
- Removed root `/Game` entries: `282`

## Removed Root Groups

- `/Game/Campaign/CampaignArcs/BorderChanges`: `6`
- `/Game/UI/FrontEnd/Starmap`: `10`
- `/Game/UI/FrontEnd/StarMapPawn`: `2`
- `/Game/Levels/FrontEnd/StarMap`: `2`
- `/Game/InnerSphereData`: `6`
- `/Game/Employers`: `216`
- `/Game/Factions`: `34`
- `/Game/Campaign/Personas`: `4`
- `/Game/Libraries/MW5_TOI_Functions`: `2`
- `/Game/other`: `0`

## Next Runtime Meaning

- If this profile still crashes with the original `0x4C` hash, then plugin content or the always-loaded loose override still contains a fatal path and the plugin-only assumption is false.
- If this profile loads, it becomes the safe baseline for editor-authored current-schema repairs: map bounds via current `StarMapPawn`, overlay via `MWClusterDataAsset`, and only recreated/reparented border assets if proven necessary.
- If it loads but lacks expanded map bounds or non-major overlays, that is expected and should not be papered over by restoring old root assets.

## What Not To Restore In This Build

- Do not restore TKU root `BaseStarMapBorderActor`, `Borders3015`, or dated root border assets.
- Do not restore TKU root `StarMapActor`, `StarSystemBody`, `StarMapPawn`, or `StarMap.umap` directly.
- Do not restore TKU root employer/faction assets as a group; previous runtime evidence tied that pattern to ownership regressions.

## Evidence Sources

- `reports\tku_runtime_isolation_20260510.md`
- `reports\tku_editor_first\ue4_starmap_border_path_inspection.md`
- `reports\tku_editor_first\tku_cooked_package_refs.md`
- `reports\tku_editor_first\tku_structured_reference_findings_20260510.md`
