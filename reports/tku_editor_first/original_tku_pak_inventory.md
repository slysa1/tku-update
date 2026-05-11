# Original TKU Pak Inventory

This report inventories the unaltered TKU build-38 pak only. After the 2026-05-10 Nexus restore, the live TheKnownUniverse folder is the clean source under test; quarantined blind-build artifacts are not source evidence.

## Source

- pak: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TheKnownUniverse\Paks\TheKnownUniverse.pak`
- mount: `../../../MW5Mercs/`
- entry_count: `2709`
- pak_version: `11`
- compressed_or_encrypted_entries: `0`

## High-Signal Findings

- No path-level `/Game/Campaign/Clusters` assets exist in the original TKU pak.
- No scanned original TKU cooked asset strings mention `MWClusterDataAsset`.
- No scanned original TKU cooked asset strings mention `/Game/Campaign/Clusters`.
- The only path-level cluster-named original TKU assets are the `CareerModeCustomClusters` campaign arc sidecars.
- Original TKU contains many dated `StarMapBorderActor`, `Borders`, and `StarMapBordersUpdate_Action` plugin assets, consistent with an older border-overlay pipeline.
- Current MW5 editor evidence shows modern overlays also depend on `/Game/Campaign/Clusters` `MWClusterDataAsset` assets, which are absent from original TKU build 38.

## Path Categories

### `modern_cluster_assets`

- count: `0`

### `cluster_named_assets`

- count: `2`
- `/Plugins/TheKnownUniverse/Content/Regions/War/CareerModeCustomClusters.uasset`
- `/Plugins/TheKnownUniverse/Content/Regions/War/CareerModeCustomClusters.uexp`

### `starmap_assets`

- count: `134`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor.uasset`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor.uexp`
- `/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges.uasset`
- `/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges.uexp`
- `/Game/Levels/FrontEnd/StarMap.uexp`
- `/Game/Levels/FrontEnd/StarMap.umap`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL.uasset`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL.uexp`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL.uasset`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL.uexp`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF.uasset`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF.uexp`
- `/Game/UI/FrontEnd/Starmap/StarMapActor.uasset`
- `/Game/UI/FrontEnd/Starmap/StarMapActor.uexp`
- `/Game/UI/FrontEnd/Starmap/StarSystemBody.uasset`
- `/Game/UI/FrontEnd/Starmap/StarSystemBody.uexp`
- `/Game/UI/FrontEnd/StarMapPawn.uasset`
- `/Game/UI/FrontEnd/StarMapPawn.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/StarMapBorderActor2864-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/StarMapBorderActor2864-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/StarMapBordersUpdate_Action_2864-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/StarMapBordersUpdate_Action_2864-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3025-01-01/StarMapBorderActor3025-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3025-01-01/StarMapBorderActor3025-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3025-01-01/StarMapBordersUpdate_Action_3025-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3025-01-01/StarMapBordersUpdate_Action_3025-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3030-01-01/StarMapBorderActor3030-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3030-01-01/StarMapBorderActor3030-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3030-01-01/StarMapBordersUpdate_Action_3030-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3030-01-01/StarMapBordersUpdate_Action_3030-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3034-01-01/StarMapBorderActor3034-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3034-01-01/StarMapBorderActor3034-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3034-01-01/StarMapBordersUpdate_Action_3034-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3034-01-01/StarMapBordersUpdate_Action_3034-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3040-01-01/StarMapBorderActor3040-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3040-01-01/StarMapBorderActor3040-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3040-01-01/StarMapBordersUpdate_Action_3040-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3040-01-01/StarMapBordersUpdate_Action_3040-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3049-09-01/StarMapBorderActor3049-09-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3049-09-01/StarMapBorderActor3049-09-01.uexp`

### `border_assets`

- count: `182`
- `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015.uasset`
- `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015.uexp`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor.uasset`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor.uexp`
- `/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges.uasset`
- `/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges.uexp`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL.uasset`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/Borders2864-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/Borders2864-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/StarMapBorderActor2864-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/StarMapBorderActor2864-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/StarMapBordersUpdate_Action_2864-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/StarMapBordersUpdate_Action_2864-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3025-01-01/Borders3025-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3025-01-01/Borders3025-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3025-01-01/StarMapBorderActor3025-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3025-01-01/StarMapBorderActor3025-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3025-01-01/StarMapBordersUpdate_Action_3025-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3025-01-01/StarMapBordersUpdate_Action_3025-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3030-01-01/Borders3030-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3030-01-01/Borders3030-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3030-01-01/StarMapBorderActor3030-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3030-01-01/StarMapBorderActor3030-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3030-01-01/StarMapBordersUpdate_Action_3030-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3030-01-01/StarMapBordersUpdate_Action_3030-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3034-01-01/Borders3034-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3034-01-01/Borders3034-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3034-01-01/StarMapBorderActor3034-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3034-01-01/StarMapBorderActor3034-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3034-01-01/StarMapBordersUpdate_Action_3034-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3034-01-01/StarMapBordersUpdate_Action_3034-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3040-01-01/Borders3040-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3040-01-01/Borders3040-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3040-01-01/StarMapBorderActor3040-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3040-01-01/StarMapBorderActor3040-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3040-01-01/StarMapBordersUpdate_Action_3040-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3040-01-01/StarMapBordersUpdate_Action_3040-01-01.uexp`
- `/Plugins/TheKnownUniverse/Content/3049-09-01/Borders3049-09-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3049-09-01/Borders3049-09-01.uexp`

### `inner_sphere_data`

- count: `6`
- `/Game/InnerSphereData/MW5_InnerSphereData.uasset`
- `/Game/InnerSphereData/MW5_InnerSphereData.uexp`
- `/Game/InnerSphereData/Updated/EmployerInfoData.uasset`
- `/Game/InnerSphereData/Updated/EmployerInfoData.uexp`
- `/Game/InnerSphereData/Updated/SystemFactionChanges.uasset`
- `/Game/InnerSphereData/Updated/SystemFactionChanges.uexp`

### `root_factions_employers`

- count: `250`
- `/Game/Employers/ClanGhostBear.uasset`
- `/Game/Employers/ClanGhostBear.uexp`
- `/Game/Employers/ClanJadeFalcon.uasset`
- `/Game/Employers/ClanJadeFalcon.uexp`
- `/Game/Employers/ClanSmokeJaguar.uasset`
- `/Game/Employers/ClanSmokeJaguar.uexp`
- `/Game/Employers/ClanWolf.uasset`
- `/Game/Employers/ClanWolf.uexp`
- `/Game/Employers/Unused/AllianceOfGaledon.uasset`
- `/Game/Employers/Unused/AllianceOfGaledon.uexp`
- `/Game/Employers/Unused/AmarisEmpire.uasset`
- `/Game/Employers/Unused/AmarisEmpire.uexp`
- `/Game/Employers/Unused/AxumiteProvidence.uasset`
- `/Game/Employers/Unused/AxumiteProvidence.uexp`
- `/Game/Employers/Unused/AzamiBrotherhood.uasset`
- `/Game/Employers/Unused/AzamiBrotherhood.uexp`
- `/Game/Employers/Unused/AzamiCaliphate.uasset`
- `/Game/Employers/Unused/AzamiCaliphate.uexp`
- `/Game/Employers/Unused/CalderonProtectorate.uasset`
- `/Game/Employers/Unused/CalderonProtectorate.uexp`
- `/Game/Employers/Unused/CapellanCommonality.uasset`
- `/Game/Employers/Unused/CapellanCommonality.uexp`
- `/Game/Employers/Unused/CapellanHegemony.uasset`
- `/Game/Employers/Unused/CapellanHegemony.uexp`
- `/Game/Employers/Unused/ChainelaneIsles.uasset`
- `/Game/Employers/Unused/ChainelaneIsles.uexp`
- `/Game/Employers/Unused/ChaosMarch.uasset`
- `/Game/Employers/Unused/ChaosMarch.uexp`
- `/Game/Employers/Unused/ChestertonTradeFederation.uasset`
- `/Game/Employers/Unused/ChestertonTradeFederation.uexp`
- `/Game/Employers/Unused/ClanBloodSpirit.uasset`
- `/Game/Employers/Unused/ClanBloodSpirit.uexp`
- `/Game/Employers/Unused/ClanBurrock.uasset`
- `/Game/Employers/Unused/ClanBurrock.uexp`
- `/Game/Employers/Unused/ClanCloudCobra.uasset`
- `/Game/Employers/Unused/ClanCloudCobra.uexp`
- `/Game/Employers/Unused/ClanCoyote.uasset`
- `/Game/Employers/Unused/ClanCoyote.uexp`
- `/Game/Employers/Unused/ClanDiamondShark.uasset`
- `/Game/Employers/Unused/ClanDiamondShark.uexp`

### `plugin_campaign_arcs`

- count: `2424`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_10.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_10.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_12.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_12.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_13.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_13.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_14.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_14.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_15.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_15.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_16.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_16.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_17.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_17.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_18.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_18.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_19.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_19.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_2.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_2.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_20.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_20.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_25.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_25.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_26.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_26.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_27.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_27.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_28.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_28.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_29.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_29.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_3.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_3.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_30.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_30.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_32.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_32.uexp`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_34.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_34.uexp`

## String Token Hits

### `/Game/Campaign/Clusters`

- assets_with_token: `0`

### `MWClusterDataAsset`

- assets_with_token: `0`

### `ClusterDataAsset`

- assets_with_token: `0`

### `ClusterOverlay`

- assets_with_token: `2`
- sample assets:
- `/Game/InnerSphereData/MW5_InnerSphereData.uasset`
- `/Game/UI/FrontEnd/Starmap/StarSystemBody.uasset`
- sample strings:
- `ClusterOverlay`
- `CallFunc_GetClusterOverlayState_ReturnValue`
- `ClusterOverlayMeshComponent`
- `ClusterOverlayState`
- `CreateClusterOverlayMesh`
- `EClusterOverlayState`
- `GetClusterOverlayState`
- `L NewClusterOverlayState`

### `ClusterConstellation`

- assets_with_token: `2`
- sample assets:
- `/Game/InnerSphereData/MW5_InnerSphereData.uasset`
- `/Game/UI/FrontEnd/Starmap/StarSystemBody.uasset`
- sample strings:
- `ClusterConstellation`
- `ClusterConstellationMeshComponent`

### `cluster_overlay`

- assets_with_token: `0`

### `cluster_constellation`

- assets_with_token: `0`

### `PlaceCluster`

- assets_with_token: `9`
- sample assets:
- `/Plugins/TheKnownUniverse/Content/Regions/Safezones/PlaceSafeZone_Clan1_ArcAction.uasset`
- `/Plugins/TheKnownUniverse/Content/Regions/Safezones/PlaceSafeZone_Clan2_ArcAction.uasset`
- `/Plugins/TheKnownUniverse/Content/Regions/Safezones/PlaceSafeZone_Custom1_ArcAction.uasset`
- `/Plugins/TheKnownUniverse/Content/Regions/Safezones/PlaceSafeZone_Custom2_ArcAction.uasset`
- `/Plugins/TheKnownUniverse/Content/Regions/War/Place_ClanConflict_1.uasset`
- `/Plugins/TheKnownUniverse/Content/Regions/War/Place_ClanConflict_2.uasset`
- `/Plugins/TheKnownUniverse/Content/Regions/War/Place_ClanConflict_3.uasset`
- `/Plugins/TheKnownUniverse/Content/Regions/War/Place_ClanConflict_4.uasset`
- `/Plugins/TheKnownUniverse/Content/Regions/War/Place_CustomConflict.uasset`
- sample strings:
- `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- `Default__PlaceClusterToi_ArcAction_C`
- `PlaceClusterToi_ArcAction_C`
- `PlaceClusterToi_Config`
- `PlaceClusterToi_Markups`

