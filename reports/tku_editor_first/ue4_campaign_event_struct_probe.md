# UE4 Campaign Event Struct Probe

- Generated: `2026-05-25T09:25:37.978868+00:00`
- Target mod: `TKUCompatEditorPatch`
- Safety: read-only commandlet; no assets saved.

## Findings

- /ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/CareerModeCoreCampaign events=None event_field=None.
- /ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters events=None event_field=None.
- /ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones events=None event_field=None.
- /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors events=9 event_field=campaign_events.
- Event PlacePeriphery has date field date=<Struct 'CampaignTrigger_Date' (0x0000023F10562510) {check: True, value: {}, condition: GreaterThanEquals}> actions=6.
- Event PlaceWave1 has date field date=<Struct 'CampaignTrigger_Date' (0x0000023F10562290) {check: True, value: {}, condition: GreaterThanEquals}> actions=6.
- Event PlaceWave2 has date field date=<Struct 'CampaignTrigger_Date' (0x0000023F10562010) {check: True, value: {}, condition: GreaterThanEquals}> actions=6.
- Event PlaceWave3 has date field date=<Struct 'CampaignTrigger_Date' (0x0000023F10561D90) {check: True, value: {}, condition: GreaterThanEquals}> actions=6.
- Event PlaceWave4 has date field date=<Struct 'CampaignTrigger_Date' (0x0000023F10561B10) {check: True, value: {}, condition: GreaterThanEquals}> actions=6.
- Event PlaceWave5 has date field date=<Struct 'CampaignTrigger_Date' (0x0000023F10561890) {check: True, value: {}, condition: GreaterThanEquals}> actions=5.
- Event PlaceCampaignCluster1 has date field date=<Struct 'CampaignTrigger_Date' (0x0000023F10561610) {check: False, value: {}, condition: GreaterThanEquals}> actions=1.
- Event ReCheckRemovePeriphery has date field date=<Struct 'CampaignTrigger_Date' (0x0000023F10561390) {check: True, value: {}, condition: GreaterThanEquals}> actions=1.
- /Game/DLC7/CampaignData/DLC7_ShowUnchartedSystems events=1 event_field=campaign_events.
- Event ShowUnchartedSystems has date field date=<Struct 'CampaignTrigger_Date' (0x0000023F100AD390) {check: False, value: {}, condition: GreaterThanEquals}> actions=2.

## Campaign Arcs

### `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/CareerModeCoreCampaign`
- Exists: `False`
- Class: `None`
- Event count: `None`
- Event array field: `None`

### `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- Exists: `False`
- Class: `None`
- Event count: `None`
- Event array field: `None`

### `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- Exists: `False`
- Class: `None`
- Event count: `None`
- Event array field: `None`

### `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- Exists: `True`
- Class: `MWCampaignArcAsset`
- Event count: `9`
- Event array field: `campaign_events`
- Event `PlacePeriphery` actions `6` paths `['/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Periphery_PlaceCluster_ArcAction.CGB_Periphery_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Periphery_PlaceCluster_ArcAction.CJF_Periphery_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Periphery_PlaceCluster_ArcAction.CSJ_Periphery_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Periphery_PlaceCluster_ArcAction.CWF_Periphery_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Periphery_PlaceCluster_ArcAction.ConflictZone_Periphery_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByPeripheryWave.RemovedByPeripheryWave_C']`
  - Date field `date` `<Struct 'CampaignTrigger_Date' (0x0000023F10562510) {check: True, value: {}, condition: GreaterThanEquals}>`
- Event `PlaceWave1` actions `6` paths `['/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave1.RemovedByWave1_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave1_PlaceCluster_ArcAction.CGB_Wave1_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave1_PlaceCluster_ArcAction.CJF_Wave1_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave1_PlaceCluster_ArcAction.CSJ_Wave1_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave1_PlaceCluster_ArcAction.CWF_Wave1_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave1_PlaceCluster_ArcAction.ConflictZone_Wave1_PlaceCluster_ArcAction_C']`
  - Date field `date` `<Struct 'CampaignTrigger_Date' (0x0000023F10562290) {check: True, value: {}, condition: GreaterThanEquals}>`
- Event `PlaceWave2` actions `6` paths `['/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave2.RemovedByWave2_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave2_PlaceCluster_ArcAction.CGB_Wave2_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave2_PlaceCluster_ArcAction.CJF_Wave2_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave2_PlaceCluster_ArcAction.CSJ_Wave2_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave2_PlaceCluster_ArcAction.CWF_Wave2_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave2_PlaceCluster_ArcAction.ConflictZone_Wave2_PlaceCluster_ArcAction_C']`
  - Date field `date` `<Struct 'CampaignTrigger_Date' (0x0000023F10562010) {check: True, value: {}, condition: GreaterThanEquals}>`
- Event `PlaceWave3` actions `6` paths `['/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave3.RemovedByWave3_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave3_PlaceCluster_ArcAction.CGB_Wave3_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave3_PlaceCluster_ArcAction.CJF_Wave3_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave3_PlaceCluster_ArcAction.CSJ_Wave3_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave3_PlaceCluster_ArcAction.CWF_Wave3_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave3_PlaceCluster_ArcAction.ConflictZone_Wave3_PlaceCluster_ArcAction_C']`
  - Date field `date` `<Struct 'CampaignTrigger_Date' (0x0000023F10561D90) {check: True, value: {}, condition: GreaterThanEquals}>`
