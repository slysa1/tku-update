# TKU Crash Surface Scan

This report scans strings across original TKU cooked assets to narrow the editor/tool inspection surface for the repeated Davion career-load `0x4C` crash. It is not proof of runtime execution by itself.

- Source pak: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TheKnownUniverse\Paks\TheKnownUniverse.pak`
- Assets with relevant token hits or high-risk classification: `1215`

## High-Signal Interpretation

- The crash reproduces with TKU alone, so assets in this pak are sufficient to trigger it.
- Any asset listed here still needs editor/tool inspection before a rebuild is justified.
- Root `/Game` substitutions are higher risk than plugin-only content because reduced plugin-only builds previously loaded farther.

## Token Coverage

- `/Game/Campaign/CampaignArcs/BorderChanges`: `1` assets
- `/Game/UI/FrontEnd/Starmap`: `6` assets
- `AllStarMapBorderChanges`: `1` assets
- `BaseStarMapBorderActor`: `30` assets
- `Borders3015`: `1` assets
- `CampaignArc`: `108` assets
- `CampaignArcs`: `33` assets
- `CareerMode`: `4` assets
- `Clan`: `97` assets
- `CustomContent`: `1` assets
- `Davion`: `2` assets
- `EmployerInfoData`: `1` assets
- `Haynesville`: `2` assets
- `Lyran`: `6` assets
- `MW5_InnerSphereData`: `1` assets
- `ModOverride`: `1053` assets
- `PersonaAnonymousEmployer`: `2` assets
- `PlaceClusterToi`: `9` assets
- `StarMapActor`: `3` assets
- `StarMapBorderActor`: `61` assets
- `StarMapBordersUpdate_Action`: `58` assets
- `StarMapPawn`: `1` assets
- `StarSystemBody`: `3` assets
- `Steiner`: `4` assets
- `SystemFactionChanges`: `1` assets

## Class Counts

- `plugin_timeline_border`: `999`
- `root_game_override`: `141`
- `plugin_support`: `58`
- `plugin_region_or_campaign`: `17`

## High-Risk Root Assets

### `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015`

- files: /Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015.uasset, /Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015.uexp
- strings: `13`
- tokens: `CampaignArc`, `CampaignArcs`, `Borders3015`, `StarMapBorderActor`, `ModOverride`
- `Borders3015` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015`; `Borders3015`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015`

### `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

- files: /Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor.uasset, /Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor.uexp
- strings: `80`
- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`

- files: /Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges.uasset, /Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges.uexp
- strings: `75`
- tokens: `CampaignArc`, `CampaignArcs`, `AllStarMapBorderChanges`, `ModOverride`
- `AllStarMapBorderChanges` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`; `AllStarMapBorderChanges`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`

### `/Game/Campaign/Personas/ProcMissionPersonas/PersonaAnonymousEmployer`

- files: /Game/Campaign/Personas/ProcMissionPersonas/PersonaAnonymousEmployer.uasset, /Game/Campaign/Personas/ProcMissionPersonas/PersonaAnonymousEmployer.uexp
- strings: `32`
- tokens: `PersonaAnonymousEmployer`, `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/Personas/ProcMissionPersonas/PersonaAnonymousEmployer`

### `/Game/Campaign/Personas/ProcMissionPersonas/PersonaAnonymousEmployer2`

- files: /Game/Campaign/Personas/ProcMissionPersonas/PersonaAnonymousEmployer2.uasset, /Game/Campaign/Personas/ProcMissionPersonas/PersonaAnonymousEmployer2.uexp
- strings: `32`
- tokens: `PersonaAnonymousEmployer`, `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/Personas/ProcMissionPersonas/PersonaAnonymousEmployer2`

### `/Game/Employers/ClanGhostBear`

- files: /Game/Employers/ClanGhostBear.uasset, /Game/Employers/ClanGhostBear.uexp
- strings: `28`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/ClanGhostBear`

### `/Game/Employers/ClanJadeFalcon`

- files: /Game/Employers/ClanJadeFalcon.uasset, /Game/Employers/ClanJadeFalcon.uexp
- strings: `27`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/ClanJadeFalcon`

### `/Game/Employers/ClanSmokeJaguar`

- files: /Game/Employers/ClanSmokeJaguar.uasset, /Game/Employers/ClanSmokeJaguar.uexp
- strings: `28`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/ClanSmokeJaguar`

### `/Game/Employers/ClanWolf`

- files: /Game/Employers/ClanWolf.uasset, /Game/Employers/ClanWolf.uexp
- strings: `28`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/ClanWolf`

### `/Game/Employers/Unused/AllianceOfGaledon`

- files: /Game/Employers/Unused/AllianceOfGaledon.uasset, /Game/Employers/Unused/AllianceOfGaledon.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/AllianceOfGaledon`

### `/Game/Employers/Unused/AmarisEmpire`

- files: /Game/Employers/Unused/AmarisEmpire.uasset, /Game/Employers/Unused/AmarisEmpire.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/AmarisEmpire`

### `/Game/Employers/Unused/AxumiteProvidence`

- files: /Game/Employers/Unused/AxumiteProvidence.uasset, /Game/Employers/Unused/AxumiteProvidence.uexp
- strings: `27`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/AxumiteProvidence`

### `/Game/Employers/Unused/AzamiBrotherhood`

- files: /Game/Employers/Unused/AzamiBrotherhood.uasset, /Game/Employers/Unused/AzamiBrotherhood.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/AzamiBrotherhood`

### `/Game/Employers/Unused/AzamiCaliphate`

- files: /Game/Employers/Unused/AzamiCaliphate.uasset, /Game/Employers/Unused/AzamiCaliphate.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/AzamiCaliphate`

### `/Game/Employers/Unused/CalderonProtectorate`

- files: /Game/Employers/Unused/CalderonProtectorate.uasset, /Game/Employers/Unused/CalderonProtectorate.uexp
- strings: `27`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/CalderonProtectorate`

### `/Game/Employers/Unused/CapellanCommonality`

- files: /Game/Employers/Unused/CapellanCommonality.uasset, /Game/Employers/Unused/CapellanCommonality.uexp
- strings: `30`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/CapellanCommonality`

### `/Game/Employers/Unused/CapellanHegemony`

- files: /Game/Employers/Unused/CapellanHegemony.uasset, /Game/Employers/Unused/CapellanHegemony.uexp
- strings: `30`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/CapellanHegemony`

### `/Game/Employers/Unused/ChainelaneIsles`

- files: /Game/Employers/Unused/ChainelaneIsles.uasset, /Game/Employers/Unused/ChainelaneIsles.uexp
- strings: `26`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ChainelaneIsles`

### `/Game/Employers/Unused/ChaosMarch`

- files: /Game/Employers/Unused/ChaosMarch.uasset, /Game/Employers/Unused/ChaosMarch.uexp
- strings: `31`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ChaosMarch`

### `/Game/Employers/Unused/ChestertonTradeFederation`

- files: /Game/Employers/Unused/ChestertonTradeFederation.uasset, /Game/Employers/Unused/ChestertonTradeFederation.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ChestertonTradeFederation`

### `/Game/Employers/Unused/ClanBloodSpirit`

- files: /Game/Employers/Unused/ClanBloodSpirit.uasset, /Game/Employers/Unused/ClanBloodSpirit.uexp
- strings: `23`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ClanBloodSpirit`

### `/Game/Employers/Unused/ClanBurrock`

- files: /Game/Employers/Unused/ClanBurrock.uasset, /Game/Employers/Unused/ClanBurrock.uexp
- strings: `22`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ClanBurrock`

### `/Game/Employers/Unused/ClanCloudCobra`

- files: /Game/Employers/Unused/ClanCloudCobra.uasset, /Game/Employers/Unused/ClanCloudCobra.uexp
- strings: `21`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ClanCloudCobra`

### `/Game/Employers/Unused/ClanCoyote`

- files: /Game/Employers/Unused/ClanCoyote.uasset, /Game/Employers/Unused/ClanCoyote.uexp
- strings: `21`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ClanCoyote`

### `/Game/Employers/Unused/ClanDiamondShark`

- files: /Game/Employers/Unused/ClanDiamondShark.uasset, /Game/Employers/Unused/ClanDiamondShark.uexp
- strings: `22`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ClanDiamondShark`

### `/Game/Employers/Unused/ClanFireMandrill`

- files: /Game/Employers/Unused/ClanFireMandrill.uasset, /Game/Employers/Unused/ClanFireMandrill.uexp
- strings: `22`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ClanFireMandrill`

### `/Game/Employers/Unused/ClanGoliathScorpion`

- files: /Game/Employers/Unused/ClanGoliathScorpion.uasset, /Game/Employers/Unused/ClanGoliathScorpion.uexp
- strings: `22`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ClanGoliathScorpion`

### `/Game/Employers/Unused/ClanHellsHorses`

- files: /Game/Employers/Unused/ClanHellsHorses.uasset, /Game/Employers/Unused/ClanHellsHorses.uexp
- strings: `21`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ClanHellsHorses`

### `/Game/Employers/Unused/ClanIceHellion`

- files: /Game/Employers/Unused/ClanIceHellion.uasset, /Game/Employers/Unused/ClanIceHellion.uexp
- strings: `22`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ClanIceHellion`

### `/Game/Employers/Unused/ClanMongoose`

- files: /Game/Employers/Unused/ClanMongoose.uasset, /Game/Employers/Unused/ClanMongoose.uexp
- strings: `22`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ClanMongoose`

### `/Game/Employers/Unused/ClanNovaCat`

