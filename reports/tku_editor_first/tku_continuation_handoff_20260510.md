# TKU Continuation Handoff - 2026-05-10

This handoff exists to survive context-window loss. It records the current evidence state, safety boundaries, active profile, ruled-out branches, and a continuation prompt for a fresh Codex session using GPT-5.5 with extra-high reasoning.

## Workspace

- Project workspace: `D:\Downloads\OneDrive\Documents\code\tku-update`
- Game install root: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries`
- MW5 Mod Editor: `E:\Games\MechWarrior5Editor`
- Editor project: `E:\Games\MechWarrior5Editor\MW5Mercs\MW5Mercs.uproject`
- Editor command binary: `E:\Games\MechWarrior5Editor\Engine\Binaries\Win64\UE4Editor-Cmd.exe`
- UnrealPak binary: `E:\Games\MechWarrior5Editor\Engine\Binaries\Win64\UnrealPak.exe`
- FModel: `C:\Program Files\fmodel`
- UEViewer/umodel: `C:\Program Files\umodel`
- Blender 5.1 with Unreal PSK/PSA addon: `C:\Program Files\Blender Foundation\Blender 5.1`
- UAssetAPI/MW5AssetTool: `D:\Downloads\OneDrive\Documents\code\tku-update\tools\MW5AssetTool`
- UAssetGUI: `C:\Program Files\UassetGUI`
- UE4SS v3.0.1 dev extraction: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Binaries\Win64`
- Original restored TKU mod folder: `MW5Mercs\Mods\TheKnownUniverse`
- Original TKU mod pak: `MW5Mercs\Mods\TheKnownUniverse\Paks\TheKnownUniverse.pak`
- Original loose required override pak: `MW5Mercs\Content\Paks\MW5Mercs-zKnownUniverseStarmap.pak`
- Failed blind builds quarantine: `codex_quarantine\tku_failed_compat_20260510`

## Current Active Runtime State

- `MW5Mercs\Mods\modlist.json` currently enables only `TKUEvidenceCorePluginOnly`.
- `TheKnownUniverse`, `TKUEvidenceStarmapCompat`, `TKUEvidenceStartBorderCompat`, `TKUEvidenceBoundsPawn`, and `TKUEvidenceCurrentPawnBounds` are disabled.
- The current live game process, if still open from the last test, was launched with the failed `TKUEvidenceCurrentPawnBounds` profile. Close and relaunch before trusting current `modlist.json`.
- Saved stable profile: `MW5Mercs\Mods\modlist.profile-tku-evidence-core-after-current-pawn-bounds-fail-20260510.json`
- Re-verified on 2026-05-10 at approximately 21:35 Australia/Brisbane time: live `modlist.json` still enables only `TKUEvidenceCorePluginOnly`, and no MW5 or MW5 Mod Editor process was running.
- Re-verified again on 2026-05-10 at approximately 22:30 Australia/Brisbane time: live `modlist.json` still enables only `TKUEvidenceCorePluginOnly`, and no MW5 or MW5 Mod Editor process was running.
- Re-verified again on 2026-05-10 at approximately 23:55 Australia/Brisbane time: live `modlist.json` still enables only `TKUEvidenceCorePluginOnly`, and the process query returned no MW5 or UE4 editor process entries.

## Clean Source Facts

- The user restored the original Nexus `TheKnownUniverse` folder and original `MW5Mercs-zKnownUniverseStarmap.pak`.
- Original TKU build 38 `TheKnownUniverse.pak` SHA256: `0F23FC683DEBEC27D07FF6739137BA1E4069934082D5AFFF6B3F2161CC64C678`
- Original loose starmap pak SHA256: `DFAC2CA2E1DEDCD96709A95A778DA1BB55EB02BB87E9E62B7DFC8320DD9F1FCB`
- The loose starmap pak contains `/Game/CustomContent/*`, `/Game/InnerSphereData/MW5_InnerSphereData.uasset/.uexp`, and `/Game/Levels/FrontEnd/StarMap.umap/.uexp`.
- The loose starmap pak is not fatal by itself: with zero enabled mods, Davion career, vanilla starmap, and mechbay loaded.
- Original TKU mod pak is sufficient to reproduce the new-career post-load fatal crash, even with the loose override disabled.

## Runtime Results So Far

