# TKU Content Mirror - 20260525-193027

Purpose: stage a late-loading `Content\Paks` mirror of the current editor-authored TKU compat package so root `/Game` assets can win over the legacy loose TKU starmap pak during a controlled runtime test.

- Apply requested: `False`
- Source pak: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch\Paks\TKUCompatEditorPatch.pak`
- Mirror scope: `all-game`
- Source pak candidates: `4`
- Staged mirror pak: `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\staging\MW5Mercs-zzzzTKUCompatEditorPatch-20260525-193027.pak`
- Live mirror pak: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak`
- Disabled live mirror sibling: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak.disabled-by-tku-isolation`
- Mirror pak SHA256: `50A7E76335BC12877EBADB8C1ECD1BA420E464E34C4598C85B31C1D034B3D1C2`
- Files mirrored: `72`

## Safety

- No safety failures.

## Conflicting Content Paks

- `MW5Mercs-WindowsNoEditor.pak` target entries `52` mount `../../../` sha `None`
- `MW5Mercs-zzzzTKUCompatEditorPatch.pak` target entries `8` mount `../../../MW5Mercs/Content/` sha `4414AC6DA60FD9D04E5BCB9098E0D716A689912AF4C484288AD54680537860DC`

## Actions

- staged UnrealPak-built content-root mirror pak at D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\staging\MW5Mercs-zzzzTKUCompatEditorPatch-20260525-193027.pak

## Rollback

- Remove only the staged live mirror pak `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak` to return to the previous content-pak set.

## Mirrored Path Sample

- `/Game/Campaign/Clusters/TKU_ClanConflict/ClanConflict.uasset`
- `/Game/Campaign/Clusters/TKU_ClanConflict/ClanConflict.uexp`
- `/Game/Campaign/Clusters/TKU_ClanConflict/TKU_ClanConflict_NoOverlay_ClusterAsset.uasset`
- `/Game/Campaign/Clusters/TKU_ClanConflict/TKU_ClanConflict_NoOverlay_ClusterAsset.uexp`
- `/Game/Campaign/Clusters/TKU_ClanConflict_Zones_ClanConf_1/TKU_ClanConflict_Zones_ClanConf_1_ClusterAsset.uasset`
- `/Game/Campaign/Clusters/TKU_ClanConflict_Zones_ClanConf_1/TKU_ClanConflict_Zones_ClanConf_1_ClusterAsset.uexp`
- `/Game/Campaign/Clusters/TKU_ClanConflict_Zones_ClanConf_2/TKU_ClanConflict_Zones_ClanConf_2_ClusterAsset.uasset`
- `/Game/Campaign/Clusters/TKU_ClanConflict_Zones_ClanConf_2/TKU_ClanConflict_Zones_ClanConf_2_ClusterAsset.uexp`
- `/Game/Campaign/Clusters/TKU_ClanConflict_Zones_ClanConf_3/TKU_ClanConflict_Zones_ClanConf_3_ClusterAsset.uasset`
- `/Game/Campaign/Clusters/TKU_ClanConflict_Zones_ClanConf_3/TKU_ClanConflict_Zones_ClanConf_3_ClusterAsset.uexp`
- `/Game/Campaign/Clusters/TKU_ClanConflict_Zones_ClanConf_4/TKU_ClanConflict_Zones_ClanConf_4_ClusterAsset.uasset`
- `/Game/Campaign/Clusters/TKU_ClanConflict_Zones_ClanConf_4/TKU_ClanConflict_Zones_ClanConf_4_ClusterAsset.uexp`
- `/Game/Campaign/Clusters/TKU_RepairSystem_Clan/RepairSystem_Clan.uasset`
- `/Game/Campaign/Clusters/TKU_RepairSystem_Clan/RepairSystem_Clan.uexp`
- `/Game/Campaign/Clusters/TKU_RepairSystem_Clan/TKU_RepairSystem_Clan_NoOverlay_ClusterAsset.uasset`
- `/Game/Campaign/Clusters/TKU_RepairSystem_Clan/TKU_RepairSystem_Clan_NoOverlay_ClusterAsset.uexp`
- `/Game/Campaign/Clusters/TKU_RepairSystem_Clan_Zones_Clan_Safezone_1/TKU_RepairSystem_Clan_Zones_Clan_Safezone_1_ClusterAsset.uasset`
- `/Game/Campaign/Clusters/TKU_RepairSystem_Clan_Zones_Clan_Safezone_1/TKU_RepairSystem_Clan_Zones_Clan_Safezone_1_ClusterAsset.uexp`
- `/Game/Campaign/Clusters/TKU_RepairSystem_Clan_Zones_Clan_Safezone_2/TKU_RepairSystem_Clan_Zones_Clan_Safezone_2_ClusterAsset.uasset`
- `/Game/Campaign/Clusters/TKU_RepairSystem_Clan_Zones_Clan_Safezone_2/TKU_RepairSystem_Clan_Zones_Clan_Safezone_2_ClusterAsset.uexp`
- `/Game/Campaign/_common/DefaultSystemGenerator.uasset`
- `/Game/Campaign/_common/DefaultSystemGenerator.uexp`
- `/Game/DLC1/CareerMode/CareerModeCoreCampaign.uasset`
- `/Game/DLC1/CareerMode/CareerModeCoreCampaign.uexp`
- `/Game/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset.uasset`
- `/Game/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset.uexp`
- `/Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters.uasset`
- `/Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters.uexp`
- `/Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones.uasset`
- `/Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones.uexp`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode.uasset`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode.uexp`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Davion_Start.uasset`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Davion_Start.uexp`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Davion_Start_Tutorial.uasset`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Davion_Start_Tutorial.uexp`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_FRR_Start.uasset`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_FRR_Start.uexp`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_FRR_Start_Tutorial.uasset`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_FRR_Start_Tutorial.uexp`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Kurita_Start.uasset`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Kurita_Start.uexp`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Kurita_Start_Tutorial.uasset`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Kurita_Start_Tutorial.uexp`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Liao_Start.uasset`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Liao_Start.uexp`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Liao_Start_Tutorial.uasset`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Liao_Start_Tutorial.uexp`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Marik_Start.uasset`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Marik_Start.uexp`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Marik_Start_Tutorial.uasset`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Marik_Start_Tutorial.uexp`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Start.uasset`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Start.uexp`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Steiner_Start.uasset`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Steiner_Start.uexp`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Steiner_Start_Tutorial.uasset`
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Steiner_Start_Tutorial.uexp`
- `/Game/DLC1/CareerMode/StartConditions/FRR_CareerMode_Start.uasset`
- `/Game/DLC1/CareerMode/StartConditions/FRR_CareerMode_Start.uexp`
- `/Game/InnerSphereData/MW5_InnerSphereData.uasset`
- `/Game/InnerSphereData/MW5_InnerSphereData.uexp`
- `/Game/InnerSphereData/StarSystemGenerator.uasset`
- `/Game/InnerSphereData/StarSystemGenerator.uexp`
- `/Game/Levels/FrontEnd/StarMap.uexp`
- `/Game/Levels/FrontEnd/StarMap.umap`
- `/Game/Modes/CampaignMode.uasset`
- `/Game/Modes/CampaignMode.uexp`
- `/Game/Modes/MW5GameMode.uasset`
- `/Game/Modes/MW5GameMode.uexp`
- `/Game/UI/FrontEnd/StarMapPawn.uasset`
- `/Game/UI/FrontEnd/StarMapPawn.uexp`