- files: /Game/Employers/Unused/ClanNovaCat.uasset, /Game/Employers/Unused/ClanNovaCat.uexp
- strings: `22`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ClanNovaCat`

### `/Game/Employers/Unused/ClanSeaFox`

- files: /Game/Employers/Unused/ClanSeaFox.uasset, /Game/Employers/Unused/ClanSeaFox.uexp
- strings: `21`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ClanSeaFox`

### `/Game/Employers/Unused/ClanSnowRaven`

- files: /Game/Employers/Unused/ClanSnowRaven.uasset, /Game/Employers/Unused/ClanSnowRaven.uexp
- strings: `22`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ClanSnowRaven`

### `/Game/Employers/Unused/ClanStarAdder`

- files: /Game/Employers/Unused/ClanStarAdder.uasset, /Game/Employers/Unused/ClanStarAdder.uexp
- strings: `22`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ClanStarAdder`

### `/Game/Employers/Unused/ClanSteelViper`

- files: /Game/Employers/Unused/ClanSteelViper.uasset, /Game/Employers/Unused/ClanSteelViper.uexp
- strings: `22`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ClanSteelViper`

### `/Game/Employers/Unused/ClanStoneLion`

- files: /Game/Employers/Unused/ClanStoneLion.uasset, /Game/Employers/Unused/ClanStoneLion.uexp
- strings: `22`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ClanStoneLion`

### `/Game/Employers/Unused/ClanWidowmaker`

- files: /Game/Employers/Unused/ClanWidowmaker.uasset, /Game/Employers/Unused/ClanWidowmaker.uexp
- strings: `23`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ClanWidowmaker`

### `/Game/Employers/Unused/ClanWolfinExile`

- files: /Game/Employers/Unused/ClanWolfinExile.uasset, /Game/Employers/Unused/ClanWolfinExile.uexp
- strings: `23`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ClanWolfinExile`

### `/Game/Employers/Unused/ClanWolverine`

- files: /Game/Employers/Unused/ClanWolverine.uasset, /Game/Employers/Unused/ClanWolverine.uexp
- strings: `23`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ClanWolverine`

### `/Game/Employers/Unused/CoalitionForces`

- files: /Game/Employers/Unused/CoalitionForces.uasset, /Game/Employers/Unused/CoalitionForces.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/CoalitionForces`

### `/Game/Employers/Unused/DuchyOfGrahamMarik`

- files: /Game/Employers/Unused/DuchyOfGrahamMarik.uasset, /Game/Employers/Unused/DuchyOfGrahamMarik.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/DuchyOfGrahamMarik`

### `/Game/Employers/Unused/DuchyOfLiao`

- files: /Game/Employers/Unused/DuchyOfLiao.uasset, /Game/Employers/Unused/DuchyOfLiao.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/DuchyOfLiao`

### `/Game/Employers/Unused/DuchyOfOriente`

- files: /Game/Employers/Unused/DuchyOfOriente.uasset, /Game/Employers/Unused/DuchyOfOriente.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/DuchyOfOriente`

### `/Game/Employers/Unused/DuchyOfOrloff`

- files: /Game/Employers/Unused/DuchyOfOrloff.uasset, /Game/Employers/Unused/DuchyOfOrloff.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/DuchyOfOrloff`

### `/Game/Employers/Unused/DuchyOfSmall`

- files: /Game/Employers/Unused/DuchyOfSmall.uasset, /Game/Employers/Unused/DuchyOfSmall.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/DuchyOfSmall`

### `/Game/Employers/Unused/DuchyOfTamarind`

- files: /Game/Employers/Unused/DuchyOfTamarind.uasset, /Game/Employers/Unused/DuchyOfTamarind.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/DuchyOfTamarind`

### `/Game/Employers/Unused/DuchyOfTamarindAbbey`

- files: /Game/Employers/Unused/DuchyOfTamarindAbbey.uasset, /Game/Employers/Unused/DuchyOfTamarindAbbey.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/DuchyOfTamarindAbbey`

### `/Game/Employers/Unused/EscorpinImperio`

- files: /Game/Employers/Unused/EscorpinImperio.uasset, /Game/Employers/Unused/EscorpinImperio.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/EscorpinImperio`

### `/Game/Employers/Unused/FederationOfOriente`

- files: /Game/Employers/Unused/FederationOfOriente.uasset, /Game/Employers/Unused/FederationOfOriente.uexp
- strings: `30`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/FederationOfOriente`

### `/Game/Employers/Unused/FederationOfSkye`

- files: /Game/Employers/Unused/FederationOfSkye.uasset, /Game/Employers/Unused/FederationOfSkye.uexp
- strings: `29`
- tokens: `Steiner`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/FederationOfSkye`

### `/Game/Employers/Unused/FerrisCollective`

- files: /Game/Employers/Unused/FerrisCollective.uasset, /Game/Employers/Unused/FerrisCollective.uexp
- strings: `27`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/FerrisCollective`

### `/Game/Employers/Unused/FiltveltCoalition`

- files: /Game/Employers/Unused/FiltveltCoalition.uasset, /Game/Employers/Unused/FiltveltCoalition.uexp
- strings: `27`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/FiltveltCoalition`

### `/Game/Employers/Unused/FinmarkFreeRepublic`

- files: /Game/Employers/Unused/FinmarkFreeRepublic.uasset, /Game/Employers/Unused/FinmarkFreeRepublic.uexp
- strings: `26`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/FinmarkFreeRepublic`

### `/Game/Employers/Unused/FreeWorldsLeagueMilitaryRegion`

- files: /Game/Employers/Unused/FreeWorldsLeagueMilitaryRegion.uasset, /Game/Employers/Unused/FreeWorldsLeagueMilitaryRegion.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/FreeWorldsLeagueMilitaryRegion`

### `/Game/Employers/Unused/FroncReaches`

- files: /Game/Employers/Unused/FroncReaches.uasset, /Game/Employers/Unused/FroncReaches.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/FroncReaches`

### `/Game/Employers/Unused/GalateanLeague`

- files: /Game/Employers/Unused/GalateanLeague.uasset, /Game/Employers/Unused/GalateanLeague.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/GalateanLeague`

### `/Game/Employers/Unused/GhostBearDominion`

- files: /Game/Employers/Unused/GhostBearDominion.uasset, /Game/Employers/Unused/GhostBearDominion.uexp
- strings: `22`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/GhostBearDominion`

### `/Game/Employers/Unused/HanseaticLeague`

- files: /Game/Employers/Unused/HanseaticLeague.uasset, /Game/Employers/Unused/HanseaticLeague.uexp
- strings: `27`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/HanseaticLeague`

### `/Game/Employers/Unused/Jarnfolk`

- files: /Game/Employers/Unused/Jarnfolk.uasset, /Game/Employers/Unused/Jarnfolk.uexp
- strings: `26`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/Jarnfolk`

### `/Game/Employers/Unused/KhwarazmEmpire`

- files: /Game/Employers/Unused/KhwarazmEmpire.uasset, /Game/Employers/Unused/KhwarazmEmpire.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/KhwarazmEmpire`

### `/Game/Employers/Unused/KitteryPrefecture`

- files: /Game/Employers/Unused/KitteryPrefecture.uasset, /Game/Employers/Unused/KitteryPrefecture.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/KitteryPrefecture`

### `/Game/Employers/Unused/LiaoRepublic`

- files: /Game/Employers/Unused/LiaoRepublic.uasset, /Game/Employers/Unused/LiaoRepublic.uexp
- strings: `30`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/LiaoRepublic`

### `/Game/Employers/Unused/LyranAlliance`

- files: /Game/Employers/Unused/LyranAlliance.uasset, /Game/Employers/Unused/LyranAlliance.uexp
- strings: `28`
- tokens: `Lyran`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/LyranAlliance`

### `/Game/Employers/Unused/MalagrottaCooperative`

- files: /Game/Employers/Unused/MalagrottaCooperative.uasset, /Game/Employers/Unused/MalagrottaCooperative.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/MalagrottaCooperative`

### `/Game/Employers/Unused/MarikCommonwealth`

- files: /Game/Employers/Unused/MarikCommonwealth.uasset, /Game/Employers/Unused/MarikCommonwealth.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/MarikCommonwealth`

### `/Game/Employers/Unused/MarikRepublic`

- files: /Game/Employers/Unused/MarikRepublic.uasset, /Game/Employers/Unused/MarikRepublic.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/MarikRepublic`

### `/Game/Employers/Unused/MarikStewartCommonwealth`

- files: /Game/Employers/Unused/MarikStewartCommonwealth.uasset, /Game/Employers/Unused/MarikStewartCommonwealth.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/MarikStewartCommonwealth`

### `/Game/Employers/Unused/MarletteAssociation`

- files: /Game/Employers/Unused/MarletteAssociation.uasset, /Game/Employers/Unused/MarletteAssociation.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/MarletteAssociation`

### `/Game/Employers/Unused/MosiroArchipelago`

- files: /Game/Employers/Unused/MosiroArchipelago.uasset, /Game/Employers/Unused/MosiroArchipelago.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/MosiroArchipelago`

### `/Game/Employers/Unused/MuskegonCoalition`

- files: /Game/Employers/Unused/MuskegonCoalition.uasset, /Game/Employers/Unused/MuskegonCoalition.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/MuskegonCoalition`

### `/Game/Employers/Unused/NewColonyRegion`

- files: /Game/Employers/Unused/NewColonyRegion.uasset, /Game/Employers/Unused/NewColonyRegion.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/NewColonyRegion`

### `/Game/Employers/Unused/NewDelphiCompact`

- files: /Game/Employers/Unused/NewDelphiCompact.uasset, /Game/Employers/Unused/NewDelphiCompact.uexp
- strings: `27`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/NewDelphiCompact`

