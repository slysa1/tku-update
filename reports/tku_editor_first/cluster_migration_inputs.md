# Cluster Migration Inputs

This report compares the current editor cluster pipeline against the original unaltered TKU cooked InnerSphere table. It does not modify the editor, game, or original TKU backup.

## Current Editor Runtime CSV

- rows: `2173`
- nonempty cluster rows: `824`
- unique nonempty cluster ids: `77`
- cluster overlay rows: `74`
- cluster constellation rows: `31`

Top cluster ids:
- `TaurianCorridor`: `43`
- `OutworldsBorder`: `28`
- `LowerClassWorlds`: `25`
- `AlarionPeriphery`: `24`
- `LyranStrongholds`: `23`
- `DavionBorder`: `22`
- `DavionKurita_1`: `21`
- `RepairSystem_20`: `21`
- `RebeliousLyranTerritory`: `18`
- `SteinerBorder`: `18`
- `RasalagueReaches`: `18`
- `MarikLiaoBorder`: `17`
- `FWLInterior`: `17`
- `SianCommonality`: `17`
- `DutchyOfAndurien`: `17`
- `AgriculturalBelt`: `16`
- `DavionBorderlands`: `16`
- `FWLCommercialHub`: `16`
- `DroughtWorlds`: `16`
- `SteinerMarikBorder`: `15`
- `InfernosWake`: `15`
- `RepairSystem_26`: `14`
- `IndustrialMiningCompany`: `14`
- `StewartCommonality`: `13`
- `TheJunkyard`: `13`
- `PirateCluster`: `13`
- `RepairSystem_27`: `12`
- `RogueSystems`: `12`
- `BackwaterRegion`: `12`
- `MercenaryRow`: `12`

## Current Editor Cluster Assets

- `MWClusterDataAsset` count: `79`
- total system id memberships: `815`
- CSV cluster ids missing matching editor cluster faction names: `4`
- editor cluster faction names not found in CSV ids: `4`

