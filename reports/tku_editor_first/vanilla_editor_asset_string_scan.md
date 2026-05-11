# Vanilla Editor Asset String Reference Scan

This scans loose assets from the MW5 Mod Editor install. It is useful for package/reference comparison against cooked TKU assets.

- Editor root: `E:\Games\MechWarrior5Editor`

### `/Game/Levels/FrontEnd/StarMap`

- existing_files: E:\Games\MechWarrior5Editor\MW5Mercs\Content\Levels\FrontEnd\StarMap.umap
- missing_files: none
- string_count: 3206
- notable tokens: /Game/, Bounds, Camera, Faction, StarMap, StarMapActor, StarSystemBody, Zoom

Key `/Game/` examples:
- `/Game/Levels/FrontEnd/StarMap`
- `/Game/Levels/FrontEnd/StarMap.StarMap`
- `/Game/Levels/FrontEnd/StarMapSceneManager`
- `/Game/Levels/FrontEnd/StarSystemSceneManager`
- `/Game/Levels/Lighting/_common/Textures/Starfields/hdr_starfield_01_TEX`
- `/Game/Levels/TestMaps/Test_Basic`
- `/Game/Modes/SceneManagers/SceneManager`
- `/Game/UI/FrontEnd/Starmap/AbstractStarSystem`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTI`
- `/Game/UI/FrontEnd/Starmap/Materials/Nebula_MST`
- `/Game/UI/FrontEnd/Starmap/Materials/StarMap_Nebula_MST`
- `/Game/UI/FrontEnd/Starmap/Nebulae/Nebula`
- `/Game/UI/FrontEnd/Starmap/Nebulae/StarMap_Nebula`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_AClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_BClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_FClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_GClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_KClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_MClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/StarMapActor`

Key `StarMapActor` examples:
- `/Game/UI/FrontEnd/Starmap/StarMapActor`
- `Default__StarMapActor_C`
- `StarMapActor`
- `StarMapActor_C`

Key `StarSystemBody` examples:
- `/Game/UI/FrontEnd/Starmap/StarSystemBody`
- `Default__StarSystemBody_C`
- `StarSystemBody`
- `StarSystemBody1`
- `StarSystemBody10`
- `StarSystemBody100`
- `StarSystemBody1000`
- `StarSystemBody1001`
- `StarSystemBody1002`
- `StarSystemBody1003`
- `StarSystemBody1004`
- `StarSystemBody1005`
- `StarSystemBody1006`
- `StarSystemBody1007`
- `StarSystemBody1008`
- `StarSystemBody1009`
- `StarSystemBody101`
- `StarSystemBody1010`
- `StarSystemBody1011`
- `StarSystemBody1012`

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

Key `Zoom` examples:
- `CamOrthoZoom`
- `SavedZoomAmount`

### `/Game/UI/FrontEnd/Starmap/StarMapActor`

- existing_files: E:\Games\MechWarrior5Editor\MW5Mercs\Content\UI\FrontEnd\Starmap\StarMapActor.uasset
- missing_files: none
- string_count: 3674
- notable tokens: /Game/, Camera, Faction, InnerSphere, StarMap, StarMapActor, StarMapBorderActor, StarSystemBody, Zoom

