# TKU Compatibility Project Full Handoff - 2026-05-11

This handoff records the work completed so far, the evidence behind the main decisions, and the exact place the project stopped. It is written so another engineer or agent can pick up without repeating the blind pak work that has already been ruled out.

## Current Status

- Primary project workspace for future sessions: `D:\Downloads\OneDrive\Documents\code\tku-update`
- Live MW5 install: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries`
- MW5 Mod Editor: `E:\Games\MechWarrior5Editor`
- Current MW5 version under test: `1.13.378`
- Current stable runtime floor: only `TKUEvidenceCorePluginOnly` enabled in `MW5Mercs\Mods\modlist.json`
- No runtime pak build is currently authorized.
- The next required gate is manual interactive creation of an MW5 Mod Editor mod target named `TKUCompatEditorPatch`.

The compatibility project has moved away from blind cooked-pak substitutions. The active strategy is evidence-first and editor-first: use restored original TKU files only as source evidence, reconstruct or port needed behavior through the MW5 Mod Editor using current-compatible assets and schemas, and package only after an explicit evidence gate.

## Stop Point

Codex reached the editor authoring gate but could not complete the first interactive `Create Mod` step from the automation session.

What is needed next:

1. Manually open `E:\Games\MechWarrior5Editor\MW5Mercs\MW5Mercs.uproject`.
2. In the MW5 Mod Editor UI, create a new mod named `TKUCompatEditorPatch`.
3. After it exists, inspect the created folders and metadata under:
   - `E:\Games\MechWarrior5Editor\MW5Mercs\Mods`
   - `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins`
4. Continue with the mod-owned DataTable import gate. Do not package yet.

Codex attempted to launch the editor directly. `UE4Editor.exe` started, generated the Python stub, completed asset discovery, and compiled shaders down to one remaining, but no usable top-level window was exposed to the Codex session (`MainWindowHandle` stayed `0`). The process was stopped. Launch through Explorer association returned without starting `UE4Editor`. This is documented in `reports\tku_editor_first\editor_gui_launch_attempt_20260510.md`.

## Hard Safety Rules

- Work from the restored original Nexus TKU build-38 files only.
- Do not use quarantined failed builds as source material.
- Do not overwrite or edit original paks.
- Do not edit `MW5Mercs\Content\Paks\MW5Mercs-zKnownUniverseStarmap.pak`.
- Do not resume blind pak toggling.
- Do not build another runtime pak until a specific evidence gate says to.
- Use MW5 Mod Editor behavior and UE4.27 docs as the Unreal source of truth.
- Do not restore TKU root `/Game` substitutions wholesale.
- Do not use old cooked TKU starmap, pawn, body, or border classes directly.

These rules exist because earlier runtime tests showed cooked assets can look plausible by package path while hiding incompatible Blueprint graphs, parent assumptions, CDO defaults, data schemas, and level references.

## Source State

The live `MW5Mercs\Mods\TheKnownUniverse` folder was restored from the original Nexus TKU download and is treated as the clean original source under test.

Known hashes:

- Original TKU mod pak: `MW5Mercs\Mods\TheKnownUniverse\Paks\TheKnownUniverse.pak`
- TKU mod pak SHA256: `0F23FC683DEBEC27D07FF6739137BA1E4069934082D5AFFF6B3F2161CC64C678`
- Original loose starmap override pak: `MW5Mercs\Content\Paks\MW5Mercs-zKnownUniverseStarmap.pak`
- Loose starmap pak SHA256: `DFAC2CA2E1DEDCD96709A95A778DA1BB55EB02BB87E9E62B7DFC8320DD9F1FCB`

Failed blind-build artifacts were preserved under `codex_quarantine\tku_failed_compat_20260510` for history only.

## Runtime Work Completed

The original TKU setup failed on new-career load with `EXCEPTION_ACCESS_VIOLATION reading address 0x000000000000004c`.

Runtime isolation established:

- The loose required override pak alone is not fatal. With zero enabled mods, Davion career, vanilla starmap, and mechbay loaded.
- `vonBiomes` is not sufficient to explain the crash. The same `0x4C` crash reproduced with `vonBiomes` disabled.
- TKU's mod pak is sufficient to reproduce the crash, even with the loose required override disabled.
- The fatal path is therefore centered on old TKU mod-pak content, not on the loose override alone and not on `vonBiomes`.

Evidence builds tested:

- `TKUEvidenceStarmapCompat`
  - Replaced only TKU `StarMapActor` and `StarSystemBody` with current vanilla assets on top of original TKU.
  - Changed the repeated `0x4C` fatal crash into a loading stall.
  - Reasoning: this implicated the stale old starmap class stack, but showed replacement of that pair alone is not coherent with the remaining TKU root assets.

- `TKUEvidenceStartBorderCompat`
  - Reasserted current vanilla `Borders3015`, `AllStarMapBorderChanges`, and `BaseStarMapBorderActor`.
  - Failed with `Could not find SuperStruct BaseStarMapBorderActor_C to create StarMapActor_2570_C`.
  - Reasoning: direct cooked border substitution is unsafe. The issue involves current HoloTable/border child Blueprints and stale TKU root base-class overrides.

- `TKUEvidenceCorePluginOnly`
  - Rebuilt from restored original TKU build 38.
  - Kept 2,427 non-`/Game` entries and removed all 282 root `/Game` substitutions.
  - Runtime result: career and starmap loaded, contracts/travel/save basic checks passed, Steiner/Lyran ownership restored.
  - Remaining limitation: starmap bounds are vanilla and territory overlay remains incomplete/vanilla-like.
  - Reasoning: this is the stable floor because removing root `/Game` substitutions avoids stale class and data overrides while retaining useful TKU plugin content.

- `TKUEvidenceBoundsPawn`
  - Restored original TKU cooked `StarMapPawn` on top of core plugin-only.
  - Runtime result: career loaded, but pressing starmap entered first-person hangar view.
  - Decision: old cooked pawn restore is ruled out.

- `TKUEvidenceCurrentPawnBounds`
  - Started from current vanilla `StarMapPawn`, preserved current widget/tooltip references, changed only serialized pan/zoom defaults.
  - Runtime result: same first-person hangar behavior.
  - Decision: current-package cooked StarMapPawn CDO patch is also ruled out.

The active `modlist.json` was repeatedly verified with only `TKUEvidenceCorePluginOnly` enabled. At the last checks no MW5 or UE4 editor process was running.

## Major Findings And Reasoning

### Why The Old Root `/Game` TKU Assets Are Blocked

Original TKU build 38 predates important current MW5 starmap and cluster systems. Its root `/Game` assets include stale starmap classes, stale border parents, old data tables, and old faction/employer assets.

Evidence:

- Original TKU mod-pak `StarMap.umap` binds to `/ModOverride/TheKnownUniverse/...` starmap classes.
- Loose required override `StarMap.umap` binds to current `/Game/...` starmap classes and is not fatal by itself.
- Current vanilla `StarSystemBody` imports `/Script/MechWarrior.MWClusterDataAsset` and exports current cluster functions such as `ResetClusterMeshes`, `GetClusterOverlayMesh`, and `GetClusterConstellationMesh`.
- Original TKU `StarSystemBody` lacks that modern cluster pipeline.
- TKU root border assets can break current HoloTable/border children through `BaseStarMapBorderActor_C`.

Choice made:

Do not restore original TKU root `/Game` assets as a group. Recreate or port only the needed behavior through editor-authored current-compatible assets.

### Why The Project Became Editor-First

Pak manifests and string scans were useful for triage, but cooked assets hide too much behavior to safely port TKU. Blueprint graphs, class parents, CDO defaults, construction scripts, asset references, and row schemas need MW5 Mod Editor visibility.

Choice made:

Use commandlet Python, FModel, umodel, and package parsers for evidence. Use the MW5 Mod Editor UI or a proven UE4.27-compatible editor script path for mutating assets. No more blind cooked-pak patching.

### Why Bounds And Territory Overlay Are Separate Tracks

Current stable floor loads but has vanilla map bounds and incomplete overlays. Evidence shows these are not solved by only changing `StarMapPawn` defaults.

Bounds evidence:

- Current `StarMapPawn` defaults are vanilla-scale:
  - `PanBoundsHorizontal=5500`
  - `PanBoundsVertical=4500`
  - `ZoomDistanceList=[400,550,700,1400,1600,1800,3500]`
  - `ZoomLevelThresholds=[2000,1000]`
- Original TKU defaults are wider:
  - `PanBoundsHorizontal=8500`
  - `PanBoundsVertical=16000`
  - `ZoomDistanceList=[300,600,900,1300,1800,2200,2800,3500,5000,7500,9000]`
  - `ZoomLevelThresholds=[3500,1000]`
- But both old and current cooked pawn patch attempts broke starmap opening into first-person hangar view.
- Current `/Game/Levels/FrontEnd/StarMap` has 2,182 actors, including 2,172 placed `StarSystemBody_C` actors.
- The runtime CSV has 2,173 rows, while the wider source JSON has 3,446 systems.

Overlay evidence:

- Current editor has 79 `MWClusterDataAsset` assets and 261 assets under `/Game/Campaign/Clusters`.
- Original TKU has no `/Game/Campaign/Clusters` assets and no scanned `MWClusterDataAsset` strings.
- Current cluster assets expose `system_ids`, `cluster_faction_asset`, `cluster_overlay`, and `cluster_constellation`.

Choice made:

Bounds repair should inspect `StarMapActor`, level placement/generation, and source-to-runtime data import. Overlay repair should proceed as current-schema `MWClusterDataAsset` migration. Do not assume another pawn patch will fix the map.

## Data Extraction And Import Planning

Original TKU `/Game/InnerSphereData/MW5_InnerSphereData` was parsed directly from the restored original TKU pak.

Clean-source parse results:

- 3,929 parsed TKU rows.
- Row IDs range from `0` to `7921`.
- PosX range about `-1877..1937`.
- PosY range about `-2004..1912`.
- 1,091 clustered rows.
- 69 unique cluster IDs.
- 103 overlay rows.
- 38 constellation rows.

Important parser fix:

UE4 `FName` numeric suffix handling was corrected. Enum values such as `C_8` and `H_0` must preserve suffixes. Earlier collapsed `C`/`H` output was wrong and was fixed before import candidates were generated.

Current placement formula recovered from editor evidence:

```text
LevelX = 51336 + 8 * PosY
LevelY = 51039 + 8 * PosX
```

Projected TKU span with that formula:

- Level X about `35305..66633`.
- Level Y about `36020..66538`.
- This is roughly 3.6x / 3.2x current placed-body half-span.

Import candidates generated:

- Raw original TKU current-schema CSV.
- Merged current-plus-TKU-additions CSV.

Preferred first candidate:

`reports\tku_editor_first\tku_inner_sphere_merged_current_plus_tku_additions_20260510.csv`

Reasoning:

- It preserves all 2,173 current MW5 v1.13 rows.
- It adds 1,801 TKU-only systems.
- It retains 45 current-only rows.
- It totals 3,974 rows.
- Raw original TKU import is riskier because shared current/TKU rows differ heavily in positions and 468 cluster assignments.

## Editor And Python API Probes

Non-mutating editor API probes were run.

Findings:

- `MWModPluginInfo`, `ModPackageArgs`, `MWModUtils`, and `MWModEditorWidget.package_mod(args)` exist.
- No safe direct module-level `CreateMod`, `SaveToMod`, `SaveTo`, or `PackageMod` symbol was found.
- `MWModEditorWidget` is exposed but abstract in commandlet construction.
- Commandlet saw no active mod plugin.
- `MWModUtils.create_mod_entry` can return a transient editor list entry, but creates no mod/plugin folders and is not a safe Create Mod workflow.

The generated editor Python stub exposes useful post-target APIs:

- `EditorAssetLibrary.duplicate_asset`
- `DataTableFunctionLibrary.fill_data_table_from_csv_file`
- `EditorAssetLibrary.save_asset`
- `AssetTools.import_asset_tasks`
- `AssetImportTask`
- `DataTableFactory`
- `CSVImportFactory`

Choice made:

The first mod target must be created in the MW5 Mod Editor UI. After that target exists, Python may be used for a controlled mod-owned DataTable import/save test, but only on a mod-owned asset and only after filesystem inspection confirms the target structure.

## Current Blocker

The current blocker is not technical evidence. It is the first interactive editor action:

Create `TKUCompatEditorPatch` in the MW5 Mod Editor UI.

The project is intentionally stopped here because:

- Python-only Create Mod was not proven safe.
- `create_mod_entry` did not scaffold a real mod.
- Codex could not expose an interactive editor GUI window from its launch attempt.
- Manually creating the mod target through the editor is the smallest safe mutation.

## Next Exact Steps

After `TKUCompatEditorPatch` exists:

1. Inspect the created files:
   - `E:\Games\MechWarrior5Editor\MW5Mercs\Mods\TKUCompatEditorPatch`
   - `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins\TKUCompatEditorPatch`
   - Any `.uplugin`, `mod.json`, config, content, or `ModOverride` folders.

2. Record the filesystem delta in a new report.

3. Confirm active editor mod metadata through a non-mutating commandlet if possible.

4. Create or confirm a mod-owned copy of:
   - `/Game/InnerSphereData/MW5_InnerSphereData`

   Prefer the editor's `Save To Mod` UI for the initial same-path override copy if available.

5. Import the merged CSV into the mod-owned DataTable only:
   - `reports\tku_editor_first\tku_inner_sphere_merged_current_plus_tku_additions_20260510.csv`

6. Verify:
   - Row count is `3,974`.
   - Sample IDs exist, including `1`, `2`, `3501`, `4001`, `4110`, and `7921`.
   - No enum import errors.
   - Base current rows still exist and descriptions remain current where expected.

7. Do not package yet.

8. Decide next track:
   - If the DataTable import is clean, inspect/generate current-compatible starmap placement and bounds.
   - For overlays, write a mapping policy before creating any `MWClusterDataAsset` files.

## Important Reports

Use these first:

- `TKU_COMPAT_PATCH_ROADMAP.md`
- `reports\tku_editor_first\tku_continuation_handoff_20260510.md`
- `reports\tku_editor_first\reference_trace_manifest.md`
- `reports\tku_editor_first\editor_authoring_runbook_20260510.md`
- `reports\tku_editor_first\editor_gui_launch_attempt_20260510.md`
- `reports\tku_editor_first\ue4_mod_entry_creation_probe_20260510.md`
- `reports\tku_editor_first\ue4_asset_authoring_api_stub_probe_20260510.md`
- `reports\tku_editor_first\tku_inner_sphere_import_candidates_20260510.md`
- `reports\tku_editor_first\tku_editor_repair_candidate_manifest_20260510.md`
- `reports\tku_editor_first\starmap_generation_trace_20260510.md`
- `reports\tku_editor_first\original_tku_inner_sphere_datatable_rows_20260510.md`

## Tooling Notes

Available local tools:

- MW5 Mod Editor: `E:\Games\MechWarrior5Editor`
- UnrealPak: `E:\Games\MechWarrior5Editor\Engine\Binaries\Win64\UnrealPak.exe`
- UE4Editor-Cmd: `E:\Games\MechWarrior5Editor\Engine\Binaries\Win64\UE4Editor-Cmd.exe`
- FModel: `C:\Program Files\fmodel`
- UEViewer/umodel: `C:\Program Files\umodel`
- Blender 5.1 with Unreal PSK/PSA addon: `C:\Program Files\Blender Foundation\Blender 5.1`
- UAssetAPI/MW5AssetTool: `D:\Downloads\OneDrive\Documents\code\tku-update\tools\MW5AssetTool`
- UAssetGUI: `C:\Program Files\UassetGUI`
- UE4SS v3.0.1 dev extraction: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Binaries\Win64`