- `/Game/Campaign/Clusters/A2M1/A2M1_ClusterAsset` systems `10` faction `RefinerySystems`
- `/Game/Campaign/Clusters/A2M2/A2M2_ClusterAsset` systems `13` faction `TheJunkyard`
- `/Game/Campaign/Clusters/A2M3/A2M3_ClusterAsset` systems `15` faction `AgriculturalBelt`
- `/Game/Campaign/Clusters/Alarion/Alarion_ClusterAsset` systems `24` faction `AlarionPeriphery`
- `/Game/Campaign/Clusters/BackwaterRegion/BackwaterRegion_ClusterAsset` systems `11` faction `BackwaterRegion`
- `/Game/Campaign/Clusters/Davion-KuritaFrontline/Davion-KuritaFrontline_ClusterAsset` systems `21` faction `DavionKurita_1`
- `/Game/Campaign/Clusters/DavionBorderlands/DavionBorderlands_ClusterAsset` systems `14` faction `DavionBorderlands`
- `/Game/Campaign/Clusters/DraconisBadlands/DraconisBadlands_ClusterAsset` systems `11` faction `KuritanBadlands`
- `/Game/Campaign/Clusters/DroughtWorlds/DroughtWorlds_ClusterAsset` systems `16` faction `DroughtWorlds`
- `/Game/Campaign/Clusters/DuchyOfAndurien/DuchyOfAndurien_ClusterAsset` systems `17` faction `DutchyOfAndurien`
- `/Game/Campaign/Clusters/DuchyOfTamarind/DuchyOfTamarind_ClusterAsset` systems `11` faction `TamarindAbbey`
- `/Game/Campaign/Clusters/DuchyOfTsitsang/DuchyOfTsitsang_ClusterAsset` systems `10` faction `TsinghaiCommonality`
- `/Game/Campaign/Clusters/FreeWorldCommerceHub/FreeWorldCommerceHub_ClusterAsset` systems `17` faction `FWLCommercialHub`
- `/Game/Campaign/Clusters/FreeWorldInterior/FreeWorldInterior_ClusterAsset` systems `17` faction `FWLInterior`
- `/Game/Campaign/Clusters/FWL_ShippingLane/FWL_ShippingLane_ClusterAsset` systems `12` faction `FWLShippingRoute`
- `/Game/Campaign/Clusters/HerotitusZone/HerotitusZone_ClusterAsset` systems `1` faction `Herotitus`
- `/Game/Campaign/Clusters/IndustrialHub_1/IndustrialHub_1_ClusterAsset` systems `6` faction `RepairSystem_1`
- `/Game/Campaign/Clusters/IndustrialHub_10/IndustrialHub_10_ClusterAsset` systems `6` faction `RepairSystem_11`
- `/Game/Campaign/Clusters/IndustrialHub_11/IndustrialHub_11_ClusterAsset` systems `6` faction `RepairSystem_12`
- `/Game/Campaign/Clusters/IndustrialHub_12/IndustrialHub_12_ClusterAsset` systems `5` faction `RepairSystem_14`
- `/Game/Campaign/Clusters/IndustrialHub_13/IndustrialHub_13_ClusterAsset` systems `6` faction `RepairSystem_13`
- `/Game/Campaign/Clusters/IndustrialHub_14/IndustrialHub_14_ClusterAsset` systems `5` faction `RepairSystem_15`
- `/Game/Campaign/Clusters/IndustrialHub_15/IndustrialHub_15_ClusterAsset` systems `4` faction `RepairSystem_16`
- `/Game/Campaign/Clusters/IndustrialHub_16/IndustrialHub_16_ClusterAsset` systems `6` faction `RepairSystem_18`
- `/Game/Campaign/Clusters/IndustrialHub_17/IndustrialHub_17_ClusterAsset` systems `4` faction `RepairSystem_17`
- `/Game/Campaign/Clusters/IndustrialHub_18/IndustrialHub_18_ClusterAsset` systems `5` faction `RepairSystem_19`
- `/Game/Campaign/Clusters/IndustrialHub_19/IndustrialHub_19_ClusterAsset` systems `4` faction `RepairSystem_7`
- `/Game/Campaign/Clusters/IndustrialHub_2/IndustrialHub_2_ClusterAsset` systems `7` faction `RepairSystem_2`
- `/Game/Campaign/Clusters/IndustrialHub_20/IndustrialHub_20_ClusterAsset` systems `4` faction `RepairSystem_21`
- `/Game/Campaign/Clusters/IndustrialHub_21/IndustrialHub_21_ClusterAsset` systems `10` faction `RepairSystem_22`
- `/Game/Campaign/Clusters/IndustrialHub_22/IndustrialHub_22_ClusterAsset` systems `8` faction `RepairSystem_23`
- `/Game/Campaign/Clusters/IndustrialHub_23/IndustrialHub_23_ClusterAsset` systems `6` faction `RepairSystem_24`
- `/Game/Campaign/Clusters/IndustrialHub_24/IndustrialHub_24_ClusterAsset` systems `6` faction `RepairSystem_25`
- `/Game/Campaign/Clusters/IndustrialHub_25/IndustrialHub_25_ClusterAsset` systems `20` faction `RepairSystem_20`
- `/Game/Campaign/Clusters/IndustrialHub_26/IndustrialHub_26_ClusterAsset` systems `13` faction `RepairSystem_26`
- `/Game/Campaign/Clusters/IndustrialHub_27/IndustrialHub_27_ClusterAsset` systems `9` faction `RepairSystem_27`
- `/Game/Campaign/Clusters/IndustrialHub_28/IndustrialHub_28_ClusterAsset` systems `4` faction `RepairSystem_28`
- `/Game/Campaign/Clusters/IndustrialHub_29/IndustrialHub_29_ClusterAsset` systems `4` faction `RepairSystem_29`
- `/Game/Campaign/Clusters/IndustrialHub_3/IndustrialHub_3_ClusterAsset` systems `5` faction `RepairSystem_6`
- `/Game/Campaign/Clusters/IndustrialHub_30/IndustrialHub_30_ClusterAsset` systems `5` faction `RepairSystem_30`

## Current Place Cluster Actions

- place assets with cluster refs: `44`

