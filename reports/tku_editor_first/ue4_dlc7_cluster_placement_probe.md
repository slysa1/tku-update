# UE4 DLC7 Cluster Placement Probe

- Generated: `2026-05-25T05:59:08.484436+00:00`
- Target mod: `TKUCompatEditorPatch`
- Safety: read-only commandlet; no assets saved.

## Findings

- DLC7 focused asset paths discovered: 128.
- DLC7 MWClusterDataAsset assets inspected: 32.
- DLC7 place-cluster action assets inspected: 46.
- DLC7 campaign arc assets inspected: 1.
- Cluster paths mentioned by inspected actions/arcs: 311.

## Roots

- `/Game/DLC7/CampaignData/Clusters`: `{'ok': True, 'asset_path_count': 62, 'match_count': 62}`
- `/Game/DLC7/PlaceClusterActions`: `{'ok': True, 'asset_path_count': 45, 'match_count': 45}`
- `/Game/DLC7/CampaignData/CampaignArcActions`: `{'ok': True, 'asset_path_count': 34, 'match_count': 3}`
- `/Game/DLC7/CampaignData`: `{'ok': True, 'asset_path_count': 364, 'match_count': 83}`

## Assets

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_CustomMarket4_Rasalhague_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_CustomMarket4_Rasalhague_ArcAction.Default__DLC7_CustomMarket4_Rasalhague_ArcAction_C` class `DLC7_CustomMarket4_Rasalhague_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029B24EE7DB0) {id: 0}>", 'python_type': 'CampaignArcActionId'}}`
- dependencies: `1`
  - `/Game/Campaign/CampaignArcActions/StateChangeActions/CustomMarket_ArcAction`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceHiddenSystemsCluster`
- class: `Blueprint`
- cdo: `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceHiddenSystemsCluster.Default__DLC7_PlaceHiddenSystemsCluster_C` class `DLC7_PlaceHiddenSystemsCluster_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB933DAD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster.DLC7_HiddenSystems_CampaignCluster' (0x0000029B0D866980) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'DLC7_HiddenSystems_CampaignCluster', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster.DLC7_HiddenSystems_CampaignCluster', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster.DLC7_HiddenSystems_CampaignCluster', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB933DB70) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_ShowUnchartedSystems`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceRasalhagueCluster`
- class: `Blueprint`
- cdo: `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceRasalhagueCluster.Default__DLC7_PlaceRasalhagueCluster_C` class `DLC7_PlaceRasalhagueCluster_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB933F290) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_CampaignCluster1.DLC7_CampaignCluster1' (0x0000029B0D866840) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'DLC7_CampaignCluster1', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_CampaignCluster1.DLC7_CampaignCluster1', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_CampaignCluster1.DLC7_CampaignCluster1', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB933F330) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `3`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceRasalhagueCluster`
  - `/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_CampaignCluster1`
- referencers: `2`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceRasalhagueCluster`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_CampaignCluster1`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/Factions/FreeRasalhagueRepublic.FreeRasalhagueRepublic' (0x0000029B60550D40) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'FreeRasalhagueRepublic', 'get_path_name': '/Game/Factions/FreeRasalhagueRepublic.FreeRasalhagueRepublic', 'get_full_name': 'MWFactionAsset /Game/Factions/FreeRasalhagueRepublic.FreeRasalhagueRepublic', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 3, 'sample': [1644, 1637, 697], 'tail_sample': [1644, 1637, 697]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/Factions/FreeRasalhagueRepublic`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceRasalhagueCluster`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave3`

### `/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/Factions/Independent.Independent' (0x0000029B60551B40) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'Independent', 'get_path_name': '/Game/Factions/Independent.Independent', 'get_full_name': 'MWFactionAsset /Game/Factions/Independent.Independent', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 4, 'sample': [3463, 3497, 3501, 3500], 'tail_sample': [3463, 3497, 3501, 3500]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/Factions/Independent`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceHiddenSystemsCluster`

### `/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_Faction.CGB_Periphery_Faction' (0x0000029B60541980) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CGB_Periphery_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_Faction.CGB_Periphery_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_Faction.CGB_Periphery_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 3, 'sample': [1121, 1614, 1779], 'tail_sample': [1121, 1614, 1779]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_Faction`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Periphery_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave2`

### `/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/ConflictCluster_Periphery_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_Faction.CJF_Periphery_Faction' (0x0000029B60542400) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CJF_Periphery_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_Faction.CJF_Periphery_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_Faction.CJF_Periphery_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 5, 'sample': [1463, 941, 921, 922, 1484], 'tail_sample': [1463, 941, 921, 922, 1484]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_Faction`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Periphery_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave2`

### `/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_Faction.CSJ_Periphery_Faction' (0x0000029B60541EC0) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CSJ_Periphery_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_Faction.CSJ_Periphery_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_Faction.CSJ_Periphery_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 1, 'sample': [1138], 'tail_sample': [1138]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_Faction`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Periphery_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave2`

### `/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_Faction.CWF_Periphery_Faction' (0x0000029B60542940) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CWF_Periphery_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_Faction.CWF_Periphery_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_Faction.CWF_Periphery_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 11, 'sample': [1510, 1537, 1557, 1555, 1137, 1578, 1136, 1567, 1519, 1534, 1558], 'tail_sample': [1510, 1537, 1557, 1555, 1137, 1578, 1136, 1567, 1519, 1534, 1558]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_Faction`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Periphery_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave2`

### `/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Periphery/Cluster_Perifery_STM`
- class: `StaticMesh`
- dependencies: `2`
  - `/Game/UI/FrontEnd/Starmap/Materials/Factions/Warzone_MTI`
  - `/Script/NavigationSystem`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/ConflictCluster_Periphery_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Periphery/ConflictCluster_Periphery_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_Faction.CGB_Periphery_Faction' (0x0000029B60541980) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CGB_Periphery_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_Faction.CGB_Periphery_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_Faction.CGB_Periphery_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/Cluster_Perifery_STM.Cluster_Perifery_STM' (0x0000029C12832400) Class 'StaticMesh'>", 'python_type': 'StaticMesh', 'get_name': 'Cluster_Perifery_STM', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Periphery/Cluster_Perifery_STM.Cluster_Perifery_STM', 'get_full_name': 'StaticMesh /Game/DLC7/CampaignData/Clusters/Periphery/Cluster_Perifery_STM.Cluster_Perifery_STM', 'unreal_class': 'StaticMesh', 'unreal_class_path': '/Script/Engine.StaticMesh'}, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 0, 'sample': [], 'tail_sample': []}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_Faction`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/Cluster_Perifery_STM`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Periphery_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave1`

### `/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_Faction.CGB_Wave1_Faction' (0x0000029B605425C0) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CGB_Wave1_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_Faction.CGB_Wave1_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_Faction.CGB_Wave1_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 5, 'sample': [1788, 1756, 723, 1754, 785], 'tail_sample': [1788, 1756, 723, 1754, 785]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_Faction`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave1_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave3`

### `/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_Faction.CJF_Wave1_Faction' (0x0000029B60543040) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CJF_Wave1_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_Faction.CJF_Wave1_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_Faction.CJF_Wave1_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 8, 'sample': [914, 940, 916, 1075, 1494, 926, 909, 875], 'tail_sample': [914, 940, 916, 1075, 1494, 926, 909, 875]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_Faction`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave1_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave3`

### `/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_Faction.CSJ_Wave1_Faction' (0x0000029B60542B00) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CSJ_Wave1_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_Faction.CSJ_Wave1_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_Faction.CSJ_Wave1_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 10, 'sample': [1855, 912, 1812, 1824, 1839, 1863, 1899, 1937, 1844, 1887], 'tail_sample': [1855, 912, 1812, 1824, 1839, 1863, 1899, 1937, 1844, 1887]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_Faction`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave1_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave3`