- Original TKU-only failure: Single Player -> New Career -> Davion -> loading completes -> fatal before gameplay. Crash: `EXCEPTION_ACCESS_VIOLATION reading address 0x000000000000004c`, hash `0039C4B8A7510FAC9074DFC881C752315D75F42F`.
- Same fatal reproduced with the intended stack minus `vonBiomes`, so `vonBiomes` is not sufficient to explain the crash.
- `TKUEvidenceStarmapCompat`: replaced only TKU `StarMapActor` and `StarSystemBody` with current vanilla assets on top of original TKU. Result: hard loading stall, no fresh crash folder. It implicated the stale starmap class pair but did not produce a viable patch.
- `TKUEvidenceStartBorderCompat`: reasserted current vanilla `Borders3015`, `AllStarMapBorderChanges`, and `BaseStarMapBorderActor`. Result: fatal `Could not find SuperStruct BaseStarMapBorderActor_C to create StarMapActor_2570_C`. Direct cooked border substitution is unsafe.
- `TKUEvidenceCorePluginOnly`: stripped all 282 root `/Game` substitutions from original TKU and kept plugin content only. Result: career and starmap loaded, contracts/travel/save basic checks passed, Steiner ownership restored. Limitation: map bounds stayed vanilla and territory overlay remained incomplete/vanilla-like.
- `TKUEvidenceBoundsPawn`: restored only original TKU cooked `StarMapPawn` on top of core plugin-only. Result: career loaded, but pressing starmap entered first-person hangar view.
- `TKUEvidenceCurrentPawnBounds`: started from current vanilla `StarMapPawn`, preserved current references, changed serialized pan/zoom defaults to TKU values. Result: career loaded, but pressing starmap again entered first-person hangar view. Cooked `StarMapPawn` substitution is ruled out.

## Evidence-Based Conclusions

- The old blind-build strategy was weak because cooked UE4 assets hide Blueprint graphs, CDO defaults, construction scripts, parent-class assumptions, data table row schemas, and level references behind coarse package paths. Path-level pak manifests are not enough to reason safely about behavior.
- Original TKU root `/Game` substitutions are unsafe as a group. They include stale starmap classes, stale border parents, old root faction/employer data, and old map/data assets.
- The stable floor is plugin content from TKU plus no root `/Game` substitutions: `TKUEvidenceCorePluginOnly`.
- The remaining missing functionality is not "TKU is absent"; plugin-only restored enough to load and recover some ownership. The missing pieces are current-compatible expanded starmap bounds and full territory overlay/minor-power rendering.
- Direct cooked substitutions are now ruled out for `BaseStarMapBorderActor`, dated border assets, old `StarMapActor`, old `StarSystemBody`, old `StarMap.umap`, old root faction/employer data as a group, and both old/current cooked `StarMapPawn` variants.
- Next changes must be produced through the MW5 Mod Editor or a clearly validated UE4.27-compatible asset-editing workflow, not byte-patched cooked paks.
- `ue4_mod_entry_creation_probe_20260510` proves `MWModUtils.create_mod_entry` is only a transient editor-entry helper in commandlet context: it returned successfully but created no mod/plugin filesystem scaffold.
- `ue4_asset_authoring_api_stub_probe_20260510` found the generated editor Python stub exposes likely post-target authoring APIs: `EditorAssetLibrary.duplicate_asset`, `DataTableFunctionLibrary.fill_data_table_from_csv_file`, and `EditorAssetLibrary.save_asset`. This supports a controlled mod-owned DataTable import later, but it does not replace the MW5 Mod Editor UI Create Mod gate.
- `editor_gui_launch_attempt_20260510` records that Codex could not expose a usable MW5 Mod Editor GUI window from this session. Direct launch produced process `41600` and the generated stub, but `MainWindowHandle` stayed `0`; Explorer association did not start `UE4Editor`. The first `Create Mod` gate is therefore waiting on manual interactive user action.

## Important Asset Findings