### `/Game/Employers/Unused/NewOberonConfederation`

- files: /Game/Employers/Unused/NewOberonConfederation.uasset, /Game/Employers/Unused/NewOberonConfederation.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/NewOberonConfederation`

### `/Game/Employers/Unused/NuevaCastile`

- files: /Game/Employers/Unused/NuevaCastile.uasset, /Game/Employers/Unused/NuevaCastile.uexp
- strings: `30`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/NuevaCastile`

### `/Game/Employers/Unused/OhrensonZionProvince`

- files: /Game/Employers/Unused/OhrensonZionProvince.uasset, /Game/Employers/Unused/OhrensonZionProvince.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/OhrensonZionProvince`

### `/Game/Employers/Unused/OrienteProtectorate`

- files: /Game/Employers/Unused/OrienteProtectorate.uasset, /Game/Employers/Unused/OrienteProtectorate.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/OrienteProtectorate`

### `/Game/Employers/Unused/OzawaMercantileAssociation`

- files: /Game/Employers/Unused/OzawaMercantileAssociation.uasset, /Game/Employers/Unused/OzawaMercantileAssociation.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/OzawaMercantileAssociation`

### `/Game/Employers/Unused/PrincipalityOfGibson`

- files: /Game/Employers/Unused/PrincipalityOfGibson.uasset, /Game/Employers/Unused/PrincipalityOfGibson.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/PrincipalityOfGibson`

### `/Game/Employers/Unused/PrincipalityOfRasalhague`

- files: /Game/Employers/Unused/PrincipalityOfRasalhague.uasset, /Game/Employers/Unused/PrincipalityOfRasalhague.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/PrincipalityOfRasalhague`

### `/Game/Employers/Unused/PrincipalityOfRegulus`

- files: /Game/Employers/Unused/PrincipalityOfRegulus.uasset, /Game/Employers/Unused/PrincipalityOfRegulus.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/PrincipalityOfRegulus`

### `/Game/Employers/Unused/ProtectorateOfDonegal`

- files: /Game/Employers/Unused/ProtectorateOfDonegal.uasset, /Game/Employers/Unused/ProtectorateOfDonegal.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/ProtectorateOfDonegal`

### `/Game/Employers/Unused/RagnarkUnion`

- files: /Game/Employers/Unused/RagnarkUnion.uasset, /Game/Employers/Unused/RagnarkUnion.uexp
- strings: `30`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/RagnarkUnion`

### `/Game/Employers/Unused/RasalhagueDominion`

- files: /Game/Employers/Unused/RasalhagueDominion.uasset, /Game/Employers/Unused/RasalhagueDominion.uexp
- strings: `27`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/RasalhagueDominion`

### `/Game/Employers/Unused/RavenAlliance`

- files: /Game/Employers/Unused/RavenAlliance.uasset, /Game/Employers/Unused/RavenAlliance.uexp
- strings: `27`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/RavenAlliance`

### `/Game/Employers/Unused/RegulanFiefs`

- files: /Game/Employers/Unused/RegulanFiefs.uasset, /Game/Employers/Unused/RegulanFiefs.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/RegulanFiefs`

### `/Game/Employers/Unused/RegulanFreeStates`

- files: /Game/Employers/Unused/RegulanFreeStates.uasset, /Game/Employers/Unused/RegulanFreeStates.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/RegulanFreeStates`

### `/Game/Employers/Unused/RegulanPrincipality`

- files: /Game/Employers/Unused/RegulanPrincipality.uasset, /Game/Employers/Unused/RegulanPrincipality.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/RegulanPrincipality`

### `/Game/Employers/Unused/RepublicOfTheBarrens`

- files: /Game/Employers/Unused/RepublicOfTheBarrens.uasset, /Game/Employers/Unused/RepublicOfTheBarrens.uexp
- strings: `27`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/RepublicOfTheBarrens`

### `/Game/Employers/Unused/RepublicOfTheSphere`

- files: /Game/Employers/Unused/RepublicOfTheSphere.uasset, /Game/Employers/Unused/RepublicOfTheSphere.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/RepublicOfTheSphere`

### `/Game/Employers/Unused/RimCommonality`

- files: /Game/Employers/Unused/RimCommonality.uasset, /Game/Employers/Unused/RimCommonality.uexp
- strings: `30`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/RimCommonality`

### `/Game/Employers/Unused/RimTerritories`

- files: /Game/Employers/Unused/RimTerritories.uasset, /Game/Employers/Unused/RimTerritories.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/RimTerritories`

### `/Game/Employers/Unused/RimWorldsRepublic`

- files: /Game/Employers/Unused/RimWorldsRepublic.uasset, /Game/Employers/Unused/RimWorldsRepublic.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/RimWorldsRepublic`

### `/Game/Employers/Unused/SaiphTriumvirate`

- files: /Game/Employers/Unused/SaiphTriumvirate.uasset, /Game/Employers/Unused/SaiphTriumvirate.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/SaiphTriumvirate`

### `/Game/Employers/Unused/SarnaSupremacy`

- files: /Game/Employers/Unused/SarnaSupremacy.uasset, /Game/Employers/Unused/SarnaSupremacy.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/SarnaSupremacy`

### `/Game/Employers/Unused/SenateAlliance`

- files: /Game/Employers/Unused/SenateAlliance.uasset, /Game/Employers/Unused/SenateAlliance.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/SenateAlliance`

### `/Game/Employers/Unused/SianCommonwealth`

- files: /Game/Employers/Unused/SianCommonwealth.uasset, /Game/Employers/Unused/SianCommonwealth.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/SianCommonwealth`

### `/Game/Employers/Unused/SilverHawkCoalition`

- files: /Game/Employers/Unused/SilverHawkCoalition.uasset, /Game/Employers/Unused/SilverHawkCoalition.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/SilverHawkCoalition`

### `/Game/Employers/Unused/StarLeagueinExile`

- files: /Game/Employers/Unused/StarLeagueinExile.uasset, /Game/Employers/Unused/StarLeagueinExile.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/StarLeagueinExile`

### `/Game/Employers/Unused/StewartConfederation`

- files: /Game/Employers/Unused/StewartConfederation.uasset, /Game/Employers/Unused/StewartConfederation.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/StewartConfederation`

### `/Game/Employers/Unused/StIvesMercantileAssociation`

- files: /Game/Employers/Unused/StIvesMercantileAssociation.uasset, /Game/Employers/Unused/StIvesMercantileAssociation.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/StIvesMercantileAssociation`

### `/Game/Employers/Unused/StykCommonality`

- files: /Game/Employers/Unused/StykCommonality.uasset, /Game/Employers/Unused/StykCommonality.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/StykCommonality`

### `/Game/Employers/Unused/TamarPact`

- files: /Game/Employers/Unused/TamarPact.uasset, /Game/Employers/Unused/TamarPact.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/TamarPact`

### `/Game/Employers/Unused/TaurianHomeworlds`

- files: /Game/Employers/Unused/TaurianHomeworlds.uasset, /Game/Employers/Unused/TaurianHomeworlds.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/TaurianHomeworlds`

### `/Game/Employers/Unused/TerracapConfederation`

- files: /Game/Employers/Unused/TerracapConfederation.uasset, /Game/Employers/Unused/TerracapConfederation.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/TerracapConfederation`

### `/Game/Employers/Unused/TerranAlliance`

- files: /Game/Employers/Unused/TerranAlliance.uasset, /Game/Employers/Unused/TerranAlliance.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/TerranAlliance`

### `/Game/Employers/Unused/TerranHegemony`

- files: /Game/Employers/Unused/TerranHegemony.uasset, /Game/Employers/Unused/TerranHegemony.uexp
- strings: `27`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/TerranHegemony`

### `/Game/Employers/Unused/TheHavens`

- files: /Game/Employers/Unused/TheHavens.uasset, /Game/Employers/Unused/TheHavens.uexp
- strings: `27`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/TheHavens`

### `/Game/Employers/Unused/TheProtectorate`

- files: /Game/Employers/Unused/TheProtectorate.uasset, /Game/Employers/Unused/TheProtectorate.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/TheProtectorate`

### `/Game/Employers/Unused/TheRepublicRemnant`

- files: /Game/Employers/Unused/TheRepublicRemnant.uasset, /Game/Employers/Unused/TheRepublicRemnant.uexp
- strings: `29`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/TheRepublicRemnant`

### `/Game/Employers/Unused/TikonovGrandUnion`

- files: /Game/Employers/Unused/TikonovGrandUnion.uasset, /Game/Employers/Unused/TikonovGrandUnion.uexp
- strings: `28`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/TikonovGrandUnion`

### `/Game/Employers/Unused/UnitedHinduCollective`

- files: /Game/Employers/Unused/UnitedHinduCollective.uasset, /Game/Employers/Unused/UnitedHinduCollective.uexp
- strings: `30`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/UnitedHinduCollective`

### `/Game/Employers/Unused/WolfEmpire`

- files: /Game/Employers/Unused/WolfEmpire.uasset, /Game/Employers/Unused/WolfEmpire.uexp
- strings: `21`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/WolfEmpire`

### `/Game/Employers/Unused/WordOfBlake`

- files: /Game/Employers/Unused/WordOfBlake.uasset, /Game/Employers/Unused/WordOfBlake.uexp
- strings: `30`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Employers/Unused/WordOfBlake`

### `/Game/Factions/CircinusFederation`

- files: /Game/Factions/CircinusFederation.uasset, /Game/Factions/CircinusFederation.uexp
- strings: `40`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Factions/CircinusFederation`