### `/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_Faction.CWF_Wave1_Faction' (0x0000029B60543740) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CWF_Wave1_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_Faction.CWF_Wave1_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_Faction.CWF_Wave1_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 9, 'sample': [1694, 933, 927, 1585, 889, 834, 990, 804, 1606], 'tail_sample': [1694, 933, 927, 1585, 889, 834, 990, 804, 1606]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_Faction`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave1_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave3`

### `/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave1/Cluster_3050_w1_STM`
- class: `StaticMesh`
- dependencies: `2`
  - `/Game/UI/FrontEnd/Starmap/Materials/Factions/Warzone_MTI`
  - `/Script/NavigationSystem`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave1/ConflictCluster_Wave1_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave1/ConflictCluster_Wave1_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': None, 'cluster_overlay': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave1/Cluster_3050_w1_STM.Cluster_3050_w1_STM' (0x0000029C12831800) Class 'StaticMesh'>", 'python_type': 'StaticMesh', 'get_name': 'Cluster_3050_w1_STM', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave1/Cluster_3050_w1_STM.Cluster_3050_w1_STM', 'get_full_name': 'StaticMesh /Game/DLC7/CampaignData/Clusters/Wave1/Cluster_3050_w1_STM.Cluster_3050_w1_STM', 'unreal_class': 'StaticMesh', 'unreal_class_path': '/Script/Engine.StaticMesh'}, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 0, 'sample': [], 'tail_sample': []}, 'is_legacy_cluster': False}`
- dependencies: `3`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave1/Cluster_3050_w1_STM`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave1_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave2`

### `/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_Faction.CGB_Wave2_Faction' (0x0000029B60543200) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CGB_Wave2_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_Faction.CGB_Wave2_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_Faction.CGB_Wave2_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 2, 'sample': [1791, 1724], 'tail_sample': [1791, 1724]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_Faction`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave2_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave4`

### `/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_Faction.CJF_Wave2_Faction' (0x0000029B60543C80) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CJF_Wave2_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_Faction.CJF_Wave2_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_Faction.CJF_Wave2_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 12, 'sample': [672, 944, 1507, 924, 1547, 923, 1544, 1551, 1561, 971, 1528, 908], 'tail_sample': [672, 944, 1507, 924, 1547, 923, 1544, 1551, 1561, 971, 1528, 908]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_Faction`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave2_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave4`

### `/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_Faction.CSJ_Wave2_Faction' (0x0000029B60543900) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CSJ_Wave2_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_Faction.CSJ_Wave2_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_Faction.CSJ_Wave2_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 6, 'sample': [2232, 1912, 1871, 1818, 1811, 1923], 'tail_sample': [2232, 1912, 1871, 1818, 1811, 1923]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_Faction`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave2_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave4`

### `/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_Faction.CWF_Wave2_Faction' (0x0000029B60543E40) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CWF_Wave2_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_Faction.CWF_Wave2_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_Faction.CWF_Wave2_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 5, 'sample': [1573, 1706, 1616, 718, 1637], 'tail_sample': [1573, 1706, 1616, 718, 1637]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_Faction`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave2_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave4`

### `/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave2/Cluster_3050_w2_STM`
- class: `StaticMesh`
- dependencies: `2`
  - `/Game/UI/FrontEnd/Starmap/Materials/Factions/Warzone_MTI`
  - `/Script/NavigationSystem`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave2/ConflictCluster_Wave2_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave2/ConflictCluster_Wave2_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': None, 'cluster_overlay': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave2/Cluster_3050_w2_STM.Cluster_3050_w2_STM' (0x0000029C12830C00) Class 'StaticMesh'>", 'python_type': 'StaticMesh', 'get_name': 'Cluster_3050_w2_STM', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave2/Cluster_3050_w2_STM.Cluster_3050_w2_STM', 'get_full_name': 'StaticMesh /Game/DLC7/CampaignData/Clusters/Wave2/Cluster_3050_w2_STM.Cluster_3050_w2_STM', 'unreal_class': 'StaticMesh', 'unreal_class_path': '/Script/Engine.StaticMesh'}, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 0, 'sample': [], 'tail_sample': []}, 'is_legacy_cluster': False}`
- dependencies: `3`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave2/Cluster_3050_w2_STM`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave2_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave3`

### `/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_Faction.CGB_Wave3_Faction' (0x0000029B605482C0) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CGB_Wave3_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_Faction.CGB_Wave3_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_Faction.CGB_Wave3_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 2, 'sample': [1797, 1731], 'tail_sample': [1797, 1731]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_Faction`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave3_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5`

### `/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_Faction.CJF_Wave3_Faction' (0x0000029B60548800) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CJF_Wave3_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_Faction.CJF_Wave3_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_Faction.CJF_Wave3_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 5, 'sample': [949, 1471, 957, 1459, 1505], 'tail_sample': [949, 1471, 957, 1459, 1505]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_Faction`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave3_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5`

### `/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_Faction.CSJ_Wave3_Faction' (0x0000029B60548480) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CSJ_Wave3_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_Faction.CSJ_Wave3_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_Faction.CSJ_Wave3_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 6, 'sample': [1073, 1858, 1903, 1894, 1833, 1810], 'tail_sample': [1073, 1858, 1903, 1894, 1833, 1810]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_Faction`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave3_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5`

### `/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_Faction.CWF_Wave3_Faction' (0x0000029B60548F00) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CWF_Wave3_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_Faction.CWF_Wave3_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_Faction.CWF_Wave3_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 10, 'sample': [1651, 1630, 1581, 1688, 1600, 1629, 1602, 1587, 952, 1568], 'tail_sample': [1651, 1630, 1581, 1688, 1600, 1629, 1602, 1587, 952, 1568]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_Faction`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave3_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5`

### `/Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave3/Cluster_3050_w3_STM`
- class: `StaticMesh`
- dependencies: `2`
  - `/Game/UI/FrontEnd/Starmap/Materials/Factions/Warzone_MTI`
  - `/Script/NavigationSystem`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave3/ConflictCluster_Wave3_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave3/ConflictCluster_Wave3_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/ClusterOwners/HiddenFactionInfo/Hidden_ClanGhostBear.Hidden_ClanGhostBear' (0x0000029B6054B200) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'Hidden_ClanGhostBear', 'get_path_name': '/Game/DLC7/ClusterOwners/HiddenFactionInfo/Hidden_ClanGhostBear.Hidden_ClanGhostBear', 'get_full_name': 'MWFactionAsset /Game/DLC7/ClusterOwners/HiddenFactionInfo/Hidden_ClanGhostBear.Hidden_ClanGhostBear', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave3/Cluster_3050_w3_STM.Cluster_3050_w3_STM' (0x0000029C111F3800) Class 'StaticMesh'>", 'python_type': 'StaticMesh', 'get_name': 'Cluster_3050_w3_STM', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave3/Cluster_3050_w3_STM.Cluster_3050_w3_STM', 'get_full_name': 'StaticMesh /Game/DLC7/CampaignData/Clusters/Wave3/Cluster_3050_w3_STM.Cluster_3050_w3_STM', 'unreal_class': 'StaticMesh', 'unreal_class_path': '/Script/Engine.StaticMesh'}, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 1, 'sample': [1764], 'tail_sample': [1764]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave3/Cluster_3050_w3_STM`
  - `/Game/DLC7/ClusterOwners/HiddenFactionInfo/Hidden_ClanGhostBear`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave3_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave4`

### `/Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_Faction.CGB_Wave4_Faction' (0x0000029B605489C0) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CGB_Wave4_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_Faction.CGB_Wave4_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_Faction.CGB_Wave4_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 8, 'sample': [1760, 1713, 1776, 1729, 881, 1774, 1733, 640], 'tail_sample': [1760, 1713, 1776, 1729, 881, 1774, 1733, 640]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_Faction`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave4_PlaceCluster_ArcAction`