- Loose override `StarMap.umap` hard-references current `/Game/UI/FrontEnd/Starmap/StarMapActor` and `/Game/UI/FrontEnd/Starmap/StarSystemBody`.
- Original TKU mod-pak `StarMap.umap` hard-references `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarMapActor` and `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarSystemBody`.
- Current vanilla `StarSystemBody` imports `/Script/MechWarrior.MWClusterDataAsset` and exports `ResetClusterMeshes`, `GetClusterOverlayMesh`, and `GetClusterConstellationMesh`.
- Original TKU `StarSystemBody` lacks `MWClusterDataAsset` and those cluster-mesh exports.
- `StarMapActor_2570_C` is not the frontend starmap actor; it is a vanilla HoloTable border blueprint parented to `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor_C`.
- Current vanilla dated border actors also inherit current root `BaseStarMapBorderActor_C`. TKU's stale root `BaseStarMapBorderActor` can break vanilla HoloTable/border children.
- Current vanilla `Borders3015` points to `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/StarMapBorderActor3015_C`; TKU `Borders3015` points to `/TheKnownUniverse/2864-01-01/StarMapBorderActor2864-01-01`.
- Current vanilla `StarMapPawn` defaults: `PanBoundsHorizontal=5500`, `PanBoundsVertical=4500`, `ZoomDistanceList=[400,550,700,1400,1600,1800,3500]`, `ZoomLevelThresholds=[2000,1000]`.
- Original TKU `StarMapPawn` defaults: `PanBoundsHorizontal=8500`, `PanBoundsVertical=16000`, `ZoomDistanceList=[300,600,900,1300,1800,2200,2800,3500,5000,7500,9000]`, `ZoomLevelThresholds=[3500,1000]`.
- Editor source `Content\Data\InnerSphereMap\MW5_InnerSphereData.json` has 3,446 systems and wide coordinates, including Clan-homeworld scale.
- Runtime/editor `Content\InnerSphereData\MW5_InnerSphereData.csv/uasset` has 2,173 vanilla-scale rows.
- Current editor has 261 assets under `/Game/Campaign/Clusters`, including 79 `MWClusterDataAsset` assets.
- Original TKU has no `/Game/Campaign/Clusters` assets and no scanned `MWClusterDataAsset` strings.
- Current cluster assets expose `system_ids`, `cluster_faction_asset`, `cluster_overlay`, and `cluster_constellation`.
- Current editor utility `/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets` appears designed to migrate old InnerSphere/PlaceCluster data into `MWClusterDataAsset` files.
- `starmap_generation_trace_20260510` recovered the current level placement formula exactly: `LevelX = 51336 + 8 * PosY` and `LevelY = 51039 + 8 * PosX`.
- The original TKU cooked `/Game/InnerSphereData/MW5_InnerSphereData` parse recovered 3,929 rows, 1,091 clustered rows, 69 unique cluster IDs, 103 overlay rows, and 38 constellation rows from the restored original TKU pak.
- The parser now preserves UE4 `FName` numeric enum suffixes for current-compatible values such as `C_8` and `H_0`; a prior collapsed `C`/`H` display bug was fixed before import candidate generation.
- Original TKU projected through the current placement formula spans about level X `35305..66633` and level Y `36020..66538`, roughly 3.6x / 3.2x the current placed-body half-span.
- The repair-candidate manifest found 134 unique old TKU overlay/constellation soft paths. Only 20 resolve to loose editor assets; 114 are absent from loose editor content, the current base game pak, and original TKU pak. Treat those old paths as deprecated migration clues, not direct asset dependencies to restore.
- The manifest found `RepairSystem` is a legacy generic TKU cluster ID that splits across 32 current CSV cluster targets, while `CareerCluster` maps to current rows with no active CSV cluster. `ClanConflict`, `RepairSystem_Clan`, `RepairSystem_Custom`, and `PirateKingdoms` have TKU rows missing from the current runtime CSV.
- The InnerSphere import candidate report produced a raw original-TKU current-schema CSV and a safer merged current-plus-TKU-additions CSV. The merged candidate preserves 2,173 current rows, adds 1,801 TKU-only rows, retains 45 current-only rows, totals 3,974 rows, and is currently the preferred first editor data candidate.

## Key Reports And Tools