Use FModel, umodel, Blender, UAssetAPI/MW5AssetTool, UAssetGUI, and UE4SS for cooked asset inspection, structured UAsset comparison, mesh/animation import-export, runtime instrumentation, Lua/mod hooks, and supporting evidence where appropriate. Prefer MW5 Mod Editor and UE4.27 docs for final asset-authoring decisions.

## What Not To Do Next

- Do not re-enable original `TheKnownUniverse` for a runtime test unless explicitly reproducing a known failure.
- Do not re-enable `TKUEvidenceStarmapCompat`, `TKUEvidenceStartBorderCompat`, `TKUEvidenceBoundsPawn`, or `TKUEvidenceCurrentPawnBounds`.
- Do not create another pawn-only bounds patch.
- Do not directly restore old TKU `StarMap.umap`, `StarMapActor`, `StarSystemBody`, `StarMapPawn`, `BaseStarMapBorderActor`, or dated border actors.
- Do not import the raw original TKU DataTable as the first editor import.
- Do not run the cluster migration utility on live assets blindly.
- Do not package before the editor-created target, DataTable import, row verification, build manifest, and rollback plan exist.

## Short Continuation Prompt

Continue the MW5 TKU compatibility work from `D:\Downloads\OneDrive\Documents\code\tku-update`. The stable runtime floor is `TKUEvidenceCorePluginOnly` only. The next required gate is manual MW5 Mod Editor creation of `TKUCompatEditorPatch`, followed by filesystem inspection and a mod-owned `MW5_InnerSphereData` DataTable import test using the merged current-plus-TKU-additions CSV. Do not build or package until row verification and a build manifest exist. Preserve all original paks and avoid quarantined failed builds as sources.
