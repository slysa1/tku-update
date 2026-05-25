# Known Universe Recovery Report - 2026-05-11

## Summary

The current evidence points to an old cooked TKU root `/Game` starmap and border stack failing against the current installed MW5 content, not a simple missing dependency or metadata-only issue.

The strongest confirmed failure remains:

- `EXCEPTION_ACCESS_VIOLATION reading address 0x000000000000004c`
- repeated call stack hash `0039C4B8A7510FAC9074DFC881C752315D75F42F`
- repro previously isolated to `TheKnownUniverse.pak` being sufficient to crash a Davion career load

A second confirmed failure path is:

- `Could not find SuperStruct BaseStarMapBorderActor_C to create StarMapActor_2570_C`
- call stack hash `6B39ADBEAC4A925A9AA74C71905744CB2C6A6097`
- reproduced by cooked border/starmap evidence patches, which rules out blind cooked-pak substitution as a safe repair method

No game install, live mod folder, editor project, cooked asset, or pak file was edited in this run.

## Inventory

### Repo

- Project root: `D:\Downloads\OneDrive\Documents\code\tku-update`
- Top-level purpose: evidence, scripts, reports, path configuration, and the MW5 Mod Editor guide
- No source `.uproject`, `.uplugin`, `mod.json`, or Content folder exists inside the repo root. The source evidence currently comes from the live restored TKU paks and the external MW5 Mod Editor project.
- Key repo areas:
  - `tools\`: pak readers/builders, profile helpers, smoke launcher, report generators
  - `tools\tku_reference_audit\`: UE4/MW5 inspection and migration probes
  - `reports\tku_editor_first\`: current best diagnostics area
  - `MW5Mercs_Mod_Editor_Guide_(v2.3).pdf`: local MW5 editor guide

### Guide Evidence

The extracted guide at `reports\tku_editor_first\mw5_mod_editor_guide_v2_3_reference.md` confirms:

- Existing game assets should be copied through `Save To Mod` into ModOverride Content.
- New mod-owned assets should live under the mod content folder.
- Packaging should be performed through Manage Mod and tested as packaged output.
- Old v1 pak-only mods can still be read from `MW5Mercs\Content\Paks`, but they do not become normal in-game Mods-screen entries unless ported.

This supports an editor-first repair track for TKU starmap, DataTable, and Blueprint work.

### Linked Paths

| Path | Status | Treatment | Evidence |
| --- | --- | --- | --- |
| `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries` | exists/readable | read-only game install | current executable, pak, appmanifest evidence |
| `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods` | exists/readable | comparison/deployment target only | live local mods, active `modlist.json` |
| `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods_manual_install` | exists/readable, empty | comparison only | no current evidence |
| `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks` | exists/readable | read-only game pak area | base pak, TKU loose override, stray archive |
| `E:\SteamLibrary\steamapps\workshop\content\784080` | exists/readable | comparison-only live Workshop mods | 39 Workshop mod folders |
| `E:\Games\MechWarrior5Editor` | exists/readable | preferred asset authoring tool | no TKU compat mod target exists yet |
| `C:\Program Files\umodel` | exists/readable | supporting inspection | cooked asset evidence |
| `C:\Program Files\fmodel` | exists/readable | supporting inspection | cooked asset browsing/search |
| `C:\Program Files\Blender Foundation\Blender 5.1` | exists/readable | mesh/animation inspection if needed | not used in this run |
| `D:\Downloads\OneDrive\Documents\code\tku-update\tools\MW5AssetTool` | exists/readable | structured UAsset support | not used for mutation |
| `C:\Program Files\UAssetGUI` | exists/readable | supporting inspection | not used in this run |
| `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Binaries\Win64` | exists/readable | UE4SS/runtime evidence only | UE4SS v3.0.1 present |

### Game And DLC State

Local evidence:

- Steam appmanifest: `E:\SteamLibrary\steamapps\appmanifest_784080.acf`
- Steam app build id: `20534414`
- Live game modlist version: `1.1.380`
- Game target file reports UE `4.26.2`, build id `f925942a-0cae-4cd3-ac6f-57cf6e887b1d`
- Recent crash contexts also report `EngineVersion` `4.26.2-0+++UE4+Release-4.26`

Installed content evidence from `MW5Mercs-WindowsNoEditor.pak`:

| DLC folder | Pak entries |
| --- | ---: |
| `/Game/DLC1` | 22,719 |
| `/Game/DLC2` | 6,814 |
| `/Game/DLC3` | 4,289 |
| `/Game/DLC4` | 4,057 |
| `/Game/DLC5` | 2,659 |
| `/Game/DLC6` | 3,076 |
| `/Game/DLC7` | 29,982 |

The base pak contains current DLC1-DLC7 content, including DLC7 start-condition assets. Steam's manifest only exposes one DLC depot record locally, so the pak evidence proves content presence; it does not by itself prove storefront/license state.

### Live Mod State

Current live `modlist.json` enables 46 mods, including TKU, YAML family mods, `vonBiomes`, `Mod Options`, `MW5 Compatibility Pack`, `Coyotesmission`, `BattleFXEnhanced`, and several Workshop/local additions.

The restored live TKU folder:

- `TheKnownUniverse` build `38`
- `gameVersion`: `1.1.380`
- `manifest`: 141 entries
- `TheKnownUniverse.pak` SHA256: `0F23FC683DEBEC27D07FF6739137BA1E4069934082D5AFFF6B3F2161CC64C678`
- loose required override `MW5Mercs-zKnownUniverseStarmap.pak` SHA256: `DFAC2CA2E1DEDCD96709A95A778DA1BB55EB02BB87E9E62B7DFC8320DD9F1FCB`

Evidence mods still exist on disk under the local Mods folder, but they are not listed in the current live `modlist.json`.

`MW5Mercs\Content\Paks` currently contains:

- `MW5Mercs-WindowsNoEditor.pak`
- `MW5Mercs-zKnownUniverseStarmap.pak`
- `REQUIRED Override PAK-786-1-0-1713972397.7z`

The `.7z` archive is not a `.pak` and should not be mounted by MW5, but it is clutter in the game pak directory and should be moved out only during an explicit deployment cleanup step.

### Editor State

Current editor project:

- `E:\Games\MechWarrior5Editor\MW5Mercs\MW5Mercs.uproject`
- `E:\Games\MechWarrior5Editor\MW5Mercs\Mods` contains only `modlist.json`
- `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins` contains stock/editor plugins only
- No `TKUCompatEditorPatch` or other TKU compatibility authoring target exists

This blocks safe DataTable, Blueprint, and ModOverride asset mutation.

## Required Search Summary

Searches were run across the repo plus text/descriptors in the local and Workshop mod folders for the required terms, including `Known Universe`, `mod.json`, `.uplugin`, `.uproject`, `MW5`, `MechWarrior`, `DLC`, `DLC2` through `DLC7`, `missing`, `failed`, `crash`, `error`, `warning`, `blueprint`, `DataTable`, `PrimaryAsset`, `AssetRegistry`, `redirector`, `pak`, `load order`, `dependency`, `conflict`, `override`, `editor`, `cooked`, `packaging`, `GameVersion`, `EngineVersion`, `plugin`, `mount point`, `object path`, `class redirect`, and `deprecated`.

High-signal hits:

- Repo: 145 text files scanned. Prior reports heavily reference stale starmap Blueprints, current cluster assets, DataTables, crash signatures, and editor-first gates.
- Local mods: active descriptors show the live local mod set is currently updated to `gameVersion` `1.1.380`; TKU evidence patch folders still exist but are not active in `modlist.json`.
- Workshop mods: 152 text files scanned. Workshop descriptors and manifests reference current DLC folders, especially DLC7 content through YAML/vonBiomes-related mods.

## Hypothesis Tree

### 1. Stale TKU root `/Game` starmap stack is incompatible with current MW5

Rank: highest.

Evidence:

- TKU-only crash reproduced with `0x4c`.
- Loose required override alone did not crash in previous isolation.
- Replacing only selected starmap classes changed the failure mode.
- Border patch produced `BaseStarMapBorderActor_C` SuperStruct failure.
- Current vanilla `StarSystemBody` uses modern cluster functions and `MWClusterDataAsset`; original TKU build 38 does not contain current `/Game/Campaign/Clusters` assets.

Expected repair:

- Do not direct-restore old cooked `StarMapActor`, `StarSystemBody`, `StarMapPawn`, `BaseStarMapBorderActor`, or `StarMap.umap`.
- Recreate needed behavior through the MW5 Mod Editor using current-compatible parents and schemas.

### 2. Current DLC/cluster schema drift breaks TKU overlays and map behavior

Rank: high.

Evidence:

- Current base pak contains DLC1-DLC7 and many current cluster assets.
- Original TKU has no `/Game/Campaign/Clusters` assets and no `MWClusterDataAsset` strings.
- Stable plugin-only evidence floor loaded but retained vanilla-width bounds and incomplete/vanilla-like territory overlay.

Expected repair:

- Migrate TKU territory and cluster data into current `MWClusterDataAsset`/current DataTable schema rather than reviving old border-only cooked assets.

### 3. `MW5_InnerSphereData` and related tables need current-schema merge, not raw replacement

Rank: high.

Evidence:

- Current runtime table has 2,173 rows.
- Parsed TKU source has wider historical data and more systems.
- Existing candidate `tku_inner_sphere_merged_current_plus_tku_additions_20260510.csv` preserves current rows and adds TKU-only systems.

Expected repair:

- First editor mutation should be a mod-owned DataTable import using the merged current-plus-TKU candidate, followed by row and enum validation.

### 4. Loadout/deployment state can confuse diagnosis

Rank: moderate.

Evidence:

- Current live `modlist.json` has 46 active mods, not the earlier stable floor.
- Previous reports differ between TKU-only crash, intended-stack smoke pass, and plugin-only stable floor.
- Evidence mods remain on disk and should stay inactive unless deliberately testing one gate.

Expected repair:

- Use explicit named profiles for every runtime test.
- Never infer active state from folders alone; inspect `modlist.json`.

### 5. Metadata/version drift is not the crash cause, but it is a tooling defect

Rank: low as root cause, high as safe first fix.

Evidence:

- Live mod descriptors and live `modlist.json` use `1.1.380`.
- Repo build scripts still stamped future evidence builds as `1.13.378`.
- Incorrect metadata can make future test artifacts ambiguous even though it does not explain the `0x4c` crash.

Fix implemented in this run.

## Repair Plan

1. Keep all live game/editor/pak folders read-only until a specific deployment or editor-authoring gate is reached.
2. Fix repo-side metadata/tooling drift so future generated artifacts report the current local game version.
3. Create `TKUCompatEditorPatch` through the MW5 Mod Editor UI, not by manually scaffolding binary asset folders.
4. Inspect the created editor mod target and record file deltas.
5. Create a mod-owned copy of `/Game/InnerSphereData/MW5_InnerSphereData`.
6. Import `reports\tku_editor_first\tku_inner_sphere_merged_current_plus_tku_additions_20260510.csv`.
7. Validate DataTable row count and representative rows, including current rows and TKU-only additions.
8. Only after DataTable validation, build current-compatible starmap placement/bounds and cluster overlay assets in the editor.
9. Package through Manage Mod, inspect package output, and test explicit profiles:
   - vanilla plus `TKUCompatEditorPatch`
   - original TKU intended dependency family
   - current 46-mod stack only after smaller gates pass

Rollback:

- Repo changes are normal git diffs.
- Editor-created assets must be contained in `TKUCompatEditorPatch`.
- Live deployment tests must use named `modlist.profile-*.json` backups and never overwrite original TKU paks.

## Changes Made

Safe repo-only tooling fixes:

- `tools\tku_project_paths.py`
  - Added `GAME_VERSION` detection.
  - Detection prefers `TKU_GAME_VERSION`, then path config `game_version`, then live game `MW5Mercs\Mods\modlist.json`, then editor modlist, then fallback `1.1.380`.
- `tools\tku_compat_config.py`
  - `PATCH_GAME_VERSION` now uses detected `GAME_VERSION`.
  - Patch descriptions now interpolate the detected version instead of hard-coding `1.13.378`.
- Updated generated-patch/evidence scripts to stamp `GAME_VERSION`:
  - `tools\build_tku_tier_c_restore.py`
  - `tools\tku_reference_audit\build_tku_evidence_core_plugin_only.py`
  - `tools\tku_reference_audit\build_tku_evidence_bounds_pawn_patch.py`
  - `tools\tku_reference_audit\build_tku_evidence_current_pawn_bounds_patch.py`
  - `tools\tku_reference_audit\build_tku_evidence_starmap_class_patch.py`
  - `tools\tku_reference_audit\build_tku_evidence_start_border_patch.py`

## Validation

Completed:

- Read AGENTS.md.
- Read extracted MW5 Mod Editor Guide v2.3 reference.
- Mapped repo layout and linked paths.
- Parsed current game appmanifest, live modlist, editor project state, live mod descriptors, Workshop descriptors, pak index, and crash contexts.
- Confirmed base pak contains DLC1-DLC7 content.
- Confirmed no editor TKU compat mod target exists.
- Confirmed detected repo game version resolves to `1.1.380`.
- Confirmed patch descriptions now emit `Local MW5 v1.1.380...`.
- AST-parsed all edited Python files successfully.
- Imported the edited generated-patch/evidence modules successfully with `PYTHONDONTWRITEBYTECODE` behavior via `python -B`.
- `git diff --check` reported no whitespace errors.

Could not complete:

- `python -m compileall tools` failed because existing `__pycache__` files deny overwrite access. AST parsing was used instead because it does not mutate cache files.
- No MW5 runtime smoke was launched in this run. The current live modlist has 46 active mods, and a smoke run would mutate live `Engine.ini` temporarily and launch the game; that should be done with an explicit named profile after the next asset-authoring gate.
- No MW5 Mod Editor asset mutation was attempted because the required editor mod target does not exist.

## Remaining Blockers

1. `TKUCompatEditorPatch` has not been created in the MW5 Mod Editor.
2. The first safe DataTable import has not been performed.
3. Current-compatible cluster/overlay assets have not been generated.
4. Full all-DLC in-game validation is still pending.
5. The live game pak folder contains a `.7z` archive; harmless for pak mounting, but it should be moved out during a controlled deployment cleanup.
6. Current live modlist has 46 active mods, so any crash reproduction must start from a named profile to avoid mixing user stack noise into core TKU evidence.

## 2026-05-11 Continuation

Follow-up inspection confirmed the editor target is still absent:

- `E:\Games\MechWarrior5Editor\MW5Mercs\Mods` contains only `modlist.json`.
- `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins` contains only stock/editor plugins.
- The generated editor Python stub exposes `MWModUtils.create_mod_entry`, `set_active_mod`, and `save_mod_info_to_file`, but no direct safe Create Mod / Save To Mod authoring function. The prior `create_mod_entry` probe returned an in-memory entry and created no folders or plugin descriptor.
- The editor `Content\ModTemplates\BaseTemplate` contains only starter `Config\Input`, `Config\Tags`, and `Resources\Icon128.png` files. It does not contain a complete `.uplugin`, mod descriptor, or on-disk scaffold sufficient to safely reproduce the MW5 editor's Create Mod behavior by hand.

Safe next-step tooling added:

- `tools\Invoke-TKUInnerSphereImport.ps1`
- `tools\tku_reference_audit\ue4_import_tku_inner_sphere_datatable.py`

These tools are intentionally gated. They default to a dry run, require an editor-created `TKUCompatEditorPatch` target, require an explicit target DataTable asset path before writes, validate the merged CSV row count (`3974`) and sample rows, validate `InnerSphereMapData`, and refuse same-path `/Game/InnerSphereData/MW5_InnerSphereData` writes unless root override mode is explicitly enabled after the MW5 editor `Save To Mod` workflow.

Because no editor target exists yet, the import tool was prepared but not launched against the editor project. A local non-Unreal dry run wrote `reports\tku_editor_first\ue4_inner_sphere_import_20260511.md` and confirmed the CSV is readable as UTF-16 with `3974` rows and required samples `0`, `1`, `2`, `3501`, `4001`, `4110`, and `7921`; it correctly refused to proceed because the Unreal `unreal` module was unavailable, `TKUCompatEditorPatch` was absent, and no target asset path was supplied.

The MW5 Mod Editor GUI was launched as `UE4Editor.exe` process `40356` at local time `2026-05-11 18:28`. The editor log reached startup completion and asset discovery completion, but the process still exposed no usable top-level window handle to Codex. Repeated filesystem checks after launch still found no `TKUCompatEditorPatch` target, so the next action remains a human UI click in the visible editor.

After the human Create Mod step, the editor created:

- `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins\TKUCompatEditorPatch\TKUCompatEditorPatch.uplugin`
- `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins\TKUCompatEditorPatch\Content`
- `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins\TKUCompatEditorPatch\ModOverride`
- `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins\TKUCompatEditorPatch\Config`
- `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins\TKUCompatEditorPatch\Resources`

The `.uplugin` has `IsMod: true`, `CanContainContent: true`, `FriendlyName: TKUCompatEditorPatch`, and the intended description/author. The next human UI action is to ensure `TKUCompatEditorPatch` is the active mod, then open `/Game/InnerSphereData/MW5_InnerSphereData` and press `Save To Mod`.

The human `Save To Mod` step created `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins\TKUCompatEditorPatch\ModOverride\InnerSphereData\MW5_InnerSphereData.uasset`. The editor log confirmed the object path `/ModOverride/TKUCompatEditorPatch/InnerSphereData/MW5_InnerSphereData.MW5_InnerSphereData`. The save produced a handled DataValidation ensure from `EditorValidator_Localization` not setting pass/fail state; the package still saved and reopened. This is recorded as an editor validation quirk to watch, not a confirmed TKU content failure.

Before import, the saved mod override DataTable was copied to `reports\tku_editor_first\backups\TKUCompatEditorPatch_pre_import_20260511\MW5_InnerSphereData.uasset`; SHA256 matched the editor asset at `102000614114FC1EC946C7877BB3CE59A7C36E3638D270BDA46714F9F7BA33FA`.

The guarded commandlet import then loaded `/Game/InnerSphereData/MW5_InnerSphereData` with `TKUCompatEditorPatch` active, and Unreal resolved it to `/ModOverride/TKUCompatEditorPatch/InnerSphereData/MW5_InnerSphereData.MW5_InnerSphereData`. The dry run reported no safety failures:

- Target class: `DataTable`
- Row struct: `/Script/MechWarrior.InnerSphereMapData`
- Pre-import row count: `2173`
- Pre-import missing TKU sample rows: `4001`, `4110`, `7921`

The apply run imported `reports\tku_editor_first\tku_inner_sphere_merged_current_plus_tku_additions_20260510.csv` and saved the mod-owned asset:

- Applied: `true`
- Saved: `true`
- Post-import row count: `3974`
- Sample rows present after import: `0`, `1`, `2`, `3501`, `4001`, `4110`, `7921`
- Post-import SHA256: `FE8F7DB2F948AAB64503155B160EC063D0166511EF65C702775E657E684F155E`
- Preserved apply report: `reports\tku_editor_first\ue4_inner_sphere_import_apply_20260511.md`

The human `Save To Mod` step also created the StarMap map override:

- `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins\TKUCompatEditorPatch\ModOverride\Levels\FrontEnd\StarMap.umap`
- Size: `2691871`
- Last write time: `2026-05-11 19:06:37` local
- SHA256: `5B822218AAD3DDD33C5D595A4A26AE6F5E816A89B7BCDE1E43714E5A8864521C`

This gives the repair track a mod-owned current StarMap asset to modify instead of restoring the old cooked TKU map. The editor process was still running at the time this evidence was captured, so no commandlet was launched against the map yet.

Safe next-step tooling added:

- `tools\Invoke-TKUStarMapActorPatch.ps1`
- `tools\tku_reference_audit\ue4_patch_tku_starmap_level.py`

The StarMap actor patch gate is intentionally dry-run first. It validates the active DataTable resolves through `/ModOverride/TKUCompatEditorPatch/`, validates the saved StarMap resolves through `/ModOverride/TKUCompatEditorPatch/`, validates the merged CSV row count is `3974`, and refuses to write unless there are no safety failures and `-Apply` is explicitly supplied. Local syntax validation passed with `python -B` so no `__pycache__` write was required.

The first apply attempt using `EditorLevelLibrary.spawn_actor_from_class` crashed the commandlet in `EditorScriptingUtilities` before the report was updated. The StarMap file hash remained unchanged, and a pre-patch backup existed at `reports\tku_editor_first\backups\TKUCompatEditorPatch_starmap_pre_actor_patch_20260511\StarMap.umap` with SHA256 `5B822218AAD3DDD33C5D595A4A26AE6F5E816A89B7BCDE1E43714E5A8864521C`.

Follow-up probes established the safe authoring path:

- `spawn_actor_from_object` with the current `/Game/UI/FrontEnd/Starmap/StarSystemBody` Blueprint asset does not crash.
- Directly setting `star_system_id` fails because `MWStarSystemBody.StarSystemId` is read-only.
- Calling `setup_info(StarSystemInfo)` sets the read-only values correctly. The no-save probe spawned ID `4001`, verified `star_system_id_after_setup: 4001`, `desired_zoom_level_after_setup: 0`, destroyed the probe actor, and left the map hash unchanged.

The final guarded apply then succeeded:

- Apply requested: `true`
- Spawn method: `object`
- Safety failures: none
- Missing before: `1801`
- Spawned: `1801`
- Saved: `true`
- StarSystemBody count before: `2172`
- StarSystemBody count after: `3973`
- Desired body count: `3973`
- Missing desired IDs after: `0`
- Duplicate star system IDs after: none
- Extra actor IDs after: `0`
- Placement errors after: `0`
- Base `Content\Levels\FrontEnd\StarMap.umap` unchanged: `true`
- Target StarMap SHA256 before: `5B822218AAD3DDD33C5D595A4A26AE6F5E816A89B7BCDE1E43714E5A8864521C`
- Target StarMap SHA256 after: `A83271BF3B67CEE20208E6F1FBB8F364EA768BEE406A6756A36D1A0572692181`
- Target StarMap size after: `4399244`
- Target StarMap last write time: `2026-05-11 19:30:41` local

## Next Gate

After the editor was closed, a fresh non-mutating commandlet validation was run against the saved assets:

- Command: `.\tools\Invoke-TKUStarMapActorPatch.ps1 -SpawnMethod object`
- Unreal result: `Success - 0 error(s), 31 warning(s)`
- Warnings were the same stock editor missing-effect references observed in earlier commandlets, not TKUCompatEditorPatch-specific load failures.
- Active DataTable object path: `/ModOverride/TKUCompatEditorPatch/InnerSphereData/MW5_InnerSphereData.MW5_InnerSphereData`
- Active DataTable row count: `3974`
- Active StarMap world path: `/ModOverride/TKUCompatEditorPatch/Levels/FrontEnd/StarMap.StarMap`
- StarSystemBody count: `3973`
- Desired body count: `3973`
- Missing desired IDs: `0`
- Duplicate star system IDs: none
- Extra actor IDs: `0`
- Placement errors: `0`
- Base `Content\Levels\FrontEnd\StarMap.umap` unchanged: `true`
- StarMap override SHA256: `A83271BF3B67CEE20208E6F1FBB8F364EA768BEE406A6756A36D1A0572692181`
- InnerSphereData override SHA256: `FE8F7DB2F948AAB64503155B160EC063D0166511EF65C702775E657E684F155E`

The editor-authored compatibility patch currently contains exactly the active mod descriptor/template files plus two authored override assets:

- `ModOverride\InnerSphereData\MW5_InnerSphereData.uasset`
- `ModOverride\Levels\FrontEnd\StarMap.umap`

The next highest-value validation gate is now to package `TKUCompatEditorPatch` through the MW5 Mod Editor `Manage Mod` UI and inspect/test the packaged output. This is intentionally before any new `StarMapPawn` mutation because earlier cooked pawn substitutions broke the starmap button into first-person hangar view. Bounds and cluster/territory overlays remain separate follow-up repair tracks after the current editor-authored stack proves it can package and load.

Manual package instructions:

1. Open the MW5 Mod Editor.
2. Confirm `TKUCompatEditorPatch` is selected in the `Active Mod` selector.
3. Click `Manage Mod`.
4. Keep version `1.0` for this first package unless the editor requires a change.
5. Keep the default load order unless the Manage Mod screen requires an explicit value.
6. Click `Package Mod`.
7. When asked for the output folder, use the default editor output folder: `E:\Games\MechWarrior5Editor\MW5Mercs\Mods`.
8. If the editor asks whether to open the packaged folder, either choice is fine.
9. Close the editor yourself when packaging completes, then tell Codex `packaged`.

After packaging, inspect the package folder, `mod.json`, pak contents, mount paths, and package logs before copying anything into the live game mod folder.

Package inspection tooling added:

- `tools\Inspect-TKUPackagedMod.ps1`
- `tools\tku_reference_audit\inspect_tku_packaged_mod.py`

The Python syntax check passed. A pre-package read-only scan wrote `reports\tku_editor_first\tku_packaged_mod_inspection_20260511.md` and correctly failed only because `E:\Games\MechWarrior5Editor\MW5Mercs\Mods\TKUCompatEditorPatch` does not exist yet. Once the editor creates that folder, rerun `.\tools\Inspect-TKUPackagedMod.ps1` to validate `mod.json`, pak presence, hashes, and the expected `ModOverride\InnerSphereData\MW5_InnerSphereData` plus `ModOverride\Levels\FrontEnd\StarMap` package entries.

The human packaging step completed and created `E:\Games\MechWarrior5Editor\MW5Mercs\Mods\TKUCompatEditorPatch`. The corrected read-only package inspection passed:

- Packaged folder exists: `true`
- File count: `3`
- Pak count: `1`
- `mod.json` SHA256: `915029771DF2F0AD587F0A14D035FF6E1A1B93D13C65AF718388297455EC4CA9`
- `Paks\TKUCompatEditorPatch.pak` SHA256: `3214395F1E9EDB88957903C88CE364A48AD634902A26EF461284E3D27BAAED0D`
- `Resources\Icon128.png` SHA256: `EC157F56F486E5A68FD4B27DF6C88FECDB1B8F9BFFF18AA5EF10A21BCA6A4C5E`
- `UnrealPak -List` returned `0`
- Expected cooked entries present:
  - `Content/InnerSphereData/MW5_InnerSphereData.uasset`
  - `Content/InnerSphereData/MW5_InnerSphereData.uexp`
  - `Content/Levels/FrontEnd/StarMap.umap`
  - `Content/Levels/FrontEnd/StarMap.uexp`

The packaged `mod.json` manifest lists `/Game/InnerSphereData/MW5_InnerSphereData.uasset` and `/Game/Levels/FrontEnd/StarMap.umap`. The package generated `gameVersion: 1.13.64` and `defaultLoadOrder: 0`; for live testing, the deployed copy was adjusted to the installed live modlist version and a later load order.

Live isolated test deployment was applied through `tools\Deploy-TKUCompatTestProfile.ps1 -Apply`:

- Source package: `E:\Games\MechWarrior5Editor\MW5Mercs\Mods\TKUCompatEditorPatch`
- Live destination: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch`
- Deployed `mod.json` `defaultLoadOrder`: `95`
- Deployed `mod.json` `gameVersion`: `1.1.380`
- Deployed `mod.json` SHA256: `469D22A8FD9A94F8CEA1045B147432272710F8FE155BA739366F0332C76305EA`
- Deployed pak SHA256: `3214395F1E9EDB88957903C88CE364A48AD634902A26EF461284E3D27BAAED0D`
- Original live modlist backup: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260512-070216.json`
- Repo copy of backup: `reports\tku_editor_first\modlist.backup-before-TKUCompatEditorPatch-20260512-070216.json`
- Active live `modlist.json` now enables only:
  - `TKUEvidenceCorePluginOnly`
  - `TKUCompatEditorPatch`

This is intentionally an isolated runtime gate, not the final full-mod-stack deployment. The old live `TheKnownUniverse` folder is untouched and disabled for this first test because its manifest still includes stale `/Game` root substitutions for `StarMapPawn`, `StarMapActor`, `StarSystemBody`, border actors, faction materials, and old data assets. If the isolated editor-authored stack loads, the next repair step is to merge or replace unsafe original TKU root overrides with current-compatible editor-authored equivalents.

Runtime smoke checklist:

1. Launch MW5.
2. Confirm the Mods screen shows only `TKU Evidence Core Plugin Only` and `TKUCompatEditorPatch` enabled.
3. Apply/restart if the game asks.
4. Start or load a Career.
5. Open the Starmap.
6. Check whether the game reaches the starmap without crash or hang.
7. Check whether clan/TKU far systems exist on the map.
8. Record whether pan/zoom reaches the full expanded region or remains constrained.
9. Exit after the result is clear so logs can be inspected.

Do not re-enable the original `TheKnownUniverse` or the failed evidence pawn/border patches until this isolated gate has been logged.

Runtime smoke result reported by the human tester:

- MW5 launched with the isolated test profile.
- Game loaded successfully.
- Starmap opened successfully.
- No new crash folder appeared under `%LOCALAPPDATA%\MW5Mercs\Saved\Crashes`; newest crash folders remain from `2026-05-10`.
- The visible starmap still appeared vanilla, including vanilla faction overlay.
- TKU-added stars were not visible to the tester.

Interpretation:

- The current editor-authored package is runtime-safe in the isolated baseline stack.
- It is not yet feature-complete.
- The result does not by itself prove the `MW5_InnerSphereData` and `StarMap.umap` package failed to mount, because the currently active `StarMapPawn` still has vanilla-scale camera defaults:
  - `pan_bounds_horizontal`: `5500`
  - `pan_bounds_vertical`: `4500`
  - `zoom_distance_list`: `[400,550,700,1400,1600,1800,3500]`
  - `zoom_level_thresholds`: `[2000,1000]`
- The merged TKU star extents require roughly `15664` half-span in X and `15259` half-span in Y. The next safe repair gate is therefore an editor-authored `StarMapPawn` override with pan bounds and zoom distances expanded from the current Blueprint, not a direct cooked pawn substitution.

New guarded tooling:

- `tools\Invoke-TKUStarMapPawnBoundsPatch.ps1`
- `tools\tku_reference_audit\ue4_patch_tku_starmap_pawn_bounds.py`

The dry run was successful as a gate and refused to mutate anything because `/Game/UI/FrontEnd/StarMapPawn` has not yet been saved into `TKUCompatEditorPatch`:

- Target mod-owned file missing: `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins\TKUCompatEditorPatch\ModOverride\UI\FrontEnd\StarMapPawn.uasset`
- Active object still resolves to `/Game/UI/FrontEnd/StarMapPawn.StarMapPawn`
- Active class still resolves to `/Game/UI/FrontEnd/StarMapPawn.StarMapPawn_C`
- Active CDO still resolves to `/Game/UI/FrontEnd/StarMapPawn.Default__StarMapPawn_C`
- Base asset unchanged: `true`

Next manual editor step:

1. Open MW5 Mod Editor.
2. Ensure `TKUCompatEditorPatch` is the Active Mod.
3. Open `/Game/UI/FrontEnd/StarMapPawn`.
4. Click `Save To Mod`.
5. Save if prompted.
6. Close the editor yourself and report `pawn saved`.

After that, run `.\tools\Invoke-TKUStarMapPawnBoundsPatch.ps1 -Apply`, then repackage, redeploy, and retest. This is still expected to leave faction/territory overlay vanilla until the separate current-schema `MWClusterDataAsset` migration is done.

## Version Target Correction - 2026-05-12

The current repair target is MW5: Mercenaries DLC7 on the live `1.13.x` line, with special attention to Steam/GOG `1.13.378`.

Evidence:

- Local Steam manifest `E:\SteamLibrary\steamapps\appmanifest_784080.acf` reports build ID `20534414`.
- SteamDB lists app `784080` public branch build ID `20534414`, built `2025-10-24` and updated `2025-10-30`: <https://steamdb.info/app/784080/depots/>
- GOGDB lists the current GOG offline installer and patch target as version `1.13.378`: <https://www.gogdb.org/product/2147483045>
- The older live `modlist.json` value `1.1.380` was a stale local mod metadata artifact, not the intended compatibility target.
- The MW5 Mod Editor-generated `gameVersion: 1.13.64` appears to be editor/mod-tool metadata and should not override the live compatibility target for deployment.

Changes made after this correction:

- `config\tku_paths.local.json` and `config\tku_paths.example.json` now explicitly set `game_version` to `1.13.378`.
- `tools\tku_project_paths.py` now falls back to `1.13.378` instead of `1.1.380`.
- `tools\Deploy-TKUCompatTestProfile.ps1` now defaults deployment metadata to `1.13.378` instead of seeding from the stale `1.1.380` value.
- Added `tools\Set-TKUCompatVersionMetadata.ps1` to correct packaged/deployed mod metadata with backups and reports.
- Applied the metadata correction to:
  - `E:\Games\MechWarrior5Editor\MW5Mercs\Mods\TKUCompatEditorPatch\mod.json`
  - `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch\mod.json`
  - `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.json`
- Metadata correction report: `reports\tku_editor_first\tku_version_metadata_20260512-072817.md`

Current live deployed metadata after correction:

- `TKUCompatEditorPatch\mod.json` `gameVersion`: `1.13.378`
- `TKUCompatEditorPatch\mod.json` description: `Editor-authored compatibility patch for Known Universe on MW5 1.13.x / DLC7 (Steam/GOG 1.13.378)`
- Active live `modlist.json` `gameVersion`: `1.13.378`
- Active isolated test stack remains:
  - `TKUEvidenceCorePluginOnly`
  - `TKUCompatEditorPatch`

The next asset repair step is unchanged: save `/Game/UI/FrontEnd/StarMapPawn` into `TKUCompatEditorPatch`, then apply the guarded bounds/zoom patch from `tools\Invoke-TKUStarMapPawnBoundsPatch.ps1`.

## StarMapPawn Bounds Repair - 2026-05-12

The human operator saved `/Game/UI/FrontEnd/StarMapPawn` into `TKUCompatEditorPatch`, creating the mod-owned override:

- `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins\TKUCompatEditorPatch\ModOverride\UI\FrontEnd\StarMapPawn.uasset`

The guarded pawn bounds commandlet was run first as a dry run, then with `-Apply`.

Dry-run evidence:

- Active object resolved to `/ModOverride/TKUCompatEditorPatch/UI/FrontEnd/StarMapPawn.StarMapPawn`
- Active class resolved to `/ModOverride/TKUCompatEditorPatch/UI/FrontEnd/StarMapPawn.StarMapPawn_C`
- CDO resolved to `/ModOverride/TKUCompatEditorPatch/UI/FrontEnd/StarMapPawn.Default__StarMapPawn_C`
- Vanilla defaults before patch:
  - `pan_bounds_horizontal`: `5500`
  - `pan_bounds_vertical`: `4500`
  - `zoom_distance_list`: `[400,550,700,1400,1600,1800,3500]`
  - `zoom_level_thresholds`: `[2000,1000]`
- Merged TKU coordinate extents require approximately `15664` half-span in X and `15259` half-span in Y.
- Safety failures: none

Apply result:

- Command: `.\tools\Invoke-TKUStarMapPawnBoundsPatch.ps1 -Apply -SpawnMethod object`
- Unreal result: `Success - 0 error(s), 31 warning(s)`
- Warnings were the same stock editor missing-effect references seen in prior commandlets.
- New mod-owned pawn defaults:
  - `pan_bounds_horizontal`: `17500`
  - `pan_bounds_vertical`: `17500`
  - `zoom_distance_list`: `[300,600,900,1300,1800,2200,2800,3500,5000,7500,9000]`
  - `zoom_level_thresholds`: `[3500,1000]`
- Backup: `reports\tku_editor_first\backups\TKUCompatEditorPatch_starmap_pawn_pre_bounds_patch_20260512\StarMapPawn.uasset`
- Mod-owned pawn SHA256 before: `2C2121628B6B968B158C2A87CDF2E50E1541761B82103A0CE0B2BDA15D4097B9`
- Mod-owned pawn SHA256 after: `3A4EC0F8DE697928057F24985E9715B6EEFA199FB56776E0C89C34212FDF1FF0`
- Base editor asset unchanged: `true`

The patch was then repackaged by the human operator through the MW5 Mod Editor. Package inspection passed:

- Package folder: `E:\Games\MechWarrior5Editor\MW5Mercs\Mods\TKUCompatEditorPatch`
- Pak SHA256: `43F98D4D171E1F189D96E3D5D7DA5BF6F2355C603381ED3E05AD5649811DA30D`
- `UnrealPak -List` expected entries present:
  - `Content/InnerSphereData/MW5_InnerSphereData.uasset`
  - `Content/InnerSphereData/MW5_InnerSphereData.uexp`
  - `Content/Levels/FrontEnd/StarMap.umap`
  - `Content/Levels/FrontEnd/StarMap.uexp`
  - `Content/UI/FrontEnd/StarMapPawn.uasset`
  - `Content/UI/FrontEnd/StarMapPawn.uexp`
- Package inspection report: `reports\tku_editor_first\tku_packaged_mod_inspection_20260511.md`

The editor regenerated packaged `mod.json` with `gameVersion: 1.13.64` and the old `1.1.380` description. This was corrected again with `tools\Set-TKUCompatVersionMetadata.ps1`.

Live isolated redeploy was then applied:

- Command: `.\tools\Deploy-TKUCompatTestProfile.ps1 -Apply -ReplaceExisting`
- Deployment report: `reports\tku_editor_first\tkucompat_live_test_deploy_20260512-074753.md`
- Existing live deployed patch backup: `reports\tku_editor_first\backups\live_mod_before_deploy_TKUCompatEditorPatch_20260512-074753`
- Live modlist backup: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260512-074753.json`
- Live deployed pak SHA256: `43F98D4D171E1F189D96E3D5D7DA5BF6F2355C603381ED3E05AD5649811DA30D`
- Live deployed `mod.json`:
  - `gameVersion`: `1.13.378`
  - `defaultLoadOrder`: `95`
  - manifest includes `MW5_InnerSphereData`, `StarMapPawn`, and `StarMap`
