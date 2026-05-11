# TKU Compatibility Patch Operator Notes

## Current State

- Compat mod root:
  [TheKnownUniverseCompatPatch](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Mods/TheKnownUniverseCompatPatch>)
- Source-strip mod root:
  [TheKnownUniverseCompatSource](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Mods/TheKnownUniverseCompatSource>)
- Plugin-only mod root:
  [TheKnownUniverseCompatPluginOnly](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Mods/TheKnownUniverseCompatPluginOnly>)
- Tier C restore mod root:
  [TheKnownUniverseCompatTierCRestore](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Mods/TheKnownUniverseCompatTierCRestore>)
- Active profile:
  [modlist.profile-full-stack-with-tku-compat-20260506.json](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Mods/modlist.profile-full-stack-with-tku-compat-20260506.json>)
- Current `modlist.json` has already been set to that full-stack-plus-compat profile.

## Built Artifact

- Pak:
  [TheKnownUniverseCompatPatch.pak](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Mods/TheKnownUniverseCompatPatch/Paks/TheKnownUniverseCompatPatch.pak>)
- Content mirror pak:
  [MW5Mercs-zzzKnownUniverseCompatPatch.pak](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Content/Paks/MW5Mercs-zzzKnownUniverseCompatPatch.pak>)
- Stripped override live pak:
  [MW5Mercs-zKnownUniverseStarmap.pak](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Content/Paks/MW5Mercs-zKnownUniverseStarmap.pak>)
- Stripped override backup pak:
  [MW5Mercs-zKnownUniverseStarmap.original-20260506.pak](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Content/Paks/MW5Mercs-zKnownUniverseStarmap.original-20260506.pak>)
- Mod metadata:
  [mod.json](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Mods/TheKnownUniverseCompatPatch/mod.json>)
- Tier A manifest:
  [tier-a-manifest.json](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Mods/TheKnownUniverseCompatPatch/Resources/tier-a-manifest.json>)
- Tier B manifest:
  [tier-b-manifest.json](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Mods/TheKnownUniverseCompatPatch/Resources/tier-b-manifest.json>)

The current live build is a broad vanilla-root rescue. It exists both as a mod pak and as a late-loading content mirror pak so the rescue assets can still win if `Content/Paks` mount after mod-folder paks. It replaces current vanilla versions of `138` TKU root `/Game` assets that have current vanilla counterparts, including:

- `/Game/InnerSphereData/MW5_InnerSphereData`
- `/Game/InnerSphereData/Updated/EmployerInfoData`
- `/Game/InnerSphereData/Updated/SystemFactionChanges`
- `/Game/Levels/FrontEnd/StarMap`
- `/Game/Libraries/MW5_TOI_Functions`
- `/Game/UI/FrontEnd/StarMapPawn`
- `/Game/UI/FrontEnd/Starmap/StarMapActor`
- `/Game/UI/FrontEnd/Starmap/StarSystemBody`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/*`
- `/Game/Factions/*` where a current vanilla counterpart exists
- `/Game/Employers/*` where a current vanilla counterpart exists
- `/Game/Campaign/Personas/ProcMissionPersonas/*`
- `/Game/Campaign/CampaignArcs/BorderChanges/*`

The current source-strip experiment also adds:

- `TheKnownUniverseCompatSource`, a repacked TKU variant with the original plugin content preserved
- removal of three unmatched root employer assets from the TKU mod source:
  - `/Game/Employers/Unused/ClanDiamondShark`
  - `/Game/Employers/Unused/ClanNovaCat`
  - `/Game/Employers/Unused/ClanSteelViper`
- a stripped replacement for `MW5Mercs-zKnownUniverseStarmap.pak` that keeps only:
  - `/Game/InnerSphereData/MW5_InnerSphereData`
  - `/Game/Levels/FrontEnd/StarMap`

The current plugin-only experiment goes one step further:

- `TheKnownUniverseCompatPluginOnly` keeps `2425` plugin entries and `0` root `/Game` entries from the original TKU mod pak
- the live `MW5Mercs-zKnownUniverseStarmap.pak` now keeps only `CustomContent/*` entries
- the live override pak contains `36` `CustomContent` entries and `0` remaining `StarMap` or `MW5_InnerSphereData` conflict entries

The current Tier C restore experiment layers one more helper on top:

- `TheKnownUniverseCompatTierCRestore` with `defaultLoadOrder = 1001`
- restores the original TKU versions of:
  - `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
  - `/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`
  - `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015`
  - `/Game/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`
  - `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL`
  - `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF`

## Generated Profiles

- [modlist.profile-single-knownuniverse-compat-20260506.json](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Mods/modlist.profile-single-knownuniverse-compat-20260506.json>)
- [modlist.profile-named-local-with-compat-20260506.json](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Mods/modlist.profile-named-local-with-compat-20260506.json>)
- [modlist.profile-full-stack-with-tku-compat-20260506.json](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Mods/modlist.profile-full-stack-with-tku-compat-20260506.json>)

## Smoke Results

Timed smoke runs completed with no new crash directory created for:

- `TKU + compat patch` for 120 seconds
- named local companion mods + compat patch for 90 seconds
- full desired stack + compat patch for 90 seconds

These smoke runs confirm:

- the compat mod is discoverable and launchable
- startup with the patch does not immediately reproduce the known-red crash
- the full desired stack still boots with the patch enabled

These smoke runs do **not** prove:

- new career creation succeeds
- starmap browsing succeeds
- first travel or first contract generation succeeds

## Inventory And Build Reports

- [tku_compat_inventory_summary.md](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/reports/tku_compat_inventory_summary.md>)
- [tku_compat_asset_matrix.json](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/reports/tku_compat_asset_matrix.json>)
- [tku_compat_patch_tier_a.md](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/reports/tku_compat_patch_tier_a.md>)
- [tku_compat_patch_tier_b.md](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/reports/tku_compat_patch_tier_b.md>)
- [tku_compat_patch_vanilla_root_rescue.md](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/reports/tku_compat_patch_vanilla_root_rescue.md>)
- [tku_source_strip_variant.md](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/reports/tku_source_strip_variant.md>)
- [tku_plugin_only_variant.md](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/reports/tku_plugin_only_variant.md>)
- [tku_tier_c_restore.md](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/reports/tku_tier_c_restore.md>)

## Remaining Manual Validation

To close the roadmap completely, perform these in-game checks with the active full-stack-plus-compat profile:

1. Launch MW5.
2. Start a new career.
3. Open the starmap.
4. Perform at least one travel action.
5. Confirm the game does not create a new crash folder under `%LOCALAPPDATA%\MW5Mercs\Saved\Crashes`.

Tier A smoke boots passed, but the first interactive `TKU + compat patch` attempt soft-failed by hanging on the loading screen while still consuming CPU. Tier B was the first response to that result. After Tier B also hung, a content-level mirror pak was added to test whether `MW5Mercs-zKnownUniverseStarmap.pak` was beating the mod-folder compat patch on shared `StarMap` and `MW5_InnerSphereData` paths. A later interactive attempt still hung and also showed faction-selection display issues, so the next escalation became the broad vanilla-root rescue build. That still did not clear the load, which narrowed the remaining suspect set to `21` unmatched root assets. A source-strip variant then removed those unmatched roots from the source paks, but the next launch produced `CDO Constructor (MWInnerSphereData)` before the title screen. The plugin-only source variant plus a customcontent-only override pak cleared that startup blocker and reached title/new-career, but the first career-load crash then asserted `Could not find SuperStruct BaseStarMapBorderActor_C`. The current escalation restores only the original TKU border root assets and faction materials on top of the plugin-only setup.