### `/Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_Faction.CJF_Wave4_Faction' (0x0000029B60549600) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CJF_Wave4_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_Faction.CJF_Wave4_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_Faction.CJF_Wave4_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 14, 'sample': [421, 1520, 958, 1489, 1579, 1524, 1526, 1566, 1491, 1538, 1550, 1504, 1556, 1563], 'tail_sample': [958, 1489, 1579, 1524, 1526, 1566, 1491, 1538, 1550, 1504, 1556, 1563]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_Faction`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave4_PlaceCluster_ArcAction`

### `/Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_Faction.CSJ_Wave4_Faction' (0x0000029B605490C0) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CSJ_Wave4_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_Faction.CSJ_Wave4_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_Faction.CSJ_Wave4_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 5, 'sample': [1865, 1825, 1782, 918, 1814], 'tail_sample': [1865, 1825, 1782, 918, 1814]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_Faction`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave4_PlaceCluster_ArcAction`

### `/Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_Faction.CWF_Wave4_Faction' (0x0000029B60549D00) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CWF_Wave4_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_Faction.CWF_Wave4_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_Faction.CWF_Wave4_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 16, 'sample': [1604, 1695, 1583, 1681, 1689, 1633, 1649, 1130, 1610, 605, 1707, 1598, 1675, 1582, 1661, 1577], 'tail_sample': [1689, 1633, 1649, 1130, 1610, 605, 1707, 1598, 1675, 1582, 1661, 1577]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_Faction`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave4_PlaceCluster_ArcAction`

### `/Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave4/Cluster_3050_w4_STM`
- class: `StaticMesh`
- dependencies: `2`
  - `/Game/UI/FrontEnd/Starmap/Materials/Factions/Warzone_MTI`
  - `/Script/NavigationSystem`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave4/ConflictCluster_Wave4_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave4/ConflictCluster_Wave4_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': None, 'cluster_overlay': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave4/Cluster_3050_w4_STM.Cluster_3050_w4_STM' (0x0000029C111F2C00) Class 'StaticMesh'>", 'python_type': 'StaticMesh', 'get_name': 'Cluster_3050_w4_STM', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave4/Cluster_3050_w4_STM.Cluster_3050_w4_STM', 'get_full_name': 'StaticMesh /Game/DLC7/CampaignData/Clusters/Wave4/Cluster_3050_w4_STM.Cluster_3050_w4_STM', 'unreal_class': 'StaticMesh', 'unreal_class_path': '/Script/Engine.StaticMesh'}, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 0, 'sample': [], 'tail_sample': []}, 'is_legacy_cluster': False}`
- dependencies: `3`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave4/Cluster_3050_w4_STM`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave4_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByEndOfInvasion`

### `/Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_Faction.CGB_Wave5_Faction' (0x0000029B605497C0) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CGB_Wave5_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_Faction.CGB_Wave5_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_Faction.CGB_Wave5_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 18, 'sample': [1732, 677, 1699, 1698, 1735, 1714, 1730, 1720, 1740, 722, 844, 1711, 1742, 1741, 1757, 389, 553, 710], 'tail_sample': [1730, 1720, 1740, 722, 844, 1711, 1742, 1741, 1757, 389, 553, 710]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_Faction`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave5_PlaceCluster_ArcAction`

### `/Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_Faction.CJF_Wave5_Faction' (0x0000029B6054A400) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CJF_Wave5_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_Faction.CJF_Wave5_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_Faction.CJF_Wave5_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 7, 'sample': [1500, 583, 1540, 1618, 208, 1584, 1612], 'tail_sample': [1500, 583, 1540, 1618, 208, 1584, 1612]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_Faction`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave5_PlaceCluster_ArcAction`

### `/Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_Faction.CSJ_Wave5_Faction' (0x0000029B60549EC0) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CSJ_Wave5_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_Faction.CSJ_Wave5_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_Faction.CSJ_Wave5_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 16, 'sample': [654, 429, 1890, 1870, 618, 1853, 390, 1752, 1830, 1854, 659, 1847, 760, 1819, 1878, 557], 'tail_sample': [618, 1853, 390, 1752, 1830, 1854, 659, 1847, 760, 1819, 1878, 557]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_Faction`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave5_PlaceCluster_ArcAction`

### `/Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_Faction.CWF_Wave5_Faction' (0x0000029B6054AB00) Class 'MWFactionAsset'>", 'python_type': 'MWFactionAsset', 'get_name': 'CWF_Wave5_Faction', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_Faction.CWF_Wave5_Faction', 'get_full_name': 'MWFactionAsset /Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_Faction.CWF_Wave5_Faction', 'unreal_class': 'MWFactionAsset', 'unreal_class_path': '/Script/MechWarrior.MWFactionAsset'}, 'cluster_overlay': None, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 32, 'sample': [350, 1622, 664, 1638, 751, 1656, 1608, 1639, 1673, 843, 1663, 1631, 1643, 1640, 1594, 479, 477, 1666, 775, 1659, 1605, 853, 8, 690, 728, 706, 1646, 522, 1625, 549, 1632, 1613], 'tail_sample': [1605, 853, 8, 690, 728, 706, 1646, 522, 1625, 549, 1632, 1613]}, 'is_legacy_cluster': False}`
- dependencies: `4`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_Faction`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave5_PlaceCluster_ArcAction`

### `/Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_Faction`
- class: `MWFactionAsset`
- dependencies: `2`
  - `/Game/Campaign/Clusters/_common/Faction_StringTable`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave5/Cluster_3051_w5_STM`
- class: `StaticMesh`
- dependencies: `2`
  - `/Game/UI/FrontEnd/Starmap/Materials/Factions/Warzone_MTI`
  - `/Script/NavigationSystem`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Clusters/Wave5/ConflictCluster_Wave5_ClusterAsset`