- Active isolated test profile remains:
  - `TKUEvidenceCorePluginOnly`
  - `TKUCompatEditorPatch`

Next runtime validation:

1. Launch MW5.
2. Confirm only `TKUEvidenceCorePluginOnly` and `TKUCompatEditorPatch` are enabled.
3. Load or start a Career.
4. Open the starmap.
5. Check whether TKU-added stars are visible or reachable with the expanded pan/zoom range.
6. Check whether the starmap still looks vanilla in faction/territory overlay. A vanilla overlay is expected until the separate current-schema `MWClusterDataAsset` migration is implemented.
7. Exit after the result is clear so logs and crash folders can be inspected.

## Runtime Result After Pawn Repair - 2026-05-12

Human runtime result with build `2`:

- MW5 loaded successfully.
- Starmap opened successfully.
- The user could pan farther than before, confirming the packaged `StarMapPawn` override is mounted and active at runtime.
- Faction overlay remained vanilla.
- Base starmap star population remained effectively vanilla/incomplete:
  - many periphery stars are missing around the cluster;
  - Clans, Taurians, Rim Worlds Republic, and Magistracy of Canopus cannot be represented without their star systems;
  - the core appears to have fewer stars than remembered from TKU.

Interpretation:

- The mod pak mounts and at least `/Game/UI/FrontEnd/StarMapPawn` overrides successfully.
- The remaining failure is not a simple package/load-order failure.
- Either `/Game/Levels/FrontEnd/StarMap` and/or `/Game/InnerSphereData/MW5_InnerSphereData` is not the runtime source that controls visible star population in the tested career starmap, or the current runtime starmap path filters/regenerates bodies from another current data source after level load.
- A save-cache possibility remains: an existing career may preserve or derive starmap state differently from a new career after data changes.