- `/Game/Campaign/CampaignArcs/Regions/10_1/PlaceFWL_ShippingLaneCluster_ArcAction` refs `/Game/Campaign/Clusters/FWL_ShippingLane/FWL_ShippingLane_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/10_2/PlaceDuchyOfTamarindCluster_ArcAction` refs `/Game/Campaign/Clusters/DuchyOfTamarind/DuchyOfTamarind_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/10_3/PlaceMarik-StrinerBorderCluster_ArcAction` refs `/Game/Campaign/Clusters/Marik-StrinerBorder/Marik-StrinerBorder_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/11_1/PlaceStweartCommonwealthCluster_ArcAction` refs `/Game/Campaign/Clusters/StweartCommonwealth/StweartCommonwealth_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/11_2/PlaceRebelliousLyranPrinceCluster_ArcAction` refs `/Game/Campaign/Clusters/RebelliousLyranPrince/RebelliousLyranPrince_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/11_3/PlaceLyranMilitaryStrongholdsCluster_ArcAction` refs `/Game/Campaign/Clusters/LyranMilitaryStrongholds/LyranMilitaryStrongholds_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/12_1/PlaceSteiner-KuritaBorderCluster_ArcAction` refs `/Game/Campaign/Clusters/Steiner-KuritaBorder/Steiner-KuritaBorder_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/12_2/PlaceLower-ClassKuritanWorldsCluster_ArcAction` refs `/Game/Campaign/Clusters/Lower-ClassKuritanWorlds/Lower-ClassKuritanWorlds_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/12_3/PlaceRogueCluster_ArcAction` refs `/Game/Campaign/Clusters/Rogue/Rogue_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/12_4/PlacePiratesLairCluster_ArcAction` refs `/Game/Campaign/Clusters/PiratesLair/PiratesLair_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/13_1/PlaceDraconisBadlandsCluster_ArcaCtion` refs `/Game/Campaign/Clusters/DraconisBadlands/DraconisBadlands_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/13_2/PlaceDroughtWorldsCluster_ArcAction` refs `/Game/Campaign/Clusters/DroughtWorlds/DroughtWorlds_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/13_3/PlaceTheGraveyardCluster_ArcAction` refs `/Game/Campaign/Clusters/TheGraveyard/TheGraveyard_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/3_1/PlaceMercenaryRowCluster_ArcAction` refs `/Game/Campaign/Clusters/MercenaryRow/MercenaryRow_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/4_1/PlaceInfernosWakeCluster_ArcAction` refs `/Game/Campaign/Clusters/InfernosWake/InfernosWake_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/5_1/PlaceDavion-KuritaFrontlineCluster_ArcAction` refs `/Game/Campaign/Clusters/Davion-KuritaFrontline/Davion-KuritaFrontline_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/5_2/PlaceIndustrialMiningCollectiveCluster_ArcAction` refs `/Game/Campaign/Clusters/IndustrialMiningCollective/IndustrialMiningCollective_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/6_1/PlaceKurita-DavionFrontLineCluster_ArcAction` refs `/Game/Campaign/Clusters/Kurita-DavionFrontLine/Kurita-DavionFrontLine_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/6_2/PlaceDavionBorderlandsCluster_ArcAction` refs `/Game/Campaign/Clusters/DavionBorderlands/DavionBorderlands_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/6_3/PlaceShippingRouteCluster_ArcAction` refs `/Game/Campaign/Clusters/ShippingRoute/ShippingRoute_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/7_1/PlaceRashpur-OwensMenufacturingWorldsCluster_ArcAction` refs `/Game/Campaign/Clusters/Rashpur-OwensMenufacturingWorlds/Rashpur-OwensMenufacturingWorlds_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/7_2/PlaceDuchyOfTsitsangCluster_ArcAction` refs `/Game/Campaign/Clusters/DuchyOfTsitsang/DuchyOfTsitsang_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/8_1/PlaceSianCommonalityCluster_ArcAction` refs `/Game/Campaign/Clusters/SianCommonality/SianCommonality_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/8_2/PlaceLiao-DavionBorderCluster_ArcAction` refs `/Game/Campaign/Clusters/Liao-DavionBorder/Liao-DavionBorder_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/8_3/PlaceDuchyOfAndurienCluster_ArcAction` refs `/Game/Campaign/Clusters/DuchyOfAndurien/DuchyOfAndurien_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/8_4/PlaceBackwaterRegionCluster_ArcAction` refs `/Game/Campaign/Clusters/BackwaterRegion/BackwaterRegion_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/9_1/PlaceMarik-LiaoBorderCluster_ArcAction` refs `/Game/Campaign/Clusters/Marik-LiaoBorder/Marik-LiaoBorder_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/9_2/PlaceVacantWorldsCluster_ArcAction` refs `/Game/Campaign/Clusters/VacantWorlds/VacantWorlds_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/9_3/PlaceFreeWorldInteriorCluster_ArcAction` refs `/Game/Campaign/Clusters/FreeWorldInterior/FreeWorldInterior_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/9_4/PlaceFreeWorldCommerceHubCluster_ArcAction` refs `/Game/Campaign/Clusters/FreeWorldCommerceHub/FreeWorldCommerceHub_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/EndgameClusters/PlaceAlarion_ArcAction` refs `/Game/Campaign/Clusters/Alarion/Alarion_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/EndgameClusters/PlaceOutworldsAlliance_ArcAction` refs `/Game/Campaign/Clusters/OutworldsAlliance/OutworldsAlliance_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/EndgameClusters/PlaceRasalhague_ArcAction` refs `/Game/Campaign/Clusters/Rasalhague/Rasalhague_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/EndgameClusters/PlaceTaurian_ArcAction` refs `/Game/Campaign/Clusters/Taurian/Taurian_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/MercStars/Place_HerotitusZone` refs `/Game/Campaign/Clusters/HerotitusZone/HerotitusZone_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/MercStars/Place_Outreach` refs `/Game/Campaign/Clusters/Outreach/Outreach_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/MercStars/Place_WesterhandZone` refs `/Game/Campaign/Clusters/WesterhandZone/WesterhandZone_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/StoryCluster_01/PlaceCluster_SC01` refs `/Game/Campaign/Clusters/SC01/SC01_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/StoryCluster_02/PlaceCluster_SC02` refs `/Game/Campaign/Clusters/SC02/SC02_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/StoryCluster_03/PlaceCluster_SC03` refs `/Game/Campaign/Clusters/SC03/SC03_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/StoryCluster_04/PlaceCluster_SC04` refs `/Game/Campaign/Clusters/SC04/SC04_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/StoryCluster_05/PlaceCluster_SC05` refs `/Game/Campaign/Clusters/SC05/SC05_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/StoryCluster_06/PlaceCluster_SC06` refs `/Game/Campaign/Clusters/SC06/SC06_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`
- `/Game/Campaign/CampaignArcs/Regions/StoryCluster_07/PlaceCluster_SC07` refs `/Game/Campaign/Clusters/SC07/SC07_ClusterAsset`, `ClusterDataAsset`, `ClusterDataAssetId`