### `/Game/DLC7/CampaignData/Clusters/Wave5/ConflictCluster_Wave5_ClusterAsset`
- class: `MWClusterDataAsset`
- asset properties: `{'cluster_faction_asset': None, 'cluster_overlay': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave5/Cluster_3051_w5_STM.Cluster_3051_w5_STM' (0x0000029C111F2000) Class 'StaticMesh'>", 'python_type': 'StaticMesh', 'get_name': 'Cluster_3051_w5_STM', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave5/Cluster_3051_w5_STM.Cluster_3051_w5_STM', 'get_full_name': 'StaticMesh /Game/DLC7/CampaignData/Clusters/Wave5/Cluster_3051_w5_STM.Cluster_3051_w5_STM', 'unreal_class': 'StaticMesh', 'unreal_class_path': '/Script/Engine.StaticMesh'}, 'cluster_constellation': None, 'system_ids': {'kind': 'Set', 'count': 0, 'sample': [], 'tail_sample': []}, 'is_legacy_cluster': False}`
- dependencies: `3`
  - `/Game/Campaign/_common/ClusterToiDataFragment`
  - `/Game/DLC7/CampaignData/Clusters/Wave5/Cluster_3051_w5_STM`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave5_PlaceCluster_ArcAction`

### `/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague`
- class: `MWCampaignArcAsset`
- asset properties: `{'campaign_arc_script': {'repr': "<Object '/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague.DLC7_Pt2_Rasalhague:LinearCampaignArcScript_C_0' (0x0000029BEB59DF80) Class 'LinearCampaignArcScript_C'>", 'python_type': 'MWCampaignArcScript', 'get_name': 'LinearCampaignArcScript_C_0', 'get_path_name': '/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague.DLC7_Pt2_Rasalhague:LinearCampaignArcScript_C_0', 'get_full_name': 'LinearCampaignArcScript_C /Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague.DLC7_Pt2_Rasalhague:LinearCampaignArcScript_C_0', 'unreal_class': 'LinearCampaignArcScript_C', 'unreal_class_path': '/Game/DLC2/CampaignData/_CampaignStructsAndScripts/LinearCampaignArcScript.LinearCampaignArcScript_C'}, 'campaign_event_list': {'repr': '<Struct \'CampaignArcEventList\' (0x0000029C163D24E8) {campaign_events: ((EventName="Pt.2_FailureCheck",TriggerConditions=(TriggerType=Oneoff,Events=((Condition=NotResolved,EventIdentifier=(EventName="Pt.2_AbandonTracker",CampaignArc=MWCampaignArcAsset\'"/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague.DLC7_Pt2_Rasalhague"\')),(Condition=NotResolved,EventIdentifier=(EventName="Pt.2_End",CampaignArc=MWCampaignArcAsset\'"/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague.DLC7_Pt2_Rasalhague"\'))))),(EventName="Pt.2_AbandonTracker",TriggerConditions=(TriggerType=Oneoff,Events=((Condition=HasTriggered,EventIdentifier=(EventName="Pt.2_Start",CampaignArc=MWCampaignArcAsset\'"/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague.DLC7_Pt2_Rasalhague"\')),(Condition=NotResolved,EventIdentifier=(EventName="Pt.2_FailureCheck",CampaignArc=MWCampaignArcAsset\'"/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague.DLC7_Pt2_Rasalhague"\')))),ExpiryConditions=(Events=((Condition=Triggerable,bInvertCondition=True,EventIdentifier=(EventName="Pt.2_End",CampaignArc=MWCampaignArcAsset\'"/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague.DLC7_Pt2_Rasalhague"\')))),bHasExpiryConditions=True,CampaignActions=(/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction.AbandonContractTracker_ArcAction_C)),(EventName="Pt.2_Start",TriggerConditions=(Events=((Condition=HasTriggered,EventIdentifier=(EventName="Pt1.2_End",CampaignArc=MWCampaignArcAsset\'"/Game/DLC7/CampaignData/DLC7_Pt1-2_LastFrontier.DLC7_Pt1-2_LastFrontier"\'))),DLC=(bCheck=True,DLCAsset=MWDLCAsset\'"/Game/DLC7/DLC_7.DLC_7"\')),ExpiryConditions=(Events=((EventIdentifier=(EventName="Pt.2_FailureCheck",CampaignArc=MWCampaignArcAsset\'"/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague.DLC7_Pt2_Rasalhague"\')))),bHasExpiryConditions=True),(EventName="Pt.2_TravelEvent",TriggerConditions=(Events=((EventIdentifier=(EventName="Pt.2_Start",CampaignArc=MWCampaignArcAsset\'"/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague.DLC7_Pt2_Rasalhague"\')))),ExpiryConditions=(Events=((EventIdentifier=(EventName="Pt.2_FailureCheck",CampaignArc=MWCampaignArcAsset\'"/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague.DLC7_Pt2_Rasalhague"\')))),bHasExpiryConditions=True,CampaignActions=(/Game/DLC7/CampaignData/CampaignArcActions/TravelTo_D7M4.TravelTo_D7M4_C,/Game/DLC7/CampaignData/CampaignArcActions/DLC7_CustomMarket4_Rasalhague_ArcAction.DLC7_CustomMarket4_Rasalhague_ArcAction_C)),(EventName="Pt.2_TravelReachedEvent",TriggerConditions=(Events=((EventIdentifier=(EventName="Pt.2_TravelEvent",CampaignArc=MWCampaignArcAsset\'"/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague.DLC7_Pt2_Rasalhague"\'))),StarSystemTrigger=(bCheck=True,StarSystemId=697)),ExpiryConditions=(Events=((EventIdentifier=(EventName="Pt.2_FailureCheck",CampaignArc=MWCampaignArcAsset\'"/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague.DLC7_Pt2_Rasalhague"\')))),bHasExpiryConditions=True),(EventName="D7M4_Offer",TriggerConditions=(TriggerType=Always,Events=((EventIdentifier=(EventName="Pt.2_TravelReachedEvent",CampaignArc=MWCampaignArcAsset\'"/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague.DLC7_Pt2_Rasalhague"\')))),ExpiryConditions=(Events=((Condition=Triggerable,bInvertCondition=True,EventIdentifier=(EventName="D7M4_Complete",CampaignArc=MWCampaignArcAsset\'"/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague.DLC7_Pt2_Rasalhague"\')))),bHasExpiryConditions=True,CampaignActions=(/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_Offer.D7M4_Offer_C)),(EventName="D7M4_Place",TriggerConditions=(TriggerType=Always,Objectives=((Objective=MWMetagameObjectiveAsset\'"/Game/DLC7/CampaignData/Missions/D7_Spaceport/D7M4_Prompt.D7M4_Prompt"\'))),ExpiryConditions=(Events=((Condition=Triggerable,bInvertCondition=True,EventIdentifier=(EventName="D7M4_Complete",CampaignArc=MWCampaignArcAsset\'"/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague.DLC7_Pt2_Rasalhague"\')))),bHasExpiryConditions=True,CampaignActions=(/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_Place_Mission.D7M4_Place_Mission_C)),(EventName="D7M4_AutoAcceptObjective",TriggerConditions=(Objectives=((Objective=MWMetagameObjectiveAsset\'"/Game/DLC7/CampaignData/Missions/D7_Spaceport/D7M4_Prompt.D7M4_Prompt"\',Condition=Offered))),ExpiryConditions=(Events=((Condition=Triggerable,bInvertCondition=True,EventIdentifier=(EventName="D7M4_Complete",CampaignArc=MWCampaignArcAsset\'"/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague.DLC7_Pt2_Rasalhague"\')))),bHasExpiryConditions=True,CampaignActions=(/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_AutoAcceptObjective.D7M4_AutoAcceptObjective_C)),(EventName="D7M4_AutoAcceptMission",TriggerConditions=(Scenarios=((Scenario=MWScenarioSpecificationAsset\'"/Game/DLC7/CampaignData/Missions/D7_Spaceport/D7_Spaceport_Mission_Scenario.D7_Spaceport_Mission_Scenario"\',Condition=Offered)),AdditionalTriggers=((CustomEvent=/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady.HasNoMissionsReady_C))),ExpiryConditions=(Events=((Condition=Triggerable,bInvertCondition=True,EventIdentifier=(EventName="D7M4_Complete",CampaignArc=MWCampaignArcAsset\'"/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague.DLC7_Pt2_Rasalhague"\')))),bHasExpiryConditions=True,CampaignActions=(/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_AutoAcceptMission.D7M4_AutoAcceptMission_C)),(EventName="D7M4_Complete",TriggerConditions=(TriggerType=Oneoff,Scenarios=((Scenario=MWScenarioSpecificationAsset\'"/Game/DLC7/CampaignData/Missions/D7_Spaceport/D7_Spaceport_Mission_Scenario.D7_Spaceport_Mission_Scenario"\',Condition=Succeeded))),ExpiryConditions=(Events=((EventIdentifier=(EventName="Pt.2_FailureCheck",CampaignArc=MWCampaignArcAsset\'"/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague.DLC7_Pt2_Rasalhague"\')))),bHasExpiryConditions=True,CampaignActions=(/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_Completed.D7M4_Completed_C,/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/Unlock_D7M4_InstantAction.Unlock_D7M4_InstantAction_C)),(EventName="Pt.2_End",TriggerConditions=(Events=((Condition=HasTriggered,EventIdentifier=(EventName="D7M4_Complete",CampaignArc=MWCampaignArcAsset\'"/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague.DLC7_Pt2_Rasalhague"\'))),Objectives=((Objective=MWMetagameObjectiveAsset\'"/Game/DLC7/CampaignData/Missions/D7_Spaceport/D7M4_Prompt.D7M4_Prompt"\',Condition=Completed))),ExpiryConditions=(Events=((EventIdentifier=(EventName="Pt.2_FailureCheck",CampaignArc=MWCampaignArcAsset\'"/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague.DLC7_Pt2_Rasalhague"\')))),bHasExpiryConditions=True))}>', 'python_type': 'CampaignArcEventList'}, 'run_campaign_arc_script_on_save': True, 'sub_campaigns': {'kind': 'Set', 'count': 0, 'sample': [], 'tail_sample': []}}`
- dependencies: `18`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/LinearCampaignArcScript`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_CustomMarket4_Rasalhague_ArcAction`
  - `/Game/DLC7/CampaignData/CampaignArcActions/TravelTo_D7M4`
  - `/Game/DLC7/CampaignData/DLC7_Pt1-2_LastFrontier`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_AutoAcceptMission`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_AutoAcceptObjective`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_Completed`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_Offer`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_Place_Mission`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_Reset_Scenario`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/Show_D7M4`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/Unlock_D7M4_InstantAction`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/D7M4_Prompt`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/D7_Spaceport_Mission_Scenario`
  - `/Game/DLC7/DLC_7`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/CampaignData/DLC7_CoreCampaign`
  - `/Game/DLC7/CampaignData/DLC7_Pt0_Warnings`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_AutoAcceptMission`
- class: `Blueprint`
- cdo: `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_AutoAcceptMission.Default__D7M11_AutoAcceptMission_C` class `D7M11_AutoAcceptMission_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BF85F9DD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}}`
- dependencies: `2`
  - `/Game/DLC2/CampaignData/AutoAcceptMission_ArcAction`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7_WavesDefend_Mission_Scenario`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_AutoAcceptObjective`
- class: `Blueprint`
- cdo: `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_AutoAcceptObjective.Default__D7M11_AutoAcceptObjective_C` class `D7M11_AutoAcceptObjective_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BF85FA4F0) {id: 0}>", 'python_type': 'CampaignArcActionId'}}`
- dependencies: `2`
  - `/Game/DLC2/CampaignData/AutoAcceptObjective_ArcAction`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7M11_Prompt`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_Completed`
