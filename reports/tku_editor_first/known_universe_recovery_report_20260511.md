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