UE4SS runtime instrumentation attempt:

- Temporary probe installed: `tools\tku_reference_audit\ue4ss_tku_runtime_probe.lua`
- Installer report: `reports\tku_editor_first\ue4ss_runtime_probe_install_20260512-080011.md`
- UE4SS failed before Lua mods could start; no `ue4ss_tku_runtime_probe_*.txt` files were written.
- Log evidence: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Binaries\Win64\UE4SS.log` repeatedly reports failure to find `FText::FText(FString&&)` and ends with `Fatal Error: PS scan timed out`.
- Setting `EngineVersionOverride` to `4.27` did not resolve the missing FText signature.
- Probe and settings were restored/disabled:
  - restore report: `reports\tku_editor_first\ue4ss_probe_restore_20260512-081158.md`
  - `TKURuntimeProbe : 0`
  - `EngineVersionOverride` fields blank again

Next clean discriminator:

1. Run one new-career starmap test using the same isolated live mod profile.
2. If a new career still shows vanilla/incomplete stars, treat this as confirmed runtime data path mismatch rather than save-cache.
3. Inspect current MW5 editor references to identify the actual star population path used by the career starmap in DLC7 `1.13.378`, especially references to `StarMap`, `StarSystemSceneManager`, `StarMapActor`, `MW5_InnerSphereData`, current runtime CSV/data assets, and cluster assets.

## New-Career Result And Content-Pak Mirror Test - 2026-05-12

The new-career discriminator was run by the human tester after the pawn repair. Result:

- A new career still looked the same as the previous test.
- The user could still pan farther than the vanilla camera bounds.
- The missing periphery/clan-area stars remained missing.

Interpretation:

- Save-game starmap caching is no longer the leading explanation.
- The patched `StarMapPawn` is still proven active at runtime.
- The patched `StarMap.umap` and/or `MW5_InnerSphereData` are either being beaten by another root `/Game` package, or the current runtime starmap path is not using those authored root assets as the visible-star source.

Content-pak evidence gathered next:

- Active `MW5Mercs\Content\Paks` contained:
  - `MW5Mercs-WindowsNoEditor.pak`
  - `MW5Mercs-zKnownUniverseStarmap.pak`
  - `REQUIRED Override PAK-786-1-0-1713972397.7z`
- `MW5Mercs-zKnownUniverseStarmap.pak` is outside the in-game modlist and still contains root replacements for:
  - `/Game/InnerSphereData/MW5_InnerSphereData`
  - `/Game/Levels/FrontEnd/StarMap`
- That makes it a direct root-path conflict with the editor-authored `TKUCompatEditorPatch` package for the two assets still failing at runtime.

New tooling added:

- `tools\tku_reference_audit\build_tku_content_mirror.py`
- `tools\Build-TKUCompatContentMirror.ps1`

The tool stages a separate late-loading content mirror pak from the current editor-authored package without modifying the original game pak or original TKU loose override pak.

Dry-run/staging report:

- `reports\tku_editor_first\tku_content_mirror_20260512-082143.md`
- Staged mirror pak: `reports\tku_editor_first\staging\MW5Mercs-zzzzTKUCompatEditorPatch.pak`
- Staged mirror SHA256: `34A15D270F1041CEB315A26940DF026E603F2E04E44B6D2DE07BA2FDCF837C7D`
- Staged mirror contains all six expected files:
  - `/Game/InnerSphereData/MW5_InnerSphereData.uasset`
  - `/Game/InnerSphereData/MW5_InnerSphereData.uexp`
  - `/Game/Levels/FrontEnd/StarMap.umap`
  - `/Game/Levels/FrontEnd/StarMap.uexp`
  - `/Game/UI/FrontEnd/StarMapPawn.uasset`
  - `/Game/UI/FrontEnd/StarMapPawn.uexp`

Live mirror deployment:

- Command: `.\tools\Build-TKUCompatContentMirror.ps1 -Apply`
- Deployment report: `reports\tku_editor_first\tku_content_mirror_20260512-082155.md`
- Live mirror pak: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak`
- Live mirror SHA256: `34A15D270F1041CEB315A26940DF026E603F2E04E44B6D2DE07BA2FDCF837C7D`
- Original `MW5Mercs-zKnownUniverseStarmap.pak` was not overwritten or edited.
- Rollback for this test is to remove only `MW5Mercs-zzzzTKUCompatEditorPatch.pak`.