Key `/Game/` examples:
- `/Game/InnerSphereData/StarMapBP_UTILS`
- `/Game/Libraries/MW5_PersistentModel_ActorLibrary`
- `/Game/UI/FrontEnd/Starmap/AbstractStarSystem`
- `/Game/UI/FrontEnd/Starmap/Cluster_MTI`
- `/Game/UI/FrontEnd/Starmap/CurrentCourse_MTI`
- `/Game/UI/FrontEnd/Starmap/cylinder_STM`
- `/Game/UI/FrontEnd/Starmap/Materials/FogOfWar_MTL`
- `/Game/UI/FrontEnd/Starmap/Materials/FogOfWarRenderTarget`
- `/Game/UI/FrontEnd/Starmap/Materials/FogOfWarSplat_MTL`
- `/Game/UI/FrontEnd/Starmap/MaxTravelDistance_MTI`
- `/Game/UI/FrontEnd/Starmap/Nebulae/StarMap_Nebula`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_AClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_BClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_FClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_GClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_KClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/Star/Materials/StarMap_MClass_Star_MTI`
- `/Game/UI/FrontEnd/Starmap/StarMapActor`
- `/Game/UI/FrontEnd/Starmap/StarMapActor.StarMapActor`
- `/Game/UI/FrontEnd/Starmap/StarMapRoute_MTI`

Key `StarMapActor` examples:
- `/Game/UI/FrontEnd/Starmap/StarMapActor`
- `/Game/UI/FrontEnd/Starmap/StarMapActor.StarMapActor`
- `BlueprintGeneratedClass'/Game/UI/FrontEnd/Starmap/StarMapActor.StarMapActor_C'`
- `Default__StarMapActor_C`
- `ExecuteUbergraph_StarMapActor`
- `StarMapActor`
- `StarMapActor_C`

Key `StarSystemBody` examples:
- `/Game/UI/FrontEnd/Starmap/StarSystemBody`
- `FindStarSystemBodyById`
- `MWStarSystemBody`
- `StarSystemBody_C`
- `StarSystemBodyLookUp`

Key `Camera` examples:
- `Camera`
- `CameraActor`
- `Initial Camera Transform`
- `InitialCameraTransform`
- `Star Map Camera`
- `StarMapCamera`

Key `Zoom` examples:
- `SavedZoomAmount`

### `/Game/UI/FrontEnd/StarMapPawn`

- existing_files: E:\Games\MechWarrior5Editor\MW5Mercs\Content\UI\FrontEnd\StarMapPawn.uasset
- missing_files: none
- string_count: 245
- notable tokens: /Game/, StarMap, StarMapPawn, Zoom

Key `/Game/` examples:
- `/Game/UI/Components/StarSystemTOITooltip`
- `/Game/UI/FrontEnd/StarMap_MPC`
- `/Game/UI/FrontEnd/StarmapGamepadWidget`
- `/Game/UI/FrontEnd/StarMapPawn`
- `/Game/UI/FrontEnd/StarMapPawn.StarMapPawn`
- `/Game/UI/FrontEnd/StarMapPawn.StarMapPawn_C:SimpleConstructionScript_0.SCS_Node_0.CategoryName`
- `BlueprintGeneratedClass'/Game/UI/FrontEnd/StarMapPawn.StarMapPawn_C'`

Key `StarMapPawn` examples:
- `/Game/UI/FrontEnd/StarMapPawn`
- `/Game/UI/FrontEnd/StarMapPawn.StarMapPawn`
- `/Game/UI/FrontEnd/StarMapPawn.StarMapPawn_C:SimpleConstructionScript_0.SCS_Node_0.CategoryName`
- `BlueprintGeneratedClass'/Game/UI/FrontEnd/StarMapPawn.StarMapPawn_C'`
- `Class'/Script/MechWarrior.MWStarMapPawn'`
- `Default__MWStarMapPawn`
- `Default__StarMapPawn_C`
- `MWStarMapPawn`
- `StarMapPawn`
- `StarMapPawn-1`
- `StarMapPawn_C`

Key `Zoom` examples:
- `SavedZoomAmount`
- `ZoomDistanceList`
- `ZoomLevelThresholds`

### `/Game/UI/FrontEnd/Starmap/StarSystemBody`

- existing_files: E:\Games\MechWarrior5Editor\MW5Mercs\Content\UI\FrontEnd\Starmap\StarSystemBody.uasset
- missing_files: none
- string_count: 3191
- notable tokens: /Game/, Camera, Faction, MWClusterDataAsset, StarMap, StarMapActor, StarSystemBody, Zoom

Key `/Game/` examples:
- `/Game/Campaign/TOIs/ClusterToiLogic`
- `/Game/Libraries/MW5_PersistentModel_ActorLibrary`
- `/Game/UI/Components/StarSystemBannerWidget`
- `/Game/UI/Components/StarSystemTagWidget`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/Safezone_MTI1`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/SafezoneLine_MTI`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/Warzone_MTI`
- `/Game/UI/FrontEnd/Starmap/StarMapActor`
- `/Game/UI/FrontEnd/Starmap/StarSystemBody`
- `/Game/UI/FrontEnd/Starmap/StarSystemBody.StarSystemBody`
- `/Game/UI/Mech/Materials/VerticalMask_MTL`
- `BlueprintGeneratedClass'/Game/UI/FrontEnd/Starmap/StarSystemBody.StarSystemBody_C'`

Key `StarMapActor` examples:
- `/Game/UI/FrontEnd/Starmap/StarMapActor`
- `CallFunc_GetStarmapActor_Output`
- `GetStarmapActor`
- `StarMapActor_C`