- class: `Blueprint`
- cdo: `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_Completed.Default__D7M11_Completed_C` class `D7M11_Completed_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029C19276C30) {id: 0}>", 'python_type': 'CampaignArcActionId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/StateChangeActions/SetObjectiveState_ArcAction`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7M11_Prompt`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_Offer`
- class: `Blueprint`
- cdo: `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_Offer.Default__D7M11_Offer_C` class `D7M11_Offer_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029C19276B50) {id: 0}>", 'python_type': 'CampaignArcActionId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/StateChangeActions/SetObjectiveState_ArcAction`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7M11_Prompt`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_Place_Mission`
- class: `Blueprint`
- cdo: `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_Place_Mission.Default__D7M11_Place_Mission_C` class `D7M11_Place_Mission_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BA6AA42D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}}`
- dependencies: `3`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceMission_ArcAction`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7M11_Prompt`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7_WavesDefend_Mission_Scenario`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_Reset_Scenario`
- class: `Blueprint`
- cdo: `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_Reset_Scenario.Default__D7M11_Reset_Scenario_C` class `D7M11_Reset_Scenario_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029C194AC850) {id: 0}>", 'python_type': 'CampaignArcActionId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/ResetScenario_ArcAction`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7_WavesDefend_Mission_Scenario`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/Show_D7M11`
- class: `Blueprint`
- cdo: `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/Show_D7M11.Default__Show_D7M11_C` class `Show_D7M11_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029B9F7FFC90) {id: 0}>", 'python_type': 'CampaignArcActionId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/ShowSideQuest_ArcAction`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7M11_Prompt`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/Unlock_D7M11_InstantAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/Unlock_D7M11_InstantAction.Default__Unlock_D7M11_InstantAction_C` class `Unlock_D7M11_InstantAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029C19580B60) {id: 0}>", 'python_type': 'CampaignArcActionId'}}`
- dependencies: `1`
  - `/Game/Campaign/CampaignArcActions/StateChangeActions/UnlockInstantActionScenario_ArcAction`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7M11_Briefing`
- class: `MWBriefingAsset`
- dependencies: `3`
  - `/Game/Campaign/Personas/Ryana`
  - `/Game/Factions/Mercenaries`
  - `/Script/MechWarrior`
- referencers: `0`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7M11_Prompt`
- class: `MWMetagameObjectiveAsset`
- dependencies: `4`
  - `/Game/Campaign/_common/BaseObjectiveContext`
  - `/Game/Employers/InterstellarExpeditions`
  - `/Script/GameplayTags`
  - `/Script/MechWarrior`
- referencers: `6`
  - `/Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_AutoAcceptObjective`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_Completed`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_Offer`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_Place_Mission`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/Show_D7M11`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7_WavesDefend_BattleGrid`
- class: `Texture2D`
- dependencies: `0`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/Level/D7_WavesDefend_Mission_Enemies_AreaTile`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7_WavesDefend_Biome`
- class: `MWBiomeAsset`
- dependencies: `1`
  - `/Script/MechWarrior`
- referencers: `0`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7_WavesDefend_Mission_AreaSpec`
- class: `MWAreaSpecificationAsset`
- dependencies: `25`
  - `/Game/DLC7/CampaignData/Missions/D7_Investigate/D7_Investigate_Biome`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/Level/D7_WavesDefend_Mission_Enemies_AreaTile`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/Level/D7_WavesDefend_Mission_Friendlies_AreaTile`
  - `/Game/DLC7/Dialogue/Missions/D07WAVESDEFEND`
  - `/Game/DLC7/Objects/Mechs/CLANS/Adder/UnitCard/ADR-PRIME_UnitCard`
  - `/Game/DLC7/Objects/Mechs/CLANS/FireMoth/UnitCard/FMT-PRIME_UnitCard`
  - `/Game/DLC7/Objects/Mechs/CLANS/Gargoyle/UnitCard/GAR-PRIME_UnitCard`
  - `/Game/DLC7/Objects/Mechs/CLANS/Hellbringer/Unitcard/HBR-PRIME_UnitCard`
  - `/Game/DLC7/Objects/Mechs/CLANS/KitFox/UnitCard/KFX-PRIME_UnitCard`
  - `/Game/DLC7/Objects/Mechs/CLANS/Maddog/UnitCard/MDD-PRIME_UnitCard`
  - `/Game/DLC7/Objects/Mechs/CLANS/Nova/UnitCard/NVA-PRIME_UnitCard`
  - `/Game/DLC7/Objects/Mechs/CLANS/ShadowCat/UnitCard/SHC-PRIME_UnitCard`
  - `/Game/DLC7/Objects/Mechs/CLANS/Stormcrow/UnitCard/SCR-PRIME_UnitCard`
  - `/Game/DLC7/Objects/Mechs/CLANS/Summoner/UnitCard/SMN-PRIME_UnitCard`
  - `/Game/DLC7/Objects/Mechs/CLANS/TimberWolf/UnitCard/TBR-PRIME_UnitCard`
  - `/Game/DLC7/Objects/Mechs/CLANS/Viper/UnitCard/VPR-PRIME_UnitCard`
  - `/Game/Modes/MissionDirectorSystem/MissionSpecificationAsset/ObjectiveChainMissionParameter`
  - `/Game/Objects/Mechs/Atlas/UnitCard/AS7-D_UnitCard`
  - `/Game/Objects/Mechs/Awesome/UnitCard/AWS-8Q_UnitCard`
  - `/Game/Objects/Mechs/Grasshopper/UnitCard/GHR-5J_UnitCard`
  - `/Game/Objects/Mechs/Victor/UnitCard/VTR-9B_UnitCard`
  - `/Game/Quirks/UnitCard_PilotSkillLevel_Quirk`
  - `/Game/Quirks/UnitCard_WeaponTechLevel_Quirk`
  - `/Script/GameplayTags`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7_WavesDefend_Mission_Scenario`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7_WavesDefend_Mission_Scenario`
- class: `MWScenarioSpecificationAsset`
- dependencies: `5`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7_WavesDefend_Mission_AreaSpec`
  - `/Game/DLC7/UI/Textures/ghost_DLC7_icon_color_256px_UIX`
  - `/Game/DLC7/UI/Textures/ghost_DLC7_icon_white_256px_UIX`
  - `/Script/GameplayTags`
  - `/Script/MechWarrior`
- referencers: `4`
  - `/Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_AutoAcceptMission`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_Place_Mission`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_Reset_Scenario`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/Level/D7_WavesDefend_Garrison_TileElement`
