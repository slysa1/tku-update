# TKU Cooked Asset String Reference Scan

This is a terminal-only scan of strings embedded in selected cooked TKU assets. It is evidence for references and naming, not a substitute for MW5 Mod Editor inspection.

- Source pak: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TheKnownUniverse\Paks\TheKnownUniverse.pak`
- Selected exact files: 26

## Selected Assets

### `/Game/Levels/FrontEnd/StarMap`

- files: /Game/Levels/FrontEnd/StarMap.uexp, /Game/Levels/FrontEnd/StarMap.umap
- string_count: 1611
- notable tokens: Bounds, Camera, Faction, FactionBorder, Map, StarMap, StarMapActor, StarSystemBody, TheKnownUniverse, asset_paths

Key `asset_paths` examples:
- `/Game/Levels/FrontEnd/StarMapSceneManager`
- `/Game/Levels/FrontEnd/StarSystemSceneManager`
- `/Game/Levels/Lighting/_common/Textures/Starfields/hdr_starfield_01_TEX`
- `/Game/Levels/TestMaps/Test_Basic`
- `/Game/Modes/SceneManagers/SceneManager`
- `/Game/UI/FrontEnd/Starmap/AbstractStarSystem`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTI`
- `/Game/UI/FrontEnd/Starmap/Materials/Nebula_MST`
- `/Game/UI/FrontEnd/Starmap/Nebulae/Nebula`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_AClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_BClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_FClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_GClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_KClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_MClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/StarSystem`
- `BlueprintGeneratedClass`

Key `StarMapActor` examples:
- `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarMapActor`
- `Default__StarMapActor_C`
- `StarMapActor`
- `StarMapActor_C`

Key `StarSystemBody` examples:
- `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarSystemBody`
- `Default__StarSystemBody_C`
- `StarSystemBody_C`

Key `Faction` examples:
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTI`
- `FactionBorder_MTI`

Key `Bounds` examples:
- `BoxSphereBounds`
- `BuiltInstanceBounds`
- `CacheMeshExtendedBounds`

Key `Camera` examples:
- `CameraActor`
- `CameraComponent`
- `Default__CameraActor`
- `StarMapCamera`
- `StarSystemCamera`
- `StarSystemCamera_GEN_VARIABLE`

### `/Game/UI/FrontEnd/Starmap/StarMapActor`

- files: /Game/UI/FrontEnd/Starmap/StarMapActor.uasset, /Game/UI/FrontEnd/Starmap/StarMapActor.uexp
- string_count: 526
- notable tokens: Camera, InnerSphere, Map, StarMap, StarMapActor, StarMapBorderActor, StarSystemBody, TheKnownUniverse, asset_paths

