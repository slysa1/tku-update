# TKU Evidence Current Pawn Bounds Patch - 2026-05-10

## Purpose

Retest expanded map bounds without restoring old TKU `StarMapPawn` behavior.

The prior `TKUEvidenceBoundsPawn` restored the old cooked TKU pawn wholesale. It let the career load, but pressing the starmap button dropped to first-person hangar view instead of opening the starmap. That rules out the old pawn as a safe runtime asset.

This patch starts from the current vanilla `StarMapPawn` package and changes only serialized CDO defaults needed for the bounds hypothesis.

## Changes

- Added current-package name-map entries: `['PanBoundsVertical', 'PanBoundsHorizontal']`
- Added `PanBoundsVertical`: `16000.0`
- Added `PanBoundsHorizontal`: `8500.0`
- Replaced `ZoomDistanceList`: `[400.0, 550.0, 700.0, 1400.0, 1600.0, 1800.0, 3500.0]` -> `[300.0, 600.0, 900.0, 1300.0, 1800.0, 2200.0, 2800.0, 3500.0, 5000.0, 7500.0, 9000.0]`
- Replaced `ZoomLevelThresholds`: `[2000, 1000]` -> `[3500, 1000]`
- Current package CDO byte delta: `74`
- Current package name-map byte delta: `54`

## Safety Boundary

- Keeps the current `/Game/UI/FrontEnd/StarMapPawn` package and current widget/tooltip references.
- Does not restore TKU `StarMap.umap`, `StarMapActor`, `StarSystemBody`, `BaseStarMapBorderActor`, dated border actors, root data tables, employers, or factions.
- Still a cooked-package evidence patch, not the final preferred editor-authored asset.

## Build Output

- Output mod: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUEvidenceCurrentPawnBounds`
- Output pak: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUEvidenceCurrentPawnBounds\Paks\TKUEvidenceCurrentPawnBounds.pak`
- Output pak SHA256: `A7C5625A726B02256A5E79E8967F00162B52AB645B832D38994FF18763A4CA4F`

## Expected Runtime Meaning

- `success`: Career loads, starmap opens normally, and map bounds/zoom expand.
- `no_bounds_change`: Bounds are likely controlled outside StarMapPawn CDO defaults.
- `crash_or_starmap_button_failure`: Manual current-package CDO patch is unsafe; disable this mod and return to core-only baseline.

## Rollback

Disable `TKUEvidenceCurrentPawnBounds`. The stable floor remains `TKUEvidenceCorePluginOnly` alone.
