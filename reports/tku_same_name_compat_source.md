# TKU Same-Name Compat Source

- Strategy: preserve a full backup of the original `TheKnownUniverse` folder, then repack the live `TheKnownUniverse` mod under the same mod id with the stable TKU root substitutions, all original plugin content, and the legacy `CustomContent` starmap assets merged into the mod package.
- Live mod root: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TheKnownUniverse`
- Backup mod root: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TheKnownUniverse.original-20260506`

## Merge Notes

- Merged legacy custom-content entries: `0`
- Legacy custom-content source pak: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zKnownUniverseStarmap.original-20260506.pak`

## Excluded Bases

- `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015`
- `/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `/Game/InnerSphereData/MW5_InnerSphereData`
- `/Game/InnerSphereData/Updated/EmployerInfoData`
- `/Game/InnerSphereData/Updated/SystemFactionChanges`
- `/Game/Libraries/MW5_TOI_Functions`
- `/Game/UI/FrontEnd/StarMapPawn`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`
- `/Game/UI/FrontEnd/Starmap/StarMapActor`
- `/Game/UI/FrontEnd/Starmap/StarSystemBody`
