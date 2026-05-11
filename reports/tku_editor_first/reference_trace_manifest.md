# TKU Editor-First Reference Trace Manifest

## Source Discipline

- Original TKU evidence source: `MW5Mercs\Mods\TheKnownUniverse`
- Original TKU mod build: build 38
- Original TKU pak: `MW5Mercs\Mods\TheKnownUniverse\Paks\TheKnownUniverse.pak`
- Original TKU pak SHA256: `0F23FC683DEBEC27D07FF6739137BA1E4069934082D5AFFF6B3F2161CC64C678`
- Restored live TKU folder: `MW5Mercs\Mods\TheKnownUniverse`
- Failed blind-build artifacts: quarantined under `codex_quarantine\tku_failed_compat_20260510`
- Rule: use restored build-38 files for TKU evidence. Use quarantined blind-build artifacts only to document failed history, not as source evidence.

## Editor Baseline

- MW5 Mod Editor root: `E:\Games\MechWarrior5Editor`
- Project: `E:\Games\MechWarrior5Editor\MW5Mercs\MW5Mercs.uproject`
- Project SHA256: `A66A2197DF7AE9780A648735520884D04A7BDB2CCE656E324E9ECD5AC4EBAEAB`
- Editor binaries found:
- `E:\Games\MechWarrior5Editor\Engine\Binaries\Win64\UE4Editor.exe`
- `E:\Games\MechWarrior5Editor\Engine\Binaries\Win64\UE4Editor-Cmd.exe`
- `E:\Games\MechWarrior5Editor\Engine\Binaries\Win64\UnrealPak.exe`
- Project plugins include `PythonScriptPlugin` and `EditorScriptingUtilities`, so command-line editor inspection may be possible after approval if it needs to write editor logs/cache.
- Local inspection tools also available and encouraged for supporting evidence:
  - `C:\Program Files\fmodel`
  - `C:\Program Files\umodel`
  - `C:\Program Files\Blender Foundation\Blender 5.1` with the Unreal PSK/PSA addon
  - `D:\Downloads\OneDrive\Documents\code\tku-update\tools\MW5AssetTool`
  - `C:\Program Files\UassetGUI`
  - UE4SS v3.0.1 dev build extracted from `zDEV-UE4SS_v3.0.1.zip` in `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Binaries\Win64`
- Treat FModel, umodel, Blender, UAssetAPI/MW5AssetTool, UAssetGUI, and UE4SS output as supporting cooked-asset/reference/visual/runtime evidence unless separately validated; prefer MW5 Mod Editor behavior for authoritative repair decisions.

## Local Evidence Outputs