Key `asset_paths` examples:
- `/Game/InnerSphereData/StarMapBP_UTILS`
- `/Game/UI/FrontEnd/Starmap/AbstractStarSystem`
- `/Game/UI/FrontEnd/Starmap/Cluster_MTI`
- `/Game/UI/FrontEnd/Starmap/CurrentCourse_MTI`
- `/Game/UI/FrontEnd/Starmap/cylinder_STM`
- `/Game/UI/FrontEnd/Starmap/Materials/FogOfWar_MTL`
- `/Game/UI/FrontEnd/Starmap/Materials/FogOfWarRenderTarget`
- `/Game/UI/FrontEnd/Starmap/Materials/FogOfWarSplat_MTL`
- `/Game/UI/FrontEnd/Starmap/MaxTravelDistance_MTI`
- `/Game/UI/FrontEnd/Starmap/Nebulae/Nebula`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_AClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_BClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_FClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_GClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_KClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_MClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/StarMapRoute_MTI`
- `/Game/UI/FrontEnd/Starmap/StarMapSelectionActor`
- `/Game/UI/FrontEnd/Starmap/StarMapSelectionActor.StarMapSelectionActor_C`
- `/Game/UI/FrontEnd/Starmap/StarSystem`

Key `StarMapActor` examples:
- `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarMapActor`
- `Default__StarMapActor_C`
- `ExecuteUbergraph_StarMapActor`
- `StarMapActor_C`

Key `StarSystemBody` examples:
- `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarSystemBody`
- `Default__StarSystemBody_C`
- `FindStarSystemBodyById`
- `MWStarSystemBody`
- `StarSystemBody_C`
- `StarSystemBodyLookUp`

Key `Camera` examples:
- `Camera`
- `CameraActor`
- `CameraComponent`
- `InitialCameraTransform`
- `StarMapCamera`
- `StarSystemCamera_GEN_VARIABLE`

### `/Game/UI/FrontEnd/StarMapPawn`

- files: /Game/UI/FrontEnd/StarMapPawn.uasset, /Game/UI/FrontEnd/StarMapPawn.uexp
- string_count: 56
- notable tokens: Bounds, Map, StarMap, StarMapPawn, TheKnownUniverse, Zoom, asset_paths

Key `asset_paths` examples:
- `/Game/UI/FrontEnd/StarMap_MPC`
- `/Game/UI/FrontEnd/StarmapGamepadWidget`
- `BlueprintGeneratedClass`

Key `StarMapPawn` examples:
- `/ModOverride/TheKnownUniverse/UI/FrontEnd/StarMapPawn`
- `Default__MWStarMapPawn`
- `Default__StarMapPawn_C`
- `MWStarMapPawn`
- `StarMapPawn_C`

Key `Bounds` examples:
- `PanBoundsHorizontal`
- `PanBoundsVertical`

Key `Zoom` examples:
- `ZoomDistanceList`
- `ZoomLevelThresholds`

### `/Game/UI/FrontEnd/Starmap/StarSystemBody`

- files: /Game/UI/FrontEnd/Starmap/StarSystemBody.uasset, /Game/UI/FrontEnd/Starmap/StarSystemBody.uexp
- string_count: 377
- notable tokens: Camera, Faction, Map, StarMap, StarMapActor, StarSystemBody, TheKnownUniverse, Zoom, asset_paths

Key `asset_paths` examples:
- `/Game/Campaign/TOIs/ClusterToiLogic`
- `/Game/UI/Components/StarSystemBannerWidget`
- `/Game/UI/Components/StarSystemTagWidget`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/Safezone_MTI1`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/SafezoneLine_MTI`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/Warzone_MTI`
- `/Game/UI/Mech/Materials/VerticalMask_MTL`
- `BlueprintGeneratedClass`

Key `StarMapActor` examples:
- `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarMapActor`
- `CallFunc_GetStarmapActor_Output`
- `Default__StarMapActor_C`
- `GetStarmapActor`
- `StarMapActor_C`

Key `StarSystemBody` examples:
- `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarSystemBody`
- `Default__MWStarSystemBody`
- `Default__StarSystemBody_C`
- `ExecuteUbergraph_StarSystemBody`
- `MWStarSystemBody`
- `StarSystemBody_C`

Key `Faction` examples:
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/Safezone_MTI1`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/SafezoneLine_MTI`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/Warzone_MTI`

Key `Camera` examples:
- `Camera`

Key `Zoom` examples:
- `HandleZoomChange`
- `InZoomLevel`
- `K2Node_Event_InZoomLevel`
- `K2Node_Event_NewZoomLevel`
- `NewZoomLevel`
- `OnZoomChange`
- `OnZoomLevelChangedHelper`
- `ReceiveOnZoomLevelChanged`
- `ZoomLevel`

### `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

- files: /Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor.uasset, /Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor.uexp
- string_count: 80
- notable tokens: BaseStarMapBorderActor, BorderChanges, Map, StarMap, StarMapBorderActor, TheKnownUniverse, asset_paths