### `/Game/Factions/Clan`

- files: /Game/Factions/Clan.uasset, /Game/Factions/Clan.uexp
- strings: `35`
- tokens: `Clan`, `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Factions/Clan`

### `/Game/Factions/ElysianFields`

- files: /Game/Factions/ElysianFields.uasset, /Game/Factions/ElysianFields.uexp
- strings: `37`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Factions/ElysianFields`

### `/Game/Factions/GreaterValkyrate`

- files: /Game/Factions/GreaterValkyrate.uasset, /Game/Factions/GreaterValkyrate.uexp
- strings: `37`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Factions/GreaterValkyrate`

### `/Game/Factions/IllyrianPalatinate`

- files: /Game/Factions/IllyrianPalatinate.uasset, /Game/Factions/IllyrianPalatinate.uexp
- strings: `36`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Factions/IllyrianPalatinate`

### `/Game/Factions/LothianLeague`

- files: /Game/Factions/LothianLeague.uasset, /Game/Factions/LothianLeague.uexp
- strings: `36`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Factions/LothianLeague`

### `/Game/Factions/MarianHegemony`

- files: /Game/Factions/MarianHegemony.uasset, /Game/Factions/MarianHegemony.uexp
- strings: `36`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Factions/MarianHegemony`

### `/Game/Factions/MorgrainesValkyrate`

- files: /Game/Factions/MorgrainesValkyrate.uasset, /Game/Factions/MorgrainesValkyrate.uexp
- strings: `37`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Factions/MorgrainesValkyrate`

### `/Game/Factions/NiopsAssociation`

- files: /Game/Factions/NiopsAssociation.uasset, /Game/Factions/NiopsAssociation.uexp
- strings: `37`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Factions/NiopsAssociation`

### `/Game/Factions/NoFaction`

- files: /Game/Factions/NoFaction.uasset, /Game/Factions/NoFaction.uexp
- strings: `27`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Factions/NoFaction`

### `/Game/Factions/OutworldsAlliance`

- files: /Game/Factions/OutworldsAlliance.uasset, /Game/Factions/OutworldsAlliance.uexp
- strings: `41`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Factions/OutworldsAlliance`

### `/Game/Factions/RimCollection`

- files: /Game/Factions/RimCollection.uasset, /Game/Factions/RimCollection.uexp
- strings: `39`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Factions/RimCollection`

### `/Game/Factions/TortugaDominions`

- files: /Game/Factions/TortugaDominions.uasset, /Game/Factions/TortugaDominions.uexp
- strings: `37`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Factions/TortugaDominions`

### `/Game/Factions/Unused/Amaris`

- files: /Game/Factions/Unused/Amaris.uasset, /Game/Factions/Unused/Amaris.uexp
- strings: `32`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Factions/Unused/Amaris`

### `/Game/Factions/Unused/StarLeague`

- files: /Game/Factions/Unused/StarLeague.uasset, /Game/Factions/Unused/StarLeague.uexp
- strings: `57`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Factions/Unused/StarLeague`

### `/Game/Factions/Unused/TikonovGrandUnion`

- files: /Game/Factions/Unused/TikonovGrandUnion.uasset, /Game/Factions/Unused/TikonovGrandUnion.uexp
- strings: `31`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Factions/Unused/TikonovGrandUnion`

### `/Game/Factions/Unused/WordOfBlake`

- files: /Game/Factions/Unused/WordOfBlake.uasset, /Game/Factions/Unused/WordOfBlake.uexp
- strings: `43`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Factions/Unused/WordOfBlake`

### `/Game/InnerSphereData/MW5_InnerSphereData`

- files: /Game/InnerSphereData/MW5_InnerSphereData.uasset, /Game/InnerSphereData/MW5_InnerSphereData.uexp
- strings: `7461`
- tokens: `CareerMode`, `Davion`, `Haynesville`, `CampaignArc`, `CampaignArcs`, `MW5_InnerSphereData`, `Lyran`, `Steiner`, `Clan`, `CustomContent`, `ModOverride`, `/Game/Campaign/CampaignArcs/BorderChanges`
- `CareerMode` examples: `/Game/DLC1/CareerMode/IndustrialHubs/IndustrialHubs_Meshes/RepairSystem`; `/Game/DLC1/CareerMode/IndustrialHubs/IndustrialHubs_Meshes/RepairSystem_35.RepairSystem`; `/Game/DLC1/CareerMode/IndustrialHubs/IndustrialHubs_Meshes/RepairSystem_36.RepairSystem`; `/Game/DLC1/CareerMode/IndustrialHubs/IndustrialHubs_Meshes/RepairSystem_37.RepairSystem`; `/Game/DLC1/CareerMode/Warzones/D_15/D`; `/Game/DLC1/CareerMode/Warzones/D_15/D_15.D`; `/Game/DLC1/CareerMode/Warzones/D_2_3/D_2`; `/Game/DLC1/CareerMode/Warzones/D_2_3/D_2_3.D_2`
- `Davion` examples: `DavionBorder`; `DavionBorderlands`; `DavionKurita`; `KuritaDavion`
- `Haynesville` examples: `Haynesville`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/InnerSphereData/MW5_InnerSphereData`

### `/Game/InnerSphereData/Updated/EmployerInfoData`

- files: /Game/InnerSphereData/Updated/EmployerInfoData.uasset, /Game/InnerSphereData/Updated/EmployerInfoData.uexp
- strings: `184`
- tokens: `EmployerInfoData`, `Lyran`, `Clan`, `ModOverride`
- `EmployerInfoData` examples: `/ModOverride/TheKnownUniverse/InnerSphereData/Updated/EmployerInfoData`; `EmployerInfoData`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/InnerSphereData/Updated/EmployerInfoData`

### `/Game/InnerSphereData/Updated/SystemFactionChanges`

- files: /Game/InnerSphereData/Updated/SystemFactionChanges.uasset, /Game/InnerSphereData/Updated/SystemFactionChanges.uexp
- strings: `4574`
- tokens: `Haynesville`, `SystemFactionChanges`, `Clan`, `ModOverride`
- `Haynesville` examples: `Haynesville`
- `SystemFactionChanges` examples: `/ModOverride/TheKnownUniverse/InnerSphereData/Updated/SystemFactionChanges`; `SystemFactionChanges`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/InnerSphereData/Updated/SystemFactionChanges`

### `/Game/Levels/FrontEnd/StarMap`

- files: /Game/Levels/FrontEnd/StarMap.uexp, /Game/Levels/FrontEnd/StarMap.umap
- strings: `1611`
- tokens: `StarMapActor`, `StarSystemBody`, `ModOverride`, `/Game/UI/FrontEnd/Starmap`
- `StarMapActor` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarMapActor`; `Default__StarMapActor_C`; `StarMapActor`; `StarMapActor_C`
- `StarSystemBody` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarSystemBody`; `Default__StarSystemBody_C`; `StarSystemBody_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Levels/FrontEnd/StarMap`; `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarMapActor`; `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarSystemBody`

### `/Game/Libraries/MW5_TOI_Functions`

- files: /Game/Libraries/MW5_TOI_Functions.uasset, /Game/Libraries/MW5_TOI_Functions.uexp
- strings: `346`
- tokens: `Davion`, `Steiner`, `ModOverride`
- `Davion` examples: `Davion`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Libraries/MW5_TOI_Functions`

### `/Game/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

- files: /Game/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL.uasset, /Game/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL.uexp
- strings: `610`
- tokens: `ModOverride`, `/Game/UI/FrontEnd/Starmap`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`; `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF`

### `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL`

- files: /Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL.uasset, /Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL.uexp
- strings: `229`
- tokens: `ModOverride`, `/Game/UI/FrontEnd/Starmap`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL`; `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF`

### `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF`

- files: /Game/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF.uasset, /Game/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF.uexp
- strings: `13`
- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF`

### `/Game/UI/FrontEnd/Starmap/StarMapActor`

- files: /Game/UI/FrontEnd/Starmap/StarMapActor.uasset, /Game/UI/FrontEnd/Starmap/StarMapActor.uexp
- strings: `526`
- tokens: `StarMapBorderActor`, `StarMapActor`, `StarSystemBody`, `ModOverride`, `/Game/UI/FrontEnd/Starmap`
- `StarMapActor` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarMapActor`; `Default__StarMapActor_C`; `ExecuteUbergraph_StarMapActor`; `StarMapActor_C`
- `StarSystemBody` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarSystemBody`; `Default__StarSystemBody_C`; `FindStarSystemBodyById`; `MWStarSystemBody`; `StarSystemBody_C`; `StarSystemBodyLookUp`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarMapActor`; `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarSystemBody`

### `/Game/UI/FrontEnd/Starmap/StarSystemBody`

- files: /Game/UI/FrontEnd/Starmap/StarSystemBody.uasset, /Game/UI/FrontEnd/Starmap/StarSystemBody.uexp
- strings: `377`
- tokens: `StarMapActor`, `StarSystemBody`, `ModOverride`, `/Game/UI/FrontEnd/Starmap`
- `StarMapActor` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarMapActor`; `CallFunc_GetStarmapActor_Output`; `Default__StarMapActor_C`; `GetStarmapActor`; `StarMapActor_C`
- `StarSystemBody` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarSystemBody`; `Default__MWStarSystemBody`; `Default__StarSystemBody_C`; `ExecuteUbergraph_StarSystemBody`; `MWStarSystemBody`; `StarSystemBody_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarMapActor`; `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarSystemBody`

### `/Game/UI/FrontEnd/StarMapPawn`