- Roadmap: `TKU_COMPAT_PATCH_ROADMAP.md`
- Editor-first strategy: `reports\tku_editor_first_strategy.md`
- Runtime isolation: `reports\tku_runtime_isolation_20260510.md`
- Reference manifest: `reports\tku_editor_first\reference_trace_manifest.md`
- Core plugin-only evidence: `reports\tku_editor_first\tku_evidence_core_plugin_only_20260510.md`
- Old pawn evidence: `reports\tku_editor_first\tku_evidence_bounds_pawn_20260510.md`
- Current pawn evidence: `reports\tku_editor_first\tku_evidence_current_pawn_bounds_20260510.md`
- UE4 editor API probe: `reports\tku_editor_first\ue4_modding_api_probe.md`
- Focused MW5 mod type/API probe: `reports\tku_editor_first\ue4_mod_types_probe.md`
- Focused MW5 mod type/API probe JSON: `reports\tku_editor_first\ue4_mod_types_probe.json`
- Focused starmap bounds and cluster probe: `reports\tku_editor_first\ue4_starmap_bounds_clusters_probe.md`
- Focused starmap bounds and cluster probe JSON: `reports\tku_editor_first\ue4_starmap_bounds_clusters_probe.json`
- Current repair-track decision: `reports\tku_editor_first\tku_repair_track_decision_20260510.md`
- Current repair-track decision JSON: `reports\tku_editor_first\tku_repair_track_decision_20260510.json`
- Starmap generation trace: `reports\tku_editor_first\starmap_generation_trace_20260510.md`
- Starmap generation trace JSON: `reports\tku_editor_first\starmap_generation_trace_20260510.json`
- Original TKU InnerSphere DataTable parse: `reports\tku_editor_first\original_tku_inner_sphere_datatable_rows_20260510.md`
- Original TKU InnerSphere DataTable parse JSON/CSV: `reports\tku_editor_first\original_tku_inner_sphere_datatable_rows_20260510.json`, `reports\tku_editor_first\original_tku_inner_sphere_datatable_rows_20260510.csv`
- Editor repair candidate manifest: `reports\tku_editor_first\tku_editor_repair_candidate_manifest_20260510.md`
- Editor repair candidate manifest JSON: `reports\tku_editor_first\tku_editor_repair_candidate_manifest_20260510.json`
- Editor mod target status: `reports\tku_editor_first\editor_mod_target_status_20260510.md`
- Editor mod target status JSON: `reports\tku_editor_first\editor_mod_target_status_20260510.json`
- InnerSphere import candidates: `reports\tku_editor_first\tku_inner_sphere_import_candidates_20260510.md`
- InnerSphere import candidates JSON: `reports\tku_editor_first\tku_inner_sphere_import_candidates_20260510.json`
- InnerSphere import candidate CSVs: `reports\tku_editor_first\tku_inner_sphere_raw_original_current_schema_20260510.csv`, `reports\tku_editor_first\tku_inner_sphere_merged_current_plus_tku_additions_20260510.csv`
- Editor authoring runbook: `reports\tku_editor_first\editor_authoring_runbook_20260510.md`
- Editor authoring runbook JSON: `reports\tku_editor_first\editor_authoring_runbook_20260510.json`
- Mod entry creation probe: `reports\tku_editor_first\ue4_mod_entry_creation_probe_20260510.md`
- Mod entry creation probe JSON: `reports\tku_editor_first\ue4_mod_entry_creation_probe_20260510.json`
- Asset authoring API stub probe: `reports\tku_editor_first\ue4_asset_authoring_api_stub_probe_20260510.md`
- Asset authoring API stub probe JSON: `reports\tku_editor_first\ue4_asset_authoring_api_stub_probe_20260510.json`
- Editor GUI launch attempt: `reports\tku_editor_first\editor_gui_launch_attempt_20260510.md`
- Editor GUI launch attempt JSON: `reports\tku_editor_first\editor_gui_launch_attempt_20260510.json`
- Cooked package reference parser: `tools\tku_reference_audit\parse_ue4_package_refs.py`
- Core plugin builder: `tools\tku_reference_audit\build_tku_evidence_core_plugin_only.py`
- Current pawn builder, now ruled out: `tools\tku_reference_audit\build_tku_evidence_current_pawn_bounds_patch.py`
- Editor API probe script: `tools\tku_reference_audit\ue4_dump_modding_apis.py`
- Focused MW5 mod type/API probe script: `tools\tku_reference_audit\ue4_probe_mod_types.py`
- Focused starmap bounds and cluster probe script: `tools\tku_reference_audit\ue4_probe_starmap_bounds_clusters.py`
- Starmap generation trace script: `tools\tku_reference_audit\ue4_probe_starmap_generation_trace.py`
- Original TKU InnerSphere DataTable parser: `tools\tku_reference_audit\parse_original_tku_inner_sphere_datatable.py`
- Editor repair candidate manifest builder: `tools\tku_reference_audit\plan_tku_editor_repair_candidate.py`
- Editor mod target inspector: `tools\tku_reference_audit\inspect_editor_mod_targets.py`
- InnerSphere import candidate builder: `tools\tku_reference_audit\build_tku_inner_sphere_import_candidates.py`
- Mod entry creation probe script: `tools\tku_reference_audit\ue4_probe_mod_entry_creation.py`