- TKU cooked asset scan: `reports\tku_editor_first\tku_cooked_asset_string_scan.md`
- TKU cooked asset scan JSON: `reports\tku_editor_first\tku_cooked_asset_string_scan.json`
- Vanilla editor asset scan: `reports\tku_editor_first\vanilla_editor_asset_string_scan.md`
- Vanilla editor asset scan JSON: `reports\tku_editor_first\vanilla_editor_asset_string_scan.json`
- Editor InnerSphere source analysis: `reports\tku_editor_first\editor_inner_sphere_source_analysis.md`
- Editor InnerSphere source analysis JSON: `reports\tku_editor_first\editor_inner_sphere_source_analysis.json`
- Original clean TKU pak inventory: `reports\tku_editor_first\original_tku_pak_inventory.md`
- Original clean TKU pak inventory JSON: `reports\tku_editor_first\original_tku_pak_inventory.json`
- Cluster migration input analysis: `reports\tku_editor_first\cluster_migration_inputs.md`
- Cluster migration input analysis JSON: `reports\tku_editor_first\cluster_migration_inputs.json`
- MW5 editor asset dump: `reports\tku_editor_first\ue4_editor_asset_dump.md`
- MW5 editor asset dump JSON: `reports\tku_editor_first\ue4_editor_asset_dump.json`
- Cooked UE4 package reference parse: `reports\tku_editor_first\tku_cooked_package_refs.md`
- Cooked UE4 package reference parse JSON: `reports\tku_editor_first\tku_cooked_package_refs.json`
- Structured reference findings: `reports\tku_editor_first\tku_structured_reference_findings_20260510.md`
- Evidence starmap class compat build rationale: `reports\tku_editor_first\tku_evidence_starmap_class_patch_20260510.md`
- Evidence starmap class compat build JSON: `reports\tku_editor_first\tku_evidence_starmap_class_patch_20260510.json`
- Evidence start-border compat build rationale: `reports\tku_editor_first\tku_evidence_start_border_patch_20260510.md`
- Evidence start-border compat build JSON: `reports\tku_editor_first\tku_evidence_start_border_patch_20260510.json`
- Focused starmap/border editor inspection: `reports\tku_editor_first\ue4_starmap_border_path_inspection.md`
- Focused starmap/border editor inspection JSON: `reports\tku_editor_first\ue4_starmap_border_path_inspection.json`
- Evidence core plugin-only build rationale: `reports\tku_editor_first\tku_evidence_core_plugin_only_20260510.md`
- Evidence core plugin-only build JSON: `reports\tku_editor_first\tku_evidence_core_plugin_only_20260510.json`
- Evidence bounds pawn build rationale: `reports\tku_editor_first\tku_evidence_bounds_pawn_20260510.md`
- Evidence bounds pawn build JSON: `reports\tku_editor_first\tku_evidence_bounds_pawn_20260510.json`
- Evidence current pawn bounds build rationale: `reports\tku_editor_first\tku_evidence_current_pawn_bounds_20260510.md`
- Evidence current pawn bounds build JSON: `reports\tku_editor_first\tku_evidence_current_pawn_bounds_20260510.json`
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
- Scan tools:
- `tools\tku_reference_audit\extract_asset_strings.py`
- `tools\tku_reference_audit\scan_loose_editor_asset_strings.py`
- `tools\tku_reference_audit\analyze_editor_inner_sphere_sources.py`
- `tools\tku_reference_audit\inventory_original_tku_pak.py`
- `tools\tku_reference_audit\analyze_cluster_migration_inputs.py`
- `tools\tku_reference_audit\ue4_dump_assets.py`
- `tools\tku_reference_audit\parse_ue4_package_refs.py`
- `tools\tku_reference_audit\build_tku_evidence_starmap_class_patch.py`
- `tools\tku_reference_audit\build_tku_evidence_start_border_patch.py`
- `tools\tku_reference_audit\ue4_probe_mod_types.py`
- `tools\tku_reference_audit\ue4_probe_starmap_bounds_clusters.py`
- `tools\tku_reference_audit\ue4_probe_starmap_generation_trace.py`
- `tools\tku_reference_audit\parse_original_tku_inner_sphere_datatable.py`
- `tools\tku_reference_audit\plan_tku_editor_repair_candidate.py`
- `tools\tku_reference_audit\inspect_editor_mod_targets.py`
- `tools\tku_reference_audit\build_tku_inner_sphere_import_candidates.py`
- `tools\tku_reference_audit\ue4_probe_mod_entry_creation.py`

## Current Findings

