# TKU Evidence Bounds Pawn Patch - 2026-05-10

## Purpose

Test exactly one remaining runtime symptom: the vanilla-width starmap bounds observed after the stable core-plugin-only run.

This patch is deliberately narrow. It restores only original TKU build-38 `/Game/UI/FrontEnd/StarMapPawn.uasset` and `.uexp` on top of `TKUEvidenceCorePluginOnly`.

## Evidence Gate

- User runtime evidence: `TKUEvidenceCorePluginOnly` loads successfully, but starmap panning remains bounded by vanilla limits.
- Current editor default evidence: vanilla `StarMapPawn` has `PanBoundsHorizontal=5500`, `PanBoundsVertical=4500`, and zoom distances ending at `3500`.
- Cooked package-table evidence: original TKU `StarMapPawn` and current vanilla `StarMapPawn` have matching import/export structure and both inherit native `/Script/MechWarrior.MWStarMapPawn`.
- Recovered cooked CDO values show TKU changes only the expected pan/zoom defaults for this hypothesis.
- The patch does not restore TKU `StarMap.umap`, `StarMapActor`, `StarSystemBody`, `BaseStarMapBorderActor`, dated border actors, faction/employer data, or root data tables.

## Recovered TKU Defaults

- `PanBoundsHorizontal`: `8500.0`
- `PanBoundsVertical`: `16000.0`
- `ZoomDistanceList`: `[300.0, 600.0, 900.0, 1300.0, 1800.0, 2200.0, 2800.0, 3500.0, 5000.0, 7500.0, 9000.0]`
- `ZoomLevelThresholds`: `[3500, 1000]`

## Build Output

- Output mod: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUEvidenceBoundsPawn`
- Output pak: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUEvidenceBoundsPawn\Paks\TKUEvidenceBoundsPawn.pak`
- Output pak SHA256: `0212E693BF2BB50F651235FB4A0BE7136B406C93133E09BFA86837D8B38410F0`
- Source pak SHA256: `0F23FC683DEBEC27D07FF6739137BA1E4069934082D5AFFF6B3F2161CC64C678`
- Pak entries: `2`

## Expected Runtime Meaning

- `success`: Career still loads and the starmap can pan/zoom beyond vanilla bounds. This validates StarMapPawn defaults as the bounds source and leaves overlay as a separate cluster-data problem.
- `no_bounds_change`: Bounds are controlled elsewhere, likely StarMap level actors or StarMapActor logic, and StarMapPawn should be removed again.
- `crash_or_stall`: Even though package tables looked compatible, the old cooked StarMapPawn is not safe; disable this patch and recreate the defaults in the editor/current asset pipeline.

## What This Does Not Test

- It does not fix the missing minor-power territory overlay.
- It does not prove old TKU starmap classes are safe.
- It does not authorize restoring old border actors or root faction/employer assets.

## Rollback

Disable `TKUEvidenceBoundsPawn` in `MW5Mercs\Mods\modlist.json`. `TKUEvidenceCorePluginOnly` remains the stable floor.