## Next Workstream

1. Do not launch another runtime test until there is a new evidence-authored patch candidate. The active profile is verified as core-only.
2. The focused `ue4_mod_types_probe` found `MWModPluginInfo`, `ModPackageArgs`, `MWModUtils`, and `MWModEditorWidget.package_mod(args)`, but no direct module-level `CreateMod`, `SaveToMod`, `SaveTo`, or `PackageMod` symbol.
3. `MWModEditorWidget` is abstract from commandlet construction, and the commandlet saw no active mod plugin. Treat Python-only MW5 mod creation and `Save To Mod` as not proven.
4. `ue4_mod_entry_creation_probe_20260510` proved `MWModUtils.create_mod_entry` can return a transient entry but does not create mod/plugin folders or a proper editor mod target on disk.
5. `ue4_asset_authoring_api_stub_probe_20260510` found likely Python APIs for mod-owned asset duplication, CSV DataTable fill, and save once a real target exists.
6. `editor_gui_launch_attempt_20260510` found Codex cannot currently expose a usable MW5 Mod Editor GUI window from this session. The user must manually open the editor and create `TKUCompatEditorPatch`.
7. Use editor commandlet Python for non-mutating inspection/export. Use the MW5 Mod Editor UI for first safe `Create Mod` / `Save To Mod` authoring unless a later widget-spawn or AutomationTool workflow is proven separately.
8. `ue4_starmap_bounds_clusters_probe` found current `/Game/Levels/FrontEnd/StarMap` has 2,182 actors, including 2,172 `StarSystemBody_C` actors, while the wide source JSON has 3,446 systems and the runtime CSV has 2,173 rows. Do not assume another pawn-only bounds edit can restore the TKU map.
9. Next bounds work should inspect `StarMapActor`, `StarMap.umap` generation/placement, source-to-runtime InnerSphere data import, placed actors, world settings, and native/default settings before authoring any build.
10. The same probe found 79 current `MWClusterDataAsset` assets, 815 total system memberships, 74 overlay meshes, and 31 constellation meshes. Separately inspect the modern cluster overlay path; the likely full-overlay repair is current-schema `MWClusterDataAsset` creation or migration from TKU source/old table data, not restoring old cooked territory/border assets.
11. Treat map bounds and territory overlays as separate features unless editor evidence proves they share the same asset.
12. Use `original_tku_inner_sphere_datatable_rows_20260510.csv` as the clean-source TKU row evidence for data import planning. Do not import the old cooked DataTable directly.
13. Use `tku_editor_repair_candidate_manifest_20260510` as the current authoring gate. It does not authorize a runtime pak yet; it authorizes planning a dedicated editor mod and resolving cluster mapping policy first.
14. `editor_mod_target_status_20260510` found no existing dedicated TKU compatibility editor mod. The MW5 Mod Editor UI must create the first safe mod target unless a later scripted Create Mod path is proven.
15. Use the merged current-plus-TKU-additions CSV as the preferred first data candidate for editor import planning, because it preserves current 1.13 rows while adding TKU-only systems.
16. Follow `editor_authoring_runbook_20260510` for the first mutating editor session. It still keeps `build_authorized=false`; it only defines the manual Create Mod / Save To Mod gate and the first asset candidates.

## Safety Boundaries