- files: /Game/UI/FrontEnd/StarMapPawn.uasset, /Game/UI/FrontEnd/StarMapPawn.uexp
- strings: `56`
- tokens: `StarMapPawn`, `ModOverride`, `/Game/UI/FrontEnd/Starmap`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/StarMapPawn`

## Plugin Region And Timeline Assets

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_13`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_16`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_18`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_20`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_27`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_39`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/2864-01-01_8`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/Borders2864-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/2864-01-01/StarMapBorderActor2864-01-01`; `/TheKnownUniverse/2864-01-01/StarMapBorderActor2864-01-01.StarMapBorderActor2864-01-01_C`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/StarMapBorderActor2864-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/2864-01-01/StarMapBorderActor2864-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor2864-01-01_C`; `StarMapBorderActor2864-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/StarMapBordersUpdate_Action_2864-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/2864-01-01/StarMapBordersUpdate_Action_2864-01-01`; `Default__StarMapBordersUpdate_Action_2864-01-01_C`; `StarMapBordersUpdate_Action_2864-01-01_C`

### `/Plugins/TheKnownUniverse/Content/2864-01-01/year_2864-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/2864-01-01/StarMapBordersUpdate_Action_2864-01-01`; `/TheKnownUniverse/2864-01-01/StarMapBordersUpdate_Action_2864-01-01.StarMapBordersUpdate_Action_2864-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_20`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_22`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_27`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_39`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/3025-01-01_8`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/Borders3025-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3025-01-01/StarMapBorderActor3025-01-01`; `/TheKnownUniverse/3025-01-01/StarMapBorderActor3025-01-01.StarMapBorderActor3025-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/StarMapBorderActor3025-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3025-01-01/StarMapBorderActor3025-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3025-01-01_C`; `StarMapBorderActor3025-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/StarMapBordersUpdate_Action_3025-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3025-01-01/StarMapBordersUpdate_Action_3025-01-01`; `Default__StarMapBordersUpdate_Action_3025-01-01_C`; `StarMapBordersUpdate_Action_3025-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3025-01-01/year_3025-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3025-01-01/StarMapBordersUpdate_Action_3025-01-01`; `/TheKnownUniverse/3025-01-01/StarMapBordersUpdate_Action_3025-01-01.StarMapBordersUpdate_Action_3025-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_18`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_20`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_22`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_24`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_27`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_39`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/3030-01-01_8`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/Borders3030-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3030-01-01/StarMapBorderActor3030-01-01`; `/TheKnownUniverse/3030-01-01/StarMapBorderActor3030-01-01.StarMapBorderActor3030-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/StarMapBorderActor3030-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3030-01-01/StarMapBorderActor3030-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3030-01-01_C`; `StarMapBorderActor3030-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/StarMapBordersUpdate_Action_3030-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3030-01-01/StarMapBordersUpdate_Action_3030-01-01`; `Default__StarMapBordersUpdate_Action_3030-01-01_C`; `StarMapBordersUpdate_Action_3030-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3030-01-01/year_3030-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3030-01-01/StarMapBordersUpdate_Action_3030-01-01`; `/TheKnownUniverse/3030-01-01/StarMapBordersUpdate_Action_3030-01-01.StarMapBordersUpdate_Action_3030-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_18`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_20`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_22`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_24`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_27`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_39`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_8`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/3034-01-01_9`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/Borders3034-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3034-01-01/StarMapBorderActor3034-01-01`; `/TheKnownUniverse/3034-01-01/StarMapBorderActor3034-01-01.StarMapBorderActor3034-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/StarMapBorderActor3034-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3034-01-01/StarMapBorderActor3034-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3034-01-01_C`; `StarMapBorderActor3034-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/StarMapBordersUpdate_Action_3034-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3034-01-01/StarMapBordersUpdate_Action_3034-01-01`; `Default__StarMapBordersUpdate_Action_3034-01-01_C`; `StarMapBordersUpdate_Action_3034-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3034-01-01/year_3034-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3034-01-01/StarMapBordersUpdate_Action_3034-01-01`; `/TheKnownUniverse/3034-01-01/StarMapBordersUpdate_Action_3034-01-01.StarMapBordersUpdate_Action_3034-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_20`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_22`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_24`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_27`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_39`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_8`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/3040-01-01_9`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/Borders3040-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3040-01-01/StarMapBorderActor3040-01-01`; `/TheKnownUniverse/3040-01-01/StarMapBorderActor3040-01-01.StarMapBorderActor3040-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/StarMapBorderActor3040-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3040-01-01/StarMapBorderActor3040-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3040-01-01_C`; `StarMapBorderActor3040-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/StarMapBordersUpdate_Action_3040-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3040-01-01/StarMapBordersUpdate_Action_3040-01-01`; `Default__StarMapBordersUpdate_Action_3040-01-01_C`; `StarMapBordersUpdate_Action_3040-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3040-01-01/year_3040-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3040-01-01/StarMapBordersUpdate_Action_3040-01-01`; `/TheKnownUniverse/3040-01-01/StarMapBordersUpdate_Action_3040-01-01.StarMapBordersUpdate_Action_3040-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_16`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_20`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_24`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_27`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_8`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/3049-09-01_9`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/Borders3049-09-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3049-09-01/StarMapBorderActor3049-09-01`; `/TheKnownUniverse/3049-09-01/StarMapBorderActor3049-09-01.StarMapBorderActor3049-09-01_C`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/StarMapBorderActor3049-09-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3049-09-01/StarMapBorderActor3049-09-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3049-09-01_C`; `StarMapBorderActor3049-09-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/StarMapBordersUpdate_Action_3049-09-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3049-09-01/StarMapBordersUpdate_Action_3049-09-01`; `Default__StarMapBordersUpdate_Action_3049-09-01_C`; `StarMapBordersUpdate_Action_3049-09-01_C`

### `/Plugins/TheKnownUniverse/Content/3049-09-01/year_3049-09-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3049-09-01/StarMapBordersUpdate_Action_3049-09-01`; `/TheKnownUniverse/3049-09-01/StarMapBordersUpdate_Action_3049-09-01.StarMapBordersUpdate_Action_3049-09-01_C`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_16`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_20`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_24`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_27`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_8`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/3050-04-01_9`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/Borders3050-04-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3050-04-01/StarMapBorderActor3050-04-01`; `/TheKnownUniverse/3050-04-01/StarMapBorderActor3050-04-01.StarMapBorderActor3050-04-01_C`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/StarMapBorderActor3050-04-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3050-04-01/StarMapBorderActor3050-04-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3050-04-01_C`; `StarMapBorderActor3050-04-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/StarMapBordersUpdate_Action_3050-04-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3050-04-01/StarMapBordersUpdate_Action_3050-04-01`; `Default__StarMapBordersUpdate_Action_3050-04-01_C`; `StarMapBordersUpdate_Action_3050-04-01_C`

### `/Plugins/TheKnownUniverse/Content/3050-04-01/year_3050-04-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3050-04-01/StarMapBordersUpdate_Action_3050-04-01`; `/TheKnownUniverse/3050-04-01/StarMapBordersUpdate_Action_3050-04-01.StarMapBordersUpdate_Action_3050-04-01_C`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_16`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_20`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_24`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_27`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_8`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/3050-06-01_9`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/Borders3050-06-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3050-06-01/StarMapBorderActor3050-06-01`; `/TheKnownUniverse/3050-06-01/StarMapBorderActor3050-06-01.StarMapBorderActor3050-06-01_C`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/StarMapBorderActor3050-06-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3050-06-01/StarMapBorderActor3050-06-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3050-06-01_C`; `StarMapBorderActor3050-06-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/StarMapBordersUpdate_Action_3050-06-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3050-06-01/StarMapBordersUpdate_Action_3050-06-01`; `Default__StarMapBordersUpdate_Action_3050-06-01_C`; `StarMapBordersUpdate_Action_3050-06-01_C`

### `/Plugins/TheKnownUniverse/Content/3050-06-01/year_3050-06-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3050-06-01/StarMapBordersUpdate_Action_3050-06-01`; `/TheKnownUniverse/3050-06-01/StarMapBordersUpdate_Action_3050-06-01.StarMapBordersUpdate_Action_3050-06-01_C`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_16`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_20`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_24`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_27`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_8`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/3050-08-01_9`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/Borders3050-08-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3050-08-01/StarMapBorderActor3050-08-01`; `/TheKnownUniverse/3050-08-01/StarMapBorderActor3050-08-01.StarMapBorderActor3050-08-01_C`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/StarMapBorderActor3050-08-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3050-08-01/StarMapBorderActor3050-08-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3050-08-01_C`; `StarMapBorderActor3050-08-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/StarMapBordersUpdate_Action_3050-08-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3050-08-01/StarMapBordersUpdate_Action_3050-08-01`; `Default__StarMapBordersUpdate_Action_3050-08-01_C`; `StarMapBordersUpdate_Action_3050-08-01_C`

### `/Plugins/TheKnownUniverse/Content/3050-08-01/year_3050-08-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3050-08-01/StarMapBordersUpdate_Action_3050-08-01`; `/TheKnownUniverse/3050-08-01/StarMapBordersUpdate_Action_3050-08-01.StarMapBordersUpdate_Action_3050-08-01_C`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_16`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_20`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_24`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_27`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_8`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/3050-10-01_9`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/Borders3050-10-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3050-10-01/StarMapBorderActor3050-10-01`; `/TheKnownUniverse/3050-10-01/StarMapBorderActor3050-10-01.StarMapBorderActor3050-10-01_C`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/StarMapBorderActor3050-10-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3050-10-01/StarMapBorderActor3050-10-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3050-10-01_C`; `StarMapBorderActor3050-10-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/StarMapBordersUpdate_Action_3050-10-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3050-10-01/StarMapBordersUpdate_Action_3050-10-01`; `Default__StarMapBordersUpdate_Action_3050-10-01_C`; `StarMapBordersUpdate_Action_3050-10-01_C`