## Wide Source JSON

- rows: `3446`
- `Cluster` rows `1`, unique `1`
- `ClusterOverlay` rows `0`, unique `0`
- `ClusterConstellation` rows `0`, unique `0`

## Original TKU Cooked InnerSphere Strings

- string_count: `7461`
- asset path strings: `240`
- current editor cluster ids found in original cooked strings: `46`

Original term hit counts:
- `ClusterOverlay`: `1`
- `ClusterConstellation`: `1`
- `MWFactionAsset`: `1`
- `FactionBorderMeshes`: `80`
- `Regions/`: `80`
- `CustomContent/Zones_Clan`: `8`
- `Lyran`: `2`
- `Steiner`: `2`
- `Clan`: `19`
- `Taurian`: `1`
- `Outworlds`: `1`
- `Canopus`: `1`

Current cluster ids found in original TKU strings:
- `A2M1_Cluster`
- `AgriculturalBelt`
- `AlarionPeriphery`
- `BackwaterRegion`
- `DavionBorder`
- `DavionBorderlands`
- `DropshipGraveyard`
- `DroughtWorlds`
- `DutchyOfAndurien`
- `EmptyWorlds`
- `FWLCommercialHub`
- `FWLInterior`
- `FWLShippingRoute`
- `IndustrialMiningCompany`
- `InfernosWake`
- `KuritaBorder`
- `KuritaDavion`
- `KuritanBadlands`
- `LowerClassWorlds`
- `LyranStrongholds`
- `MarikLiaoBorder`
- `MercenaryRow`
- `OutworldsBorder`
- `PirateCluster`
- `RasalagueReaches`
- `RashpurOwensInc`
- `RebeliousLyranTerritory`
- `RepairSystem_3`
- `RogueSystems`
- `ShippingRoute`
- `SianCommonality`
- `SteinerBorder`
- `SteinerMarikBorder`
- `StewartCommonality`
- `StoryCluster1`
- `StoryCluster10`
- `StoryCluster2`
- `StoryCluster3`
- `StoryCluster4`
- `StoryCluster5`
- `StoryCluster6`
- `StoryCluster7`
- `TamarindAbbey`
- `TaurianCorridor`
- `TheJunkyard`
- `TsinghaiCommonality`

## Interpretation

- Current MW5 converts old `Cluster`, `ClusterOverlay`, and `ClusterConstellation` table fields into explicit `MWClusterDataAsset` assets.
- Original TKU build 38 does not contain modern cluster assets, but its cooked InnerSphere table still exposes old cluster field names, faction-like cluster IDs, and overlay mesh paths as strings.
- Terminal string extraction is not enough to reconstruct row-to-cluster mappings safely; the next evidence step is editor/tool inspection of the migration utility and a structured export path for original TKU `MW5_InnerSphereData`.