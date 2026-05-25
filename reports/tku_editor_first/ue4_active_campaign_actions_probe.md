# UE4 Active Campaign Actions Probe

- Generated: `2026-05-25T07:02:00.142598+00:00`
- Target mod: `TKUCompatEditorPatch`
- Safety: read-only commandlet; no assets saved.

## Findings

- Active graph assets inspected: 800 class counts {'Blueprint': 337, 'MWCampaignArcAsset': 192, 'MWClusterDataAsset': 179, 'MWMetagameObjectiveAsset': 34, 'MWFactionAsset': 19, 'MWScenarioSpecificationAsset': 15, 'ObjectRedirector': 6, 'MWBriefingAsset': 6, 'Texture2D': 6, 'UserDefinedStruct': 2, 'DataTable': 1, 'StringTable': 1, 'EditorUtilityBlueprint': 1, 'EditorUtilityWidgetBlueprint': 1}.
- Active ArcAction blueprints discovered from campaign-event lists/references: 252.
- PlaceCluster-like actions in walked graph: 47.
- PlaceSafeZone actions in walked graph: 35.
- Cluster references in walked graph: 212; mod-owned cluster references: 1.
- /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters subcampaigns=60 event_actions=0.
- /ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters subcampaigns=60 event_actions=0.
- /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones subcampaigns=0 event_actions=35.
- /ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones subcampaigns=0 event_actions=35.

## Graph Summary

- asset_count: `800`
- class_counts: `{'Blueprint': 337, 'MWCampaignArcAsset': 192, 'MWClusterDataAsset': 179, 'MWMetagameObjectiveAsset': 34, 'MWFactionAsset': 19, 'MWScenarioSpecificationAsset': 15, 'ObjectRedirector': 6, 'MWBriefingAsset': 6, 'Texture2D': 6, 'UserDefinedStruct': 2, 'DataTable': 1, 'StringTable': 1, 'EditorUtilityBlueprint': 1, 'EditorUtilityWidgetBlueprint': 1}`
- action_count: `252`
- place_cluster_action_count: `47`
- place_safezone_action_count: `35`
- cluster_reference_count: `212`
- mod_cluster_reference_count: `1`

## Action Cluster Bindings

- `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceHiddenSystemsCluster` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster`
- `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceHiddenSystemsCluster` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB96E3E70) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceRasalhagueCluster` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_CampaignCluster1`
- `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceRasalhagueCluster` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB96E0C70) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC1/CareerMode/Warzones/Rasalhauge_Clusters/PlaceRasalhague_ArcAction_7_10` `ClusterDataAsset` -> `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset`
- `/Game/DLC1/CareerMode/Warzones/Rasalhauge_Clusters/PlaceRasalhague_ArcAction_7_10` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB91A1F30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Rasalhague_7_10_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/Warzones/Rasalhauge_Clusters/PlaceRasalhague_ArcAction_1_3` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/Rasalhague_1_3/Rasalhague_1_3_ClusterAsset`
- `/Game/DLC1/CareerMode/Warzones/Rasalhauge_Clusters/PlaceRasalhague_ArcAction_1_3` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB919A6B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Rasalhague_1_3_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_10_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_10/SafeZone_10_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_10_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB90997B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_10_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_11_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_11/SafeZone_11_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_11_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB9099CB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_11_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_12_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_12/SafeZone_12_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_12_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB90992B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_12_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_13_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_13/SafeZone_13_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_13_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB909ABB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_13_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_14_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_14/SafeZone_14_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_14_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB909BBF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_14_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_15_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_15/SafeZone_15_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_15_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB909A7F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_15_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_16_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_16/SafeZone_16_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_16_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB9099530) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_16_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_17_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_17/SafeZone_17_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_17_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8FF67F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_17_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_18_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_18/SafeZone_18_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_18_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8FF70B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_18_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_19_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_19/SafeZone_19_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_19_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8FF6570) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_19_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_1_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_1/SafeZone_1_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_1_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB94CB970) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_1_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_20_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_20/SafeZone_20_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_20_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8FF5CB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_20_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_21_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_21/SafeZone_21_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_21_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8FF5530) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_21_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_22_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_22/SafeZone_22_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_22_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8FF4C70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_22_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_23_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_23/SafeZone_23_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_23_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8FF6930) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_23_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_24_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_24/SafeZone_24_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_24_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8FF7970) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_24_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_25_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_25/SafeZone_25_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_25_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8FF62F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_25_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_26_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_26/SafeZone_26_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_26_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8FF6CF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_26_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_27_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_27/SafeZone_27_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_27_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8FF53F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_27_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_28_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_28/SafeZone_28_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_28_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB904ECF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_28_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_29_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_29/SafeZone_29_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_29_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB904E930) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_29_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_2_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_2/SafeZone_2_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_2_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB94CBE70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_2_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_30_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_30/SafeZone_30_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_30_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB904F970) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_30_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_31_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_31/SafeZone_31_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_31_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB9177830) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_31_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_32_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_32/SafeZone_32_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_32_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB9174DB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_32_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_33_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_33/SafeZone_33_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_33_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB9176E30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_33_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_34_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_34/SafeZone_34_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_34_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB9175DF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_34_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_35_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_35/SafeZone_35_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_35_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB9176570) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_35_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_3_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_3/SafeZone_3_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_3_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB94C8630) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_3_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_4_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_4/SafeZone_4_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_4_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB94C8B30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_4_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_5_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_5/SafeZone_5_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_5_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB94C9030) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_5_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_6_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_6/SafeZone_6_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_6_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB94C93F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_6_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_7_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_7/SafeZone_7_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_7_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB94C9B70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_7_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_8_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_8/SafeZone_8_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_8_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB9098270) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_8_ClusterAsset"}}>`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_9_ArcAction` `ClusterDataAsset` -> `/Game/DLC1/CareerMode/Clusters/SafeZone_9/SafeZone_9_ClusterAsset`
- `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_9_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB909AA70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_9_ClusterAsset"}}>`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Periphery_PlaceCluster_ArcAction` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Periphery_PlaceCluster_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8B9F330) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave1_PlaceCluster_ArcAction` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_ClusterAsset`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave1_PlaceCluster_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB7C69170) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave2_PlaceCluster_ArcAction` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_ClusterAsset`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave2_PlaceCluster_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8BFF0B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave3_PlaceCluster_ArcAction` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_ClusterAsset`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave3_PlaceCluster_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB930DB70) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave4_PlaceCluster_ArcAction` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_ClusterAsset`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave4_PlaceCluster_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB930FBF0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave5_PlaceCluster_ArcAction` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_ClusterAsset`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave5_PlaceCluster_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB96E2430) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Periphery_PlaceCluster_ArcAction` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_ClusterAsset`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Periphery_PlaceCluster_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8B9E1B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave1_PlaceCluster_ArcAction` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_ClusterAsset`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave1_PlaceCluster_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8BFF330) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave2_PlaceCluster_ArcAction` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_ClusterAsset`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave2_PlaceCluster_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8BFF970) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave3_PlaceCluster_ArcAction` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_ClusterAsset`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave3_PlaceCluster_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB930D7B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave4_PlaceCluster_ArcAction` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_ClusterAsset`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave4_PlaceCluster_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB930EE30) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave5_PlaceCluster_ArcAction` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_ClusterAsset`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave5_PlaceCluster_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB96E17B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Periphery_PlaceCluster_ArcAction` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_ClusterAsset`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Periphery_PlaceCluster_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8B9DA30) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave1_PlaceCluster_ArcAction` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_ClusterAsset`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave1_PlaceCluster_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8BFD7B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave2_PlaceCluster_ArcAction` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_ClusterAsset`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave2_PlaceCluster_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8BFD170) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave3_PlaceCluster_ArcAction` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_ClusterAsset`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave3_PlaceCluster_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB930D8F0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave4_PlaceCluster_ArcAction` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_ClusterAsset`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave4_PlaceCluster_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB930C270) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave5_PlaceCluster_ArcAction` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_ClusterAsset`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave5_PlaceCluster_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB96E1CB0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Periphery_PlaceCluster_ArcAction` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_ClusterAsset`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Periphery_PlaceCluster_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8CB9A30) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave1_PlaceCluster_ArcAction` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_ClusterAsset`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave1_PlaceCluster_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8BFE570) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave2_PlaceCluster_ArcAction` `ClusterDataAsset` -> `/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_ClusterAsset`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave2_PlaceCluster_ArcAction` `ClusterDataAssetId` -> `<Struct 'ClusterDataAssetId' (0x000001BAB8BFE1B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>`

## Place Cluster Actions

- `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/PlaceCluster_SC01`
- `/Game/Campaign/CampaignArcs/Regions/StoryCluster_02/PlaceCluster_SC02`
- `/Game/Campaign/CampaignArcs/Regions/StoryCluster_03/PlaceCluster_SC03`
- `/Game/Campaign/CampaignArcs/Regions/StoryCluster_04/PlaceCluster_SC04`
- `/Game/Campaign/CampaignArcs/Regions/StoryCluster_05/PlaceCluster_SC05`
- `/Game/Campaign/CampaignArcs/Regions/StoryCluster_06/PlaceCluster_SC06`
- `/Game/Campaign/CampaignArcs/Regions/StoryCluster_07/PlaceCluster_SC07`
- `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceHiddenSystemsCluster`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Periphery_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave1_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave2_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave3_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave4_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave5_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Periphery_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave1_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave2_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave3_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave4_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave5_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Periphery_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave1_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave2_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave3_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave4_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave5_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Periphery_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave1_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave2_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave3_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave4_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave5_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Periphery_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave1_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave2_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave3_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave4_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave5_PlaceCluster_ArcAction`
- `/Game/DLC7/PlaceClusterActions/RemoveClusterToiArcAction`
- `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByEndOfInvasion`
- `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByPeripheryWave`
- `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave1`
- `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave2`
- `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave3`
- `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave4`
- `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5`

## Mod Cluster References

- `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset`

## Discovery Inventory

- `/Game/DLC7/CampaignData`: `{'exists': True, 'asset_count': 364, 'focused_count': 364, 'focused_sample': ['/Game/DLC7/CampaignData/AtlasII_MarketArc', '/Game/DLC7/CampaignData/AtlasII_PlaceToi_ArcAction', '/Game/DLC7/CampaignData/AtlasII_Purchased', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_CustomMarket1_Alleghe_ArcAction', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_CustomMarket2_Rodrigo_ArcAction', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_CustomMarket3_LastFrontier_ArcAction', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_CustomMarket4_Rasalhague_ArcAction', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_CustomMarket4_UnchartedSystems_ArcAction', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_CustomMarket5_UnchartedSystems_ArcAction', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_D7M10_TravelBriefing', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_D7M1_TravelBriefing', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_D7M2_TravelBriefing', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_D7M4_TravelBriefing', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_D7M7_TravelBriefing', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_DeclinedContract', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_FailedContract_Complete', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Holo1_Objective', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Holo1_SpeakToRyana', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Holo2_Objective', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Holo2_SpeakToRyana', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Holo3_Objective', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Holo3_SpeakToRyana', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PastStarDate_ArcAction', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceHiddenSystemsCluster', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceRasalhagueCluster', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Pt0_CompleteKickoff', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Pt0_KickoffBriefing', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Pt0_Offer_1MonthWarning_ArcAction', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Pt0_Offer_3MonthWarning_ArcAction', '/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Pt0_PriorityTransmission', '/Game/DLC7/CampaignData/CampaignArcActions/ShowSpears_ArcAction', '/Game/DLC7/CampaignData/CampaignArcActions/TravelTo_D7M1', '/Game/DLC7/CampaignData/CampaignArcActions/TravelTo_D7M10', '/Game/DLC7/CampaignData/CampaignArcActions/TravelTo_D7M2', '/Game/DLC7/CampaignData/CampaignArcActions/TravelTo_D7M4', '/Game/DLC7/CampaignData/CampaignArcActions/TravelTo_D7M7', '/Game/DLC7/CampaignData/CampaignArcActions/Unhide_BaseCampaignStars', '/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_CampaignCluster1', '/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster', '/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_Faction', '/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_Faction', '/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_Faction', '/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_Faction', '/Game/DLC7/CampaignData/Clusters/Periphery/Cluster_Perifery_STM', '/Game/DLC7/CampaignData/Clusters/Periphery/ConflictCluster_Periphery_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_Faction', '/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_Faction', '/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_Faction', '/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_Faction', '/Game/DLC7/CampaignData/Clusters/Wave1/Cluster_3050_w1_STM', '/Game/DLC7/CampaignData/Clusters/Wave1/ConflictCluster_Wave1_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_Faction', '/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_Faction', '/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_Faction', '/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_Faction', '/Game/DLC7/CampaignData/Clusters/Wave2/Cluster_3050_w2_STM', '/Game/DLC7/CampaignData/Clusters/Wave2/ConflictCluster_Wave2_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_Faction', '/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_Faction', '/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_Faction', '/Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_Faction', '/Game/DLC7/CampaignData/Clusters/Wave3/Cluster_3050_w3_STM', '/Game/DLC7/CampaignData/Clusters/Wave3/ConflictCluster_Wave3_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_Faction', '/Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_Faction', '/Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_Faction', '/Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_Faction', '/Game/DLC7/CampaignData/Clusters/Wave4/Cluster_3050_w4_STM', '/Game/DLC7/CampaignData/Clusters/Wave4/ConflictCluster_Wave4_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_Faction', '/Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_Faction', '/Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_Faction', '/Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_Faction', '/Game/DLC7/CampaignData/Clusters/Wave5/Cluster_3051_w5_STM', '/Game/DLC7/CampaignData/Clusters/Wave5/ConflictCluster_Wave5_ClusterAsset', '/Game/DLC7/CampaignData/DEBUG_DLC7_Act2_CampaignArc', '/Game/DLC7/CampaignData/DEBUG_DLC7_Act3_CampaignArc', '/Game/DLC7/CampaignData/DLC7_CampaignMissionText', '/Game/DLC7/CampaignData/DLC7_CoreCampaign', '/Game/DLC7/CampaignData/DLC7_DeclineContract_Prompt', '/Game/DLC7/CampaignData/DLC7_FailedContract_Prompt', '/Game/DLC7/CampaignData/DLC7_Holo2_CampaignArc', '/Game/DLC7/CampaignData/DLC7_Holo3_CampaignArc', '/Game/DLC7/CampaignData/DLC7_NewReelArc', '/Game/DLC7/CampaignData/DLC7_NewsFeed_ArcAction', '/Game/DLC7/CampaignData/DLC7_PastStartDate_Transmission', '/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors', '/Game/DLC7/CampaignData/DLC7_Pt0_KickoffPrompt', '/Game/DLC7/CampaignData/DLC7_Pt0_Offer_1MonthWarning', '/Game/DLC7/CampaignData/DLC7_Pt0_Offer_3MonthWarning', '/Game/DLC7/CampaignData/DLC7_Pt0_Warnings', '/Game/DLC7/CampaignData/DLC7_Pt1-2_LastFrontier', '/Game/DLC7/CampaignData/DLC7_Pt1_Rodigo', '/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague', '/Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions', '/Game/DLC7/CampaignData/DLC7_Pt4_ReturnToUnchartedSystems', '/Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape', '/Game/DLC7/CampaignData/DLC7_ShowUnchartedSystems', '/Game/DLC7/CampaignData/IsInLastFrontier', '/Game/DLC7/CampaignData/Missions/D7_Battle_A/ArcActions/D7M2_AutoAcceptMission', '/Game/DLC7/CampaignData/Missions/D7_Battle_A/ArcActions/D7M2_AutoAcceptObjective', '/Game/DLC7/CampaignData/Missions/D7_Battle_A/ArcActions/D7M2_Completed', '/Game/DLC7/CampaignData/Missions/D7_Battle_A/ArcActions/D7M2_Offer', '/Game/DLC7/CampaignData/Missions/D7_Battle_A/ArcActions/D7M2_Place_Mission', '/Game/DLC7/CampaignData/Missions/D7_Battle_A/ArcActions/D7M2_Reset_Scenario', '/Game/DLC7/CampaignData/Missions/D7_Battle_A/ArcActions/Show_D7M2', '/Game/DLC7/CampaignData/Missions/D7_Battle_A/ArcActions/Unlock_D7M2_InstantAction', '/Game/DLC7/CampaignData/Missions/D7_Battle_A/D7M2_Briefing', '/Game/DLC7/CampaignData/Missions/D7_Battle_A/D7M2_Prompt', '/Game/DLC7/CampaignData/Missions/D7_Battle_A/D7_Battle_A_BattleGrid', '/Game/DLC7/CampaignData/Missions/D7_Battle_A/D7_Battle_A_Biome', '/Game/DLC7/CampaignData/Missions/D7_Battle_A/D7_Battle_A_Mission_AreaSpec', '/Game/DLC7/CampaignData/Missions/D7_Battle_A/D7_Battle_A_Mission_Scenario', '/Game/DLC7/CampaignData/Missions/D7_Battle_A/Level/D7_Battle_A_Mission_Enemies_AreaTile', '/Game/DLC7/CampaignData/Missions/D7_Battle_A/Level/D7_Battle_A_Mission_Friendlies_AreaTile', '/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/D7M3_AutoAcceptMission', '/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/D7M3_AutoAcceptObjective', '/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/D7M3_Completed', '/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/D7M3_Offer', '/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/D7M3_Place_Mission', '/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/D7M3_Reset_Scenario', '/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/Show_D7M3', '/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/Unlock_D7M3_InstantAction', '/Game/DLC7/CampaignData/Missions/D7_Counterattack/D7M3_Briefing', '/Game/DLC7/CampaignData/Missions/D7_Counterattack/D7M3_HBR-A_Reward_Loadout', '/Game/DLC7/CampaignData/Missions/D7_Counterattack/D7M3_Prompt', '/Game/DLC7/CampaignData/Missions/D7_Counterattack/D7_Counterattack_BattleGrid', '/Game/DLC7/CampaignData/Missions/D7_Counterattack/D7_Counterattack_Biome', '/Game/DLC7/CampaignData/Missions/D7_Counterattack/D7_Counterattack_Mission_AreaSpec', '/Game/DLC7/CampaignData/Missions/D7_Counterattack/D7_Counterattack_Mission_Scenario', '/Game/DLC7/CampaignData/Missions/D7_Counterattack/D7_Counterattack_Trees_DCC', '/Game/DLC7/CampaignData/Missions/D7_Counterattack/Level/D7_Counterattack_Mission_Enemies_AreaTile', '/Game/DLC7/CampaignData/Missions/D7_Counterattack/Level/D7_Counterattack_Mission_Friendlies_AreaTile', '/Game/DLC7/CampaignData/Missions/D7_DefendComms/ArcActions/D7M5_AutoAcceptMission', '/Game/DLC7/CampaignData/Missions/D7_DefendComms/ArcActions/D7M5_AutoAcceptObjective', '/Game/DLC7/CampaignData/Missions/D7_DefendComms/ArcActions/D7M5_Completed', '/Game/DLC7/CampaignData/Missions/D7_DefendComms/ArcActions/D7M5_Offer', '/Game/DLC7/CampaignData/Missions/D7_DefendComms/ArcActions/D7M5_Place_Mission', '/Game/DLC7/CampaignData/Missions/D7_DefendComms/ArcActions/D7M5_Reset_Scenario', '/Game/DLC7/CampaignData/Missions/D7_DefendComms/ArcActions/Show_D7M5', '/Game/DLC7/CampaignData/Missions/D7_DefendComms/ArcActions/Unlock_D7M5_InstantAction', '/Game/DLC7/CampaignData/Missions/D7_DefendComms/D7M5_Briefing', '/Game/DLC7/CampaignData/Missions/D7_DefendComms/D7M5_Prompt', '/Game/DLC7/CampaignData/Missions/D7_DefendComms/D7_DefendComms_BattleGrid', '/Game/DLC7/CampaignData/Missions/D7_DefendComms/D7_DefendComms_Biome', '/Game/DLC7/CampaignData/Missions/D7_DefendComms/D7_DefendComms_Mission_AreaSpec', '/Game/DLC7/CampaignData/Missions/D7_DefendComms/D7_DefendComms_Mission_Scenario', '/Game/DLC7/CampaignData/Missions/D7_DefendComms/Level/D7_DefendComms_Mission_Enemies_AreaTile', '/Game/DLC7/CampaignData/Missions/D7_DefendComms/Level/D7_DefendComms_Mission_Friendlies_AreaTile', '/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/D7M12_AutoAcceptMission', '/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/D7M12_AutoAcceptObjective', '/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/D7M12_Completed', '/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/D7M12_Offer', '/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/D7M12_Place_Mission', '/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/D7M12_Reset_Scenario', '/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/Show_D7M12']}`
- `/Game/DLC7/PlaceClusterActions`: `{'exists': True, 'asset_count': 45, 'focused_count': 45, 'focused_sample': ['/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Periphery_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave1_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave2_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave3_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave4_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave5_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Periphery_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave1_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave2_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave3_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave4_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave5_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Periphery_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave1_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave2_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave3_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave4_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave5_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Periphery_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave1_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave2_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave3_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave4_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave5_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Periphery_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave1_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave2_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave3_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave4_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave5_PlaceCluster_ArcAction', '/Game/DLC7/PlaceClusterActions/RemoveClusterToiArcAction', '/Game/DLC7/PlaceClusterActions/RemoveClusters/RemoveWave1', '/Game/DLC7/PlaceClusterActions/RemoveClusters/RemoveWave2', '/Game/DLC7/PlaceClusterActions/RemoveClusters/RemoveWave3', '/Game/DLC7/PlaceClusterActions/RemoveClusters/RemoveWave4', '/Game/DLC7/PlaceClusterActions/RemoveClusters/RemoveWave5', '/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByEndOfInvasion', '/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByPeripheryWave', '/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave1', '/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave2', '/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave3', '/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave4', '/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5', '/Game/DLC7/PlaceClusterActions/ReplacementClusterDataTable', '/Game/DLC7/PlaceClusterActions/ReplacementClusterStruct']}`
- `/ModOverride/TKUCompatEditorPatch/Campaign/Clusters`: `{'exists': True, 'asset_count': 0, 'focused_count': 0, 'focused_sample': []}`
- `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/Clusters`: `{'exists': True, 'asset_count': 0, 'focused_count': 0, 'focused_sample': []}`
- `/ModOverride/TKUCompatEditorPatch/DLC7`: `{'exists': False, 'asset_count': 0, 'focused_count': 0, 'focused_sample': []}`
- `dlc7_arc_assets`: `55`

## Walked Assets

### `/Game/DLC1/CareerMode/StartConditions/CareerMode_Start`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/CareerModeCoreCampaign`
- event actions: `5`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CreateCoOpReadySave_ArcAction`
  - `/Game/Campaign/NewsReel/NewsFeed_ArcAction`
  - `/Game/DLC1/CareerMode/StartConditions/Arcs/SetCompanyUnfounded`
  - `/Game/DLC1/CareerMode/Warzones/Rasalhauge_Clusters/PlaceRasalhague_ArcAction_7_10`
  - `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/CareerMode_Start`

### `/Game/DLC1/CareerMode/StartConditions/FRR_CareerMode_Start`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/CareerModeCoreCampaign`
- event actions: `5`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CreateCoOpReadySave_ArcAction`
  - `/Game/Campaign/NewsReel/NewsFeed_ArcAction`
  - `/Game/DLC1/CareerMode/StartConditions/Arcs/SetCompanyUnfounded`
  - `/Game/DLC1/CareerMode/Warzones/Rasalhauge_Clusters/PlaceRasalhague_ArcAction_1_3`
  - `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/FRR_CareerMode_Start`

### `/Game/DLC1/CareerMode/CareerModeCoreCampaign`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `16`
  - `/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`
  - `/Game/Campaign/CampaignArcs/FactionStarts/AddDefaultCodexEntries_Arc`
  - `/Game/Campaign/CampaignArcs/GameOver/Overdraft_Arc`
  - `/Game/Campaign/CampaignArcs/HidingSystems/HidingSystemsArc`
  - `/Game/Campaign/CampaignArcs/Razer_Exclusive/Razer_WolverineArc`
  - `/Game/DLC1/CareerMode/CantinaArc`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
  - `/Game/DLC1/CareerMode/Sidequests/MS_Exclusive/DLC1_GoblinArc`
  - `/Game/DLC2/CampaignData/DLC2_CoreCampaign`
  - `/Game/DLC3/HatchetmanQuestData/DLC3_HatchetmanQuest`
  - `/Game/DLC4/CampaignData/DLC4_CoreCampaign`
  - `/Game/DLC5/CampaignData/DLC5_CoreCampaign`
  - `/Game/DLC6/CampaignData/DLC6_CoreCampaign`
  - `/Game/DLC7/CampaignData/DLC7_CoreCampaign`
  - `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
  - `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- event actions: `3`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/Lock_Operations_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/OfferCantinaAsperational_ArcAction`
  - `/Game/DLC1/DLC_1`

### `/Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `60`
  - `/Game/Campaign/CampaignArcs/Regions/MercStars/Place_MercStars_Arc`
  - `/Game/DLC1/CareerMode/Warzones/D_11_12/Common_D_11_12`
  - `/Game/DLC1/CareerMode/Warzones/D_12_13/Common_D_12_13`
  - `/Game/DLC1/CareerMode/Warzones/D_15/Common_D_15`
  - `/Game/DLC1/CareerMode/Warzones/D_1_2/Common_D_1_2`
  - `/Game/DLC1/CareerMode/Warzones/D_2_3/Common_D_2_3`
  - `/Game/DLC1/CareerMode/Warzones/D_2_4/Common_D_2_4`
  - `/Game/DLC1/CareerMode/Warzones/D_3_5/Common_D_3_5`
  - `/Game/DLC1/CareerMode/Warzones/D_3_6/Common_D_3_6`
  - `/Game/DLC1/CareerMode/Warzones/D_4_6/Common_D_4_6`
  - `/Game/DLC1/CareerMode/Warzones/D_5_7/Common_D_5_7`
  - `/Game/DLC1/CareerMode/Warzones/D_5_8/Common_D_5_8`
  - `/Game/DLC1/CareerMode/Warzones/D_6_7/Common_D_6_7`
  - `/Game/DLC1/CareerMode/Warzones/D_6_8/Common_D_6_8`
  - `/Game/DLC1/CareerMode/Warzones/D_7_10/Common_D_7_10`
  - `/Game/DLC1/CareerMode/Warzones/K_12_13/Common_K_12_13`
  - `/Game/DLC1/CareerMode/Warzones/K_13_14/Common_K_13_14`
  - `/Game/DLC1/CareerMode/Warzones/K_1_2/Common_K_1_2`
  - `/Game/DLC1/CareerMode/Warzones/K_2_3/Common_K_2_3`
  - `/Game/DLC1/CareerMode/Warzones/K_3_4/Common_K_3_4`
  - `/Game/DLC1/CareerMode/Warzones/K_3_5/Common_K_3_5`
  - `/Game/DLC1/CareerMode/Warzones/K_3_5_1/Common_K_3_5_1`
  - `/Game/DLC1/CareerMode/Warzones/K_4_5/Common_K_4_5`
  - `/Game/DLC1/CareerMode/Warzones/K_5_6/Common_K_5_6`
  - `/Game/DLC1/CareerMode/Warzones/K_6_7/Common_K_6_7`
  - `/Game/DLC1/CareerMode/Warzones/K_6_8/Common_K_6_8`
  - `/Game/DLC1/CareerMode/Warzones/K_7_9/Common_K_7_9`
  - `/Game/DLC1/CareerMode/Warzones/K_8_10/Common_K_8_10`
  - `/Game/DLC1/CareerMode/Warzones/L_11_12/Common_L_11_12`
  - `/Game/DLC1/CareerMode/Warzones/L_12_13/Common_L_12_13`
  - `/Game/DLC1/CareerMode/Warzones/L_13_14/Common_L_13_14`
  - `/Game/DLC1/CareerMode/Warzones/L_1_2/Common_L_1_2`
  - `/Game/DLC1/CareerMode/Warzones/L_2_5/Common_L_2_5`
  - `/Game/DLC1/CareerMode/Warzones/L_3_6/Common_L_3_6`
  - `/Game/DLC1/CareerMode/Warzones/L_5_8/Common_L_5_8`
  - `/Game/DLC1/CareerMode/Warzones/L_7_10/Common_L_7_10`
  - `/Game/DLC1/CareerMode/Warzones/M_11_12/Common_M_11_12`
  - `/Game/DLC1/CareerMode/Warzones/M_12_13/Common_M_12_13`
  - `/Game/DLC1/CareerMode/Warzones/M_12_13_1/Common_M_12_13_1`
  - `/Game/DLC1/CareerMode/Warzones/M_13_14/Common_M_13_14`
  - `/Game/DLC1/CareerMode/Warzones/M_15/Common_M_15`
  - `/Game/DLC1/CareerMode/Warzones/M_1_2/Common_M_1_2`
  - `/Game/DLC1/CareerMode/Warzones/M_2_5/Common_M_2_5`
  - `/Game/DLC1/CareerMode/Warzones/M_3_6/Common_M_3_6`
  - `/Game/DLC1/CareerMode/Warzones/M_5_8/Common_M_5_8`
  - `/Game/DLC1/CareerMode/Warzones/M_7_10/Common_M_7_10`
  - `/Game/DLC1/CareerMode/Warzones/M_9_11/Common_M_9_11`
  - `/Game/DLC1/CareerMode/Warzones/S_10_12/Common_S_10_12`
  - `/Game/DLC1/CareerMode/Warzones/S_12_13/Common_S_12_13`
  - `/Game/DLC1/CareerMode/Warzones/S_13_14/Common_S_13_14`

### `/Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `35`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_10_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_11_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_12_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_13_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_14_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_15_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_16_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_17_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_18_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_19_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_1_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_20_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_21_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_22_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_23_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_24_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_25_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_26_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_27_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_28_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_29_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_2_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_30_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_31_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_32_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_33_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_34_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_35_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_3_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_4_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_5_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_6_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_7_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_8_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_9_ArcAction`

### `/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `8`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3025_ThirdSuccession/3025_ThirdSuccession`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3029_FormationOfTikinovAndStIves/3029_FormationOfTikinovAndStIves`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3030_FourthSuccession/3030_FourthSuccession`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3031_TikinovJoinsFederatedSuns/3031_TikinovJoinsFederatedSuns`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3034_RassalhaugeRecognized/Borders_Year3034_RassalhaugeRecognized`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3039_WarOf3039/3039_WarOf3039`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3041_FormationOfFederatedCommonwealth/3041_FormationOfFederatedCommonwealth`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3049_ClanInvasion/3049_ClanInvasion`

### `/Game/DLC7/CampaignData/DLC7_CoreCampaign`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `9`
  - `/Game/DLC7/CampaignData/AtlasII_MarketArc`
  - `/Game/DLC7/CampaignData/DLC7_NewReelArc`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
  - `/Game/DLC7/CampaignData/DLC7_Pt0_Warnings`
  - `/Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
  - `/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague`
  - `/Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
  - `/Game/DLC7/CampaignData/DLC7_Pt4_ReturnToUnchartedSystems`
  - `/Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
- event actions: `17`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_CustomMarket1_Alleghe_ArcAction`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Pt0_CompleteKickoff`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Pt0_PriorityTransmission`
  - `/Game/DLC7/CampaignData/CampaignArcActions/TravelTo_D7M1`
  - `/Game/DLC7/CampaignData/DLC7_CoreCampaign`
  - `/Game/DLC7/CampaignData/DLC7_Pt0_KickoffPrompt`
  - `/Game/DLC7/CampaignData/Missions/D7_Hunting/ArcActions/D7M1_AutoAcceptMission`
  - `/Game/DLC7/CampaignData/Missions/D7_Hunting/ArcActions/D7M1_AutoAcceptObjective`
  - `/Game/DLC7/CampaignData/Missions/D7_Hunting/ArcActions/D7M1_Completed`
  - `/Game/DLC7/CampaignData/Missions/D7_Hunting/ArcActions/D7M1_Offer`
  - `/Game/DLC7/CampaignData/Missions/D7_Hunting/ArcActions/D7M1_Place_Mission`
  - `/Game/DLC7/CampaignData/Missions/D7_Hunting/ArcActions/Unlock_D7M1_InstantAction`
  - `/Game/DLC7/CampaignData/Missions/D7_Hunting/D7M1_Prompt`
  - `/Game/DLC7/CampaignData/Missions/D7_Hunting/D7_Hunting_Mission_Scenario`
  - `/Game/DLC7/DLC_7`

### `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `40`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceRasalhagueCluster`
  - `/Game/DLC7/CampaignData/DLC7_CoreCampaign`
  - `/Game/DLC7/DLC_7`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Periphery_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave1_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave2_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave3_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave4_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave5_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Periphery_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave1_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave2_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave3_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave4_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave5_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Periphery_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave1_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave2_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave3_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave4_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave5_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Periphery_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave1_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave2_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave3_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave4_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave5_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Periphery_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave1_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave2_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave3_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave4_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave5_PlaceCluster_ArcAction`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByEndOfInvasion`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByPeripheryWave`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave1`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave2`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave3`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave4`
  - `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5`

### `/Game/DLC7/CampaignData/DLC7_ShowUnchartedSystems`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `3`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceHiddenSystemsCluster`
  - `/Game/DLC7/CampaignData/CampaignArcActions/Unhide_BaseCampaignStars`
  - `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/D7M9_Prompt`

### `/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `15`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_CustomMarket4_Rasalhague_ArcAction`
  - `/Game/DLC7/CampaignData/CampaignArcActions/TravelTo_D7M4`
  - `/Game/DLC7/CampaignData/DLC7_Pt1-2_LastFrontier`
  - `/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_AutoAcceptMission`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_AutoAcceptObjective`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_Completed`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_Offer`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_Place_Mission`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/Unlock_D7M4_InstantAction`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/D7M4_Prompt`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/D7_Spaceport_Mission_Scenario`
  - `/Game/DLC7/DLC_7`

### `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/CareerModeCoreCampaign`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `16`
  - `/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`
  - `/Game/Campaign/CampaignArcs/FactionStarts/AddDefaultCodexEntries_Arc`
  - `/Game/Campaign/CampaignArcs/GameOver/Overdraft_Arc`
  - `/Game/Campaign/CampaignArcs/HidingSystems/HidingSystemsArc`
  - `/Game/Campaign/CampaignArcs/Razer_Exclusive/Razer_WolverineArc`
  - `/Game/DLC1/CareerMode/CantinaArc`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
  - `/Game/DLC1/CareerMode/Sidequests/MS_Exclusive/DLC1_GoblinArc`
  - `/Game/DLC2/CampaignData/DLC2_CoreCampaign`
  - `/Game/DLC3/HatchetmanQuestData/DLC3_HatchetmanQuest`
  - `/Game/DLC4/CampaignData/DLC4_CoreCampaign`
  - `/Game/DLC5/CampaignData/DLC5_CoreCampaign`
  - `/Game/DLC6/CampaignData/DLC6_CoreCampaign`
  - `/Game/DLC7/CampaignData/DLC7_CoreCampaign`
  - `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
  - `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- event actions: `3`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/Lock_Operations_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/OfferCantinaAsperational_ArcAction`
  - `/Game/DLC1/DLC_1`

### `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `60`
  - `/Game/Campaign/CampaignArcs/Regions/MercStars/Place_MercStars_Arc`
  - `/Game/DLC1/CareerMode/Warzones/D_11_12/Common_D_11_12`
  - `/Game/DLC1/CareerMode/Warzones/D_12_13/Common_D_12_13`
  - `/Game/DLC1/CareerMode/Warzones/D_15/Common_D_15`
  - `/Game/DLC1/CareerMode/Warzones/D_1_2/Common_D_1_2`
  - `/Game/DLC1/CareerMode/Warzones/D_2_3/Common_D_2_3`
  - `/Game/DLC1/CareerMode/Warzones/D_2_4/Common_D_2_4`
  - `/Game/DLC1/CareerMode/Warzones/D_3_5/Common_D_3_5`
  - `/Game/DLC1/CareerMode/Warzones/D_3_6/Common_D_3_6`
  - `/Game/DLC1/CareerMode/Warzones/D_4_6/Common_D_4_6`
  - `/Game/DLC1/CareerMode/Warzones/D_5_7/Common_D_5_7`
  - `/Game/DLC1/CareerMode/Warzones/D_5_8/Common_D_5_8`
  - `/Game/DLC1/CareerMode/Warzones/D_6_7/Common_D_6_7`
  - `/Game/DLC1/CareerMode/Warzones/D_6_8/Common_D_6_8`
  - `/Game/DLC1/CareerMode/Warzones/D_7_10/Common_D_7_10`
  - `/Game/DLC1/CareerMode/Warzones/K_12_13/Common_K_12_13`
  - `/Game/DLC1/CareerMode/Warzones/K_13_14/Common_K_13_14`
  - `/Game/DLC1/CareerMode/Warzones/K_1_2/Common_K_1_2`
  - `/Game/DLC1/CareerMode/Warzones/K_2_3/Common_K_2_3`
  - `/Game/DLC1/CareerMode/Warzones/K_3_4/Common_K_3_4`
  - `/Game/DLC1/CareerMode/Warzones/K_3_5/Common_K_3_5`
  - `/Game/DLC1/CareerMode/Warzones/K_3_5_1/Common_K_3_5_1`
  - `/Game/DLC1/CareerMode/Warzones/K_4_5/Common_K_4_5`
  - `/Game/DLC1/CareerMode/Warzones/K_5_6/Common_K_5_6`
  - `/Game/DLC1/CareerMode/Warzones/K_6_7/Common_K_6_7`
  - `/Game/DLC1/CareerMode/Warzones/K_6_8/Common_K_6_8`
  - `/Game/DLC1/CareerMode/Warzones/K_7_9/Common_K_7_9`
  - `/Game/DLC1/CareerMode/Warzones/K_8_10/Common_K_8_10`
  - `/Game/DLC1/CareerMode/Warzones/L_11_12/Common_L_11_12`
  - `/Game/DLC1/CareerMode/Warzones/L_12_13/Common_L_12_13`
  - `/Game/DLC1/CareerMode/Warzones/L_13_14/Common_L_13_14`
  - `/Game/DLC1/CareerMode/Warzones/L_1_2/Common_L_1_2`
  - `/Game/DLC1/CareerMode/Warzones/L_2_5/Common_L_2_5`
  - `/Game/DLC1/CareerMode/Warzones/L_3_6/Common_L_3_6`
  - `/Game/DLC1/CareerMode/Warzones/L_5_8/Common_L_5_8`
  - `/Game/DLC1/CareerMode/Warzones/L_7_10/Common_L_7_10`
  - `/Game/DLC1/CareerMode/Warzones/M_11_12/Common_M_11_12`
  - `/Game/DLC1/CareerMode/Warzones/M_12_13/Common_M_12_13`
  - `/Game/DLC1/CareerMode/Warzones/M_12_13_1/Common_M_12_13_1`
  - `/Game/DLC1/CareerMode/Warzones/M_13_14/Common_M_13_14`
  - `/Game/DLC1/CareerMode/Warzones/M_15/Common_M_15`
  - `/Game/DLC1/CareerMode/Warzones/M_1_2/Common_M_1_2`
  - `/Game/DLC1/CareerMode/Warzones/M_2_5/Common_M_2_5`
  - `/Game/DLC1/CareerMode/Warzones/M_3_6/Common_M_3_6`
  - `/Game/DLC1/CareerMode/Warzones/M_5_8/Common_M_5_8`
  - `/Game/DLC1/CareerMode/Warzones/M_7_10/Common_M_7_10`
  - `/Game/DLC1/CareerMode/Warzones/M_9_11/Common_M_9_11`
  - `/Game/DLC1/CareerMode/Warzones/S_10_12/Common_S_10_12`
  - `/Game/DLC1/CareerMode/Warzones/S_12_13/Common_S_12_13`
  - `/Game/DLC1/CareerMode/Warzones/S_13_14/Common_S_13_14`

### `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `35`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_10_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_11_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_12_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_13_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_14_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_15_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_16_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_17_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_18_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_19_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_1_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_20_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_21_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_22_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_23_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_24_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_25_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_26_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_27_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_28_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_29_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_2_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_30_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_31_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_32_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_33_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_34_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_35_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_3_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_4_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_5_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_6_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_7_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_8_ArcAction`
  - `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_9_ArcAction`

### `/Game/DLC7/CampaignData/AtlasII_MarketArc`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `3`
  - `/Game/DLC7/CampaignData/AtlasII_PlaceToi_ArcAction`
  - `/Game/DLC7/CampaignData/AtlasII_Purchased`
  - `/Game/DLC7/DLC_7`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_CustomMarket1_Alleghe_ArcAction`
- depth/reason: `0` / `root`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB0CD4FBF0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB0CD4FBF0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_CustomMarket2_Rodrigo_ArcAction`
- depth/reason: `0` / `root`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB0B57EDF0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB0B57EDF0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_CustomMarket3_LastFrontier_ArcAction`
- depth/reason: `0` / `root`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB0B57D570) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB0B57D570) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_CustomMarket4_Rasalhague_ArcAction`
- depth/reason: `0` / `root`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB0B1BE450) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB0B1BE450) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_CustomMarket4_UnchartedSystems_ArcAction`
- depth/reason: `0` / `root`
- class: `ObjectRedirector` exists `True`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_CustomMarket5_UnchartedSystems_ArcAction`
- depth/reason: `0` / `root`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB0B57D030) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB0B57D030) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_D7M10_TravelBriefing`
- depth/reason: `0` / `root`
- class: `MWBriefingAsset` exists `True`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_D7M1_TravelBriefing`
- depth/reason: `0` / `root`
- class: `MWBriefingAsset` exists `True`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_D7M2_TravelBriefing`
- depth/reason: `0` / `root`
- class: `MWBriefingAsset` exists `True`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_D7M4_TravelBriefing`
- depth/reason: `0` / `root`
- class: `MWBriefingAsset` exists `True`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_D7M7_TravelBriefing`
- depth/reason: `0` / `root`
- class: `MWBriefingAsset` exists `True`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_DeclinedContract`
- depth/reason: `0` / `root`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB184E1F80) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB184E1F80) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_FailedContract_Complete`
- depth/reason: `0` / `root`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB184E1EA0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB184E1EA0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Holo1_Objective`
- depth/reason: `0` / `root`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Holo1_SpeakToRyana`
- depth/reason: `0` / `root`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB0A63B950) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB0A63B950) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Holo2_Objective`
- depth/reason: `0` / `root`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Holo2_SpeakToRyana`
- depth/reason: `0` / `root`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB0A63B250) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB0A63B250) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Holo3_Objective`
- depth/reason: `0` / `root`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Holo3_SpeakToRyana`
- depth/reason: `0` / `root`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB0A63AED0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB0A63AED0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PastStarDate_ArcAction`
- depth/reason: `0` / `root`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB185466F0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB185466F0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceHiddenSystemsCluster`
- depth/reason: `0` / `root`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster.DLC7_HiddenSystems_CampaignCluster' (0x000001BA19C5FB00) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'DLC7_HiddenSystems_CampaignCluster', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster.DLC7_HiddenSystems_CampaignCluster', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster.DLC7_HiddenSystems_CampaignCluster', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster.DLC7_HiddenSystems_CampaignCluster', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster.DLC7_HiddenSystems_CampaignCluster' (0x000001BA19C5FB00) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB96E3E70) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB96E3E70) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB96E3DD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB96E3DD0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceRasalhagueCluster`
- depth/reason: `0` / `root`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_CampaignCluster1']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_CampaignCluster1.DLC7_CampaignCluster1' (0x000001BA19C5F9C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'DLC7_CampaignCluster1', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_CampaignCluster1.DLC7_CampaignCluster1', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_CampaignCluster1.DLC7_CampaignCluster1', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_CampaignCluster1.DLC7_CampaignCluster1', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_CampaignCluster1'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_CampaignCluster1.DLC7_CampaignCluster1' (0x000001BA19C5F9C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB96E0C70) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB96E0C70) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB96E0BD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB96E0BD0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Pt0_CompleteKickoff`
- depth/reason: `0` / `root`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB181D0770) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB181D0770) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Pt0_KickoffBriefing`
- depth/reason: `0` / `root`
- class: `MWBriefingAsset` exists `True`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Pt0_Offer_1MonthWarning_ArcAction`
- depth/reason: `0` / `root`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18546530) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18546530) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Pt0_Offer_3MonthWarning_ArcAction`
- depth/reason: `0` / `root`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18546450) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18546450) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Pt0_PriorityTransmission`
- depth/reason: `0` / `root`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB9403B50) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB9403B50) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_CampaignCluster1`
- depth/reason: `0` / `root`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_CampaignCluster1']`

### `/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster`
- depth/reason: `0` / `root`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster']`

### `/Game/DLC7/CampaignData/DEBUG_DLC7_Act2_CampaignArc`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `19`
  - `/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`
  - `/Game/Campaign/CampaignArcs/FactionStarts/AddDefaultCodexEntries_Arc`
  - `/Game/Campaign/CampaignArcs/GameOver/Overdraft_Arc`
  - `/Game/Campaign/CampaignArcs/Razer_Exclusive/Razer_WolverineArc`
  - `/Game/DLC1/CareerMode/CantinaArc`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
  - `/Game/DLC1/CareerMode/Sidequests/MS_Exclusive/DLC1_GoblinArc`
  - `/Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
  - `/Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
  - `/Game/DLC2/CampaignData/DLC2_CoreCampaign`
  - `/Game/DLC3/HatchetmanQuestData/DLC3_HatchetmanQuest`
  - `/Game/DLC4/CampaignData/DLC4_CoreCampaign`
  - `/Game/DLC5/CampaignData/DLC5_CoreCampaign`
  - `/Game/DLC6/CampaignData/DLC6_CoreCampaign`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
  - `/Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
  - `/Game/DLC7/CampaignData/DLC7_Pt4_ReturnToUnchartedSystems`
  - `/Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
  - `/Game/DLC7/CampaignData/DLC7_ShowUnchartedSystems`
- event actions: `7`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CreateCoOpReadySave_ArcAction`
  - `/Game/DLC1/CareerMode/StartConditions/Arcs/SetCompanyUnfounded`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_AutoAcceptObjective`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_Completed`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_Offer`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/D7M4_Prompt`
  - `/Game/DLC7/_StartConditions/DLC7AddRep_ArcAction`

### `/Game/DLC7/CampaignData/DEBUG_DLC7_Act3_CampaignArc`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `20`
  - `/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`
  - `/Game/Campaign/CampaignArcs/FactionStarts/AddDefaultCodexEntries_Arc`
  - `/Game/Campaign/CampaignArcs/GameOver/Overdraft_Arc`
  - `/Game/Campaign/CampaignArcs/HidingSystems/HidingSystemsArc`
  - `/Game/Campaign/CampaignArcs/Razer_Exclusive/Razer_WolverineArc`
  - `/Game/DLC1/CareerMode/CantinaArc`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
  - `/Game/DLC1/CareerMode/Sidequests/MS_Exclusive/DLC1_GoblinArc`
  - `/Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
  - `/Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
  - `/Game/DLC2/CampaignData/DLC2_CoreCampaign`
  - `/Game/DLC3/HatchetmanQuestData/DLC3_HatchetmanQuest`
  - `/Game/DLC4/CampaignData/DLC4_CoreCampaign`
  - `/Game/DLC5/CampaignData/DLC5_CoreCampaign`
  - `/Game/DLC6/CampaignData/DLC6_CoreCampaign`
  - `/Game/DLC7/CampaignData/DLC7_Holo2_CampaignArc`
  - `/Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
  - `/Game/DLC7/CampaignData/DLC7_Pt4_ReturnToUnchartedSystems`
  - `/Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
  - `/Game/DLC7/CampaignData/DLC7_ShowUnchartedSystems`
- event actions: `9`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CreateCoOpReadySave_ArcAction`
  - `/Game/Campaign/NewsReel/NewsFeed_ArcAction`
  - `/Game/DLC1/CareerMode/StartConditions/Arcs/SetCompanyUnfounded`
  - `/Game/DLC3/HatchetmanQuestData/_StartConditions/DLC3Campaign_Start`
  - `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/ArcActions/D7M9_AutoAcceptObjective`
  - `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/ArcActions/D7M9_Completed`
  - `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/ArcActions/D7M9_Offer`
  - `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/D7M9_Prompt`
  - `/Game/DLC7/_StartConditions/DLC7AddRep_ArcAction`

### `/Game/DLC7/CampaignData/DLC7_CampaignMissionText`
- depth/reason: `0` / `root`
- class: `DataTable` exists `True`

### `/Game/DLC7/CampaignData/DLC7_DeclineContract_Prompt`
- depth/reason: `0` / `root`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/DLC7_FailedContract_Prompt`
- depth/reason: `0` / `root`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/DLC7_Holo2_CampaignArc`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `4`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/SetFahadToBridge_ArcAction`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Holo2_SpeakToRyana`
  - `/Game/DLC7/CampaignData/CampaignArcActions/ShowSpears_ArcAction`
  - `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/D7M9_Prompt`

### `/Game/DLC7/CampaignData/DLC7_Holo3_CampaignArc`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `4`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/SetFahadToBridge_ArcAction`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Holo3_SpeakToRyana`
  - `/Game/DLC7/CampaignData/CampaignArcActions/ShowSpears_ArcAction`
  - `/Game/DLC7/CampaignData/Missions/D7_Investigate/D7M10_Prompt`

### `/Game/DLC7/CampaignData/DLC7_NewReelArc`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `3`
  - `/Game/DLC7/CampaignData/DLC7_NewReelArc`
  - `/Game/DLC7/CampaignData/DLC7_NewsFeed_ArcAction`
  - `/Game/DLC7/DLC_7`

### `/Game/DLC7/CampaignData/DLC7_NewsFeed_ArcAction`
- depth/reason: `0` / `root`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18547A30) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18547A30) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/DLC7_PastStartDate_Transmission`
- depth/reason: `0` / `root`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/DLC7_Pt0_KickoffPrompt`
- depth/reason: `0` / `root`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/DLC7_Pt0_Offer_1MonthWarning`
- depth/reason: `0` / `root`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/DLC7_Pt0_Offer_3MonthWarning`
- depth/reason: `0` / `root`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/DLC7_Pt0_Warnings`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `16`
  - `/Game/DLC5/DLC_5`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_DeclinedContract`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_FailedContract_Complete`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_PastStarDate_ArcAction`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Pt0_Offer_1MonthWarning_ArcAction`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Pt0_Offer_3MonthWarning_ArcAction`
  - `/Game/DLC7/CampaignData/DLC7_CoreCampaign`
  - `/Game/DLC7/CampaignData/DLC7_PastStartDate_Transmission`
  - `/Game/DLC7/CampaignData/DLC7_Pt0_Offer_1MonthWarning`
  - `/Game/DLC7/CampaignData/DLC7_Pt0_Offer_3MonthWarning`
  - `/Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
  - `/Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague`
  - `/Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
  - `/Game/DLC7/CampaignData/DLC7_Pt4_ReturnToUnchartedSystems`
  - `/Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
  - `/Game/DLC7/DLC_7`

### `/Game/DLC7/CampaignData/DLC7_Pt1-2_LastFrontier`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `20`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/SetFahadToBridge_ArcAction`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_CustomMarket3_LastFrontier_ArcAction`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Holo1_Objective`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_Holo1_SpeakToRyana`
  - `/Game/DLC7/CampaignData/CampaignArcActions/TravelTo_D7M7`
  - `/Game/DLC7/CampaignData/DLC7_Pt1-2_LastFrontier`
  - `/Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
  - `/Game/DLC7/CampaignData/IsInLastFrontier`
  - `/Game/DLC7/CampaignData/Missions/D7_Counterattack/D7M3_Prompt`
  - `/Game/DLC7/CampaignData/Missions/D7_LongRange/ArcActions/D7M7_AutoAcceptMission`
  - `/Game/DLC7/CampaignData/Missions/D7_LongRange/ArcActions/D7M7_AutoAcceptObjective`
  - `/Game/DLC7/CampaignData/Missions/D7_LongRange/ArcActions/D7M7_Completed`
  - `/Game/DLC7/CampaignData/Missions/D7_LongRange/ArcActions/D7M7_Offer`
  - `/Game/DLC7/CampaignData/Missions/D7_LongRange/ArcActions/D7M7_Place_Mission`
  - `/Game/DLC7/CampaignData/Missions/D7_LongRange/ArcActions/Unlock_D7M7_InstantAction`
  - `/Game/DLC7/CampaignData/Missions/D7_LongRange/D7M7_Prompt`
  - `/Game/DLC7/CampaignData/Missions/D7_LongRange/D7_LongRange_Mission_Scenario`
  - `/Game/DLC7/DLC_7`

### `/Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC7/CampaignData/DLC7_Pt1-2_LastFrontier`
- event actions: `24`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_CustomMarket2_Rodrigo_ArcAction`
  - `/Game/DLC7/CampaignData/CampaignArcActions/TravelTo_D7M2`
  - `/Game/DLC7/CampaignData/DLC7_CoreCampaign`
  - `/Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
  - `/Game/DLC7/CampaignData/Missions/D7_Battle_A/ArcActions/D7M2_AutoAcceptMission`
  - `/Game/DLC7/CampaignData/Missions/D7_Battle_A/ArcActions/D7M2_AutoAcceptObjective`
  - `/Game/DLC7/CampaignData/Missions/D7_Battle_A/ArcActions/D7M2_Completed`
  - `/Game/DLC7/CampaignData/Missions/D7_Battle_A/ArcActions/D7M2_Offer`
  - `/Game/DLC7/CampaignData/Missions/D7_Battle_A/ArcActions/D7M2_Place_Mission`
  - `/Game/DLC7/CampaignData/Missions/D7_Battle_A/ArcActions/Unlock_D7M2_InstantAction`
  - `/Game/DLC7/CampaignData/Missions/D7_Battle_A/D7M2_Prompt`
  - `/Game/DLC7/CampaignData/Missions/D7_Battle_A/D7_Battle_A_Mission_Scenario`
  - `/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/D7M3_AutoAcceptMission`
  - `/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/D7M3_AutoAcceptObjective`
  - `/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/D7M3_Completed`
  - `/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/D7M3_Offer`
  - `/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/D7M3_Place_Mission`
  - `/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/Show_D7M3`
  - `/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/Unlock_D7M3_InstantAction`
  - `/Game/DLC7/CampaignData/Missions/D7_Counterattack/D7M3_Prompt`
  - `/Game/DLC7/CampaignData/Missions/D7_Counterattack/D7_Counterattack_Mission_Scenario`
  - `/Game/DLC7/DLC_7`

### `/Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC7/CampaignData/DLC7_Holo2_CampaignArc`
- event actions: `39`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
  - `/Game/DLC7/CampaignData/Missions/D7_DefendComms/ArcActions/D7M5_AutoAcceptObjective`
  - `/Game/DLC7/CampaignData/Missions/D7_DefendComms/ArcActions/D7M5_Completed`
  - `/Game/DLC7/CampaignData/Missions/D7_DefendComms/ArcActions/D7M5_Offer`
  - `/Game/DLC7/CampaignData/Missions/D7_DefendComms/ArcActions/D7M5_Place_Mission`
  - `/Game/DLC7/CampaignData/Missions/D7_DefendComms/ArcActions/D7M5_Reset_Scenario`
  - `/Game/DLC7/CampaignData/Missions/D7_DefendComms/ArcActions/Unlock_D7M5_InstantAction`
  - `/Game/DLC7/CampaignData/Missions/D7_DefendComms/D7M5_Prompt`
  - `/Game/DLC7/CampaignData/Missions/D7_DefendComms/D7_DefendComms_Mission_Scenario`
  - `/Game/DLC7/CampaignData/Missions/D7_HoldTheLine/ArcActions/D7M8_AutoAcceptObjective`
  - `/Game/DLC7/CampaignData/Missions/D7_HoldTheLine/ArcActions/D7M8_Completed`
  - `/Game/DLC7/CampaignData/Missions/D7_HoldTheLine/ArcActions/D7M8_Offer`
  - `/Game/DLC7/CampaignData/Missions/D7_HoldTheLine/ArcActions/D7M8_Place_Mission`
  - `/Game/DLC7/CampaignData/Missions/D7_HoldTheLine/ArcActions/D7M8_Reset_Scenario`
  - `/Game/DLC7/CampaignData/Missions/D7_HoldTheLine/ArcActions/Show_D7M8`
  - `/Game/DLC7/CampaignData/Missions/D7_HoldTheLine/ArcActions/Unlock_D7M8_InstantAction`
  - `/Game/DLC7/CampaignData/Missions/D7_HoldTheLine/D7M8_Prompt`
  - `/Game/DLC7/CampaignData/Missions/D7_HoldTheLine/D7_HoldTheLine_Mission_Scenario`
  - `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/ArcActions/D7M9_AutoAcceptObjective`
  - `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/ArcActions/D7M9_Completed`
  - `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/ArcActions/D7M9_Offer`
  - `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/ArcActions/D7M9_Place_Mission`
  - `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/ArcActions/D7M9_Reset_Scenario`
  - `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/ArcActions/Show_D7M9`
  - `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/ArcActions/Unlock_D7M9_InstantAction`
  - `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/D7M9_Prompt`
  - `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/D7_Reinforcements_Mission_Scenario`
  - `/Game/DLC7/CampaignData/Missions/D7_Spaceport/D7M4_Prompt`
  - `/Game/DLC7/CampaignData/Missions/D7_SupplyLines/ArcActions/D7M6_AutoAcceptObjective`
  - `/Game/DLC7/CampaignData/Missions/D7_SupplyLines/ArcActions/D7M6_Completed`
  - `/Game/DLC7/CampaignData/Missions/D7_SupplyLines/ArcActions/D7M6_Offer`
  - `/Game/DLC7/CampaignData/Missions/D7_SupplyLines/ArcActions/D7M6_Place_Mission`
  - `/Game/DLC7/CampaignData/Missions/D7_SupplyLines/ArcActions/D7M6_Reset_Scenario`
  - `/Game/DLC7/CampaignData/Missions/D7_SupplyLines/ArcActions/Show_D7M6`
  - `/Game/DLC7/CampaignData/Missions/D7_SupplyLines/ArcActions/Unlock_D7M6_InstantAction`
  - `/Game/DLC7/CampaignData/Missions/D7_SupplyLines/D7M6_Prompt`
  - `/Game/DLC7/CampaignData/Missions/D7_SupplyLines/D7_SupplyLines_Mission_Scenario`
  - `/Game/DLC7/DLC_7`

### `/Game/DLC7/CampaignData/DLC7_Pt4_ReturnToUnchartedSystems`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `2`
  - `/Game/DLC7/CampaignData/DLC7_Holo3_CampaignArc`
  - `/Game/DLC7/CampaignData/DLC7_ShowUnchartedSystems`
- event actions: `18`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC7/CampaignData/CampaignArcActions/DLC7_CustomMarket5_UnchartedSystems_ArcAction`
  - `/Game/DLC7/CampaignData/CampaignArcActions/TravelTo_D7M10`
  - `/Game/DLC7/CampaignData/DLC7_Holo2_CampaignArc`
  - `/Game/DLC7/CampaignData/DLC7_Pt4_ReturnToUnchartedSystems`
  - `/Game/DLC7/CampaignData/Missions/D7_Investigate/ArcActions/D7M10_AutoAcceptMission`
  - `/Game/DLC7/CampaignData/Missions/D7_Investigate/ArcActions/D7M10_AutoAcceptObjective`
  - `/Game/DLC7/CampaignData/Missions/D7_Investigate/ArcActions/D7M10_Completed`
  - `/Game/DLC7/CampaignData/Missions/D7_Investigate/ArcActions/D7M10_Offer`
  - `/Game/DLC7/CampaignData/Missions/D7_Investigate/ArcActions/D7M10_Place_Mission`
  - `/Game/DLC7/CampaignData/Missions/D7_Investigate/ArcActions/Unlock_D7M10_InstantAction`
  - `/Game/DLC7/CampaignData/Missions/D7_Investigate/D7M10_KickoffPrompt`
  - `/Game/DLC7/CampaignData/Missions/D7_Investigate/D7M10_Prompt`
  - `/Game/DLC7/CampaignData/Missions/D7_Investigate/D7_Investigate_Mission_Scenario`
  - `/Game/DLC7/CampaignData/Missions/D7_Investigate/DLC7_Pt4_KickoffComplete`
  - `/Game/DLC7/CampaignData/Missions/D7_Investigate/DLC7_Pt4_Kickoff_PriorityTransmission`
  - `/Game/DLC7/DLC_7`

### `/Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
- depth/reason: `0` / `root`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `23`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC7/CampaignData/DLC7_Holo3_CampaignArc`
  - `/Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
  - `/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/D7M12_AutoAcceptMission`
  - `/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/D7M12_AutoAcceptObjective`
  - `/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/D7M12_Completed`
  - `/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/D7M12_Offer`
  - `/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/D7M12_Place_Mission`
  - `/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/D7M12_Reset_Scenario`
  - `/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/Show_D7M12`
  - `/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/Unlock_D7M12_InstantAction`
  - `/Game/DLC7/CampaignData/Missions/D7_FirstBattle/D7M12_Prompt`
  - `/Game/DLC7/CampaignData/Missions/D7_FirstBattle/D7_FirstBattle_Mission_Scenario`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_AutoAcceptMission`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_AutoAcceptObjective`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_Completed`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_Offer`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_Place_Mission`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_Reset_Scenario`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/Unlock_D7M11_InstantAction`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7M11_Prompt`
  - `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7_WavesDefend_Mission_Scenario`

### `/Game/DLC7/CampaignData/Missions/D7_Investigate/DLC7_Pt4_KickoffComplete`
- depth/reason: `0` / `root`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18582840) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18582840) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Investigate/DLC7_Pt4_Kickoff_PriorityTransmission`
- depth/reason: `0` / `root`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8405FD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8405FD0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CreateCoOpReadySave_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/CareerMode_Start`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB05D8550) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB05D8550) {id: 0}>"}}`

### `/Game/Campaign/NewsReel/NewsFeed_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/CareerMode_Start`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB180CC690) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB180CC690) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/StartConditions/Arcs/SetCompanyUnfounded`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/CareerMode_Start`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAF889C330) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAF889C330) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/Rasalhauge_Clusters/PlaceRasalhague_ArcAction_7_10`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/CareerMode_Start`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset', '/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset.Rasalhague_7_10_ClusterAsset' (0x000001BAB91A34C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'Rasalhague_7_10_ClusterAsset', 'get_path_name': '/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset.Rasalhague_7_10_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset.Rasalhague_7_10_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset.Rasalhague_7_10_ClusterAsset', 'asset_paths': ['/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset'], 'repr': "<Object '/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset.Rasalhague_7_10_ClusterAsset' (0x000001BAB91A34C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB91A1F30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Rasalhague_7_10_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB91A1F30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Rasalhague_7_10_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB91A1E90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB91A1E90) {id: 0}>"}}`

### `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/CareerMode_Start`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/CareerMode_Start`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/CareerModeCoreCampaign`
- event actions: `5`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CreateCoOpReadySave_ArcAction`
  - `/Game/Campaign/NewsReel/NewsFeed_ArcAction`
  - `/Game/DLC1/CareerMode/StartConditions/Arcs/SetCompanyUnfounded`
  - `/Game/DLC1/CareerMode/Warzones/Rasalhauge_Clusters/PlaceRasalhague_ArcAction_7_10`
  - `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/CareerMode_Start`

### `/Game/DLC1/CareerMode/Warzones/Rasalhauge_Clusters/PlaceRasalhague_ArcAction_1_3`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/FRR_CareerMode_Start`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/Rasalhague_1_3/Rasalhague_1_3_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/Rasalhague_1_3/Rasalhague_1_3_ClusterAsset.Rasalhague_1_3_ClusterAsset' (0x000001BA9C333240) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'Rasalhague_1_3_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/Rasalhague_1_3/Rasalhague_1_3_ClusterAsset.Rasalhague_1_3_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/Rasalhague_1_3/Rasalhague_1_3_ClusterAsset.Rasalhague_1_3_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/Rasalhague_1_3/Rasalhague_1_3_ClusterAsset.Rasalhague_1_3_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/Rasalhague_1_3/Rasalhague_1_3_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/Rasalhague_1_3/Rasalhague_1_3_ClusterAsset.Rasalhague_1_3_ClusterAsset' (0x000001BA9C333240) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB919A6B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Rasalhague_1_3_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB919A6B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Rasalhague_1_3_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB919A610) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB919A610) {id: 0}>"}}`

### `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/FRR_CareerMode_Start`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/FRR_CareerMode_Start`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/CareerModeCoreCampaign`
- event actions: `5`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CreateCoOpReadySave_ArcAction`
  - `/Game/Campaign/NewsReel/NewsFeed_ArcAction`
  - `/Game/DLC1/CareerMode/StartConditions/Arcs/SetCompanyUnfounded`
  - `/Game/DLC1/CareerMode/Warzones/Rasalhauge_Clusters/PlaceRasalhague_ArcAction_1_3`
  - `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/FRR_CareerMode_Start`

### `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/Lock_Operations_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/CareerModeCoreCampaign`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB13224F30) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB13224F30) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/OfferCantinaAsperational_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/CareerModeCoreCampaign`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1807D960) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1807D960) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/FactionStarts/AddDefaultCodexEntries_Arc`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/CareerModeCoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/Campaign/CampaignArcActions/StateChangeActions/AddDefaultCodexEntries_ArcAction`

### `/Game/Campaign/CampaignArcs/GameOver/Overdraft_Arc`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/CareerModeCoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `2`
  - `/Game/Campaign/CampaignArcs/GameOver/OverdraftTimelineEvent_ArcAction`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`

### `/Game/Campaign/CampaignArcs/HidingSystems/HidingSystemsArc`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/CareerModeCoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `10`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A3_Arc/Travel_A3M1`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A3_Arc/Travel_A3M2`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A3_Arc/Travel_A3M3`
  - `/Game/Campaign/CampaignArcs/HidingSystems/A3M1_HideSystemArc`
  - `/Game/Campaign/CampaignArcs/HidingSystems/A3M2_HideSystemArc`
  - `/Game/Campaign/CampaignArcs/HidingSystems/A3MFinal_HideSystemArc`
  - `/Game/Campaign/CampaignArcs/HidingSystems/Q10_HideSystemArc`
  - `/Game/Campaign/CampaignArcs/HidingSystems/Q9_HideSystemArc`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_06/RaidOnComstar/SC06_Q9_Prompt`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_07/HitAndRun/SC07_Q10_Prompt`

### `/Game/Campaign/CampaignArcs/Razer_Exclusive/Razer_WolverineArc`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/CareerModeCoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `5`
  - `/Game/Campaign/CampaignArcs/Razer_Exclusive/CompleteRazerWolverineUnlocked_ArcAction`
  - `/Game/Campaign/CampaignArcs/Razer_Exclusive/RazerWolverineUnlocked_Transmission`
  - `/Game/Campaign/CampaignArcs/Razer_Exclusive/RazerWolverine_GiveReward_ArcAction`
  - `/Game/Campaign/CampaignArcs/Razer_Exclusive/Razer_WolverineArc`
  - `/Game/DLC1/DLC_1`

### `/Game/DLC1/CareerMode/CantinaArc`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/CareerModeCoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `6`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/CompleteCantinaUnlocked_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/Lock_Cantinas_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/Lock_Cantinas_Fallback_ArcAction`
  - `/Game/Careers/CantinaAsperational_Transmission`
  - `/Game/Careers/CantinaUnlocked_Transmission`
  - `/Game/DLC1/DLC_1`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/CareerModeCoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `32`
  - `/Game/DLC1/CareerMode/Clusters/S_10_12/CareerCluster_6`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/CompleteDragon4_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_HM4_GeneratedMission_1_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_HM4_GeneratedMission_2_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_HM4_GeneratedMission_3_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC_DRGN_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC_DRGN_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC_DRGN_Prompt3`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC_DRGN_Prompt4`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DRG_Mission_1/DRG1_Complete_AuthoredScenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DRG_Mission_1/DRG1_Place_Authored_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DRG_Mission_1/DRG1_Reset_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DRG_Mission_2/DRG2_Complete_AuthoredScenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DRG_Mission_2/DRG2_Place_Authored_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DRG_Mission_2/DRG2_Reset_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DRG_Mission_3/DRG3_Complete_AuthoredScenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DRG_Mission_3/DRG3_Place_Authored_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DRG_Mission_3/DRG3_Reset_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/OfferDragon1_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/OfferDragon2_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/OfferDragon3_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/OfferDragon4_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/Place_Authored_Dragon`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/Reset_Scenario_DRG`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/ShowDragonSideQuest_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/Unlock_DLC1_DRG_01_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/Unlock_DLC1_DRG_02_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/Unlock_DLC1_DRG_03_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/Unlock_DLC1_DRG_04_InstantAction_ArcAction`
  - `/Game/DLC1/DLC_1`
  - `/Game/DLC1/Levels/AuthoredMissions/D1M_Chase/D1M_Chase_Scenario`

### `/Game/DLC1/CareerMode/Sidequests/MS_Exclusive/DLC1_GoblinArc`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/CareerModeCoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `5`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasMSMechEntitlement`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoGoblin`
  - `/Game/DLC1/CareerMode/Sidequests/MS_Exclusive/CompleteGoblinUnlocked_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/MS_Exclusive/GoblinUnlocked_Transmission`
  - `/Game/DLC1/DLC_1`

### `/Game/DLC2/CampaignData/DLC2_CoreCampaign`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/CareerModeCoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `6`
  - `/Game/DLC2/CampaignData/DLC2_Act1`
  - `/Game/DLC2/CampaignData/DLC2_Act2`
  - `/Game/DLC2/CampaignData/DLC2_Act3`
  - `/Game/DLC2/CampaignData/DLC2_Prologue`
  - `/Game/DLC2/CampaignData/PlanetClusterData/DLC2_SetupPlanetaryWarzones`
  - `/Game/DLC2/Sidequests/DLC2_BattleQuests`

### `/Game/DLC4/CampaignData/DLC4_CoreCampaign`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/CareerModeCoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `6`
  - `/Game/DLC4/CampaignData/DLC4_Pt2_Kirchbach`
  - `/Game/DLC4/CampaignData/DLC4_Pt3_Rasalhague`
  - `/Game/DLC4/CampaignData/DLC4_Pt4_Predilitz`
  - `/Game/DLC4/CampaignData/DLC4_Pt5_Gunzberg`
  - `/Game/DLC4/CampaignData/DLC4_Pt6_Radstadt`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/DLC4_BountyHunterTransmissions`

### `/Game/DLC5/CampaignData/DLC5_CoreCampaign`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/CareerModeCoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `5`
  - `/Game/DLC5/CampaignData/DLC5_Pt0_Dieron`
  - `/Game/DLC5/CampaignData/DLC5_Pt1_Vega`
  - `/Game/DLC5/CampaignData/DLC5_Pt2_Auldhouse`
  - `/Game/DLC5/CampaignData/DLC5_Pt3_Arcturus`
  - `/Game/DLC5/CampaignData/DLC5_Pt4_TrollocPrime`

### `/Game/DLC6/CampaignData/DLC6_CoreCampaign`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/CareerModeCoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `4`
  - `/Game/DLC6/CampaignData/DLC6_Pt0_Galatea`
  - `/Game/DLC6/CampaignData/DLC6_Pt1_Hardcore`
  - `/Game/DLC6/CampaignData/DLC6_Pt2_Solaris`
  - `/Game/DLC6/CampaignData/PlanetClusterData/DLC6_SetupPlanetaryWarzones`

### `/Game/Campaign/CampaignArcs/Regions/MercStars/Place_MercStars_Arc`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/Campaign/CampaignArcs/Regions/MercStars/Place_Outreach_Arc`
- event actions: `2`
  - `/Game/Campaign/CampaignArcs/Regions/MercStars/Place_HerotitusZone`
  - `/Game/Campaign/CampaignArcs/Regions/MercStars/Place_WesterhandZone`

### `/Game/DLC1/CareerMode/Warzones/D_11_12/Common_D_11_12`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/Career_ACunningDecoy/D10_ACunningDecoy`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/D_11_12/Place_D_11_12`

### `/Game/DLC1/CareerMode/Warzones/D_12_13/Common_D_12_13`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `5`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/AnIntriguingOffer/D8_IntriguingOffer`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/BackChannelDeal/D9_Backchannel`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/DefenseSupportDavion/D7_DefenseDavion`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/InvasionSupportKurita/D6_InvasionKurita`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/DLC1_VTR`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/D_12_13/Place_D_12_13`

### `/Game/DLC1/CareerMode/Warzones/D_15/Common_D_15`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/D_15/Place_D_15`

### `/Game/DLC1/CareerMode/Warzones/D_1_2/Common_D_1_2`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/Career_ArmedRobery/D1_ArmedRobbery`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/D_1_2/Place_D_1_2`

### `/Game/DLC1/CareerMode/Warzones/D_2_3/Common_D_2_3`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/D_2_3/Place_D_2_3`

### `/Game/DLC1/CareerMode/Warzones/D_2_4/Common_D_2_4`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/D_2_4/Place_D_2_4`

### `/Game/DLC1/CareerMode/Warzones/D_3_5/Common_D_3_5`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/D_3_5/Place_D_3_5`

### `/Game/DLC1/CareerMode/Warzones/D_3_6/Common_D_3_6`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `2`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D2/Career_PickingUpThePieces/D2_PickingUpThePieces`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D2/Career_PickingUpTheScraps/D3_PickingUpScraps`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/D_3_6/Place_D_3_6`

### `/Game/DLC1/CareerMode/Warzones/D_4_6/Common_D_4_6`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/D_4_6/Place_D_4_6`

### `/Game/DLC1/CareerMode/Warzones/D_5_7/Common_D_5_7`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/D_5_7/Place_D_5_7`

### `/Game/DLC1/CareerMode/Warzones/D_5_8/Common_D_5_8`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/D_5_8/Place_D_5_8`

### `/Game/DLC1/CareerMode/Warzones/D_6_7/Common_D_6_7`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/D_6_7/Place_D_6_7`

### `/Game/DLC1/CareerMode/Warzones/D_6_8/Common_D_6_8`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/D_6_8/Place_D_6_8`

### `/Game/DLC1/CareerMode/Warzones/D_7_10/Common_D_7_10`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `2`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D4/FrontlineSupportDavion/D4_FrontlineDavion`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D4/FrontlineSupportKurita/D5_FrontlineKurita`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/D_7_10/Place_D_7_10`

### `/Game/DLC1/CareerMode/Warzones/K_12_13/Common_K_12_13`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `2`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K5/PeasantUprising/K6_PeasantUprising`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K5/TheChairmen/K5_Chairmen`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/K_12_13/Place_K_12_13`

### `/Game/DLC1/CareerMode/Warzones/K_13_14/Common_K_13_14`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/K_13_14/Place_K_13_14`

### `/Game/DLC1/CareerMode/Warzones/K_1_2/Common_K_1_2`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_EchoesOfThePast/K3_EchoesOfThePast`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/K_1_2/Place_K_1_2`

### `/Game/DLC1/CareerMode/Warzones/K_2_3/Common_K_2_3`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_CharityCase/K2_CharityCase`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/K_2_3/Place_K_2_3`

### `/Game/DLC1/CareerMode/Warzones/K_3_4/Common_K_3_4`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/K_3_4/Place_K_3_4`

### `/Game/DLC1/CareerMode/Warzones/K_3_5/Common_K_3_5`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/K_3_5/Place_K_3_5`

### `/Game/DLC1/CareerMode/Warzones/K_3_5_1/Common_K_3_5_1`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_05/ComstarBullies/Child_SC05_Q8`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/K_3_5_1/Place_K_3_5_1`

### `/Game/DLC1/CareerMode/Warzones/K_4_5/Common_K_4_5`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/K_4_5/Place_K_4_5`

### `/Game/DLC1/CareerMode/Warzones/K_5_6/Common_K_5_6`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_PirateHunt/K1_PirateHunt`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/K_5_6/Place_K_5_6`

### `/Game/DLC1/CareerMode/Warzones/K_6_7/Common_K_6_7`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/K_6_7/Place_K_6_7`

### `/Game/DLC1/CareerMode/Warzones/K_6_8/Common_K_6_8`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/K_6_8/Place_K_6_8`

### `/Game/DLC1/CareerMode/Warzones/K_7_9/Common_K_7_9`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_RiseOfTheBlackDragon/K4_RiseOfBlackDragon`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/K_7_9/Place_K_7_9`

### `/Game/DLC1/CareerMode/Warzones/K_8_10/Common_K_8_10`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/K_8_10/Place_K_8_10`

### `/Game/DLC1/CareerMode/Warzones/L_11_12/Common_L_11_12`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/L_11_12/Place_L_11_12`

### `/Game/DLC1/CareerMode/Warzones/L_12_13/Common_L_12_13`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/GreatHouses/Child_SC01_Arc`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/L_12_13/Place_L_12_13`

### `/Game/DLC1/CareerMode/Warzones/L_13_14/Common_L_13_14`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_TheTraitor/L7_TheTraitor`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/L_13_14/Place_L_13_14`

### `/Game/DLC1/CareerMode/Warzones/L_1_2/Common_L_1_2`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_ErrantSignal/L_1_ErrantSignal`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/L_1_2/Place_L_1_2_ArcAction`

### `/Game/DLC1/CareerMode/Warzones/L_2_5/Common_L_2_5`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `2`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/DLC1_ON1`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_CerebusHounds/L_2_CerebusHounds`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/L_2_5/Place_L_2_5`

### `/Game/DLC1/CareerMode/Warzones/L_3_6/Common_L_3_6`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `2`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_FrontlineDefenseDavion/L3_InvasionDefenseDavion`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_FrontlineInvasionLiao/L4_FrontlineInvasionLiao`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/L_3_6/Place_L_3_6`

### `/Game/DLC1/CareerMode/Warzones/L_5_8/Common_L_5_8`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_UprisingQuelled/L5_UprisingQuelled`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/L_5_8/Place_L_5_8`

### `/Game/DLC1/CareerMode/Warzones/L_7_10/Common_L_7_10`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `2`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/DLC1_RFL`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_IndustrialEspionage/L6_IndustrialEspionage`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/L_7_10/Place_L_7_10`

### `/Game/DLC1/CareerMode/Warzones/M_11_12/Common_M_11_12`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ForcefulNegotiations/M7_ForcefulNegotiations`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/M_11_12/Place_M_11_12`

### `/Game/DLC1/CareerMode/Warzones/M_12_13/Common_M_12_13`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_FalseFlag/M11_FalseFlag`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/M_12_13/Place_M_12_13`

### `/Game/DLC1/CareerMode/Warzones/M_12_13_1/Common_M_12_13_1`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_DeathToEnhanced/M10_DeathToEnhanced`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/M_12_13_1/Place_M_12_13_1`

### `/Game/DLC1/CareerMode/Warzones/M_13_14/Common_M_13_14`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/DLC1_Archer`
- event actions: `2`
  - `/Game/DLC1/CareerMode/Warzones/M_13_14/Place_M_13_14`
  - `/Game/DLC1/DLC_1`

### `/Game/DLC1/CareerMode/Warzones/M_15/Common_M_15`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/M_15/Place_M_15`

### `/Game/DLC1/CareerMode/Warzones/M_1_2/Common_M_1_2`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ChasingGhosts/M1_ChasingGhosts`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/M_1_2/Place_M_1_2`

### `/Game/DLC1/CareerMode/Warzones/M_2_5/Common_M_2_5`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_NoPilotLeftBehind/M2_NoPilotLeftBehind`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/M_2_5/Place_M_2_5`

### `/Game/DLC1/CareerMode/Warzones/M_3_6/Common_M_3_6`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `2`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_Destabalization/Career_CorporateInterests/M4_CorporateInterests`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_Destabalization/M3_Destabalization`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/M_3_6/Place_M_3_6`

### `/Game/DLC1/CareerMode/Warzones/M_5_8/Common_M_5_8`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_EnemyOfMyEnemy/M5_EnemyOfMyEnemy`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/M_5_8/Place_M_5_8`

### `/Game/DLC1/CareerMode/Warzones/M_7_10/Common_M_7_10`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_DefendingtheHonor/M6_DefendingTheHonor`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/M_7_10/Place_M_7_10`

### `/Game/DLC1/CareerMode/Warzones/M_9_11/Common_M_9_11`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ShippingDisruption/M8_ShippingDistruption`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/M_9_11/Place_M_9_11`

### `/Game/DLC1/CareerMode/Warzones/S_10_12/Common_S_10_12`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K10/DLC1_ThePowderKeg`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/S_10_12/Place_S_10_12`

### `/Game/DLC1/CareerMode/Warzones/S_12_13/Common_S_12_13`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/Career_ShadowCoup/S5_ShadowCoup`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/S_12_13/Place_S_12_13`

### `/Game/DLC1/CareerMode/Warzones/S_13_14/Common_S_13_14`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/DLC1_KGC`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/S_13_14/Place_S_13_14`

### `/Game/DLC1/CareerMode/Warzones/S_1_2/Common_S_1_2`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/S_1_2/Place_S_1_2`

### `/Game/DLC1/CareerMode/Warzones/S_2_4/Common_S_2_4`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/S_2_4/Place_S_2_4`

### `/Game/DLC1/CareerMode/Warzones/S_2_5/Common_S_2_5`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S5/DLC1_CompetitiveEdge`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/S_2_5/Place_S_2_5`

### `/Game/DLC1/CareerMode/Warzones/S_3_5/Common_S_3_5`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S3/DLC1_ReturnOfTheRangers`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/S_3_5/Place_S_3_5`

### `/Game/DLC1/CareerMode/Warzones/S_4_6/Common_S_4_6`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S4/DLC1_BowieElectronics`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/S_4_6/Place_S_4_6`

### `/Game/DLC1/CareerMode/Warzones/S_5_8/Common_S_5_8`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/S_5_8/Place_S_5_8`

### `/Game/DLC1/CareerMode/Warzones/S_5_8_1/Common_S_5_8_1`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/S_5_8_1/Place_S_5_8_1`

### `/Game/DLC1/CareerMode/Warzones/S_6_7/Common_S_6_7`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/DLC1_COR`
- event actions: `2`
  - `/Game/DLC1/CareerMode/Warzones/S_6_7/Place_S_6_7`
  - `/Game/DLC1/DLC_1`

### `/Game/DLC1/CareerMode/Warzones/S_6_9/Common_S_6_9`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/Career_DragonInSheepsClothing/S6_DragonInSheepsClothing`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/S_6_9/Place_S_6_9`

### `/Game/DLC1/CareerMode/Warzones/S_9_11/Common_S_9_11`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `4`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/CostOfFreedom/S3_CostOfFreedom`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/CostOfLoyalty/S4_CostOfLoyalty`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranIndependence/S1_LyranIndependence`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranRebellion/S2_LyranRebellion`
- event actions: `1`
  - `/Game/DLC1/CareerMode/Warzones/S_9_11/Place_S_9_11`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_10_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_10/SafeZone_10_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_10/SafeZone_10_ClusterAsset.SafeZone_10_ClusterAsset' (0x000001BA9C3339C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_10_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_10/SafeZone_10_ClusterAsset.SafeZone_10_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_10/SafeZone_10_ClusterAsset.SafeZone_10_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_10/SafeZone_10_ClusterAsset.SafeZone_10_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_10/SafeZone_10_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_10/SafeZone_10_ClusterAsset.SafeZone_10_ClusterAsset' (0x000001BA9C3339C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB90997B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_10_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB90997B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_10_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB9099710) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB9099710) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_11_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_11/SafeZone_11_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_11/SafeZone_11_ClusterAsset.SafeZone_11_ClusterAsset' (0x000001BA9C333C40) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_11_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_11/SafeZone_11_ClusterAsset.SafeZone_11_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_11/SafeZone_11_ClusterAsset.SafeZone_11_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_11/SafeZone_11_ClusterAsset.SafeZone_11_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_11/SafeZone_11_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_11/SafeZone_11_ClusterAsset.SafeZone_11_ClusterAsset' (0x000001BA9C333C40) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB9099CB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_11_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB9099CB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_11_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB9099C10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB9099C10) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_12_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_12/SafeZone_12_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_12/SafeZone_12_ClusterAsset.SafeZone_12_ClusterAsset' (0x000001BA9C333EC0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_12_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_12/SafeZone_12_ClusterAsset.SafeZone_12_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_12/SafeZone_12_ClusterAsset.SafeZone_12_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_12/SafeZone_12_ClusterAsset.SafeZone_12_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_12/SafeZone_12_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_12/SafeZone_12_ClusterAsset.SafeZone_12_ClusterAsset' (0x000001BA9C333EC0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB90992B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_12_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB90992B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_12_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB9099210) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB9099210) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_13_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_13/SafeZone_13_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_13/SafeZone_13_ClusterAsset.SafeZone_13_ClusterAsset' (0x000001BA9C332AC0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_13_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_13/SafeZone_13_ClusterAsset.SafeZone_13_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_13/SafeZone_13_ClusterAsset.SafeZone_13_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_13/SafeZone_13_ClusterAsset.SafeZone_13_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_13/SafeZone_13_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_13/SafeZone_13_ClusterAsset.SafeZone_13_ClusterAsset' (0x000001BA9C332AC0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB909ABB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_13_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB909ABB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_13_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB909AB10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB909AB10) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_14_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_14/SafeZone_14_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_14/SafeZone_14_ClusterAsset.SafeZone_14_ClusterAsset' (0x000001BA9C332E80) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_14_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_14/SafeZone_14_ClusterAsset.SafeZone_14_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_14/SafeZone_14_ClusterAsset.SafeZone_14_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_14/SafeZone_14_ClusterAsset.SafeZone_14_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_14/SafeZone_14_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_14/SafeZone_14_ClusterAsset.SafeZone_14_ClusterAsset' (0x000001BA9C332E80) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB909BBF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_14_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB909BBF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_14_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB909BB50) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB909BB50) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_15_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_15/SafeZone_15_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_15/SafeZone_15_ClusterAsset.SafeZone_15_ClusterAsset' (0x000001BA9C332C00) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_15_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_15/SafeZone_15_ClusterAsset.SafeZone_15_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_15/SafeZone_15_ClusterAsset.SafeZone_15_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_15/SafeZone_15_ClusterAsset.SafeZone_15_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_15/SafeZone_15_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_15/SafeZone_15_ClusterAsset.SafeZone_15_ClusterAsset' (0x000001BA9C332C00) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB909A7F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_15_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB909A7F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_15_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB909A750) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB909A750) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_16_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_16/SafeZone_16_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_16/SafeZone_16_ClusterAsset.SafeZone_16_ClusterAsset' (0x000001BA9C332D40) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_16_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_16/SafeZone_16_ClusterAsset.SafeZone_16_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_16/SafeZone_16_ClusterAsset.SafeZone_16_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_16/SafeZone_16_ClusterAsset.SafeZone_16_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_16/SafeZone_16_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_16/SafeZone_16_ClusterAsset.SafeZone_16_ClusterAsset' (0x000001BA9C332D40) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB9099530) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_16_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB9099530) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_16_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB9099490) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB9099490) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_17_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_17/SafeZone_17_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_17/SafeZone_17_ClusterAsset.SafeZone_17_ClusterAsset' (0x000001BA19C3C180) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_17_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_17/SafeZone_17_ClusterAsset.SafeZone_17_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_17/SafeZone_17_ClusterAsset.SafeZone_17_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_17/SafeZone_17_ClusterAsset.SafeZone_17_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_17/SafeZone_17_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_17/SafeZone_17_ClusterAsset.SafeZone_17_ClusterAsset' (0x000001BA19C3C180) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF67F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_17_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF67F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_17_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF6750) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF6750) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_18_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_18/SafeZone_18_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_18/SafeZone_18_ClusterAsset.SafeZone_18_ClusterAsset' (0x000001BA19C3C400) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_18_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_18/SafeZone_18_ClusterAsset.SafeZone_18_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_18/SafeZone_18_ClusterAsset.SafeZone_18_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_18/SafeZone_18_ClusterAsset.SafeZone_18_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_18/SafeZone_18_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_18/SafeZone_18_ClusterAsset.SafeZone_18_ClusterAsset' (0x000001BA19C3C400) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF70B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_18_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF70B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_18_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF7010) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF7010) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_19_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_19/SafeZone_19_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_19/SafeZone_19_ClusterAsset.SafeZone_19_ClusterAsset' (0x000001BA19C3C680) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_19_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_19/SafeZone_19_ClusterAsset.SafeZone_19_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_19/SafeZone_19_ClusterAsset.SafeZone_19_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_19/SafeZone_19_ClusterAsset.SafeZone_19_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_19/SafeZone_19_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_19/SafeZone_19_ClusterAsset.SafeZone_19_ClusterAsset' (0x000001BA19C3C680) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF6570) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_19_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF6570) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_19_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF64D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF64D0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_1_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_1/SafeZone_1_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_1/SafeZone_1_ClusterAsset.SafeZone_1_ClusterAsset' (0x000001BA9C333740) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_1_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_1/SafeZone_1_ClusterAsset.SafeZone_1_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_1/SafeZone_1_ClusterAsset.SafeZone_1_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_1/SafeZone_1_ClusterAsset.SafeZone_1_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_1/SafeZone_1_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_1/SafeZone_1_ClusterAsset.SafeZone_1_ClusterAsset' (0x000001BA9C333740) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB94CB970) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_1_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB94CB970) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_1_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB94CB8D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB94CB8D0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_20_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_20/SafeZone_20_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_20/SafeZone_20_ClusterAsset.SafeZone_20_ClusterAsset' (0x000001BA19C3CB80) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_20_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_20/SafeZone_20_ClusterAsset.SafeZone_20_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_20/SafeZone_20_ClusterAsset.SafeZone_20_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_20/SafeZone_20_ClusterAsset.SafeZone_20_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_20/SafeZone_20_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_20/SafeZone_20_ClusterAsset.SafeZone_20_ClusterAsset' (0x000001BA19C3CB80) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF5CB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_20_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF5CB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_20_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF5C10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF5C10) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_21_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_21/SafeZone_21_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_21/SafeZone_21_ClusterAsset.SafeZone_21_ClusterAsset' (0x000001BA19C3CE00) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_21_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_21/SafeZone_21_ClusterAsset.SafeZone_21_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_21/SafeZone_21_ClusterAsset.SafeZone_21_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_21/SafeZone_21_ClusterAsset.SafeZone_21_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_21/SafeZone_21_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_21/SafeZone_21_ClusterAsset.SafeZone_21_ClusterAsset' (0x000001BA19C3CE00) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF5530) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_21_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF5530) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_21_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF5490) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF5490) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_22_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_22/SafeZone_22_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_22/SafeZone_22_ClusterAsset.SafeZone_22_ClusterAsset' (0x000001BA19C3CF40) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_22_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_22/SafeZone_22_ClusterAsset.SafeZone_22_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_22/SafeZone_22_ClusterAsset.SafeZone_22_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_22/SafeZone_22_ClusterAsset.SafeZone_22_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_22/SafeZone_22_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_22/SafeZone_22_ClusterAsset.SafeZone_22_ClusterAsset' (0x000001BA19C3CF40) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF4C70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_22_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF4C70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_22_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF4BD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF4BD0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_23_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_23/SafeZone_23_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_23/SafeZone_23_ClusterAsset.SafeZone_23_ClusterAsset' (0x000001BA19C3D1C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_23_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_23/SafeZone_23_ClusterAsset.SafeZone_23_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_23/SafeZone_23_ClusterAsset.SafeZone_23_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_23/SafeZone_23_ClusterAsset.SafeZone_23_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_23/SafeZone_23_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_23/SafeZone_23_ClusterAsset.SafeZone_23_ClusterAsset' (0x000001BA19C3D1C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF6930) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_23_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF6930) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_23_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF6890) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF6890) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_24_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_24/SafeZone_24_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_24/SafeZone_24_ClusterAsset.SafeZone_24_ClusterAsset' (0x000001BA19C3D440) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_24_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_24/SafeZone_24_ClusterAsset.SafeZone_24_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_24/SafeZone_24_ClusterAsset.SafeZone_24_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_24/SafeZone_24_ClusterAsset.SafeZone_24_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_24/SafeZone_24_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_24/SafeZone_24_ClusterAsset.SafeZone_24_ClusterAsset' (0x000001BA19C3D440) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF7970) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_24_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF7970) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_24_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF78D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF78D0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_25_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_25/SafeZone_25_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_25/SafeZone_25_ClusterAsset.SafeZone_25_ClusterAsset' (0x000001BA19C3D6C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_25_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_25/SafeZone_25_ClusterAsset.SafeZone_25_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_25/SafeZone_25_ClusterAsset.SafeZone_25_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_25/SafeZone_25_ClusterAsset.SafeZone_25_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_25/SafeZone_25_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_25/SafeZone_25_ClusterAsset.SafeZone_25_ClusterAsset' (0x000001BA19C3D6C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF62F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_25_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF62F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_25_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF6250) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF6250) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_26_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_26/SafeZone_26_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_26/SafeZone_26_ClusterAsset.SafeZone_26_ClusterAsset' (0x000001BA19C3D940) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_26_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_26/SafeZone_26_ClusterAsset.SafeZone_26_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_26/SafeZone_26_ClusterAsset.SafeZone_26_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_26/SafeZone_26_ClusterAsset.SafeZone_26_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_26/SafeZone_26_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_26/SafeZone_26_ClusterAsset.SafeZone_26_ClusterAsset' (0x000001BA19C3D940) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF6CF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_26_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF6CF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_26_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF6C50) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF6C50) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_27_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_27/SafeZone_27_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_27/SafeZone_27_ClusterAsset.SafeZone_27_ClusterAsset' (0x000001BA19C3DBC0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_27_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_27/SafeZone_27_ClusterAsset.SafeZone_27_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_27/SafeZone_27_ClusterAsset.SafeZone_27_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_27/SafeZone_27_ClusterAsset.SafeZone_27_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_27/SafeZone_27_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_27/SafeZone_27_ClusterAsset.SafeZone_27_ClusterAsset' (0x000001BA19C3DBC0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF53F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_27_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8FF53F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_27_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF5350) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8FF5350) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_28_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_28/SafeZone_28_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_28/SafeZone_28_ClusterAsset.SafeZone_28_ClusterAsset' (0x000001BA19C3DD00) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_28_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_28/SafeZone_28_ClusterAsset.SafeZone_28_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_28/SafeZone_28_ClusterAsset.SafeZone_28_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_28/SafeZone_28_ClusterAsset.SafeZone_28_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_28/SafeZone_28_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_28/SafeZone_28_ClusterAsset.SafeZone_28_ClusterAsset' (0x000001BA19C3DD00) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB904ECF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_28_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB904ECF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_28_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB904EC50) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB904EC50) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_29_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_29/SafeZone_29_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_29/SafeZone_29_ClusterAsset.SafeZone_29_ClusterAsset' (0x000001BA19C3DE40) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_29_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_29/SafeZone_29_ClusterAsset.SafeZone_29_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_29/SafeZone_29_ClusterAsset.SafeZone_29_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_29/SafeZone_29_ClusterAsset.SafeZone_29_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_29/SafeZone_29_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_29/SafeZone_29_ClusterAsset.SafeZone_29_ClusterAsset' (0x000001BA19C3DE40) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB904E930) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_29_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB904E930) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_29_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB904E890) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB904E890) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_2_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_2/SafeZone_2_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_2/SafeZone_2_ClusterAsset.SafeZone_2_ClusterAsset' (0x000001BA19C3C900) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_2_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_2/SafeZone_2_ClusterAsset.SafeZone_2_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_2/SafeZone_2_ClusterAsset.SafeZone_2_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_2/SafeZone_2_ClusterAsset.SafeZone_2_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_2/SafeZone_2_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_2/SafeZone_2_ClusterAsset.SafeZone_2_ClusterAsset' (0x000001BA19C3C900) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB94CBE70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_2_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB94CBE70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_2_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB94CBDD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB94CBDD0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_30_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_30/SafeZone_30_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_30/SafeZone_30_ClusterAsset.SafeZone_30_ClusterAsset' (0x000001BA19C3E480) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_30_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_30/SafeZone_30_ClusterAsset.SafeZone_30_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_30/SafeZone_30_ClusterAsset.SafeZone_30_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_30/SafeZone_30_ClusterAsset.SafeZone_30_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_30/SafeZone_30_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_30/SafeZone_30_ClusterAsset.SafeZone_30_ClusterAsset' (0x000001BA19C3E480) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB904F970) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_30_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB904F970) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_30_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB904F8D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB904F8D0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_31_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_31/SafeZone_31_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_31/SafeZone_31_ClusterAsset.SafeZone_31_ClusterAsset' (0x000001BA19C3E700) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_31_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_31/SafeZone_31_ClusterAsset.SafeZone_31_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_31/SafeZone_31_ClusterAsset.SafeZone_31_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_31/SafeZone_31_ClusterAsset.SafeZone_31_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_31/SafeZone_31_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_31/SafeZone_31_ClusterAsset.SafeZone_31_ClusterAsset' (0x000001BA19C3E700) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB9177830) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_31_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB9177830) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_31_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB9177790) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB9177790) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_32_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_32/SafeZone_32_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_32/SafeZone_32_ClusterAsset.SafeZone_32_ClusterAsset' (0x000001BA19C3E840) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_32_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_32/SafeZone_32_ClusterAsset.SafeZone_32_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_32/SafeZone_32_ClusterAsset.SafeZone_32_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_32/SafeZone_32_ClusterAsset.SafeZone_32_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_32/SafeZone_32_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_32/SafeZone_32_ClusterAsset.SafeZone_32_ClusterAsset' (0x000001BA19C3E840) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB9174DB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_32_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB9174DB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_32_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB9174D10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB9174D10) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_33_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_33/SafeZone_33_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_33/SafeZone_33_ClusterAsset.SafeZone_33_ClusterAsset' (0x000001BA19C3EAC0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_33_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_33/SafeZone_33_ClusterAsset.SafeZone_33_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_33/SafeZone_33_ClusterAsset.SafeZone_33_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_33/SafeZone_33_ClusterAsset.SafeZone_33_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_33/SafeZone_33_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_33/SafeZone_33_ClusterAsset.SafeZone_33_ClusterAsset' (0x000001BA19C3EAC0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB9176E30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_33_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB9176E30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_33_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB9176D90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB9176D90) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_34_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_34/SafeZone_34_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_34/SafeZone_34_ClusterAsset.SafeZone_34_ClusterAsset' (0x000001BA19C3EC00) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_34_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_34/SafeZone_34_ClusterAsset.SafeZone_34_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_34/SafeZone_34_ClusterAsset.SafeZone_34_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_34/SafeZone_34_ClusterAsset.SafeZone_34_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_34/SafeZone_34_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_34/SafeZone_34_ClusterAsset.SafeZone_34_ClusterAsset' (0x000001BA19C3EC00) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB9175DF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_34_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB9175DF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_34_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB9175D50) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB9175D50) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_35_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_35/SafeZone_35_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_35/SafeZone_35_ClusterAsset.SafeZone_35_ClusterAsset' (0x000001BA19C3ED40) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_35_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_35/SafeZone_35_ClusterAsset.SafeZone_35_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_35/SafeZone_35_ClusterAsset.SafeZone_35_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_35/SafeZone_35_ClusterAsset.SafeZone_35_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_35/SafeZone_35_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_35/SafeZone_35_ClusterAsset.SafeZone_35_ClusterAsset' (0x000001BA19C3ED40) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB9176570) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_35_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB9176570) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_35_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB91764D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB91764D0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_3_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_3/SafeZone_3_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_3/SafeZone_3_ClusterAsset.SafeZone_3_ClusterAsset' (0x000001BA19C3E200) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_3_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_3/SafeZone_3_ClusterAsset.SafeZone_3_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_3/SafeZone_3_ClusterAsset.SafeZone_3_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_3/SafeZone_3_ClusterAsset.SafeZone_3_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_3/SafeZone_3_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_3/SafeZone_3_ClusterAsset.SafeZone_3_ClusterAsset' (0x000001BA19C3E200) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB94C8630) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_3_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB94C8630) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_3_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB94C8590) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB94C8590) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_4_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_4/SafeZone_4_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_4/SafeZone_4_ClusterAsset.SafeZone_4_ClusterAsset' (0x000001BA19C3EFC0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_4_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_4/SafeZone_4_ClusterAsset.SafeZone_4_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_4/SafeZone_4_ClusterAsset.SafeZone_4_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_4/SafeZone_4_ClusterAsset.SafeZone_4_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_4/SafeZone_4_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_4/SafeZone_4_ClusterAsset.SafeZone_4_ClusterAsset' (0x000001BA19C3EFC0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB94C8B30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_4_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB94C8B30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_4_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB94C8A90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB94C8A90) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_5_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_5/SafeZone_5_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_5/SafeZone_5_ClusterAsset.SafeZone_5_ClusterAsset' (0x000001BA19C3F100) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_5_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_5/SafeZone_5_ClusterAsset.SafeZone_5_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_5/SafeZone_5_ClusterAsset.SafeZone_5_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_5/SafeZone_5_ClusterAsset.SafeZone_5_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_5/SafeZone_5_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_5/SafeZone_5_ClusterAsset.SafeZone_5_ClusterAsset' (0x000001BA19C3F100) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB94C9030) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_5_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB94C9030) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_5_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB94C8F90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB94C8F90) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_6_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_6/SafeZone_6_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_6/SafeZone_6_ClusterAsset.SafeZone_6_ClusterAsset' (0x000001BA19C3F240) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_6_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_6/SafeZone_6_ClusterAsset.SafeZone_6_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_6/SafeZone_6_ClusterAsset.SafeZone_6_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_6/SafeZone_6_ClusterAsset.SafeZone_6_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_6/SafeZone_6_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_6/SafeZone_6_ClusterAsset.SafeZone_6_ClusterAsset' (0x000001BA19C3F240) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB94C93F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_6_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB94C93F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_6_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB94C9350) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB94C9350) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_7_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_7/SafeZone_7_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_7/SafeZone_7_ClusterAsset.SafeZone_7_ClusterAsset' (0x000001BA19C3F380) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_7_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_7/SafeZone_7_ClusterAsset.SafeZone_7_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_7/SafeZone_7_ClusterAsset.SafeZone_7_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_7/SafeZone_7_ClusterAsset.SafeZone_7_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_7/SafeZone_7_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_7/SafeZone_7_ClusterAsset.SafeZone_7_ClusterAsset' (0x000001BA19C3F380) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB94C9B70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_7_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB94C9B70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_7_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB94C9AD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB94C9AD0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_8_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_8/SafeZone_8_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_8/SafeZone_8_ClusterAsset.SafeZone_8_ClusterAsset' (0x000001BA19C3F600) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_8_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_8/SafeZone_8_ClusterAsset.SafeZone_8_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_8/SafeZone_8_ClusterAsset.SafeZone_8_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_8/SafeZone_8_ClusterAsset.SafeZone_8_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_8/SafeZone_8_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_8/SafeZone_8_ClusterAsset.SafeZone_8_ClusterAsset' (0x000001BA19C3F600) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB9098270) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_8_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB9098270) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_8_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB90981D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB90981D0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_9_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_9/SafeZone_9_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_9/SafeZone_9_ClusterAsset.SafeZone_9_ClusterAsset' (0x000001BA19C3F880) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SafeZone_9_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/SafeZone_9/SafeZone_9_ClusterAsset.SafeZone_9_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/SafeZone_9/SafeZone_9_ClusterAsset.SafeZone_9_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/SafeZone_9/SafeZone_9_ClusterAsset.SafeZone_9_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/SafeZone_9/SafeZone_9_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/SafeZone_9/SafeZone_9_ClusterAsset.SafeZone_9_ClusterAsset' (0x000001BA19C3F880) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB909AA70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_9_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB909AA70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SafeZone_9_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB909A9D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB909A9D0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/BorderChanges/3025_ThirdSuccession/3025_ThirdSuccession`
- depth/reason: `1` / `referenced by /Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3025_ThirdSuccession/StarMapBordersUpdate_3025_ArcAction`

### `/Game/Campaign/CampaignArcs/BorderChanges/3029_FormationOfTikinovAndStIves/3029_FormationOfTikinovAndStIves`
- depth/reason: `1` / `referenced by /Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3029_FormationOfTikinovAndStIves/StarMapBordersUpdate_3029_ArcAction`

### `/Game/Campaign/CampaignArcs/BorderChanges/3030_FourthSuccession/3030_FourthSuccession`
- depth/reason: `1` / `referenced by /Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3030_FourthSuccession/StarMapBordersUpdate_3030_ArcAction`

### `/Game/Campaign/CampaignArcs/BorderChanges/3031_TikinovJoinsFederatedSuns/3031_TikinovJoinsFederatedSuns`
- depth/reason: `1` / `referenced by /Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3031_TikinovJoinsFederatedSuns/StarMapBordersUpdate_3031_ArcAction`

### `/Game/Campaign/CampaignArcs/BorderChanges/3034_RassalhaugeRecognized/Borders_Year3034_RassalhaugeRecognized`
- depth/reason: `1` / `referenced by /Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3034_RassalhaugeRecognized/StarMapBordersUpdate_3034_ArcAction`

### `/Game/Campaign/CampaignArcs/BorderChanges/3039_WarOf3039/3039_WarOf3039`
- depth/reason: `1` / `referenced by /Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3039_WarOf3039/StarMapBordersUpdate_3039_ArcAction`

### `/Game/Campaign/CampaignArcs/BorderChanges/3041_FormationOfFederatedCommonwealth/3041_FormationOfFederatedCommonwealth`
- depth/reason: `1` / `referenced by /Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3041_FormationOfFederatedCommonwealth/StarMapBordersUpdate_3041_ArcAction`

### `/Game/Campaign/CampaignArcs/BorderChanges/3049_ClanInvasion/3049_ClanInvasion`
- depth/reason: `1` / `referenced by /Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `5`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3050_OperationRevival_Wave1/3050_ClanInvasion_Wave1`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3050_OperationRevival_Wave2/3050_ClanInvasion_Wave2`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3050_OperationRevival_Wave3/3050_ClanInvasion_Wave3`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3050_YearOfPeace_Wave4/3050_ClanInvasion_Wave4`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3051_EndOfOperationRevival_Wave5/3050_ClanInvasion_Wave5`
- event actions: `2`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3049_ClanInvasion/StarMapBordersUpdate_3049_ArcAction`
  - `/Game/DLC7/DLC_7`

### `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_CoreCampaign`
- class: `Blueprint` exists `True`

### `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_CoreCampaign`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1365C0F0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1365C0F0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/CampaignArcActions/TravelTo_D7M1`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_CoreCampaign`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAA84815D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAA84815D0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Hunting/ArcActions/D7M1_AutoAcceptMission`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_CoreCampaign`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB11000930) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB11000930) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Hunting/ArcActions/D7M1_AutoAcceptObjective`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_CoreCampaign`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB11000630) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB11000630) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Hunting/ArcActions/D7M1_Completed`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_CoreCampaign`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB184F9570) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB184F9570) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Hunting/ArcActions/D7M1_Offer`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_CoreCampaign`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB181FEC30) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB181FEC30) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Hunting/ArcActions/D7M1_Place_Mission`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_CoreCampaign`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BA735A90D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BA735A90D0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Hunting/ArcActions/Unlock_D7M1_InstantAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_CoreCampaign`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB184F8930) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB184F8930) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Hunting/D7M1_Prompt`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_CoreCampaign`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/Missions/D7_Hunting/D7_Hunting_Mission_Scenario`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_CoreCampaign`
- class: `MWScenarioSpecificationAsset` exists `True`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Periphery_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset.CGB_Periphery_ClusterAsset' (0x000001BA19C5FC40) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CGB_Periphery_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset.CGB_Periphery_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset.CGB_Periphery_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset.CGB_Periphery_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset.CGB_Periphery_ClusterAsset' (0x000001BA19C5FC40) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8B9F330) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8B9F330) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8B9F290) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8B9F290) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave1_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_ClusterAsset.CGB_Wave1_ClusterAsset' (0x000001BA19C5D300) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CGB_Wave1_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_ClusterAsset.CGB_Wave1_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_ClusterAsset.CGB_Wave1_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_ClusterAsset.CGB_Wave1_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_ClusterAsset.CGB_Wave1_ClusterAsset' (0x000001BA19C5D300) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB7C69170) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB7C69170) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB7C690D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB7C690D0) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave2_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_ClusterAsset.CGB_Wave2_ClusterAsset' (0x000001BA19CCC540) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CGB_Wave2_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_ClusterAsset.CGB_Wave2_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_ClusterAsset.CGB_Wave2_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_ClusterAsset.CGB_Wave2_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_ClusterAsset.CGB_Wave2_ClusterAsset' (0x000001BA19CCC540) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8BFF0B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8BFF0B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8BFF010) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8BFF010) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave3_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_ClusterAsset.CGB_Wave3_ClusterAsset' (0x000001BA19CCCA40) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CGB_Wave3_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_ClusterAsset.CGB_Wave3_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_ClusterAsset.CGB_Wave3_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_ClusterAsset.CGB_Wave3_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_ClusterAsset.CGB_Wave3_ClusterAsset' (0x000001BA19CCCA40) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB930DB70) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB930DB70) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB930DAD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB930DAD0) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave4_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_ClusterAsset.CGB_Wave4_ClusterAsset' (0x000001BA19CCD6C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CGB_Wave4_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_ClusterAsset.CGB_Wave4_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_ClusterAsset.CGB_Wave4_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_ClusterAsset.CGB_Wave4_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_ClusterAsset.CGB_Wave4_ClusterAsset' (0x000001BA19CCD6C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB930FBF0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB930FBF0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB930FB50) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB930FB50) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave5_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_ClusterAsset.CGB_Wave5_ClusterAsset' (0x000001BA19CCE200) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CGB_Wave5_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_ClusterAsset.CGB_Wave5_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_ClusterAsset.CGB_Wave5_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_ClusterAsset.CGB_Wave5_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_ClusterAsset.CGB_Wave5_ClusterAsset' (0x000001BA19CCE200) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB96E2430) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB96E2430) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB96E2390) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB96E2390) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Periphery_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_ClusterAsset.CJF_Periphery_ClusterAsset' (0x000001BA19C5FD80) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CJF_Periphery_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_ClusterAsset.CJF_Periphery_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_ClusterAsset.CJF_Periphery_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_ClusterAsset.CJF_Periphery_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_ClusterAsset.CJF_Periphery_ClusterAsset' (0x000001BA19C5FD80) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8B9E1B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8B9E1B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8B9E110) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8B9E110) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave1_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_ClusterAsset.CJF_Wave1_ClusterAsset' (0x000001BA19C5D580) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CJF_Wave1_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_ClusterAsset.CJF_Wave1_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_ClusterAsset.CJF_Wave1_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_ClusterAsset.CJF_Wave1_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_ClusterAsset.CJF_Wave1_ClusterAsset' (0x000001BA19C5D580) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8BFF330) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8BFF330) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8BFF290) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8BFF290) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave2_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_ClusterAsset.CJF_Wave2_ClusterAsset' (0x000001BA19CCC680) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CJF_Wave2_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_ClusterAsset.CJF_Wave2_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_ClusterAsset.CJF_Wave2_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_ClusterAsset.CJF_Wave2_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_ClusterAsset.CJF_Wave2_ClusterAsset' (0x000001BA19CCC680) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8BFF970) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8BFF970) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8BFF8D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8BFF8D0) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave3_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_ClusterAsset.CJF_Wave3_ClusterAsset' (0x000001BA19CCCB80) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CJF_Wave3_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_ClusterAsset.CJF_Wave3_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_ClusterAsset.CJF_Wave3_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_ClusterAsset.CJF_Wave3_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_ClusterAsset.CJF_Wave3_ClusterAsset' (0x000001BA19CCCB80) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB930D7B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB930D7B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB930D710) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB930D710) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave4_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_ClusterAsset.CJF_Wave4_ClusterAsset' (0x000001BA19CCD940) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CJF_Wave4_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_ClusterAsset.CJF_Wave4_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_ClusterAsset.CJF_Wave4_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_ClusterAsset.CJF_Wave4_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_ClusterAsset.CJF_Wave4_ClusterAsset' (0x000001BA19CCD940) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB930EE30) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB930EE30) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB930ED90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB930ED90) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave5_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_ClusterAsset.CJF_Wave5_ClusterAsset' (0x000001BA19CCE480) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CJF_Wave5_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_ClusterAsset.CJF_Wave5_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_ClusterAsset.CJF_Wave5_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_ClusterAsset.CJF_Wave5_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_ClusterAsset.CJF_Wave5_ClusterAsset' (0x000001BA19CCE480) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB96E17B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB96E17B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB96E1710) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB96E1710) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Periphery_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_ClusterAsset.CSJ_Periphery_ClusterAsset' (0x000001BA19C5C900) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CSJ_Periphery_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_ClusterAsset.CSJ_Periphery_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_ClusterAsset.CSJ_Periphery_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_ClusterAsset.CSJ_Periphery_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_ClusterAsset.CSJ_Periphery_ClusterAsset' (0x000001BA19C5C900) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8B9DA30) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8B9DA30) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8B9D990) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8B9D990) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave1_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_ClusterAsset.CSJ_Wave1_ClusterAsset' (0x000001BA19CCD300) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CSJ_Wave1_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_ClusterAsset.CSJ_Wave1_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_ClusterAsset.CSJ_Wave1_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_ClusterAsset.CSJ_Wave1_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_ClusterAsset.CSJ_Wave1_ClusterAsset' (0x000001BA19CCD300) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8BFD7B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8BFD7B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8BFD710) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8BFD710) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave2_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_ClusterAsset.CSJ_Wave2_ClusterAsset' (0x000001BA19CCEAC0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CSJ_Wave2_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_ClusterAsset.CSJ_Wave2_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_ClusterAsset.CSJ_Wave2_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_ClusterAsset.CSJ_Wave2_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_ClusterAsset.CSJ_Wave2_ClusterAsset' (0x000001BA19CCEAC0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8BFD170) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8BFD170) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8BFD0D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8BFD0D0) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave3_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_ClusterAsset.CSJ_Wave3_ClusterAsset' (0x000001BA19CCCF40) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CSJ_Wave3_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_ClusterAsset.CSJ_Wave3_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_ClusterAsset.CSJ_Wave3_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_ClusterAsset.CSJ_Wave3_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_ClusterAsset.CSJ_Wave3_ClusterAsset' (0x000001BA19CCCF40) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB930D8F0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB930D8F0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB930D850) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB930D850) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave4_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_ClusterAsset.CSJ_Wave4_ClusterAsset' (0x000001BA19CCDD00) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CSJ_Wave4_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_ClusterAsset.CSJ_Wave4_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_ClusterAsset.CSJ_Wave4_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_ClusterAsset.CSJ_Wave4_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_ClusterAsset.CSJ_Wave4_ClusterAsset' (0x000001BA19CCDD00) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB930C270) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB930C270) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB930C1D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB930C1D0) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave5_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_ClusterAsset.CSJ_Wave5_ClusterAsset' (0x000001BA19CCF240) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CSJ_Wave5_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_ClusterAsset.CSJ_Wave5_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_ClusterAsset.CSJ_Wave5_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_ClusterAsset.CSJ_Wave5_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_ClusterAsset.CSJ_Wave5_ClusterAsset' (0x000001BA19CCF240) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB96E1CB0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB96E1CB0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB96E1C10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB96E1C10) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Periphery_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_ClusterAsset.CWF_Periphery_ClusterAsset' (0x000001BA19C5CA40) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CWF_Periphery_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_ClusterAsset.CWF_Periphery_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_ClusterAsset.CWF_Periphery_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_ClusterAsset.CWF_Periphery_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_ClusterAsset.CWF_Periphery_ClusterAsset' (0x000001BA19C5CA40) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8CB9A30) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8CB9A30) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8CB9990) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8CB9990) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave1_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_ClusterAsset.CWF_Wave1_ClusterAsset' (0x000001BA19CCC2C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CWF_Wave1_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_ClusterAsset.CWF_Wave1_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_ClusterAsset.CWF_Wave1_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_ClusterAsset.CWF_Wave1_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_ClusterAsset.CWF_Wave1_ClusterAsset' (0x000001BA19CCC2C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8BFE570) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8BFE570) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8BFE4D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8BFE4D0) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave2_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_ClusterAsset.CWF_Wave2_ClusterAsset' (0x000001BA19CCED40) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CWF_Wave2_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_ClusterAsset.CWF_Wave2_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_ClusterAsset.CWF_Wave2_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_ClusterAsset.CWF_Wave2_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_ClusterAsset.CWF_Wave2_ClusterAsset' (0x000001BA19CCED40) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8BFE1B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8BFE1B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8BFE110) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8BFE110) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave3_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_ClusterAsset.CWF_Wave3_ClusterAsset' (0x000001BA19CCD440) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CWF_Wave3_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_ClusterAsset.CWF_Wave3_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_ClusterAsset.CWF_Wave3_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_ClusterAsset.CWF_Wave3_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_ClusterAsset.CWF_Wave3_ClusterAsset' (0x000001BA19CCD440) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB930C3B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB930C3B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB930C310) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB930C310) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave4_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_ClusterAsset.CWF_Wave4_ClusterAsset' (0x000001BA19CCDF80) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CWF_Wave4_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_ClusterAsset.CWF_Wave4_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_ClusterAsset.CWF_Wave4_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_ClusterAsset.CWF_Wave4_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_ClusterAsset.CWF_Wave4_ClusterAsset' (0x000001BA19CCDF80) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB930F970) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB930F970) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB930F8D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB930F8D0) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave5_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_ClusterAsset.CWF_Wave5_ClusterAsset' (0x000001BA19CCF4C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'CWF_Wave5_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_ClusterAsset.CWF_Wave5_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_ClusterAsset.CWF_Wave5_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_ClusterAsset.CWF_Wave5_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_ClusterAsset.CWF_Wave5_ClusterAsset' (0x000001BA19CCF4C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB96E2930) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB96E2930) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB96E2890) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB96E2890) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Periphery_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Periphery/ConflictCluster_Periphery_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/ConflictCluster_Periphery_ClusterAsset.ConflictCluster_Periphery_ClusterAsset' (0x000001BA19C5C7C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'ConflictCluster_Periphery_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Periphery/ConflictCluster_Periphery_ClusterAsset.ConflictCluster_Periphery_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Periphery/ConflictCluster_Periphery_ClusterAsset.ConflictCluster_Periphery_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Periphery/ConflictCluster_Periphery_ClusterAsset.ConflictCluster_Periphery_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Periphery/ConflictCluster_Periphery_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Periphery/ConflictCluster_Periphery_ClusterAsset.ConflictCluster_Periphery_ClusterAsset' (0x000001BA19C5C7C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8CB97B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8CB97B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8CB9710) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8CB9710) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave1_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave1/ConflictCluster_Wave1_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave1/ConflictCluster_Wave1_ClusterAsset.ConflictCluster_Wave1_ClusterAsset' (0x000001BA19CCD1C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'ConflictCluster_Wave1_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave1/ConflictCluster_Wave1_ClusterAsset.ConflictCluster_Wave1_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave1/ConflictCluster_Wave1_ClusterAsset.ConflictCluster_Wave1_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave1/ConflictCluster_Wave1_ClusterAsset.ConflictCluster_Wave1_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave1/ConflictCluster_Wave1_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave1/ConflictCluster_Wave1_ClusterAsset.ConflictCluster_Wave1_ClusterAsset' (0x000001BA19CCD1C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8BFFAB0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8BFFAB0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8BFFA10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8BFFA10) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave2_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave2/ConflictCluster_Wave2_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave2/ConflictCluster_Wave2_ClusterAsset.ConflictCluster_Wave2_ClusterAsset' (0x000001BA19CCC900) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'ConflictCluster_Wave2_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave2/ConflictCluster_Wave2_ClusterAsset.ConflictCluster_Wave2_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave2/ConflictCluster_Wave2_ClusterAsset.ConflictCluster_Wave2_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave2/ConflictCluster_Wave2_ClusterAsset.ConflictCluster_Wave2_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave2/ConflictCluster_Wave2_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave2/ConflictCluster_Wave2_ClusterAsset.ConflictCluster_Wave2_ClusterAsset' (0x000001BA19CCC900) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB930C4F0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB930C4F0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB930C450) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB930C450) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave3_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave3/ConflictCluster_Wave3_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave3/ConflictCluster_Wave3_ClusterAsset.ConflictCluster_Wave3_ClusterAsset' (0x000001BA19CCCE00) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'ConflictCluster_Wave3_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave3/ConflictCluster_Wave3_ClusterAsset.ConflictCluster_Wave3_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave3/ConflictCluster_Wave3_ClusterAsset.ConflictCluster_Wave3_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave3/ConflictCluster_Wave3_ClusterAsset.ConflictCluster_Wave3_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave3/ConflictCluster_Wave3_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave3/ConflictCluster_Wave3_ClusterAsset.ConflictCluster_Wave3_ClusterAsset' (0x000001BA19CCCE00) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB930F830) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB930F830) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB930F790) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB930F790) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave4_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave4/ConflictCluster_Wave4_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave4/ConflictCluster_Wave4_ClusterAsset.ConflictCluster_Wave4_ClusterAsset' (0x000001BA19CCDBC0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'ConflictCluster_Wave4_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave4/ConflictCluster_Wave4_ClusterAsset.ConflictCluster_Wave4_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave4/ConflictCluster_Wave4_ClusterAsset.ConflictCluster_Wave4_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave4/ConflictCluster_Wave4_ClusterAsset.ConflictCluster_Wave4_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave4/ConflictCluster_Wave4_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave4/ConflictCluster_Wave4_ClusterAsset.ConflictCluster_Wave4_ClusterAsset' (0x000001BA19CCDBC0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB96E1F30) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB96E1F30) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB96E1E90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB96E1E90) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave5_PlaceCluster_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave5/ConflictCluster_Wave5_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave5/ConflictCluster_Wave5_ClusterAsset.ConflictCluster_Wave5_ClusterAsset' (0x000001BA19CCF100) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'ConflictCluster_Wave5_ClusterAsset', 'get_path_name': '/Game/DLC7/CampaignData/Clusters/Wave5/ConflictCluster_Wave5_ClusterAsset.ConflictCluster_Wave5_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC7/CampaignData/Clusters/Wave5/ConflictCluster_Wave5_ClusterAsset.ConflictCluster_Wave5_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC7/CampaignData/Clusters/Wave5/ConflictCluster_Wave5_ClusterAsset.ConflictCluster_Wave5_ClusterAsset', 'asset_paths': ['/Game/DLC7/CampaignData/Clusters/Wave5/ConflictCluster_Wave5_ClusterAsset'], 'repr': "<Object '/Game/DLC7/CampaignData/Clusters/Wave5/ConflictCluster_Wave5_ClusterAsset.ConflictCluster_Wave5_ClusterAsset' (0x000001BA19CCF100) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB96E2BB0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB96E2BB0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB96E2B10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB96E2B10) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByEndOfInvasion`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave4/ConflictCluster_Wave4_ClusterAsset']`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18412F40) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18412F40) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByPeripheryWave`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/PiratesLair/PiratesLair_ClusterAsset', '/Game/DLC1/CareerMode/Clusters/S_6_7/S_6_7_ClusterAsset']`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB184128B0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB184128B0) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave1`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/DroughtWorlds/DroughtWorlds_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_29/IndustrialHub_29_ClusterAsset', '/Game/Campaign/Clusters/Rasalhague/Rasalhague_ClusterAsset', '/Game/Campaign/Clusters/TheGraveyard/TheGraveyard_ClusterAsset', '/Game/DLC1/CareerMode/Clusters/K_1_2/K_1_2_ClusterAsset', '/Game/DLC1/CareerMode/Clusters/Rasalhague_1_3/Rasalhague_1_3_ClusterAsset', '/Game/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset', '/Game/DLC1/CareerMode/Clusters/SafeZone_16/SafeZone_16_ClusterAsset', '/Game/DLC1/CareerMode/Clusters/SafeZone_31/SafeZone_31_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Periphery/ConflictCluster_Periphery_ClusterAsset']`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18412A00) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18412A00) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave2`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/SC07/SC07_ClusterAsset', '/Game/DLC1/CareerMode/Clusters/K_4_5/K_4_5_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave1/ConflictCluster_Wave1_ClusterAsset']`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18412920) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18412920) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave3`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_2_3/K_2_3_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave2/ConflictCluster_Wave2_ClusterAsset']`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18412B50) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18412B50) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave4`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/SC05/SC05_ClusterAsset', '/Game/Campaign/Clusters/SC06/SC06_ClusterAsset', '/Game/DLC1/CareerMode/Clusters/K_3_4/K_3_4_ClusterAsset', '/Game/DLC1/CareerMode/Clusters/K_3_5_1/K_3_5_1_ClusterAsset', '/Game/DLC4/CampaignData/Clusters/RadstadtZone/RadstadtZone_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave3/ConflictCluster_Wave3_ClusterAsset']`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18412C30) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18412C30) {id: 0}>"}}`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_PlaceInvasionCorridors`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/DraconisBadlands/DraconisBadlands_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_17/IndustrialHub_17_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_22/IndustrialHub_22_ClusterAsset', '/Game/Campaign/Clusters/Lower-ClassKuritanWorlds/Lower-ClassKuritanWorlds_ClusterAsset', '/Game/Campaign/Clusters/Steiner-KuritaBorder/Steiner-KuritaBorder_ClusterAsset', '/Game/DLC1/CareerMode/Clusters/K_5_6/K_5_6_ClusterAsset', '/Game/DLC1/CareerMode/Clusters/K_7_9/K_7_9_ClusterAsset', '/Game/DLC1/CareerMode/Clusters/S_6_9/S_6_9_ClusterAsset', '/Game/DLC1/CareerMode/Clusters/SafeZone_14/SafeZone_14_ClusterAsset', '/Game/DLC1/CareerMode/Clusters/SafeZone_30/SafeZone_30_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_ClusterAsset', '/Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_ClusterAsset']`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18412D80) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18412D80) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/CampaignArcActions/Unhide_BaseCampaignStars`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_ShowUnchartedSystems`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB184107E0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB184107E0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/D7M9_Prompt`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_ShowUnchartedSystems`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/CampaignArcActions/TravelTo_D7M4`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BA9C65D170) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BA9C65D170) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_AutoAcceptMission`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB12B93090) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB12B93090) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_AutoAcceptObjective`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB12B93330) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB12B93330) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_Completed`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB184105B0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB184105B0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_Offer`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB184108C0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB184108C0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/D7M4_Place_Mission`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAA77CDE50) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAA77CDE50) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Spaceport/ArcActions/Unlock_D7M4_InstantAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18410AF0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18410AF0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Spaceport/D7M4_Prompt`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/Missions/D7_Spaceport/D7_Spaceport_Mission_Scenario`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt2_Rasalhague`
- class: `MWScenarioSpecificationAsset` exists `True`

### `/Game/DLC7/CampaignData/AtlasII_PlaceToi_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/AtlasII_MarketArc`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB184E2060) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB184E2060) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/AtlasII_Purchased`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/AtlasII_MarketArc`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/Factions/InterstellarExpeditions`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/CampaignArcActions/DLC7_D7M10_TravelBriefing`
- class: `MWFactionAsset` exists `True`

### `/Game/Factions/FreeRasalhagueRepublic`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/CampaignArcActions/DLC7_D7M1_TravelBriefing`
- class: `MWFactionAsset` exists `True`

### `/Game/Factions/Mercenaries`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/CampaignArcActions/DLC7_D7M2_TravelBriefing`
- class: `MWFactionAsset` exists `True`

### `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/CampaignArcActions/DLC7_PlaceHiddenSystemsCluster`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/_common/MW5_ClusterAssetCacheActor', '/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets']`
- cdo focused properties: `{'ClusterDataAsset': {'value': None, 'path': None, 'asset_paths': [], 'repr': 'None'}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BB0B5348B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BB0B5348B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB0B534810) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB0B534810) {id: 0}>"}}`

### `/Game/Campaign/Clusters/_common/Faction_StringTable`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_CampaignCluster1`
- class: `StringTable` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/A2M1/A2M1_ClusterAsset', '/Game/Campaign/Clusters/A2M2/A2M2_ClusterAsset', '/Game/Campaign/Clusters/A2M3/A2M3_ClusterAsset', '/Game/Campaign/Clusters/Alarion/Alarion_ClusterAsset', '/Game/Campaign/Clusters/BackwaterRegion/BackwaterRegion_ClusterAsset', '/Game/Campaign/Clusters/Davion-KuritaFrontline/Davion-KuritaFrontline_ClusterAsset', '/Game/Campaign/Clusters/DavionBorderlands/DavionBorderlands_ClusterAsset', '/Game/Campaign/Clusters/DraconisBadlands/DraconisBadlands_ClusterAsset', '/Game/Campaign/Clusters/DroughtWorlds/DroughtWorlds_ClusterAsset', '/Game/Campaign/Clusters/DuchyOfAndurien/DuchyOfAndurien_ClusterAsset', '/Game/Campaign/Clusters/DuchyOfTamarind/DuchyOfTamarind_ClusterAsset', '/Game/Campaign/Clusters/DuchyOfTsitsang/DuchyOfTsitsang_ClusterAsset', '/Game/Campaign/Clusters/FWL_ShippingLane/FWL_ShippingLane_ClusterAsset', '/Game/Campaign/Clusters/FreeWorldCommerceHub/FreeWorldCommerceHub_ClusterAsset', '/Game/Campaign/Clusters/FreeWorldInterior/FreeWorldInterior_ClusterAsset', '/Game/Campaign/Clusters/HerotitusZone/HerotitusZone_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_1/IndustrialHub_1_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_10/IndustrialHub_10_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_11/IndustrialHub_11_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_12/IndustrialHub_12_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_13/IndustrialHub_13_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_14/IndustrialHub_14_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_15/IndustrialHub_15_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_16/IndustrialHub_16_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_17/IndustrialHub_17_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_18/IndustrialHub_18_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_19/IndustrialHub_19_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_2/IndustrialHub_2_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_20/IndustrialHub_20_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_21/IndustrialHub_21_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_22/IndustrialHub_22_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_23/IndustrialHub_23_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_24/IndustrialHub_24_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_25/IndustrialHub_25_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_26/IndustrialHub_26_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_27/IndustrialHub_27_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_28/IndustrialHub_28_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_29/IndustrialHub_29_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_3/IndustrialHub_3_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_30/IndustrialHub_30_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_31/IndustrialHub_31_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_4/IndustrialHub_4_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_5/IndustrialHub_5_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_6/IndustrialHub_6_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_7/IndustrialHub_7_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_8/IndustrialHub_8_ClusterAsset', '/Game/Campaign/Clusters/IndustrialHub_9/IndustrialHub_9_ClusterAsset', '/Game/Campaign/Clusters/IndustrialMiningCollective/IndustrialMiningCollective_ClusterAsset', '/Game/Campaign/Clusters/InfernosWake/InfernosWake_ClusterAsset', '/Game/Campaign/Clusters/Kurita-DavionFrontLine/Kurita-DavionFrontLine_ClusterAsset', '/Game/Campaign/Clusters/Liao-DavionBorder/Liao-DavionBorder_ClusterAsset', '/Game/Campaign/Clusters/Lower-ClassKuritanWorlds/Lower-ClassKuritanWorlds_ClusterAsset', '/Game/Campaign/Clusters/LyranMilitaryStrongholds/LyranMilitaryStrongholds_ClusterAsset', '/Game/Campaign/Clusters/Marik-LiaoBorder/Marik-LiaoBorder_ClusterAsset', '/Game/Campaign/Clusters/Marik-StrinerBorder/Marik-StrinerBorder_ClusterAsset', '/Game/Campaign/Clusters/MercenaryRow/MercenaryRow_ClusterAsset', '/Game/Campaign/Clusters/Outreach/Outreach_ClusterAsset', '/Game/Campaign/Clusters/OutworldsAlliance/OutworldsAlliance_ClusterAsset', '/Game/Campaign/Clusters/PiratesLair/PiratesLair_ClusterAsset', '/Game/Campaign/Clusters/Rasalhague/Rasalhague_ClusterAsset', '/Game/Campaign/Clusters/Rashpur-OwensMenufacturingWorlds/Rashpur-OwensMenufacturingWorlds_ClusterAsset', '/Game/Campaign/Clusters/RebelliousLyranPrince/RebelliousLyranPrince_ClusterAsset', '/Game/Campaign/Clusters/Rogue/Rogue_ClusterAsset', '/Game/Campaign/Clusters/SC01/SC01_ClusterAsset', '/Game/Campaign/Clusters/SC02/SC02_ClusterAsset', '/Game/Campaign/Clusters/SC03/SC03_ClusterAsset', '/Game/Campaign/Clusters/SC04/SC04_ClusterAsset', '/Game/Campaign/Clusters/SC05/SC05_ClusterAsset', '/Game/Campaign/Clusters/SC06/SC06_ClusterAsset', '/Game/Campaign/Clusters/SC07/SC07_ClusterAsset', '/Game/Campaign/Clusters/ShippingRoute/ShippingRoute_ClusterAsset', '/Game/Campaign/Clusters/SianCommonality/SianCommonality_ClusterAsset', '/Game/Campaign/Clusters/Steiner-KuritaBorder/Steiner-KuritaBorder_ClusterAsset', '/Game/Campaign/Clusters/Steiner-KuritaBorder/Steiner-KuritaBorder_PostClanReplacement_ClusterAsset', '/Game/Campaign/Clusters/StweartCommonwealth/StweartCommonwealth_ClusterAsset', '/Game/Campaign/Clusters/Taurian/Taurian_ClusterAsset', '/Game/Campaign/Clusters/TheGraveyard/TheGraveyard_ClusterAsset', '/Game/Campaign/Clusters/VacantWorlds/VacantWorlds_ClusterAsset', '/Game/Campaign/Clusters/WesterhandZone/WesterhandZone_ClusterAsset', '/Game/DLC1/CareerMode/Clusters/D_11_12/D_11_12_ClusterAsset']`

### `/Game/Factions/Independent`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/Clusters/CampaignClusters/DLC7_HiddenSystems_CampaignCluster`
- class: `MWFactionAsset` exists `True`

### `/Game/DLC7/_StartConditions/DLC7AddRep_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DEBUG_DLC7_Act2_CampaignArc`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1157CB10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1157CB10) {id: 0}>"}}`

### `/Game/DLC3/HatchetmanQuestData/_StartConditions/DLC3Campaign_Start`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DEBUG_DLC7_Act3_CampaignArc`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC3/HatchetmanQuestData/DLC3_HatchetmanQuest`
- event actions: `5`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CreateCoOpReadySave_ArcAction`
  - `/Game/Campaign/NewsReel/NewsFeed_ArcAction`
  - `/Game/DLC1/CareerMode/StartConditions/Arcs/SetCompanyUnfounded`
  - `/Game/DLC1/CareerMode/Warzones/Rasalhauge_Clusters/PlaceRasalhague_ArcAction_7_10`
  - `/Game/DLC3/HatchetmanQuestData/_StartConditions/DLC3Campaign_Start`

### `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/ArcActions/D7M9_AutoAcceptObjective`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DEBUG_DLC7_Act3_CampaignArc`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1157C510) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1157C510) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/ArcActions/D7M9_Completed`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DEBUG_DLC7_Act3_CampaignArc`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18544E00) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18544E00) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/ArcActions/D7M9_Offer`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DEBUG_DLC7_Act3_CampaignArc`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18544D20) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18544D20) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/SetFahadToBridge_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Holo2_CampaignArc`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB185478E0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB185478E0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/CampaignArcActions/ShowSpears_ArcAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Holo2_CampaignArc`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18547950) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18547950) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Investigate/D7M10_Prompt`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Holo3_CampaignArc`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/CampaignArcActions/TravelTo_D7M7`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1-2_LastFrontier`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB08CE61B0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB08CE61B0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/IsInLastFrontier`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1-2_LastFrontier`
- class: `Blueprint` exists `True`

### `/Game/DLC7/CampaignData/Missions/D7_Counterattack/D7M3_Prompt`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1-2_LastFrontier`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/Missions/D7_LongRange/ArcActions/D7M7_AutoAcceptMission`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1-2_LastFrontier`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1086A4F0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1086A4F0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_LongRange/ArcActions/D7M7_AutoAcceptObjective`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1-2_LastFrontier`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1086A730) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1086A730) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_LongRange/ArcActions/D7M7_Completed`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1-2_LastFrontier`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB185440E0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB185440E0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_LongRange/ArcActions/D7M7_Offer`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1-2_LastFrontier`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18547170) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18547170) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_LongRange/ArcActions/D7M7_Place_Mission`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1-2_LastFrontier`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAA20F10D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAA20F10D0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_LongRange/ArcActions/Unlock_D7M7_InstantAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1-2_LastFrontier`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18547800) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18547800) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_LongRange/D7M7_Prompt`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1-2_LastFrontier`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/Missions/D7_LongRange/D7_LongRange_Mission_Scenario`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1-2_LastFrontier`
- class: `MWScenarioSpecificationAsset` exists `True`

### `/Game/DLC7/CampaignData/CampaignArcActions/TravelTo_D7M2`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB08CE4810) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB08CE4810) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Battle_A/ArcActions/D7M2_AutoAcceptMission`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1086ADF0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1086ADF0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Battle_A/ArcActions/D7M2_AutoAcceptObjective`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1086A850) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1086A850) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Battle_A/ArcActions/D7M2_Completed`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB185475D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB185475D0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Battle_A/ArcActions/D7M2_Offer`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18547250) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18547250) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Battle_A/ArcActions/D7M2_Place_Mission`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAA20F2750) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAA20F2750) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Battle_A/ArcActions/Unlock_D7M2_InstantAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18547410) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18547410) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Battle_A/D7M2_Prompt`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/Missions/D7_Battle_A/D7_Battle_A_Mission_Scenario`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
- class: `MWScenarioSpecificationAsset` exists `True`

### `/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/D7M3_AutoAcceptMission`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB10A35170) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB10A35170) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/D7M3_AutoAcceptObjective`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB10A357D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB10A357D0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/D7M3_Completed`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB185600E0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB185600E0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/D7M3_Offer`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18560230) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18560230) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/D7M3_Place_Mission`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAA227A150) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAA227A150) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/Show_D7M3`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB0873DE90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB0873DE90) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Counterattack/ArcActions/Unlock_D7M3_InstantAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB185603F0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB185603F0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Counterattack/D7_Counterattack_Mission_Scenario`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt1_Rodigo`
- class: `MWScenarioSpecificationAsset` exists `True`

### `/Game/DLC7/CampaignData/Missions/D7_DefendComms/ArcActions/D7M5_AutoAcceptObjective`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB10A345D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB10A345D0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_DefendComms/ArcActions/D7M5_Completed`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18560540) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18560540) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_DefendComms/ArcActions/D7M5_Offer`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB185605B0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB185605B0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_DefendComms/ArcActions/D7M5_Place_Mission`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAA2279250) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAA2279250) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_DefendComms/ArcActions/D7M5_Reset_Scenario`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18581340) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18581340) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_DefendComms/ArcActions/Unlock_D7M5_InstantAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB185607E0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB185607E0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_DefendComms/D7M5_Prompt`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/Missions/D7_DefendComms/D7_DefendComms_Mission_Scenario`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `MWScenarioSpecificationAsset` exists `True`

### `/Game/DLC7/CampaignData/Missions/D7_HoldTheLine/ArcActions/D7M8_AutoAcceptObjective`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB0FB90510) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB0FB90510) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_HoldTheLine/ArcActions/D7M8_Completed`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18580D90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18580D90) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_HoldTheLine/ArcActions/D7M8_Offer`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB185811F0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB185811F0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_HoldTheLine/ArcActions/D7M8_Place_Mission`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAA9247950) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAA9247950) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_HoldTheLine/ArcActions/D7M8_Reset_Scenario`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18580BD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18580BD0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_HoldTheLine/ArcActions/Show_D7M8`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAAD448DB0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAAD448DB0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_HoldTheLine/ArcActions/Unlock_D7M8_InstantAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18580C40) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18580C40) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_HoldTheLine/D7M8_Prompt`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/Missions/D7_HoldTheLine/D7_HoldTheLine_Mission_Scenario`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `MWScenarioSpecificationAsset` exists `True`

### `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/ArcActions/D7M9_Place_Mission`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAA92469D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAA92469D0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/ArcActions/D7M9_Reset_Scenario`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18580A10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18580A10) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/ArcActions/Show_D7M9`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAAD4FA250) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAAD4FA250) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/ArcActions/Unlock_D7M9_InstantAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18580A80) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18580A80) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Reinforcements/D7_Reinforcements_Mission_Scenario`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `MWScenarioSpecificationAsset` exists `True`

### `/Game/DLC7/CampaignData/Missions/D7_SupplyLines/ArcActions/D7M6_AutoAcceptObjective`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BA699FE070) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BA699FE070) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_SupplyLines/ArcActions/D7M6_Completed`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18581110) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18581110) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_SupplyLines/ArcActions/D7M6_Offer`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18581260) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18581260) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_SupplyLines/ArcActions/D7M6_Place_Mission`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAA9244ED0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAA9244ED0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_SupplyLines/ArcActions/D7M6_Reset_Scenario`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18580F50) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18580F50) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_SupplyLines/ArcActions/Show_D7M6`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAAD44A7F0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAAD44A7F0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_SupplyLines/ArcActions/Unlock_D7M6_InstantAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18580FC0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18580FC0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_SupplyLines/D7M6_Prompt`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/Missions/D7_SupplyLines/D7_SupplyLines_Mission_Scenario`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt3_BreadCrumbMissions`
- class: `MWScenarioSpecificationAsset` exists `True`

### `/Game/DLC7/CampaignData/CampaignArcActions/TravelTo_D7M10`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt4_ReturnToUnchartedSystems`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAAD504EF0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAAD504EF0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Investigate/ArcActions/D7M10_AutoAcceptMission`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt4_ReturnToUnchartedSystems`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB0FB91590) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB0FB91590) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Investigate/ArcActions/D7M10_AutoAcceptObjective`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt4_ReturnToUnchartedSystems`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB0FB912F0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB0FB912F0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Investigate/ArcActions/D7M10_Completed`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt4_ReturnToUnchartedSystems`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18582680) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18582680) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Investigate/ArcActions/D7M10_Offer`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt4_ReturnToUnchartedSystems`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18582760) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18582760) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Investigate/ArcActions/D7M10_Place_Mission`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt4_ReturnToUnchartedSystems`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAA83344D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAA83344D0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Investigate/ArcActions/Unlock_D7M10_InstantAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt4_ReturnToUnchartedSystems`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB185824C0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB185824C0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_Investigate/D7M10_KickoffPrompt`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt4_ReturnToUnchartedSystems`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/Missions/D7_Investigate/D7_Investigate_Mission_Scenario`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt4_ReturnToUnchartedSystems`
- class: `MWScenarioSpecificationAsset` exists `True`

### `/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/D7M12_AutoAcceptMission`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB0FB930F0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB0FB930F0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/D7M12_AutoAcceptObjective`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB0FB92DF0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB0FB92DF0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/D7M12_Completed`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18582060) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18582060) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/D7M12_Offer`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18582300) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18582300) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/D7M12_Place_Mission`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAA8337850) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAA8337850) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/D7M12_Reset_Scenario`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18581E30) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18581E30) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/Show_D7M12`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAABFBBAB0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAABFBBAB0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_FirstBattle/ArcActions/Unlock_D7M12_InstantAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18581EA0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18581EA0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_FirstBattle/D7M12_Prompt`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/Missions/D7_FirstBattle/D7_FirstBattle_Mission_Scenario`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
- class: `MWScenarioSpecificationAsset` exists `True`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_AutoAcceptMission`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB0FB924F0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB0FB924F0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_AutoAcceptObjective`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB0FB92F70) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB0FB92F70) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_Completed`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB185825A0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB185825A0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_Offer`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18582450) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18582450) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_Place_Mission`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAA83361D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAA83361D0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/D7M11_Reset_Scenario`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB185821B0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB185821B0) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/ArcActions/Unlock_D7M11_InstantAction`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18582220) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18582220) {id: 0}>"}}`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7M11_Prompt`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC7/CampaignData/Missions/D7_WavesDefend/D7_WavesDefend_Mission_Scenario`
- depth/reason: `1` / `referenced by /Game/DLC7/CampaignData/DLC7_Pt5_CrucibleEscape`
- class: `MWScenarioSpecificationAsset` exists `True`

### `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/A1_Arc`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CreateCoOpReadySave_ArcAction`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC1/CareerMode/CantinaArc`
- event actions: `67`
  - `/Game/Campaign/CampaignArcActions/Activities/Activity_EndA1M1_ArcAction`
  - `/Game/Campaign/CampaignArcActions/Activities/Activity_EndA1M2_ArcAction`
  - `/Game/Campaign/CampaignArcActions/Activities/Activity_EndA1M3_ArcAction`
  - `/Game/Campaign/CampaignArcActions/Activities/Activity_EndA1M4_ArcAction`
  - `/Game/Campaign/CampaignArcActions/Activities/Activity_MakeAvailable_ArcAction`
  - `/Game/Campaign/CampaignArcActions/TimelineActions/EstablishCompanyPromptEvent_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/A1_Arc`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/AwardAct1Achievement_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/AwardCenturion_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/CenturionAvailable_Transmission`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/CompleteCN9Available_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/CompleteMPAvailable_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/Complete_A1M1_Objective_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/Complete_A1M2_Objective_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/Complete_A1M3_Objective_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/CreateCenturionRepairWorkOrder_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/EnableCampaignMultiplayer_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/EnableOperations_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/Lock_Barracks_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/Lock_Home_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/Lock_Market_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/Lock_MechLab_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/Lock_Operations_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/Lock_StarMap_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/MultiplayerAvailable_Transmission`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/OfferCN9Available_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/OfferCantinaAsperational_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/OfferMPAvailable_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/ResolveA1Complete_Objective_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/SetFahadToGroundBay2_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/SpeakToFahad_A1H1_01_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/SpeakToFahad_A1H2_01_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/SpeakToFahad_A1H4_01_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/SpeakToRyana_A1H1_01_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/SpeakToRyana_A1H1_02_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/SpeakToRyana_A1H2_01_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/SpeakToRyana_A1H3_01_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/SpeakToRyana_A1H4_01_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/SpeakToRyana_A1H4_02_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/SpeakToRyana_A1H5_01_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/UnlockA1M1_InstantAction_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/UnlockA1M2_InstantAction_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/UnlockA1M3_InstantAction_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/UnlockA1M4_InstantAction_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CompleteA1M4_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CreateA1M1AcceptContract`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CreateCoOpReadySave_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/OfferA1M4_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/PlaceA1M1Mission_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/PlaceA1M2Mission_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/PlaceA1M3Mission_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/PlaceA1M4Mission_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/TravelToA1M4_ArcAction`
  - `/Game/Campaign/CampaignArcs/MW5Core_InjectSpareParts_ArcAction`
  - `/Game/Campaign/CampaignArcs/StoryArcs/Act1/A1M1_Objective`
  - `/Game/Campaign/CampaignArcs/StoryArcs/Act1/A1M2_Objective`
  - `/Game/Campaign/CampaignArcs/StoryArcs/Act1/A1M3_Objective`
  - `/Game/Campaign/CampaignArcs/StoryArcs/Act1/A1M4_Objective`
  - `/Game/Campaign/CampaignArcs/StoryArcs/Act1/CreateA1M1_TimelineEvent_ArcAction`
  - `/Game/Campaign/CampaignArcs/StoryArcs/Act1/OfferA1M1_ArcAction`
  - `/Game/Campaign/CampaignArcs/StoryArcs/Act1/OfferA1M2_ArcAction`
  - `/Game/Campaign/CampaignArcs/StoryArcs/Act1/OfferA1M3_ArcAction`
  - `/Game/DLC1/DLC_1`
  - `/Game/Levels/AuthoredMissions/A1M1_SupplyRun/AreaTiles/A1M1_SupplyRun_Scenario`
  - `/Game/Levels/AuthoredMissions/A1M2_Recon/AreaTiles/A1M2_Recon_Scenario`
  - `/Game/Levels/AuthoredMissions/A1M3_Offensive/AreaTiles/A1M3_Offensive_Scenario`
  - `/Game/Levels/AuthoredMissions/A1M4_Defender/AreaTiles/A1M4_Defender_Scenario`

### `/Game/Campaign/CampaignArcs/FactionStarts/PostAct3Start/Post_Act3Start`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CreateCoOpReadySave_ArcAction`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `3`
  - `/Game/Campaign/CampaignArcs/Campaign_DLC1HeroMissions`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A3_Arc/A3_Arc`
  - `/Game/Campaign/CampaignArcs/MW5CoreCampaign`
- event actions: `8`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/Lock_Cantinas_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/ResolveA1Complete_Objective_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/ResolveA2Complete_Objective_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CreateCoOpReadySave_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/PostAct3Start/Post_Act3Start`
  - `/Game/Campaign/CampaignArcs/FactionStarts/PostAct3Start/Post_Act3_AddRep_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/PostAct3Start/ResolveA3Complete_Objective_ArcAction`
  - `/Game/Campaign/CampaignArcs/MW5Core_InjectSpareParts_ArcAction`

### `/Game/Campaign/CampaignArcs/FactionStarts/Post_Act1Start/Post_Act1Start`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CreateCoOpReadySave_ArcAction`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `4`
  - `/Game/Campaign/CampaignArcs/Campaign_DLC1HeroMissions`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/A2_Arc`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A3_Arc/A3_Arc`
  - `/Game/Campaign/CampaignArcs/MW5CoreCampaign`
- event actions: `3`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/ResolveA1Complete_Objective_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CreateCoOpReadySave_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/Post_Act1Start/AddPostAct1Rep_ArcAction`

### `/Game/Campaign/CampaignArcs/FactionStarts/Post_Act2Start/Post_Act2Start`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CreateCoOpReadySave_ArcAction`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `5`
  - `/Game/Campaign/CampaignArcs/Campaign_DLC1HeroMissions`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A3_Arc/A3_Arc`
  - `/Game/Campaign/CampaignArcs/MW5CoreCampaign`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_04/BreakTheSiege/Child_SC04_Q7`
  - `/Game/DLC1/CareerMode/Sidequests/MS_Exclusive/DLC1_GoblinArc`
- event actions: `11`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/Lock_Cantinas_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/ResolveA1Complete_Objective_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/CompleteA2M4_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/CompleteRep12_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/ResolveA2Complete_Objective_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CreateCoOpReadySave_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/Post_Act2Start/Post_Act2Start`
  - `/Game/Campaign/CampaignArcs/FactionStarts/Post_Act2Start/Post_Act2_AddRep_ArcAction`
  - `/Game/Campaign/CampaignArcs/MW5Core_InjectSpareParts_ArcAction`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_03/BloodAnTreasure/Complete_SC03_Q6`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_03/HostageRescue/Complete_SC03_Q5`

### `/Game/Campaign/CampaignArcs/FactionStarts/Pre_Act2Start/Pre_Act2Start`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CreateCoOpReadySave_ArcAction`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `3`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/A2_Arc`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A3_Arc/A3_Arc`
  - `/Game/Campaign/CampaignArcs/MW5CoreCampaign`
- event actions: `7`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/Lock_Cantinas_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/ResolveA1Complete_Objective_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CreateCoOpReadySave_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/Pre_Act2Start/Pre_Act2_AddRep_ArcAction`
  - `/Game/Campaign/CampaignArcs/Regions/5_2/WorkersRebellion/CompleteWRStoryCluster_ArcAction`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/GreatHouses/Complete_SC01_Q1`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/GreatHouses/Complete_SC01_Q2`

### `/Game/Campaign/CampaignArcs/FactionStarts/Pre_Act3Start/Pre_Act3Start`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CreateCoOpReadySave_ArcAction`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `2`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A3_Arc/A3_Arc`
  - `/Game/Campaign/CampaignArcs/MW5CoreCampaign`
- event actions: `8`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/Lock_Cantinas_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/ResolveA1Complete_Objective_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/ResolveA2Complete_Objective_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/CreateCoOpReadySave_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/Pre_Act3Start/Pre_Act3Start`
  - `/Game/Campaign/CampaignArcs/FactionStarts/Pre_Act3Start/Pre_Act3_AddRep_ArcAction`
  - `/Game/Campaign/CampaignArcs/MW5Core_InjectSpareParts_ArcAction`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_05/ComstarBullies/Complete_SC05_Q8`

### `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/MainCampaignStart_Arc`
- depth/reason: `2` / `referenced by /Game/Campaign/NewsReel/NewsFeed_ArcAction`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `2`
  - `/Game/Campaign/CampaignArcs/FactionStarts/CommonStart`
  - `/Game/Campaign/CampaignArcs/MW5CoreCampaign`
- event actions: `3`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/DisableCampaignMultiplayer_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/MainCampaignStart/MainCampaignStart_Arc`
  - `/Game/Campaign/NewsReel/NewsFeed_ArcAction`

### `/Game/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/Rasalhauge_Clusters/PlaceRasalhague_ArcAction_7_10`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset']`

### `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/Rasalhauge_Clusters/PlaceRasalhague_ArcAction_7_10`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/Rasalhague_1_3/Rasalhague_1_3_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/Rasalhauge_Clusters/PlaceRasalhague_ArcAction_1_3`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/Rasalhague_1_3/Rasalhague_1_3_ClusterAsset']`

### `/Game/Campaign/CampaignArcActions/StateChangeActions/AddDefaultCodexEntries_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/FactionStarts/AddDefaultCodexEntries_Arc`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB185A8310) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB185A8310) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/GameOver/OverdraftTimelineEvent_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/GameOver/Overdraft_Arc`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB186575D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB186575D0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/FactionStarts/A3_Arc/Travel_A3M1`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/HidingSystems/HidingSystemsArc`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/Campaign/CampaignArcs/FactionStarts/A3_Arc/Travel_A3M2`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/HidingSystems/HidingSystemsArc`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/Campaign/CampaignArcs/FactionStarts/A3_Arc/Travel_A3M3`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/HidingSystems/HidingSystemsArc`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/Campaign/CampaignArcs/HidingSystems/A3M1_HideSystemArc`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/HidingSystems/HidingSystemsArc`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18656680) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18656680) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/HidingSystems/A3M2_HideSystemArc`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/HidingSystems/HidingSystemsArc`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18655C00) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18655C00) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/HidingSystems/A3MFinal_HideSystemArc`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/HidingSystems/HidingSystemsArc`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18655DC0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18655DC0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/HidingSystems/Q10_HideSystemArc`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/HidingSystems/HidingSystemsArc`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18655CE0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18655CE0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/HidingSystems/Q9_HideSystemArc`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/HidingSystems/HidingSystemsArc`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB186558F0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB186558F0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/StoryCluster_06/RaidOnComstar/SC06_Q9_Prompt`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/HidingSystems/HidingSystemsArc`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/Campaign/CampaignArcs/Regions/StoryCluster_07/HitAndRun/SC07_Q10_Prompt`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/HidingSystems/HidingSystemsArc`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/A2_Arc`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/Razer_Exclusive/Razer_WolverineArc`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `2`
  - `/Game/Campaign/CampaignArcs/Razer_Exclusive/Razer_WolverineArc`
  - `/Game/DLC1/CareerMode/Sidequests/MS_Exclusive/DLC1_GoblinArc`
- event actions: `45`
  - `/Game/Campaign/CampaignArcActions/Activities/Activity_EndA2M1_ArcAction`
  - `/Game/Campaign/CampaignArcActions/Activities/Activity_EndA2M2_ArcAction`
  - `/Game/Campaign/CampaignArcActions/Activities/Activity_EndA2M3_ArcAction`
  - `/Game/Campaign/CampaignArcActions/Activities/Activity_EndA2M4_ArcAction`
  - `/Game/Campaign/CampaignArcActions/Activities/Activity_EndAct2Rep_ArcAction`
  - `/Game/Campaign/CampaignArcActions/Activities/Activity_EndRep10_ArcAction`
  - `/Game/Campaign/CampaignArcActions/Activities/Activity_EndRep11_ArcAction`
  - `/Game/Campaign/CampaignArcActions/Activities/Activity_EndRep12_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/A2_Arc`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/AwardAct2Achievement_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/CompleteA2M1_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/CompleteA2M2_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/CompleteA2M3_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/CompleteA2M4_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/OfferA2M1_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/OfferA2M2_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/OfferA2M3_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/OfferA2M4_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/PlaceA2M1_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/PlaceA2M2_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/PlaceA2M3_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/PlaceA2M4_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/ResolveA2Complete_Objective_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/SpeakToFahad_A2H1_01_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/SpeakToFahad_A2H2_01_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/SpeakToFahad_A2H4_01_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/SpeakToRyana_A2H1_01_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/SpeakToRyana_A2H2_01_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/SpeakToRyana_A2H3_01_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/SpeakToRyana_A2H4_01_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/UnlockA2M1_InstantAction_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/UnlockA2M2_InstantAction_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/UnlockA2M3_InstantAction_ArcAction`
  - `/Game/Campaign/CampaignArcs/FactionStarts/A2_Arc/UnlockA2M4_InstantAction_ArcAction`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/GreatHouses/SC01_Q2_Prompt`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_02/DistressCall/SC02_Prompt`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_03/BloodAnTreasure/SC03_Q6_Prompt`
  - `/Game/Campaign/CampaignArcs/StoryArcs/Act2/A2M1_Objective`
  - `/Game/Campaign/CampaignArcs/StoryArcs/Act2/A2M2_Objective`
  - `/Game/Campaign/CampaignArcs/StoryArcs/Act2/A2M3_Objective`
  - `/Game/Campaign/CampaignArcs/StoryArcs/Act2/A2M4_Objective`
  - `/Game/Levels/AuthoredMissions/A2M1_InfernoCaptain1/AreaTiles/A2M1_InfernoCaptain1_Scenario`
  - `/Game/Levels/AuthoredMissions/A2M2_Port/AreaTiles/A2M2_Port_Scenario`
  - `/Game/Levels/AuthoredMissions/A2M3_Zombie/AreaTiles/A2M3_Zombie_Scenario`
  - `/Game/Levels/AuthoredMissions/A2M4/AreaTiles/A2M4_Scenario`

### `/Game/Campaign/CampaignArcs/Razer_Exclusive/CompleteRazerWolverineUnlocked_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/Razer_Exclusive/Razer_WolverineArc`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18655EA0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18655EA0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Razer_Exclusive/RazerWolverineUnlocked_Transmission`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/Razer_Exclusive/Razer_WolverineArc`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/Campaign/CampaignArcs/Razer_Exclusive/RazerWolverine_GiveReward_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/Razer_Exclusive/Razer_WolverineArc`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1007ECD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1007ECD0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/CompleteCantinaUnlocked_ArcAction`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/CantinaArc`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863E4C0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863E4C0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/Lock_Cantinas_ArcAction`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/CantinaArc`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BA7FF69FD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BA7FF69FD0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/FactionStarts/A1_Arc/Lock_Cantinas_Fallback_ArcAction`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/CantinaArc`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863C7E0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863C7E0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Clusters/S_10_12/CareerCluster_6`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `MWFactionAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/S_10_12/S_10_12_ClusterAsset']`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/CompleteDragon4_ArcAction`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863D180) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863D180) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_HM4_GeneratedMission_1_Scenario`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `MWScenarioSpecificationAsset` exists `True`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_HM4_GeneratedMission_2_Scenario`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `MWScenarioSpecificationAsset` exists `True`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_HM4_GeneratedMission_3_Scenario`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `MWScenarioSpecificationAsset` exists `True`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC_DRGN_Prompt`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC_DRGN_Prompt2`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC_DRGN_Prompt3`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC_DRGN_Prompt4`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DRG_Mission_1/DRG1_Complete_AuthoredScenario`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863C9A0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863C9A0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DRG_Mission_1/DRG1_Place_Authored_Scenario`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAAE081DD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAAE081DD0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DRG_Mission_1/DRG1_Reset_Scenario`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863CBD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863CBD0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DRG_Mission_2/DRG2_Complete_AuthoredScenario`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863CD90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863CD90) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DRG_Mission_2/DRG2_Place_Authored_Scenario`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAAE080650) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAAE080650) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DRG_Mission_2/DRG2_Reset_Scenario`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863CD20) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863CD20) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DRG_Mission_3/DRG3_Complete_AuthoredScenario`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863D0A0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863D0A0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DRG_Mission_3/DRG3_Place_Authored_Scenario`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAAE081650) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAAE081650) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DRG_Mission_3/DRG3_Reset_Scenario`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863E060) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863E060) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/OfferDragon1_ArcAction`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863DB90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863DB90) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/OfferDragon2_ArcAction`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863C8C0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863C8C0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/OfferDragon3_ArcAction`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863C930) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863C930) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/OfferDragon4_ArcAction`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863CCB0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863CCB0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/Place_Authored_Dragon`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAA7FF4ED0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAA7FF4ED0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/Reset_Scenario_DRG`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863E3E0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863E3E0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/ShowDragonSideQuest_ArcAction`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BA19F0B790) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BA19F0B790) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/Unlock_DLC1_DRG_01_InstantAction_ArcAction`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863CB60) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863CB60) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/Unlock_DLC1_DRG_02_InstantAction_ArcAction`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863CE70) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863CE70) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/Unlock_DLC1_DRG_03_InstantAction_ArcAction`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863E0D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863E0D0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/Unlock_DLC1_DRG_04_InstantAction_ArcAction`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Dragon/DLC1_Dragon`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863E290) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863E290) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasMSMechEntitlement`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/MS_Exclusive/DLC1_GoblinArc`
- class: `Blueprint` exists `True`

### `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoGoblin`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/MS_Exclusive/DLC1_GoblinArc`
- class: `Blueprint` exists `True`

### `/Game/DLC1/CareerMode/Sidequests/MS_Exclusive/CompleteGoblinUnlocked_ArcAction`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/MS_Exclusive/DLC1_GoblinArc`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863E5A0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB1863E5A0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/MS_Exclusive/GoblinUnlocked_Transmission`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Sidequests/MS_Exclusive/DLC1_GoblinArc`
- class: `MWMetagameObjectiveAsset` exists `True`

### `/Game/DLC2/CampaignData/DLC2_Act1`
- depth/reason: `2` / `referenced by /Game/DLC2/CampaignData/DLC2_CoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission3/DLC2_Act1_Warnings`
- event actions: `34`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/DLC2_Act1`
  - `/Game/DLC2/CampaignData/DLC2_Prologue`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission3/Act1Kickoff_Prompt`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission3/DLC2_Act1_CompleteKickoff`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission3/DLC2_Act1_CustomMarket`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission3/DLC2_Act1_PriorityTransmission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission3/DLC2_M3_AutoAcceptMission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission3/DLC2_M3_AutoAcceptObjective`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission3/DLC2_M3_Completed`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission3/DLC2_M3_Offer`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission3/DLC2_M3_Place_Mission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission3/DLC2_M3_Prompt`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission3/TravelToDLC2_Act1`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission3/Unlock_DLC2_M3_InstantAction`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission4/DLC2_M4_AutoAcceptMission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission4/DLC2_M4_AutoAcceptObjective`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission4/DLC2_M4_Completed`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission4/DLC2_M4_Offer`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission4/DLC2_M4_Place_Mission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission4/DLC2_M4_Prompt`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission4/Unlock_DLC2_M4_InstantAction`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission5/DLC2_M5_AutoAcceptMission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission5/DLC2_M5_AutoAcceptObjective`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission5/DLC2_M5_Completed`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission5/DLC2_M5_Offer`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission5/DLC2_M5_Place_Mission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission5/DLC2_M5_Prompt`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission5/Unlock_DLC2_M5_InstantAction`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC2/DLC_2`
  - `/Game/DLC2/Levels/MiniCampaign/AuthoredMissions/D2M5/D2M5_Scenario`
  - `/Game/DLC2/Levels/MiniCampaign/ProcMissions/D2M3/D2M3_Scenario`
  - `/Game/DLC2/Levels/MiniCampaign/ProcMissions/D2M4/D2M4_Scenario`

### `/Game/DLC2/CampaignData/DLC2_Act2`
- depth/reason: `2` / `referenced by /Game/DLC2/CampaignData/DLC2_CoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `30`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/DLC2_Act2`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission5/DLC2_M5_Prompt`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission7/DLC2_Act2_CustomMarket`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission7/DLC2_M7_AutoAcceptMission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission7/DLC2_M7_AutoAcceptObjective`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission7/DLC2_M7_Completed`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission7/DLC2_M7_Offer`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission7/DLC2_M7_Place_Mission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission7/DLC2_M7_Prompt`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission7/TravelToDLC2_Act2`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission7/Unlock_DLC2_M7_InstantAction`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission8/DLC2_M8_AutoAcceptMission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission8/DLC2_M8_AutoAcceptObjective`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission8/DLC2_M8_Completed`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission8/DLC2_M8_Offer`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission8/DLC2_M8_Place_Mission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission8/DLC2_M8_Prompt`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission8/Unlock_DLC2_M8_InstantAction`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission9/DLC2_M9_AutoAcceptMission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission9/DLC2_M9_AutoAcceptObjective`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission9/DLC2_M9_Completed`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission9/DLC2_M9_Offer`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission9/DLC2_M9_Place_Mission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission9/DLC2_M9_Prompt`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission9/Unlock_DLC2_M9_InstantAction`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC2/Levels/MiniCampaign/AuthoredMissions/D2M7/D2M7_Scenario`
  - `/Game/DLC2/Levels/MiniCampaign/ProcMissions/D2M8/D2M8_Scenario`
  - `/Game/DLC2/Levels/MiniCampaign/ProcMissions/D2M9/D2M9_Scenario`

### `/Game/DLC2/CampaignData/DLC2_Act3`
- depth/reason: `2` / `referenced by /Game/DLC2/CampaignData/DLC2_CoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `3`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission10/DLC2_M10_SpecialRewards`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission13/DLC2_M13_SpecialRewards`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission15/DLC2_M15_SpecialRewards`
- event actions: `54`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/DLC2_Act3`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission10/DLC2_Act3_CustomMarket`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission10/DLC2_M10_AutoAcceptMission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission10/DLC2_M10_AutoAcceptObjective`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission10/DLC2_M10_Completed`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission10/DLC2_M10_Offer`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission10/DLC2_M10_Place_Mission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission10/DLC2_M10_Prompt`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission10/TravelToDLC2_Act3`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission10/Unlock_DLC2_M10_InstantAction`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission11/DLC2_M11_AutoAcceptMission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission11/DLC2_M11_AutoAcceptObjective`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission11/DLC2_M11_Completed`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission11/DLC2_M11_Offer`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission11/DLC2_M11_Place_Mission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission11/DLC2_M11_Prompt`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission11/Unlock_DLC2_M11_InstantAction`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission12/DLC2_M12_AutoAcceptMission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission12/DLC2_M12_AutoAcceptObjective`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission12/DLC2_M12_Completed`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission12/DLC2_M12_Offer`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission12/DLC2_M12_Place_Mission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission12/DLC2_M12_Prompt`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission12/Unlock_DLC2_M12_InstantAction`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission13/DLC2_M13_AutoAcceptMission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission13/DLC2_M13_AutoAcceptObjective`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission13/DLC2_M13_Completed`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission13/DLC2_M13_Offer`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission13/DLC2_M13_Place_Mission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission13/DLC2_M13_Prompt`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission13/Unlock_DLC2_M13_InstantAction`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission14/DLC2_M14_AutoAcceptMission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission14/DLC2_M14_AutoAcceptObjective`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission14/DLC2_M14_Completed`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission14/DLC2_M14_Offer`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission14/DLC2_M14_Place_Mission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission14/DLC2_M14_Prompt`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission14/Unlock_DLC2_M14_InstantAction`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission15/DLC2_M15_AutoAcceptMission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission15/DLC2_M15_AutoAcceptObjective`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission15/DLC2_M15_Completed`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission15/DLC2_M15_Offer`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission15/DLC2_M15_Place_Mission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission15/DLC2_M15_Prompt`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission15/Unlock_DLC2_M15_InstantAction`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission9/DLC2_M9_Prompt`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC2/Levels/MiniCampaign/AuthoredMissions/D2M15/D2M15_Scenario`
  - `/Game/DLC2/Levels/MiniCampaign/ProcMissions/D2M10/D2M10_Scenario`
  - `/Game/DLC2/Levels/MiniCampaign/ProcMissions/D2M11/D2M11_Scenario`
  - `/Game/DLC2/Levels/MiniCampaign/ProcMissions/D2M12/D2M12_Scenario`
  - `/Game/DLC2/Levels/MiniCampaign/ProcMissions/D2M13/D2M13_Scenario`
  - `/Game/DLC2/Levels/MiniCampaign/ProcMissions/D2M14/D2M14_Scenario`

### `/Game/DLC2/CampaignData/DLC2_Prologue`
- depth/reason: `2` / `referenced by /Game/DLC2/CampaignData/DLC2_CoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `2`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission1/DLC2_Prologue_Warnings`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission2/DLC2_M2_SpecialRewards`
- event actions: `25`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/DLC2_Prologue`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission1/DLC2_M1_AutoAcceptMission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission1/DLC2_M1_AutoAcceptObjective`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission1/DLC2_M1_Completed`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission1/DLC2_M1_Offer`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission1/DLC2_M1_Place_Mission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission1/DLC2_M1_Prompt`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission1/DLC2_Prologue_CompleteKickoff`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission1/DLC2_Prologue_CustomMarket`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission1/DLC2_Prologue_PriorityTransmission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission1/PrologueKickoff_Prompt`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission1/TravelToDLC2_Prologue`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission1/Unlock_DLC2_M1_InstantAction`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission2/DLC2_M2_AutoAcceptMission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission2/DLC2_M2_AutoAcceptObjective`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission2/DLC2_M2_Completed`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission2/DLC2_M2_Offer`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission2/DLC2_M2_Place_Mission`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission2/DLC2_M2_Prompt`
  - `/Game/DLC2/CampaignData/Missions/DLC2_Mission2/Unlock_DLC2_M2_InstantAction`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC2/DLC_2`
  - `/Game/DLC2/Levels/MiniCampaign/ProcMissions/D2M1/D2M1_Scenario`
  - `/Game/DLC2/Levels/MiniCampaign/ProcMissions/D2M2/D2M2_Scenario`

### `/Game/DLC2/CampaignData/PlanetClusterData/DLC2_SetupPlanetaryWarzones`
- depth/reason: `2` / `referenced by /Game/DLC2/CampaignData/DLC2_CoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `6`
  - `/Game/DLC2/CampaignData/PlanetClusterData/Place_BethonologZone`
  - `/Game/DLC2/CampaignData/PlanetClusterData/Place_CaseltonZone`
  - `/Game/DLC2/CampaignData/PlanetClusterData/Place_PiratesHavenZone`
  - `/Game/DLC2/CampaignData/PlanetClusterData/Place_SarnaZone`
  - `/Game/DLC2/CampaignData/PlanetClusterData/Place_TigressZone`
  - `/Game/DLC2/CampaignData/PlanetClusterData/Place_TikonovZone`

### `/Game/DLC4/CampaignData/DLC4_Pt2_Kirchbach`
- depth/reason: `2` / `referenced by /Game/DLC4/CampaignData/DLC4_CoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `3`
  - `/Game/DLC4/CampaignData/Missions/D4M03/DLC4_Pt2_Warnings`
  - `/Game/DLC4/CampaignData/Missions/D4M04/D4M04_SpecialRewards`
  - `/Game/DLC4/CampaignData/PlanetClusterData/DLC4_SetupPlanetaryWarzones`
- event actions: `24`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC4/CampaignData/DLC4_Pt2_Kirchbach`
  - `/Game/DLC4/CampaignData/Missions/D4M03/D4M03_AutoAcceptMission`
  - `/Game/DLC4/CampaignData/Missions/D4M03/D4M03_AutoAcceptObjective`
  - `/Game/DLC4/CampaignData/Missions/D4M03/D4M03_Completed`
  - `/Game/DLC4/CampaignData/Missions/D4M03/D4M03_Place_Mission`
  - `/Game/DLC4/CampaignData/Missions/D4M03/D4M03_Prompt`
  - `/Game/DLC4/CampaignData/Missions/D4M03/D4M03_Scenario`
  - `/Game/DLC4/CampaignData/Missions/D4M03/DLC4_Pt2_CompleteKickoff`
  - `/Game/DLC4/CampaignData/Missions/D4M03/DLC4_Pt2_Kickoff_Prompt`
  - `/Game/DLC4/CampaignData/Missions/D4M03/DLC4_Pt2_PriorityTransmission`
  - `/Game/DLC4/CampaignData/Missions/D4M03/Show_D4M03`
  - `/Game/DLC4/CampaignData/Missions/D4M03/TravelTo_D4M03`
  - `/Game/DLC4/CampaignData/Missions/D4M03/Unlock_D4M03_InstantAction`
  - `/Game/DLC4/CampaignData/Missions/D4M04/D4M04_AutoAcceptMission`
  - `/Game/DLC4/CampaignData/Missions/D4M04/D4M04_AutoAcceptObjective`
  - `/Game/DLC4/CampaignData/Missions/D4M04/D4M04_Completed`
  - `/Game/DLC4/CampaignData/Missions/D4M04/D4M04_Place_Mission`
  - `/Game/DLC4/CampaignData/Missions/D4M04/D4M04_Prompt`
  - `/Game/DLC4/CampaignData/Missions/D4M04/D4M04_Scenario`
  - `/Game/DLC4/CampaignData/Missions/D4M04/Show_D3M04`
  - `/Game/DLC4/CampaignData/Missions/D4M04/Unlock_D3M04_InstantAction`
  - `/Game/DLC4/DLC_4`

### `/Game/DLC4/CampaignData/DLC4_Pt3_Rasalhague`
- depth/reason: `2` / `referenced by /Game/DLC4/CampaignData/DLC4_CoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC4/CampaignData/Missions/D4M05/DLC3_Pt3_Warnings`
- event actions: `26`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC4/CampaignData/DLC4_Pt2_Kirchbach`
  - `/Game/DLC4/CampaignData/DLC4_Pt3_Rasalhague`
  - `/Game/DLC4/CampaignData/Missions/D4M05/D4M05_AutoAcceptMission`
  - `/Game/DLC4/CampaignData/Missions/D4M05/D4M05_AutoAcceptObjective`
  - `/Game/DLC4/CampaignData/Missions/D4M05/D4M05_Completed`
  - `/Game/DLC4/CampaignData/Missions/D4M05/D4M05_Offer`
  - `/Game/DLC4/CampaignData/Missions/D4M05/D4M05_Place_Mission`
  - `/Game/DLC4/CampaignData/Missions/D4M05/D4M05_Prompt`
  - `/Game/DLC4/CampaignData/Missions/D4M05/D4M05_Scenario`
  - `/Game/DLC4/CampaignData/Missions/D4M05/DLC3_Pt3_CompleteKickoff`
  - `/Game/DLC4/CampaignData/Missions/D4M05/DLC3_Pt3_Kickoff_Prompt`
  - `/Game/DLC4/CampaignData/Missions/D4M05/DLC3_Pt3_PriorityTransmission`
  - `/Game/DLC4/CampaignData/Missions/D4M05/DLC4_Rasalhague_CustomMarket`
  - `/Game/DLC4/CampaignData/Missions/D4M05/TravelTo_D4M05`
  - `/Game/DLC4/CampaignData/Missions/D4M05/Unlock_D4M05_InstantAction`
  - `/Game/DLC4/CampaignData/Missions/D4M06/D4M06_AutoAcceptMission`
  - `/Game/DLC4/CampaignData/Missions/D4M06/D4M06_AutoAcceptObjective`
  - `/Game/DLC4/CampaignData/Missions/D4M06/D4M06_Completed`
  - `/Game/DLC4/CampaignData/Missions/D4M06/D4M06_Offer`
  - `/Game/DLC4/CampaignData/Missions/D4M06/D4M06_Place_Mission`
  - `/Game/DLC4/CampaignData/Missions/D4M06/D4M06_Prompt`
  - `/Game/DLC4/CampaignData/Missions/D4M06/D4M06_Scenario`
  - `/Game/DLC4/CampaignData/Missions/D4M06/Unlock_D4M06_InstantAction`
  - `/Game/DLC4/DLC_4`

### `/Game/DLC4/CampaignData/DLC4_Pt4_Predilitz`
- depth/reason: `2` / `referenced by /Game/DLC4/CampaignData/DLC4_CoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `30`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC4/CampaignData/DLC4_Pt4_Predilitz`
  - `/Game/DLC4/CampaignData/Missions/D4M06/D4M06_Prompt`
  - `/Game/DLC4/CampaignData/Missions/D4M07/D4M07_AutoAcceptMission`
  - `/Game/DLC4/CampaignData/Missions/D4M07/D4M07_AutoAcceptObjective`
  - `/Game/DLC4/CampaignData/Missions/D4M07/D4M07_Completed`
  - `/Game/DLC4/CampaignData/Missions/D4M07/D4M07_Offer`
  - `/Game/DLC4/CampaignData/Missions/D4M07/D4M07_Place_Mission`
  - `/Game/DLC4/CampaignData/Missions/D4M07/D4M07_Prompt`
  - `/Game/DLC4/CampaignData/Missions/D4M07/D4M07_Scenario`
  - `/Game/DLC4/CampaignData/Missions/D4M07/DLC4_Predlitz_CustomMarket`
  - `/Game/DLC4/CampaignData/Missions/D4M07/TravelTo_D4M07`
  - `/Game/DLC4/CampaignData/Missions/D4M07/Unlock_D4M07_InstantAction`
  - `/Game/DLC4/CampaignData/Missions/D4M08/D4M08_AutoAcceptMission`
  - `/Game/DLC4/CampaignData/Missions/D4M08/D4M08_AutoAcceptObjective`
  - `/Game/DLC4/CampaignData/Missions/D4M08/D4M08_Completed`
  - `/Game/DLC4/CampaignData/Missions/D4M08/D4M08_Offer`
  - `/Game/DLC4/CampaignData/Missions/D4M08/D4M08_Place_Mission`
  - `/Game/DLC4/CampaignData/Missions/D4M08/D4M08_Prompt`
  - `/Game/DLC4/CampaignData/Missions/D4M08/D4M08_Scenario`
  - `/Game/DLC4/CampaignData/Missions/D4M08/Unlock_D4M08_InstantAction`
  - `/Game/DLC4/CampaignData/Missions/D4M09/D4M09_AutoAcceptMission`
  - `/Game/DLC4/CampaignData/Missions/D4M09/D4M09_AutoAcceptObjective`
  - `/Game/DLC4/CampaignData/Missions/D4M09/D4M09_Completed`
  - `/Game/DLC4/CampaignData/Missions/D4M09/D4M09_Offer`
  - `/Game/DLC4/CampaignData/Missions/D4M09/D4M09_Place_Mission`
  - `/Game/DLC4/CampaignData/Missions/D4M09/D4M09_Prompt`
  - `/Game/DLC4/CampaignData/Missions/D4M09/D4M09_Scenario`
  - `/Game/DLC4/CampaignData/Missions/D4M09/Unlock_D4M09_InstantAction`

### `/Game/DLC4/CampaignData/DLC4_Pt5_Gunzberg`
- depth/reason: `2` / `referenced by /Game/DLC4/CampaignData/DLC4_CoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `30`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC4/CampaignData/DLC4_Pt5_Gunzberg`
  - `/Game/DLC4/CampaignData/Missions/D4M09/D4M09_Prompt`
  - `/Game/DLC4/CampaignData/Missions/D4M10/D4M10_AutoAcceptMission`
  - `/Game/DLC4/CampaignData/Missions/D4M10/D4M10_AutoAcceptObjective`
  - `/Game/DLC4/CampaignData/Missions/D4M10/D4M10_Completed`
  - `/Game/DLC4/CampaignData/Missions/D4M10/D4M10_Offer`
  - `/Game/DLC4/CampaignData/Missions/D4M10/D4M10_Place_Mission`
  - `/Game/DLC4/CampaignData/Missions/D4M10/D4M10_Prompt`
  - `/Game/DLC4/CampaignData/Missions/D4M10/D4M10_Scenario`
  - `/Game/DLC4/CampaignData/Missions/D4M10/DLC4_Gunzburg_CustomMarket`
  - `/Game/DLC4/CampaignData/Missions/D4M10/TravelTo_D4M10`
  - `/Game/DLC4/CampaignData/Missions/D4M10/Unlock_D4M10_InstantAction`
  - `/Game/DLC4/CampaignData/Missions/D4M11/D4M11_AutoAcceptMission`
  - `/Game/DLC4/CampaignData/Missions/D4M11/D4M11_AutoAcceptObjective`
  - `/Game/DLC4/CampaignData/Missions/D4M11/D4M11_Completed`
  - `/Game/DLC4/CampaignData/Missions/D4M11/D4M11_Offer`
  - `/Game/DLC4/CampaignData/Missions/D4M11/D4M11_Place_Mission`
  - `/Game/DLC4/CampaignData/Missions/D4M11/D4M11_Prompt`
  - `/Game/DLC4/CampaignData/Missions/D4M11/Level/D4M11_Scenario`
  - `/Game/DLC4/CampaignData/Missions/D4M11/Unlock_D4M11_InstantAction`
  - `/Game/DLC4/CampaignData/Missions/D4M12/D4M12_AutoAcceptMission`
  - `/Game/DLC4/CampaignData/Missions/D4M12/D4M12_AutoAcceptObjective`
  - `/Game/DLC4/CampaignData/Missions/D4M12/D4M12_Completed`
  - `/Game/DLC4/CampaignData/Missions/D4M12/D4M12_Offer`
  - `/Game/DLC4/CampaignData/Missions/D4M12/D4M12_Place_Mission`
  - `/Game/DLC4/CampaignData/Missions/D4M12/D4M12_Prompt`
  - `/Game/DLC4/CampaignData/Missions/D4M12/Level/D4M12_Scenario`
  - `/Game/DLC4/CampaignData/Missions/D4M12/Unlock_D4M12_InstantAction`

### `/Game/DLC4/CampaignData/DLC4_Pt6_Radstadt`
- depth/reason: `2` / `referenced by /Game/DLC4/CampaignData/DLC4_CoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC4/CampaignData/Missions/D4M14/D4M14_SpecialRewards`
- event actions: `22`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC4/CampaignData/DLC4_Pt6_Radstadt`
  - `/Game/DLC4/CampaignData/Missions/D4M12/D4M12_Prompt`
  - `/Game/DLC4/CampaignData/Missions/D4M13/D4M13_AutoAcceptMission`
  - `/Game/DLC4/CampaignData/Missions/D4M13/D4M13_AutoAcceptObjective`
  - `/Game/DLC4/CampaignData/Missions/D4M13/D4M13_Completed`
  - `/Game/DLC4/CampaignData/Missions/D4M13/D4M13_Offer`
  - `/Game/DLC4/CampaignData/Missions/D4M13/D4M13_Place_Mission`
  - `/Game/DLC4/CampaignData/Missions/D4M13/D4M13_Prompt`
  - `/Game/DLC4/CampaignData/Missions/D4M13/D4M13_Scenario`
  - `/Game/DLC4/CampaignData/Missions/D4M13/DLC4_Radstadt_CustomMarket`
  - `/Game/DLC4/CampaignData/Missions/D4M13/TravelTo_D4M13`
  - `/Game/DLC4/CampaignData/Missions/D4M13/Unlock_D4M13_InstantAction`
  - `/Game/DLC4/CampaignData/Missions/D4M14/D4M14_AutoAcceptMission`
  - `/Game/DLC4/CampaignData/Missions/D4M14/D4M14_AutoAcceptObjective`
  - `/Game/DLC4/CampaignData/Missions/D4M14/D4M14_Completed`
  - `/Game/DLC4/CampaignData/Missions/D4M14/D4M14_Offer`
  - `/Game/DLC4/CampaignData/Missions/D4M14/D4M14_Place_Mission`
  - `/Game/DLC4/CampaignData/Missions/D4M14/D4M14_Prompt`
  - `/Game/DLC4/CampaignData/Missions/D4M14/Level/D4M14_Scenario`
  - `/Game/DLC4/CampaignData/Missions/D4M14/Unlock_D4M14_InstantAction`

### `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/DLC4_BountyHunterTransmissions`
- depth/reason: `2` / `referenced by /Game/DLC4/CampaignData/DLC4_CoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `41`
  - `/Game/DLC4/CampaignData/Missions/D4BH/Level/D4BH_Scenario`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/D4BH_Mission_Trigger`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/DLC4_BountyHunterTransmissions`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/Lvl10/D4BH_Completed`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/Lvl10/D4BH_Offer`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/Lvl10/D4BH_Place_Mission`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/Lvl10/D4BH_Prompt`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/Lvl10/D4BH_Reset_Scenario`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/Lvl10/Show_D4BH`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/Lvl10/Unlock_D4BH_InstantAction`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/RivalMercTakedowns/BH_BlackHearts_Takedown`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/RivalMercTakedowns/BH_Blackhearts_TakedownTransmission`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/RivalMercTakedowns/BH_BrionsLegion_Takedown`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/RivalMercTakedowns/BH_BrionsLegion_TakedownTransmission`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/RivalMercTakedowns/BH_EridaniLightHorse_Takedown`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/RivalMercTakedowns/BH_EridaniLightHorse_TakedownTransmission`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/RivalMercTakedowns/BH_GrayDeathLegion_Takedown`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/RivalMercTakedowns/BH_GrayDeathLegion_TakedownTransmission`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/RivalMercTakedowns/BH_HansensRoughRiders_Takedown`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/RivalMercTakedowns/BH_HansensRoughRiders_TakedownTransmission`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/RivalMercTakedowns/BH_KellHounds_Takedown`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/RivalMercTakedowns/BH_KellHounds_TakedownTransmission`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/RivalMercTakedowns/BH_McCarronsArmoredCalvalry_Takedown`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/RivalMercTakedowns/BH_McCarronsArmoredCalvary_TakedownTransmission`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/RivalMercTakedowns/BH_NorthwindHighlanders_Takedown`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/RivalMercTakedowns/BH_NorthwindHighlanders_TakedownTransmission`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/RivalMercTakedowns/BH_WacoRangers_Takedown`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/RivalMercTakedowns/BH_WacoRangers_TakedownTransmission`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/RivalMercTakedowns/BH_WolfsDragoonsTakedown`
  - `/Game/DLC4/CampaignData/RivalMercs/BountyHunterIntel/RivalMercTakedowns/BH_WolfsDragoons_TakedownTransmission`
  - `/Game/DLC4/CampaignData/RivalMercs/Companies/BlackHeartsData`
  - `/Game/DLC4/CampaignData/RivalMercs/Companies/BrionsLegionData`
  - `/Game/DLC4/CampaignData/RivalMercs/Companies/EridaniLightHorseData`
  - `/Game/DLC4/CampaignData/RivalMercs/Companies/GrayDeathLegionData`
  - `/Game/DLC4/CampaignData/RivalMercs/Companies/HansensRoughridersData`
  - `/Game/DLC4/CampaignData/RivalMercs/Companies/KellHoundsData`
  - `/Game/DLC4/CampaignData/RivalMercs/Companies/McCarronsArmoredCavalryData`
  - `/Game/DLC4/CampaignData/RivalMercs/Companies/NorthwindHighlandersData`
  - `/Game/DLC4/CampaignData/RivalMercs/Companies/WacoRangersData`
  - `/Game/DLC4/CampaignData/RivalMercs/Companies/WolfsDragoonsData`
  - `/Game/DLC4/DLC_4`

### `/Game/DLC5/CampaignData/DLC5_Pt0_Dieron`
- depth/reason: `2` / `referenced by /Game/DLC5/CampaignData/DLC5_CoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `2`
  - `/Game/DLC5/CampaignData/Missions/D5_Contact/DLC5_Pt1_Warnings`
  - `/Game/DLC5/CampaignData/PlanetClusterData/DLC5_SetupPlanetaryWarzones`
- event actions: `16`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC5/CampaignData/DLC5_Pt0_Dieron`
  - `/Game/DLC5/CampaignData/Missions/D5_Contact/ArcActions/DLC5_Pt1_CompleteKickoff`
  - `/Game/DLC5/CampaignData/Missions/D5_Contact/ArcActions/DLC5_Pt1_PriorityTransmission`
  - `/Game/DLC5/CampaignData/Missions/D5_Contact/DLC5_Pt1_Kickoff_Prompt`
  - `/Game/DLC5/CampaignData/Missions/D5_Home/ArcAction/D5M14_AutoAcceptMission`
  - `/Game/DLC5/CampaignData/Missions/D5_Home/ArcAction/D5M14_AutoAcceptObjective`
  - `/Game/DLC5/CampaignData/Missions/D5_Home/ArcAction/D5M14_Completed`
  - `/Game/DLC5/CampaignData/Missions/D5_Home/ArcAction/D5M14_Offer`
  - `/Game/DLC5/CampaignData/Missions/D5_Home/ArcAction/D5M14_Place_Mission`
  - `/Game/DLC5/CampaignData/Missions/D5_Home/ArcAction/TravelTo_D5M00`
  - `/Game/DLC5/CampaignData/Missions/D5_Home/ArcAction/Unlock_D5M14_InstantAction`
  - `/Game/DLC5/CampaignData/Missions/D5_Home/D5M14_Prompt`
  - `/Game/DLC5/CampaignData/Missions/D5_Home/D5_Home_Mission_Scenario`
  - `/Game/DLC5/DLC_5`

### `/Game/DLC5/CampaignData/DLC5_Pt1_Vega`
- depth/reason: `2` / `referenced by /Game/DLC5/CampaignData/DLC5_CoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `60`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC5/CampaignData/DLC5_Pt0_Dieron`
  - `/Game/DLC5/CampaignData/DLC5_Pt1_Vega`
  - `/Game/DLC5/CampaignData/DLC5_Vega_CustomMarket`
  - `/Game/DLC5/CampaignData/Missions/D5_Contact/ArcActions/D5M01_AutoAcceptMission`
  - `/Game/DLC5/CampaignData/Missions/D5_Contact/ArcActions/D5M01_AutoAcceptObjective`
  - `/Game/DLC5/CampaignData/Missions/D5_Contact/ArcActions/D5M01_Completed`
  - `/Game/DLC5/CampaignData/Missions/D5_Contact/ArcActions/D5M01_Offer`
  - `/Game/DLC5/CampaignData/Missions/D5_Contact/ArcActions/D5M01_Place_Mission`
  - `/Game/DLC5/CampaignData/Missions/D5_Contact/ArcActions/TravelTo_D5M01`
  - `/Game/DLC5/CampaignData/Missions/D5_Contact/ArcActions/Unlock_D5M01_InstantAction`
  - `/Game/DLC5/CampaignData/Missions/D5_Contact/D5M01_Prompt`
  - `/Game/DLC5/CampaignData/Missions/D5_Contact/D5_Contact_Mission_Scenario`
  - `/Game/DLC5/CampaignData/Missions/D5_Forced/ArcActions/D5M06_AutoAcceptMission`
  - `/Game/DLC5/CampaignData/Missions/D5_Forced/ArcActions/D5M06_AutoAcceptObjective`
  - `/Game/DLC5/CampaignData/Missions/D5_Forced/ArcActions/D5M06_Completed`
  - `/Game/DLC5/CampaignData/Missions/D5_Forced/ArcActions/D5M06_Offer`
  - `/Game/DLC5/CampaignData/Missions/D5_Forced/ArcActions/D5M06_Place_Mission`
  - `/Game/DLC5/CampaignData/Missions/D5_Forced/ArcActions/Show_D5M06`
  - `/Game/DLC5/CampaignData/Missions/D5_Forced/ArcActions/Unlock_D5M06_InstantAction`
  - `/Game/DLC5/CampaignData/Missions/D5_Forced/D5M06_Prompt`
  - `/Game/DLC5/CampaignData/Missions/D5_Forced/D5_Forced_Mission_Scenario`
  - `/Game/DLC5/CampaignData/Missions/D5_Forward/ArcActions/D5M04_AutoAcceptMission`
  - `/Game/DLC5/CampaignData/Missions/D5_Forward/ArcActions/D5M04_AutoAcceptObjective`
  - `/Game/DLC5/CampaignData/Missions/D5_Forward/ArcActions/D5M04_Completed`
  - `/Game/DLC5/CampaignData/Missions/D5_Forward/ArcActions/D5M04_Offer`
  - `/Game/DLC5/CampaignData/Missions/D5_Forward/ArcActions/D5M04_Place_Mission`
  - `/Game/DLC5/CampaignData/Missions/D5_Forward/ArcActions/Show_D5M04`
  - `/Game/DLC5/CampaignData/Missions/D5_Forward/ArcActions/Unlock_D5M04_InstantAction`
  - `/Game/DLC5/CampaignData/Missions/D5_Forward/D5M04_Prompt`
  - `/Game/DLC5/CampaignData/Missions/D5_Forward/D5_Forward_Mission_Scenario`
  - `/Game/DLC5/CampaignData/Missions/D5_Olesko/ArcActions/D5M05_AutoAcceptMission`
  - `/Game/DLC5/CampaignData/Missions/D5_Olesko/ArcActions/D5M05_AutoAcceptObjective`
  - `/Game/DLC5/CampaignData/Missions/D5_Olesko/ArcActions/D5M05_Completed`
  - `/Game/DLC5/CampaignData/Missions/D5_Olesko/ArcActions/D5M05_Offer`
  - `/Game/DLC5/CampaignData/Missions/D5_Olesko/ArcActions/D5M05_Place_Mission`
  - `/Game/DLC5/CampaignData/Missions/D5_Olesko/ArcActions/Show_D5M05`
  - `/Game/DLC5/CampaignData/Missions/D5_Olesko/ArcActions/Unlock_D5M05_InstantAction`
  - `/Game/DLC5/CampaignData/Missions/D5_Olesko/D5M05_Prompt`
  - `/Game/DLC5/CampaignData/Missions/D5_Olesko/D5_Olesko_Mission_Scenario`
  - `/Game/DLC5/CampaignData/Missions/D5_Probing/ArcActions/D5M02_AutoAcceptMission`
  - `/Game/DLC5/CampaignData/Missions/D5_Probing/ArcActions/D5M02_AutoAcceptObjective`
  - `/Game/DLC5/CampaignData/Missions/D5_Probing/ArcActions/D5M02_Completed`
  - `/Game/DLC5/CampaignData/Missions/D5_Probing/ArcActions/D5M02_Offer`
  - `/Game/DLC5/CampaignData/Missions/D5_Probing/ArcActions/D5M02_Place_Mission`
  - `/Game/DLC5/CampaignData/Missions/D5_Probing/ArcActions/Show_D5M02`
  - `/Game/DLC5/CampaignData/Missions/D5_Probing/ArcActions/Unlock_D5M02_InstantAction`
  - `/Game/DLC5/CampaignData/Missions/D5_Probing/D5M02_Prompt`
  - `/Game/DLC5/CampaignData/Missions/D5_Probing/D5_Probing_Mission_Scenario`
  - `/Game/DLC5/CampaignData/Missions/D5_Seek/ArcActions/D5M03_AutoAcceptMission`
  - `/Game/DLC5/CampaignData/Missions/D5_Seek/ArcActions/D5M03_AutoAcceptObjective`
  - `/Game/DLC5/CampaignData/Missions/D5_Seek/ArcActions/D5M03_Completed`
  - `/Game/DLC5/CampaignData/Missions/D5_Seek/ArcActions/D5M03_Offer`
  - `/Game/DLC5/CampaignData/Missions/D5_Seek/ArcActions/D5M03_Place_Mission`
  - `/Game/DLC5/CampaignData/Missions/D5_Seek/ArcActions/Show_D5M03`
  - `/Game/DLC5/CampaignData/Missions/D5_Seek/ArcActions/Unlock_D5M03_InstantAction`
  - `/Game/DLC5/CampaignData/Missions/D5_Seek/D5M03_Prompt`
  - `/Game/DLC5/CampaignData/Missions/D5_Seek/D5_Seek_Mission_Scenario`
  - `/Game/DLC5/DLC_5`

### `/Game/DLC5/CampaignData/DLC5_Pt2_Auldhouse`
- depth/reason: `2` / `referenced by /Game/DLC5/CampaignData/DLC5_CoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `24`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC5/CampaignData/DLC5_Auldhouse_CustomMarket`
  - `/Game/DLC5/CampaignData/DLC5_Pt1_Vega`
  - `/Game/DLC5/CampaignData/DLC5_Pt2_Auldhouse`
  - `/Game/DLC5/CampaignData/Missions/D5_Pickup/ArcActions/D5M07_AutoAcceptMission`
  - `/Game/DLC5/CampaignData/Missions/D5_Pickup/ArcActions/D5M07_AutoAcceptObjective`
  - `/Game/DLC5/CampaignData/Missions/D5_Pickup/ArcActions/D5M07_Completed`
  - `/Game/DLC5/CampaignData/Missions/D5_Pickup/ArcActions/D5M07_Offer`
  - `/Game/DLC5/CampaignData/Missions/D5_Pickup/ArcActions/D5M07_Place_Mission`
  - `/Game/DLC5/CampaignData/Missions/D5_Pickup/ArcActions/TravelTo_D5M07`
  - `/Game/DLC5/CampaignData/Missions/D5_Pickup/ArcActions/Unlock_D5M07_InstantAction`
  - `/Game/DLC5/CampaignData/Missions/D5_Pickup/D5M07_Prompt`
  - `/Game/DLC5/CampaignData/Missions/D5_Pickup/D5_Pickup_Mission_Scenario`
  - `/Game/DLC5/CampaignData/Missions/D5_Raiders/ArcActions/D5M08_AutoAcceptMission`
  - `/Game/DLC5/CampaignData/Missions/D5_Raiders/ArcActions/D5M08_AutoAcceptObjective`
  - `/Game/DLC5/CampaignData/Missions/D5_Raiders/ArcActions/D5M08_Completed`
  - `/Game/DLC5/CampaignData/Missions/D5_Raiders/ArcActions/D5M08_Offer`
  - `/Game/DLC5/CampaignData/Missions/D5_Raiders/ArcActions/D5M08_Place_Mission`
  - `/Game/DLC5/CampaignData/Missions/D5_Raiders/ArcActions/Show_D5M08`
  - `/Game/DLC5/CampaignData/Missions/D5_Raiders/ArcActions/Unlock_D5M08_InstantAction`
  - `/Game/DLC5/CampaignData/Missions/D5_Raiders/D5M08_Prompt`
  - `/Game/DLC5/CampaignData/Missions/D5_Raiders/D5_Raiders_Mission_Scenario`
  - `/Game/DLC5/DLC_5`

### `/Game/DLC5/CampaignData/DLC5_Pt3_Arcturus`
- depth/reason: `2` / `referenced by /Game/DLC5/CampaignData/DLC5_CoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `42`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC5/CampaignData/DLC5_Arcturus_CustomMarket`
  - `/Game/DLC5/CampaignData/DLC5_Pt2_Auldhouse`
  - `/Game/DLC5/CampaignData/DLC5_Pt3_Arcturus`
  - `/Game/DLC5/CampaignData/Missions/D5_Blackout/ArcActions/D5M10_AutoAcceptMission`
  - `/Game/DLC5/CampaignData/Missions/D5_Blackout/ArcActions/D5M10_AutoAcceptObjective`
  - `/Game/DLC5/CampaignData/Missions/D5_Blackout/ArcActions/D5M10_Completed`
  - `/Game/DLC5/CampaignData/Missions/D5_Blackout/ArcActions/D5M10_Offer`
  - `/Game/DLC5/CampaignData/Missions/D5_Blackout/ArcActions/D5M10_Place_Mission`
  - `/Game/DLC5/CampaignData/Missions/D5_Blackout/ArcActions/Show_D5M10`
  - `/Game/DLC5/CampaignData/Missions/D5_Blackout/ArcActions/Unlock_D5M10_InstantAction`
  - `/Game/DLC5/CampaignData/Missions/D5_Blackout/D5M10_Prompt`
  - `/Game/DLC5/CampaignData/Missions/D5_Blackout/D5_Blackout_Mission_Scenario`
  - `/Game/DLC5/CampaignData/Missions/D5_Factory/ArcActions/D5M11_AutoAcceptMission`
  - `/Game/DLC5/CampaignData/Missions/D5_Factory/ArcActions/D5M11_AutoAcceptObjective`
  - `/Game/DLC5/CampaignData/Missions/D5_Factory/ArcActions/D5M11_Completed`
  - `/Game/DLC5/CampaignData/Missions/D5_Factory/ArcActions/D5M11_Offer`
  - `/Game/DLC5/CampaignData/Missions/D5_Factory/ArcActions/D5M11_Place_Mission`
  - `/Game/DLC5/CampaignData/Missions/D5_Factory/ArcActions/Show_D5M11`
  - `/Game/DLC5/CampaignData/Missions/D5_Factory/ArcActions/Unlock_D5M11_InstantAction`
  - `/Game/DLC5/CampaignData/Missions/D5_Factory/D5M11_Prompt`
  - `/Game/DLC5/CampaignData/Missions/D5_Factory/D5_Factory_Mission_Scenario`
  - `/Game/DLC5/CampaignData/Missions/D5_Foothold/ArcActions/D5M09_AutoAcceptMission`
  - `/Game/DLC5/CampaignData/Missions/D5_Foothold/ArcActions/D5M09_AutoAcceptObjective`
  - `/Game/DLC5/CampaignData/Missions/D5_Foothold/ArcActions/D5M09_Completed`
  - `/Game/DLC5/CampaignData/Missions/D5_Foothold/ArcActions/D5M09_Offer`
  - `/Game/DLC5/CampaignData/Missions/D5_Foothold/ArcActions/D5M09_Place_Mission`
  - `/Game/DLC5/CampaignData/Missions/D5_Foothold/ArcActions/TravelTo_D5M09`
  - `/Game/DLC5/CampaignData/Missions/D5_Foothold/ArcActions/Unlock_D5M09_InstantAction`
  - `/Game/DLC5/CampaignData/Missions/D5_Foothold/D5M09_Prompt`
  - `/Game/DLC5/CampaignData/Missions/D5_Foothold/D5_Foothold_Mission_Scenario`
  - `/Game/DLC5/CampaignData/Missions/D5_Military/ArcActions/D5M12_AutoAcceptMission`
  - `/Game/DLC5/CampaignData/Missions/D5_Military/ArcActions/D5M12_AutoAcceptObjective`
  - `/Game/DLC5/CampaignData/Missions/D5_Military/ArcActions/D5M12_Completed`
  - `/Game/DLC5/CampaignData/Missions/D5_Military/ArcActions/D5M12_Offer`
  - `/Game/DLC5/CampaignData/Missions/D5_Military/ArcActions/D5M12_Place_Mission`
  - `/Game/DLC5/CampaignData/Missions/D5_Military/ArcActions/Show_D5M12`
  - `/Game/DLC5/CampaignData/Missions/D5_Military/ArcActions/Unlock_D5M12_InstantAction`
  - `/Game/DLC5/CampaignData/Missions/D5_Military/D5M12_Prompt`
  - `/Game/DLC5/CampaignData/Missions/D5_Military/D5_Military_Mission_Scenario`
  - `/Game/DLC5/DLC_5`

### `/Game/DLC5/CampaignData/DLC5_Pt4_TrollocPrime`
- depth/reason: `2` / `referenced by /Game/DLC5/CampaignData/DLC5_CoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC5/CampaignData/Missions/D5_Knights/D5M15_SpecialRewards`
- event actions: `24`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC5/CampaignData/DLC5_Pt3_Arcturus`
  - `/Game/DLC5/CampaignData/DLC5_Pt4_TrollocPrime`
  - `/Game/DLC5/CampaignData/DLC5_TrollocPrime_CustomMarket`
  - `/Game/DLC5/CampaignData/Missions/D5_Knights/ArcActions/D5M15_AutoAcceptMission`
  - `/Game/DLC5/CampaignData/Missions/D5_Knights/ArcActions/D5M15_AutoAcceptObjective`
  - `/Game/DLC5/CampaignData/Missions/D5_Knights/ArcActions/D5M15_Completed`
  - `/Game/DLC5/CampaignData/Missions/D5_Knights/ArcActions/D5M15_Offer`
  - `/Game/DLC5/CampaignData/Missions/D5_Knights/ArcActions/D5M15_Place_Mission`
  - `/Game/DLC5/CampaignData/Missions/D5_Knights/ArcActions/Show_D5M15`
  - `/Game/DLC5/CampaignData/Missions/D5_Knights/ArcActions/Unlock_D5M15_InstantAction`
  - `/Game/DLC5/CampaignData/Missions/D5_Knights/D5M15_Prompt`
  - `/Game/DLC5/CampaignData/Missions/D5_Knights/D5_Knights_Mission_Scenario`
  - `/Game/DLC5/CampaignData/Missions/D5_Political/ArcActions/D5M13_AutoAcceptMission`
  - `/Game/DLC5/CampaignData/Missions/D5_Political/ArcActions/D5M13_AutoAcceptObjective`
  - `/Game/DLC5/CampaignData/Missions/D5_Political/ArcActions/D5M13_Completed`
  - `/Game/DLC5/CampaignData/Missions/D5_Political/ArcActions/D5M13_Offer`
  - `/Game/DLC5/CampaignData/Missions/D5_Political/ArcActions/D5M13_Place_Mission`
  - `/Game/DLC5/CampaignData/Missions/D5_Political/ArcActions/TravelTo_D5M13`
  - `/Game/DLC5/CampaignData/Missions/D5_Political/ArcActions/Unlock_D5M13_InstantAction`
  - `/Game/DLC5/CampaignData/Missions/D5_Political/D5M13_Prompt`
  - `/Game/DLC5/CampaignData/Missions/D5_Political/D5_Political_Mission_Scenario`
  - `/Game/DLC5/DLC_5`

### `/Game/DLC6/CampaignData/DLC6_Pt0_Galatea`
- depth/reason: `2` / `referenced by /Game/DLC6/CampaignData/DLC6_CoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `2`
  - `/Game/DLC6/CampaignData/DLC6_Pt0_Warnings`
  - `/Game/DLC6/CampaignData/PlanetClusterData/DLC6_SetupPlanetaryWarzones`
- event actions: `25`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC6/CampaignData/CampaignArcActions/DLC6_Pt0_CompleteKickoff`
  - `/Game/DLC6/CampaignData/CampaignArcActions/DLC6_Pt0_PriorityTransmission`
  - `/Game/DLC6/CampaignData/CampaignArcActions/TravelTo_D6M1`
  - `/Game/DLC6/CampaignData/DLC6_Pt0_Galatea`
  - `/Game/DLC6/CampaignData/DLC6_Pt0_KickoffPrompt`
  - `/Game/DLC6/CampaignData/Missions/D6M1/ArcActions/D6M1_AutoAcceptMission`
  - `/Game/DLC6/CampaignData/Missions/D6M1/ArcActions/D6M1_AutoAcceptObjective`
  - `/Game/DLC6/CampaignData/Missions/D6M1/ArcActions/D6M1_Completed`
  - `/Game/DLC6/CampaignData/Missions/D6M1/ArcActions/D6M1_Offer`
  - `/Game/DLC6/CampaignData/Missions/D6M1/ArcActions/D6M1_Place_Mission`
  - `/Game/DLC6/CampaignData/Missions/D6M1/ArcActions/Unlock_D6M1_InstantAction`
  - `/Game/DLC6/CampaignData/Missions/D6M1/D6M1_Prompt`
  - `/Game/DLC6/CampaignData/Missions/D6M1/D6M1_Scenario`
  - `/Game/DLC6/CampaignData/Missions/D6M2/ArcActions/D6M2_AutoAcceptMission`
  - `/Game/DLC6/CampaignData/Missions/D6M2/ArcActions/D6M2_AutoAcceptObjective`
  - `/Game/DLC6/CampaignData/Missions/D6M2/ArcActions/D6M2_Completed`
  - `/Game/DLC6/CampaignData/Missions/D6M2/ArcActions/D6M2_Offer`
  - `/Game/DLC6/CampaignData/Missions/D6M2/ArcActions/D6M2_Place_Mission`
  - `/Game/DLC6/CampaignData/Missions/D6M2/ArcActions/Show_D6M2`
  - `/Game/DLC6/CampaignData/Missions/D6M2/ArcActions/Unlock_D6M2_InstantAction`
  - `/Game/DLC6/CampaignData/Missions/D6M2/D6M2_Prompt`
  - `/Game/DLC6/CampaignData/Missions/D6M2/D6M2_Scenario`
  - `/Game/DLC6/DLC_6`

### `/Game/DLC6/CampaignData/DLC6_Pt1_Hardcore`
- depth/reason: `2` / `referenced by /Game/DLC6/CampaignData/DLC6_CoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `23`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC6/CampaignData/CampaignArcActions/TravelTo_D6M3`
  - `/Game/DLC6/CampaignData/DLC6_Pt0_Galatea`
  - `/Game/DLC6/CampaignData/DLC6_Pt1_Hardcore`
  - `/Game/DLC6/CampaignData/Missions/D6M3/ArcActions/D6M3_AutoAcceptMission`
  - `/Game/DLC6/CampaignData/Missions/D6M3/ArcActions/D6M3_AutoAcceptObjective`
  - `/Game/DLC6/CampaignData/Missions/D6M3/ArcActions/D6M3_Completed`
  - `/Game/DLC6/CampaignData/Missions/D6M3/ArcActions/D6M3_Offer`
  - `/Game/DLC6/CampaignData/Missions/D6M3/ArcActions/D6M3_Place_Mission`
  - `/Game/DLC6/CampaignData/Missions/D6M3/ArcActions/Unlock_D6M3_InstantAction`
  - `/Game/DLC6/CampaignData/Missions/D6M3/D6M3_Prompt`
  - `/Game/DLC6/CampaignData/Missions/D6M3/D6M3_Scenario`
  - `/Game/DLC6/CampaignData/Missions/D6M4/ArcActions/D6M4_AutoAcceptMission`
  - `/Game/DLC6/CampaignData/Missions/D6M4/ArcActions/D6M4_AutoAcceptObjective`
  - `/Game/DLC6/CampaignData/Missions/D6M4/ArcActions/D6M4_Completed`
  - `/Game/DLC6/CampaignData/Missions/D6M4/ArcActions/D6M4_Offer`
  - `/Game/DLC6/CampaignData/Missions/D6M4/ArcActions/D6M4_Place_Mission`
  - `/Game/DLC6/CampaignData/Missions/D6M4/ArcActions/Show_D6M4`
  - `/Game/DLC6/CampaignData/Missions/D6M4/ArcActions/Unlock_D6M4_InstantAction`
  - `/Game/DLC6/CampaignData/Missions/D6M4/D6M4_Prompt`
  - `/Game/DLC6/CampaignData/Missions/D6M4/D6M4_Scenario`
  - `/Game/DLC6/DLC_6`

### `/Game/DLC6/CampaignData/DLC6_Pt2_Solaris`
- depth/reason: `2` / `referenced by /Game/DLC6/CampaignData/DLC6_CoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/DLC6/CampaignData/DLC6_Rewards`
- event actions: `32`
  - `/Game/Campaign/CampaignArcs/_common/CustomTriggers/HasNoMissionsReady`
  - `/Game/DLC2/CampaignData/_CampaignStructsAndScripts/AbandonContractTracker_ArcAction`
  - `/Game/DLC6/CampaignData/CampaignArcActions/TravelTo_D6M5`
  - `/Game/DLC6/CampaignData/DLC6_Pt1_Hardcore`
  - `/Game/DLC6/CampaignData/DLC6_Pt2_Solaris`
  - `/Game/DLC6/CampaignData/Missions/D6M5/ArcActions/D6M5_AutoAcceptMission`
  - `/Game/DLC6/CampaignData/Missions/D6M5/ArcActions/D6M5_AutoAcceptObjective`
  - `/Game/DLC6/CampaignData/Missions/D6M5/ArcActions/D6M5_Completed`
  - `/Game/DLC6/CampaignData/Missions/D6M5/ArcActions/D6M5_Offer`
  - `/Game/DLC6/CampaignData/Missions/D6M5/ArcActions/D6M5_Place_Mission`
  - `/Game/DLC6/CampaignData/Missions/D6M5/ArcActions/Unlock_D6M5_InstantAction`
  - `/Game/DLC6/CampaignData/Missions/D6M5/D6M5_Prompt`
  - `/Game/DLC6/CampaignData/Missions/D6M5/D6M5_Scenario`
  - `/Game/DLC6/CampaignData/Missions/D6M6/ArcActions/D6M6_AutoAcceptMission`
  - `/Game/DLC6/CampaignData/Missions/D6M6/ArcActions/D6M6_AutoAcceptObjective`
  - `/Game/DLC6/CampaignData/Missions/D6M6/ArcActions/D6M6_Completed`
  - `/Game/DLC6/CampaignData/Missions/D6M6/ArcActions/D6M6_Offer`
  - `/Game/DLC6/CampaignData/Missions/D6M6/ArcActions/D6M6_Place_Mission`
  - `/Game/DLC6/CampaignData/Missions/D6M6/ArcActions/Show_D6M6`
  - `/Game/DLC6/CampaignData/Missions/D6M6/ArcActions/Unlock_D6M6_InstantAction`
  - `/Game/DLC6/CampaignData/Missions/D6M6/D6M6_Prompt`
  - `/Game/DLC6/CampaignData/Missions/D6M6/D6M6_Scenario`
  - `/Game/DLC6/CampaignData/Missions/D6M7/ArcActions/D6M7_AutoAcceptMission`
  - `/Game/DLC6/CampaignData/Missions/D6M7/ArcActions/D6M7_AutoAcceptObjective`
  - `/Game/DLC6/CampaignData/Missions/D6M7/ArcActions/D6M7_Completed`
  - `/Game/DLC6/CampaignData/Missions/D6M7/ArcActions/D6M7_Offer`
  - `/Game/DLC6/CampaignData/Missions/D6M7/ArcActions/D6M7_Place_Mission`
  - `/Game/DLC6/CampaignData/Missions/D6M7/ArcActions/Show_D6M7`
  - `/Game/DLC6/CampaignData/Missions/D6M7/ArcActions/Unlock_D6M7_InstantAction`
  - `/Game/DLC6/CampaignData/Missions/D6M7/D6M7_Prompt`
  - `/Game/DLC6/CampaignData/Missions/D6M7/D6M7_Scenario`
  - `/Game/DLC6/DLC_6`

### `/Game/DLC6/CampaignData/PlanetClusterData/DLC6_SetupPlanetaryWarzones`
- depth/reason: `2` / `referenced by /Game/DLC6/CampaignData/DLC6_CoreCampaign`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `4`
  - `/Game/DLC6/CampaignData/PlanetClusterData/Place_GalateaZone`
  - `/Game/DLC6/CampaignData/PlanetClusterData/Place_HardcoreZone`
  - `/Game/DLC6/CampaignData/PlanetClusterData/Place_SolarisZone`
  - `/Game/DLC6/DLC_6`

### `/Game/Campaign/CampaignArcs/Regions/MercStars/Place_HerotitusZone`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/Regions/MercStars/Place_MercStars_Arc`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/HerotitusZone/HerotitusZone_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/HerotitusZone/HerotitusZone_ClusterAsset.HerotitusZone_ClusterAsset' (0x000001BA89CC60C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'HerotitusZone_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/HerotitusZone/HerotitusZone_ClusterAsset.HerotitusZone_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/HerotitusZone/HerotitusZone_ClusterAsset.HerotitusZone_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/HerotitusZone/HerotitusZone_ClusterAsset.HerotitusZone_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/HerotitusZone/HerotitusZone_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/HerotitusZone/HerotitusZone_ClusterAsset.HerotitusZone_ClusterAsset' (0x000001BA89CC60C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB820A1B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "HerotitusZone_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB820A1B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "HerotitusZone_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB820A110) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB820A110) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/MercStars/Place_Outreach_Arc`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/Regions/MercStars/Place_MercStars_Arc`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `1`
  - `/Game/Campaign/CampaignArcs/Regions/MercStars/Place_Outreach`

### `/Game/Campaign/CampaignArcs/Regions/MercStars/Place_WesterhandZone`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/Regions/MercStars/Place_MercStars_Arc`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/WesterhandZone/WesterhandZone_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/WesterhandZone/WesterhandZone_ClusterAsset.WesterhandZone_ClusterAsset' (0x000001BA9C354180) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'WesterhandZone_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/WesterhandZone/WesterhandZone_ClusterAsset.WesterhandZone_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/WesterhandZone/WesterhandZone_ClusterAsset.WesterhandZone_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/WesterhandZone/WesterhandZone_ClusterAsset.WesterhandZone_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/WesterhandZone/WesterhandZone_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/WesterhandZone/WesterhandZone_ClusterAsset.WesterhandZone_ClusterAsset' (0x000001BA9C354180) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BA36FA5530) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "WesterhandZone_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BA36FA5530) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "WesterhandZone_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BA36FA5490) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BA36FA5490) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Davion/Career_ACunningDecoy/D10_ACunningDecoy`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_11_12/Common_D_11_12`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `7`
  - `/Game/Campaign/Clusters/ShippingRoute/ShippingRoute`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/Career_ACunningDecoy/ChainCunningDecoy_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/Career_ACunningDecoy/D10_ACunningDecoy`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/Career_ACunningDecoy/D10_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/Career_ACunningDecoy/GenerateCunningDecoy_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/Career_ACunningDecoy/GenerateCunningDecoy_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/Career_ACunningDecoy/ShowCunningDecoySideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/D_11_12/Place_D_11_12`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_11_12/Common_D_11_12`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_11_12/D_11_12_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_11_12/D_11_12_ClusterAsset.D_11_12_ClusterAsset' (0x000001BA9C3542C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'D_11_12_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/D_11_12/D_11_12_ClusterAsset.D_11_12_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/D_11_12/D_11_12_ClusterAsset.D_11_12_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/D_11_12/D_11_12_ClusterAsset.D_11_12_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/D_11_12/D_11_12_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_11_12/D_11_12_ClusterAsset.D_11_12_ClusterAsset' (0x000001BA9C3542C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BA36FA52B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_11_12_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BA36FA52B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_11_12_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BA36FA5210) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BA36FA5210) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Davion/D6/AnIntriguingOffer/D8_IntriguingOffer`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_12_13/Common_D_12_13`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `6`
  - `/Game/Campaign/Clusters/Kurita-DavionFrontLine/KuritaDavion`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/AnIntriguingOffer/D8_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/AnIntriguingOffer/GenerateIntriguing_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/AnIntriguingOffer/OfferIntriguing_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/DefenseSupportDavion/D7_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/DefenseSupportDavion/D7_Prompt_2`

### `/Game/DLC1/CareerMode/Sidequests/Davion/D6/BackChannelDeal/D9_Backchannel`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_12_13/Common_D_12_13`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `6`
  - `/Game/Campaign/Clusters/Kurita-DavionFrontLine/KuritaDavion`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/BackChannelDeal/D9_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/BackChannelDeal/GenerateBackchannel_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/BackChannelDeal/OfferBackchannel_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/InvasionSupportKurita/D6_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/InvasionSupportKurita/D6_Prompt_2`

### `/Game/DLC1/CareerMode/Sidequests/Davion/D6/DefenseSupportDavion/D7_DefenseDavion`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_12_13/Common_D_12_13`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `9`
  - `/Game/Campaign/Clusters/Kurita-DavionFrontLine/KuritaDavion`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/AnIntriguingOffer/D8_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/DefenseSupportDavion/D7_DefenseDavion`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/DefenseSupportDavion/D7_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/DefenseSupportDavion/GenerateDefenseDavion_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/DefenseSupportDavion/GenerateDefenseDavion_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/DefenseSupportDavion/OfferDefenseDavionPrimpt2_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/DefenseSupportDavion/ShowDefenseDavionSideQuest_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/InvasionSupportKurita/D6_Prompt`

### `/Game/DLC1/CareerMode/Sidequests/Davion/D6/InvasionSupportKurita/D6_InvasionKurita`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_12_13/Common_D_12_13`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `10`
  - `/Game/Campaign/Clusters/Kurita-DavionFrontLine/KuritaDavion`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/BackChannelDeal/D9_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/DefenseSupportDavion/D7_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/DefenseSupportDavion/D7_Prompt_2`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/InvasionSupportKurita/D6_InvasionKurita`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/InvasionSupportKurita/D6_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/InvasionSupportKurita/GenerateInvasionKurita_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/InvasionSupportKurita/GenerateInvasionKurita_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/InvasionSupportKurita/OfferInvasionKuritaPrompt2_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D6/InvasionSupportKurita/ShowInvasionKuritaSideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/DLC1_VTR`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_12_13/Common_D_12_13`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `32`
  - `/Game/Campaign/Clusters/Kurita-DavionFrontLine/KuritaDavion`
  - `/Game/DLC1/CareerMode/Clusters/S_10_12/CareerCluster_6`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/CompleteVTR_4_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/DLC1_HM2_GeneratedMission_1_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/DLC1_HM2_GeneratedMission_2_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/DLC1_HM2_GeneratedMission_3_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/DLC1_VTR`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/DLC_Victor_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/DLC_Victor_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/DLC_Victor_Prompt3`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/DLC_Victor_Prompt4`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/OfferVTR_1_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/OfferVTR_2_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/OfferVTR_3_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/OfferVTR_4_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/Place_Authored_VTR`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/Reset_Scenario_VTR`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/ShowVTRSideQuest_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/Unlock_DLC1_VTR_01_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/Unlock_DLC1_VTR_02_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/Unlock_DLC1_VTR_03_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/Unlock_DLC1_VTR_04_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/VictorMission_1/VTR1_Complete_AuthoredScenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/VictorMission_1/VTR1_Place_Authored_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/VictorMission_1/VTR1_Reset_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/VictorMission_2/VTR2_Complete_AuthoredScenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/VictorMission_2/VTR2_Place_Authored_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/VictorMission_2/VTR2_Reset_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/VictorMission_3/VTR3_Complete_AuthoredScenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Victor/VictorMission_3/VTR3_Place_Authored_Scenario`
  - `/Game/DLC1/DLC_1`
  - `/Game/DLC1/Levels/AuthoredMissions/D1M_Fog/D1M_Fog_Scenario`

### `/Game/DLC1/CareerMode/Warzones/D_12_13/Place_D_12_13`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_12_13/Common_D_12_13`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_12_13/D_12_13_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_12_13/D_12_13_ClusterAsset.D_12_13_ClusterAsset' (0x000001BA9C354540) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'D_12_13_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/D_12_13/D_12_13_ClusterAsset.D_12_13_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/D_12_13/D_12_13_ClusterAsset.D_12_13_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/D_12_13/D_12_13_ClusterAsset.D_12_13_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/D_12_13/D_12_13_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_12_13/D_12_13_ClusterAsset.D_12_13_ClusterAsset' (0x000001BA9C354540) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830C770) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_12_13_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830C770) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_12_13_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830C6D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830C6D0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/D_15/Place_D_15`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_15/Common_D_15`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_15/D_15_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_15/D_15_ClusterAsset.D_15_ClusterAsset' (0x000001BA9C357C40) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'D_15_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/D_15/D_15_ClusterAsset.D_15_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/D_15/D_15_ClusterAsset.D_15_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/D_15/D_15_ClusterAsset.D_15_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/D_15/D_15_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_15/D_15_ClusterAsset.D_15_ClusterAsset' (0x000001BA9C357C40) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830D8F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_15_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830D8F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_15_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830D850) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830D850) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Davion/Career_ArmedRobery/D1_ArmedRobbery`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_1_2/Common_D_1_2`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `5`
  - `/Game/Campaign/Clusters/MercenaryRow/MercenaryRow`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/Career_ArmedRobery/D1_ArmedRobbery`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/Career_ArmedRobery/D1_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/Career_ArmedRobery/GenerateArmedRobery_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/Career_ArmedRobery/ShowArmedRobery_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/D_1_2/Place_D_1_2`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_1_2/Common_D_1_2`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_1_2/D_1_2_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_1_2/D_1_2_ClusterAsset.D_1_2_ClusterAsset' (0x000001BA9C320180) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'D_1_2_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/D_1_2/D_1_2_ClusterAsset.D_1_2_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/D_1_2/D_1_2_ClusterAsset.D_1_2_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/D_1_2/D_1_2_ClusterAsset.D_1_2_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/D_1_2/D_1_2_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_1_2/D_1_2_ClusterAsset.D_1_2_ClusterAsset' (0x000001BA9C320180) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830C4F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_1_2_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830C4F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_1_2_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830C450) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830C450) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/D_2_3/Place_D_2_3`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_2_3/Common_D_2_3`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_2_3/D_2_3_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_2_3/D_2_3_ClusterAsset.D_2_3_ClusterAsset' (0x000001BA9C320400) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'D_2_3_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/D_2_3/D_2_3_ClusterAsset.D_2_3_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/D_2_3/D_2_3_ClusterAsset.D_2_3_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/D_2_3/D_2_3_ClusterAsset.D_2_3_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/D_2_3/D_2_3_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_2_3/D_2_3_ClusterAsset.D_2_3_ClusterAsset' (0x000001BA9C320400) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830CC70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_2_3_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830CC70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_2_3_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830CBD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830CBD0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/D_2_4/Place_D_2_4`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_2_4/Common_D_2_4`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_2_4/D_2_4_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_2_4/D_2_4_ClusterAsset.D_2_4_ClusterAsset' (0x000001BA9C320680) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'D_2_4_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/D_2_4/D_2_4_ClusterAsset.D_2_4_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/D_2_4/D_2_4_ClusterAsset.D_2_4_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/D_2_4/D_2_4_ClusterAsset.D_2_4_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/D_2_4/D_2_4_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_2_4/D_2_4_ClusterAsset.D_2_4_ClusterAsset' (0x000001BA9C320680) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830D2B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_2_4_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830D2B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_2_4_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830D210) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830D210) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/D_3_5/Place_D_3_5`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_3_5/Common_D_3_5`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_3_5/D_3_5_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_3_5/D_3_5_ClusterAsset.D_3_5_ClusterAsset' (0x000001BA9C3207C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'D_3_5_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/D_3_5/D_3_5_ClusterAsset.D_3_5_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/D_3_5/D_3_5_ClusterAsset.D_3_5_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/D_3_5/D_3_5_ClusterAsset.D_3_5_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/D_3_5/D_3_5_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_3_5/D_3_5_ClusterAsset.D_3_5_ClusterAsset' (0x000001BA9C3207C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830E2F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_3_5_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830E2F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_3_5_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830E250) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830E250) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Davion/D2/Career_PickingUpThePieces/D2_PickingUpThePieces`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_3_6/Common_D_3_6`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `9`
  - `/Game/Campaign/Clusters/InfernosWake/InfernosWake`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D2/Career_PickingUpThePieces/D2_PickingUpThePieces`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D2/Career_PickingUpThePieces/D2_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D2/Career_PickingUpThePieces/GeneratePickingUpThePieces_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D2/Career_PickingUpThePieces/GeneratePickingUpThePieces_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D2/Career_PickingUpThePieces/OfferPickingUpThePiecesPrompt2_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D2/Career_PickingUpThePieces/ShowPickingUpThePiecesSideQuest_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D2/Career_PickingUpTheScraps/D3_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D2/Career_PickingUpTheScraps/D3_Prompt_2`

### `/Game/DLC1/CareerMode/Sidequests/Davion/D2/Career_PickingUpTheScraps/D3_PickingUpScraps`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_3_6/Common_D_3_6`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `9`
  - `/Game/Campaign/Clusters/InfernosWake/InfernosWake`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D2/Career_PickingUpThePieces/D2_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D2/Career_PickingUpThePieces/D2_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D2/Career_PickingUpTheScraps/D3_PickingUpScraps`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D2/Career_PickingUpTheScraps/D3_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D2/Career_PickingUpTheScraps/GeneratePickingUpScraps_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D2/Career_PickingUpTheScraps/GeneratePickingUpScraps_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D2/Career_PickingUpTheScraps/OfferPickingUpScrapsPrompt2_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D2/Career_PickingUpTheScraps/ShowPickingUpScrapsSideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/D_3_6/Place_D_3_6`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_3_6/Common_D_3_6`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_3_6/D_3_6_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_3_6/D_3_6_ClusterAsset.D_3_6_ClusterAsset' (0x000001BA9C320900) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'D_3_6_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/D_3_6/D_3_6_ClusterAsset.D_3_6_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/D_3_6/D_3_6_ClusterAsset.D_3_6_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/D_3_6/D_3_6_ClusterAsset.D_3_6_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/D_3_6/D_3_6_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_3_6/D_3_6_ClusterAsset.D_3_6_ClusterAsset' (0x000001BA9C320900) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830E7F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_3_6_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830E7F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_3_6_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830E750) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830E750) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/D_4_6/Place_D_4_6`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_4_6/Common_D_4_6`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_4_6/D_4_6_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_4_6/D_4_6_ClusterAsset.D_4_6_ClusterAsset' (0x000001BA9C320B80) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'D_4_6_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/D_4_6/D_4_6_ClusterAsset.D_4_6_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/D_4_6/D_4_6_ClusterAsset.D_4_6_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/D_4_6/D_4_6_ClusterAsset.D_4_6_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/D_4_6/D_4_6_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_4_6/D_4_6_ClusterAsset.D_4_6_ClusterAsset' (0x000001BA9C320B80) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830ECF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_4_6_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830ECF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_4_6_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830EC50) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830EC50) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/D_5_7/Place_D_5_7`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_5_7/Common_D_5_7`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_5_7/D_5_7_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_5_7/D_5_7_ClusterAsset.D_5_7_ClusterAsset' (0x000001BA9C320E00) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'D_5_7_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/D_5_7/D_5_7_ClusterAsset.D_5_7_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/D_5_7/D_5_7_ClusterAsset.D_5_7_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/D_5_7/D_5_7_ClusterAsset.D_5_7_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/D_5_7/D_5_7_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_5_7/D_5_7_ClusterAsset.D_5_7_ClusterAsset' (0x000001BA9C320E00) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830DDF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_5_7_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830DDF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_5_7_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830DD50) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830DD50) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/D_5_8/Place_D_5_8`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_5_8/Common_D_5_8`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_5_8/D_5_8_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_5_8/D_5_8_ClusterAsset.D_5_8_ClusterAsset' (0x000001BA9C321580) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'D_5_8_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/D_5_8/D_5_8_ClusterAsset.D_5_8_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/D_5_8/D_5_8_ClusterAsset.D_5_8_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/D_5_8/D_5_8_ClusterAsset.D_5_8_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/D_5_8/D_5_8_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_5_8/D_5_8_ClusterAsset.D_5_8_ClusterAsset' (0x000001BA9C321580) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830EF70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_5_8_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830EF70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_5_8_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830EED0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830EED0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/D_6_7/Place_D_6_7`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_6_7/Common_D_6_7`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_6_7/D_6_7_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_6_7/D_6_7_ClusterAsset.D_6_7_ClusterAsset' (0x000001BA9C3216C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'D_6_7_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/D_6_7/D_6_7_ClusterAsset.D_6_7_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/D_6_7/D_6_7_ClusterAsset.D_6_7_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/D_6_7/D_6_7_ClusterAsset.D_6_7_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/D_6_7/D_6_7_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_6_7/D_6_7_ClusterAsset.D_6_7_ClusterAsset' (0x000001BA9C3216C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830F470) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_6_7_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB830F470) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_6_7_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830F3D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB830F3D0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/D_6_8/Place_D_6_8`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_6_8/Common_D_6_8`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_6_8/D_6_8_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_6_8/D_6_8_ClusterAsset.D_6_8_ClusterAsset' (0x000001BA9C321940) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'D_6_8_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/D_6_8/D_6_8_ClusterAsset.D_6_8_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/D_6_8/D_6_8_ClusterAsset.D_6_8_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/D_6_8/D_6_8_ClusterAsset.D_6_8_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/D_6_8/D_6_8_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_6_8/D_6_8_ClusterAsset.D_6_8_ClusterAsset' (0x000001BA9C321940) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8097FB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_6_8_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8097FB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_6_8_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8097F10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8097F10) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Davion/D4/FrontlineSupportDavion/D4_FrontlineDavion`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_7_10/Common_D_7_10`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `8`
  - `/Game/Campaign/Clusters/Davion-KuritaFrontline/DavionKurita_1`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D4/FrontlineSupportDavion/ChainFrontlineDavion_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D4/FrontlineSupportDavion/D4_FrontlineDavion`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D4/FrontlineSupportDavion/D4_Prompt1`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D4/FrontlineSupportDavion/GenerateFrontlineDavion_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D4/FrontlineSupportDavion/GenerateFrontlineDavion_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D4/FrontlineSupportDavion/ShowFrontlineDavionSideQuest_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D4/FrontlineSupportKurita/D5_Prompt1`

### `/Game/DLC1/CareerMode/Sidequests/Davion/D4/FrontlineSupportKurita/D5_FrontlineKurita`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_7_10/Common_D_7_10`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `8`
  - `/Game/Campaign/Clusters/Davion-KuritaFrontline/DavionKurita_1`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D4/FrontlineSupportDavion/D4_Prompt1`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D4/FrontlineSupportKurita/ChainFrontlineKurita_ArcActio_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D4/FrontlineSupportKurita/D5_FrontlineKurita`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D4/FrontlineSupportKurita/D5_Prompt1`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D4/FrontlineSupportKurita/GenerateFrontlineKurita_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D4/FrontlineSupportKurita/GenerateFrontlineKurita_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Davion/D4/FrontlineSupportKurita/ShowFrontlineKuritaSideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/D_7_10/Place_D_7_10`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/D_7_10/Common_D_7_10`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_7_10/D_7_10_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_7_10/D_7_10_ClusterAsset.D_7_10_ClusterAsset' (0x000001BA9C321D00) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'D_7_10_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/D_7_10/D_7_10_ClusterAsset.D_7_10_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/D_7_10/D_7_10_ClusterAsset.D_7_10_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/D_7_10/D_7_10_ClusterAsset.D_7_10_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/D_7_10/D_7_10_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/D_7_10/D_7_10_ClusterAsset.D_7_10_ClusterAsset' (0x000001BA9C321D00) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8094DB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_7_10_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8094DB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "D_7_10_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8094D10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8094D10) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Kurita/K5/PeasantUprising/K6_PeasantUprising`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/K_12_13/Common_K_12_13`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `6`
  - `/Game/Campaign/Clusters/Rogue/RogueSystems`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K5/PeasantUprising/GeneratePeasantUprising_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K5/PeasantUprising/K6_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K5/PeasantUprising/OfferPeasantUprising_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K5/TheChairmen/K5_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K5/TheChairmen/K5_Prompt3`

### `/Game/DLC1/CareerMode/Sidequests/Kurita/K5/TheChairmen/K5_Chairmen`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/K_12_13/Common_K_12_13`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `11`
  - `/Game/Campaign/Clusters/Rogue/RogueSystems`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K5/PeasantUprising/K6_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K5/TheChairmen/GenerateChairmen_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K5/TheChairmen/GenerateChairmen_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K5/TheChairmen/GenerateChairmen_03_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K5/TheChairmen/K5_Chairmen`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K5/TheChairmen/K5_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K5/TheChairmen/K5_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K5/TheChairmen/OfferChairmenPrompt2_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K5/TheChairmen/OfferChairmenPrompt3_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K5/TheChairmen/ShowChairmenSideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/K_12_13/Place_K_12_13`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/K_12_13/Common_K_12_13`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_12_13/K_12_13_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_12_13/K_12_13_ClusterAsset.K_12_13_ClusterAsset' (0x000001BA9C321F80) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'K_12_13_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/K_12_13/K_12_13_ClusterAsset.K_12_13_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/K_12_13/K_12_13_ClusterAsset.K_12_13_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/K_12_13/K_12_13_ClusterAsset.K_12_13_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/K_12_13/K_12_13_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_12_13/K_12_13_ClusterAsset.K_12_13_ClusterAsset' (0x000001BA9C321F80) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8094630) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_12_13_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8094630) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_12_13_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8094590) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8094590) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/K_13_14/Place_K_13_14`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/K_13_14/Common_K_13_14`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_13_14/K_13_14_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_13_14/K_13_14_ClusterAsset.K_13_14_ClusterAsset' (0x000001BA9C322200) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'K_13_14_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/K_13_14/K_13_14_ClusterAsset.K_13_14_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/K_13_14/K_13_14_ClusterAsset.K_13_14_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/K_13_14/K_13_14_ClusterAsset.K_13_14_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/K_13_14/K_13_14_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_13_14/K_13_14_ClusterAsset.K_13_14_ClusterAsset' (0x000001BA9C322200) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8094B30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_13_14_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8094B30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_13_14_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8094A90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8094A90) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_EchoesOfThePast/K3_EchoesOfThePast`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/K_1_2/Common_K_1_2`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `7`
  - `/Game/Campaign/Clusters/TheGraveyard/DropshipGraveyard`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_EchoesOfThePast/ChainEchoesOfThePast_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_EchoesOfThePast/GenerateEchoesOfThePast_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_EchoesOfThePast/GenerateEchoesOfThePast_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_EchoesOfThePast/K3_EchoesOfThePast`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_EchoesOfThePast/K3_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_EchoesOfThePast/ShowEchoesOfThePastSideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/K_1_2/Place_K_1_2`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/K_1_2/Common_K_1_2`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_1_2/K_1_2_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_1_2/K_1_2_ClusterAsset.K_1_2_ClusterAsset' (0x000001BA9C322C00) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'K_1_2_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/K_1_2/K_1_2_ClusterAsset.K_1_2_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/K_1_2/K_1_2_ClusterAsset.K_1_2_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/K_1_2/K_1_2_ClusterAsset.K_1_2_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/K_1_2/K_1_2_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_1_2/K_1_2_ClusterAsset.K_1_2_ClusterAsset' (0x000001BA9C322C00) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8096CF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_1_2_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8096CF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_1_2_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8096C50) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8096C50) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_CharityCase/K2_CharityCase`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/K_2_3/Common_K_2_3`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `9`
  - `/Game/Campaign/Clusters/DroughtWorlds/DroughtWorlds`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_CharityCase/ChainCharityCase_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_CharityCase/GenerateCharityCase_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_CharityCase/GenerateCharityCase_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_CharityCase/GenerateCharityCase_03_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_CharityCase/K2_CharityCase`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_CharityCase/K2_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_CharityCase/OfferCharityCasePrompt2_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_CharityCase/ShowCharityCaseSideQeust_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/K_2_3/Place_K_2_3`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/K_2_3/Common_K_2_3`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_2_3/K_2_3_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_2_3/K_2_3_ClusterAsset.K_2_3_ClusterAsset' (0x000001BA9C322E80) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'K_2_3_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/K_2_3/K_2_3_ClusterAsset.K_2_3_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/K_2_3/K_2_3_ClusterAsset.K_2_3_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/K_2_3/K_2_3_ClusterAsset.K_2_3_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/K_2_3/K_2_3_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_2_3/K_2_3_ClusterAsset.K_2_3_ClusterAsset' (0x000001BA9C322E80) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB80970B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_2_3_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB80970B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_2_3_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8097010) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8097010) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/K_3_4/Place_K_3_4`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/K_3_4/Common_K_3_4`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_3_4/K_3_4_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_3_4/K_3_4_ClusterAsset.K_3_4_ClusterAsset' (0x000001BA9C323100) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'K_3_4_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/K_3_4/K_3_4_ClusterAsset.K_3_4_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/K_3_4/K_3_4_ClusterAsset.K_3_4_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/K_3_4/K_3_4_ClusterAsset.K_3_4_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/K_3_4/K_3_4_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_3_4/K_3_4_ClusterAsset.K_3_4_ClusterAsset' (0x000001BA9C323100) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8095DF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_3_4_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8095DF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_3_4_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8095D50) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8095D50) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/K_3_5/Place_K_3_5`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/K_3_5/Common_K_3_5`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_3_5/K_3_5_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_3_5/K_3_5_ClusterAsset.K_3_5_ClusterAsset' (0x000001BA9C323240) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'K_3_5_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/K_3_5/K_3_5_ClusterAsset.K_3_5_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/K_3_5/K_3_5_ClusterAsset.K_3_5_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/K_3_5/K_3_5_ClusterAsset.K_3_5_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/K_3_5/K_3_5_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_3_5/K_3_5_ClusterAsset.K_3_5_ClusterAsset' (0x000001BA9C323240) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8097970) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_3_5_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8097970) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_3_5_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB80978D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB80978D0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/StoryCluster_05/ComstarBullies/Child_SC05_Q8`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/K_3_5_1/Common_K_3_5_1`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `1`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_05/ComstarBullies/SC05_Q8_H1_Arc`
- event actions: `7`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_04/BreakTheSiege/SC04_Q7_Prompt`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_05/ComstarBullies/Complete_SC05_Q8`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_05/ComstarBullies/Offer_SC05_Q8`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_05/ComstarBullies/Place_SC05_Q8`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_05/ComstarBullies/SC05_Q8_H1_Arc`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_05/ComstarBullies/SC05_Q8_Prompt`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_05/ComstarBullies/SC05_Q8_Scenario`

### `/Game/DLC1/CareerMode/Warzones/K_3_5_1/Place_K_3_5_1`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/K_3_5_1/Common_K_3_5_1`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_3_5_1/K_3_5_1_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_3_5_1/K_3_5_1_ClusterAsset.K_3_5_1_ClusterAsset' (0x000001BA9C323380) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'K_3_5_1_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/K_3_5_1/K_3_5_1_ClusterAsset.K_3_5_1_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/K_3_5_1/K_3_5_1_ClusterAsset.K_3_5_1_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/K_3_5_1/K_3_5_1_ClusterAsset.K_3_5_1_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/K_3_5_1/K_3_5_1_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_3_5_1/K_3_5_1_ClusterAsset.K_3_5_1_ClusterAsset' (0x000001BA9C323380) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8097E70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_3_5_1_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8097E70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_3_5_1_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8097DD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8097DD0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/K_4_5/Place_K_4_5`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/K_4_5/Common_K_4_5`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_4_5/K_4_5_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_4_5/K_4_5_ClusterAsset.K_4_5_ClusterAsset' (0x000001BA9C323600) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'K_4_5_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/K_4_5/K_4_5_ClusterAsset.K_4_5_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/K_4_5/K_4_5_ClusterAsset.K_4_5_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/K_4_5/K_4_5_ClusterAsset.K_4_5_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/K_4_5/K_4_5_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_4_5/K_4_5_ClusterAsset.K_4_5_ClusterAsset' (0x000001BA9C323600) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB80976F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_4_5_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB80976F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_4_5_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8097650) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8097650) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_PirateHunt/K1_PirateHunt`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/K_5_6/Common_K_5_6`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `10`
  - `/Game/Campaign/Clusters/DraconisBadlands/KuritanBadlands`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_PirateHunt/GeneratePirateHunt_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_PirateHunt/GeneratePirateHunt_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_PirateHunt/GeneratePirateHunt_03_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_PirateHunt/K1_PirateHunt`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_PirateHunt/K1_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_PirateHunt/K1_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_PirateHunt/OfferPirateHuntPrompt2_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_PirateHunt/OfferPirateHuntPrompt3_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_PirateHunt/ShowPirateHuntSideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/K_5_6/Place_K_5_6`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/K_5_6/Common_K_5_6`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_5_6/K_5_6_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_5_6/K_5_6_ClusterAsset.K_5_6_ClusterAsset' (0x000001BA9C323740) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'K_5_6_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/K_5_6/K_5_6_ClusterAsset.K_5_6_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/K_5_6/K_5_6_ClusterAsset.K_5_6_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/K_5_6/K_5_6_ClusterAsset.K_5_6_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/K_5_6/K_5_6_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_5_6/K_5_6_ClusterAsset.K_5_6_ClusterAsset' (0x000001BA9C323740) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8095670) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_5_6_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8095670) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_5_6_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB80955D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB80955D0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/K_6_7/Place_K_6_7`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/K_6_7/Common_K_6_7`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_6_7/K_6_7_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_6_7/K_6_7_ClusterAsset.K_6_7_ClusterAsset' (0x000001BA9C3239C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'K_6_7_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/K_6_7/K_6_7_ClusterAsset.K_6_7_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/K_6_7/K_6_7_ClusterAsset.K_6_7_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/K_6_7/K_6_7_ClusterAsset.K_6_7_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/K_6_7/K_6_7_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_6_7/K_6_7_ClusterAsset.K_6_7_ClusterAsset' (0x000001BA9C3239C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB80962F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_6_7_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB80962F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_6_7_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8096250) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8096250) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/K_6_8/Place_K_6_8`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/K_6_8/Common_K_6_8`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_6_8/K_6_8_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_6_8/K_6_8_ClusterAsset.K_6_8_ClusterAsset' (0x000001BA9C323C40) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'K_6_8_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/K_6_8/K_6_8_ClusterAsset.K_6_8_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/K_6_8/K_6_8_ClusterAsset.K_6_8_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/K_6_8/K_6_8_ClusterAsset.K_6_8_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/K_6_8/K_6_8_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_6_8/K_6_8_ClusterAsset.K_6_8_ClusterAsset' (0x000001BA9C323C40) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8013AB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_6_8_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8013AB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_6_8_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8013A10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8013A10) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_RiseOfTheBlackDragon/K4_RiseOfBlackDragon`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/K_7_9/Common_K_7_9`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `10`
  - `/Game/Campaign/Clusters/Lower-ClassKuritanWorlds/LowerClassWorlds`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_RiseOfTheBlackDragon/GenerateRiseOfTheBlackDragon_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_RiseOfTheBlackDragon/GenerateRiseOfTheBlackDragon_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_RiseOfTheBlackDragon/GenerateRiseOfTheBlackDragon_03_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_RiseOfTheBlackDragon/K4_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_RiseOfTheBlackDragon/K4_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_RiseOfTheBlackDragon/K4_RiseOfBlackDragon`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_RiseOfTheBlackDragon/OfferRiseOfTheBlackDragonPrompt2_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_RiseOfTheBlackDragon/OfferRiseOfTheBlackDragonPrompt3_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/Career_RiseOfTheBlackDragon/ShowRiseOfTheBlackDragonSideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/K_7_9/Place_K_7_9`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/K_7_9/Common_K_7_9`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_7_9/K_7_9_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_7_9/K_7_9_ClusterAsset.K_7_9_ClusterAsset' (0x000001BA9C323EC0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'K_7_9_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/K_7_9/K_7_9_ClusterAsset.K_7_9_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/K_7_9/K_7_9_ClusterAsset.K_7_9_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/K_7_9/K_7_9_ClusterAsset.K_7_9_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/K_7_9/K_7_9_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_7_9/K_7_9_ClusterAsset.K_7_9_ClusterAsset' (0x000001BA9C323EC0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB80112B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_7_9_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB80112B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_7_9_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8011210) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8011210) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/K_8_10/Place_K_8_10`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/K_8_10/Common_K_8_10`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_8_10/K_8_10_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_8_10/K_8_10_ClusterAsset.K_8_10_ClusterAsset' (0x000001BA9C322980) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'K_8_10_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/K_8_10/K_8_10_ClusterAsset.K_8_10_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/K_8_10/K_8_10_ClusterAsset.K_8_10_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/K_8_10/K_8_10_ClusterAsset.K_8_10_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/K_8_10/K_8_10_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/K_8_10/K_8_10_ClusterAsset.K_8_10_ClusterAsset' (0x000001BA9C322980) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB80103B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_8_10_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB80103B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "K_8_10_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8010310) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8010310) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/L_11_12/Place_L_11_12`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/L_11_12/Common_L_11_12`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/L_11_12/L_11_12_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/L_11_12/L_11_12_ClusterAsset.L_11_12_ClusterAsset' (0x000001BA9C322700) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'L_11_12_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/L_11_12/L_11_12_ClusterAsset.L_11_12_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/L_11_12/L_11_12_ClusterAsset.L_11_12_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/L_11_12/L_11_12_ClusterAsset.L_11_12_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/L_11_12/L_11_12_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/L_11_12/L_11_12_ClusterAsset.L_11_12_ClusterAsset' (0x000001BA9C322700) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB80113F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "L_11_12_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB80113F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "L_11_12_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8011350) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8011350) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/GreatHouses/Child_SC01_Arc`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/L_12_13/Common_L_12_13`
- class: `MWCampaignArcAsset` exists `True`
- subcampaigns: `2`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/GreatHouses/SC01_H1_Arc`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/GreatHouses/SC01_H2_Arc`
- event actions: `12`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/GreatHouses/Complete_SC01_Q1`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/GreatHouses/Complete_SC01_Q2`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/GreatHouses/Offer_SC01_Q1`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/GreatHouses/Offer_SC01_Q2`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/GreatHouses/Place_SC01_Q1`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/GreatHouses/Place_SC01_Q2`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/GreatHouses/SC01_H1_Arc`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/GreatHouses/SC01_H2_Arc`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/GreatHouses/SC01_Q1_Prompt`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/GreatHouses/SC01_Q1_Scenario`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/GreatHouses/SC01_Q2_Prompt`
  - `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/GreatHouses/SC01_Q2_Scenario1`

### `/Game/DLC1/CareerMode/Warzones/L_12_13/Place_L_12_13`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/L_12_13/Common_L_12_13`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/L_12_13/L_12_13_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/L_12_13/L_12_13_ClusterAsset.L_12_13_ClusterAsset' (0x000001BA9C322480) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'L_12_13_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/L_12_13/L_12_13_ClusterAsset.L_12_13_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/L_12_13/L_12_13_ClusterAsset.L_12_13_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/L_12_13/L_12_13_ClusterAsset.L_12_13_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/L_12_13/L_12_13_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/L_12_13/L_12_13_ClusterAsset.L_12_13_ClusterAsset' (0x000001BA9C322480) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8011CB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "L_12_13_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8011CB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "L_12_13_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8011C10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8011C10) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Liao/Career_TheTraitor/L7_TheTraitor`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/L_13_14/Common_L_13_14`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `7`
  - `/Game/Campaign/Clusters/DavionBorderlands/DavionBorderlands`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_TheTraitor/ChainTheTraitor_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_TheTraitor/GenerateTheTraitor_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_TheTraitor/GenerateTheTraitor_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_TheTraitor/L7_Prompt1`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_TheTraitor/L7_TheTraitor`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_TheTraitor/ShowTheTraitorSideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/L_13_14/Place_L_13_14`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/L_13_14/Common_L_13_14`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/L_13_14/L_13_14_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/L_13_14/L_13_14_ClusterAsset.L_13_14_ClusterAsset' (0x000001BA9C321A80) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'L_13_14_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/L_13_14/L_13_14_ClusterAsset.L_13_14_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/L_13_14/L_13_14_ClusterAsset.L_13_14_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/L_13_14/L_13_14_ClusterAsset.L_13_14_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/L_13_14/L_13_14_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/L_13_14/L_13_14_ClusterAsset.L_13_14_ClusterAsset' (0x000001BA9C321A80) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8010630) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "L_13_14_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8010630) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "L_13_14_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8010590) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8010590) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Liao/Career_ErrantSignal/L_1_ErrantSignal`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/L_1_2/Common_L_1_2`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `7`
  - `/Game/Campaign/Clusters/BackwaterRegion/BackwaterRegion`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_ErrantSignal/GenerateL1_01_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_ErrantSignal/Generate_L1_02_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_ErrantSignal/L_1_ErrantSignal`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_ErrantSignal/L_1_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_ErrantSignal/OfferL1Prompt_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_ErrantSignal/ShowL1SideQuest_ArcAction`

### `/Game/DLC1/CareerMode/Warzones/L_1_2/Place_L_1_2_ArcAction`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/L_1_2/Common_L_1_2`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/L_1_2/L_1_2_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/L_1_2/L_1_2_ClusterAsset.L_1_2_ClusterAsset' (0x000001BA9C3325C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'L_1_2_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/L_1_2/L_1_2_ClusterAsset.L_1_2_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/L_1_2/L_1_2_ClusterAsset.L_1_2_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/L_1_2/L_1_2_ClusterAsset.L_1_2_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/L_1_2/L_1_2_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/L_1_2/L_1_2_ClusterAsset.L_1_2_ClusterAsset' (0x000001BA9C3325C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8013470) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "L_1_2_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8013470) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "L_1_2_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB80133D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB80133D0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/DLC1_ON1`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/L_2_5/Common_L_2_5`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `33`
  - `/Game/Campaign/Clusters/SianCommonality/SianCommonality`
  - `/Game/DLC1/CareerMode/Clusters/S_10_12/CareerCluster_6`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/CompleteON1_4_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/DLC1_HM1_GeneratedMission_1_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/DLC1_HM1_GeneratedMission_2_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/DLC1_HM1_GeneratedMission_3_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/DLC1_ON1`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/DLC_ON1_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/DLC_ON1_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/DLC_ON1_Prompt3`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/DLC_ON1_Prompt4`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/ON1_Mission_1/ON1_Complete_AuthoredScenario_1`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/ON1_Mission_1/ON1_Place_Authored_Scenario_1`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/ON1_Mission_1/ON1_Reset_Scenario_1`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/ON1_Mission_2/ON1_Complete_AuthoredScenario_2`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/ON1_Mission_2/ON1_Place_Authored_Scenario_2`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/ON1_Mission_2/ON1_Reset_Scenario_2`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/ON1_Mission_3/ON1_Complete_AuthoredScenario_3`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/ON1_Mission_3/ON1_Place_Authored_Scenario_3`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/ON1_Mission_3/ON1_Reset_Scenario_3`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/OfferON1_1_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/OfferON1_2_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/OfferON1_3_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/OfferON1_4_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/Place_Authored_ON1`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/Reset_Scenario_ON1`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/ShowON1SideQuest_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/Unlock_DLC1_ON1_01_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/Unlock_DLC1_ON1_02_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/Unlock_DLC1_ON1_03_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Orion/Unlock_DLC1_ON1_04_InstantAction_ArcAction`
  - `/Game/DLC1/DLC_1`
  - `/Game/DLC1/Levels/AuthoredMissions/D1M_Hotdrop/D1M_Hotdrop_Scenario`

### `/Game/DLC1/CareerMode/Sidequests/Liao/Career_CerebusHounds/L_2_CerebusHounds`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/L_2_5/Common_L_2_5`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `7`
  - `/Game/Campaign/Clusters/SianCommonality/SianCommonality`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_CerebusHounds/Generate_L2_01_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_CerebusHounds/Generate_L2_02_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_CerebusHounds/L2_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_CerebusHounds/L_2_CerebusHounds`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_CerebusHounds/Offer_L2Prompt2_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_CerebusHounds/ShowL2_ArcAction`

### `/Game/DLC1/CareerMode/Warzones/L_2_5/Place_L_2_5`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/L_2_5/Common_L_2_5`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/L_2_5/L_2_5_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/L_2_5/L_2_5_ClusterAsset.L_2_5_ClusterAsset' (0x000001BA9C332840) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'L_2_5_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/L_2_5/L_2_5_ClusterAsset.L_2_5_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/L_2_5/L_2_5_ClusterAsset.L_2_5_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/L_2_5/L_2_5_ClusterAsset.L_2_5_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/L_2_5/L_2_5_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/L_2_5/L_2_5_ClusterAsset.L_2_5_ClusterAsset' (0x000001BA9C332840) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB80121B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "L_2_5_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB80121B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "L_2_5_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8012110) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8012110) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Liao/Career_FrontlineDefenseDavion/L3_InvasionDefenseDavion`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/L_3_6/Common_L_3_6`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `8`
  - `/Game/Campaign/Clusters/Liao-DavionBorder/DavionBorder`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_FrontlineDefenseDavion/Career_ChainInvasionDefenseDavion_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_FrontlineDefenseDavion/Career_GenerateInvasionDefenseDavion_01_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_FrontlineDefenseDavion/Career_GenerateInvasionDefenseDavion_02_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_FrontlineDefenseDavion/Career_ShowInvasionDefenseDavionSideQuest_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_FrontlineDefenseDavion/L3_InvasionDefenseDavion`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_FrontlineDefenseDavion/L3_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_FrontlineInvasionLiao/L4_Prompt`

### `/Game/DLC1/CareerMode/Sidequests/Liao/Career_FrontlineInvasionLiao/L4_FrontlineInvasionLiao`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/L_3_6/Common_L_3_6`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `8`
  - `/Game/Campaign/Clusters/Liao-DavionBorder/DavionBorder`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_FrontlineDefenseDavion/L3_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_FrontlineInvasionLiao/Career_ChainFrontlineInvasionLiao_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_FrontlineInvasionLiao/Career_GenerateFrontlineInvasionLiao_01_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_FrontlineInvasionLiao/Career_GenerateFrontlineInvasionLiao_02_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_FrontlineInvasionLiao/Career_ShowFrontlineInvasionLiaoSideQuest`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_FrontlineInvasionLiao/L4_FrontlineInvasionLiao`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_FrontlineInvasionLiao/L4_Prompt`

### `/Game/DLC1/CareerMode/Warzones/L_3_6/Place_L_3_6`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/L_3_6/Common_L_3_6`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/L_3_6/L_3_6_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/L_3_6/L_3_6_ClusterAsset.L_3_6_ClusterAsset' (0x000001BA9C330400) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'L_3_6_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/L_3_6/L_3_6_ClusterAsset.L_3_6_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/L_3_6/L_3_6_ClusterAsset.L_3_6_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/L_3_6/L_3_6_ClusterAsset.L_3_6_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/L_3_6/L_3_6_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/L_3_6/L_3_6_ClusterAsset.L_3_6_ClusterAsset' (0x000001BA9C330400) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB80127F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "L_3_6_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB80127F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "L_3_6_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8012750) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8012750) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Liao/Career_UprisingQuelled/L5_UprisingQuelled`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/L_5_8/Common_L_5_8`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `7`
  - `/Game/Campaign/Clusters/DuchyOfTsitsang/TsinghaiCommonality`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_UprisingQuelled/GenerateUprisingQuelled_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_UprisingQuelled/GenerateUprisingQuelled_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_UprisingQuelled/L5_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_UprisingQuelled/L5_UprisingQuelled`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_UprisingQuelled/OfferUprisingQuelledPrompt2_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_UprisingQuelled/ShowUprisingQuelledSideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/L_5_8/Place_L_5_8`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/L_5_8/Common_L_5_8`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/L_5_8/L_5_8_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/L_5_8/L_5_8_ClusterAsset.L_5_8_ClusterAsset' (0x000001BA9C330680) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'L_5_8_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/L_5_8/L_5_8_ClusterAsset.L_5_8_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/L_5_8/L_5_8_ClusterAsset.L_5_8_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/L_5_8/L_5_8_ClusterAsset.L_5_8_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/L_5_8/L_5_8_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/L_5_8/L_5_8_ClusterAsset.L_5_8_ClusterAsset' (0x000001BA9C330680) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8013BF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "L_5_8_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8013BF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "L_5_8_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8013B50) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8013B50) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/DLC1_RFL`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/L_7_10/Common_L_7_10`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `34`
  - `/Game/Campaign/Clusters/Rashpur-OwensMenufacturingWorlds/RashpurOwensInc`
  - `/Game/DLC1/CareerMode/Clusters/S_10_12/CareerCluster_6`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/CompleteRFL4_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/CompleteRFL4_Prompt4_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/DLC1_HM5_GeneratedMission_1_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/DLC1_HM5_GeneratedMission_2_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/DLC1_HM5_GeneratedMission_3_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/DLC1_RFL`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/DLC_RFL_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/DLC_RFL_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/DLC_RFL_Prompt3`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/DLC_RFL_Prompt4`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/OfferRFL1_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/OfferRFL2_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/OfferRFL3_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/OfferRFL4_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/Place_Authored_RFL`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/RFL_Mission_1/RFL1_Complete_AuthoredScenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/RFL_Mission_1/RFL1_Place_Authored_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/RFL_Mission_1/RFL1_Reset_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/RFL_Mission_2/RFL2_Complete_AuthoredScenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/RFL_Mission_2/RFL2_Place_Authored_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/RFL_Mission_2/RFL2_Reset_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/RFL_Mission_3/RFL3_Complete_AuthoredScenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/RFL_Mission_3/RFL3_Place_Authored_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/RFL_Mission_3/RFL3_Reset_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/Reset_Scenario_RFL`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/ShowRFLSideQuest_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/Unlock_DLC1_RFL_01_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/Unlock_DLC1_RFL_02_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/Unlock_DLC1_RFL_03_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Rifleman/Unlock_DLC1_RFL_04_InstantAction_ArcAction`
  - `/Game/DLC1/DLC_1`
  - `/Game/DLC1/Levels/AuthoredMissions/D1M_Longshot/D1M_Longshot_Scenario`

### `/Game/DLC1/CareerMode/Sidequests/Liao/Career_IndustrialEspionage/L6_IndustrialEspionage`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/L_7_10/Common_L_7_10`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `7`
  - `/Game/Campaign/Clusters/Rashpur-OwensMenufacturingWorlds/RashpurOwensInc`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_IndustrialEspionage/ChainIndustrialEspionage_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_IndustrialEspionage/GenerateIndustrialEspionage_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_IndustrialEspionage/GenerateIndustrialEspionage_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_IndustrialEspionage/L6_IndustrialEspionage`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_IndustrialEspionage/L6_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Liao/Career_IndustrialEspionage/ShowIndustrialEspionageSideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/L_7_10/Place_L_7_10`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/L_7_10/Common_L_7_10`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/L_7_10/L_7_10_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/L_7_10/L_7_10_ClusterAsset.L_7_10_ClusterAsset' (0x000001BA9C330900) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'L_7_10_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/L_7_10/L_7_10_ClusterAsset.L_7_10_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/L_7_10/L_7_10_ClusterAsset.L_7_10_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/L_7_10/L_7_10_ClusterAsset.L_7_10_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/L_7_10/L_7_10_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/L_7_10/L_7_10_ClusterAsset.L_7_10_ClusterAsset' (0x000001BA9C330900) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8012F70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "L_7_10_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8012F70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "L_7_10_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8012ED0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8012ED0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ForcefulNegotiations/M7_ForcefulNegotiations`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_11_12/Common_M_11_12`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `10`
  - `/Game/Campaign/Clusters/DuchyOfTamarind/TamarindAbbey`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ForcefulNegotiations/Generate_ForcefulNegotiation_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ForcefulNegotiations/Generate_ForcefulNegotiation_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ForcefulNegotiations/Generate_ForcefulNegotiation_03_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ForcefulNegotiations/M7_ForcefulNegotiations`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ForcefulNegotiations/M7_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ForcefulNegotiations/M7_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ForcefulNegotiations/OfferForcefulNegotiation_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ForcefulNegotiations/OfferForcefulNegotiation_03_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ForcefulNegotiations/ShowForcefulNegotiationSideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/M_11_12/Place_M_11_12`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_11_12/Common_M_11_12`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/M_11_12/M_11_12_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_11_12/M_11_12_ClusterAsset.M_11_12_ClusterAsset' (0x000001BA9C330B80) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'M_11_12_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/M_11_12/M_11_12_ClusterAsset.M_11_12_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/M_11_12/M_11_12_ClusterAsset.M_11_12_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/M_11_12/M_11_12_ClusterAsset.M_11_12_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/M_11_12/M_11_12_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_11_12/M_11_12_ClusterAsset.M_11_12_ClusterAsset' (0x000001BA9C330B80) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB80108B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_11_12_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB80108B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_11_12_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8010810) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8010810) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Marik/Career_FalseFlag/M11_FalseFlag`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_12_13/Common_M_12_13`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `10`
  - `/Game/Campaign/Clusters/Marik-StrinerBorder/SteinerMarikBorder`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_FalseFlag/ChainFalseFlag_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_FalseFlag/GenerateFalseFlag_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_FalseFlag/GenerateFalseFlag_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_FalseFlag/GenerateFalseFlag_03_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_FalseFlag/M11_FalseFlag`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_FalseFlag/M11_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_FalseFlag/M11_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_FalseFlag/OfferFalseFlag_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_FalseFlag/ShowFalseFlagSideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/M_12_13/Place_M_12_13`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_12_13/Common_M_12_13`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/M_12_13/M_12_13_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_12_13/M_12_13_ClusterAsset.M_12_13_ClusterAsset' (0x000001BA9C330E00) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'M_12_13_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/M_12_13/M_12_13_ClusterAsset.M_12_13_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/M_12_13/M_12_13_ClusterAsset.M_12_13_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/M_12_13/M_12_13_ClusterAsset.M_12_13_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/M_12_13/M_12_13_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_12_13/M_12_13_ClusterAsset.M_12_13_ClusterAsset' (0x000001BA9C330E00) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8626570) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_12_13_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8626570) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_12_13_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB86264D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB86264D0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Marik/Career_DeathToEnhanced/M10_DeathToEnhanced`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_12_13_1/Common_M_12_13_1`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `7`
  - `/Game/Campaign/Clusters/StweartCommonwealth/StewartCommonality`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_DeathToEnhanced/ChainDeathToEnhanced_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_DeathToEnhanced/GenerateDeathToEnhanced_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_DeathToEnhanced/GenerateDeathToEnhanced_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_DeathToEnhanced/M10_DeathToEnhanced`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_DeathToEnhanced/M10_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_DeathToEnhanced/ShowDeathToEnhancedSideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/M_12_13_1/Place_M_12_13_1`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_12_13_1/Common_M_12_13_1`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/M_12_13_1/M_12_13_1_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_12_13_1/M_12_13_1_ClusterAsset.M_12_13_1_ClusterAsset' (0x000001BA9C331080) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'M_12_13_1_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/M_12_13_1/M_12_13_1_ClusterAsset.M_12_13_1_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/M_12_13_1/M_12_13_1_ClusterAsset.M_12_13_1_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/M_12_13_1/M_12_13_1_ClusterAsset.M_12_13_1_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/M_12_13_1/M_12_13_1_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_12_13_1/M_12_13_1_ClusterAsset.M_12_13_1_ClusterAsset' (0x000001BA9C331080) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB86261B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_12_13_1_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB86261B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_12_13_1_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8626110) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8626110) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/DLC1_Archer`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_13_14/Common_M_13_14`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `33`
  - `/Game/DLC1/CareerMode/Clusters/M_13_14/CareerCluster_2`
  - `/Game/DLC1/CareerMode/Clusters/S_10_12/CareerCluster_6`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/ARC_Mission_1/ARC_Complete_AuthoredScenario_1`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/ARC_Mission_1/ARC_Place_Authored_Scenario_1`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/ARC_Mission_1/ARC_Reset_Scenario_1`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/ARC_Mission_2/ARC_Complete_AuthoredScenario_2`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/ARC_Mission_2/ARC_Place_Authored_Scenario_2`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/ARC_Mission_2/ARC_Reset_Scenario_2`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/ARC_Mission_3/ARC_Complete_AuthoredScenario_3`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/ARC_Mission_3/ARC_Place_Authored_Scenario_3`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/ARC_Mission_3/ARC_Reset_Scenario_3`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/CompleteArcher4_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/DLC1_Archer`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/DLC1_HM6_GeneratedMission_1_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/DLC1_HM6_GeneratedMission_2_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/DLC1_HM6_GeneratedMission_3_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/DLC_ARC_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/DLC_ARC_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/DLC_ARC_Prompt3`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/DLC_ARC_Prompt4`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/OfferArcher1_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/OfferArcher2_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/OfferArcher3_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/OfferArcher4_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/Place_Authored_Archer`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/Reset_Scenario_ARC`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/ShowArcherSideQuest_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/Unlock_DLC1_ARC_01_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/Unlock_DLC1_ARC_02_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/Unlock_DLC1_ARC_03_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Archer/Unlock_DLC1_ARC_04_InstantAction_ArcAction`
  - `/Game/DLC1/DLC_1`
  - `/Game/DLC1/Levels/AuthoredMissions/D1M_Effect/D1M_Effect_Scenario`

### `/Game/DLC1/CareerMode/Warzones/M_13_14/Place_M_13_14`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_13_14/Common_M_13_14`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/M_13_14/M_13_14_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_13_14/M_13_14_ClusterAsset.M_13_14_ClusterAsset' (0x000001BA9C331300) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'M_13_14_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/M_13_14/M_13_14_ClusterAsset.M_13_14_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/M_13_14/M_13_14_ClusterAsset.M_13_14_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/M_13_14/M_13_14_ClusterAsset.M_13_14_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/M_13_14/M_13_14_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_13_14/M_13_14_ClusterAsset.M_13_14_ClusterAsset' (0x000001BA9C331300) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8625530) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_13_14_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8625530) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_13_14_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8625490) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8625490) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/M_15/Place_M_15`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_15/Common_M_15`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/M_15/M_15_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_15/M_15_ClusterAsset.M_15_ClusterAsset' (0x000001BA9C331440) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'M_15_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/M_15/M_15_ClusterAsset.M_15_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/M_15/M_15_ClusterAsset.M_15_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/M_15/M_15_ClusterAsset.M_15_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/M_15/M_15_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_15/M_15_ClusterAsset.M_15_ClusterAsset' (0x000001BA9C331440) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8625A30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_15_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8625A30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_15_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8625990) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8625990) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ChasingGhosts/M1_ChasingGhosts`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_1_2/Common_M_1_2`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `10`
  - `/Game/Campaign/Clusters/VacantWorlds/EmptyWorlds`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ChasingGhosts/ChainChasingGhosts_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ChasingGhosts/GenerateChasingGhosts_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ChasingGhosts/GenerateChasingGhosts_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ChasingGhosts/GenerateChasingGhosts_03_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ChasingGhosts/M1_ChasingGhosts`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ChasingGhosts/M1_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ChasingGhosts/M1_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ChasingGhosts/OfferChasingGhostsPrompt2_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ChasingGhosts/ShowChasingGhostsSideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/M_1_2/Place_M_1_2`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_1_2/Common_M_1_2`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/M_1_2/M_1_2_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_1_2/M_1_2_ClusterAsset.M_1_2_ClusterAsset' (0x000001BA9C3316C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'M_1_2_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/M_1_2/M_1_2_ClusterAsset.M_1_2_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/M_1_2/M_1_2_ClusterAsset.M_1_2_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/M_1_2/M_1_2_ClusterAsset.M_1_2_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/M_1_2/M_1_2_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_1_2/M_1_2_ClusterAsset.M_1_2_ClusterAsset' (0x000001BA9C3316C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8624C70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_1_2_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8624C70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_1_2_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8624BD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8624BD0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Marik/Career_NoPilotLeftBehind/M2_NoPilotLeftBehind`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_2_5/Common_M_2_5`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `7`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_NoPilotLeftBehind/GenerateNoPilotLeftBehind_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_NoPilotLeftBehind/GenerateNoPilotLeftBehind_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_NoPilotLeftBehind/M2_NoPilotLeftBehind`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_NoPilotLeftBehind/M2_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_NoPilotLeftBehind/OfferNoPilotLeftBehindPrompt2_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_NoPilotLeftBehind/ShowNoPilotLeftBehindSideQuest_ArcAction_Career`
  - `/Game/Factions/DuchyOfAndurien`

### `/Game/DLC1/CareerMode/Warzones/M_2_5/Place_M_2_5`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_2_5/Common_M_2_5`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/M_2_5/M_2_5_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_2_5/M_2_5_ClusterAsset.M_2_5_ClusterAsset' (0x000001BA9C331940) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'M_2_5_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/M_2_5/M_2_5_ClusterAsset.M_2_5_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/M_2_5/M_2_5_ClusterAsset.M_2_5_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/M_2_5/M_2_5_ClusterAsset.M_2_5_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/M_2_5/M_2_5_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_2_5/M_2_5_ClusterAsset.M_2_5_ClusterAsset' (0x000001BA9C331940) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8625170) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_2_5_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8625170) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_2_5_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB86250D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB86250D0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Marik/Career_Destabalization/Career_CorporateInterests/M4_CorporateInterests`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_3_6/Common_M_3_6`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `5`
  - `/Game/Campaign/Clusters/FreeWorldCommerceHub/FWLInterior`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_Destabalization/Career_CorporateInterests/GenerateCorporateInterests_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_Destabalization/Career_CorporateInterests/OfferCorporateInterests_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_Destabalization/M3_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_Destabalization/M3_Prompt3`

### `/Game/DLC1/CareerMode/Sidequests/Marik/Career_Destabalization/M3_Destabalization`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_3_6/Common_M_3_6`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `13`
  - `/Game/Campaign/Clusters/FreeWorldCommerceHub/FWLInterior`
  - `/Game/Campaign/Clusters/FreeWorldInterior/FWLCommercialHub`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_Destabalization/Career_CorporateInterests/M4_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_Destabalization/GenerateDestabalization_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_Destabalization/GenerateDestabalization_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_Destabalization/GenerateDestabalization_03_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_Destabalization/M3_Destabalization`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_Destabalization/M3_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_Destabalization/M3_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_Destabalization/M3_Prompt3`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_Destabalization/OfferDestabalizationPrompt2_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_Destabalization/OfferDestabalizationPrompt3_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_Destabalization/ShowDestabalizationSideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/M_3_6/Place_M_3_6`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_3_6/Common_M_3_6`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/M_3_6/M_3_6_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_3_6/M_3_6_ClusterAsset.M_3_6_ClusterAsset' (0x000001BA9C331BC0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'M_3_6_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/M_3_6/M_3_6_ClusterAsset.M_3_6_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/M_3_6/M_3_6_ClusterAsset.M_3_6_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/M_3_6/M_3_6_ClusterAsset.M_3_6_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/M_3_6/M_3_6_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_3_6/M_3_6_ClusterAsset.M_3_6_ClusterAsset' (0x000001BA9C331BC0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8624630) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_3_6_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8624630) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_3_6_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8624590) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8624590) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Marik/Career_EnemyOfMyEnemy/M5_EnemyOfMyEnemy`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_5_8/Common_M_5_8`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `10`
  - `/Game/Campaign/Clusters/Marik-LiaoBorder/MarikLiaoBorder`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_EnemyOfMyEnemy/GenerateEnemyOfMyEnemy_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_EnemyOfMyEnemy/GenerateEnemyOfMyEnemy_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_EnemyOfMyEnemy/GenerateEnemyOfMyEnemy_03_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_EnemyOfMyEnemy/M5_EnemyOfMyEnemy`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_EnemyOfMyEnemy/M5_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_EnemyOfMyEnemy/M5_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_EnemyOfMyEnemy/OfferEnemyOfMyEnemyPrompt2_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_EnemyOfMyEnemy/OfferEnemyOfMyEnemyPrompt3_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_EnemyOfMyEnemy/ShowEnemyOfMyEnemySideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/M_5_8/Place_M_5_8`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_5_8/Common_M_5_8`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/M_5_8/M_5_8_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_5_8/M_5_8_ClusterAsset.M_5_8_ClusterAsset' (0x000001BA9C331E40) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'M_5_8_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/M_5_8/M_5_8_ClusterAsset.M_5_8_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/M_5_8/M_5_8_ClusterAsset.M_5_8_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/M_5_8/M_5_8_ClusterAsset.M_5_8_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/M_5_8/M_5_8_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_5_8/M_5_8_ClusterAsset.M_5_8_ClusterAsset' (0x000001BA9C331E40) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB86266B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_5_8_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB86266B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_5_8_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8626610) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8626610) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Marik/Career_DefendingtheHonor/M6_DefendingTheHonor`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_7_10/Common_M_7_10`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `11`
  - `/Game/Campaign/Clusters/FreeWorldCommerceHub/FWLInterior`
  - `/Game/Campaign/Clusters/FreeWorldInterior/FWLCommercialHub`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_DefendingtheHonor/GenerateDefendingTheHonor_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_DefendingtheHonor/GenerateDefendingTheHonor_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_DefendingtheHonor/GenerateDefendingTheHonor_03_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_DefendingtheHonor/M6_DefendingTheHonor`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_DefendingtheHonor/M6_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_DefendingtheHonor/M6_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_DefendingtheHonor/OfferDefendingTheHonorPrompt2_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_DefendingtheHonor/OfferDefendingTheHonorPrompt3_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_DefendingtheHonor/ShowDefendingTheHonorSideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/M_7_10/Place_M_7_10`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_7_10/Common_M_7_10`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/M_7_10/M_7_10_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_7_10/M_7_10_ClusterAsset.M_7_10_ClusterAsset' (0x000001BA9C3320C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'M_7_10_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/M_7_10/M_7_10_ClusterAsset.M_7_10_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/M_7_10/M_7_10_ClusterAsset.M_7_10_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/M_7_10/M_7_10_ClusterAsset.M_7_10_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/M_7_10/M_7_10_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_7_10/M_7_10_ClusterAsset.M_7_10_ClusterAsset' (0x000001BA9C3320C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8626BB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_7_10_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8626BB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_7_10_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8626B10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8626B10) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ShippingDisruption/M8_ShippingDistruption`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_9_11/Common_M_9_11`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `7`
  - `/Game/Campaign/Clusters/FWL_ShippingLane/FWLShippingRoute`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ShippingDisruption/ChainShippingDistruption_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ShippingDisruption/Generate_ShippingDistruption_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ShippingDisruption/Generate_ShippingDistruption_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ShippingDisruption/M8_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ShippingDisruption/M8_ShippingDistruption`
  - `/Game/DLC1/CareerMode/Sidequests/Marik/Career_ShippingDisruption/ShowShippingDistruptionSideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/M_9_11/Place_M_9_11`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/M_9_11/Common_M_9_11`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/M_9_11/M_9_11_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_9_11/M_9_11_ClusterAsset.M_9_11_ClusterAsset' (0x000001BA9C332FC0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'M_9_11_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/M_9_11/M_9_11_ClusterAsset.M_9_11_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/M_9_11/M_9_11_ClusterAsset.M_9_11_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/M_9_11/M_9_11_ClusterAsset.M_9_11_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/M_9_11/M_9_11_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/M_9_11/M_9_11_ClusterAsset.M_9_11_ClusterAsset' (0x000001BA9C332FC0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB86270B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_9_11_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB86270B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "M_9_11_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8627010) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8627010) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Kurita/K10/DLC1_ThePowderKeg`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_10_12/Common_S_10_12`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `10`
  - `/Game/DLC1/CareerMode/Clusters/S_10_12/CareerCluster_6`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K10/DLC1_10_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K10/DLC1_10_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K10/DLC1_ThePowderKeg`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K10/GenerateThePowderKeg_01_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K10/GenerateThePowderKeg_02_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K10/GenerateThePowderKeg_03_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K10/OfferThePowderKegPrompt2_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K10/OfferThePowderKegPrompt3_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Kurita/K10/ShowThePowderKegSideQuest_ArcAction`

### `/Game/DLC1/CareerMode/Warzones/S_10_12/Place_S_10_12`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_10_12/Common_S_10_12`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/S_10_12/S_10_12_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_10_12/S_10_12_ClusterAsset.S_10_12_ClusterAsset' (0x000001BA19C3FB00) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'S_10_12_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/S_10_12/S_10_12_ClusterAsset.S_10_12_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/S_10_12/S_10_12_ClusterAsset.S_10_12_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/S_10_12/S_10_12_ClusterAsset.S_10_12_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/S_10_12/S_10_12_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_10_12/S_10_12_ClusterAsset.S_10_12_ClusterAsset' (0x000001BA19C3FB00) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB86275B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_10_12_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB86275B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_10_12_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8627510) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8627510) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Steiner/Career_ShadowCoup/S5_ShadowCoup`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_12_13/Common_S_12_13`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `7`
  - `/Game/Campaign/Clusters/LyranMilitaryStrongholds/LyranStrongholds`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/Career_ShadowCoup/ChainShadowCorp_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/Career_ShadowCoup/GenereateShadowCorp_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/Career_ShadowCoup/GenereateShadowCorp_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/Career_ShadowCoup/S5_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/Career_ShadowCoup/S5_ShadowCoup`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/Career_ShadowCoup/ShowShadowCorpSideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/S_12_13/Place_S_12_13`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_12_13/Common_S_12_13`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/S_12_13/S_12_13_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_12_13/S_12_13_ClusterAsset.S_12_13_ClusterAsset' (0x000001BA19C3FD80) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'S_12_13_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/S_12_13/S_12_13_ClusterAsset.S_12_13_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/S_12_13/S_12_13_ClusterAsset.S_12_13_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/S_12_13/S_12_13_ClusterAsset.S_12_13_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/S_12_13/S_12_13_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_12_13/S_12_13_ClusterAsset.S_12_13_ClusterAsset' (0x000001BA19C3FD80) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8627AB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_12_13_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB8627AB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_12_13_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8627A10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB8627A10) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/DLC1_KGC`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_13_14/Common_S_13_14`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `33`
  - `/Game/Campaign/Clusters/A2M3/AgriculturalBelt`
  - `/Game/DLC1/CareerMode/Clusters/S_10_12/CareerCluster_6`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/CompleteKGC4_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/DLC1_HM3_GeneratedMission_1_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/DLC1_HM3_GeneratedMission_2_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/DLC1_HM3_GeneratedMission_3_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/DLC1_KGC`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/DLC_KGC_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/DLC_KGC_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/DLC_KGC_Prompt3`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/DLC_KGC_Prompt4`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/KGC_Mission_1/KGC_Complete_AuthoredScenario_1`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/KGC_Mission_1/KGC_Place_Authored_Scenario_1`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/KGC_Mission_1/KGC_Reset_Scenario_1`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/KGC_Mission_2/KGC_Complete_AuthoredScenario_2`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/KGC_Mission_2/KGC_Place_Authored_Scenario_2`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/KGC_Mission_2/KGC_Reset_Scenario_2`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/KGC_Mission_3/KGC_Complete_AuthoredScenario_3`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/KGC_Mission_3/KGC_Place_Authored_Scenario_3`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/KGC_Mission_3/KGC_Reset_Scenario_3`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/OfferKGC1_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/OfferKGC2_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/OfferKGC3_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/OfferKGC4_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/Place_Authored_KGC`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/Reset_Scenario_KGC`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/ShowKGCSideQuest_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/Unlock_DLC1_KGC_01_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/Unlock_DLC1_KGC_02_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/Unlock_DLC1_KGC_03_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_KingCrab/Unlock_DLC1_KGC_04_InstantAction_ArcAction`
  - `/Game/DLC1/DLC_1`
  - `/Game/DLC1/Levels/AuthoredMissions/D1M_Battle/D1M_Battle_Scenario`

### `/Game/DLC1/CareerMode/Warzones/S_13_14/Place_S_13_14`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_13_14/Common_S_13_14`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/S_13_14/S_13_14_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_13_14/S_13_14_ClusterAsset.S_13_14_ClusterAsset' (0x000001BA19C5E5C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'S_13_14_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/S_13_14/S_13_14_ClusterAsset.S_13_14_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/S_13_14/S_13_14_ClusterAsset.S_13_14_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/S_13_14/S_13_14_ClusterAsset.S_13_14_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/S_13_14/S_13_14_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_13_14/S_13_14_ClusterAsset.S_13_14_ClusterAsset' (0x000001BA19C5E5C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765FFB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_13_14_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765FFB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_13_14_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765FF10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765FF10) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/S_1_2/Place_S_1_2`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_1_2/Common_S_1_2`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/S_1_2/S_1_2_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_1_2/S_1_2_ClusterAsset.S_1_2_ClusterAsset' (0x000001BA19C5E840) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'S_1_2_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/S_1_2/S_1_2_ClusterAsset.S_1_2_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/S_1_2/S_1_2_ClusterAsset.S_1_2_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/S_1_2/S_1_2_ClusterAsset.S_1_2_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/S_1_2/S_1_2_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_1_2/S_1_2_ClusterAsset.S_1_2_ClusterAsset' (0x000001BA19C5E840) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765EE30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_1_2_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765EE30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_1_2_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765ED90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765ED90) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/S_2_4/Place_S_2_4`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_2_4/Common_S_2_4`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/S_2_4/S_2_4_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_2_4/S_2_4_ClusterAsset.S_2_4_ClusterAsset' (0x000001BA19C5E980) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'S_2_4_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/S_2_4/S_2_4_ClusterAsset.S_2_4_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/S_2_4/S_2_4_ClusterAsset.S_2_4_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/S_2_4/S_2_4_ClusterAsset.S_2_4_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/S_2_4/S_2_4_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_2_4/S_2_4_ClusterAsset.S_2_4_ClusterAsset' (0x000001BA19C5E980) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765F330) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_2_4_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765F330) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_2_4_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765F290) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765F290) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Steiner/S5/DLC1_CompetitiveEdge`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_2_5/Common_S_2_5`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `9`
  - `/Game/DLC1/CareerMode/Clusters/S_2_5/CareerCluster_7`
  - `/Game/DLC1/CareerMode/Clusters/S_3_5/CareerCluster_9`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S5/DLC1_5_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S5/DLC1_5_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S5/DLC1_CompetitiveEdge`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S5/GenerateCompetitiveEdge_01_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S5/GenerateCompetitiveEdge_02_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S5/OfferCompetitiveEdgePrompt2_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S5/ShowCompetitiveEdgeSideQuest_ArcAction`

### `/Game/DLC1/CareerMode/Warzones/S_2_5/Place_S_2_5`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_2_5/Common_S_2_5`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/S_2_5/S_2_5_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_2_5/S_2_5_ClusterAsset.S_2_5_ClusterAsset' (0x000001BA19C5C2C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'S_2_5_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/S_2_5/S_2_5_ClusterAsset.S_2_5_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/S_2_5/S_2_5_ClusterAsset.S_2_5_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/S_2_5/S_2_5_ClusterAsset.S_2_5_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/S_2_5/S_2_5_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_2_5/S_2_5_ClusterAsset.S_2_5_ClusterAsset' (0x000001BA19C5C2C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765E1B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_2_5_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765E1B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_2_5_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765E110) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765E110) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Steiner/S3/DLC1_ReturnOfTheRangers`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_3_5/Common_S_3_5`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `10`
  - `/Game/DLC1/CareerMode/Clusters/S_3_5/CareerCluster_9`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S3/DLC1_3_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S3/DLC1_3_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S3/DLC1_ReturnOfTheRangers`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S3/GenerateReturnOfTheRangers_01_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S3/GenerateReturnOfTheRangers_02_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S3/GenerateReturnOfTheRangers_03_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S3/OfferReturnOfTheRangersPrompt2_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S3/OfferReturnOfTheRangersPrompt3_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S3/ShowReturnOfTheRangersSideQuest_ArcAction`

### `/Game/DLC1/CareerMode/Warzones/S_3_5/Place_S_3_5`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_3_5/Common_S_3_5`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/S_3_5/S_3_5_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_3_5/S_3_5_ClusterAsset.S_3_5_ClusterAsset' (0x000001BA19C5C540) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'S_3_5_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/S_3_5/S_3_5_ClusterAsset.S_3_5_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/S_3_5/S_3_5_ClusterAsset.S_3_5_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/S_3_5/S_3_5_ClusterAsset.S_3_5_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/S_3_5/S_3_5_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_3_5/S_3_5_ClusterAsset.S_3_5_ClusterAsset' (0x000001BA19C5C540) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765E6B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_3_5_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765E6B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_3_5_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765E610) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765E610) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Steiner/S4/DLC1_BowieElectronics`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_4_6/Common_S_4_6`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `11`
  - `/Game/DLC1/CareerMode/Clusters/S_2_4/CareerCluster_8`
  - `/Game/DLC1/CareerMode/Clusters/S_3_5/CareerCluster_9`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S4/DLC1_4_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S4/DLC1_4_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S4/DLC1_BowieElectronics`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S4/GenerateBowieElectronics_01_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S4/GenerateBowieElectronics_01_ArcAction2`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S4/GenerateBowieElectronics_01_ArcAction3`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S4/OfferBowieElectronicsPrompt2_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S4/OfferBowieElectronicsPrompt3_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S4/ShowBowieElectronicsSideQuest_ArcAction`

### `/Game/DLC1/CareerMode/Warzones/S_4_6/Place_S_4_6`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_4_6/Common_S_4_6`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/S_4_6/S_4_6_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_4_6/S_4_6_ClusterAsset.S_4_6_ClusterAsset' (0x000001BA19C5CCC0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'S_4_6_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/S_4_6/S_4_6_ClusterAsset.S_4_6_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/S_4_6/S_4_6_ClusterAsset.S_4_6_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/S_4_6/S_4_6_ClusterAsset.S_4_6_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/S_4_6/S_4_6_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_4_6/S_4_6_ClusterAsset.S_4_6_ClusterAsset' (0x000001BA19C5CCC0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765DA30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_4_6_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765DA30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_4_6_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765D990) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765D990) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/S_5_8/Place_S_5_8`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_5_8/Common_S_5_8`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/S_5_8/S_5_8_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_5_8/S_5_8_ClusterAsset.S_5_8_ClusterAsset' (0x000001BA19C5CF40) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'S_5_8_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/S_5_8/S_5_8_ClusterAsset.S_5_8_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/S_5_8/S_5_8_ClusterAsset.S_5_8_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/S_5_8/S_5_8_ClusterAsset.S_5_8_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/S_5_8/S_5_8_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_5_8/S_5_8_ClusterAsset.S_5_8_ClusterAsset' (0x000001BA19C5CF40) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765D670) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_5_8_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765D670) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_5_8_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765D5D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765D5D0) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Warzones/S_5_8_1/Place_S_5_8_1`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_5_8_1/Common_S_5_8_1`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/S_5_8_1/S_5_8_1_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_5_8_1/S_5_8_1_ClusterAsset.S_5_8_1_ClusterAsset' (0x000001BA19C5D1C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'S_5_8_1_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/S_5_8_1/S_5_8_1_ClusterAsset.S_5_8_1_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/S_5_8_1/S_5_8_1_ClusterAsset.S_5_8_1_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/S_5_8_1/S_5_8_1_ClusterAsset.S_5_8_1_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/S_5_8_1/S_5_8_1_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_5_8_1/S_5_8_1_ClusterAsset.S_5_8_1_ClusterAsset' (0x000001BA19C5D1C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765D530) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_5_8_1_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765D530) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_5_8_1_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765D490) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765D490) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/DLC1_COR`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_6_7/Common_S_6_7`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `33`
  - `/Game/Campaign/Clusters/PiratesLair/PirateCluster`
  - `/Game/DLC1/CareerMode/Clusters/S_10_12/CareerCluster_6`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/COR_Mission_1/COR_Complete_AuthoredScenario_1`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/COR_Mission_1/COR_Place_Authored_Scenario_1`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/COR_Mission_1/COR_Reset_Scenario_1`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/COR_Mission_2/COR_Complete_AuthoredScenario_2`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/COR_Mission_2/COR_Place_Authored_Scenario_2`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/COR_Mission_2/COR_Reset_Scenario_2`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/COR_Mission_3/COR_Complete_AuthoredScenario_3`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/COR_Mission_3/COR_Place_Authored_Scenario_3`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/COR_Mission_3/COR_Reset_Scenario_3`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/CompleteCOR4_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/DLC1_COR`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/DLC1_HM7_GeneratedMission_1_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/DLC1_HM7_GeneratedMission_2_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/DLC1_HM7_GeneratedMission_3_Scenario`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/DLC_COR_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/DLC_COR_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/DLC_COR_Prompt3`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/DLC_COR_Prompt4`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/OfferCOR1_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/OfferCOR2_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/OfferCOR3_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/OfferCOR4_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/Place_Authored_Cor`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/Reset_Scenario_COR`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/ShowCorSideQuest_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/Unlock_DLC1_COR_01_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/Unlock_DLC1_COR_02_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/Unlock_DLC1_COR_03_InstantAction_ArcAction`
  - `/Game/DLC1/CareerMode/Sidequests/HeroesOfTheIS/Quest_Corsair/Unlock_DLC1_COR_04_InstantAction_ArcAction`
  - `/Game/DLC1/DLC_1`
  - `/Game/DLC1/Levels/AuthoredMissions/D1M_Pirate/D1M_Pirate_Scenario`

### `/Game/DLC1/CareerMode/Warzones/S_6_7/Place_S_6_7`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_6_7/Common_S_6_7`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/S_6_7/S_6_7_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_6_7/S_6_7_ClusterAsset.S_6_7_ClusterAsset' (0x000001BA19C5D940) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'S_6_7_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/S_6_7/S_6_7_ClusterAsset.S_6_7_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/S_6_7/S_6_7_ClusterAsset.S_6_7_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/S_6_7/S_6_7_ClusterAsset.S_6_7_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/S_6_7/S_6_7_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_6_7/S_6_7_ClusterAsset.S_6_7_ClusterAsset' (0x000001BA19C5D940) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765C3B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_6_7_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765C3B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_6_7_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765C310) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765C310) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Steiner/Career_DragonInSheepsClothing/S6_DragonInSheepsClothing`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_6_9/Common_S_6_9`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `10`
  - `/Game/Campaign/Clusters/Steiner-KuritaBorder/SteinerBorder`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/Career_DragonInSheepsClothing/GenerateDragonInSheepsClothing_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/Career_DragonInSheepsClothing/GenerateDragonInSheepsClothing_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/Career_DragonInSheepsClothing/GenerateDragonInSheepsClothing_03_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/Career_DragonInSheepsClothing/OfferDragonInSheepsClothingPrompt2_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/Career_DragonInSheepsClothing/OfferDragonInSheepsClothingPrompt3_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/Career_DragonInSheepsClothing/S6_DragonInSheepsClothing`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/Career_DragonInSheepsClothing/S6_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/Career_DragonInSheepsClothing/S6_Prompt2`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/Career_DragonInSheepsClothing/ShowDragonInSheepsClothingSideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/S_6_9/Place_S_6_9`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_6_9/Common_S_6_9`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/S_6_9/S_6_9_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_6_9/S_6_9_ClusterAsset.S_6_9_ClusterAsset' (0x000001BA19C5DBC0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'S_6_9_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/S_6_9/S_6_9_ClusterAsset.S_6_9_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/S_6_9/S_6_9_ClusterAsset.S_6_9_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/S_6_9/S_6_9_ClusterAsset.S_6_9_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/S_6_9/S_6_9_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_6_9/S_6_9_ClusterAsset.S_6_9_ClusterAsset' (0x000001BA19C5DBC0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765CB30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_6_9_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765CB30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_6_9_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765CA90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765CA90) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/CostOfFreedom/S3_CostOfFreedom`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_9_11/Common_S_9_11`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `5`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/CostOfFreedom/GenerateCostOfFreedom_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/CostOfFreedom/OfferGenerateCostOfFreedom_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/CostOfFreedom/S3_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranRebellion/S2_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranRebellion/S2_Prompt2`

### `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/CostOfLoyalty/S4_CostOfLoyalty`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_9_11/Common_S_9_11`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `5`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/CostOfLoyalty/GenerateCostOfLoyalty_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/CostOfLoyalty/OfferCostOfLoyalty_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/CostOfLoyalty/S4_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranIndependence/S1_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranIndependence/S1_Prompt2`

### `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranIndependence/S1_LyranIndependence`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_9_11/Common_S_9_11`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `11`
  - `/Game/Campaign/Clusters/RebelliousLyranPrince/RebeliousLyranTerritory`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/CostOfLoyalty/S4_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranIndependence/ChainLyranIndependence_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranIndependence/GenerateLyranIndependence_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranIndependence/GenerateLyranIndependence_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranIndependence/GenerateLyranIndependence_03_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranIndependence/OfferLyranIndependence_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranIndependence/S1_LyranIndependence`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranIndependence/S1_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranIndependence/ShowLyranIndependenceSideQuest_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranRebellion/S2_Prompt`

### `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranRebellion/S2_LyranRebellion`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_9_11/Common_S_9_11`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `11`
  - `/Game/Campaign/Clusters/RebelliousLyranPrince/RebeliousLyranTerritory`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/CostOfFreedom/S3_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranIndependence/S1_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranRebellion/ChainLyranRebellion_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranRebellion/GenerateLyranRebellion_01_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranRebellion/GenerateLyranRebellion_02_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranRebellion/GenerateLyranRebellion_03_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranRebellion/OfferLyranRebellion_Prompt2_ArcAction_Career`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranRebellion/S2_LyranRebellion`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranRebellion/S2_Prompt`
  - `/Game/DLC1/CareerMode/Sidequests/Steiner/S1/LyranRebellion/ShowLyranRebellionSideQuest_ArcAction_Career`

### `/Game/DLC1/CareerMode/Warzones/S_9_11/Place_S_9_11`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/Warzones/S_9_11/Common_S_9_11`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/S_9_11/S_9_11_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_9_11/S_9_11_ClusterAsset.S_9_11_ClusterAsset' (0x000001BA19C5DE40) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'S_9_11_ClusterAsset', 'get_path_name': '/Game/DLC1/CareerMode/Clusters/S_9_11/S_9_11_ClusterAsset.S_9_11_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/DLC1/CareerMode/Clusters/S_9_11/S_9_11_ClusterAsset.S_9_11_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/DLC1/CareerMode/Clusters/S_9_11/S_9_11_ClusterAsset.S_9_11_ClusterAsset', 'asset_paths': ['/Game/DLC1/CareerMode/Clusters/S_9_11/S_9_11_ClusterAsset'], 'repr': "<Object '/Game/DLC1/CareerMode/Clusters/S_9_11/S_9_11_ClusterAsset.S_9_11_ClusterAsset' (0x000001BA19C5DE40) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765D030) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_9_11_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BAB765D030) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "S_9_11_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765CF90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BAB765CF90) {id: 0}>"}}`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_10/SafeZone_10_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_10_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_10/SafeZone_10_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_11/SafeZone_11_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_11_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_11/SafeZone_11_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_12/SafeZone_12_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_12_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_12/SafeZone_12_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_13/SafeZone_13_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_13_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_13/SafeZone_13_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_14/SafeZone_14_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_14_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_14/SafeZone_14_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_15/SafeZone_15_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_15_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_15/SafeZone_15_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_16/SafeZone_16_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_16_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_16/SafeZone_16_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_17/SafeZone_17_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_17_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_17/SafeZone_17_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_18/SafeZone_18_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_18_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_18/SafeZone_18_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_19/SafeZone_19_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_19_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_19/SafeZone_19_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_1/SafeZone_1_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_1_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_1/SafeZone_1_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_20/SafeZone_20_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_20_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_20/SafeZone_20_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_21/SafeZone_21_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_21_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_21/SafeZone_21_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_22/SafeZone_22_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_22_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_22/SafeZone_22_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_23/SafeZone_23_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_23_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_23/SafeZone_23_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_24/SafeZone_24_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_24_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_24/SafeZone_24_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_25/SafeZone_25_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_25_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_25/SafeZone_25_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_26/SafeZone_26_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_26_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_26/SafeZone_26_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_27/SafeZone_27_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_27_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_27/SafeZone_27_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_28/SafeZone_28_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_28_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_28/SafeZone_28_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_29/SafeZone_29_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_29_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_29/SafeZone_29_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_2/SafeZone_2_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_2_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_2/SafeZone_2_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_30/SafeZone_30_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_30_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_30/SafeZone_30_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_31/SafeZone_31_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_31_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_31/SafeZone_31_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_32/SafeZone_32_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_32_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_32/SafeZone_32_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_33/SafeZone_33_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_33_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_33/SafeZone_33_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_34/SafeZone_34_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_34_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_34/SafeZone_34_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_35/SafeZone_35_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_35_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_35/SafeZone_35_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_3/SafeZone_3_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_3_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_3/SafeZone_3_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_4/SafeZone_4_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_4_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_4/SafeZone_4_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_5/SafeZone_5_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_5_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_5/SafeZone_5_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_6/SafeZone_6_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_6_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_6/SafeZone_6_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_7/SafeZone_7_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_7_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_7/SafeZone_7_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_8/SafeZone_8_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_8_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_8/SafeZone_8_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/SafeZone_9/SafeZone_9_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC1/CareerMode/IndustrialHubs/PlaceSafeZone_9_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/SafeZone_9/SafeZone_9_ClusterAsset']`

### `/Game/Campaign/CampaignArcs/BorderChanges/3025_ThirdSuccession/StarMapBordersUpdate_3025_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/BorderChanges/3025_ThirdSuccession/3025_ThirdSuccession`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB101C74B0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB101C74B0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/BorderChanges/3029_FormationOfTikinovAndStIves/StarMapBordersUpdate_3029_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/BorderChanges/3029_FormationOfTikinovAndStIves/3029_FormationOfTikinovAndStIves`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB101C6DF0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB101C6DF0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/BorderChanges/3030_FourthSuccession/StarMapBordersUpdate_3030_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/BorderChanges/3030_FourthSuccession/3030_FourthSuccession`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB101C6C70) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB101C6C70) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/BorderChanges/3031_TikinovJoinsFederatedSuns/StarMapBordersUpdate_3031_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/BorderChanges/3031_TikinovJoinsFederatedSuns/3031_TikinovJoinsFederatedSuns`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB101C49F0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB101C49F0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/BorderChanges/3034_RassalhaugeRecognized/StarMapBordersUpdate_3034_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/BorderChanges/3034_RassalhaugeRecognized/Borders_Year3034_RassalhaugeRecognized`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB101C7ED0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB101C7ED0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/BorderChanges/3039_WarOf3039/StarMapBordersUpdate_3039_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/BorderChanges/3039_WarOf3039/3039_WarOf3039`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB101C5290) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB101C5290) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/BorderChanges/3041_FormationOfFederatedCommonwealth/StarMapBordersUpdate_3041_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/BorderChanges/3041_FormationOfFederatedCommonwealth/3041_FormationOfFederatedCommonwealth`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB101C7690) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB101C7690) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/BorderChanges/3049_ClanInvasion/StarMapBordersUpdate_3049_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/BorderChanges/3049_ClanInvasion/3049_ClanInvasion`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB101C7D50) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB101C7D50) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/BorderChanges/3050_OperationRevival_Wave1/3050_ClanInvasion_Wave1`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/BorderChanges/3049_ClanInvasion/3049_ClanInvasion`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `2`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3050_OperationRevival_Wave1/StarMapBordersUpdate_3050_Wave1_ArcAction`
  - `/Game/DLC7/DLC_7`

### `/Game/Campaign/CampaignArcs/BorderChanges/3050_OperationRevival_Wave2/3050_ClanInvasion_Wave2`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/BorderChanges/3049_ClanInvasion/3049_ClanInvasion`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `2`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3050_OperationRevival_Wave2/StarMapBordersUpdate_3050_Wave2_ArcAction`
  - `/Game/DLC7/DLC_7`

### `/Game/Campaign/CampaignArcs/BorderChanges/3050_OperationRevival_Wave3/3050_ClanInvasion_Wave3`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/BorderChanges/3049_ClanInvasion/3049_ClanInvasion`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `2`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3050_OperationRevival_Wave3/StarMapBordersUpdate_3050_Wave3_ArcAction`
  - `/Game/DLC7/DLC_7`

### `/Game/Campaign/CampaignArcs/BorderChanges/3050_YearOfPeace_Wave4/3050_ClanInvasion_Wave4`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/BorderChanges/3049_ClanInvasion/3049_ClanInvasion`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `2`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3050_YearOfPeace_Wave4/StarMapBordersUpdate_3050_Wave4_ArcAction`
  - `/Game/DLC7/DLC_7`

### `/Game/Campaign/CampaignArcs/BorderChanges/3051_EndOfOperationRevival_Wave5/3050_ClanInvasion_Wave5`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcs/BorderChanges/3049_ClanInvasion/3049_ClanInvasion`
- class: `MWCampaignArcAsset` exists `True`
- event actions: `2`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3051_EndOfOperationRevival_Wave5/StarMapBordersUpdate_3050_Wave5_ArcAction`
  - `/Game/DLC7/DLC_7`

### `/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CGB_Periphery_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Periphery/CGB_Periphery_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave1_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave1/CGB_Wave1_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave2_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave2/CGB_Wave2_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave3_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave3/CGB_Wave3_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave4_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave4/CGB_Wave4_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CGB_Wave5_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave5/CGB_Wave5_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CJF_Periphery_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Periphery/CJF_Periphery_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave1_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave1/CJF_Wave1_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave2_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave2/CJF_Wave2_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave3_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave3/CJF_Wave3_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave4_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave4/CJF_Wave4_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CJF_Wave5_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave5/CJF_Wave5_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Periphery_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Periphery/CSJ_Periphery_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave1_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave1/CSJ_Wave1_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave2_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave2/CSJ_Wave2_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave3_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave3/CSJ_Wave3_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave4_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave4/CSJ_Wave4_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CSJ_Wave5_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave5/CSJ_Wave5_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CWF_Periphery_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Periphery/CWF_Periphery_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave1_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave1/CWF_Wave1_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave2_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave2/CWF_Wave2_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave3_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave3/CWF_Wave3_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave4_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave4/CWF_Wave4_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/CWF_Wave5_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave5/CWF_Wave5_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Periphery/ConflictCluster_Periphery_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Periphery_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Periphery/ConflictCluster_Periphery_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave1/ConflictCluster_Wave1_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave1_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave1/ConflictCluster_Wave1_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave2/ConflictCluster_Wave2_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave2_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave2/ConflictCluster_Wave2_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave3/ConflictCluster_Wave3_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave3_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave3/ConflictCluster_Wave3_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave4/ConflictCluster_Wave4_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave4_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave4/ConflictCluster_Wave4_ClusterAsset']`

### `/Game/DLC7/CampaignData/Clusters/Wave5/ConflictCluster_Wave5_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/NewClusters/ConflictZone_Wave5_PlaceCluster_ArcAction`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC7/CampaignData/Clusters/Wave5/ConflictCluster_Wave5_ClusterAsset']`

### `/Game/DLC7/PlaceClusterActions/RemoveClusterToiArcAction`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByEndOfInvasion`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BB18412840) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BB18412840) {id: 0}>"}}`

### `/Game/Campaign/Clusters/PiratesLair/PiratesLair_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByPeripheryWave`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/PiratesLair/PiratesLair_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/S_6_7/S_6_7_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByPeripheryWave`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/S_6_7/S_6_7_ClusterAsset']`

### `/Game/Campaign/Clusters/DroughtWorlds/DroughtWorlds_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave1`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/DroughtWorlds/DroughtWorlds_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_29/IndustrialHub_29_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave1`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_29/IndustrialHub_29_ClusterAsset']`

### `/Game/Campaign/Clusters/Rasalhague/Rasalhague_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave1`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Rasalhague/Rasalhague_ClusterAsset']`

### `/Game/Campaign/Clusters/TheGraveyard/TheGraveyard_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave1`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/TheGraveyard/TheGraveyard_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/K_1_2/K_1_2_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave1`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_1_2/K_1_2_ClusterAsset']`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemoveWave1`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave1`
- class: `ObjectRedirector` exists `True`

### `/Game/Campaign/Clusters/SC07/SC07_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave2`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/SC07/SC07_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/K_4_5/K_4_5_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave2`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_4_5/K_4_5_ClusterAsset']`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemoveWave2`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave2`
- class: `ObjectRedirector` exists `True`

### `/Game/DLC1/CareerMode/Clusters/K_2_3/K_2_3_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave3`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_2_3/K_2_3_ClusterAsset']`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemoveWave3`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave3`
- class: `ObjectRedirector` exists `True`

### `/Game/Campaign/Clusters/SC05/SC05_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave4`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/SC05/SC05_ClusterAsset']`

### `/Game/Campaign/Clusters/SC06/SC06_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave4`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/SC06/SC06_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/K_3_4/K_3_4_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave4`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_3_4/K_3_4_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/K_3_5_1/K_3_5_1_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave4`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_3_5_1/K_3_5_1_ClusterAsset']`

### `/Game/DLC4/CampaignData/Clusters/RadstadtZone/RadstadtZone_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave4`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC4/CampaignData/Clusters/RadstadtZone/RadstadtZone_ClusterAsset']`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemoveWave4`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave4`
- class: `ObjectRedirector` exists `True`

### `/Game/Campaign/Clusters/DraconisBadlands/DraconisBadlands_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/DraconisBadlands/DraconisBadlands_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_17/IndustrialHub_17_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_17/IndustrialHub_17_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_22/IndustrialHub_22_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_22/IndustrialHub_22_ClusterAsset']`

### `/Game/Campaign/Clusters/Lower-ClassKuritanWorlds/Lower-ClassKuritanWorlds_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Lower-ClassKuritanWorlds/Lower-ClassKuritanWorlds_ClusterAsset']`

### `/Game/Campaign/Clusters/Steiner-KuritaBorder/Steiner-KuritaBorder_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Steiner-KuritaBorder/Steiner-KuritaBorder_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/K_5_6/K_5_6_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_5_6/K_5_6_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/K_7_9/K_7_9_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_7_9/K_7_9_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/S_6_9/S_6_9_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/S_6_9/S_6_9_ClusterAsset']`

### `/Game/DLC7/PlaceClusterActions/RemoveClusters/RemoveWave5`
- depth/reason: `2` / `referenced by /Game/DLC7/PlaceClusterActions/RemoveClusters/RemovedByWave5`
- class: `ObjectRedirector` exists `True`

### `/Game/UI/Textures/Factions/IE_Logo_32px_UIX`
- depth/reason: `2` / `referenced by /Game/Factions/InterstellarExpeditions`
- class: `Texture2D` exists `True`

### `/Game/UI/Textures/Factions/IE_Logo_Large`
- depth/reason: `2` / `referenced by /Game/Factions/InterstellarExpeditions`
- class: `Texture2D` exists `True`

### `/Game/UI/Textures/Factions/main_factions/Faction_Rasalhague_1024PX_STD_UIX`
- depth/reason: `2` / `referenced by /Game/Factions/FreeRasalhagueRepublic`
- class: `Texture2D` exists `True`

### `/Game/UI/Textures/Factions/main_factions/Faction_Rasalhague_Logo_32px_UIX`
- depth/reason: `2` / `referenced by /Game/Factions/FreeRasalhagueRepublic`
- class: `Texture2D` exists `True`

### `/Game/UI/Textures/Factions/main_factions/Faction_Mercs_1024PX_STD_UIX`
- depth/reason: `2` / `referenced by /Game/Factions/Mercenaries`
- class: `Texture2D` exists `True`

### `/Game/UI/Textures/Factions/main_factions/Faction_Mercs_Logo_32px_UIX`
- depth/reason: `2` / `referenced by /Game/Factions/Mercenaries`
- class: `Texture2D` exists `True`

### `/Game/Campaign/CampaignArcActions/MissionActions/MissionConfigs/PlaceClusterToi_Config`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `UserDefinedStruct` exists `True`
- referenced clusters: `['/Game/Campaign/_common/MW5_ClusterAssetCacheActor', '/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets']`

### `/Game/Campaign/CampaignArcActions/MissionActions/MissionConfigs/PlaceClusterToi_Markups`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `UserDefinedStruct` exists `True`
- referenced clusters: `['/Game/Campaign/_common/MW5_ClusterAssetCacheActor', '/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets']`

### `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToiUtility`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `EditorUtilityBlueprint` exists `True`

### `/Game/Campaign/CampaignArcs/MetagameObjectives/PlaceBanditsLair_Cluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- cdo focused properties: `{'ClusterDataAsset': {'value': None, 'path': None, 'asset_paths': [], 'repr': 'None'}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BA1A3CB5B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BA1A3CB5B0) {id: {primary_asset_type: {name: ""}, primary_asset_name: ""}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BA1A3CB510) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BA1A3CB510) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/10_1/PlaceFWL_ShippingLaneCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/FWL_ShippingLane/FWL_ShippingLane_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/FWL_ShippingLane/FWL_ShippingLane_ClusterAsset.FWL_ShippingLane_ClusterAsset' (0x000001BA89CC7D80) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'FWL_ShippingLane_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/FWL_ShippingLane/FWL_ShippingLane_ClusterAsset.FWL_ShippingLane_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/FWL_ShippingLane/FWL_ShippingLane_ClusterAsset.FWL_ShippingLane_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/FWL_ShippingLane/FWL_ShippingLane_ClusterAsset.FWL_ShippingLane_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/FWL_ShippingLane/FWL_ShippingLane_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/FWL_ShippingLane/FWL_ShippingLane_ClusterAsset.FWL_ShippingLane_ClusterAsset' (0x000001BA89CC7D80) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BA1A3CA570) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "FWL_ShippingLane_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BA1A3CA570) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "FWL_ShippingLane_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BA1A3CA4D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BA1A3CA4D0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/10_2/PlaceDuchyOfTamarindCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/DuchyOfTamarind/DuchyOfTamarind_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/DuchyOfTamarind/DuchyOfTamarind_ClusterAsset.DuchyOfTamarind_ClusterAsset' (0x000001BA89CC65C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'DuchyOfTamarind_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/DuchyOfTamarind/DuchyOfTamarind_ClusterAsset.DuchyOfTamarind_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/DuchyOfTamarind/DuchyOfTamarind_ClusterAsset.DuchyOfTamarind_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/DuchyOfTamarind/DuchyOfTamarind_ClusterAsset.DuchyOfTamarind_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/DuchyOfTamarind/DuchyOfTamarind_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/DuchyOfTamarind/DuchyOfTamarind_ClusterAsset.DuchyOfTamarind_ClusterAsset' (0x000001BA89CC65C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BA1A3C84F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "DuchyOfTamarind_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BA1A3C84F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "DuchyOfTamarind_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BA1A3C8450) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BA1A3C8450) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/10_3/PlaceMarik-StrinerBorderCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Marik-StrinerBorder/Marik-StrinerBorder_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/Marik-StrinerBorder/Marik-StrinerBorder_ClusterAsset.Marik-StrinerBorder_ClusterAsset' (0x000001BA89D03880) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'Marik-StrinerBorder_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/Marik-StrinerBorder/Marik-StrinerBorder_ClusterAsset.Marik-StrinerBorder_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/Marik-StrinerBorder/Marik-StrinerBorder_ClusterAsset.Marik-StrinerBorder_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/Marik-StrinerBorder/Marik-StrinerBorder_ClusterAsset.Marik-StrinerBorder_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/Marik-StrinerBorder/Marik-StrinerBorder_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/Marik-StrinerBorder/Marik-StrinerBorder_ClusterAsset.Marik-StrinerBorder_ClusterAsset' (0x000001BA89D03880) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BA1A3C8C70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Marik-StrinerBorder_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BA1A3C8C70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Marik-StrinerBorder_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BA1A3C8BD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BA1A3C8BD0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/11_1/PlaceStweartCommonwealthCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/StweartCommonwealth/StweartCommonwealth_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/StweartCommonwealth/StweartCommonwealth_ClusterAsset.StweartCommonwealth_ClusterAsset' (0x000001BA9C356E80) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'StweartCommonwealth_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/StweartCommonwealth/StweartCommonwealth_ClusterAsset.StweartCommonwealth_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/StweartCommonwealth/StweartCommonwealth_ClusterAsset.StweartCommonwealth_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/StweartCommonwealth/StweartCommonwealth_ClusterAsset.StweartCommonwealth_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/StweartCommonwealth/StweartCommonwealth_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/StweartCommonwealth/StweartCommonwealth_ClusterAsset.StweartCommonwealth_ClusterAsset' (0x000001BA9C356E80) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BA1A3C9CB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "StweartCommonwealth_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BA1A3C9CB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "StweartCommonwealth_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BA1A3C9C10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BA1A3C9C10) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/11_2/PlaceRebelliousLyranPrinceCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/RebelliousLyranPrince/RebelliousLyranPrince_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/RebelliousLyranPrince/RebelliousLyranPrince_ClusterAsset.RebelliousLyranPrince_ClusterAsset' (0x000001BA9C354B80) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'RebelliousLyranPrince_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/RebelliousLyranPrince/RebelliousLyranPrince_ClusterAsset.RebelliousLyranPrince_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/RebelliousLyranPrince/RebelliousLyranPrince_ClusterAsset.RebelliousLyranPrince_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/RebelliousLyranPrince/RebelliousLyranPrince_ClusterAsset.RebelliousLyranPrince_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/RebelliousLyranPrince/RebelliousLyranPrince_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/RebelliousLyranPrince/RebelliousLyranPrince_ClusterAsset.RebelliousLyranPrince_ClusterAsset' (0x000001BA9C354B80) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54CEF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "RebelliousLyranPrince_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54CEF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "RebelliousLyranPrince_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54CE50) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54CE50) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/11_3/PlaceLyranMilitaryStrongholdsCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/LyranMilitaryStrongholds/LyranMilitaryStrongholds_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/LyranMilitaryStrongholds/LyranMilitaryStrongholds_ClusterAsset.LyranMilitaryStrongholds_ClusterAsset' (0x000001BA89D03380) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'LyranMilitaryStrongholds_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/LyranMilitaryStrongholds/LyranMilitaryStrongholds_ClusterAsset.LyranMilitaryStrongholds_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/LyranMilitaryStrongholds/LyranMilitaryStrongholds_ClusterAsset.LyranMilitaryStrongholds_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/LyranMilitaryStrongholds/LyranMilitaryStrongholds_ClusterAsset.LyranMilitaryStrongholds_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/LyranMilitaryStrongholds/LyranMilitaryStrongholds_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/LyranMilitaryStrongholds/LyranMilitaryStrongholds_ClusterAsset.LyranMilitaryStrongholds_ClusterAsset' (0x000001BA89D03380) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54C630) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "LyranMilitaryStrongholds_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54C630) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "LyranMilitaryStrongholds_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54C590) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54C590) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/12_1/PlaceSteiner-KuritaBorderCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Steiner-KuritaBorder/Steiner-KuritaBorder_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/Steiner-KuritaBorder/Steiner-KuritaBorder_ClusterAsset.Steiner-KuritaBorder_ClusterAsset' (0x000001BA9C356C00) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'Steiner-KuritaBorder_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/Steiner-KuritaBorder/Steiner-KuritaBorder_ClusterAsset.Steiner-KuritaBorder_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/Steiner-KuritaBorder/Steiner-KuritaBorder_ClusterAsset.Steiner-KuritaBorder_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/Steiner-KuritaBorder/Steiner-KuritaBorder_ClusterAsset.Steiner-KuritaBorder_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/Steiner-KuritaBorder/Steiner-KuritaBorder_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/Steiner-KuritaBorder/Steiner-KuritaBorder_ClusterAsset.Steiner-KuritaBorder_ClusterAsset' (0x000001BA9C356C00) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54D7B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Steiner-KuritaBorder_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54D7B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Steiner-KuritaBorder_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54D710) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54D710) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/12_2/PlaceLower-ClassKuritanWorldsCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Lower-ClassKuritanWorlds/Lower-ClassKuritanWorlds_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/Lower-ClassKuritanWorlds/Lower-ClassKuritanWorlds_ClusterAsset.Lower-ClassKuritanWorlds_ClusterAsset' (0x000001BA89D03240) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'Lower-ClassKuritanWorlds_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/Lower-ClassKuritanWorlds/Lower-ClassKuritanWorlds_ClusterAsset.Lower-ClassKuritanWorlds_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/Lower-ClassKuritanWorlds/Lower-ClassKuritanWorlds_ClusterAsset.Lower-ClassKuritanWorlds_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/Lower-ClassKuritanWorlds/Lower-ClassKuritanWorlds_ClusterAsset.Lower-ClassKuritanWorlds_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/Lower-ClassKuritanWorlds/Lower-ClassKuritanWorlds_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/Lower-ClassKuritanWorlds/Lower-ClassKuritanWorlds_ClusterAsset.Lower-ClassKuritanWorlds_ClusterAsset' (0x000001BA89D03240) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54E070) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Lower-ClassKuritanWorlds_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54E070) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Lower-ClassKuritanWorlds_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54DFD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54DFD0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/12_3/PlaceRogueCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Rogue/Rogue_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/Rogue/Rogue_ClusterAsset.Rogue_ClusterAsset' (0x000001BA9C354E00) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'Rogue_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/Rogue/Rogue_ClusterAsset.Rogue_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/Rogue/Rogue_ClusterAsset.Rogue_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/Rogue/Rogue_ClusterAsset.Rogue_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/Rogue/Rogue_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/Rogue/Rogue_ClusterAsset.Rogue_ClusterAsset' (0x000001BA9C354E00) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54C9F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Rogue_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54C9F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Rogue_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54C950) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54C950) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/12_4/PlacePiratesLairCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/PiratesLair/PiratesLair_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/PiratesLair/PiratesLair_ClusterAsset.PiratesLair_ClusterAsset' (0x000001BA9C357100) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'PiratesLair_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/PiratesLair/PiratesLair_ClusterAsset.PiratesLair_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/PiratesLair/PiratesLair_ClusterAsset.PiratesLair_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/PiratesLair/PiratesLair_ClusterAsset.PiratesLair_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/PiratesLair/PiratesLair_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/PiratesLair/PiratesLair_ClusterAsset.PiratesLair_ClusterAsset' (0x000001BA9C357100) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54E6B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "PiratesLair_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54E6B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "PiratesLair_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54E610) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54E610) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/13_1/PlaceDraconisBadlandsCluster_ArcaCtion`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/DraconisBadlands/DraconisBadlands_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/DraconisBadlands/DraconisBadlands_ClusterAsset.DraconisBadlands_ClusterAsset' (0x000001BA89CC6E80) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'DraconisBadlands_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/DraconisBadlands/DraconisBadlands_ClusterAsset.DraconisBadlands_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/DraconisBadlands/DraconisBadlands_ClusterAsset.DraconisBadlands_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/DraconisBadlands/DraconisBadlands_ClusterAsset.DraconisBadlands_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/DraconisBadlands/DraconisBadlands_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/DraconisBadlands/DraconisBadlands_ClusterAsset.DraconisBadlands_ClusterAsset' (0x000001BA89CC6E80) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54EE30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "DraconisBadlands_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54EE30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "DraconisBadlands_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54ED90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54ED90) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/13_2/PlaceDroughtWorldsCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/DroughtWorlds/DroughtWorlds_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/DroughtWorlds/DroughtWorlds_ClusterAsset.DroughtWorlds_ClusterAsset' (0x000001BA89CC7100) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'DroughtWorlds_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/DroughtWorlds/DroughtWorlds_ClusterAsset.DroughtWorlds_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/DroughtWorlds/DroughtWorlds_ClusterAsset.DroughtWorlds_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/DroughtWorlds/DroughtWorlds_ClusterAsset.DroughtWorlds_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/DroughtWorlds/DroughtWorlds_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/DroughtWorlds/DroughtWorlds_ClusterAsset.DroughtWorlds_ClusterAsset' (0x000001BA89CC7100) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54E430) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "DroughtWorlds_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54E430) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "DroughtWorlds_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54E390) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54E390) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/13_3/PlaceTheGraveyardCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/TheGraveyard/TheGraveyard_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/TheGraveyard/TheGraveyard_ClusterAsset.TheGraveyard_ClusterAsset' (0x000001BA9C357880) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'TheGraveyard_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/TheGraveyard/TheGraveyard_ClusterAsset.TheGraveyard_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/TheGraveyard/TheGraveyard_ClusterAsset.TheGraveyard_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/TheGraveyard/TheGraveyard_ClusterAsset.TheGraveyard_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/TheGraveyard/TheGraveyard_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/TheGraveyard/TheGraveyard_ClusterAsset.TheGraveyard_ClusterAsset' (0x000001BA9C357880) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54E7F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "TheGraveyard_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54E7F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "TheGraveyard_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54E750) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54E750) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/3_1/PlaceMercenaryRowCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/MercenaryRow/MercenaryRow_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/MercenaryRow/MercenaryRow_ClusterAsset.MercenaryRow_ClusterAsset' (0x000001BA89D02700) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'MercenaryRow_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/MercenaryRow/MercenaryRow_ClusterAsset.MercenaryRow_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/MercenaryRow/MercenaryRow_ClusterAsset.MercenaryRow_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/MercenaryRow/MercenaryRow_ClusterAsset.MercenaryRow_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/MercenaryRow/MercenaryRow_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/MercenaryRow/MercenaryRow_ClusterAsset.MercenaryRow_ClusterAsset' (0x000001BA89D02700) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54D030) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "MercenaryRow_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54D030) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "MercenaryRow_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54CF90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54CF90) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/4_1/PlaceInfernosWakeCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/InfernosWake/InfernosWake_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/InfernosWake/InfernosWake_ClusterAsset.InfernosWake_ClusterAsset' (0x000001BA89D011C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'InfernosWake_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/InfernosWake/InfernosWake_ClusterAsset.InfernosWake_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/InfernosWake/InfernosWake_ClusterAsset.InfernosWake_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/InfernosWake/InfernosWake_ClusterAsset.InfernosWake_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/InfernosWake/InfernosWake_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/InfernosWake/InfernosWake_ClusterAsset.InfernosWake_ClusterAsset' (0x000001BA89D011C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54DB70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "InfernosWake_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB54DB70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "InfernosWake_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54DAD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB54DAD0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/5_1/PlaceDavion-KuritaFrontlineCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Davion-KuritaFrontline/Davion-KuritaFrontline_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/Davion-KuritaFrontline/Davion-KuritaFrontline_ClusterAsset.Davion-KuritaFrontline_ClusterAsset' (0x000001BA89CC6980) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'Davion-KuritaFrontline_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/Davion-KuritaFrontline/Davion-KuritaFrontline_ClusterAsset.Davion-KuritaFrontline_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/Davion-KuritaFrontline/Davion-KuritaFrontline_ClusterAsset.Davion-KuritaFrontline_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/Davion-KuritaFrontline/Davion-KuritaFrontline_ClusterAsset.Davion-KuritaFrontline_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/Davion-KuritaFrontline/Davion-KuritaFrontline_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/Davion-KuritaFrontline/Davion-KuritaFrontline_ClusterAsset.Davion-KuritaFrontline_ClusterAsset' (0x000001BA89CC6980) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39D8F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Davion-KuritaFrontline_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39D8F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Davion-KuritaFrontline_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39D850) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39D850) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/5_2/PlaceIndustrialMiningCollectiveCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialMiningCollective/IndustrialMiningCollective_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/IndustrialMiningCollective/IndustrialMiningCollective_ClusterAsset.IndustrialMiningCollective_ClusterAsset' (0x000001BA89D02C00) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'IndustrialMiningCollective_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/IndustrialMiningCollective/IndustrialMiningCollective_ClusterAsset.IndustrialMiningCollective_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/IndustrialMiningCollective/IndustrialMiningCollective_ClusterAsset.IndustrialMiningCollective_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/IndustrialMiningCollective/IndustrialMiningCollective_ClusterAsset.IndustrialMiningCollective_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/IndustrialMiningCollective/IndustrialMiningCollective_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/IndustrialMiningCollective/IndustrialMiningCollective_ClusterAsset.IndustrialMiningCollective_ClusterAsset' (0x000001BA89D02C00) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39DCB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "IndustrialMiningCollective_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39DCB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "IndustrialMiningCollective_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39DC10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39DC10) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/6_1/PlaceKurita-DavionFrontLineCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Kurita-DavionFrontLine/Kurita-DavionFrontLine_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/Kurita-DavionFrontLine/Kurita-DavionFrontLine_ClusterAsset.Kurita-DavionFrontLine_ClusterAsset' (0x000001BA89D02AC0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'Kurita-DavionFrontLine_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/Kurita-DavionFrontLine/Kurita-DavionFrontLine_ClusterAsset.Kurita-DavionFrontLine_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/Kurita-DavionFrontLine/Kurita-DavionFrontLine_ClusterAsset.Kurita-DavionFrontLine_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/Kurita-DavionFrontLine/Kurita-DavionFrontLine_ClusterAsset.Kurita-DavionFrontLine_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/Kurita-DavionFrontLine/Kurita-DavionFrontLine_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/Kurita-DavionFrontLine/Kurita-DavionFrontLine_ClusterAsset.Kurita-DavionFrontLine_ClusterAsset' (0x000001BA89D02AC0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39F330) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Kurita-DavionFrontLine_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39F330) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Kurita-DavionFrontLine_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39F290) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39F290) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/6_2/PlaceDavionBorderlandsCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/DavionBorderlands/DavionBorderlands_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/DavionBorderlands/DavionBorderlands_ClusterAsset.DavionBorderlands_ClusterAsset' (0x000001BA89CC6C00) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'DavionBorderlands_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/DavionBorderlands/DavionBorderlands_ClusterAsset.DavionBorderlands_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/DavionBorderlands/DavionBorderlands_ClusterAsset.DavionBorderlands_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/DavionBorderlands/DavionBorderlands_ClusterAsset.DavionBorderlands_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/DavionBorderlands/DavionBorderlands_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/DavionBorderlands/DavionBorderlands_ClusterAsset.DavionBorderlands_ClusterAsset' (0x000001BA89CC6C00) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39FAB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "DavionBorderlands_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39FAB0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "DavionBorderlands_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39FA10) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39FA10) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/6_3/PlaceShippingRouteCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/ShippingRoute/ShippingRoute_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/ShippingRoute/ShippingRoute_ClusterAsset.ShippingRoute_ClusterAsset' (0x000001BA9C356340) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'ShippingRoute_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/ShippingRoute/ShippingRoute_ClusterAsset.ShippingRoute_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/ShippingRoute/ShippingRoute_ClusterAsset.ShippingRoute_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/ShippingRoute/ShippingRoute_ClusterAsset.ShippingRoute_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/ShippingRoute/ShippingRoute_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/ShippingRoute/ShippingRoute_ClusterAsset.ShippingRoute_ClusterAsset' (0x000001BA9C356340) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39E930) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "ShippingRoute_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39E930) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "ShippingRoute_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39E890) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39E890) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/7_1/PlaceRashpur-OwensMenufacturingWorldsCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Rashpur-OwensMenufacturingWorlds/Rashpur-OwensMenufacturingWorlds_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/Rashpur-OwensMenufacturingWorlds/Rashpur-OwensMenufacturingWorlds_ClusterAsset.Rashpur-OwensMenufacturingWorlds_ClusterAsset' (0x000001BA9C3551C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'Rashpur-OwensMenufacturingWorlds_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/Rashpur-OwensMenufacturingWorlds/Rashpur-OwensMenufacturingWorlds_ClusterAsset.Rashpur-OwensMenufacturingWorlds_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/Rashpur-OwensMenufacturingWorlds/Rashpur-OwensMenufacturingWorlds_ClusterAsset.Rashpur-OwensMenufacturingWorlds_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/Rashpur-OwensMenufacturingWorlds/Rashpur-OwensMenufacturingWorlds_ClusterAsset.Rashpur-OwensMenufacturingWorlds_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/Rashpur-OwensMenufacturingWorlds/Rashpur-OwensMenufacturingWorlds_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/Rashpur-OwensMenufacturingWorlds/Rashpur-OwensMenufacturingWorlds_ClusterAsset.Rashpur-OwensMenufacturingWorlds_ClusterAsset' (0x000001BA9C3551C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39EF70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Rashpur-OwensMenufacturingWorlds_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39EF70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Rashpur-OwensMenufacturingWorlds_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39EED0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39EED0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/7_2/PlaceDuchyOfTsitsangCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/DuchyOfTsitsang/DuchyOfTsitsang_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/DuchyOfTsitsang/DuchyOfTsitsang_ClusterAsset.DuchyOfTsitsang_ClusterAsset' (0x000001BA89CC7600) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'DuchyOfTsitsang_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/DuchyOfTsitsang/DuchyOfTsitsang_ClusterAsset.DuchyOfTsitsang_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/DuchyOfTsitsang/DuchyOfTsitsang_ClusterAsset.DuchyOfTsitsang_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/DuchyOfTsitsang/DuchyOfTsitsang_ClusterAsset.DuchyOfTsitsang_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/DuchyOfTsitsang/DuchyOfTsitsang_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/DuchyOfTsitsang/DuchyOfTsitsang_ClusterAsset.DuchyOfTsitsang_ClusterAsset' (0x000001BA89CC7600) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39E2F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "DuchyOfTsitsang_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39E2F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "DuchyOfTsitsang_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39E250) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39E250) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/8_1/PlaceSianCommonalityCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/SianCommonality/SianCommonality_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/SianCommonality/SianCommonality_ClusterAsset.SianCommonality_ClusterAsset' (0x000001BA9C3565C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SianCommonality_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/SianCommonality/SianCommonality_ClusterAsset.SianCommonality_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/SianCommonality/SianCommonality_ClusterAsset.SianCommonality_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/SianCommonality/SianCommonality_ClusterAsset.SianCommonality_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/SianCommonality/SianCommonality_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/SianCommonality/SianCommonality_ClusterAsset.SianCommonality_ClusterAsset' (0x000001BA9C3565C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39C9F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SianCommonality_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39C9F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SianCommonality_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39C950) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39C950) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/8_2/PlaceLiao-DavionBorderCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Liao-DavionBorder/Liao-DavionBorder_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/Liao-DavionBorder/Liao-DavionBorder_ClusterAsset.Liao-DavionBorder_ClusterAsset' (0x000001BA89D02FC0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'Liao-DavionBorder_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/Liao-DavionBorder/Liao-DavionBorder_ClusterAsset.Liao-DavionBorder_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/Liao-DavionBorder/Liao-DavionBorder_ClusterAsset.Liao-DavionBorder_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/Liao-DavionBorder/Liao-DavionBorder_ClusterAsset.Liao-DavionBorder_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/Liao-DavionBorder/Liao-DavionBorder_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/Liao-DavionBorder/Liao-DavionBorder_ClusterAsset.Liao-DavionBorder_ClusterAsset' (0x000001BA89D02FC0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39C4F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Liao-DavionBorder_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39C4F0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Liao-DavionBorder_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39C450) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39C450) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/8_3/PlaceDuchyOfAndurienCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/DuchyOfAndurien/DuchyOfAndurien_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/DuchyOfAndurien/DuchyOfAndurien_ClusterAsset.DuchyOfAndurien_ClusterAsset' (0x000001BA89CC7380) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'DuchyOfAndurien_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/DuchyOfAndurien/DuchyOfAndurien_ClusterAsset.DuchyOfAndurien_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/DuchyOfAndurien/DuchyOfAndurien_ClusterAsset.DuchyOfAndurien_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/DuchyOfAndurien/DuchyOfAndurien_ClusterAsset.DuchyOfAndurien_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/DuchyOfAndurien/DuchyOfAndurien_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/DuchyOfAndurien/DuchyOfAndurien_ClusterAsset.DuchyOfAndurien_ClusterAsset' (0x000001BA89CC7380) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39DF30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "DuchyOfAndurien_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39DF30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "DuchyOfAndurien_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39DE90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39DE90) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/8_4/PlaceBackwaterRegionCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/BackwaterRegion/BackwaterRegion_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/BackwaterRegion/BackwaterRegion_ClusterAsset.BackwaterRegion_ClusterAsset' (0x000001BA89CC6700) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'BackwaterRegion_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/BackwaterRegion/BackwaterRegion_ClusterAsset.BackwaterRegion_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/BackwaterRegion/BackwaterRegion_ClusterAsset.BackwaterRegion_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/BackwaterRegion/BackwaterRegion_ClusterAsset.BackwaterRegion_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/BackwaterRegion/BackwaterRegion_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/BackwaterRegion/BackwaterRegion_ClusterAsset.BackwaterRegion_ClusterAsset' (0x000001BA89CC6700) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39EA70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "BackwaterRegion_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39EA70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "BackwaterRegion_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39E9D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39E9D0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/9_1/PlaceMarik-LiaoBorderCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Marik-LiaoBorder/Marik-LiaoBorder_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/Marik-LiaoBorder/Marik-LiaoBorder_ClusterAsset.Marik-LiaoBorder_ClusterAsset' (0x000001BA89D03600) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'Marik-LiaoBorder_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/Marik-LiaoBorder/Marik-LiaoBorder_ClusterAsset.Marik-LiaoBorder_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/Marik-LiaoBorder/Marik-LiaoBorder_ClusterAsset.Marik-LiaoBorder_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/Marik-LiaoBorder/Marik-LiaoBorder_ClusterAsset.Marik-LiaoBorder_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/Marik-LiaoBorder/Marik-LiaoBorder_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/Marik-LiaoBorder/Marik-LiaoBorder_ClusterAsset.Marik-LiaoBorder_ClusterAsset' (0x000001BA89D03600) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39FD30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Marik-LiaoBorder_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB39FD30) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "Marik-LiaoBorder_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39FC90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB39FC90) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/9_2/PlaceVacantWorldsCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/VacantWorlds/VacantWorlds_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/VacantWorlds/VacantWorlds_ClusterAsset.VacantWorlds_ClusterAsset' (0x000001BA9C357B00) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'VacantWorlds_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/VacantWorlds/VacantWorlds_ClusterAsset.VacantWorlds_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/VacantWorlds/VacantWorlds_ClusterAsset.VacantWorlds_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/VacantWorlds/VacantWorlds_ClusterAsset.VacantWorlds_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/VacantWorlds/VacantWorlds_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/VacantWorlds/VacantWorlds_ClusterAsset.VacantWorlds_ClusterAsset' (0x000001BA9C357B00) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB3B1030) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "VacantWorlds_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB3B1030) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "VacantWorlds_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB3B0F90) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB3B0F90) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/9_3/PlaceFreeWorldInteriorCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/FreeWorldInterior/FreeWorldInterior_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/FreeWorldInterior/FreeWorldInterior_ClusterAsset.FreeWorldInterior_ClusterAsset' (0x000001BA89CC7B00) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'FreeWorldInterior_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/FreeWorldInterior/FreeWorldInterior_ClusterAsset.FreeWorldInterior_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/FreeWorldInterior/FreeWorldInterior_ClusterAsset.FreeWorldInterior_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/FreeWorldInterior/FreeWorldInterior_ClusterAsset.FreeWorldInterior_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/FreeWorldInterior/FreeWorldInterior_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/FreeWorldInterior/FreeWorldInterior_ClusterAsset.FreeWorldInterior_ClusterAsset' (0x000001BA89CC7B00) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB3B1DF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "FreeWorldInterior_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB3B1DF0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "FreeWorldInterior_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB3B1D50) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB3B1D50) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/9_4/PlaceFreeWorldCommerceHubCluster_ArcAction`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/FreeWorldCommerceHub/FreeWorldCommerceHub_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/FreeWorldCommerceHub/FreeWorldCommerceHub_ClusterAsset.FreeWorldCommerceHub_ClusterAsset' (0x000001BA89CC7880) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'FreeWorldCommerceHub_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/FreeWorldCommerceHub/FreeWorldCommerceHub_ClusterAsset.FreeWorldCommerceHub_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/FreeWorldCommerceHub/FreeWorldCommerceHub_ClusterAsset.FreeWorldCommerceHub_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/FreeWorldCommerceHub/FreeWorldCommerceHub_ClusterAsset.FreeWorldCommerceHub_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/FreeWorldCommerceHub/FreeWorldCommerceHub_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/FreeWorldCommerceHub/FreeWorldCommerceHub_ClusterAsset.FreeWorldCommerceHub_ClusterAsset' (0x000001BA89CC7880) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB3B2570) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "FreeWorldCommerceHub_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB3B2570) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "FreeWorldCommerceHub_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB3B24D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB3B24D0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/PlaceCluster_SC01`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/SC01/SC01_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/SC01/SC01_ClusterAsset.SC01_ClusterAsset' (0x000001BA9C3556C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SC01_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/SC01/SC01_ClusterAsset.SC01_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/SC01/SC01_ClusterAsset.SC01_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/SC01/SC01_ClusterAsset.SC01_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/SC01/SC01_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/SC01/SC01_ClusterAsset.SC01_ClusterAsset' (0x000001BA9C3556C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB3B2A70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SC01_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB3B2A70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SC01_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB3B29D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB3B29D0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/StoryCluster_02/PlaceCluster_SC02`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/SC02/SC02_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/SC02/SC02_ClusterAsset.SC02_ClusterAsset' (0x000001BA9C355940) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SC02_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/SC02/SC02_ClusterAsset.SC02_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/SC02/SC02_ClusterAsset.SC02_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/SC02/SC02_ClusterAsset.SC02_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/SC02/SC02_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/SC02/SC02_ClusterAsset.SC02_ClusterAsset' (0x000001BA9C355940) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB3B30B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SC02_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB3B30B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SC02_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB3B3010) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB3B3010) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/StoryCluster_03/PlaceCluster_SC03`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/SC03/SC03_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/SC03/SC03_ClusterAsset.SC03_ClusterAsset' (0x000001BA9C355A80) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SC03_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/SC03/SC03_ClusterAsset.SC03_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/SC03/SC03_ClusterAsset.SC03_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/SC03/SC03_ClusterAsset.SC03_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/SC03/SC03_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/SC03/SC03_ClusterAsset.SC03_ClusterAsset' (0x000001BA9C355A80) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB3B3970) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SC03_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB3B3970) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SC03_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB3B38D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB3B38D0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/StoryCluster_04/PlaceCluster_SC04`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/SC04/SC04_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/SC04/SC04_ClusterAsset.SC04_ClusterAsset' (0x000001BA9C355BC0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SC04_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/SC04/SC04_ClusterAsset.SC04_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/SC04/SC04_ClusterAsset.SC04_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/SC04/SC04_ClusterAsset.SC04_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/SC04/SC04_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/SC04/SC04_ClusterAsset.SC04_ClusterAsset' (0x000001BA9C355BC0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB3B3E70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SC04_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB3B3E70) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SC04_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB3B3DD0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB3B3DD0) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/StoryCluster_05/PlaceCluster_SC05`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/SC05/SC05_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/SC05/SC05_ClusterAsset.SC05_ClusterAsset' (0x000001BA9C355E40) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SC05_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/SC05/SC05_ClusterAsset.SC05_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/SC05/SC05_ClusterAsset.SC05_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/SC05/SC05_ClusterAsset.SC05_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/SC05/SC05_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/SC05/SC05_ClusterAsset.SC05_ClusterAsset' (0x000001BA9C355E40) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB3B17B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SC05_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB3B17B0) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SC05_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB3B1710) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB3B1710) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/StoryCluster_06/PlaceCluster_SC06`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/SC06/SC06_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/SC06/SC06_ClusterAsset.SC06_ClusterAsset' (0x000001BA9C3560C0) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SC06_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/SC06/SC06_ClusterAsset.SC06_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/SC06/SC06_ClusterAsset.SC06_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/SC06/SC06_ClusterAsset.SC06_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/SC06/SC06_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/SC06/SC06_ClusterAsset.SC06_ClusterAsset' (0x000001BA9C3560C0) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB3B0630) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SC06_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB3B0630) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SC06_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB3B0590) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB3B0590) {id: 0}>"}}`

### `/Game/Campaign/CampaignArcs/Regions/StoryCluster_07/PlaceCluster_SC07`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/SC07/SC07_ClusterAsset']`
- cdo focused properties: `{'ClusterDataAsset': {'value': {'repr': "<Object '/Game/Campaign/Clusters/SC07/SC07_ClusterAsset.SC07_ClusterAsset' (0x000001BA9C356200) Class 'MWClusterDataAsset'>", 'python_type': 'MWClusterDataAsset', 'get_name': 'SC07_ClusterAsset', 'get_path_name': '/Game/Campaign/Clusters/SC07/SC07_ClusterAsset.SC07_ClusterAsset', 'get_full_name': 'MWClusterDataAsset /Game/Campaign/Clusters/SC07/SC07_ClusterAsset.SC07_ClusterAsset', 'unreal_class': 'MWClusterDataAsset', 'unreal_class_path': '/Script/MechWarrior.MWClusterDataAsset'}, 'path': '/Game/Campaign/Clusters/SC07/SC07_ClusterAsset.SC07_ClusterAsset', 'asset_paths': ['/Game/Campaign/Clusters/SC07/SC07_ClusterAsset'], 'repr': "<Object '/Game/Campaign/Clusters/SC07/SC07_ClusterAsset.SC07_ClusterAsset' (0x000001BA9C356200) Class 'MWClusterDataAsset'>"}, 'ClusterDataAssetId': {'value': {'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB3B1670) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SC07_ClusterAsset"}}>', 'python_type': 'ClusterDataAssetId'}, 'path': None, 'asset_paths': [], 'repr': '<Struct \'ClusterDataAssetId\' (0x000001BABB3B1670) {id: {primary_asset_type: {name: "MWClusterDataAsset"}, primary_asset_name: "SC07_ClusterAsset"}}>'}, 'campaign_arc_action_id': {'value': {'repr': "<Struct 'CampaignArcActionId' (0x000001BABB3B15D0) {id: 0}>", 'python_type': 'CampaignArcActionId'}, 'path': None, 'asset_paths': [], 'repr': "<Struct 'CampaignArcActionId' (0x000001BABB3B15D0) {id: 0}>"}}`

### `/Game/Campaign/_common/MW5_ClusterAssetCacheActor`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `Blueprint` exists `True`
- referenced clusters: `['/Game/Campaign/_common/MW5_ClusterAssetCacheActor']`

### `/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets`
- depth/reason: `2` / `referenced by /Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- class: `EditorUtilityWidgetBlueprint` exists `True`
- referenced clusters: `['/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets']`

### `/Game/Campaign/Clusters/A2M1/A2M1_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/A2M1/A2M1_ClusterAsset']`

### `/Game/Campaign/Clusters/A2M2/A2M2_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/A2M2/A2M2_ClusterAsset']`

### `/Game/Campaign/Clusters/A2M3/A2M3_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/A2M3/A2M3_ClusterAsset']`

### `/Game/Campaign/Clusters/Alarion/Alarion_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Alarion/Alarion_ClusterAsset']`

### `/Game/Campaign/Clusters/BackwaterRegion/BackwaterRegion_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/BackwaterRegion/BackwaterRegion_ClusterAsset']`

### `/Game/Campaign/Clusters/Davion-KuritaFrontline/Davion-KuritaFrontline_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Davion-KuritaFrontline/Davion-KuritaFrontline_ClusterAsset']`

### `/Game/Campaign/Clusters/DavionBorderlands/DavionBorderlands`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWFactionAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/DavionBorderlands/DavionBorderlands_ClusterAsset', '/Game/DLC1/CareerMode/Clusters/D_13_14/D_13_14_ClusterAsset', '/Game/DLC1/CareerMode/Clusters/L_13_14/L_13_14_ClusterAsset']`

### `/Game/Campaign/Clusters/DavionBorderlands/DavionBorderlands_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/DavionBorderlands/DavionBorderlands_ClusterAsset']`

### `/Game/Campaign/Clusters/DuchyOfAndurien/DuchyOfAndurien_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/DuchyOfAndurien/DuchyOfAndurien_ClusterAsset']`

### `/Game/Campaign/Clusters/DuchyOfTamarind/DuchyOfTamarind_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/DuchyOfTamarind/DuchyOfTamarind_ClusterAsset']`

### `/Game/Campaign/Clusters/DuchyOfTsitsang/DuchyOfTsitsang_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/DuchyOfTsitsang/DuchyOfTsitsang_ClusterAsset']`

### `/Game/Campaign/Clusters/FWL_ShippingLane/FWL_ShippingLane_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/FWL_ShippingLane/FWL_ShippingLane_ClusterAsset']`

### `/Game/Campaign/Clusters/FreeWorldCommerceHub/FreeWorldCommerceHub_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/FreeWorldCommerceHub/FreeWorldCommerceHub_ClusterAsset']`

### `/Game/Campaign/Clusters/FreeWorldInterior/FreeWorldInterior_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/FreeWorldInterior/FreeWorldInterior_ClusterAsset']`

### `/Game/Campaign/Clusters/HerotitusZone/HerotitusZone_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/HerotitusZone/HerotitusZone_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_1/IndustrialHub_1_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_1/IndustrialHub_1_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_10/IndustrialHub_10_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_10/IndustrialHub_10_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_11/IndustrialHub_11_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_11/IndustrialHub_11_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_12/IndustrialHub_12_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_12/IndustrialHub_12_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_13/IndustrialHub_13_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_13/IndustrialHub_13_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_14/IndustrialHub_14_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_14/IndustrialHub_14_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_15/IndustrialHub_15_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_15/IndustrialHub_15_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_16/IndustrialHub_16_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_16/IndustrialHub_16_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_18/IndustrialHub_18_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_18/IndustrialHub_18_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_19/IndustrialHub_19_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_19/IndustrialHub_19_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_2/IndustrialHub_2_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_2/IndustrialHub_2_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_20/IndustrialHub_20_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_20/IndustrialHub_20_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_21/IndustrialHub_21_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_21/IndustrialHub_21_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_23/IndustrialHub_23_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_23/IndustrialHub_23_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_24/IndustrialHub_24_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_24/IndustrialHub_24_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_25/IndustrialHub_25_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_25/IndustrialHub_25_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_26/IndustrialHub_26_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_26/IndustrialHub_26_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_27/IndustrialHub_27_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_27/IndustrialHub_27_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_28/IndustrialHub_28_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_28/IndustrialHub_28_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_3/IndustrialHub_3_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_3/IndustrialHub_3_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_30/IndustrialHub_30_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_30/IndustrialHub_30_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_31/IndustrialHub_31_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_31/IndustrialHub_31_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_4/IndustrialHub_4_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_4/IndustrialHub_4_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_5/IndustrialHub_5_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_5/IndustrialHub_5_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_6/IndustrialHub_6_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_6/IndustrialHub_6_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_7/IndustrialHub_7_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_7/IndustrialHub_7_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_8/IndustrialHub_8_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_8/IndustrialHub_8_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialHub_9/IndustrialHub_9_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialHub_9/IndustrialHub_9_ClusterAsset']`

### `/Game/Campaign/Clusters/IndustrialMiningCollective/IndustrialMiningCollective_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/IndustrialMiningCollective/IndustrialMiningCollective_ClusterAsset']`

### `/Game/Campaign/Clusters/InfernosWake/InfernosWake_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/InfernosWake/InfernosWake_ClusterAsset']`

### `/Game/Campaign/Clusters/Kurita-DavionFrontLine/Kurita-DavionFrontLine_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Kurita-DavionFrontLine/Kurita-DavionFrontLine_ClusterAsset']`

### `/Game/Campaign/Clusters/Liao-DavionBorder/DavionBorder`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWFactionAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Liao-DavionBorder/Liao-DavionBorder_ClusterAsset', '/Game/DLC1/CareerMode/Clusters/L_3_6/L_3_6_ClusterAsset']`

### `/Game/Campaign/Clusters/Liao-DavionBorder/Liao-DavionBorder_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Liao-DavionBorder/Liao-DavionBorder_ClusterAsset']`

### `/Game/Campaign/Clusters/LyranMilitaryStrongholds/LyranMilitaryStrongholds_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/LyranMilitaryStrongholds/LyranMilitaryStrongholds_ClusterAsset']`

### `/Game/Campaign/Clusters/Marik-LiaoBorder/Marik-LiaoBorder_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Marik-LiaoBorder/Marik-LiaoBorder_ClusterAsset']`

### `/Game/Campaign/Clusters/Marik-LiaoBorder/MarikLiaoBorder`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWFactionAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Marik-LiaoBorder/Marik-LiaoBorder_ClusterAsset', '/Game/DLC1/CareerMode/Clusters/M_5_8/M_5_8_ClusterAsset']`

### `/Game/Campaign/Clusters/Marik-StrinerBorder/Marik-StrinerBorder_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Marik-StrinerBorder/Marik-StrinerBorder_ClusterAsset']`

### `/Game/Campaign/Clusters/Marik-StrinerBorder/SteinerMarikBorder`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWFactionAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Marik-StrinerBorder/Marik-StrinerBorder_ClusterAsset', '/Game/DLC1/CareerMode/Clusters/M_12_13/M_12_13_ClusterAsset']`

### `/Game/Campaign/Clusters/MercenaryRow/MercenaryRow_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/MercenaryRow/MercenaryRow_ClusterAsset']`

### `/Game/Campaign/Clusters/Outreach/Outreach_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Outreach/Outreach_ClusterAsset']`

### `/Game/Campaign/Clusters/OutworldsAlliance/OutworldsAlliance_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/OutworldsAlliance/OutworldsAlliance_ClusterAsset']`

### `/Game/Campaign/Clusters/Rashpur-OwensMenufacturingWorlds/Rashpur-OwensMenufacturingWorlds_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Rashpur-OwensMenufacturingWorlds/Rashpur-OwensMenufacturingWorlds_ClusterAsset']`

### `/Game/Campaign/Clusters/RebelliousLyranPrince/RebelliousLyranPrince_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/RebelliousLyranPrince/RebelliousLyranPrince_ClusterAsset']`

### `/Game/Campaign/Clusters/Rogue/Rogue_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Rogue/Rogue_ClusterAsset']`

### `/Game/Campaign/Clusters/SC01/SC01_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/SC01/SC01_ClusterAsset']`

### `/Game/Campaign/Clusters/SC02/SC02_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/SC02/SC02_ClusterAsset']`

### `/Game/Campaign/Clusters/SC03/SC03_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/SC03/SC03_ClusterAsset']`

### `/Game/Campaign/Clusters/SC04/SC04_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/SC04/SC04_ClusterAsset']`

### `/Game/Campaign/Clusters/ShippingRoute/ShippingRoute_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/ShippingRoute/ShippingRoute_ClusterAsset']`

### `/Game/Campaign/Clusters/SianCommonality/SianCommonality_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/SianCommonality/SianCommonality_ClusterAsset']`

### `/Game/Campaign/Clusters/Steiner-KuritaBorder/Steiner-KuritaBorder_PostClanReplacement_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Steiner-KuritaBorder/Steiner-KuritaBorder_PostClanReplacement_ClusterAsset']`

### `/Game/Campaign/Clusters/Steiner-KuritaBorder/SteinerBorder`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWFactionAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Steiner-KuritaBorder/Steiner-KuritaBorder_ClusterAsset', '/Game/Campaign/Clusters/Steiner-KuritaBorder/Steiner-KuritaBorder_PostClanReplacement_ClusterAsset', '/Game/DLC1/CareerMode/Clusters/S_6_9/S_6_9_ClusterAsset']`

### `/Game/Campaign/Clusters/StweartCommonwealth/StweartCommonwealth_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/StweartCommonwealth/StweartCommonwealth_ClusterAsset']`

### `/Game/Campaign/Clusters/Taurian/Taurian_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/Taurian/Taurian_ClusterAsset']`

### `/Game/Campaign/Clusters/VacantWorlds/VacantWorlds_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/VacantWorlds/VacantWorlds_ClusterAsset']`

### `/Game/Campaign/Clusters/WesterhandZone/WesterhandZone_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/Campaign/Clusters/WesterhandZone/WesterhandZone_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/D_11_12/D_11_12_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_11_12/D_11_12_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/D_12_13/D_12_13_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_12_13/D_12_13_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/D_13_14/D_13_14_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_13_14/D_13_14_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/D_15/CareerCluster_4`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWFactionAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_15/D_15_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/D_15/D_15_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_15/D_15_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/D_1_2/D_1_2_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_1_2/D_1_2_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/D_2_3/CareerCluster_1`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWFactionAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_2_3/D_2_3_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/D_2_3/D_2_3_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_2_3/D_2_3_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/D_2_4/D_2_4_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_2_4/D_2_4_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/D_3_5/D_3_5_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_3_5/D_3_5_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/D_3_6/D_3_6_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_3_6/D_3_6_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/D_4_6/CareerCluster_13`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWFactionAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_4_6/D_4_6_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/D_4_6/D_4_6_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_4_6/D_4_6_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/D_5_7/CareerCluster_11`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWFactionAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_5_7/D_5_7_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/D_5_7/D_5_7_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_5_7/D_5_7_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/D_5_8/D_5_8_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_5_8/D_5_8_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/D_6_7/CareerCluster_12`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWFactionAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_6_7/D_6_7_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/D_6_7/D_6_7_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_6_7/D_6_7_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/D_6_8/CareerCluster_10`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWFactionAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_6_8/D_6_8_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/D_6_8/D_6_8_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_6_8/D_6_8_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/D_7_10/D_7_10_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/D_7_10/D_7_10_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/K_12_13/K_12_13_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_12_13/K_12_13_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/K_13_14/CareerCluster_5`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWFactionAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_13_14/K_13_14_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/K_13_14/K_13_14_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_13_14/K_13_14_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/K_3_5/K_3_5_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_3_5/K_3_5_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/K_6_7/CareerCluster_14`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWFactionAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_6_7/K_6_7_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/K_6_7/K_6_7_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_6_7/K_6_7_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/K_6_8/CareerCluster_15`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWFactionAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_6_8/K_6_8_ClusterAsset']`

### `/Game/DLC1/CareerMode/Clusters/K_6_8/K_6_8_ClusterAsset`
- depth/reason: `2` / `referenced by /Game/Campaign/Clusters/_common/Faction_StringTable`
- class: `MWClusterDataAsset` exists `True`
- referenced clusters: `['/Game/DLC1/CareerMode/Clusters/K_6_8/K_6_8_ClusterAsset']`