### `PlaceClusterToi`

- assets_with_token: `9`
- sample assets:
- `/Plugins/TheKnownUniverse/Content/Regions/Safezones/PlaceSafeZone_Clan1_ArcAction.uasset`
- `/Plugins/TheKnownUniverse/Content/Regions/Safezones/PlaceSafeZone_Clan2_ArcAction.uasset`
- `/Plugins/TheKnownUniverse/Content/Regions/Safezones/PlaceSafeZone_Custom1_ArcAction.uasset`
- `/Plugins/TheKnownUniverse/Content/Regions/Safezones/PlaceSafeZone_Custom2_ArcAction.uasset`
- `/Plugins/TheKnownUniverse/Content/Regions/War/Place_ClanConflict_1.uasset`
- `/Plugins/TheKnownUniverse/Content/Regions/War/Place_ClanConflict_2.uasset`
- `/Plugins/TheKnownUniverse/Content/Regions/War/Place_ClanConflict_3.uasset`
- `/Plugins/TheKnownUniverse/Content/Regions/War/Place_ClanConflict_4.uasset`
- `/Plugins/TheKnownUniverse/Content/Regions/War/Place_CustomConflict.uasset`
- sample strings:
- `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- `Default__PlaceClusterToi_ArcAction_C`
- `PlaceClusterToi_ArcAction_C`
- `PlaceClusterToi_Config`
- `PlaceClusterToi_Markups`

### `CareerModeCustomClusters`

- assets_with_token: `2`
- sample assets:
- `/Plugins/TheKnownUniverse/Content/Regions/TKU_Zones.uasset`
- `/Plugins/TheKnownUniverse/Content/Regions/War/CareerModeCustomClusters.uasset`
- sample strings:
- `/TheKnownUniverse/Regions/War/CareerModeCustomClusters`
- `CareerModeCustomClusters`

### `StarMapBorderActor`

- assets_with_token: `61`
- sample assets:
- `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015.uasset`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor.uasset`
- `/Game/UI/FrontEnd/Starmap/StarMapActor.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/Borders2864-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/StarMapBorderActor2864-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3025-01-01/Borders3025-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3025-01-01/StarMapBorderActor3025-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3030-01-01/Borders3030-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3030-01-01/StarMapBorderActor3030-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3034-01-01/Borders3034-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3034-01-01/StarMapBorderActor3034-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3040-01-01/Borders3040-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3040-01-01/StarMapBorderActor3040-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3049-09-01/Borders3049-09-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3049-09-01/StarMapBorderActor3049-09-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3050-04-01/Borders3050-04-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3050-04-01/StarMapBorderActor3050-04-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3050-06-01/Borders3050-06-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3050-06-01/StarMapBorderActor3050-06-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3050-08-01/Borders3050-08-01.uasset`
- sample strings:
- `/TheKnownUniverse/2864-01-01/StarMapBorderActor2864-01-01`
- `/TheKnownUniverse/2864-01-01/StarMapBorderActor2864-01-01.StarMapBorderActor2864-01-01_C`
- `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor_C`
- `Default__BaseStarMapBorderActor_C`
- `Default__MWStarMapBorderActor`
- `MWStarMapBorderActor`
- `Default__StarMapBorderActor2864-01-01_C`
- `StarMapBorderActor2864-01-01_C`
- `/TheKnownUniverse/3025-01-01/StarMapBorderActor3025-01-01`
- `/TheKnownUniverse/3025-01-01/StarMapBorderActor3025-01-01.StarMapBorderActor3025-01-01_C`
- `Default__StarMapBorderActor3025-01-01_C`
- `StarMapBorderActor3025-01-01_C`
- `/TheKnownUniverse/3030-01-01/StarMapBorderActor3030-01-01`
- `/TheKnownUniverse/3030-01-01/StarMapBorderActor3030-01-01.StarMapBorderActor3030-01-01_C`
- `Default__StarMapBorderActor3030-01-01_C`
- `StarMapBorderActor3030-01-01_C`
- `/TheKnownUniverse/3034-01-01/StarMapBorderActor3034-01-01`
- `/TheKnownUniverse/3034-01-01/StarMapBorderActor3034-01-01.StarMapBorderActor3034-01-01_C`
- `Default__StarMapBorderActor3034-01-01_C`

