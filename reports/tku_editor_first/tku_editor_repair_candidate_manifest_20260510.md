# TKU Editor Repair Candidate Manifest - 2026-05-10

- Generated: `2026-05-10T12:36:12.292821+00:00`
- Method: local read-only reconciliation of editor traces, restored original TKU DataTable parse, and original TKU pak inventory.
- Safety: no editor assets, original paks, modlist, or runtime paks were modified.

## Live Floor

- modlist exists: `True`
- game version: `1.13.378`
- enabled mods: `['TKUEvidenceCorePluginOnly']`
- stable floor ok: `True`
- runtime pak build authorized: `False`

## Data Reconciliation

- Current editor DataTable rows: `2173`
- Current runtime CSV rows: `2173`
- Wide editor source JSON rows: `3446`
- Restored original TKU DataTable rows: `3929`
- TKU vs current ID delta: `{'left': 'tku', 'right': 'current', 'tku_count': 3929, 'current_count': 2173, 'tku_missing_from_current': 1801, 'current_missing_from_tku': 45, 'tku_missing_from_current_sample': [4001, 4002, 4003, 4004, 4005, 4006, 4007, 4008, 4009, 4010, 4011, 4012, 4013, 4014, 4015, 4016, 4017, 4018, 4019, 4020, 4021, 4022, 4023, 4024, 4025], 'current_missing_from_tku_sample': [3450, 3451, 3452, 3453, 3454, 3455, 3456, 3457, 3458, 3459, 3460, 3461, 3462, 3465, 3466, 3467, 3468, 3469, 3470, 3471, 3472, 3473, 3474, 3475, 3476]}`
- TKU vs wide source ID delta: `{'left': 'tku', 'right': 'wide', 'tku_count': 3929, 'wide_count': 3446, 'tku_missing_from_wide': 1808, 'wide_missing_from_tku': 1325, 'tku_missing_from_wide_sample': [3463, 3464, 3497, 3498, 3499, 3500, 3501, 4001, 4002, 4003, 4004, 4005, 4006, 4007, 4008, 4009, 4010, 4011, 4012, 4013, 4014, 4015, 4016, 4017, 4018], 'wide_missing_from_tku_sample': [71, 966, 967, 970, 972, 973, 974, 975, 976, 977, 1036, 1037, 1038, 1077, 1078, 1079, 1080, 1081, 1083, 1089, 1090, 1150, 1151, 1152, 1153]}`
- Coordinate ranges: `{'current_runtime_csv': {'count': 2173, 'x': {'min': -517.0, 'max': 685.0, 'span': 1202.0}, 'y': {'min': -524.0, 'max': 552.0, 'span': 1076.0}}, 'wide_source_json': {'count': 3443, 'x': {'min': -1875.9410400390625, 'max': 1935.8389892578125, 'span': 3811.780029296875}, 'y': {'min': -1919.68896484375, 'max': 1910.759033203125, 'span': 3830.447998046875}}, 'original_tku': {'count': 3929, 'x': {'min': -1877.4300537109375, 'max': 1937.3699951171875, 'span': 3814.800048828125}, 'y': {'min': -2003.9000244140625, 'max': 1912.1800537109375, 'span': 3916.080078125}}}`

## Bounds Candidate

- Current actor bounds: `{'count': 2172, 'x': {'min': 47144.0, 'max': 55752.0, 'span': 8608.0, 'center': 51448.0, 'half_span': 4304.0}, 'y': {'min': 46903.0, 'max': 56519.0, 'span': 9616.0, 'center': 51711.0, 'half_span': 4808.0}}`
- Original TKU projected level bounds: `{'count': 3929, 'x': {'min': 35304.7998046875, 'max': 66633.4404296875, 'span': 31328.640625, 'center': 50969.1201171875, 'half_span': 15664.3203125}, 'y': {'min': 36019.5595703125, 'max': 66537.9599609375, 'span': 30518.400390625, 'center': 51278.759765625, 'half_span': 15259.2001953125}, 'formula': {'level_x': '51336 + 8 * PosY', 'level_y': '51039 + 8 * PosX'}}`
- Current pawn defaults: `{'PanBoundsHorizontal': 5500.0, 'PanBoundsVertical': 4500.0, 'ZoomDistanceList': [400.0, 550.0, 700.0, 1400.0, 1600.0, 1800.0, 3500.0], 'ZoomLevelThresholds': [2000, 1000]}`
- Bounds half-span ratio TKU/current: `{'x_half_span_ratio': 3.639479626510223, 'y_half_span_ratio': 3.1737105231515184}`
- Estimated editor-authored bounds floor: `{'world_x_half_span_plus_1000': 16665, 'world_y_half_span_plus_1000': 16260}`
- Decision: Use current StarSystemBody/StarMapPawn classes and editor-authored data/level changes; do not restore old cooked pawn, body, actor, map, or border classes.

## Territory Candidate

- TKU clustered rows: `1091`
- Unique TKU cluster IDs: `69`
- Asset count if grouped by cluster ID: `69`
- Asset count if grouped by cluster/overlay/constellation variant: `172`
- Non-empty overlay/constellation variants: `103`

Top TKU clusters:
- `RepairSystem`: `204`
- `CareerCluster`: `189`
- `TaurianCorridor`: `42`
- `ClanConflict`: `29`
- `OutworldsBorder`: `28`
- `LowerClassWorlds`: `25`
- `DavionBorder`: `22`
- `LyranStrongholds`: `22`
- `AlarionPeriphery`: `21`
- `DavionKurita`: `21`
- `SteinerBorder`: `21`
- `RasalagueReaches`: `18`
- `DutchyOfAndurien`: `17`
- `FWLCommercialHub`: `17`
- `FWLInterior`: `17`
- `MarikLiaoBorder`: `17`
- `RebeliousLyranTerritory`: `17`
- `SianCommonality`: `17`
- `DroughtWorlds`: `16`
- `SteinerMarikBorder`: `16`

