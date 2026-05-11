# TKU Evidence Starmap Compat Build - 2026-05-10

## Purpose

Create a narrow, reversible evidence build to test the current fatal-crash hypothesis without editing original TKU files.

## Evidence Gate

- Runtime isolation pinned the repeated `0x4C` fatal crash to `TheKnownUniverse.pak`.
- The loose `MW5Mercs-zKnownUniverseStarmap.pak` loaded a Davion career successfully with no enabled mods.
- Structured package-table parsing shows the loose starmap binds to current `/Game` starmap classes.
- Structured package-table parsing shows TKU's mod-pak starmap binds to `/ModOverride/TheKnownUniverse` starmap classes.
- Structured package-table parsing shows current vanilla `StarSystemBody` imports `MWClusterDataAsset` and exports current cluster-mesh hooks that original TKU lacks.

## Build Contents

- Output mod: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUEvidenceStarmapCompat`
- Output pak: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUEvidenceStarmapCompat\Paks\TKUEvidenceStarmapCompat.pak`
- Pak size: `10006832`
- File count: `44`

## Source Groups

- Safe loose override source: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zKnownUniverseStarmap.pak`
- Current vanilla class source: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-WindowsNoEditor.pak`

## Included From Loose Override

- `/Game/CustomContent/ClanConflict_1.uasset`
- `/Game/CustomContent/ClanConflict_1.uexp`
- `/Game/CustomContent/ClanConflict_2.uasset`
- `/Game/CustomContent/ClanConflict_2.uexp`
- `/Game/CustomContent/ClanConflict_3.uasset`
- `/Game/CustomContent/ClanConflict_3.uexp`
- `/Game/CustomContent/ClanConflict_4.uasset`
- `/Game/CustomContent/ClanConflict_4.uexp`
- `/Game/CustomContent/PirateKingdoms.uasset`
- `/Game/CustomContent/PirateKingdoms.uexp`
- `/Game/CustomContent/RepairSystem_Clan_1.uasset`
- `/Game/CustomContent/RepairSystem_Clan_1.uexp`
- `/Game/CustomContent/RepairSystem_Clan_2.uasset`
- `/Game/CustomContent/RepairSystem_Clan_2.uexp`
- `/Game/CustomContent/RepairSystem_Custom_1.uasset`
- `/Game/CustomContent/RepairSystem_Custom_1.uexp`
- `/Game/CustomContent/RepairSystem_Custom_2.uasset`
- `/Game/CustomContent/RepairSystem_Custom_2.uexp`
- `/Game/CustomContent/Zones_Clan_Safezone_1.uasset`
- `/Game/CustomContent/Zones_Clan_Safezone_1.uexp`
- `/Game/CustomContent/Zones_Clan_Safezone_2.uasset`
- `/Game/CustomContent/Zones_Clan_Safezone_2.uexp`
- `/Game/CustomContent/Zones_ClanConf_1.uasset`
- `/Game/CustomContent/Zones_ClanConf_1.uexp`
- `/Game/CustomContent/Zones_ClanConf_2.uasset`
- `/Game/CustomContent/Zones_ClanConf_2.uexp`
- `/Game/CustomContent/Zones_ClanConf_3.uasset`
- `/Game/CustomContent/Zones_ClanConf_3.uexp`
- `/Game/CustomContent/Zones_ClanConf_4.uasset`
- `/Game/CustomContent/Zones_ClanConf_4.uexp`
- `/Game/CustomContent/Zones_Custom_Conflict_1.uasset`
- `/Game/CustomContent/Zones_Custom_Conflict_1.uexp`
- `/Game/CustomContent/Zones_Custom_Safezone_1.uasset`
- `/Game/CustomContent/Zones_Custom_Safezone_1.uexp`
- `/Game/CustomContent/Zones_Custom_Safezone_2.uasset`
- `/Game/CustomContent/Zones_Custom_Safezone_2.uexp`
- `/Game/InnerSphereData/MW5_InnerSphereData.uasset`
- `/Game/InnerSphereData/MW5_InnerSphereData.uexp`
- `/Game/Levels/FrontEnd/StarMap.uexp`
- `/Game/Levels/FrontEnd/StarMap.umap`

## Included From Current Vanilla

- `/Game/UI/FrontEnd/Starmap/StarMapActor.uasset`
- `/Game/UI/FrontEnd/Starmap/StarMapActor.uexp`
- `/Game/UI/FrontEnd/Starmap/StarSystemBody.uasset`
- `/Game/UI/FrontEnd/Starmap/StarSystemBody.uexp`

## Expected Result

- If the old TKU starmap class stack is the fatal cause, TKU plus this compat mod should reach career gameplay after Davion start.
- If it still crashes with the same `0x4C` hash, the next suspect moves from starmap class assets to root data/campaign-start assets.
- This build is not expected to fully restore all non-major territory overlays; cluster-data migration remains a separate task.

## Runtime Result

- Test profile: only `TheKnownUniverse` and `TKUEvidenceStarmapCompat` enabled.
- Launch path: Steam app `784080`, command line `"MechWarrior-Win64-Shipping.exe" MW5Mercs`.
- User path: Single Player -> New Career -> Davion.
- Result: loading screen hard-stalled instead of producing the previous post-loading `0x4C` fatal crash.
- Later retry result: user reported a crash/termination from the same evidence profile, but no newer crash folder was created after `10/05/2026 7:51:50 PM`; the latest available UE crash artifact remained the separate `BaseStarMapBorderActor_C` failure from `TKUEvidenceStartBorderCompat`.
- Process evidence: `MechWarrior-Win64-Shipping` remained Windows-responsive, but CPU did not advance over a 10-second sample; working set was about `1.8 GB`, private memory about `3.1 GB`.
- Crash evidence: no new crash folder was created; latest crash folder remained the earlier `10/05/2026 11:13:17 AM` `0x4C` run.
- Log evidence: no current UE gameplay log was found; only the existing Steam/Razer stderr stub was present.

## Interpretation

- This is not a successful patch.
- This patch is now disabled in the live profile; rollback snapshot is `MW5Mercs\Mods\modlist.profile-tku-only-after-starmap-evidence-crash-20260510.json`.
- The failure-mode change from fatal crash to hard stall is evidence that `StarMapActor` / `StarSystemBody` were on the old fatal path.
- The stall means the active asset set is still internally inconsistent: current `StarMapActor` / `StarSystemBody` are now mixed with still-active TKU root assets such as `StarMapPawn`, dated border assets, faction materials, root faction/employer assets, `SystemFactionChanges`, `EmployerInfoData`, and `MW5_TOI_Functions`.
- The next gated action is to trace those remaining root assets and inspect/recreate current-schema data in the editor, not to add more broad vanilla class overrides.

## Rollback

- `TKUEvidenceStarmapCompat` is disabled in the current `modlist.json`; leave the folder in place as preserved evidence unless deliberately archiving test artifacts.
- Original `TheKnownUniverse.pak` and `MW5Mercs-zKnownUniverseStarmap.pak` were not edited.