### `/Plugins/TheKnownUniverse/Content/3050-10-01/year_3050-10-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3050-10-01/StarMapBordersUpdate_Action_3050-10-01`; `/TheKnownUniverse/3050-10-01/StarMapBordersUpdate_Action_3050-10-01.StarMapBordersUpdate_Action_3050-10-01_C`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_16`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_20`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_24`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_27`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_8`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/3052-01-01_9`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/Borders3052-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3052-01-01/StarMapBorderActor3052-01-01`; `/TheKnownUniverse/3052-01-01/StarMapBorderActor3052-01-01.StarMapBorderActor3052-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/StarMapBorderActor3052-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3052-01-01/StarMapBorderActor3052-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3052-01-01_C`; `StarMapBorderActor3052-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/StarMapBordersUpdate_Action_3052-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3052-01-01/StarMapBordersUpdate_Action_3052-01-01`; `Default__StarMapBordersUpdate_Action_3052-01-01_C`; `StarMapBordersUpdate_Action_3052-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3052-01-01/year_3052-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3052-01-01/StarMapBordersUpdate_Action_3052-01-01`; `/TheKnownUniverse/3052-01-01/StarMapBordersUpdate_Action_3052-01-01.StarMapBordersUpdate_Action_3052-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_13`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_16`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_20`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_24`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_27`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/3057-01-01_9`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/Borders3057-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3057-01-01/StarMapBorderActor3057-01-01`; `/TheKnownUniverse/3057-01-01/StarMapBorderActor3057-01-01.StarMapBorderActor3057-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/StarMapBorderActor3057-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3057-01-01/StarMapBorderActor3057-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3057-01-01_C`; `StarMapBorderActor3057-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/StarMapBordersUpdate_Action_3057-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3057-01-01/StarMapBordersUpdate_Action_3057-01-01`; `Default__StarMapBordersUpdate_Action_3057-01-01_C`; `StarMapBordersUpdate_Action_3057-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3057-01-01/year_3057-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3057-01-01/StarMapBordersUpdate_Action_3057-01-01`; `/TheKnownUniverse/3057-01-01/StarMapBordersUpdate_Action_3057-01-01.StarMapBordersUpdate_Action_3057-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_13`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_16`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_20`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_21`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_24`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_27`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/3058-01-01_9`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/Borders3058-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3058-01-01/StarMapBorderActor3058-01-01`; `/TheKnownUniverse/3058-01-01/StarMapBorderActor3058-01-01.StarMapBorderActor3058-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/StarMapBorderActor3058-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3058-01-01/StarMapBorderActor3058-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3058-01-01_C`; `StarMapBorderActor3058-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/StarMapBordersUpdate_Action_3058-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3058-01-01/StarMapBordersUpdate_Action_3058-01-01`; `Default__StarMapBordersUpdate_Action_3058-01-01_C`; `StarMapBordersUpdate_Action_3058-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3058-01-01/year_3058-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3058-01-01/StarMapBordersUpdate_Action_3058-01-01`; `/TheKnownUniverse/3058-01-01/StarMapBordersUpdate_Action_3058-01-01.StarMapBordersUpdate_Action_3058-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_13`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_16`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_21`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_24`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_27`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/3059-01-01_9`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/Borders3059-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3059-01-01/StarMapBorderActor3059-01-01`; `/TheKnownUniverse/3059-01-01/StarMapBorderActor3059-01-01.StarMapBorderActor3059-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/StarMapBorderActor3059-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3059-01-01/StarMapBorderActor3059-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3059-01-01_C`; `StarMapBorderActor3059-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/StarMapBordersUpdate_Action_3059-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3059-01-01/StarMapBordersUpdate_Action_3059-01-01`; `Default__StarMapBordersUpdate_Action_3059-01-01_C`; `StarMapBordersUpdate_Action_3059-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3059-01-01/year_3059-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3059-01-01/StarMapBordersUpdate_Action_3059-01-01`; `/TheKnownUniverse/3059-01-01/StarMapBordersUpdate_Action_3059-01-01.StarMapBordersUpdate_Action_3059-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_13`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_16`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_21`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_24`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_27`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/3059-04-01_9`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/Borders3059-04-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3059-04-01/StarMapBorderActor3059-04-01`; `/TheKnownUniverse/3059-04-01/StarMapBorderActor3059-04-01.StarMapBorderActor3059-04-01_C`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/StarMapBorderActor3059-04-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3059-04-01/StarMapBorderActor3059-04-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3059-04-01_C`; `StarMapBorderActor3059-04-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/StarMapBordersUpdate_Action_3059-04-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3059-04-01/StarMapBordersUpdate_Action_3059-04-01`; `Default__StarMapBordersUpdate_Action_3059-04-01_C`; `StarMapBordersUpdate_Action_3059-04-01_C`

### `/Plugins/TheKnownUniverse/Content/3059-04-01/year_3059-04-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3059-04-01/StarMapBordersUpdate_Action_3059-04-01`; `/TheKnownUniverse/3059-04-01/StarMapBordersUpdate_Action_3059-04-01.StarMapBordersUpdate_Action_3059-04-01_C`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_13`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_16`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_21`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_24`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_27`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/3059-08-01_9`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/Borders3059-08-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3059-08-01/StarMapBorderActor3059-08-01`; `/TheKnownUniverse/3059-08-01/StarMapBorderActor3059-08-01.StarMapBorderActor3059-08-01_C`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/StarMapBorderActor3059-08-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3059-08-01/StarMapBorderActor3059-08-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3059-08-01_C`; `StarMapBorderActor3059-08-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/StarMapBordersUpdate_Action_3059-08-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3059-08-01/StarMapBordersUpdate_Action_3059-08-01`; `Default__StarMapBordersUpdate_Action_3059-08-01_C`; `StarMapBordersUpdate_Action_3059-08-01_C`

