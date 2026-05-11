# TKU Clean Install State - 2026-05-10

## Current conclusion

The restored Nexus install is structurally correct. The next test should not be another cooked-asset patch; it should be a clean run with the author-tested dependency family enabled, because the active profile was still TKU-only when the last local launch crashed.

## Source-backed install facts

- Nexus description says to extract `The Known Universe` to `MW5Mercs\Mods`, extract the `REQUIRED Override PAK` into `MW5Mercs\Content\Paks`, and enable the mod.
- Nexus files page says `REQUIRED Override PAK` contents go into `MechWarrior 5 Mercenaries/MW5Mercs/Content/Paks`, while `The Known Universe` goes into the mod folder.
- Nexus compatibility notes say TKU was made for and tested with the YetAnother family of mods and requires a mod adding mechs to the `Clan` faction for Clan faction behavior.
- MW5 Mod Editor Guide v2.3 says modified replacement assets belong in `ModOverride` when authored as a normal mod, and legacy/direct pak mods can be placed in the game's `MW5Mercs\Content\Paks` folder.
- Unreal Engine 4.27 packaging docs document `-fileopenlog` as a way to record file open order in a packaged game. That is useful for our next diagnostic launch if the game still fails without preserving a normal UE log.

## Verified local state

- Live TKU folder: `MW5Mercs\Mods\TheKnownUniverse`
- Live TKU `mod.json`: `displayName` `TheKnownUniverse`, build `38`, manifest count `141`.
- Live TKU pak SHA256: `0F23FC683DEBEC27D07FF6739137BA1E4069934082D5AFFF6B3F2161CC64C678`.
- Active required loose starmap pak: `MW5Mercs\Content\Paks\MW5Mercs-zKnownUniverseStarmap.pak`.
- Active required loose starmap pak SHA256: `DFAC2CA2E1DEDCD96709A95A778DA1BB55EB02BB87E9E62B7DFC8320DD9F1FCB`.
- The required override archive contains exactly `MW5Mercs-zKnownUniverseStarmap.pak`, size `9,882,904`, matching the active loose pak by size and hash.
- Active `.pak` files in `MW5Mercs\Content\Paks` are only the base game pak and `MW5Mercs-zKnownUniverseStarmap.pak`.
- Old Codex compatibility mods still exist on disk, but their `mod.json` files are disabled, so they should not appear as active mods.
- Active `modlist.json` before this report enabled only `TheKnownUniverse`; all other local/workshop mods were disabled.

## Pak content facts

- `MW5Mercs-zKnownUniverseStarmap.pak` mounts at `../../../MW5Mercs/Content/` and contains `/Game/InnerSphereData/MW5_InnerSphereData`, `/Game/Levels/FrontEnd/StarMap`, and `/Game/CustomContent/*` zone/conflict assets.
- `TheKnownUniverse.pak` mounts at `../../../MW5Mercs/` and contains root `/Game` overrides plus `/Plugins/TheKnownUniverse` content.
- Both paks contain StarMap and InnerSphereData root overrides, but StarMap hashes differ:
- Loose pak `Levels/FrontEnd/StarMap.umap` SHA1: `D11343E0AC66997CDA33801828F45A75D092835B`.
- TKU mod pak `Content/Levels/FrontEnd/StarMap.umap` SHA1: `E6F463F9E17A5A9FB55C37C641E1774C17379C1B`.
- Loose pak `InnerSphereData/MW5_InnerSphereData.uasset` SHA1: `DF6A9489D3F8BBA78157038FFE5DD68A3DFEC64A`.
- TKU mod pak `Content/InnerSphereData/MW5_InnerSphereData.uasset` SHA1: `9F8F44169A2822802D3491B5686D72026B15E8C6`.
- The matching `.uexp` hash for `MW5_InnerSphereData` suggests the package summary/name table changed between copies even when bulk exported data matches.

## Last crash evidence