Key `StarSystemBody` examples:
- `/Game/UI/FrontEnd/Starmap/StarSystemBody`
- `/Game/UI/FrontEnd/Starmap/StarSystemBody.StarSystemBody`
- `BlueprintGeneratedClass'/Game/UI/FrontEnd/Starmap/StarSystemBody.StarSystemBody_C'`
- `Class'/Script/MechWarrior.MWStarSystemBody'`
- `Default__MWStarSystemBody`
- `Default__StarSystemBody_C`
- `ExecuteUbergraph_StarSystemBody`
- `MWStarSystemBody`
- `Public/UI/Starmap/MWStarSystemBody.h`
- `StarSystemBody`
- `StarSystemBody-1`
- `StarSystemBody_C`

Key `Camera` examples:
- `Camera`

Key `Zoom` examples:
- `// invoked when the widget becomes visible/invisible along with the zoom level at that moment`
- `// invoked when the zoom level transitions from one state to another while the widget is visible`
- `HandleZoomChange`
- `In Zoom Level`
- `invoked when the widget becomes visible/invisible along with the zoom level at that moment`
- `invoked when the zoom level transitions from one state to another while the widget is visible`
- `InZoomLevel`
- `K2Node_Event_InZoomLevel`
- `K2Node_Event_NewZoomLevel`
- `New Zoom Level`
- `NewZoomLevel`
- `OnZoomChange`
- `OnZoomLevelChanged`
- `OnZoomLevelChangedHelper`
- `ReceiveOnZoomLevelChanged`
- `SavedZoomAmount`
- `Zoom Level`
- `ZoomLevel`

Key `MWClusterDataAsset` examples:
- `MWClusterDataAsset`

### `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

- existing_files: E:\Games\MechWarrior5Editor\MW5Mercs\Content\Campaign\CampaignArcs\BorderChanges\_common\BaseStarMapBorderActor.uasset
- missing_files: none
- string_count: 404
- notable tokens: /Game/, BaseStarMapBorderActor, StarMap, StarMapBorderActor, Zoom

Key `/Game/` examples:
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor.BaseStarMapBorderActor`
- `BlueprintGeneratedClass'/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor.BaseStarMapBorderActor_C'`

Key `BaseStarMapBorderActor` examples:
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor.BaseStarMapBorderActor`
- `BaseStarMapBorderActor`
- `BaseStarMapBorderActor_C`
- `BlueprintGeneratedClass'/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor.BaseStarMapBorderActor_C'`
- `Default__BaseStarMapBorderActor_C`

Key `Zoom` examples:
- `SavedZoomAmount`

### `/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`

- existing_files: E:\Games\MechWarrior5Editor\MW5Mercs\Content\Campaign\CampaignArcs\BorderChanges\AllStarMapBorderChanges.uasset
- missing_files: none
- string_count: 37
- notable tokens: /Game/, Clan, StarMap

Key `/Game/` examples:
- `/Game/Campaign/CampaignArcs/BorderChanges/3025_ThirdSuccession/3025_ThirdSuccession`
- `/Game/Campaign/CampaignArcs/BorderChanges/3029_FormationOfTikinovAndStIves/3029_FormationOfTikinovAndStIves`
- `/Game/Campaign/CampaignArcs/BorderChanges/3030_FourthSuccession/3030_FourthSuccession`
- `/Game/Campaign/CampaignArcs/BorderChanges/3031_TikinovJoinsFederatedSuns/3031_TikinovJoinsFederatedSuns`
- `/Game/Campaign/CampaignArcs/BorderChanges/3034_RassalhaugeRecognized/Borders_Year3034_RassalhaugeRecognized`
- `/Game/Campaign/CampaignArcs/BorderChanges/3039_WarOf3039/3039_WarOf3039`
- `/Game/Campaign/CampaignArcs/BorderChanges/3041_FormationOfFederatedCommonwealth/3041_FormationOfFederatedCommonwealth`
- `/Game/Campaign/CampaignArcs/BorderChanges/3049_ClanInvasion/3049_ClanInvasion`
- `/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`

Key `Clan` examples:
- `/Game/Campaign/CampaignArcs/BorderChanges/3049_ClanInvasion/3049_ClanInvasion`
- `3049_ClanInvasion`

### `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015`