- class: `MWTileElementAsset`
- dependencies: `3`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/Level/D7_WavesDefend_Garrison`
  - `/Script/GameplayTags`
  - `/Script/MechWarrior`
- referencers: `0`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/Level/D7_WavesDefend_Mission_Enemies_AreaTile`
- class: `MWAreaTileAsset`
- dependencies: `4`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7_WavesDefend_BattleGrid`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/Level/D7_WavesDefend_Enemies_MRK`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/Level/D7_WavesDefend_MainTile`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7_WavesDefend_Mission_AreaSpec`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/Level/D7_WavesDefend_Mission_Friendlies_AreaTile`
- class: `MWAreaTileAsset`
- dependencies: `2`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/Level/D7_WavesDefend_Friendlies_MRK`
  - `/Script/MechWarrior`
- referencers: `1`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7_WavesDefend_Mission_AreaSpec`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Periphery_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Periphery_PlaceCluster_ArcAction.Default__CGB_Periphery_PlaceCluster_ArcAction_C` class `CGB_Periphery_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB8B1BA10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset.CGB_Periphery_ClusterAsset' (0x0000029B0D867880) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CGB_Periphery_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset.CGB_Periphery_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset.CGB_Periphery_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB8B1BAB0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave1_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave1_PlaceCluster_ArcAction.Default__CGB_Wave1_PlaceCluster_ArcAction_C` class `CGB_Wave1_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB8B1AED0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_ClusterAsset.CGB_Wave1_ClusterAsset' (0x0000029B0DB0C400) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CGB_Wave1_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_ClusterAsset.CGB_Wave1_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_ClusterAsset.CGB_Wave1_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB8B1AF70) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave2_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave2_PlaceCluster_ArcAction.Default__CGB_Wave2_PlaceCluster_ArcAction_C` class `CGB_Wave2_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB92D90D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_ClusterAsset.CGB_Wave2_ClusterAsset' (0x0000029B0DB0E340) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CGB_Wave2_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_ClusterAsset.CGB_Wave2_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_ClusterAsset.CGB_Wave2_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB92D9170) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave3_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave3_PlaceCluster_ArcAction.Default__CGB_Wave3_PlaceCluster_ArcAction_C` class `CGB_Wave3_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB92D9D50) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_ClusterAsset.CGB_Wave3_ClusterAsset' (0x0000029B0DB0E840) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CGB_Wave3_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_ClusterAsset.CGB_Wave3_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_ClusterAsset.CGB_Wave3_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB92D9DF0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave4_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave4_PlaceCluster_ArcAction.Default__CGB_Wave4_PlaceCluster_ArcAction_C` class `CGB_Wave4_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB92D9FD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_ClusterAsset.CGB_Wave4_ClusterAsset' (0x0000029B0DB0ED40) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CGB_Wave4_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_ClusterAsset.CGB_Wave4_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_ClusterAsset.CGB_Wave4_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB92DA070) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave5_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave5_PlaceCluster_ArcAction.Default__CGB_Wave5_PlaceCluster_ArcAction_C` class `CGB_Wave5_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB92D95D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_ClusterAsset.CGB_Wave5_ClusterAsset' (0x0000029B0DB0D580) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CGB_Wave5_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_ClusterAsset.CGB_Wave5_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_ClusterAsset.CGB_Wave5_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB92D9670) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Periphery_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Periphery_PlaceCluster_ArcAction.Default__CJF_Periphery_PlaceCluster_ArcAction_C` class `CJF_Periphery_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB945FF10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_ClusterAsset.CJF_Periphery_ClusterAsset' (0x0000029B0DB0DBC0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CJF_Periphery_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_ClusterAsset.CJF_Periphery_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_ClusterAsset.CJF_Periphery_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB945FFB0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave1_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave1_PlaceCluster_ArcAction.Default__CJF_Wave1_PlaceCluster_ArcAction_C` class `CJF_Wave1_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB945CE50) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_ClusterAsset.CJF_Wave1_ClusterAsset' (0x0000029B0DB0C680) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CJF_Wave1_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_ClusterAsset.CJF_Wave1_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_ClusterAsset.CJF_Wave1_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB945CEF0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave2_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave2_PlaceCluster_ArcAction.Default__CJF_Wave2_PlaceCluster_ArcAction_C` class `CJF_Wave2_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB945E750) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_ClusterAsset.CJF_Wave2_ClusterAsset' (0x0000029B0DB0E480) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CJF_Wave2_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_ClusterAsset.CJF_Wave2_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_ClusterAsset.CJF_Wave2_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB945E7F0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave3_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave3_PlaceCluster_ArcAction.Default__CJF_Wave3_PlaceCluster_ArcAction_C` class `CJF_Wave3_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB93D7B50) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_ClusterAsset.CJF_Wave3_ClusterAsset' (0x0000029B0DB0E980) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CJF_Wave3_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_ClusterAsset.CJF_Wave3_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_ClusterAsset.CJF_Wave3_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB93D7BF0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave4_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave4_PlaceCluster_ArcAction.Default__CJF_Wave4_PlaceCluster_ArcAction_C` class `CJF_Wave4_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB93D7A10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_ClusterAsset.CJF_Wave4_ClusterAsset' (0x0000029B0DB0EFC0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CJF_Wave4_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_ClusterAsset.CJF_Wave4_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_ClusterAsset.CJF_Wave4_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB93D7AB0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave5_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave5_PlaceCluster_ArcAction.Default__CJF_Wave5_PlaceCluster_ArcAction_C` class `CJF_Wave5_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB93D7510) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_ClusterAsset.CJF_Wave5_ClusterAsset' (0x0000029B0DB0D800) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CJF_Wave5_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_ClusterAsset.CJF_Wave5_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_ClusterAsset.CJF_Wave5_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB93D75B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Periphery_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Periphery_PlaceCluster_ArcAction.Default__CSJ_Periphery_PlaceCluster_ArcAction_C` class `CSJ_Periphery_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB96301D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_ClusterAsset.CSJ_Periphery_ClusterAsset' (0x0000029B0DB0DF80) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CSJ_Periphery_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_ClusterAsset.CSJ_Periphery_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_ClusterAsset.CSJ_Periphery_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB9630270) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave1_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave1_PlaceCluster_ArcAction.Default__CSJ_Wave1_PlaceCluster_ArcAction_C` class `CSJ_Wave1_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB9630A90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_ClusterAsset.CSJ_Wave1_ClusterAsset' (0x0000029B0DB0CA40) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CSJ_Wave1_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_ClusterAsset.CSJ_Wave1_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_ClusterAsset.CSJ_Wave1_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB9630B30) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave2_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave2_PlaceCluster_ArcAction.Default__CSJ_Wave2_PlaceCluster_ArcAction_C` class `CSJ_Wave2_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB96338D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_ClusterAsset.CSJ_Wave2_ClusterAsset' (0x0000029B0DB0E0C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CSJ_Wave2_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_ClusterAsset.CSJ_Wave2_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_ClusterAsset.CSJ_Wave2_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB9633970) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave3_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave3_PlaceCluster_ArcAction.Default__CSJ_Wave3_PlaceCluster_ArcAction_C` class `CSJ_Wave3_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB9632750) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_ClusterAsset.CSJ_Wave3_ClusterAsset' (0x0000029B0DB0C2C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CSJ_Wave3_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_ClusterAsset.CSJ_Wave3_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_ClusterAsset.CSJ_Wave3_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB96327F0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave4_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave4_PlaceCluster_ArcAction.Default__CSJ_Wave4_PlaceCluster_ArcAction_C` class `CSJ_Wave4_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB9630D10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_ClusterAsset.CSJ_Wave4_ClusterAsset' (0x0000029B0DB0FC40) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CSJ_Wave4_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_ClusterAsset.CSJ_Wave4_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_ClusterAsset.CSJ_Wave4_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB9630DB0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave5_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave5_PlaceCluster_ArcAction.Default__CSJ_Wave5_PlaceCluster_ArcAction_C` class `CSJ_Wave5_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB9632390) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_ClusterAsset.CSJ_Wave5_ClusterAsset' (0x0000029B0DB0F380) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CSJ_Wave5_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_ClusterAsset.CSJ_Wave5_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_ClusterAsset.CSJ_Wave5_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB9632430) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Periphery_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Periphery_PlaceCluster_ArcAction.Default__CWF_Periphery_PlaceCluster_ArcAction_C` class `CWF_Periphery_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB96310D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_ClusterAsset.CWF_Periphery_ClusterAsset' (0x0000029B0DB0F880) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CWF_Periphery_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_ClusterAsset.CWF_Periphery_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_ClusterAsset.CWF_Periphery_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB9631170) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `3`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_ClusterAsset`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Periphery_PlaceCluster_ArcAction`
- referencers: `2`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Periphery_PlaceCluster_ArcAction`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave1_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave1_PlaceCluster_ArcAction.Default__CWF_Wave1_PlaceCluster_ArcAction_C` class `CWF_Wave1_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB9630F90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_ClusterAsset.CWF_Wave1_ClusterAsset' (0x0000029B0DB0CCC0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CWF_Wave1_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_ClusterAsset.CWF_Wave1_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_ClusterAsset.CWF_Wave1_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB9631030) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave2_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave2_PlaceCluster_ArcAction.Default__CWF_Wave2_PlaceCluster_ArcAction_C` class `CWF_Wave2_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB9633290) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_ClusterAsset.CWF_Wave2_ClusterAsset' (0x0000029B0DB0E5C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CWF_Wave2_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_ClusterAsset.CWF_Wave2_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_ClusterAsset.CWF_Wave2_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB9633330) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave3_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave3_PlaceCluster_ArcAction.Default__CWF_Wave3_PlaceCluster_ArcAction_C` class `CWF_Wave3_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB93AFC90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_ClusterAsset.CWF_Wave3_ClusterAsset' (0x0000029B0DB0D300) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CWF_Wave3_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_ClusterAsset.CWF_Wave3_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_ClusterAsset.CWF_Wave3_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB93AFD30) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave4_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave4_PlaceCluster_ArcAction.Default__CWF_Wave4_PlaceCluster_ArcAction_C` class `CWF_Wave4_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB93AE4D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_ClusterAsset.CWF_Wave4_ClusterAsset' (0x0000029B0DB0FEC0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CWF_Wave4_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_ClusterAsset.CWF_Wave4_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_ClusterAsset.CWF_Wave4_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB93AE570) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave5_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave5_PlaceCluster_ArcAction.Default__CWF_Wave5_PlaceCluster_ArcAction_C` class `CWF_Wave5_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB93ACBD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_ClusterAsset.CWF_Wave5_ClusterAsset' (0x0000029B0DB0F600) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CWF_Wave5_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_ClusterAsset.CWF_Wave5_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_ClusterAsset.CWF_Wave5_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB93ACC70) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Periphery_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Periphery_PlaceCluster_ArcAction.Default__ConflictZone_Periphery_PlaceCluster_ArcAction_C` class `ConflictZone_Periphery_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB93AF650) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/ConflictCluster_Periphery_ClusterAsset.ConflictCluster_Periphery_ClusterAsset' (0x0000029B0DB0DE40) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'ConflictCluster_Periphery_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Periphery/ConflictCluster_Periphery_ClusterAsset.ConflictCluster_Periphery_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Periphery/ConflictCluster_Periphery_ClusterAsset.ConflictCluster_Periphery_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB93AF6F0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `3`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/ConflictCluster_Periphery_ClusterAsset`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Periphery_PlaceCluster_ArcAction`
- referencers: `2`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Periphery_PlaceCluster_ArcAction`

### `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave1_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave1_PlaceCluster_ArcAction.Default__ConflictZone_Wave1_PlaceCluster_ArcAction_C` class `ConflictZone_Wave1_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB93AFB50) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave1/ConflictCluster_Wave1_ClusterAsset.ConflictCluster_Wave1_ClusterAsset' (0x0000029B0DB0C900) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'ConflictCluster_Wave1_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave1/ConflictCluster_Wave1_ClusterAsset.ConflictCluster_Wave1_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave1/ConflictCluster_Wave1_ClusterAsset.ConflictCluster_Wave1_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB93AFBF0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave1/ConflictCluster_Wave1_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave2_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave2_PlaceCluster_ArcAction.Default__ConflictZone_Wave2_PlaceCluster_ArcAction_C` class `ConflictZone_Wave2_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB93ADE90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave2/ConflictCluster_Wave2_ClusterAsset.ConflictCluster_Wave2_ClusterAsset' (0x0000029B0DB0D080) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'ConflictCluster_Wave2_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave2/ConflictCluster_Wave2_ClusterAsset.ConflictCluster_Wave2_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave2/ConflictCluster_Wave2_ClusterAsset.ConflictCluster_Wave2_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB93ADF30) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave2/ConflictCluster_Wave2_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave3_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave3_PlaceCluster_ArcAction.Default__ConflictZone_Wave3_PlaceCluster_ArcAction_C` class `ConflictZone_Wave3_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB915E610) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave3/ConflictCluster_Wave3_ClusterAsset.ConflictCluster_Wave3_ClusterAsset' (0x0000029B0DB0C180) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'ConflictCluster_Wave3_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave3/ConflictCluster_Wave3_ClusterAsset.ConflictCluster_Wave3_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave3/ConflictCluster_Wave3_ClusterAsset.ConflictCluster_Wave3_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB915E6B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave3/ConflictCluster_Wave3_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave4_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave4_PlaceCluster_ArcAction.Default__ConflictZone_Wave4_PlaceCluster_ArcAction_C` class `ConflictZone_Wave4_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB915C310) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave4/ConflictCluster_Wave4_ClusterAsset.ConflictCluster_Wave4_ClusterAsset' (0x0000029B0DB0FB00) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'ConflictCluster_Wave4_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave4/ConflictCluster_Wave4_ClusterAsset.ConflictCluster_Wave4_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave4/ConflictCluster_Wave4_ClusterAsset.ConflictCluster_Wave4_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB915C3B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave4/ConflictCluster_Wave4_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave5_PlaceCluster_ArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave5_PlaceCluster_ArcAction.Default__ConflictZone_Wave5_PlaceCluster_ArcAction_C` class `ConflictZone_Wave5_PlaceCluster_ArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029BB915DC10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'ClusterDataAsset': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave5/ConflictCluster_Wave5_ClusterAsset.ConflictCluster_Wave5_ClusterAsset' (0x0000029B0DB0DA80) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'ConflictCluster_Wave5_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave5/ConflictCluster_Wave5_ClusterAsset.ConflictCluster_Wave5_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave5/ConflictCluster_Wave5_ClusterAsset.ConflictCluster_Wave5_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'ClusterDataAssetId': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000029BB915DCB0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}}`
- dependencies: `2`
  - `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
  - `/Game/DLC7/CampaignData/Clusters/Wave5/ConflictCluster_Wave5_ClusterAsset`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/RemoveClusterToiArcAction`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/RemoveClusterToiArcAction.Default__RemoveClusterToiArcAction_C` class `RemoveClusterToiArcAction_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029C195B1B90) {id: 0}>", 'python_type': 'CampaignArcActionId'}}`