Key `asset_paths` examples:
- `BlueprintGeneratedClass`

Key `BaseStarMapBorderActor` examples:
- `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor_C`
- `Default__BaseStarMapBorderActor_C`

### `/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`

- files: /Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges.uasset, /Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges.uexp
- string_count: 75
- notable tokens: BorderChanges, Map, StarMap, TheKnownUniverse

### `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015`

- files: /Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015.uasset, /Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015.uexp
- string_count: 13
- notable tokens: BorderChanges, Map, StarMap, StarMapBorderActor, TheKnownUniverse

### `/Game/InnerSphereData/MW5_InnerSphereData`

- files: /Game/InnerSphereData/MW5_InnerSphereData.uasset, /Game/InnerSphereData/MW5_InnerSphereData.uexp
- string_count: 7461
- notable tokens: BorderChanges, Clan, Faction, FactionBorder, InnerSphere, Lyran, Map, Steiner, TheKnownUniverse, asset_paths

Key `asset_paths` examples:
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_1.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_10.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_11.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_12.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_13.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_14.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_15.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_16.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_17.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_18.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_2.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_3.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_4.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_5.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_6.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_7`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_7.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_7_5.Safezone_7`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_8.Safezone`

Key `Lyran` examples:
- `LyranStrongholds`
- `RebeliousLyranTerritory`

Key `Steiner` examples:
- `SteinerBorder`
- `SteinerMarikBorder`

Key `Clan` examples:
- `/Game/CustomContent/Zones_Clan_Safezone`
- `/Game/CustomContent/Zones_Clan_Safezone_1.Zones_Clan_Safezone`
- `/Game/CustomContent/Zones_Clan_Safezone_2.Zones_Clan_Safezone`
- `/Game/CustomContent/Zones_ClanConf`
- `/Game/CustomContent/Zones_ClanConf_1.Zones_ClanConf`
- `/Game/CustomContent/Zones_ClanConf_2.Zones_ClanConf`
- `/Game/CustomContent/Zones_ClanConf_3.Zones_ClanConf`
- `/Game/CustomContent/Zones_ClanConf_4.Zones_ClanConf`
- `Albion (Clan)`
- `Arcadia (Clan)`
- `Atreus (Clan)`
- `ClanConflict`
- `Dagda (Clan)`
- `Declan`
- `Niles (Clan)`
- `RepairSystem_Clan`
- `Sheridan (Clan)`
- `Tiber (Clan)`
- `York (Clan)`

Key `Faction` examples:
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_1.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_10.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_11.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_12.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_13.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_14.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_15.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_16.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_17.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_18.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_2.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_3.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_4.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_5.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_6.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_7`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_7.Safezone`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_7_5.Safezone_7`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/SafezoneTempFolder/Safezone_8.Safezone`

### `/Game/InnerSphereData/Updated/EmployerInfoData`

- files: /Game/InnerSphereData/Updated/EmployerInfoData.uasset, /Game/InnerSphereData/Updated/EmployerInfoData.uexp
- string_count: 184
- notable tokens: Clan, Employer, InnerSphere, Lyran, TheKnownUniverse

Key `Lyran` examples:
- `LyranAlliance`
- `LyranCommonwealth`

Key `Clan` examples:
- `Clan`
- `ClanBloodSpirit`
- `ClanBurrock`
- `ClanCloudCobra`
- `ClanCoyote`
- `ClanDiamondShark`
- `ClanFireMandrill`
- `ClanGhostBear`
- `ClanGoliathScorpion`
- `ClanHellsHorses`
- `ClanIceHellion`
- `ClanJadeFalcon`
- `ClanMongoose`
- `ClanNovaCat`
- `ClanSeaFox`
- `ClanSmokeJaguar`
- `ClanSnowRaven`
- `ClanStarAdder`
- `ClanSteelViper`
- `ClanStoneLion`

### `/Game/InnerSphereData/Updated/SystemFactionChanges`

- files: /Game/InnerSphereData/Updated/SystemFactionChanges.uasset, /Game/InnerSphereData/Updated/SystemFactionChanges.uexp
- string_count: 4574
- notable tokens: Clan, Faction, InnerSphere, SystemFaction, TheKnownUniverse

Key `Clan` examples:
- `Albion (Clan)`
- `Albion(Clan)`
- `Arcadia (Clan)`
- `Arcadia(Clan)`
- `Atreus (Clan)`
- `Atreus(Clan)`
- `Dagda (Clan)`
- `Dagda(Clan)`
- `Declan`
- `Niles (Clan)`
- `Niles(Clan)`
- `Sheridan (Clan)`
- `Sheridan(Clan)`
- `Tiber (Clan)`
- `Tiber(Clan)`
- `York (Clan)`
- `York(Clan)`

Key `Faction` examples:
- `/ModOverride/TheKnownUniverse/InnerSphereData/Updated/SystemFactionChanges`
- `Faction`
- `FactionChange`
- `FactionDate`
- `SystemFactionChanges`

### `/Game/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