- The original TKU pak is uncompressed and readable by local pak tooling. Selected cooked assets can be scanned safely without extracting loose files into the game or editor install.
- Runtime isolation on 2026-05-10 showed the loose required override pak is not fatal by itself: with zero enabled mods, a Davion career, vanilla starmap, and mechbay loaded successfully.
- Runtime isolation on 2026-05-10 showed `vonBiomes` is not sufficient to explain the current fatal crash: the same `0x4C` call-stack hash reproduced with `vonBiomes` disabled.
- The current fatal crash target is therefore TKU's mod pak content or the interaction between TKU's mod pak content and the loose override pak.
- Vanilla editor assets are available as loose editor-readable project assets, including `StarMap.umap`, `StarMapActor`, `StarMapPawn`, `StarSystemBody`, `BaseStarMapBorderActor`, faction materials, and InnerSphere data.
- Vanilla `StarMap.umap`, `StarMapActor`, `StarMapPawn`, and `StarSystemBody` expose clean `/Game/...` package references in string scans.
- Original TKU cooked substitutions expose `/ModOverride/TheKnownUniverse/...` references in key starmap assets.
- New structured package-table parsing confirms the safe loose override and unsafe TKU mod map bind to different class packages.
- The loose `MW5Mercs-zKnownUniverseStarmap.pak` `StarMap.umap` binds to current `/Game/UI/FrontEnd/Starmap/StarMapActor` and `/Game/UI/FrontEnd/Starmap/StarSystemBody`.
- The original TKU mod pak `StarMap.umap` binds to `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarMapActor` and `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarSystemBody`.
- Current vanilla `StarSystemBody` imports `/Script/MechWarrior.MWClusterDataAsset` and exports `ResetClusterMeshes`, `GetClusterOverlayMesh`, and `GetClusterConstellationMesh`.
- Original TKU `StarSystemBody` lacks `MWClusterDataAsset` and those current cluster-mesh exports.
- TKU `StarMapActor` and `StarSystemBody` still inherit existing native parents, so the fatal path is not a simple missing parent-class error.
- The stronger current hypothesis is stale Blueprint graph/default behavior interacting with the current native starmap/cluster pipeline.
- Runtime test of `TKUEvidenceStarmapCompat` changed the failure mode from the repeated post-loading `0x4C` fatal crash to a hard loading stall with no new crash folder. A later retry of the same profile failed/terminated without creating a newer crash artifact. This implicates the old TKU `StarMapActor` / `StarSystemBody` pair, but also shows the remaining root asset mix must be traced before another build. `TKUEvidenceStarmapCompat` is disabled in the live profile.
- Follow-up tracing found active TKU `Borders3015` redirects the Davion start border actor to `/TheKnownUniverse/2864-01-01/StarMapBorderActor2864-01-01`, while current vanilla `Borders3015` points to `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/StarMapBorderActor3015`.
- TKU `StarMapBorderActor2864-01-01` depends on `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`, which matches the previous old-border superstruct failure family.
- Runtime test of `TKUEvidenceStartBorderCompat` failed with `Could not find SuperStruct BaseStarMapBorderActor_C to create StarMapActor_2570_C`; it has been disabled.
- `StarMapActor_2570` is a current vanilla HoloTable blueprint that hard-references `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`, so the border-superstruct issue is not isolated to TKU's 2864 actor.
- Focused editor inspection confirmed `StarMapActor_2570_C` is parented to `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor_C`, and all current vanilla dated border actors also inherit that current root base.
- Therefore original TKU cannot remain enabled as-is: its stale root `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor` substitution can break vanilla HoloTable/border children before any frontend starmap repair is reached.
- `TKUEvidenceCorePluginOnly` has been built from restored original build 38 with all 282 root `/Game` substitutions removed. It is the only active mod in `modlist.json` for the next gate.
- `TKUEvidenceCorePluginOnly` passed the next runtime gate: career and starmap loaded, but starmap bounds remained vanilla and territory overlay looked vanilla/incomplete.
- `TKUEvidenceBoundsPawn` was built and tested with `TKUEvidenceCorePluginOnly`. It restored only original TKU `StarMapPawn`; career loaded, but pressing the starmap button entered first-person hangar view. It is now disabled.
- `TKUEvidenceCurrentPawnBounds` was built and tested with `TKUEvidenceCorePluginOnly`. It starts from current vanilla `StarMapPawn`, preserves modern widget/tooltip references, and changes only serialized pan/zoom defaults. It reproduced the same first-person hangar behavior and is now disabled.
- On 2026-05-10, live `modlist.json` was re-verified with only `TKUEvidenceCorePluginOnly` enabled, and no MW5 or MW5 Mod Editor process was running.
- The focused non-mutating editor commandlet probe `ue4_mod_types_probe` found `MWModPluginInfo`, `ModPackageArgs`, `MWModUtils`, and `MWModEditorWidget.package_mod(args)`.
- The same probe found no direct module-level `CreateMod`, `SaveToMod`, `SaveTo`, or `PackageMod` symbol; `MWModEditorWidget` is abstract from commandlet construction; and the commandlet saw no active mod plugin entries.
- Current API evidence does not authorize Python-only creation of a proper MW5 `ModOverride` asset. Commandlet Python remains suitable for non-mutating inspection/export, while initial `Create Mod` and `Save To Mod` authoring should use the MW5 Mod Editor UI unless a later widget-spawn or AutomationTool workflow is specifically proven.
- The focused non-mutating `ue4_starmap_bounds_clusters_probe` loaded current `/Game/Levels/FrontEnd/StarMap` and found 2,182 actors, including 2,172 `StarSystemBody_C` actors.
- The same probe measured current `StarSystemBody_C` placement range at X `47144..55752` and Y `46903..56519`, while source data remains split: runtime CSV has 2,173 rows and PosX/PosY range about `-517..685` / `-524..552`, and the wide source JSON has 3,446 systems with PosX/PosY range about `-1876..1936` / `-1920..1911`.
- Current `StarMapPawn` CDO still reports `PanBoundsHorizontal=5500`, `PanBoundsVertical=4500`, `ZoomDistanceList=[400,550,700,1400,1600,1800,3500]`, and `ZoomLevelThresholds=[2000,1000]`; however the level/body-count evidence means expanded map repair is not only a pawn-bound value.
- The current `StarMapActor` CDO exposes current cluster/border surfaces such as `cluster_material`, `procedural_border_mesh`, `BorderActor=None`, and an empty default `star_system_body_look_up`, supporting a live/runtime population path that needs graph or UI inspection before authoring.
- The focused cluster probe found 79 current `MWClusterDataAsset` assets, 815 total system memberships, 74 with overlay meshes, and 31 with constellation meshes. It also confirmed `EUW_MigratePlaceClusterTOIsToClusterAssets` depends on `PlaceClusterToi_ArcAction`, `PlaceClusterToi_Config`, `/Game/InnerSphereData/MW5_InnerSphereData`, and editor scripting modules.
- Current repair decision from this evidence: bounds work should inspect `StarMapActor`, `StarMap` level generation/placement, and source-to-runtime data import before another pawn-only patch; overlay work should proceed toward current-schema `MWClusterDataAsset` migration and not old cooked border restoration.
- Original TKU `StarMap.umap` references `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarMapActor` and `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarSystemBody`.
- Original TKU `StarMapActor` references `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarMapActor` and `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarSystemBody`.
- Original TKU `StarSystemBody` references `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarMapActor` and `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarSystemBody`.
- Original TKU `StarMapPawn` references `/ModOverride/TheKnownUniverse/UI/FrontEnd/StarMapPawn` and exposes `PanBoundsHorizontal`, `PanBoundsVertical`, `ZoomDistanceList`, and `ZoomLevelThresholds`.
- Original TKU `BaseStarMapBorderActor` references `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`, matching the previous fatal error family around `BaseStarMapBorderActor_C`.
- The editor vanilla `StarMapPawn` also exposes `ZoomDistanceList` and `ZoomLevelThresholds`; therefore map movement/bounds may be ported as a modern `StarMapPawn` substitution rather than restoring old cooked TKU `StarMapPawn`.
- The editor has two relevant InnerSphere data representations:
- `Content\Data\InnerSphereMap\MW5_InnerSphereData.json` has 3,446 systems with coordinate range approximately X `-1875.94` to `1935.84` and Y `-1919.69` to `1910.76`.
- `Content\InnerSphereData\MW5_InnerSphereData.csv` has 2,173 rows with coordinate range approximately X `-517` to `685` and Y `-524` to `552`.
- The wide JSON source includes Clan homeworld entries, while the runtime-looking CSV/uasset pair is vanilla-scale. This suggests a source-generation or data-table export gap that needs editor inspection before any data rebuild.
- `Content\Data\InnerSphereMap\EmployerInfoData.csv` has 143 rows, including 24 Clan employer rows and two Lyran rows: `LA -> LyranAlliance`, `LC -> LyranCommonwealth`.
- `Content\Data\InnerSphereMap\SystemFactionChanges.json` has 3,158 parsed rows after documented UTF-16 line-ending normalization. It includes 37 Clan-related rows and 34 `CLAN` faction-code occurrences.
- The source-style data already contains the clan-homeworld and employer/faction code information needed for a modern-schema port. This weakens any argument for restoring original TKU cooked root data tables wholesale.
- `SystemFactionChanges.json` parse note: the file starts as UTF-16LE but contains malformed line endings. The analyzer repaired it by replacing byte sequence `\r\n\0` with `\n\0`, removing 57,002 bytes before JSON parsing. This repair has only been applied in report tooling, not to the editor source file.
- Original TKU build 38 has 2,709 pak entries, zero path-level `/Game/Campaign/Clusters` assets, and no scanned cooked strings mentioning `MWClusterDataAsset` or `/Game/Campaign/Clusters`.
- The only cluster-named original TKU asset path is `/Plugins/TheKnownUniverse/Content/Regions/War/CareerModeCustomClusters`, whose strings reference `PlaceClanConflict` and `PlaceCustomConflict`.
- Current MW5 editor discovery found 261 assets under `/Game/Campaign/Clusters`, including 79 `MWClusterDataAsset` assets.
- Current `MWClusterDataAsset` assets expose `system_ids`, `cluster_faction_asset`, `cluster_overlay`, and `cluster_constellation`; these are the likely modern replacement for old `InnerSphereMapData` cluster fields.
- Current editor runtime `MW5_InnerSphereData.csv` has 2,173 rows, 824 nonempty cluster rows, 77 unique nonempty cluster IDs, 74 cluster-overlay rows, and 31 cluster-constellation rows.
- The editor dump has 79 `MWClusterDataAsset` assets with 815 total system-ID memberships. This closely matches, but does not perfectly equal, the CSV cluster-field data.
- Current editor `CampaignArcs/Regions` contains 44 `Place*` assets with cluster references. Representative assets point directly at current `/Game/Campaign/Clusters/*_ClusterAsset` assets and contain `ClusterDataAsset` / `ClusterDataAssetId` strings.
- Forty-six current editor cluster IDs are visible as strings in original TKU's cooked `MW5_InnerSphereData`, including `LyranStrongholds`, `SteinerBorder`, `SteinerMarikBorder`, `TaurianCorridor`, `OutworldsBorder`, and several non-major region IDs.
- Terminal strings prove old cluster IDs and overlay mesh paths exist in TKU, but do not provide safe row-to-cluster mappings. A structured export or editor/tool-level inspection is required before creating cluster assets.
- The MW5 editor Python stub marks `InnerSphereMapData.cluster`, `cluster_overlay`, and `cluster_constellation` as deprecated and says those values should now come from a `ClusterDataAsset`.
- The editor utility `/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets` depends on `PlaceClusterToi` configs/actions and `/Game/InnerSphereData/MW5_InnerSphereData`; its embedded text says it migrates `PlaceClusterTOI_ArcAction` and InnerSphereMap data into `MWClusterDataAsset` files.
- The current vanilla `StarMap` level loaded in the editor with 2,182 actors, including 2,172 `StarSystemBody_C` actors. Its `StarSystemBody` bounds are vanilla-scale and do not cover the wide 3,446-system source JSON.
- `starmap_generation_trace_20260510` recovered the current `StarSystemBody_C` placement transform exactly: `LevelX = 51336 + 8 * PosY` and `LevelY = 51039 + 8 * PosX`.
- The same trace decoded focused metadata from `EUW_MigratePlaceClusterTOIsToClusterAssets`, `StarSystemGenerator`, `StarMapBP_UTILS`, and `StarMapActor`. It confirmed the migration utility includes operations named `Create Cluster Data Asset`, `Copy TOIData to Cluster Asset`, `Set Cluster data asset in Place Cluster TOI`, `Set Cluster System Ids EDITORONLY`, and `Copy Cluster Data from Data Row`.
- `parse_original_tku_inner_sphere_datatable.py` reads only the restored original TKU pak and recovered 3,929 rows from original TKU `/Game/InnerSphereData/MW5_InnerSphereData` with no row parse errors.
- The parser now preserves UE4 `FName` numeric suffixes for enum values such as `C_8` and `H_0`; the derived CSV is current-schema comparable.
- Original TKU InnerSphere rows span PosX about `-1877..1937` and PosY about `-2004..1912`; projected into the current level formula they span level X about `35305..66633` and level Y about `36020..66538`.
- Original TKU cluster data includes 1,091 clustered rows, 69 unique cluster IDs, 103 overlay rows, and 38 constellation rows.
- `tku_editor_repair_candidate_manifest_20260510` keeps `build_authorized=false`: it authorizes editor-authoring planning, not runtime packaging.
- The manifest found 134 unique TKU old overlay/constellation paths: 20 resolve as loose editor assets and 114 are absent from loose editor content, the current base-game pak, and the original TKU pak. These old DataTable fields should be used as migration clues, not direct dependencies to restore.
- The manifest found original TKU `RepairSystem` splits across 32 current CSV cluster targets, while `CareerCluster` maps to current rows with no active CSV cluster. `ClanConflict`, `RepairSystem_Clan`, `RepairSystem_Custom`, and `PirateKingdoms` contain TKU rows missing from current runtime CSV.
- `editor_mod_target_status_20260510` found no dedicated TKU compatibility mod target in the MW5 Mod Editor project. `E:\Games\MechWarrior5Editor\MW5Mercs\Mods` contains only `modlist.json`; project plugins are stock/editor plugins.
- `tku_inner_sphere_import_candidates_20260510` wrote two current-schema DataTable import candidates: raw original TKU and merged current-plus-TKU-additions. The merged candidate preserves 2,173 current rows, adds 1,801 TKU-only rows, retains 45 current-only rows, and totals 3,974 rows.
- The import candidate report found no TKU enum values missing from the current observed enum value sets after the parser suffix fix. Shared current/TKU rows still differ heavily in positions and 468 cluster assignments, so raw original TKU import remains risky.
- `editor_authoring_runbook_20260510` records the first manual MW5 Mod Editor gate. Suggested target is `TKUCompatEditorPatch`; preferred first data asset is the merged current-plus-TKU-additions DataTable candidate; old cooked TKU starmap/border/pawn classes remain blocked.
- `ue4_mod_entry_creation_probe_20260510` called only `MWModUtils.create_mod_entry` with a probe `MWModPluginInfo`, skipped all known mutating mod/package/save calls, and found no mod/plugin filesystem delta. `create_mod_entry` is therefore evidence for a transient commandlet entry only, not a safe scripted Create Mod workflow.
- `ue4_asset_authoring_api_stub_probe_20260510` found the generated editor Python stub exposes likely post-target authoring APIs for duplicate/import/save work: `EditorAssetLibrary.duplicate_asset`, `DataTableFunctionLibrary.fill_data_table_from_csv_file`, and `EditorAssetLibrary.save_asset`.
- `editor_gui_launch_attempt_20260510` found direct editor launch from Codex produced a responding `UE4Editor` process and generated the Python stub, but no usable top-level window; Explorer association returned without starting `UE4Editor`. The first safe Create Mod gate remains a manual interactive action.

