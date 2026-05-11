# UE4 StarMapPawn Bounds Patch Gate - 2026-05-12

- Generated: `2026-05-11T21:36:51.013792+00:00`
- Apply requested: `True`
- Asset path: `/Game/UI/FrontEnd/StarMapPawn`
- Target mod file: `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins\TKUCompatEditorPatch\ModOverride\UI\FrontEnd\StarMapPawn.uasset`
- Target pan horizontal: `17500.0`
- Target pan vertical: `17500.0`
- Target zoom distances: `[300.0, 600.0, 900.0, 1300.0, 1800.0, 2200.0, 2800.0, 3500.0, 5000.0, 7500.0, 9000.0]`
- Target zoom thresholds: `[3500, 1000]`

## Extents

- CSV extent summary: `{'path': 'D:\\Downloads\\OneDrive\\Documents\\code\\tku-update\\reports\\tku_editor_first\\tku_inner_sphere_merged_current_plus_tku_additions_20260510.csv', 'exists': True, 'encoding': 'utf-16', 'row_count_excluding_0': 3973, 'all_x': {'min': -16031.2001953125, 'max': 15297.4404296875, 'span': 31328.640625, 'half_span': 15664.3203125}, 'all_y': {'min': -15019.4404296875, 'max': 15498.9599609375, 'span': 30518.400390625, 'half_span': 15259.2001953125}, 'vanilla_subset_x': {'min': -4192.0, 'max': 4416.0, 'span': 8608.0, 'half_span': 4304.0}, 'vanilla_subset_y': {'min': -4136.0, 'max': 5480.0, 'span': 9616.0, 'half_span': 4808.0}, 'target_pan_horizontal': 17500.0, 'target_pan_vertical': 17500.0}`

## Pawn

- Asset object path: `/ModOverride/TKUCompatEditorPatch/UI/FrontEnd/StarMapPawn.StarMapPawn`
- Blueprint class: `/ModOverride/TKUCompatEditorPatch/UI/FrontEnd/StarMapPawn.StarMapPawn_C`
- CDO path: `/ModOverride/TKUCompatEditorPatch/UI/FrontEnd/StarMapPawn.Default__StarMapPawn_C`
- Defaults before: `{'pan_bounds_horizontal': 5500.0, 'pan_bounds_vertical': 4500.0, 'zoom_distance_list': [400.0, 550.0, 700.0, 1400.0, 1600.0, 1800.0, 3500.0], 'zoom_level_thresholds': [2000, 1000]}`

## Safety

- No safety failures.

## Result

- Attempted: `True`
- Applied: `True`
- Saved: `True`
- Reason: `None`
- Writes: `{'pan_bounds_horizontal': {'ok': True, 'after': 17500.0}, 'pan_bounds_vertical': {'ok': True, 'after': 17500.0}, 'zoom_distance_list': {'ok': True, 'after': [300.0, 600.0, 900.0, 1300.0, 1800.0, 2200.0, 2800.0, 3500.0, 5000.0, 7500.0, 9000.0]}, 'zoom_level_thresholds': {'ok': True, 'after': [3500, 1000]}}`
- Backup: `{'path': 'D:\\Downloads\\OneDrive\\Documents\\code\\tku-update\\reports\\tku_editor_first\\backups\\TKUCompatEditorPatch_starmap_pawn_pre_bounds_patch_20260512\\StarMapPawn.uasset', 'sha256': '2C2121628B6B968B158C2A87CDF2E50E1541761B82103A0CE0B2BDA15D4097B9'}`

## Hashes

- Target before: `2C2121628B6B968B158C2A87CDF2E50E1541761B82103A0CE0B2BDA15D4097B9`
- Target after: `3A4EC0F8DE697928057F24985E9715B6EEFA199FB56776E0C89C34212FDF1FF0`
- Base unchanged: `True`