- Event `PlaceWave4` actions `6` paths `['/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave4.RemovedByWave4_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave4_PlaceCluster_ArcAction.CGB_Wave4_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave4_PlaceCluster_ArcAction.CJF_Wave4_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave4_PlaceCluster_ArcAction.CSJ_Wave4_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave4_PlaceCluster_ArcAction.CWF_Wave4_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave4_PlaceCluster_ArcAction.ConflictZone_Wave4_PlaceCluster_ArcAction_C']`
  - Date field `date` `<Struct 'CampaignTrigger_Date' (0x0000023F10561B10) {check: True, value: {}, condition: GreaterThanEquals}>`
- Event `PlaceWave5` actions `5` paths `['/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5.RemovedByWave5_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave5_PlaceCluster_ArcAction.CGB_Wave5_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave5_PlaceCluster_ArcAction.CJF_Wave5_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave5_PlaceCluster_ArcAction.CSJ_Wave5_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave5_PlaceCluster_ArcAction.CWF_Wave5_PlaceCluster_ArcAction_C']`
  - Date field `date` `<Struct 'CampaignTrigger_Date' (0x0000023F10561890) {check: True, value: {}, condition: GreaterThanEquals}>`
- Event `PlaceCampaignCluster1` actions `1` paths `['/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceRasalhagueCluster.DLC7_PlaceRasalhagueCluster_C']`
  - Date field `date` `<Struct 'CampaignTrigger_Date' (0x0000023F10561610) {check: False, value: {}, condition: GreaterThanEquals}>`
- Event `ReCheckRemovePeriphery` actions `1` paths `['/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByPeripheryWave.RemovedByPeripheryWave_C']`
  - Date field `date` `<Struct 'CampaignTrigger_Date' (0x0000023F10561390) {check: True, value: {}, condition: GreaterThanEquals}>`
- Event `PlaceFinalClansConflictZone` actions `2` paths `['/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave5_PlaceCluster_ArcAction.ConflictZone_Wave5_PlaceCluster_ArcAction_C', '/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByEndOfInvasion.RemovedByEndOfInvasion_C']`
  - Date field `date` `<Struct 'CampaignTrigger_Date' (0x0000023F10561110) {check: True, value: {}, condition: GreaterThanEquals}>`

### `/Game/DLC7/CampaignData/DLC7_ShowUnchartedSystems`
- Exists: `True`
- Class: `MWCampaignArcAsset`
- Event count: `1`
- Event array field: `campaign_events`
- Event `ShowUnchartedSystems` actions `2` paths `['/Game/DLC7/CampaignData/CampaignArcActions/Unhide_BaseCampaignStars.Unhide_BaseCampaignStars_C', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceHiddenSystemsCluster.DLC7_PlaceHiddenSystemsCluster_C']`
  - Date field `date` `<Struct 'CampaignTrigger_Date' (0x0000023F100AD390) {check: False, value: {}, condition: GreaterThanEquals}>`

## Blueprints

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceHiddenSystemsCluster`
- Exists: `True`
- CDO class: `DLC7_PlaceHiddenSystemsCluster_C`
- ClusterDataAsset: `{'ok': True, 'name': 'ClusterDataAsset', 'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster.DLC7_HiddenSystems_CampaignCluster' (0x0000023EB31F2C00) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'DLC7_HiddenSystems_CampaignCluster', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster.DLC7_HiddenSystems_CampaignCluster', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster.DLC7_HiddenSystems_CampaignCluster', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster.DLC7_HiddenSystems_CampaignCluster', 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster.DLC7_HiddenSystems_CampaignCluster' (0x0000023EB31F2C00) Class 'MWClusterDataAsset'>"}`
- ClusterDataAssetId: `{'ok': True, 'name': 'ClusterDataAssetId', 'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000023EB94C1A30) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'repr': '<Struct \'ClusterDataAssetId\' (0x0000023EB94C1A30) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}`
- campaign_arc_action_id: `{'ok': True, 'name': 'campaign_arc_action_id', 'value': {'repr': "<Struct 'CampaignArcActionId' (0x0000023EB94C1990) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'repr': "<Struct 'CampaignArcActionId' (0x0000023EB94C1990) {id: 0}>"}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Periphery_PlaceCluster_ArcAction`
- Exists: `True`
- CDO class: `CGB_Periphery_PlaceCluster_ArcAction_C`
- ClusterDataAsset: `{'ok': True, 'name': 'ClusterDataAsset', 'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset.CGB_Periphery_ClusterAsset' (0x0000023EB31F2D40) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CGB_Periphery_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset.CGB_Periphery_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset.CGB_Periphery_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset.CGB_Periphery_ClusterAsset', 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset.CGB_Periphery_ClusterAsset' (0x0000023EB31F2D40) Class 'MWClusterDataAsset'>"}`
- ClusterDataAssetId: `{'ok': True, 'name': 'ClusterDataAssetId', 'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x0000023EB97EDF30) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'repr': '<Struct \'ClusterDataAssetId\' (0x0000023EB97EDF30) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}`
- campaign_arc_action_id: `{'ok': True, 'name': 'campaign_arc_action_id', 'value': {'repr': "<Struct 'CampaignArcActionId' (0x0000023EB97EDE90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'repr': "<Struct 'CampaignArcActionId' (0x0000023EB97EDE90) {id: 0}>"}`