### `/Plugins/TheKnownUniverse/Content/3059-08-01/year_3059-08-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3059-08-01/StarMapBordersUpdate_Action_3059-08-01`; `/TheKnownUniverse/3059-08-01/StarMapBordersUpdate_Action_3059-08-01.StarMapBordersUpdate_Action_3059-08-01_C`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_13`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_16`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_21`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_24`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_27`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/3060-01-01_9`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/Borders3060-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3060-01-01/StarMapBorderActor3060-01-01`; `/TheKnownUniverse/3060-01-01/StarMapBorderActor3060-01-01.StarMapBorderActor3060-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/StarMapBorderActor3060-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3060-01-01/StarMapBorderActor3060-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3060-01-01_C`; `StarMapBorderActor3060-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/StarMapBordersUpdate_Action_3060-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3060-01-01/StarMapBordersUpdate_Action_3060-01-01`; `Default__StarMapBordersUpdate_Action_3060-01-01_C`; `StarMapBordersUpdate_Action_3060-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3060-01-01/year_3060-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3060-01-01/StarMapBordersUpdate_Action_3060-01-01`; `/TheKnownUniverse/3060-01-01/StarMapBordersUpdate_Action_3060-01-01.StarMapBordersUpdate_Action_3060-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_13`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_21`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_24`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_27`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/3063-01-01_9`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/Borders3063-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3063-01-01/StarMapBorderActor3063-01-01`; `/TheKnownUniverse/3063-01-01/StarMapBorderActor3063-01-01.StarMapBorderActor3063-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/StarMapBorderActor3063-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3063-01-01/StarMapBorderActor3063-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3063-01-01_C`; `StarMapBorderActor3063-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/StarMapBordersUpdate_Action_3063-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3063-01-01/StarMapBordersUpdate_Action_3063-01-01`; `Default__StarMapBordersUpdate_Action_3063-01-01_C`; `StarMapBordersUpdate_Action_3063-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3063-01-01/year_3063-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3063-01-01/StarMapBordersUpdate_Action_3063-01-01`; `/TheKnownUniverse/3063-01-01/StarMapBordersUpdate_Action_3063-01-01.StarMapBordersUpdate_Action_3063-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_13`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_21`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_27`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/3067-01-01_9`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/Borders3067-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3067-01-01/StarMapBorderActor3067-01-01`; `/TheKnownUniverse/3067-01-01/StarMapBorderActor3067-01-01.StarMapBorderActor3067-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/StarMapBorderActor3067-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3067-01-01/StarMapBorderActor3067-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3067-01-01_C`; `StarMapBorderActor3067-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/StarMapBordersUpdate_Action_3067-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3067-01-01/StarMapBordersUpdate_Action_3067-01-01`; `Default__StarMapBordersUpdate_Action_3067-01-01_C`; `StarMapBordersUpdate_Action_3067-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3067-01-01/year_3067-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3067-01-01/StarMapBordersUpdate_Action_3067-01-01`; `/TheKnownUniverse/3067-01-01/StarMapBordersUpdate_Action_3067-01-01.StarMapBordersUpdate_Action_3067-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_13`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_21`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_27`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/3068-01-01_9`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/Borders3068-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3068-01-01/StarMapBorderActor3068-01-01`; `/TheKnownUniverse/3068-01-01/StarMapBorderActor3068-01-01.StarMapBorderActor3068-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/StarMapBorderActor3068-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3068-01-01/StarMapBorderActor3068-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3068-01-01_C`; `StarMapBorderActor3068-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/StarMapBordersUpdate_Action_3068-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3068-01-01/StarMapBordersUpdate_Action_3068-01-01`; `Default__StarMapBordersUpdate_Action_3068-01-01_C`; `StarMapBordersUpdate_Action_3068-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3068-01-01/year_3068-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3068-01-01/StarMapBordersUpdate_Action_3068-01-01`; `/TheKnownUniverse/3068-01-01/StarMapBordersUpdate_Action_3068-01-01.StarMapBordersUpdate_Action_3068-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_13`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_18`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_21`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_27`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/3075-01-01_8`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/Borders3075-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3075-01-01/StarMapBorderActor3075-01-01`; `/TheKnownUniverse/3075-01-01/StarMapBorderActor3075-01-01.StarMapBorderActor3075-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/StarMapBorderActor3075-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3075-01-01/StarMapBorderActor3075-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3075-01-01_C`; `StarMapBorderActor3075-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/StarMapBordersUpdate_Action_3075-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3075-01-01/StarMapBordersUpdate_Action_3075-01-01`; `Default__StarMapBordersUpdate_Action_3075-01-01_C`; `StarMapBordersUpdate_Action_3075-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3075-01-01/year_3075-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3075-01-01/StarMapBordersUpdate_Action_3075-01-01`; `/TheKnownUniverse/3075-01-01/StarMapBordersUpdate_Action_3075-01-01.StarMapBordersUpdate_Action_3075-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_12`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_13`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_18`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_21`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_22`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_36`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/3079-01-01_8`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/Borders3079-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3079-01-01/StarMapBorderActor3079-01-01`; `/TheKnownUniverse/3079-01-01/StarMapBorderActor3079-01-01.StarMapBorderActor3079-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/StarMapBorderActor3079-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3079-01-01/StarMapBorderActor3079-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3079-01-01_C`; `StarMapBorderActor3079-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/StarMapBordersUpdate_Action_3079-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3079-01-01/StarMapBordersUpdate_Action_3079-01-01`; `Default__StarMapBordersUpdate_Action_3079-01-01_C`; `StarMapBordersUpdate_Action_3079-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3079-01-01/year_3079-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3079-01-01/StarMapBordersUpdate_Action_3079-01-01`; `/TheKnownUniverse/3079-01-01/StarMapBordersUpdate_Action_3079-01-01.StarMapBordersUpdate_Action_3079-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_13`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_18`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_21`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_22`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_36`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_8`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/3081-01-01_9`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/Borders3081-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3081-01-01/StarMapBorderActor3081-01-01`; `/TheKnownUniverse/3081-01-01/StarMapBorderActor3081-01-01.StarMapBorderActor3081-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/StarMapBorderActor3081-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3081-01-01/StarMapBorderActor3081-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3081-01-01_C`; `StarMapBorderActor3081-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/StarMapBordersUpdate_Action_3081-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3081-01-01/StarMapBordersUpdate_Action_3081-01-01`; `Default__StarMapBordersUpdate_Action_3081-01-01_C`; `StarMapBordersUpdate_Action_3081-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3081-01-01/year_3081-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3081-01-01/StarMapBordersUpdate_Action_3081-01-01`; `/TheKnownUniverse/3081-01-01/StarMapBordersUpdate_Action_3081-01-01.StarMapBordersUpdate_Action_3081-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_13`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_18`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_21`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_22`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_36`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_8`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/3085-01-01_9`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/Borders3085-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3085-01-01/StarMapBorderActor3085-01-01`; `/TheKnownUniverse/3085-01-01/StarMapBorderActor3085-01-01.StarMapBorderActor3085-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/StarMapBorderActor3085-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3085-01-01/StarMapBorderActor3085-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3085-01-01_C`; `StarMapBorderActor3085-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/StarMapBordersUpdate_Action_3085-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3085-01-01/StarMapBordersUpdate_Action_3085-01-01`; `Default__StarMapBordersUpdate_Action_3085-01-01_C`; `StarMapBordersUpdate_Action_3085-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3085-01-01/year_3085-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3085-01-01/StarMapBordersUpdate_Action_3085-01-01`; `/TheKnownUniverse/3085-01-01/StarMapBordersUpdate_Action_3085-01-01.StarMapBordersUpdate_Action_3085-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_10`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_13`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_15`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_18`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_21`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_22`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_36`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_39`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_8`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/3095-01-01_9`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/Borders3095-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3095-01-01/StarMapBorderActor3095-01-01`; `/TheKnownUniverse/3095-01-01/StarMapBorderActor3095-01-01.StarMapBorderActor3095-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/StarMapBorderActor3095-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3095-01-01/StarMapBorderActor3095-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3095-01-01_C`; `StarMapBorderActor3095-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/StarMapBordersUpdate_Action_3095-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3095-01-01/StarMapBordersUpdate_Action_3095-01-01`; `Default__StarMapBordersUpdate_Action_3095-01-01_C`; `StarMapBordersUpdate_Action_3095-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3095-01-01/year_3095-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3095-01-01/StarMapBordersUpdate_Action_3095-01-01`; `/TheKnownUniverse/3095-01-01/StarMapBordersUpdate_Action_3095-01-01.StarMapBordersUpdate_Action_3095-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_13`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_18`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_21`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_22`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_39`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/3130-01-01_8`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/Borders3130-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3130-01-01/StarMapBorderActor3130-01-01`; `/TheKnownUniverse/3130-01-01/StarMapBorderActor3130-01-01.StarMapBorderActor3130-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/StarMapBorderActor3130-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3130-01-01/StarMapBorderActor3130-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3130-01-01_C`; `StarMapBorderActor3130-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/StarMapBordersUpdate_Action_3130-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3130-01-01/StarMapBordersUpdate_Action_3130-01-01`; `Default__StarMapBordersUpdate_Action_3130-01-01_C`; `StarMapBordersUpdate_Action_3130-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3130-01-01/year_3130-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3130-01-01/StarMapBordersUpdate_Action_3130-01-01`; `/TheKnownUniverse/3130-01-01/StarMapBordersUpdate_Action_3130-01-01.StarMapBordersUpdate_Action_3130-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_13`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_14`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_18`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_19`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_21`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_22`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_39`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_7`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/3135-01-01_8`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/Borders3135-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3135-01-01/StarMapBorderActor3135-01-01`; `/TheKnownUniverse/3135-01-01/StarMapBorderActor3135-01-01.StarMapBorderActor3135-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/StarMapBorderActor3135-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3135-01-01/StarMapBorderActor3135-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3135-01-01_C`; `StarMapBorderActor3135-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/StarMapBordersUpdate_Action_3135-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3135-01-01/StarMapBordersUpdate_Action_3135-01-01`; `Default__StarMapBordersUpdate_Action_3135-01-01_C`; `StarMapBordersUpdate_Action_3135-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3135-01-01/year_3135-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3135-01-01/StarMapBordersUpdate_Action_3135-01-01`; `/TheKnownUniverse/3135-01-01/StarMapBordersUpdate_Action_3135-01-01.StarMapBordersUpdate_Action_3135-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_13`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_18`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_21`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_22`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_32`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_36`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_38`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_39`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/3145-01-01_8`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/Borders3145-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3145-01-01/StarMapBorderActor3145-01-01`; `/TheKnownUniverse/3145-01-01/StarMapBorderActor3145-01-01.StarMapBorderActor3145-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/StarMapBorderActor3145-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3145-01-01/StarMapBorderActor3145-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3145-01-01_C`; `StarMapBorderActor3145-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/StarMapBordersUpdate_Action_3145-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3145-01-01/StarMapBordersUpdate_Action_3145-01-01`; `Default__StarMapBordersUpdate_Action_3145-01-01_C`; `StarMapBordersUpdate_Action_3145-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3145-01-01/year_3145-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3145-01-01/StarMapBordersUpdate_Action_3145-01-01`; `/TheKnownUniverse/3145-01-01/StarMapBordersUpdate_Action_3145-01-01.StarMapBordersUpdate_Action_3145-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_11`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_13`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_17`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_18`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_2`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_21`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_22`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_23`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_25`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_26`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_28`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_29`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_3`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_30`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_31`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_34`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_35`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_36`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_37`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_39`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_4`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_40`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_5`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_6`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_8`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/3151-01-01_9`