- Do not overwrite, delete, or edit original TKU paks.
- Do not delete or modify the original loose `MW5Mercs-zKnownUniverseStarmap.pak`.
- Do not use quarantined blind-build artifacts as source.
- Do not restore root `/Game` TKU assets wholesale.
- Do not re-enable `TheKnownUniverse`, `TKUEvidenceStarmapCompat`, `TKUEvidenceStartBorderCompat`, `TKUEvidenceBoundsPawn`, or `TKUEvidenceCurrentPawnBounds` unless explicitly doing a documented rollback/reproduction.
- Do not install or download additional third-party tools without user approval. FModel at `C:\Program Files\fmodel`, UEViewer/umodel at `C:\Program Files\umodel`, Blender 5.1 at `C:\Program Files\Blender Foundation\Blender 5.1`, UAssetAPI/MW5AssetTool at `D:\Downloads\OneDrive\Documents\code\tku-update\tools\MW5AssetTool`, UAssetGUI at `C:\Program Files\UassetGUI`, UE4SS v3.0.1 extracted in `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Binaries\Win64`, and the MW5 Mod Editor at `E:\Games\MechWarrior5Editor` are already available and their use is encouraged for evidence gathering where appropriate. Prefer the MW5 Mod Editor for authoritative asset repair and authoring.
- Keep all temporary outputs in `reports\tku_editor_first`, `tools\tku_reference_audit`, or new clearly named test mod folders.
- Use UE4.27 documentation and MW5 Mod Editor behavior as the Unreal source of truth.
- Preserve rollback profiles before every runtime test.

## Continuation Prompt