- existing_files: E:\Games\MechWarrior5Editor\MW5Mercs\Content\Campaign\CampaignArcs\BorderChanges\3015_GameStart\Borders3015.uasset
- missing_files: none
- string_count: 22
- notable tokens: /Game/, StarMap, StarMapBorderActor

Key `/Game/` examples:
- `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015`
- `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/StarMapBorderActor3015`
- `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/StarMapBorderActor3015.StarMapBorderActor3015_C`

### `/Game/InnerSphereData/MW5_InnerSphereData`

- existing_files: E:\Games\MechWarrior5Editor\MW5Mercs\Content\InnerSphereData\MW5_InnerSphereData.uasset, E:\Games\MechWarrior5Editor\MW5Mercs\Content\InnerSphereData\MW5_InnerSphereData.csv, E:\Games\MechWarrior5Editor\MW5Mercs\Content\Data\InnerSphereMap\MW5_InnerSphereData.json
- missing_files: none
- string_count: 19145
- notable tokens: /Game/, Clan, Faction, InnerSphere, Lyran, Steiner

Key `/Game/` examples:
- `/Game/Campaign/Clusters/A2M1/A2M1`
- `/Game/Campaign/Clusters/A2M1/A2M1.A2M1`
- `/Game/Campaign/Clusters/A2M2/A2M2`
- `/Game/Campaign/Clusters/A2M2/A2M2.A2M2`
- `/Game/Campaign/Clusters/A2M3/A2M3`
- `/Game/Campaign/Clusters/A2M3/A2M3.A2M3`
- `/Game/Campaign/Clusters/Alarion/15`
- `/Game/Campaign/Clusters/Alarion/15_2.15`
- `/Game/Campaign/Clusters/BackwaterRegion/8`
- `/Game/Campaign/Clusters/BackwaterRegion/8_4.8`
- `/Game/Campaign/Clusters/Davion-KuritaFrontline/5_1_Mesh`
- `/Game/Campaign/Clusters/Davion-KuritaFrontline/5_1_Mesh.5_1_Mesh`
- `/Game/Campaign/Clusters/DavionBorderlands/6_2_Mesh`
- `/Game/Campaign/Clusters/DavionBorderlands/6_2_Mesh.6_2_Mesh`
- `/Game/Campaign/Clusters/DraconisBadlands/13`
- `/Game/Campaign/Clusters/DraconisBadlands/13_1.13`
- `/Game/Campaign/Clusters/DroughtWorlds/13`
- `/Game/Campaign/Clusters/DroughtWorlds/13_2.13`
- `/Game/Campaign/Clusters/DuchyOfAndurien/8`
- `/Game/Campaign/Clusters/DuchyOfAndurien/8_3.8`

Key `Lyran` examples:
- `/Game/Campaign/Clusters/LyranMilitaryStrongholds/11`
- `/Game/Campaign/Clusters/LyranMilitaryStrongholds/11_3.11`
- `/Game/Campaign/Clusters/RebelliousLyranPrince/11`
- `/Game/Campaign/Clusters/RebelliousLyranPrince/11_2.11`
- `104,"104","New Olympia","-151.000000","-131.000000","Normal","G","V","1","Normal","None","Unspecified","H_1Plus","","(Id=""MWFactionAsset:RebeliousLyranTerritory"")","None","None"`
- `131,"131","Mariefred","-182.000000","26.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:RebeliousLyranTerritory"")","None","None"`
- `1414,"1414","Zwenkau","-236.000000","10.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:RebeliousLyranTerritory"")","None","None"`
- `1427,"1427","Eilenburg","-222.000000","20.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:RebeliousLyranTerritory"")","None","None"`
- `1436,"1436","Uzhgorod","-216.000000","57.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:RebeliousLyranTerritory"")","None","None"`
- `1490,"1490","Callisto","-158.000000","125.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:LyranStrongholds"")","None","None"`
- `1506,"1506","Crevedia","-130.000000","162.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:LyranStrongholds"")","None","None"`
- `1515,"1515","Canonbie","-123.000000","68.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:RebeliousLyranTerritory"")","None","None"`
- `1527,"1527","Ginestra","-112.000000","165.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:LyranStrongholds"")","None","None"`
- `1543,"1543","Edasich","-97.000000","122.000000","Normal","F","IV","6","Normal","None","Unspecified","H_1Plus","","(Id=""MWFactionAsset:LyranStrongholds"")","None","None"`
- `1564,"1564","Leganes","-78.000000","162.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:LyranStrongholds"")","None","None"`
- `172,"172","Arganda","-156.000000","36.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:RebeliousLyranTerritory"")","None","None"`
- `233,"233","Lucianca","-98.000000","165.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:LyranStrongholds"")","None","None"`
- `255,"255","Apostica","-60.000000","157.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:LyranStrongholds"")","None","None"`
- `263,"263","Cumbres","-155.000000","204.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:LyranStrongholds"")","None","None"`
- `280,"280","Breukelen","-89.000000","143.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:LyranStrongholds"")","/Game/Campaign/CampaignArcs/Regions/11_3/11_3.11_3","None"`