## Asset Status

| Asset | Current status | Evidence | Next action |
| --- | --- | --- | --- |
| `/Game/Levels/FrontEnd/StarMap` | Split: loose override conditionally safe, TKU mod map unsafe | Loose override binds to current `/Game` starmap classes and passed override-only career load; TKU mod map binds to `/ModOverride/TheKnownUniverse` starmap classes | Prefer loose/current-class map path for stabilization; do not restore TKU mod map directly |
| `/Game/UI/FrontEnd/Starmap/StarMapActor` | Unsafe old TKU class stack; vanilla replacement alone insufficient | Structured parse shows TKU binds to TKU `StarSystemBody` and differs from current vanilla function/import shape; evidence patch changed fatal to loading stall | Inspect remaining root asset interactions before building another starmap class patch |
| `/Game/UI/FrontEnd/StarMapPawn` | Cooked substitution ruled out | Old cooked TKU pawn and current-package CDO patch both broke starmap open into first-person hangar view; readable CDO/default evidence was not sufficient for runtime safety | Move to editor-authored asset workflow or inspect other bounds loci (`StarMapActor`, `StarMap` level) before any further build |
| `/Game/Levels/FrontEnd/StarMap` placed systems | Needs generation/data investigation | Current editor level has 2,172 placed `StarSystemBody_C` actors while wide source JSON has 3,446 systems; runtime CSV row count matches current placed-body scale | Inspect source-to-runtime data import and level generation before any pawn-only bounds patch |
| `/Game/UI/FrontEnd/Starmap/StarSystemBody` | Unsafe old TKU class stack; vanilla replacement alone insufficient | Structured parse shows vanilla imports `MWClusterDataAsset` and exports current cluster-mesh functions; TKU lacks them and binds back to TKU `StarMapActor`; evidence patch changed fatal to loading stall | Inspect vanilla ownership/faction display paths plus TKU border/data/faction material interactions; recreate/derive rather than restore TKU cooked class |
| `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor` | Unsafe as blind restore | Previous fatal `Could not find SuperStruct BaseStarMapBorderActor_C`; cooked scan shows `/ModOverride/TheKnownUniverse` class path | Inspect vanilla parent class and current border actor inheritance |
| `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015` | Unsafe as cooked substitution | Current Davion start conditions reference this asset; TKU redirects it to a 2864 TKU plugin border actor; the vanilla cooked reassertion still triggered `BaseStarMapBorderActor_C` through `StarMapActor_2570` | Recreate or reparent in editor; do not direct-override cooked border assets again |
| TKU dated plugin border actors | Needs classification | Original pak has dated `StarMapBorderActor*`, `Borders*`, and `StarMapBordersUpdate_Action_*` assets | Determine whether they can be reparented or recreated |
| `MW5_InnerSphereData` | Needs schema/source investigation | Wide JSON source exists in editor, but runtime CSV/uasset is vanilla-scale; original TKU old table is large and unsafe as whole restore | Inspect generation/import workflow and table schema |
| Original TKU `MW5_InnerSphereData` row export | Clean-source evidence available | Parser recovered 3,929 original TKU rows and a derived CSV from the restored original TKU pak only | Use the derived CSV as input evidence for editor-authored data import; do not restore the old cooked DataTable directly |
| Merged InnerSphere import candidate | Preferred first data candidate, not build-authorized | Candidate preserves current 1.13 rows and descriptions while adding 1,801 TKU-only systems; raw TKU shared rows differ in position and 468 cluster assignments | Use for editor import planning after creating a dedicated mod target; do not import into live editor assets directly |
| `EmployerInfoData` | Needs schema/source investigation | Old root data restoration correlated with ownership breakage; vanilla editor contains Lyran and Clan strings | Compare row IDs and owner keys before porting |
| `SystemFactionChanges` | Needs schema/source investigation | Original TKU table is much larger than vanilla; plugin-only build did not restore full overlay | Compare schema and references to border/faction assets |
| `/Game/Campaign/Clusters/*` | Needs schema port/recreation | Current editor has 79 `MWClusterDataAsset` assets; original TKU has no modern cluster asset paths, but 46 current cluster IDs appear in original TKU's cooked InnerSphere strings | Inspect class requirements and migration utility before rebuilding overlays |
| Legacy TKU cluster overlay paths | Deprecated evidence, not safe assets | Manifest found 114 old overlay/constellation paths absent from loose editor content, current base game pak, and original TKU pak | Resolve through current `MWClusterDataAsset` assets or newly-authored equivalents; do not restore missing old paths blindly |
| `/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets` | Needs graph review before mutation | Probe confirms it is an `EditorUtilityWidgetBlueprint` depending on `PlaceClusterToi` assets, `/Game/InnerSphereData/MW5_InnerSphereData`, AssetTools, EditorScriptingUtilities, PythonScriptPlugin, and VictoryBPLibrary | Treat as a migration recipe until its graph is reviewed in the editor UI; do not run it on live assets blindly |
| `/Plugins/TheKnownUniverse/Content/Regions/War/CareerModeCustomClusters` | Needs source-role classification | It is the only cluster-named original TKU path and references `PlaceClanConflict` / `PlaceCustomConflict` | Determine whether it contains useful conflict-zone data, cluster overlay data, or both |
| Faction materials | Needs editor inspection | TKU faction materials reference `FactionColorMangle_MTF` and `FactionMPC`; vanilla materials use `/Game` package references | Inspect material parameter compatibility before reuse |
| MW5 editor mod creation/package APIs | Manual UI required for first authoring gate | `ue4_mod_types_probe` found metadata structs and `MWModEditorWidget.package_mod(args)`, but no direct `CreateMod`, `SaveToMod`, `SaveTo`, or module-level `PackageMod`; widget construction is abstract in commandlet. `ue4_mod_entry_creation_probe_20260510` found `create_mod_entry` returns a transient entry with no filesystem mod/plugin scaffold | Use commandlet Python for inspection/export only; use editor UI for `Create Mod` / `Save To Mod` unless a later widget/AutomationTool probe proves a safe scripted workflow |
| Post-target asset authoring APIs | Promising for mod-owned DataTable import | Generated Python stub exposes `EditorAssetLibrary.duplicate_asset`, `DataTableFunctionLibrary.fill_data_table_from_csv_file`, and `EditorAssetLibrary.save_asset` | After UI-created mod target exists, test only on a mod-owned copy of `MW5_InnerSphereData`; verify row count and samples before packaging |
| MW5 Mod Editor GUI launch from Codex | Blocked for first Create Mod gate | Direct launch exposed no top-level window despite a responding process; Explorer association did not start `UE4Editor` | User should manually open the MW5 Mod Editor and create `TKUCompatEditorPatch`; Codex can then inspect the filesystem and continue |