```text
You are Codex running as GPT-5.5 with reasoning effort set to extra high. Continue the MW5 TheKnownUniverse compatibility project from an evidence-first, editor-first strategy. Work until the goal is achieved: a stable local compatibility patch/mod that preserves TKU functionality on current MW5 v1.13.378 with the user's intended mod stack, including Yet Another MechLab family and vonBiomes, without breaking BattleFXEnhanced compatibility.

Workspace:
- Project workspace: `D:\Downloads\OneDrive\Documents\code\tku-update`
- Game install root: E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries
- MW5 Mod Editor: E:\Games\MechWarrior5Editor
- Editor project: E:\Games\MechWarrior5Editor\MW5Mercs\MW5Mercs.uproject
- Editor command binary: E:\Games\MechWarrior5Editor\Engine\Binaries\Win64\UE4Editor-Cmd.exe
- UnrealPak: E:\Games\MechWarrior5Editor\Engine\Binaries\Win64\UnrealPak.exe
- FModel: C:\Program Files\fmodel
- UEViewer/umodel: C:\Program Files\umodel
- Blender 5.1 with Unreal PSK/PSA addon: C:\Program Files\Blender Foundation\Blender 5.1
- UAssetAPI/MW5AssetTool: D:\Downloads\OneDrive\Documents\code\tku-update\tools\MW5AssetTool
- UAssetGUI: C:\Program Files\UassetGUI
- UE4SS v3.0.1 dev extraction: E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Binaries\Win64

Read first, before changing anything:
- TKU_COMPAT_PATCH_ROADMAP.md
- reports\tku_editor_first_strategy.md
- reports\tku_editor_first\tku_continuation_handoff_20260510.md
- reports\tku_runtime_isolation_20260510.md
- reports\tku_editor_first\reference_trace_manifest.md
- reports\tku_editor_first\ue4_modding_api_probe.md
- reports\tku_editor_first\tku_evidence_core_plugin_only_20260510.md
- reports\tku_editor_first\tku_evidence_bounds_pawn_20260510.md
- reports\tku_editor_first\tku_evidence_current_pawn_bounds_20260510.md

Current active profile:
- MW5Mercs\Mods\modlist.json should enable only TKUEvidenceCorePluginOnly.
- The running game, if still open, may have been launched under the failed TKUEvidenceCurrentPawnBounds profile. Close/relaunch before trusting runtime behavior.

Clean source and preservation rules:
- Use restored original Nexus TKU files as source: MW5Mercs\Mods\TheKnownUniverse and MW5Mercs\Mods\TheKnownUniverse\Paks\TheKnownUniverse.pak.
- The loose required pak MW5Mercs\Content\Paks\MW5Mercs-zKnownUniverseStarmap.pak is original and must not be edited.
- Preserve the original game install and all original mod backups. Do not delete or overwrite originals.
- Do not use quarantined blind-build artifacts as source evidence.
- Keep temp outputs in reports\tku_editor_first, tools\tku_reference_audit, or clearly named new test mod folders.

Known runtime evidence:
- Original TKU mod pak alone is sufficient to reproduce the new-career post-loading fatal crash: EXCEPTION_ACCESS_VIOLATION reading address 0x000000000000004c, hash 0039C4B8A7510FAC9074DFC881C752315D75F42F.
- The loose starmap override pak is not fatal by itself.
- vonBiomes is not sufficient to explain the crash.
- TKUEvidenceCorePluginOnly is the current stable floor: it strips all root /Game substitutions from original TKU and keeps plugin content. It loads career/starmap, recovers some ownership including Steiner, supports basic travel/contracts/save, but leaves vanilla map bounds and incomplete/vanilla-like territory overlay.
- TKUEvidenceStarmapCompat converted fatal crash into a loading stall; disabled.
- TKUEvidenceStartBorderCompat reproduced BaseStarMapBorderActor_C superstruct fatal; disabled.
- TKUEvidenceBoundsPawn and TKUEvidenceCurrentPawnBounds both caused the starmap button to enter first-person hangar view; disabled. Cooked StarMapPawn substitution is ruled out.

Important conclusions:
- Stop blind build toggling. Cooked UE4 path-level pak surgery is too coarse because Blueprint graphs, CDO defaults, parent assumptions, data schemas, level actors, and construction logic are hidden.
- Direct cooked substitutions are ruled out for old TKU StarMap.umap, StarMapActor, StarSystemBody, StarMapPawn, BaseStarMapBorderActor, dated border assets, and old root faction/employer data as a group.
- The next patch must be editor-authored or created via validated MW5 Mod Editor/UE4.27 tooling.
- Use UE4.27 documentation and observed MW5 Mod Editor APIs as the Unreal source of truth.

Immediate next task:
1. Verify active modlist and whether MW5/UE4Editor is still running.
2. Read the newest evidence: starmap_generation_trace_20260510, original_tku_inner_sphere_datatable_rows_20260510, tku_editor_repair_candidate_manifest_20260510, editor_mod_target_status_20260510, and tku_inner_sphere_import_candidates_20260510.
3. No dedicated editor-authored compatibility mod currently exists. Use the MW5 Mod Editor UI for first Create Mod / Save To Mod authoring; commandlet Python has not proven safe for creation/package.
4. Prepare a precise editor-authoring checklist for importing the merged current-plus-TKU-additions DataTable candidate and regenerating/copying StarMap level actors using current StarSystemBody_C and the recovered placement formula. Do not mutate editor assets until the target mod path and rollback plan are explicit.
5. Resolve cluster mapping policy before writing any MWClusterDataAsset assets: legacy TKU RepairSystem splits across many current RepairSystem_* clusters, CareerCluster is generic, and ClanConflict/RepairSystem_Clan rows are absent from current runtime CSV.
6. Do not build another runtime pak until a specific editor-authored asset set and dependency manifest are documented.

Likely repair tracks after current evidence:
- Track B2: editor-author/current StarMapActor, StarMap.umap, world settings, placed actors, native/default settings, or generation data controlling map movement bounds. Current placement formula is known: LevelX = 51336 + 8 * PosY, LevelY = 51039 + 8 * PosX.
- Track A1: rebuild full territory overlay through current MWClusterDataAsset assets. Use original TKU DataTable rows as membership evidence, but treat old overlay/constellation paths as deprecated clues because most are absent from current content.
- Track C: reparent/recreate TKU dated border actors only if the editor proves current parents and dependencies are safe.
- Track B1 is currently deprioritized: both cooked old pawn and current-package pawn CDO patches misrouted the starmap button into first-person hangar view.

Testing gates:
- Before every runtime test, save a modlist profile and record exactly which mods are enabled.
- First success gate: career loads, mechbay opens, starmap opens from hangar UI, no first-person-hangar misroute.
- Bounds gate: map can pan beyond vanilla limits far enough to inspect TKU/Clan regions.
- Overlay gate: major and minor territories render, not just the vanilla five majors plus ComStar.
- Ownership gate: Steiner/Lyran and minor powers show correct system owners.
- Stability gate: multiple jumps, contracts, conflict zones, industrial hubs, rare mechs, save/load.
- Stack gate: add intended mods incrementally, including Yet Another MechLab family, vonBiomes, and BattleFXEnhanced.

Be rigorous and skeptical. Prefer recorded evidence over intuition. If a proposed rebuild is not justified by a specific asset-reference or editor-inspection finding, do not build it. Update the roadmap and handoff reports as new facts are learned.
```