Key `Steiner` examples:
- `/Game/Campaign/Clusters/Steiner-KuritaBorder/12`
- `/Game/Campaign/Clusters/Steiner-KuritaBorder/12_1.12`
- `1472,"1472","Nestor","-172.000000","-26.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:SteinerMarikBorder"")","None","None"`
- `1474,"1474","Launam","-169.000000","-13.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:SteinerMarikBorder"")","/Game/Campaign/CampaignArcs/Regions/10_3/10_3.10_3","None"`
- `1562,"1562","Borghese","-80.000000","212.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:SteinerBorder"")","None","None"`
- `1579,"1579","Colmar","-67.000000","302.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:SteinerBorder"")","None","None"`
- `1584,"1584","Montmarault","-60.000000","265.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:SteinerBorder"")","None","None"`
- `1592,"1592","Orkney (LC)","-49.000000","237.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:SteinerBorder"")","None","None"`
- `1594,"1594","Laurent","-45.000000","305.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:SteinerBorder"")","None","None"`
- `1597,"1597","Rasalgethi","-42.000000","214.000000","Normal","M","Ia","9","Normal","Zenith","Unspecified","H_1Plus","","(Id=""MWFactionAsset:SteinerBorder"")","None","None"`
- `1608,"1608","Domain","-33.000000","250.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:SteinerBorder"")","None","None"`
- `1622,"1622","Bessarabia","-26.000000","279.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:SteinerBorder"")","None","None"`
- `1638,"1638","Carse","-16.000000","241.000000","Binary","G","V","1","Normal","None","Unspecified","H_1Plus","","(Id=""MWFactionAsset:SteinerBorder"")","None","None"`
- `1640,"1640","Kobe","-15.000000","284.000000","Normal","G","V","0","Normal","None","Unspecified","H_1Plus","","(Id=""MWFactionAsset:SteinerBorder"")","None","None"`
- `208,"208","La Grave","-52.000000","249.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:SteinerBorder"")","/Game/Campaign/CampaignArcs/Regions/12_1/12_1.12_1","None"`
- `262,"262","Hyde","-164.000000","3.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:SteinerMarikBorder"")","None","None"`
- `339,"339","Giausar","-210.000000","-27.000000","Normal","M","III","0","Normal","None","Unspecified","H_1Plus","","(Id=""MWFactionAsset:SteinerMarikBorder"")","None","None"`
- `436,"436","Uhuru","-140.000000","-13.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:SteinerMarikBorder"")","None","None"`
- `477,"477","Maestu","-36.000000","291.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:SteinerBorder"")","None","None"`
- `496,"496","Thermopolis","-217.000000","-59.000000","Normal","None","","0","Normal","None","Unspecified","Unspecified","","(Id=""MWFactionAsset:SteinerMarikBorder"")","None","None"`

Key `Clan` examples:
- `"Description": "NSLOCTEXT(\"\", \"9305E6504D382AEA88BFE88DAE7D7CAF\", \"The Tanite system is composed of multiple planets and was colonized by people calling themselves the Tanites that unknowingly existed within several jumps of the Clans for quite some time. When the system was discovered the Clans soon moved in and took over, though they never quite subdued the Tanites, who buckled under the restrictive Clan Class structure. Three of the four planets in the system are colonized.\")"`
- `"StarSystemName": "Albion (Clan)",`
- `"StarSystemName": "Arcadia (Clan)",`
- `"StarSystemName": "Atreus (Clan)",`
- `"StarSystemName": "Dagda (Clan)",`
- `"StarSystemName": "Declan",`
- `"StarSystemName": "Niles (Clan)",`
- `"StarSystemName": "Sheridan (Clan)",`
- `"StarSystemName": "Tiber (Clan)",`
- `"StarSystemName": "York (Clan)",`

### `/Game/InnerSphereData/Updated/EmployerInfoData`