## Current Working Hypotheses

- `StarMapPawn` or `StarMap.umap` likely clamps map movement to the vanilla-scale coordinate range, while wide source data already exists elsewhere in the editor install.
- Full territory overlay likely requires current-schema generation/import of `MWClusterDataAsset` assets, `SystemFactionChanges`, and possibly compatible border actor assets, not direct restoration of original TKU cooked root data.
- Steiner/Lyran ownership broke when old root faction/employer assets were restored because current employer/faction identifiers or schema expectations differ from TKU build 38 root assets.
- The safest first repair track is likely a modern editor-authored substitution based on vanilla assets plus source-style data import/recreation, not a cooked TKU asset restore.

## Next Editor Inspection Checklist

1. Open the MW5 Mod Editor project at `E:\Games\MechWarrior5Editor\MW5Mercs\MW5Mercs.uproject`.
2. Let asset discovery complete before opening assets.
3. Open representative `/Game/Campaign/Clusters/*_ClusterAsset` assets and record required fields, naming rules, primary asset behavior, overlay mesh references, constellation mesh references, and faction asset references.
4. Open `/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets` and inspect its graph enough to decide whether it can run safely on copied data or should only guide a custom migration.
5. Open vanilla `/Game/Levels/FrontEnd/StarMap`.
6. Record World Settings, GameMode/Pawn/controller references, level Blueprint references, placed `StarMapActor`, placed `StarSystemBody` count/pattern, camera actors, and map bounds.
7. Open vanilla `/Game/UI/FrontEnd/StarMapPawn`.
8. Record `PanBoundsHorizontal`, `PanBoundsVertical`, `ZoomDistanceList`, `ZoomLevelThresholds`, and any camera clamp variables.
9. Open vanilla `/Game/UI/FrontEnd/Starmap/StarMapActor`.
10. Record border generation references, cluster-asset lookup paths, data-table references, star-system spawning logic, material references, and calls into `StarMapBP_UTILS`.
11. Open vanilla `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`.
12. Record parent class and compare against dated vanilla border actors.
13. Determine whether original TKU cooked assets can be mounted for inspection in the editor without copying them into active project source. If not, use approved asset tools or manual reconstruction from visible references.