- files: /Game/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL.uasset, /Game/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL.uexp
- string_count: 610
- notable tokens: Camera, Faction, FactionColours, Map, StarMap, TheKnownUniverse, asset_paths

Key `asset_paths` examples:
- `/Game/Objects/_common/Effects/Materials/Noise/Noise_Clouds_01_MSK`
- `/Game/Objects/Environments/_common/Materials/Terrain/Noise_Masks/CloudsSoft_MSK`
- `/Game/Objects/Environments/Buildings/Urban/ModularCity/Material/MasterMaterials/DetailTextures/2kMasks/Fratical_sum2k_MSK`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/Textures/Clouds_Starmap_MSK`

Key `Faction` examples:
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/Textures/Clouds_Starmap_MSK`
- `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`
- `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF`
- `/TheKnownUniverse/FactionColorMangle_MTF`
- `/TheKnownUniverse/FactionMPC`
- `Faction_MTL`
- `FactionColorMangle_MTF`
- `FactionColours_MTF`
- `FactionMPC`

Key `Camera` examples:
- `/Engine/Functions/Engine_MaterialFunctions02/Utility/CameraDirectionVector`
- `CameraDirectionVector`

### `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL`

- files: /Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL.uasset, /Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL.uexp
- string_count: 229
- notable tokens: Faction, FactionBorder, FactionColours, Map, StarMap, TheKnownUniverse, asset_paths

Key `asset_paths` examples:
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/Textures/Stripe_CLR`

Key `Faction` examples:
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/Textures/Stripe_CLR`
- `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL`
- `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF`
- `/TheKnownUniverse/FactionColorMangle_MTF`
- `/TheKnownUniverse/FactionMPC`
- `FactionBorder_MTL`
- `FactionColorMangle_MTF`
- `FactionColours_MTF`
- `FactionMPC`

### `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF`

- files: /Game/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF.uasset, /Game/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF.uexp
- string_count: 13
- notable tokens: Faction, FactionColours, Map, StarMap, TheKnownUniverse

Key `Faction` examples:
- `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF`
- `FactionColours_MTF`

## Token Counts

- `BaseStarMapBorderActor`: 1
- `BorderChanges`: 4
- `Bounds`: 2
- `Camera`: 4
- `Clan`: 3
- `Employer`: 1
- `Faction`: 7
- `FactionBorder`: 3
- `FactionColours`: 3
- `InnerSphere`: 4
- `Lyran`: 2
- `Map`: 11
- `StarMap`: 10
- `StarMapActor`: 3
- `StarMapBorderActor`: 3
- `StarMapPawn`: 1
- `StarSystemBody`: 3
- `Steiner`: 1
- `SystemFaction`: 1
- `TheKnownUniverse`: 13
- `Zoom`: 2
- `asset_paths`: 8