- existing_files: E:\Games\MechWarrior5Editor\MW5Mercs\Content\InnerSphereData\Updated\EmployerInfoData.uasset
- missing_files: none
- string_count: 188
- notable tokens: /Game/, Clan, Employer, InnerSphere, Lyran

Key `/Game/` examples:
- `/Game/InnerSphereData/Updated/EmployerInfoData`

Key `Lyran` examples:
- `LyranAlliance`
- `LyranCommonwealth`

Key `Clan` examples:
- `CLAN`
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

### `/Game/InnerSphereData/Updated/SystemFactionChanges`

- existing_files: E:\Games\MechWarrior5Editor\MW5Mercs\Content\InnerSphereData\Updated\SystemFactionChanges.uasset
- missing_files: none
- string_count: 4349
- notable tokens: /Game/, Clan, Faction, InnerSphere, SystemFaction

Key `/Game/` examples:
- `/Game/InnerSphereData/Updated/SystemFactionChanges`

Key `Clan` examples:
- `Albion (Clan)`
- `Albion(Clan)`
- `Arcadia (Clan)`
- `Arcadia(Clan)`
- `Atreus (Clan)`
- `Atreus(Clan)`
- `CLAN`
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

### `/Game/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

- existing_files: E:\Games\MechWarrior5Editor\MW5Mercs\Content\UI\FrontEnd\Starmap\Materials\Factions\Faction_MTL.uasset
- missing_files: none
- string_count: 2085
- notable tokens: /Game/, Bounds, Camera, Faction, StarMap

Key `/Game/` examples:
- `/Game/Objects/_common/Effects/Materials/Noise/Noise_Clouds_01_MSK`
- `/Game/Objects/Environments/Buildings/Urban/ModularCity/Material/MasterMaterials/DetailTextures/2kMasks/Fratical_sum2k_MSK`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/Faction_Colours_MPC`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/Textures/Clouds_Starmap_MSK`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/Textures/Clouds_Starmap_MSK.Clouds_Starmap_MSK`

Key `Bounds` examples:
- `/Engine/Functions/Engine_MaterialFunctions02/ObjectLocalBounds`
- `Local Bounds Max`
- `Local Bounds Minimum`
- `Local Bounds Size`
- `ObjectLocalBounds`

Key `Camera` examples:
- `/Engine/Functions/Engine_MaterialFunctions02/Utility/CameraDirectionVector`
- `CameraDirectionVector`

### `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL`

- existing_files: E:\Games\MechWarrior5Editor\MW5Mercs\Content\UI\FrontEnd\Starmap\Materials\Factions\FactionBorder_MTL.uasset
- missing_files: none
- string_count: 815
- notable tokens: /Game/, Faction, StarMap

Key `/Game/` examples:
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/Faction_Colours_MPC`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/Textures/Stripe_CLR`

### `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF`

- existing_files: E:\Games\MechWarrior5Editor\MW5Mercs\Content\UI\FrontEnd\Starmap\Materials\Factions\FactionColours_MTF.uasset
- missing_files: none
- string_count: 1672
- notable tokens: /Game/, Clan, Faction, Lyran, StarMap

Key `/Game/` examples:
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/Faction_Colours_MPC`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF`

Key `Lyran` examples:
- `LyranCommonwealth`

Key `Clan` examples:
- `ClanGhostBear`
- `ClanInvasion`
- `ClanJadeFalcon`
- `ClanSmokeJaguar`
- `ClanWolf`

### `/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets`

- existing_files: E:\Games\MechWarrior5Editor\MW5Mercs\Content\UI\Editor\Utils\EUW_MigratePlaceClusterTOIsToClusterAssets.uasset
- missing_files: none
- string_count: 3160
- notable tokens: /Game/, EUW_MigratePlaceCluster, Faction, InnerSphere, MWClusterDataAsset, OverridePath, PlaceClusterTOI, Zoom

Key `/Game/` examples:
- `/Game/`
- `/Game/Campaign/_common/ClusterToiDataFragment`
- `/Game/Campaign/CampaignArcActions/MissionActions/MissionConfigs/PlaceClusterToi_Config`
- `/Game/Campaign/CampaignArcActions/MissionActions/MissionConfigs/PlaceClusterToi_Markups`
- `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- `/Game/DLC`
- `/Game/InnerSphereData/MW5_InnerSphereData`
- `/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets`
- `/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets.EUW_MigratePlaceClusterTOIsToClusterAssets`
- `/Game/UI/Font/Futura/Futura`
- `/Game/UI/FrontEnd/Codex/Codex_TextBox_Style`
- `Folder to filter assets for, includes sub folders. Defaults to /Game/`
- `New path to package without package name, ie /Game/SubDirectory`
- `The name of the package in which the asset is found, this is the full long package name such as /Game/Path/Package`
- `The path to the package in which the asset is found, this is /Game/Path with the Package stripped off`
- `WidgetBlueprintGeneratedClass'/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets.EUW_MigratePlaceClusterTOIsToClusterAssets_C'`