- dependencies: `9`
  - `/Engine/EditorBlueprintResources/StandardMacros`
  - `/Game/Campaign/TOIs/CLusterToi`
  - `/Game/Campaign/TOIs/ClusterToiLogic`
  - `/Game/Campaign/TOIs/DefaultMissionToiLogic`
  - `/Game/Campaign/TOIs/GeneratedMissionToiLogic`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusterToiArcAction`
  - `/Game/DLC7/PlaceClusterActions/ReplacementClusterDataTable`
  - `/Game/DLC7/PlaceClusterActions/ReplacementClusterStruct`
  - `/Script/MechWarrior`
- referencers: `8`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusterToiArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByEndOfInvasion`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByPeripheryWave`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave1`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave2`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave3`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave4`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemoveWave1`
- class: `ObjectRedirector`
- dependencies: `1`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave1`
- referencers: `0`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemoveWave2`
- class: `ObjectRedirector`
- dependencies: `1`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave2`
- referencers: `0`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemoveWave3`
- class: `ObjectRedirector`
- dependencies: `1`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave3`
- referencers: `0`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemoveWave4`
- class: `ObjectRedirector`
- dependencies: `1`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave4`
- referencers: `0`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemoveWave5`
- class: `ObjectRedirector`
- dependencies: `1`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5`
- referencers: `0`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByEndOfInvasion`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByEndOfInvasion.Default__RemovedByEndOfInvasion_C` class `RemovedByEndOfInvasion_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029C195B13B0) {id: 0}>", 'python_type': 'CampaignArcActionId'}}`
- dependencies: `2`
  - `/Game/DLC7/CampaignData/Clusters/Wave4/ConflictCluster_Wave4_ClusterAsset`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusterToiArcAction`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByPeripheryWave`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByPeripheryWave.Default__RemovedByPeripheryWave_C` class `RemovedByPeripheryWave_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029C195B12D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}}`
- dependencies: `3`
  - `/Game/Campaign/Clusters/PiratesLair/PiratesLair_ClusterAsset`
  - `/Game/DLC1/CareerMode/Clusters/S_6_7/S_6_7_ClusterAsset`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusterToiArcAction`