Runtime mirror test now in progress:

1. Launch MW5.
2. Keep the isolated mod profile:
   - `TKUEvidenceCorePluginOnly`
   - `TKUCompatEditorPatch`
3. Start a new career or load the fresh test career.
4. Open the starmap.
5. Check whether TKU-added periphery/clan-area stars and core density appear.
6. Close MW5 after the result is clear.

Decision gate:

- If the mirror test restores the missing stars, root `/Game` package precedence is confirmed as the main blocker for the star population.
- If the mirror test is unchanged, the next target is the current `StarMapActor` / `MWInnerSphereData` runtime flow rather than packaging precedence.

First mirror attempt result:

- The first live mirror was built with the repository lightweight pak writer and mounted as a normal mod-root pak.
- Runtime produced a `failed to find data table MW5_InnerSphereData` style error but still reached the main menu.
- The starmap still appeared the same as the previous test.
- The test mirror was removed from `MW5Mercs\Content\Paks`; original game/TKU paks were untouched.

Correction:

- `tools\tku_reference_audit\build_tku_content_mirror.py` now builds the mirror with Epic `UnrealPak.exe`, not the lightweight writer.
- The corrected mirror uses the same legacy content-root mount style as the original required override:
  - mount point: `../../../MW5Mercs/Content/`
  - entries such as `InnerSphereData/MW5_InnerSphereData.uasset`
