# TKU Evidence Start Border Compat Build - 2026-05-10

## Purpose

Create a narrow, reversible evidence build to test whether TKU's old career-start border chain is the remaining loading-stall trigger.

## Evidence Gate

- `TKUEvidenceStarmapCompat` changed the repeated post-loading `0x4C` fatal crash into a hard loading stall.
- The active mix still leaves TKU `Borders3015`, `AllStarMapBorderChanges`, and `BaseStarMapBorderActor` overriding current assets.
- Current editor evidence shows Davion career start conditions reference `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015`.
- String/package evidence shows TKU `Borders3015` redirects `BorderActor` to `/TheKnownUniverse/2864-01-01/StarMapBorderActor2864-01-01`.
- Package evidence shows that TKU 2864 border actor inherits through `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`.
- Previous runtime history already produced a `BaseStarMapBorderActor_C` superstruct failure when old border actors were mixed into current starmap assets.

## Build Contents

- Output mod: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUEvidenceStartBorderCompat`
- Output pak: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUEvidenceStartBorderCompat\Paks\TKUEvidenceStartBorderCompat.pak`
- Pak size: `9670`
- File count: `6`

## Included From Current Vanilla

- `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015.uasset`
- `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015.uexp`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor.uasset`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor.uexp`
- `/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges.uasset`
- `/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges.uexp`

## Expected Result

- If the old TKU start-border chain caused the hard stall, the profile `TheKnownUniverse` + `TKUEvidenceStarmapCompat` + this mod should progress past the Davion loading screen.
- If it still stalls without a crash, the next evidence target moves to root data tables, `MW5_TOI_Functions`, and faction/employer assets.
- If the old `0x4C` fatal returns, this border override changed mount interaction and should be disabled before further testing.

## Runtime Result

- Test profile: `TheKnownUniverse`, `TKUEvidenceStarmapCompat`, and `TKUEvidenceStartBorderCompat`.
- Result: crashed before reaching the Davion career result screen.
- Crash folder: `C:\Users\dogpe\AppData\Local\MW5Mercs\Saved\Crashes\UE4CC-Windows-087ADFB744721A7DFFAFE5A08D1F5254_0000`
- Error: `LowLevelFatalError [File:Unknown] [Line: 3146] Could not find SuperStruct BaseStarMapBorderActor_C to create StarMapActor_2570_C`
- Call-stack hash: `6B39ADBEAC4A925A9AA74C71905744CB2C6A6097`
- Seconds since start: `34`
- Immediate rollback performed: `TKUEvidenceStartBorderCompat` was disabled in `MW5Mercs\Mods\modlist.json`.

## Interpretation

- This build is failed and should not be used for further gameplay testing.
- The crash is not the earlier `0x4C` access violation and not the previous hard stall. It is the old border-superstruct failure family.
- `StarMapActor_2570` is a current vanilla HoloTable blueprint that hard-references `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`.
- Reasserting vanilla border assets as a pak override is not sufficient and can still expose the `BaseStarMapBorderActor_C` superstruct problem.
- The next fix should be editor-authored/reparented border reconstruction or removal of unsafe TKU root border overrides, not another direct cooked `BaseStarMapBorderActor` override.

## Known Limitation

- This intentionally restores current vanilla start-border behavior, so it is not expected to restore TKU's full historical territory overlays.

## Rollback

- `TKUEvidenceStartBorderCompat` is now disabled in `modlist.json`; it may also be removed by deleting only the new `MW5Mercs\Mods\TKUEvidenceStartBorderCompat` folder.
- Original `TheKnownUniverse.pak`, `TKUEvidenceStarmapCompat`, and `MW5Mercs-zKnownUniverseStarmap.pak` are not edited.