Generic or high-variant clusters that require explicit policy:
- `CareerCluster` rows `189`, variants `18`, risk `generic_legacy_cluster_id`
- `RepairSystem` rows `204`, variants `35`, risk `generic_legacy_cluster_id`

Legacy TKU cluster IDs that split across many current CSV clusters:
- `CareerCluster` targets `1`, no-current-row `0`, top `[{'current_cluster': '__current_no_cluster__', 'overlap_count': 189}]`
- `RepairSystem` targets `32`, no-current-row `0`, top `[{'current_cluster': 'RepairSystem_20', 'overlap_count': 20}, {'current_cluster': '__current_no_cluster__', 'overlap_count': 14}, {'current_cluster': 'RepairSystem_26', 'overlap_count': 13}, {'current_cluster': 'RepairSystem_22', 'overlap_count': 10}, {'current_cluster': 'RepairSystem_27', 'overlap_count': 9}, {'current_cluster': 'RepairSystem_23', 'overlap_count': 8}, {'current_cluster': 'RepairSystem_5', 'overlap_count': 7}, {'current_cluster': 'RepairSystem_2', 'overlap_count': 7}]`

Overlay/constellation availability:
- unique paths: `134`
- availability counts: `{'editor_loose': 20, 'missing_from_editor_base_game_and_original_tku_pak': 114}`
- current base-game sample: `[]`
- pak-only sample: `[]`
- missing sample: `[{'object_path': '/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/SafezoneCollision/Safezone_10_Blob.Safezone_10_Blob', 'package_path': '/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/SafezoneCollision/Safezone_10_Blob', 'availability': 'missing_from_editor_base_game_and_original_tku_pak'}, {'object_path': '/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/SafezoneCollision/Safezone_11_Blob.Safezone_11_Blob', 'package_path': '/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/SafezoneCollision/Safezone_11_Blob', 'availability': 'missing_from_editor_base_game_and_original_tku_pak'}, {'object_path': '/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/SafezoneCollision/Safezone_12_Blob.Safezone_12_Blob', 'package_path': '/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/SafezoneCollision/Safezone_12_Blob', 'availability': 'missing_from_editor_base_game_and_original_tku_pak'}, {'object_path': '/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/SafezoneCollision/Safezone_13_Blob.Safezone_13_Blob', 'package_path': '/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/SafezoneCollision/Safezone_13_Blob', 'availability': 'missing_from_editor_base_game_and_original_tku_pak'}, {'object_path': '/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/SafezoneCollision/Safezone_14_Blob.Safezone_14_Blob', 'package_path': '/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/SafezoneCollision/Safezone_14_Blob', 'availability': 'missing_from_editor_base_game_and_original_tku_pak'}, {'object_path': '/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/SafezoneCollision/Safezone_15_Blob.Safezone_15_Blob', 'package_path': '/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/SafezoneCollision/Safezone_15_Blob', 'availability': 'missing_from_editor_base_game_and_original_tku_pak'}, {'object_path': '/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/SafezoneCollision/Safezone_16_Blob.Safezone_16_Blob', 'package_path': '/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/SafezoneCollision/Safezone_16_Blob', 'availability': 'missing_from_editor_base_game_and_original_tku_pak'}, {'object_path': '/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/SafezoneCollision/Safezone_17_Blob.Safezone_17_Blob', 'package_path': '/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/SafezoneCollision/Safezone_17_Blob', 'availability': 'missing_from_editor_base_game_and_original_tku_pak'}]`

Original TKU pak relevant inventory:
- custom content entries: `0`
- campaign cluster entries: `0`
- DLC1 career cluster entries: `0`
- DLC1 career warzone entries: `0`
- campaign border mesh entries: `0`
- plugin war entries: `22`

Current base-game relevant inventory:
- custom content entries: `0`
- campaign cluster entries: `522`
- DLC1 career cluster entries: `274`
- DLC1 career warzone entries: `246`
- campaign border mesh entries: `0`
- plugin war entries: `0`

Decision: Modern MWClusterDataAsset overlays must be editor-authored. Original TKU DataTable columns are evidence for membership and mesh references, not a direct cooked replacement.

## Editor Authoring Gate

- Manual editor UI required: `True`
- Python commandlet create/package supported: `False`

Authorized next actions:
- Create a dedicated editor mod/project copy through the MW5 Mod Editor UI if one does not already exist.
- Import or fill an editor DataTable from the parsed original TKU rows only inside the compatibility mod.
- Regenerate or duplicate StarMap level actors using current StarSystemBody_C and the recovered placement formula.
- Create MWClusterDataAsset assets with editor-only setters/migration utility after resolving generic legacy cluster IDs.
- Save/package only after the authored assets and dependency manifest are reviewed.

Blocked actions:
- Runtime pak build from cooked StarMap assets.
- Direct substitution of original root /Game cooked assets.
- Direct substitution of old StarMapPawn, StarMapActor, StarSystemBody, StarMap.umap, BaseStarMapBorderActor, or cooked border assets.

## Decision

- Build authorized: `False`
- Next repair candidate: Editor-authored TKU data/map/cluster ModOverride candidate, prepared in MW5 Mod Editor UI from restored original TKU DataTable evidence.

Why no build yet:
- Editor Python can inspect mod APIs but commandlet creation/packaging of MW5 mod assets is not proven.
- Original TKU cluster IDs contain legacy generic RepairSystem/CareerCluster groups that need editor-side migration policy before asset writes.
- Overlay mesh dependencies must be treated as current base-game dependencies where present, and copied/imported only where absent from current content and present in the original TKU pak.