Key `Zoom` examples:
- `SavedZoomAmount`

Key `MWClusterDataAsset` examples:
- `Asset already exists, but is not a MWClusterDataAsset!`
- `Migrates PlaceClusterTOI_ArcAction and InnerSphereMap data into a MWClusterDataAsset File.`
- `MWClusterDataAsset`

Key `PlaceClusterTOI` examples:
- `/Game/Campaign/CampaignArcActions/MissionActions/MissionConfigs/PlaceClusterToi_Config`
- `/Game/Campaign/CampaignArcActions/MissionActions/MissionConfigs/PlaceClusterToi_Markups`
- `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- `/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets`
- `/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets.EUW_MigratePlaceClusterTOIsToClusterAssets`
- `BndEvt__EUW_MigratePlaceClusterTOIsToClusterAssets_btn_Stop_K2Node_ComponentBoundEvent_1_OnButtonClickedEvent__DelegateSignature`
- `BndEvt__EUW_MigratePlaceClusterTOIsToClusterAssets_Button_0_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature`
- `CallFunc_GatherPlaceClusterTOIArcActions_OutPlaceClusterTOISet`
- `Default__EUW_MigratePlaceClusterTOIsToClusterAssets_C`
- `EUW_MigratePlaceClusterTOIsToClusterAssets`
- `EUW_MigratePlaceClusterTOIsToClusterAssets_C`
- `ExecuteUbergraph_EUW_MigratePlaceClusterTOIsToClusterAssets`
- `GatherPlaceClusterTOIArcActions`
- `InPlaceClusterTOI`
- `Iterate over the campaign actions, check if the parent class is PlaceClusterTOI_ArcAction, get the default object and add to our set`
- `Migrates PlaceClusterTOI_ArcAction and InnerSphereMap data into a MWClusterDataAsset File.`
- `OutPlaceClusterTOISet`
- `PlaceClusterToi_ArcAction_C`
- `PlaceClusterToi_Config`
- `PlaceClusterToi_Markups`

Key `EUW_MigratePlaceCluster` examples:
- `/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets`
- `/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets.EUW_MigratePlaceClusterTOIsToClusterAssets`
- `BndEvt__EUW_MigratePlaceClusterTOIsToClusterAssets_btn_Stop_K2Node_ComponentBoundEvent_1_OnButtonClickedEvent__DelegateSignature`
- `BndEvt__EUW_MigratePlaceClusterTOIsToClusterAssets_Button_0_K2Node_ComponentBoundEvent_0_OnButtonClickedEvent__DelegateSignature`
- `Default__EUW_MigratePlaceClusterTOIsToClusterAssets_C`
- `EUW_MigratePlaceClusterTOIsToClusterAssets`
- `EUW_MigratePlaceClusterTOIsToClusterAssets_C`
- `ExecuteUbergraph_EUW_MigratePlaceClusterTOIsToClusterAssets`
- `WidgetBlueprintGeneratedClass'/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets.EUW_MigratePlaceClusterTOIsToClusterAssets_C'`

Key `OverridePath` examples:
- `txt_OverridePath`

## Token Counts

- `/Game/`: 14
- `BaseStarMapBorderActor`: 1
- `Bounds`: 2
- `Camera`: 4
- `Clan`: 5
- `EUW_MigratePlaceCluster`: 1
- `Employer`: 1
- `Faction`: 9
- `InnerSphere`: 5
- `Lyran`: 3
- `MWClusterDataAsset`: 2
- `OverridePath`: 1
- `PlaceClusterTOI`: 1
- `StarMap`: 10
- `StarMapActor`: 3
- `StarMapBorderActor`: 3
- `StarMapPawn`: 1
- `StarSystemBody`: 3
- `Steiner`: 1
- `SystemFaction`: 1
- `Zoom`: 6