- `tools\mw5_pak.py` was updated so repository inspections correctly normalize content-root paks back to `/Game/...` paths.

Corrected mirror deployment:

- Command: `.\tools\Build-TKUCompatContentMirror.ps1 -Apply`
- Deployment report: `reports\tku_editor_first\tku_content_mirror_20260512-082819.md`
- Live mirror pak: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak`
- Live mirror SHA256: `4E40BDBF396D776870896DCE890B23C8D834A357168FC80CDAC7E85CAD0D965A`
- `UnrealPak -List` verifies the corrected mount and six expected entries:
  - `InnerSphereData/MW5_InnerSphereData.uasset`
  - `InnerSphereData/MW5_InnerSphereData.uexp`
  - `Levels/FrontEnd/StarMap.umap`
  - `Levels/FrontEnd/StarMap.uexp`
  - `UI/FrontEnd/StarMapPawn.uasset`
  - `UI/FrontEnd/StarMapPawn.uexp`

## Career Model Source Patch - 2026-05-25

Runtime evidence from the 2026-05-25 tests narrowed the failure:

- The live mod loaded and `StarMapPawn` bounds were active.
- The starmap still showed vanilla stars and vanilla faction overlay.
- A fresh save scan did not show TKU-only sample star IDs in the serialized `StarMapModel` segment.
- This reduced confidence in generic package/load-order failure and shifted the leading hypothesis to the active career model generation path.

Read-only probe:

- Script: `tools\tku_reference_audit\ue4_probe_campaign_model_sources.py`.
- Report: `reports\tku_editor_first\ue4_campaign_model_sources_probe.md`.
- The active DLC1 career class `/Game/DLC1/CareerMode/StartConditions/CareerMode` existed and still referenced `/Game/Campaign/_common/DefaultSystemGenerator.DefaultSystemGenerator_C` for `campaign_system_generator_class`.
- `MW5GameMode` and `CampaignMode` also still referenced the vanilla campaign generator class even though `default_inner_sphere_class` resolved to the mod-owned `StarSystemGenerator`.

Applied patch:

- Script: `tools\tku_reference_audit\ue4_patch_tku_career_model_sources.py`.
- Launcher: `tools\Invoke-TKUCareerModelSourcesPatch.ps1`.
- Report: `reports\tku_editor_first\ue4_career_model_sources_patch.md`.
- The commandlet completed with no safety failures and saved:
  - `/ModOverride/TKUCompatEditorPatch/Campaign/_common/DefaultSystemGenerator`.
  - `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/CareerMode`.
  - updated `/ModOverride/TKUCompatEditorPatch/Modes/MW5GameMode`.
  - updated `/ModOverride/TKUCompatEditorPatch/Modes/CampaignMode`.
- Updated defaults:
  - `DefaultInnerSphereClass` -> `/ModOverride/TKUCompatEditorPatch/InnerSphereData/StarSystemGenerator.StarSystemGenerator_C`.
  - `CampaignSystemGeneratorClass` -> `/ModOverride/TKUCompatEditorPatch/Campaign/_common/DefaultSystemGenerator.DefaultSystemGenerator_C`.

Packaging/deployment:

- The MW5 Mod Editor produced nested package folders again. The valid fresh package was:
  - `E:\Games\MechWarrior5Editor\MW5Mercs\Mods\TKUCompatEditorPatch\TKUCompatEditorPatch\TKUCompatEditorPatch`.
- Package inspection report: `reports\tku_editor_first\tku_packaged_mod_inspection_20260511.md`.
- Valid package pak SHA256: `34C81B14DA91F69DA9655C855CAF31286BE75446FEC8FBAB5B8A749464ECCA64`.
- `UnrealPak -List` confirmed all expected fragments, including the new `DefaultSystemGenerator` and DLC1 `CareerMode` overrides.
- Live deployment report: `reports\tku_editor_first\tkucompat_live_test_deploy_20260525-034655.md`.
- Version metadata report: `reports\tku_editor_first\tku_version_metadata_20260525-034707.md`.
- Live `mod.json` is now build `5`, load order `95`, `gameVersion` `1.13.378`, and has the 1.13.x / DLC7 description.
- Active live `modlist.json` is the isolated test profile:
  - `TKUEvidenceCorePluginOnly`
  - `TKUCompatEditorPatch`

Current validation gate:

- MW5 was launched after deployment for a fresh career starmap test.
- If TKU/clan/periphery stars appear, the missing active runtime path was the DLC1 `CareerMode` / `CampaignSystemGeneratorClass` binding.
- If the result remains vanilla except for bounds, the next evidence target is native `MWStarMapModel` or campaign-arc generation rather than mod metadata, package layout, or simple mode class defaults.

## Clan Cluster Cook Fix - 2026-05-25

Runtime result after the career model source patch:

- Career mode loaded and the starmap opened.
- Extended panning remained active.
- Taurian and Magistracy of Canopus space may have had more stars than before.
- Clan stars were still missing.
- Faction overlay still looked vanilla.

Follow-up package inspection changed the diagnosis:

- The then-current package did not contain any of the new `Content/Campaign/Clusters/TKU_*` cluster assets.
- Therefore the missing-clan runtime result did not prove the cluster data was rejected at runtime; it proved the package was still missing the assets needed to test that path.

Applied fix:

- Added `tools\Set-TKUCompatClusterManifest.ps1`.
- Applied report: `reports\tku_editor_first\tku_cluster_manifest_20260525-043107.md`.
- Updated editor source `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins\TKUCompatEditorPatch\mod.json`:
  - `gameVersion`: `1.13.378`.
  - `defaultLoadOrder`: `95`.
  - manifest count: `8` -> `18`.
  - TKU cluster manifest entries: `0` -> `10`.

Cluster asset source/cook evidence:

- Cluster asset patch report: `reports\tku_editor_first\ue4_tku_clan_cluster_assets_patch.md`.
- New package inspection report: `reports\tku_editor_first\tku_packaged_mod_inspection_20260511.md`.
- New package pak SHA256: `7B9EA432C7624E4AE045F90D5E4C81F91A744F94F285A75B57232BA12C0A6C4E`.
- `UnrealPak -List` now confirms all 10 expected TKU clan cluster/faction assets and their `.uexp` files:
  - `Content/Campaign/Clusters/TKU_ClanConflict/ClanConflict.uasset`.
  - `Content/Campaign/Clusters/TKU_ClanConflict/TKU_ClanConflict_NoOverlay_ClusterAsset.uasset`.
  - `Content/Campaign/Clusters/TKU_ClanConflict_Zones_ClanConf_1/TKU_ClanConflict_Zones_ClanConf_1_ClusterAsset.uasset`.
  - `Content/Campaign/Clusters/TKU_ClanConflict_Zones_ClanConf_2/TKU_ClanConflict_Zones_ClanConf_2_ClusterAsset.uasset`.
  - `Content/Campaign/Clusters/TKU_ClanConflict_Zones_ClanConf_3/TKU_ClanConflict_Zones_ClanConf_3_ClusterAsset.uasset`.
  - `Content/Campaign/Clusters/TKU_ClanConflict_Zones_ClanConf_4/TKU_ClanConflict_Zones_ClanConf_4_ClusterAsset.uasset`.
  - `Content/Campaign/Clusters/TKU_RepairSystem_Clan/RepairSystem_Clan.uasset`.
  - `Content/Campaign/Clusters/TKU_RepairSystem_Clan/TKU_RepairSystem_Clan_NoOverlay_ClusterAsset.uasset`.
  - `Content/Campaign/Clusters/TKU_RepairSystem_Clan_Zones_Clan_Safezone_1/TKU_RepairSystem_Clan_Zones_Clan_Safezone_1_ClusterAsset.uasset`.
  - `Content/Campaign/Clusters/TKU_RepairSystem_Clan_Zones_Clan_Safezone_2/TKU_RepairSystem_Clan_Zones_Clan_Safezone_2_ClusterAsset.uasset`.

Deployment:

- Live deployment report: `reports\tku_editor_first\tkucompat_live_test_deploy_20260525-122425.md`.
- Live deployed pak SHA256 matches the inspected source package: `7B9EA432C7624E4AE045F90D5E4C81F91A744F94F285A75B57232BA12C0A6C4E`.
- Live `mod.json` was normalized after deployment to `gameVersion` `1.13.378`; the MW5 Mod Editor packaged copy still stamped `1.13.64`.
- Active live profile remains isolated to `TKUEvidenceCorePluginOnly` plus `TKUCompatEditorPatch`.

Current validation gate:

- Launch MW5 against the active isolated profile.
- Start or load a career and open the starmap.
- Check for clan systems around the cluster IDs represented by the generated assets, including sample IDs such as `4088`, `4089`, `4090`, `4098`, `4100`, `4101`, `4103`, `4108`, `4110`, `4118`, `4120`, `4124`, `4127`, `4132`, `4135`, and `4143`.
- Check whether the faction overlay remains vanilla or now shows a cluster/territory change.
- If this still looks vanilla except for bounds, the next investigation target is cluster asset registry/discovery or runtime `MWStarMapModel`/campaign-arc generation, not package omission.

## Active Career Source Surface Patch - 2026-05-25

Runtime result after the cluster-cooked package:

- Career mode loaded and the starmap opened.
- Extended panning remained active.
- Stars that exist appear to carry TKU ownership data; the user specifically observed Oberon Confederation ownership.
- The visible base starmap and faction overlay still look vanilla.
- TKU/clan stars are still missing.

Save/runtime model evidence:

- Latest save scan report: `reports\tku_editor_first\mw5_save_starmap_scan_20260525-131101.md`.
- The latest test save still used `MWStartConditionsAsset:CareerMode_Davion_Start`.
- Both latest scanned saves serialized `MWStarMapModel`, but the TKU/clan sample IDs were absent from the serialized StarMapModel segment.
- This supports a split failure: TKU row/faction data can affect existing vanilla systems, but the runtime star model is still not receiving the TKU-only systems.

Applied active-source patch:

- Script: `tools\tku_reference_audit\ue4_patch_tku_active_career_sources.py`.
- Launcher: `tools\Invoke-TKUActiveCareerSourcesPatch.ps1`.
- Report: `reports\tku_editor_first\ue4_active_career_sources_patch.md`.
- Dry-run safety failures: none.
- Apply result: `attempted=True`, `applied=True`, `saved=True`.
- Saved `17` current-schema active career source assets into `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins\TKUCompatEditorPatch\ModOverride`, covering:
  - all 12 direct DLC1 `CareerMode_*_Start` and tutorial start-condition assets.
  - `/Game/DLC1/CareerMode/StartConditions/CareerMode_Start`.
  - `/Game/DLC1/CareerMode/StartConditions/FRR_CareerMode_Start`.
  - `/Game/DLC1/CareerMode/CareerModeCoreCampaign`.
  - `/Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters`.
  - `/Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones`.

Manifest update:

- Script: `tools\Set-TKUCompatClusterManifest.ps1`.
- Applied report: `reports\tku_editor_first\tku_cluster_manifest_20260525-132824.md`.
- Editor source `mod.json` now targets `gameVersion` `1.13.378`, load order `95`.
- Source manifest count: `18` -> `35`.
- Active career source manifest entries: `0` -> `17`.
- Local source-file check found `0` missing files for the 35 manifest entries.

Verification probe:

- Probe rerun: `reports\tku_editor_first\ue4_campaign_model_sources_probe.md`.
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Davion_Start` now resolves to `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/CareerMode_Davion_Start.CareerMode_Davion_Start`.
- `/Game/DLC1/CareerMode/StartConditions/CareerMode_Start` now references the mod-owned `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/CareerModeCoreCampaign`.
- `/Game/DLC1/CareerMode/CareerModeCoreCampaign` now references mod-owned `CareerModeClusters` and `CareerMode_SafeZones`.
- The duplicated active assets still contain vanilla border and warzone action content; this patch establishes a packageable current-schema active surface for the next runtime test and later content edits, but it is not evidence that the clan star generation path is fixed.