- referencers: `1`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave1`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave1.Default__RemovedByWave1_C` class `RemovedByWave1_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029C195B1AB0) {id: 0}>", 'python_type': 'CampaignArcActionId'}}`
- dependencies: `12`
  - `/Game/Campaign/Clusters/DroughtWorlds/DroughtWorlds_ClusterAsset`
  - `/Game/Campaign/Clusters/IndustrialHub_29/IndustrialHub_29_ClusterAsset`
  - `/Game/Campaign/Clusters/Rasalhague/Rasalhague_ClusterAsset`
  - `/Game/Campaign/Clusters/TheGraveyard/TheGraveyard_ClusterAsset`
  - `/Game/DLC1/CareerMode/Clusters/K_1_2/K_1_2_ClusterAsset`
  - `/Game/DLC1/CareerMode/Clusters/Rasalhague_1_3/Rasalhague_1_3_ClusterAsset`
  - `/Game/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset`
  - `/Game/DLC1/CareerMode/Clusters/SafeZone_16/SafeZone_16_ClusterAsset`
  - `/Game/DLC1/CareerMode/Clusters/SafeZone_31/SafeZone_31_ClusterAsset`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/ConflictCluster_Periphery_ClusterAsset`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusterToiArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave1`
- referencers: `3`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemoveWave1`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave1`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave2`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave2.Default__RemovedByWave2_C` class `RemovedByWave2_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029C195B1960) {id: 0}>", 'python_type': 'CampaignArcActionId'}}`
- dependencies: `8`
  - `/Game/Campaign/Clusters/SC07/SC07_ClusterAsset`
  - `/Game/DLC1/CareerMode/Clusters/K_4_5/K_4_5_ClusterAsset`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_ClusterAsset`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_ClusterAsset`
  - `/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_ClusterAsset`
  - `/Game/DLC7/CampaignData/Clusters/Wave1/ConflictCluster_Wave1_ClusterAsset`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusterToiArcAction`
- referencers: `2`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemoveWave2`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave3`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave3.Default__RemovedByWave3_C` class `RemovedByWave3_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029C195B1880) {id: 0}>", 'python_type': 'CampaignArcActionId'}}`
- dependencies: `8`
  - `/Game/DLC1/CareerMode/Clusters/K_2_3/K_2_3_ClusterAsset`
  - `/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_CampaignCluster1`
  - `/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_ClusterAsset`
  - `/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_ClusterAsset`
  - `/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_ClusterAsset`
  - `/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_ClusterAsset`
  - `/Game/DLC7/CampaignData/Clusters/Wave2/ConflictCluster_Wave2_ClusterAsset`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusterToiArcAction`
- referencers: `2`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemoveWave3`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave4`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave4.Default__RemovedByWave4_C` class `RemovedByWave4_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029C195B1650) {id: 0}>", 'python_type': 'CampaignArcActionId'}}`
- dependencies: `11`
  - `/Game/Campaign/Clusters/SC05/SC05_ClusterAsset`
  - `/Game/Campaign/Clusters/SC06/SC06_ClusterAsset`
  - `/Game/DLC1/CareerMode/Clusters/K_3_4/K_3_4_ClusterAsset`
  - `/Game/DLC1/CareerMode/Clusters/K_3_5_1/K_3_5_1_ClusterAsset`
  - `/Game/DLC4/CampaignData/Clusters/RadstadtZone/RadstadtZone_ClusterAsset`
  - `/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_ClusterAsset`
  - `/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_ClusterAsset`
  - `/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_ClusterAsset`
  - `/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_ClusterAsset`
  - `/Game/DLC7/CampaignData/Clusters/Wave3/ConflictCluster_Wave3_ClusterAsset`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusterToiArcAction`
- referencers: `2`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemoveWave4`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5`
- class: `Blueprint`
- cdo: `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5.Default__RemovedByWave5_C` class `RemovedByWave5_C`
- cdo properties: `{'campaign_arc_action_id': {'repr': "<Struct 'CampaignArcActionId' (0x0000029C195B1A40) {id: 0}>", 'python_type': 'CampaignArcActionId'}}`
- dependencies: `15`
  - `/Game/Campaign/Clusters/DraconisBadlands/DraconisBadlands_ClusterAsset`
  - `/Game/Campaign/Clusters/IndustrialHub_17/IndustrialHub_17_ClusterAsset`
  - `/Game/Campaign/Clusters/IndustrialHub_22/IndustrialHub_22_ClusterAsset`
  - `/Game/Campaign/Clusters/Lower-ClassKuritanWorlds/Lower-ClassKuritanWorlds_ClusterAsset`
  - `/Game/Campaign/Clusters/Steiner-KuritaBorder/Steiner-KuritaBorder_ClusterAsset`
  - `/Game/DLC1/CareerMode/Clusters/K_5_6/K_5_6_ClusterAsset`
  - `/Game/DLC1/CareerMode/Clusters/K_7_9/K_7_9_ClusterAsset`
  - `/Game/DLC1/CareerMode/Clusters/S_6_9/S_6_9_ClusterAsset`
  - `/Game/DLC1/CareerMode/Clusters/SafeZone_14/SafeZone_14_ClusterAsset`
  - `/Game/DLC1/CareerMode/Clusters/SafeZone_30/SafeZone_30_ClusterAsset`
  - `/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_ClusterAsset`
  - `/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_ClusterAsset`
  - `/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_ClusterAsset`
  - `/Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_ClusterAsset`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusterToiArcAction`
- referencers: `2`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemoveWave5`

### `/Game/DLC7/PlaceClusterActions/ReplacementClusterDataTable`
- class: `DataTable`
- dependencies: `1`
  - `/Game/DLC7/PlaceClusterActions/ReplacementClusterStruct`
- referencers: `1`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusterToiArcAction`

### `/Game/DLC7/PlaceClusterActions/ReplacementClusterStruct`
- class: `UserDefinedStruct`
- dependencies: `1`
  - `/Script/MechWarrior`
- referencers: `2`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusterToiArcAction`
  - `/Game/DLC7/PlaceClusterActions/ReplacementClusterDataTable`