- Clean TKU-only launch created crash folder `C:\Users\dogpe\AppData\Local\MW5Mercs\Saved\Crashes\UE4CC-Windows-F03C0C8D46F6123064FC5FA0CF64E181_0000`.
- Crash context: `Unhandled Exception: EXCEPTION_ACCESS_VIOLATION reading address 0x000000000000004c`.
- `SecondsSinceStart`: `61`.
- `EngineVersion`: `4.26.2-0+++UE4+Release-4.26`.
- `PCallStackHash`: `0039C4B8A7510FAC9074DFC881C752315D75F42F`.
- The crash folder did not include a full `MW5Mercs.log`; only `CrashContext.runtime-xml` and `UE4Minidump.dmp` were present.

## Next profile

Created `MW5Mercs\Mods\modlist.profile-tku-yaml-vonbiomes-clean-20260510.json`.

Enabled in that profile:

- `TheKnownUniverse`
- `ModOptions`
- `2677870592` MW5 Compatibility Pack
- `2549720490` Yet Another Mechlab
- `3311350044` Yet Another Weapon - Complete Edition
- `2734262706` Yet Another Equipment Collection
- `2752897895` Yet Another Special Variant
- `3669075119` YASV Complete Edition Patch
- `2815252243` YetAnotherClanMech
- `3047887746` Yet Another IS Mech
- `2808627355` vonBiomes

## What this test means

- If this profile reaches title and career, the previous crash was probably a TKU-only/local-profile issue, not a reason to patch TKU assets.
- If this profile crashes with the same `0x4c` signature before title, the next evidence target is actual pak/file-open order, not cooked asset editing.
- If this profile loads but the map is vanilla-width or lacks TKU overlays, inspect whether the loose `zKnownUniverseStarmap` StarMap is actually winning over the TKU mod pak StarMap.
- If the starmap works in this profile, layer user extras in batches: BetterMissionChoices/Coyote/QoL first, then BattleFXEnhanced and any local compatibility patch last.

## What not to do

- Do not rebuild or strip TKU paks until a clean intended-stack run fails and we have file-open/mount evidence.
- Do not delete original archives, original TKU files, or disabled experiment outputs.
- Do not re-enable old `TheKnownUniverseCompat*` mods.
- Do not treat a TKU-only crash as proof that the author-tested YAML/vonBiomes stack is broken.

## Cleanup performed after this report was created

Quarantine root: `codex_quarantine\tku_failed_compat_20260510`.

Moved out of `MW5Mercs\Mods`:

- `TheKnownUniverse.original-20260506`
- `TheKnownUniverseCompatPatch`
- `TheKnownUniverseCompatPluginOnly`
- `TheKnownUniverseCompatSource`
- `TheKnownUniverseCompatTierCRestore`
- `BattleFXPatch`
- `The Known Universe-786-1-0-1714008576.7z`
- Old `modlist.profile-*20260506.json` diagnostic profiles

Moved out of `MW5Mercs\Content\Paks`:

- `REQUIRED Override PAK-786-1-0-1713972397.7z`
- Disabled TKU starmap repacks and disabled compatibility paks

Post-cleanup active loader state:

- `MW5Mercs\Mods` still contains the restored live `TheKnownUniverse` folder and normal non-TKU local mods.
- `MW5Mercs\Content\Paks` contains only `MW5Mercs-WindowsNoEditor.pak` and `MW5Mercs-zKnownUniverseStarmap.pak`.
- Active `modlist.json` remains the clean TKU/YAML/vonBiomes profile.

Note: an empty placeholder folder named `codex_quarantine\tku_failed_compat_20260510\Mods\TheKnownUniverse.original-20260506` was left from the first sandbox-blocked move attempt. The real moved backup is `TheKnownUniverse.original-20260506.moved-20260510-103829`; both are outside MW5 loader paths.

## Clean intended-stack smoke result

The clean TKU/YAML/vonBiomes smoke run used `tools\Invoke-MW5TimedSmoke.ps1` with `-fileopenlog` and ran for 150 seconds.

- Profile: `modlist.profile-tku-yaml-vonbiomes-clean-20260510.json`
- Log: `C:\Users\dogpe\AppData\Local\MW5Mercs\Saved\Logs\MW5Mercs-smoke-20260510-103337.log`
- New crash directories: `0`

This does not prove the starmap overlay works; it only proves the intended-stack launch did not reproduce the earlier TKU-only crash within the smoke-test window.