Current validation gate:

- Package `TKUCompatEditorPatch` again in the MW5 Mod Editor.
- Deploy the newest nested package output to the live isolated test profile.
- Start a fresh career test, preferably from a fresh slot, and open the starmap.
- Expected discriminator:
  - If the result changes, the active career source packaging was blocking some runtime path.
  - If the result remains vanilla except for bounds and TKU ownership on existing stars, the leading root cause is runtime `MWStarMapModel` generation bypassing the patched generator/table path, with a separate remaining overlay-content problem in vanilla border/warzone actions.

## Active Cluster Diagnostic Patch - 2026-05-25

Runtime result after the active career source package:

- Career mode loaded and the starmap opened.
- Extended panning remained active.
- The starmap opened at a corner rather than centered on the ship.
- Clan stars were still absent, star density remained low, and faction overlay still showed only the five major vanilla factions.
- Latest save scan report: `reports\tku_editor_first\mw5_save_starmap_scan_20260525-153826.md`.
- Save evidence: latest career save still used `MWStartConditionsAsset:CareerMode_Davion_Start`, advertised DLC1 through DLC7, serialized 80 `StarSystemId`/`MWClusterDataAsset`/`ClusterAsset` marker slots in the current scanner, and had zero `StarMapModel` occurrences for sample clan IDs `4088`, `4089`, `4090`, `4098`, `4100`, `4101`, `4103`, `4108`, `4110`, `4118`, `4120`, `4124`, `4127`, `4132`, `4135`, and `4143`.