### `BaseStarMapBorderActor`

- assets_with_token: `30`
- sample assets:
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/StarMapBorderActor2864-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3025-01-01/StarMapBorderActor3025-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3030-01-01/StarMapBorderActor3030-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3034-01-01/StarMapBorderActor3034-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3040-01-01/StarMapBorderActor3040-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3049-09-01/StarMapBorderActor3049-09-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3050-04-01/StarMapBorderActor3050-04-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3050-06-01/StarMapBorderActor3050-06-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3050-08-01/StarMapBorderActor3050-08-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3050-10-01/StarMapBorderActor3050-10-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3052-01-01/StarMapBorderActor3052-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3057-01-01/StarMapBorderActor3057-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3058-01-01/StarMapBorderActor3058-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3059-01-01/StarMapBorderActor3059-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3059-04-01/StarMapBorderActor3059-04-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3059-08-01/StarMapBorderActor3059-08-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3060-01-01/StarMapBorderActor3060-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3063-01-01/StarMapBorderActor3063-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3067-01-01/StarMapBorderActor3067-01-01.uasset`
- sample strings:
- `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor_C`
- `Default__BaseStarMapBorderActor_C`

### `StarMapBordersUpdate_Action`

- assets_with_token: `58`
- sample assets:
- `/Plugins/TheKnownUniverse/Content/2864-01-01/StarMapBordersUpdate_Action_2864-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/2864-01-01/year_2864-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3025-01-01/StarMapBordersUpdate_Action_3025-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3025-01-01/year_3025-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3030-01-01/StarMapBordersUpdate_Action_3030-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3030-01-01/year_3030-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3034-01-01/StarMapBordersUpdate_Action_3034-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3034-01-01/year_3034-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3040-01-01/StarMapBordersUpdate_Action_3040-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3040-01-01/year_3040-01-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3049-09-01/StarMapBordersUpdate_Action_3049-09-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3049-09-01/year_3049-09-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3050-04-01/StarMapBordersUpdate_Action_3050-04-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3050-04-01/year_3050-04-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3050-06-01/StarMapBordersUpdate_Action_3050-06-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3050-06-01/year_3050-06-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3050-08-01/StarMapBordersUpdate_Action_3050-08-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3050-08-01/year_3050-08-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3050-10-01/StarMapBordersUpdate_Action_3050-10-01.uasset`
- `/Plugins/TheKnownUniverse/Content/3050-10-01/year_3050-10-01.uasset`
- sample strings:
- `/TheKnownUniverse/2864-01-01/StarMapBordersUpdate_Action_2864-01-01`
- `Default__StarMapBordersUpdate_Action_2864-01-01_C`
- `StarMapBordersUpdate_Action_2864-01-01_C`
- `/TheKnownUniverse/2864-01-01/StarMapBordersUpdate_Action_2864-01-01.StarMapBordersUpdate_Action_2864-01-01_C`
- `/TheKnownUniverse/3025-01-01/StarMapBordersUpdate_Action_3025-01-01`
- `Default__StarMapBordersUpdate_Action_3025-01-01_C`
- `StarMapBordersUpdate_Action_3025-01-01_C`
- `/TheKnownUniverse/3025-01-01/StarMapBordersUpdate_Action_3025-01-01.StarMapBordersUpdate_Action_3025-01-01_C`
- `/TheKnownUniverse/3030-01-01/StarMapBordersUpdate_Action_3030-01-01`
- `Default__StarMapBordersUpdate_Action_3030-01-01_C`
- `StarMapBordersUpdate_Action_3030-01-01_C`
- `/TheKnownUniverse/3030-01-01/StarMapBordersUpdate_Action_3030-01-01.StarMapBordersUpdate_Action_3030-01-01_C`
- `/TheKnownUniverse/3034-01-01/StarMapBordersUpdate_Action_3034-01-01`
- `Default__StarMapBordersUpdate_Action_3034-01-01_C`
- `StarMapBordersUpdate_Action_3034-01-01_C`
- `/TheKnownUniverse/3034-01-01/StarMapBordersUpdate_Action_3034-01-01.StarMapBordersUpdate_Action_3034-01-01_C`
- `/TheKnownUniverse/3040-01-01/StarMapBordersUpdate_Action_3040-01-01`
- `Default__StarMapBordersUpdate_Action_3040-01-01_C`
- `StarMapBordersUpdate_Action_3040-01-01_C`
- `/TheKnownUniverse/3040-01-01/StarMapBordersUpdate_Action_3040-01-01.StarMapBordersUpdate_Action_3040-01-01_C`

### `PanBoundsHorizontal`

- assets_with_token: `1`
- sample assets:
- `/Game/UI/FrontEnd/StarMapPawn.uasset`
- sample strings:
- `PanBoundsHorizontal`

### `PanBoundsVertical`

- assets_with_token: `1`
- sample assets:
- `/Game/UI/FrontEnd/StarMapPawn.uasset`
- sample strings:
- `PanBoundsVertical`

### `ZoomDistanceList`

- assets_with_token: `1`
- sample assets:
- `/Game/UI/FrontEnd/StarMapPawn.uasset`
- sample strings:
- `ZoomDistanceList`

### `ZoomLevelThresholds`

- assets_with_token: `1`
- sample assets:
- `/Game/UI/FrontEnd/StarMapPawn.uasset`
- sample strings:
- `ZoomLevelThresholds`

### `Lyran`

- assets_with_token: `8`
- sample assets:
- `/Game/Employers/Unused/LyranAlliance.uasset`
- `/Game/Employers/Unused/LyranAlliance.uexp`
- `/Game/InnerSphereData/MW5_InnerSphereData.uasset`
- `/Game/InnerSphereData/Updated/EmployerInfoData.uasset`
- `/Plugins/TheKnownUniverse/Content/FactionColorMap.uasset`
- `/Plugins/TheKnownUniverse/Content/FactionMPC.uasset`
- `/Plugins/TheKnownUniverse/Content/Factions/LyranAlliance.uasset`
- `/Plugins/TheKnownUniverse/Content/Factions/LyranAlliance.uexp`
- sample strings:
- `/ModOverride/TheKnownUniverse/Employers/Unused/LyranAlliance`
- `LyranAlliance`
- `Lyran Alliance`
- `LyranStrongholds`
- `RebeliousLyranTerritory`
- `LyranCommonwealth`
- `/TheKnownUniverse/Factions/LyranAlliance`
- `EStarMapStencilId::LyranCommonwealth`

### `Steiner`

- assets_with_token: `4`
- sample assets:
- `/Game/Employers/Unused/FederationOfSkye.uasset`
- `/Game/InnerSphereData/MW5_InnerSphereData.uasset`
- `/Game/Libraries/MW5_TOI_Functions.uasset`
- `/Plugins/TheKnownUniverse/Content/Factions/LyranAlliance.uasset`
- sample strings:
- `Steiner`
- `SteinerBorder`
- `SteinerMarikBorder`
- `/Game/UI/Textures/Factions/main_factions/Faction_Steiner_1024PX_STD_UIX`
- `/Game/UI/Textures/Factions/main_factions/Faction_Steiner_1024PX_STD_UIX.Faction_Steiner_1024PX_STD_UIX`
- `/Game/UI/Textures/Factions/main_factions/Faction_Steiner_Logo_32px_UIX`
- `/Game/UI/Textures/Factions/main_factions/Faction_Steiner_Logo_32px_UIX.Faction_Steiner_Logo_32px_UIX`
- `PaintTheme.Faction.Steiner`
- `Persona.Faction.Steiner`

### `Clan`

- assets_with_token: `149`
- sample assets:
- `/Game/Campaign/Personas/ProcMissionPersonas/PersonaAnonymousEmployer.uasset`
- `/Game/Campaign/Personas/ProcMissionPersonas/PersonaAnonymousEmployer2.uasset`
- `/Game/Employers/ClanGhostBear.uasset`
- `/Game/Employers/ClanGhostBear.uexp`
- `/Game/Employers/ClanJadeFalcon.uasset`
- `/Game/Employers/ClanJadeFalcon.uexp`
- `/Game/Employers/ClanSmokeJaguar.uasset`
- `/Game/Employers/ClanSmokeJaguar.uexp`
- `/Game/Employers/ClanWolf.uasset`
- `/Game/Employers/ClanWolf.uexp`
- `/Game/Employers/Unused/ClanBloodSpirit.uasset`
- `/Game/Employers/Unused/ClanBloodSpirit.uexp`
- `/Game/Employers/Unused/ClanBurrock.uasset`
- `/Game/Employers/Unused/ClanBurrock.uexp`
- `/Game/Employers/Unused/ClanCloudCobra.uasset`
- `/Game/Employers/Unused/ClanCloudCobra.uexp`
- `/Game/Employers/Unused/ClanCoyote.uasset`
- `/Game/Employers/Unused/ClanCoyote.uexp`
- `/Game/Employers/Unused/ClanDiamondShark.uasset`
- `/Game/Employers/Unused/ClanDiamondShark.uexp`
- sample strings:
- `Persona.Faction.Clan`
- `/ModOverride/TheKnownUniverse/Employers/ClanGhostBear`
- `ClanGhostBear`
- `Clan Ghost Bear`
- `/ModOverride/TheKnownUniverse/Employers/ClanJadeFalcon`
- `ClanJadeFalcon`
- `Clan Jade Falcon`
- `/ModOverride/TheKnownUniverse/Employers/ClanSmokeJaguar`
- `ClanSmokeJaguar`
- `Clan Smoke Jaguar`
- `/ModOverride/TheKnownUniverse/Employers/ClanWolf`
- `ClanWolf`
- `Clan Wolf`
- `/ModOverride/TheKnownUniverse/Employers/Unused/ClanBloodSpirit`
- `ClanBloodSpirit`
- `Clan Blood Spirit`
- `/ModOverride/TheKnownUniverse/Employers/Unused/ClanBurrock`
- `ClanBurrock`
- `Clan Burrock`
- `/ModOverride/TheKnownUniverse/Employers/Unused/ClanCloudCobra`

## Border Timeline Buckets

- `2864-01-01`: `6` files
- `3025-01-01`: `6` files
- `3030-01-01`: `6` files
- `3034-01-01`: `6` files
- `3040-01-01`: `6` files
- `3049-09-01`: `6` files
- `3050-04-01`: `6` files
- `3050-06-01`: `6` files
- `3050-08-01`: `6` files
- `3050-10-01`: `6` files
- `3052-01-01`: `6` files
- `3057-01-01`: `6` files
- `3058-01-01`: `6` files
- `3059-01-01`: `6` files
- `3059-04-01`: `6` files
- `3059-08-01`: `6` files
- `3060-01-01`: `6` files
- `3063-01-01`: `6` files
- `3067-01-01`: `6` files
- `3068-01-01`: `6` files
- `3075-01-01`: `6` files
- `3079-01-01`: `6` files
- `3081-01-01`: `6` files
- `3085-01-01`: `6` files
- `3095-01-01`: `6` files
- `3130-01-01`: `6` files
- `3135-01-01`: `6` files
- `3145-01-01`: `6` files
- `3151-01-01`: `6` files

## Prefix Counts

- `/`: `2`
- `/Game/Campaign`: `10`
- `/Game/Employers`: `216`
- `/Game/Factions`: `34`
- `/Game/InnerSphereData`: `6`
- `/Game/Levels`: `2`
- `/Game/Libraries`: `2`
- `/Game/UI`: `12`
- `/Plugins`: `1`
- `/Plugins/TheKnownUniverse/Content/2864-01-01`: `68`
- `/Plugins/TheKnownUniverse/Content/3025-01-01`: `64`
- `/Plugins/TheKnownUniverse/Content/3030-01-01`: `68`
- `/Plugins/TheKnownUniverse/Content/3034-01-01`: `70`
- `/Plugins/TheKnownUniverse/Content/3040-01-01`: `66`
- `/Plugins/TheKnownUniverse/Content/3049-09-01`: `72`
- `/Plugins/TheKnownUniverse/Content/3050-04-01`: `72`
- `/Plugins/TheKnownUniverse/Content/3050-06-01`: `72`
- `/Plugins/TheKnownUniverse/Content/3050-08-01`: `72`
- `/Plugins/TheKnownUniverse/Content/3050-10-01`: `72`
- `/Plugins/TheKnownUniverse/Content/3052-01-01`: `72`
- `/Plugins/TheKnownUniverse/Content/3057-01-01`: `72`
- `/Plugins/TheKnownUniverse/Content/3058-01-01`: `74`
- `/Plugins/TheKnownUniverse/Content/3059-01-01`: `72`
- `/Plugins/TheKnownUniverse/Content/3059-04-01`: `72`
- `/Plugins/TheKnownUniverse/Content/3059-08-01`: `72`
- `/Plugins/TheKnownUniverse/Content/3060-01-01`: `72`
- `/Plugins/TheKnownUniverse/Content/3063-01-01`: `68`
- `/Plugins/TheKnownUniverse/Content/3067-01-01`: `66`
- `/Plugins/TheKnownUniverse/Content/3068-01-01`: `64`
- `/Plugins/TheKnownUniverse/Content/3075-01-01`: `66`
- `/Plugins/TheKnownUniverse/Content/3079-01-01`: `68`
- `/Plugins/TheKnownUniverse/Content/3081-01-01`: `72`
- `/Plugins/TheKnownUniverse/Content/3085-01-01`: `68`
- `/Plugins/TheKnownUniverse/Content/3095-01-01`: `72`
- `/Plugins/TheKnownUniverse/Content/3130-01-01`: `64`
- `/Plugins/TheKnownUniverse/Content/3135-01-01`: `66`
- `/Plugins/TheKnownUniverse/Content/3145-01-01`: `62`
- `/Plugins/TheKnownUniverse/Content/3151-01-01`: `60`
- `/Plugins/TheKnownUniverse/Content/Employers`: `12`
- `/Plugins/TheKnownUniverse/Content/FactionColorMangle_MTF.uasset`: `1`
- `/Plugins/TheKnownUniverse/Content/FactionColorMangle_MTF.uexp`: `1`
- `/Plugins/TheKnownUniverse/Content/FactionColorMap.uasset`: `1`
- `/Plugins/TheKnownUniverse/Content/FactionColorMap.uexp`: `1`
- `/Plugins/TheKnownUniverse/Content/FactionMPC.uasset`: `1`
- `/Plugins/TheKnownUniverse/Content/FactionMPC.uexp`: `1`
- `/Plugins/TheKnownUniverse/Content/Factions`: `372`
- `/Plugins/TheKnownUniverse/Content/Regions`: `34`
- `/Plugins/TheKnownUniverse/Content/TKUColorMap.uasset`: `1`
- `/Plugins/TheKnownUniverse/Content/TKUColorMap.uexp`: `1`

## Extension Counts

- `.bin`: `1`
- `.ini`: `2`
- `.uasset`: `1314`
- `.ubulk`: `76`
- `.uexp`: `1315`
- `.umap`: `1`