## Build Gate

A single narrow evidence build is authorized and created from this trace: `MW5Mercs\Mods\TKUEvidenceStarmapCompat`. It is not a final compatibility patch. It only tests whether forcing the safe loose starmap/data override and current vanilla `StarMapActor` / `StarSystemBody` class assets clears the repeated `0x4C` career-load fatal.

The first evidence build did not clear the run; it converted the fatal crash into a hard loading stall and later failed/terminated without a fresh crash artifact. It is now disabled. Follow-up tracing authorized one additional narrow build, `MW5Mercs\Mods\TKUEvidenceStartBorderCompat`, because the active career-start `Borders3015` path points directly into TKU's old border actor chain. That build failed with `BaseStarMapBorderActor_C` and is now disabled.

Focused editor inspection then changed the authorized repair track: original TKU cannot remain active because its root `/Game` substitutions include stale parents for assets that vanilla HoloTable/border children require. `MW5Mercs\Mods\TKUEvidenceCorePluginOnly`, built from restored original TKU build 38 with every root `/Game` substitution removed, passed its runtime gate. Both bounds-pawn follow-ups are now ruled out: `TKUEvidenceBoundsPawn` restored original TKU `StarMapPawn`, and `TKUEvidenceCurrentPawnBounds` patched current vanilla `StarMapPawn` defaults, but both caused the starmap button to enter first-person hangar view instead of opening the starmap. The active safe runtime profile is back to `TKUEvidenceCorePluginOnly` only. No further cooked border or pawn substitution is authorized; later bounds, border, and overlay work must be editor-authored/reparented or traced to a different current-compatible asset path.

The latest build gate remains closed. `starmap_generation_trace_20260510`, `original_tku_inner_sphere_datatable_rows_20260510`, and `tku_editor_repair_candidate_manifest_20260510` authorize planning an editor-authored data/map/cluster candidate, but not packaging it yet. The next gate is a dedicated MW5 Mod Editor mod target, explicit rollback path, and cluster mapping policy for legacy `RepairSystem`, `CareerCluster`, and missing Clan/custom rows.