Cross-agent review and sequential review:

- Cross-agent review via Claude recommended a narrow active-cluster diagnostic before broad DLC7/career-arc mutation.
- I accept the recommendation with one correction: the peer assumed a DLC7 campaign cluster was runtime-active, but local save evidence only proved active cluster names after a separate scan.
- Local save string extraction showed active serialized cluster names including `Rasalhague_7_10_ClusterAsset`, `SafeZone_*_ClusterAsset`, major-house region clusters, and DLC6/DLC7 clusters.
- The resulting discriminator is: append a few TKU clan system IDs to a proven active cluster, package, run a fresh career, and rescan the save. If those IDs enter `StarMapModel`, cluster membership is the blocker; if not, the remaining failure is upstream of cluster membership or in runtime initialization.

Applied diagnostic patch:

- Script: `tools\tku_reference_audit\ue4_patch_tku_active_cluster_diagnostic.py`.
- Launcher: `tools\Invoke-TKUActiveClusterDiagnosticPatch.ps1`.
- Report: `reports\tku_editor_first\ue4_active_cluster_diagnostic_patch.md`.
- Source cluster: `/Game/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset`.
- Target override: `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset`.
- Diagnostic IDs appended: `4088`, `4089`, `4090`.
- Apply result: `attempted=True`, `applied=True`, `saved=True`.
- The target cluster system count changed from `18` to `21`, preserving the original cluster faction/overlay for this diagnostic.

Manifest update:

- Manifest script updated: `tools\Set-TKUCompatClusterManifest.ps1`.
- Applied report: `reports\tku_editor_first\tku_cluster_manifest_20260525-162032.md`.
- Editor source `mod.json` now has `gameVersion` `1.13.378`, load order `95`, and manifest count `36`.
- New manifest entry: `/Game/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset.uasset`.

Current validation gate:

- Package `TKUCompatEditorPatch` again in the already-running MW5 Mod Editor.
- Inspect the newest nested package output and confirm the pak includes `Content/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset.uasset`.
- Deploy the package to the isolated live profile.
- Start a fresh career and open the starmap.
- Run the save scanner with sample IDs `4088`, `4089`, and `4090`.
- Expected discriminator:
  - If `4088`, `4089`, or `4090` appears in the serialized `StarMapModel`, then active cluster membership is confirmed as the missing path and the next fix should migrate TKU clan IDs into active/discoverable DLC7/current-schema cluster placement assets.
  - If those IDs still do not appear, the blocker is upstream of `MWClusterDataAsset.system_ids` or the active career source override is not taking package precedence at runtime.

## Runtime Result After Active Cluster Diagnostic - 2026-05-25

Package and deployment evidence:

- Package inspection report: `reports\tku_editor_first\tku_packaged_mod_inspection_20260511.md`.
- Packaged build: `8`.
- Packaged pak SHA256: `AB3D9FFAA0E1D0E0724647329889A42C1B490211EC61D14177A93D0659CE3AA6`.
- `UnrealPak -List` confirmed the diagnostic override exists in the pak:
  - `Content/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset.uasset`.
  - `Content/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset.uexp`.
- Live deployment report: `reports\tku_editor_first\tkucompat_live_test_deploy_20260525-163735.md`.
- Live deployed pak SHA256 matches the inspected source package: `AB3D9FFAA0E1D0E0724647329889A42C1B490211EC61D14177A93D0659CE3AA6`.
- Live `mod.json` was normalized to `gameVersion` `1.13.378`, load order `95`, build `8`.
- Active live profile remained isolated to `TKUEvidenceCorePluginOnly` and `TKUCompatEditorPatch`.

Runtime result:

- Career mode loaded and the starmap opened.
- The user reported the starmap looked the same as the previous run.
- The user saved after opening the starmap.
- Latest save scan report: `reports\tku_editor_first\mw5_save_starmap_scan_20260525-164145.md`.
- Latest campaign: `House Davion`, start condition `MWStartConditionsAsset:CareerMode_Davion_Start`, DLC tags `DLC1` through `DLC7`, last save `9A4F28E54B4B3C198B385CB51BF47EA4`.
- The latest save still had zero `StarMapModel` occurrences for diagnostic IDs `4088`, `4089`, and `4090`.

Important correction to the diagnostic interpretation:

- Follow-up scan report: `reports\tku_editor_first\mw5_save_starmap_scan_20260525-164254.md`.
- The same save also had zero `StarMapModel` occurrences for original `Rasalhague_7_10_ClusterAsset` member IDs such as `933`, `952`, `990`, `1568`, `1573`, `1581`, `1585`, `1586`, `1587`, `1600`, `1602`, `1606`, `1616`, `1629`, `1630`, `1637`, `1644`, and `1651`.
- Therefore the save-ID scan is not a definitive proof that `MWClusterDataAsset.system_ids` was ignored; the save appears to serialize cluster asset identifiers and TOI/state data rather than all cluster member star IDs.
- The visual result remains negative, but the failed diagnostic now narrows the next evidence target to the active campaign arc/action path, not only cluster data asset contents.

Next evidence target:

- Probe the mod-owned active career arcs and their place-cluster actions, especially `CareerModeClusters`, `CareerMode_SafeZones`, and referenced `PlaceCluster*` action Blueprints.
- For each active placement action, capture action class, CDO properties, `ClusterDataAsset`, `ClusterDataAssetId`, campaign event list entries, trigger/condition properties, and referencer chains.
- Compare the current active career action pattern against DLC7 clan placement actions under `/Game/DLC7/PlaceClusterActions/NewClusters`.
- Do not continue with blind package/retest loops until that active action graph is mapped.

## Active Campaign Action Graph Probe And Content Mirror Discriminator - 2026-05-25

Cross-agent review follow-up:

- Peer review identified four valid gaps in the first active-action probe: direct event action path collection was too string-based, traversal only enqueued cluster paths, `ClusterDataAssetId` was missing from summaries, and the 480-asset walk cap could saturate.
- Implemented corrections in `tools\tku_reference_audit\ue4_probe_active_campaign_actions.py` and `tools\Invoke-TKUActiveCampaignActionsProbe.ps1`.
- Validation: Python AST parse passed; PowerShell parser check passed.
- Probe report: `reports\tku_editor_first\ue4_active_campaign_actions_probe.md`.
- Probe result: `800` assets inspected; walk limit still hit; `252` active ArcAction Blueprints found; `47` PlaceCluster-like actions; `35` PlaceSafeZone actions; `212` cluster references; only `1` mod-owned cluster reference.
- Confirmed active mod-owned binding: `/Game/DLC1/CareerMode/Warzones/Rasalhauge_Clusters/PlaceRasalhague_ArcAction_7_10` points to `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset` with `ClusterDataAssetId` `MWClusterDataAsset:Rasalhague_7_10_ClusterAsset`.
- Important negative evidence: TKU clan cluster assets exist in the package, but the current active campaign graph does not wire them into active placement roots.