- tokens: `ModOverride`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/Borders3151-01-01`

- tokens: `StarMapBorderActor`
- `StarMapBorderActor` examples: `/TheKnownUniverse/3151-01-01/StarMapBorderActor3151-01-01`; `/TheKnownUniverse/3151-01-01/StarMapBorderActor3151-01-01.StarMapBorderActor3151-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/StarMapBorderActor3151-01-01`

- tokens: `CampaignArc`, `CampaignArcs`, `BaseStarMapBorderActor`, `StarMapBorderActor`, `ModOverride`
- `CampaignArc` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `CampaignArcs` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `BaseStarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`
- `StarMapBorderActor` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`; `/TheKnownUniverse/3151-01-01/StarMapBorderActor3151-01-01`; `BaseStarMapBorderActor_C`; `Default__BaseStarMapBorderActor_C`; `Default__StarMapBorderActor3151-01-01_C`; `StarMapBorderActor3151-01-01_C`
- `ModOverride` examples: `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/StarMapBordersUpdate_Action_3151-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/StateChangeActions/UpdateStarmapBorders_ArcAction`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3151-01-01/StarMapBordersUpdate_Action_3151-01-01`; `Default__StarMapBordersUpdate_Action_3151-01-01_C`; `StarMapBordersUpdate_Action_3151-01-01_C`

### `/Plugins/TheKnownUniverse/Content/3151-01-01/year_3151-01-01`

- tokens: `CampaignArc`, `StarMapBordersUpdate_Action`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `StarMapBordersUpdate_Action` examples: `/TheKnownUniverse/3151-01-01/StarMapBordersUpdate_Action_3151-01-01`; `/TheKnownUniverse/3151-01-01/StarMapBordersUpdate_Action_3151-01-01.StarMapBordersUpdate_Action_3151-01-01_C`

### `/Plugins/TheKnownUniverse/Content/Regions/Safezones/CareerMode_CustomSafeZones`

- tokens: `CareerMode`, `CampaignArc`, `Clan`
- `CareerMode` examples: `/TheKnownUniverse/Regions/Safezones/CareerMode_CustomSafeZones`; `CareerMode_CustomSafeZones`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `Clan` examples: `/TheKnownUniverse/Regions/Safezones/PlaceSafeZone_Clan1_ArcAction`; `/TheKnownUniverse/Regions/Safezones/PlaceSafeZone_Clan1_ArcAction.PlaceSafeZone_Clan1_ArcAction_C`; `/TheKnownUniverse/Regions/Safezones/PlaceSafeZone_Clan2_ArcAction`; `/TheKnownUniverse/Regions/Safezones/PlaceSafeZone_Clan2_ArcAction.PlaceSafeZone_Clan2_ArcAction_C`

### `/Plugins/TheKnownUniverse/Content/Regions/Safezones/PlaceSafeZone_Clan1_ArcAction`

- tokens: `CampaignArc`, `Clan`, `PlaceClusterToi`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- `Clan` examples: `/TheKnownUniverse/Regions/Safezones/PlaceSafeZone_Clan1_ArcAction`; `Default__PlaceSafeZone_Clan1_ArcAction_C`; `PlaceSafeZone_Clan1_ArcAction_C`
- `PlaceClusterToi` examples: `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`; `Default__PlaceClusterToi_ArcAction_C`; `PlaceClusterToi_ArcAction_C`; `PlaceClusterToi_Config`; `PlaceClusterToi_Markups`

### `/Plugins/TheKnownUniverse/Content/Regions/Safezones/PlaceSafeZone_Clan2_ArcAction`

- tokens: `CampaignArc`, `Clan`, `PlaceClusterToi`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- `Clan` examples: `/TheKnownUniverse/Regions/Safezones/PlaceSafeZone_Clan2_ArcAction`; `Default__PlaceSafeZone_Clan2_ArcAction_C`; `PlaceSafeZone_Clan2_ArcAction_C`
- `PlaceClusterToi` examples: `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`; `Default__PlaceClusterToi_ArcAction_C`; `PlaceClusterToi_ArcAction_C`; `PlaceClusterToi_Config`; `PlaceClusterToi_Markups`

### `/Plugins/TheKnownUniverse/Content/Regions/Safezones/PlaceSafeZone_Custom1_ArcAction`

- tokens: `CampaignArc`, `PlaceClusterToi`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- `PlaceClusterToi` examples: `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`; `Default__PlaceClusterToi_ArcAction_C`; `PlaceClusterToi_ArcAction_C`; `PlaceClusterToi_Config`; `PlaceClusterToi_Markups`

### `/Plugins/TheKnownUniverse/Content/Regions/Safezones/PlaceSafeZone_Custom2_ArcAction`

- tokens: `CampaignArc`, `PlaceClusterToi`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- `PlaceClusterToi` examples: `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`; `Default__PlaceClusterToi_ArcAction_C`; `PlaceClusterToi_ArcAction_C`; `PlaceClusterToi_Config`; `PlaceClusterToi_Markups`

### `/Plugins/TheKnownUniverse/Content/Regions/TKU_Zones`

- tokens: `CareerMode`, `CampaignArc`
- `CareerMode` examples: `/TheKnownUniverse/Regions/Safezones/CareerMode_CustomSafeZones`; `/TheKnownUniverse/Regions/War/CareerModeCustomClusters`; `CareerMode_CustomSafeZones`; `CareerModeCustomClusters`
- `CampaignArc` examples: `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`

### `/Plugins/TheKnownUniverse/Content/Regions/War/CareerModeCustomClusters`

- tokens: `CareerMode`, `CampaignArc`, `Clan`
- `CareerMode` examples: `/TheKnownUniverse/Regions/War/CareerModeCustomClusters`; `CareerModeCustomClusters`
- `CampaignArc` examples: `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `Clan` examples: `/TheKnownUniverse/Regions/War/PlaceClanConflict`; `PlaceClanConflict`

### `/Plugins/TheKnownUniverse/Content/Regions/War/Place_ClanConflict_1`

- tokens: `CampaignArc`, `Clan`, `PlaceClusterToi`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- `Clan` examples: `/TheKnownUniverse/Regions/War/Place_ClanConflict`; `Clan Homeworlds`; `Clan Homeworlds and not much else`; `Default__Place_ClanConflict_1_C`; `Place_ClanConflict_1_C`
- `PlaceClusterToi` examples: `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`; `Default__PlaceClusterToi_ArcAction_C`; `PlaceClusterToi_ArcAction_C`; `PlaceClusterToi_Config`

### `/Plugins/TheKnownUniverse/Content/Regions/War/Place_ClanConflict_2`

- tokens: `CampaignArc`, `Clan`, `PlaceClusterToi`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- `Clan` examples: `/TheKnownUniverse/Regions/War/Place_ClanConflict`; `Clan Fringes`; `Clan Homeworlds and not much else`; `Default__Place_ClanConflict_2_C`; `Place_ClanConflict_2_C`
- `PlaceClusterToi` examples: `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`; `Default__PlaceClusterToi_ArcAction_C`; `PlaceClusterToi_ArcAction_C`; `PlaceClusterToi_Config`

### `/Plugins/TheKnownUniverse/Content/Regions/War/Place_ClanConflict_3`

- tokens: `CampaignArc`, `Clan`, `PlaceClusterToi`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- `Clan` examples: `/TheKnownUniverse/Regions/War/Place_ClanConflict`; `Clan Homeworlds and not much else`; `Default__Place_ClanConflict_3_C`; `Outer Clan Worlds`; `Place_ClanConflict_3_C`
- `PlaceClusterToi` examples: `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`; `Default__PlaceClusterToi_ArcAction_C`; `PlaceClusterToi_ArcAction_C`; `PlaceClusterToi_Config`

### `/Plugins/TheKnownUniverse/Content/Regions/War/Place_ClanConflict_4`

- tokens: `CampaignArc`, `Clan`, `PlaceClusterToi`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- `Clan` examples: `/TheKnownUniverse/Regions/War/Place_ClanConflict`; `Clan Homeworlds and not much else`; `Default__Place_ClanConflict_4_C`; `Inner Clan Worlds`; `Place_ClanConflict_4_C`
- `PlaceClusterToi` examples: `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`; `Default__PlaceClusterToi_ArcAction_C`; `PlaceClusterToi_ArcAction_C`; `PlaceClusterToi_Config`

### `/Plugins/TheKnownUniverse/Content/Regions/War/Place_CustomConflict`

- tokens: `CampaignArc`, `PlaceClusterToi`
- `CampaignArc` examples: `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`
- `PlaceClusterToi` examples: `/Game/Campaign/CampaignArcActions/MissionActions/PlaceClusterToi_ArcAction`; `Default__PlaceClusterToi_ArcAction_C`; `PlaceClusterToi_ArcAction_C`; `PlaceClusterToi_Config`

### `/Plugins/TheKnownUniverse/Content/Regions/War/PlaceClanConflict_1`

- tokens: `CampaignArc`, `Clan`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `Clan` examples: `/TheKnownUniverse/Regions/War/Place_ClanConflict`; `/TheKnownUniverse/Regions/War/Place_ClanConflict_1.Place_ClanConflict_1_C`; `/TheKnownUniverse/Regions/War/PlaceClanConflict`; `Place_ClanConflict`; `PlaceClanConflict`

### `/Plugins/TheKnownUniverse/Content/Regions/War/PlaceClanConflict_2`

- tokens: `CampaignArc`, `Clan`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `Clan` examples: `/TheKnownUniverse/Regions/War/Place_ClanConflict`; `/TheKnownUniverse/Regions/War/Place_ClanConflict_2.Place_ClanConflict_2_C`; `/TheKnownUniverse/Regions/War/PlaceClanConflict`; `Place_ClanConflict`; `PlaceClanConflict`

### `/Plugins/TheKnownUniverse/Content/Regions/War/PlaceClanConflict_3`

- tokens: `CampaignArc`, `Clan`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `Clan` examples: `/TheKnownUniverse/Regions/War/Place_ClanConflict`; `/TheKnownUniverse/Regions/War/Place_ClanConflict_3.Place_ClanConflict_3_C`; `/TheKnownUniverse/Regions/War/PlaceClanConflict`; `Place_ClanConflict`; `PlaceClanConflict`

### `/Plugins/TheKnownUniverse/Content/Regions/War/PlaceClanConflict_4`

- tokens: `CampaignArc`, `Clan`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
- `Clan` examples: `/TheKnownUniverse/Regions/War/Place_ClanConflict`; `/TheKnownUniverse/Regions/War/Place_ClanConflict_4.Place_ClanConflict_4_C`; `/TheKnownUniverse/Regions/War/PlaceClanConflict`; `Place_ClanConflict`; `PlaceClanConflict`

### `/Plugins/TheKnownUniverse/Content/Regions/War/PlaceCustomConflict_5`

- tokens: `CampaignArc`
- `CampaignArc` examples: `CampaignArcEventData`; `CampaignArcEventList`; `Default__MWCampaignArcAsset`; `MWCampaignArcAsset`
