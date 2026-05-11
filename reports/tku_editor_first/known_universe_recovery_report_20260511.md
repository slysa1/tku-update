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

## Next Manual Gate

1. Open `E:\Games\MechWarrior5Editor\MW5Mercs\MW5Mercs.uproject`.
2. Let asset discovery finish.
3. Use Create Mod to create `TKUCompatEditorPatch`.
4. Close or save as needed, then run:

```powershell
python tools\tku_reference_audit\inspect_editor_mod_targets.py
```

5. If the target exists, proceed to a controlled mod-owned `MW5_InnerSphereData` copy/import test using:

```text
reports\tku_editor_first\tku_inner_sphere_merged_current_plus_tku_additions_20260510.csv
```

After the target exists and the DataTable copy/override path is known, run a dry preflight first:

```powershell
.\tools\Invoke-TKUInnerSphereImport.ps1 -TargetAssetPath '<mod-owned DataTable asset path>'
```

Only if the dry run reports no safety failures, run:

```powershell
.\tools\Invoke-TKUInnerSphereImport.ps1 -TargetAssetPath '<mod-owned DataTable asset path>' -Apply
```

For a same-path root override created with `Save To Mod`, the apply command must include `-AllowRootOverride`, and the active editor mod must be `TKUCompatEditorPatch`.

Do not package until the DataTable row validation and cluster/bounds repair plan are updated with editor evidence.