Deployment discriminator implemented:

- Root contradiction before this step: editor and package evidence showed the TKU DataTable, `StarSystemGenerator`, and `StarMap` level with clan stars, while runtime still showed vanilla stars/overlay and the latest save lacked clan star strings.
- Patched `tools\tku_reference_audit\build_tku_content_mirror.py` so the content mirror builder selects the newest available `TKUCompatEditorPatch.pak` instead of the stale 2026-05-12 top-level editor pak.
- Patched `tools\Set-TKUContentPakIsolation.ps1` with `-Target All|CompatMirror|LegacyStarmap` and fixed the PowerShell `$Target`/`$target` variable collision found during status validation.
- Dry-run mirror report: `reports\tku_editor_first\tku_content_mirror_20260525-170948.md`; staged `8` files with mount `../../../MW5Mercs/Content/` and no safety failures.
- Applied mirror report: `reports\tku_editor_first\tku_content_mirror_20260525-171114.md`.
- Live mirror deployed: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak`.
- Live mirror SHA256: `4414AC6DA60FD9D04E5BCB9098E0D716A689912AF4C484288AD54680537860DC`.
- Stale disabled compat mirror moved to repo backup: `reports\tku_editor_first\backups\content_mirror_20260525-171114\MW5Mercs-zzzzTKUCompatEditorPatch.pak.disabled-by-tku-isolation`.
- Legacy `MW5Mercs-zKnownUniverseStarmap.pak` remains disabled; it was not restored or edited.
- Isolation status report: `reports\tku_editor_first\tku_content_pak_isolation_20260525-171148.md`; compat mirror active before/after `True`, disabled sibling before/after `False`.

Current validation gate:

- Close the MW5 Mod Editor before launching the game.
- Launch MW5 with the isolated live modlist: `TKUEvidenceCorePluginOnly` and `TKUCompatEditorPatch`.
- Start a new career or a fresh test slot, open the starmap, and inspect clan/periphery space before relying on an older save.
- Record whether clan stars such as Strana Mechty appear, whether faction overlay remains vanilla, and whether the map still starts in a corner.
- After saving, run `python tools\tku_reference_audit\scan_mw5_save_starmap.py --sample-ids 4088 4089 4090 4110 7921` to capture the next save artifact.
- If the fresh content-root mirror restores TKU/clan stars, the remaining root is mod-pak mount/override precedence for root `/Game` starmap/data assets.
- If stars remain absent with the content-root mirror active, the next repair surface is runtime initialization/campaign source binding rather than basic pak presence.

## Runtime Result After Fresh Content Mirror - 2026-05-25

Runtime result:

- MW5 launched with isolated live `modlist.json` enabling only `TKUEvidenceCorePluginOnly` and `TKUCompatEditorPatch`.
- Active content mirror before launch: `MW5Mercs-zzzzTKUCompatEditorPatch.pak`, SHA256 `4414AC6DA60FD9D04E5BCB9098E0D716A689912AF4C484288AD54680537860DC`.
- The user created/loaded the test career, opened the starmap, observed no visible change, and saved.
- User-visible result: clan/TKU stars still absent and faction overlay still vanilla.

Save evidence:

- Save scan report: `reports\tku_editor_first\mw5_save_starmap_scan_20260525-190333.md`.
- Latest campaign path: `C:\Users\dogpe\AppData\Local\MW5Mercs\Saved\SaveGames\2ABF90FF4B331B545900CBAC70A9230A\Campaign.json`.
- Campaign: `House Davion`.
- Start condition: `MWStartConditionsAsset:CareerMode_Davion_Start`.
- DLC tags: `DLC1` through `DLC7`.
- Latest save: `37C711E141C90274851105B37CBC3707.sav`, timestamp `2026-05-25T19:00:06`.
- `StarMapModel` sample-id occurrences remain zero for `4088`, `4089`, `4090`, `4110`, and `7921`.
- Direct binary string scan of the latest saves found no `Strana Mechty`, `Strana`, `Babylon`, `Huntress`, `Clan`, `Oberon`, or `TKU_ClanConflict` strings.
- The same saves still contain `TaurianConcordat`, `MagistracyOfCanopus`, and `Rasalhague_7_10_ClusterAsset`, matching the visible partial-periphery/vanilla-active state.

Content mirror package evidence:

- `UnrealPak -List` on the live mirror confirms mount point `../../../MW5Mercs/Content/`.
- The live mirror contains the expected eight files:
  - `InnerSphereData/MW5_InnerSphereData.uasset/.uexp`.
  - `InnerSphereData/StarSystemGenerator.uasset/.uexp`.
  - `Levels/FrontEnd/StarMap.umap/.uexp`.
  - `UI/FrontEnd/StarMapPawn.uasset/.uexp`.

Conclusion:

- This test did not support the hypothesis that a fresh content-root mirror alone restores TKU-only stars.
- The strongest remaining repair surface is now active campaign/starmap initialization and placement-action wiring, not basic package presence for the eight mirrored root assets.
- Faction overlay remains a separate confirmed gap: the active campaign graph still has only one mod-owned cluster binding and no active TKU clan cluster placement roots.

## All-Game Content Mirror Discriminator - 2026-05-25

User-provided strategy note:

- The user supplied a public-source strategy analysis arguing that DLC7 likely broke TKU through stale base-game overrides and that the old required override pak is a critical clue.
- This was treated as strategy context, not proof. The local evidence still controls the repair path.
- The local evidence matches one part of that model: the current editor-authored `TKUCompatEditorPatch.pak` contains more root `/Game` overrides than the active content-root mirror was deploying.

Evidence before the change:

- The active content mirror from `reports\tku_editor_first\tku_content_mirror_20260525-171114.md` contained only `8` files.
- The current live/editor-authored `TKUCompatEditorPatch.pak` contains additional root `/Game` assets needed for runtime activation tests, including:
  - `/Game/Campaign/_common/DefaultSystemGenerator.uasset/.uexp`.
  - `/Game/DLC1/CareerMode/CareerModeCoreCampaign.uasset/.uexp`.
  - `/Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters.uasset/.uexp`.
  - `/Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones.uasset/.uexp`.
  - `/Game/Modes/CampaignMode.uasset/.uexp`.
  - `/Game/Modes/MW5GameMode.uasset/.uexp`.
  - TKU clan conflict and repair-system cluster assets under `/Game/Campaign/Clusters/TKU_*`.
- Therefore the previous mirror test proved only the starmap-core override path. It did not prove whether the full editor-authored `/Game` override set can win runtime precedence.

Implemented change:

- Patched `tools\tku_reference_audit\build_tku_content_mirror.py` to support mirror scopes:
  - `starmap-core`: previous 8-file behavior.
  - `all-game`: mirrors every `/Game/*` asset sidecar entry from the selected source pak.
- The tool now records source pak candidates, selected mirror scope, live disabled sibling status, and a mirrored path sample in the generated report.
- The tool still builds a separate late-loading content pak and backs up the previous live mirror; it does not rewrite game paks or cooked source assets.

Validation and deployment:

- Python AST parse passed for `tools\tku_reference_audit\build_tku_content_mirror.py`.
- Dry-run report: `reports\tku_editor_first\tku_content_mirror_20260525-193027.md`.
- Dry-run result: `72` target paths selected, `72` staged entries, no safety failures.
- Applied report: `reports\tku_editor_first\tku_content_mirror_20260525-193109.md`.
- Live mirror deployed: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak`.
- Previous 8-file live mirror backup: `reports\tku_editor_first\backups\content_mirror_20260525-193109\MW5Mercs-zzzzTKUCompatEditorPatch.pak`.
- Live all-game mirror SHA256: `158B2C6A203646E6595C761F8B8D310B4792A6C9E6C1A9330D34B81E71D2B405`.
- Live pak verification with `mw5_pak.iter_entries`:
  - mount point: `../../../MW5Mercs/Content/`.
  - total entries: `72`.
  - `/Game` sidecar entries: `72`.
  - confirmed present: `/Game/Modes/CampaignMode.uasset`.
  - confirmed present: `/Game/Modes/MW5GameMode.uasset`.
  - confirmed present: `/Game/DLC1/CareerMode/CareerModeCoreCampaign.uasset`.
  - confirmed present: `/Game/Campaign/Clusters/TKU_ClanConflict/TKU_ClanConflict_NoOverlay_ClusterAsset.uasset`.
  - confirmed present: `/Game/Levels/FrontEnd/StarMap.umap`.

Next validation gate:

- Launch MW5 from a closed state with the isolated live mod profile.
- Start a new Davion career or a fresh test career, open the starmap, and inspect visible TKU/clan star coverage.
- Record whether clan systems such as Strana Mechty appear, whether faction overlay remains vanilla, whether map centering is still wrong, and whether extended panning remains active.
- Save once after opening the starmap so `tools\tku_reference_audit\scan_mw5_save_starmap.py --sample-ids 4088 4089 4090 4110 7921` can capture the next evidence artifact.
- If nothing changes, the next confirmed repair surface is active campaign event/action rebasing onto DLC7 rather than content mirror coverage.
