# The Known Universe Compatibility Roadmap

## Goal

Deliver a local compatibility path for `TheKnownUniverse` (`TKU`) on the current `MW5 v1.13.378` install that is stable for new-career start, early starmap use, travel, contracts, saving, and the user's desired mod stack.

This roadmap now follows the editor-first strategy in [reports/tku_editor_first_strategy.md](reports/tku_editor_first_strategy.md). The next phase is not another pak rebuild. The next phase is reference tracing, editor inspection, and evidence-gated reconstruction.

For context-window resets, use the continuation handoff in [reports/tku_editor_first/tku_continuation_handoff_20260510.md](reports/tku_editor_first/tku_continuation_handoff_20260510.md). It records the latest active profile, ruled-out branches, runtime evidence, and a ready-to-paste GPT-5.5 extra-high continuation prompt.

## Current Roadmap Status

- Previous black-box pak bisection is paused.
- The live `MW5Mercs\Mods\TheKnownUniverse` folder has been restored from the original Nexus TKU download and is now the unaltered build-38 TKU source under test.
- Failed blind-build compatibility mods and old TKU artifacts were quarantined under `codex_quarantine\tku_failed_compat_20260510` instead of deleted.
- The active loose required override pak is the original Nexus `MW5Mercs\Content\Paks\MW5Mercs-zKnownUniverseStarmap.pak`.
- A failed load-order shim was disabled and preserved as `MW5Mercs\Mods\TheKnownUniverse\Paks\zzzz_MW5Mercs-zKnownUniverseStarmap.loadorder-test.pak.disabled-20260510`.
- Build 58 is the last useful stable runtime baseline: TKU plugin content only, zero root `/Game` assets, Steiner/Lyran ownership fixed, but vanilla-width starmap and limited territory overlay.
- Build 59 is a failed experimental state: TKU plugin content plus `/Game/Levels/FrontEnd/StarMap`, which hung on load.
- Root faction/employer assets are no longer presumed safe. Build 58 showed that removing all root `/Game` assets fixed the missing Steiner/Lyran ownership issue.
- TKU `StarMap.umap`, `StarMapActor`, `StarMapPawn`, `StarSystemBody`, and `BaseStarMapBorderActor` are no longer candidates for blind restore.
- The active strategic question is now: which starmap, cluster, border, faction, and data assets can be ported or recreated in the MW5 Mod Editor using current-compatible parents, schemas, and references?
- New clean-source evidence shows original TKU build 38 predates the current `/Game/Campaign/Clusters` `MWClusterDataAsset` overlay pipeline. The next repair gate is therefore cluster/data migration, not another restore of old cooked border actors.
- New runtime isolation shows the loose required override pak is not fatal by itself: with zero enabled mods, a Davion career, vanilla starmap, and mechbay loaded successfully.
- New runtime isolation also shows `vonBiomes` is not sufficient to explain the current `0x4C` fatal crash: the crash reproduced with `vonBiomes` disabled.
- New runtime isolation shows TKU's mod pak is sufficient to explain the current `0x4C` fatal crash: the same crash reproduced with only `TheKnownUniverse` enabled and the loose required override pak temporarily disabled.
- New structured package-table evidence shows the loose required starmap override binds to current `/Game` starmap classes, while TKU's mod-pak `StarMap.umap` binds to `/ModOverride/TheKnownUniverse` starmap classes.
- New structured package-table evidence shows original TKU `StarSystemBody` lacks the current vanilla `MWClusterDataAsset` import and current cluster-mesh exports (`ResetClusterMeshes`, `GetClusterOverlayMesh`, `GetClusterConstellationMesh`).
- The immediate fatal-crash suspect is now the old TKU starmap Blueprint class stack, not `vonBiomes`, not the loose override alone, and not a missing native parent class.
- A single narrow evidence build has been created as `MW5Mercs\Mods\TKUEvidenceStarmapCompat`; it is not a final compatibility patch, only a test of the old-starmap-class-stack fatal-crash hypothesis.
- Runtime test of `TKUEvidenceStarmapCompat` changed the failure mode from the repeated post-loading `0x4C` fatal crash to a hard loading stall with no new crash folder. This implicates the old starmap class stack, but also proves the remaining TKU root assets are still not coherent with the current starmap classes.
- Follow-up reference tracing found TKU `Borders3015` redirects the Davion career-start border asset to `/TheKnownUniverse/2864-01-01/StarMapBorderActor2864-01-01`, whose package depends on TKU's old `/ModOverride/.../BaseStarMapBorderActor`.
- A second narrow evidence build has been created as `MW5Mercs\Mods\TKUEvidenceStartBorderCompat`; it reasserts only current vanilla `Borders3015`, `AllStarMapBorderChanges`, and `BaseStarMapBorderActor`.
- Runtime test of `TKUEvidenceStartBorderCompat` failed with `Could not find SuperStruct BaseStarMapBorderActor_C to create StarMapActor_2570_C`; it is now disabled.
- A later retry of `TKUEvidenceStarmapCompat` also failed/terminated without a fresh crash artifact; it is now disabled.
- Focused MW5 Mod Editor inspection confirmed `StarMapActor_2570_C` is a HoloTable border Blueprint parented to `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor_C`, not a normal frontend starmap actor. This explains why TKU's stale root `BaseStarMapBorderActor` override can break vanilla Leopard/HoloTable loading.
- Current vanilla dated border actors also inherit the same current `BaseStarMapBorderActor_C`, so any viable TKU patch must avoid overriding that root base class unless it is editor-authored and current-parent compatible.
- `TKUEvidenceCorePluginOnly` has been built from the restored original build-38 TKU pak. It keeps 2,427 non-`/Game` entries and removes all 282 root `/Game` substitutions, including stale root border, starmap, data, employer, faction, persona, material, and TOI-function assets.
- Runtime test of `TKUEvidenceCorePluginOnly` succeeded: career loaded and the starmap opened, but the map remained bounded to vanilla limits and the territory overlay looked vanilla/incomplete with missing minor powers.
- `TKUEvidenceBoundsPawn` was built as a narrow follow-up that restored original TKU `StarMapPawn` wholesale. Runtime evidence ruled it out: career loaded, but pressing the starmap button entered first-person hangar view instead of opening the starmap.
- `TKUEvidenceCurrentPawnBounds` was built as the safer follow-up from the current vanilla `StarMapPawn`, preserving current widget/tooltip references and changing only serialized CDO defaults. Runtime evidence ruled it out too: career loaded, but pressing the starmap button still entered first-person hangar view.
- Active `modlist.json` now enables only `TKUEvidenceCorePluginOnly`. Original `TheKnownUniverse`, `TKUEvidenceStarmapCompat`, `TKUEvidenceStartBorderCompat`, `TKUEvidenceBoundsPawn`, and `TKUEvidenceCurrentPawnBounds` are disabled.
- On 2026-05-10 at approximately 21:35 Australia/Brisbane time, the live `modlist.json` was re-verified in that state and no MW5 or MW5 Mod Editor process was running.
- On 2026-05-10 at approximately 22:30 Australia/Brisbane time, the live `modlist.json` was re-verified again in that state. No MW5 or MW5 Mod Editor process was running.
- On 2026-05-10 at approximately 23:55 Australia/Brisbane time, the live `modlist.json` was re-verified again in that state. The process query returned no MW5 or UE4 editor process entries.
- A focused non-mutating editor commandlet probe now exists at `reports\tku_editor_first\ue4_mod_types_probe.md` and `.json`, backed by `tools\tku_reference_audit\ue4_probe_mod_types.py`.
- That probe found `MWModPluginInfo`, `ModPackageArgs`, `MWModUtils`, and `MWModEditorWidget.package_mod(args)`, but found no direct module-level `CreateMod`, `SaveToMod`, `SaveTo`, or `PackageMod` symbol.
- `MWModEditorWidget` is exposed but abstract in Python commandlet construction, and the commandlet saw no active mod plugin. Current API evidence therefore does not authorize Python-only creation of a proper MW5 `ModOverride` asset. Manual MW5 Mod Editor UI remains required for safe `Create Mod` and `Save To Mod` until a widget-spawn or AutomationTool workflow is separately proven.
- A follow-up non-mutating mod-entry creation probe now exists at `reports\tku_editor_first\ue4_mod_entry_creation_probe_20260510.md` and `.json`, backed by `tools\tku_reference_audit\ue4_probe_mod_entry_creation.py`.
- That probe called only `MWModUtils.create_mod_entry` with a probe `MWModPluginInfo`, explicitly did not call `set_active_mod`, `save_mod_info_to_file`, `package_mod`, `save_asset`, or `duplicate_asset`, and produced no mod/plugin filesystem delta. It proves `create_mod_entry` can create a transient editor list entry, not a proper on-disk MW5 mod target.
- A read-only stub probe now exists at `reports\tku_editor_first\ue4_asset_authoring_api_stub_probe_20260510.md` and `.json`. It used the MW5 Mod Editor-generated `Intermediate\PythonStub\unreal.py` and found post-target authoring APIs for duplicate/import/save work, including `EditorAssetLibrary.duplicate_asset`, `DataTableFunctionLibrary.fill_data_table_from_csv_file`, and `EditorAssetLibrary.save_asset`.
- That stub probe does not authorize editing base `/Game` assets or packaging. It only supports a later controlled import into a mod-owned DataTable after the MW5 Mod Editor UI creates the proper mod target.
- A GUI launch attempt report now exists at `reports\tku_editor_first\editor_gui_launch_attempt_20260510.md` and `.json`. Direct launch created a responding `UE4Editor` process and generated the Python stub, but exposed no usable top-level editor window to this session; the process was stopped. Launch through Explorer returned without starting `UE4Editor`. The first `Create Mod` gate therefore needs a manual interactive editor launch/action by the user.
- A second non-mutating editor commandlet probe now exists at `reports\tku_editor_first\ue4_starmap_bounds_clusters_probe.md` and `.json`, backed by `tools\tku_reference_audit\ue4_probe_starmap_bounds_clusters.py`.
- That probe loaded current `/Game/Levels/FrontEnd/StarMap` and found 2,182 actors, including 2,172 `StarSystemBody_C` actors. The editor source JSON has 3,446 systems, while the runtime CSV has 2,173 rows, so expanded TKU map repair is not only a pawn camera-bound edit.
- The same probe confirmed the current cluster pipeline has 79 `MWClusterDataAsset` assets, 815 total system memberships, 74 assets with overlay meshes, and 31 with constellation meshes. Territory-overlay repair should proceed as current-schema cluster-data migration, not old cooked border restoration.
- The current repair-track decision is recorded in `reports\tku_editor_first\tku_repair_track_decision_20260510.md`: bounds Track B2 first (`StarMapActor`, level generation/placement, data import), overlay Track A1 (`MWClusterDataAsset` migration), and no new build authorized yet.
- A non-mutating starmap generation trace now exists at `reports\tku_editor_first\starmap_generation_trace_20260510.md` and `.json`, backed by `tools\tku_reference_audit\ue4_probe_starmap_generation_trace.py`.
- That trace recovered the current placement transform exactly: `LevelX = 51336 + 8 * PosY` and `LevelY = 51039 + 8 * PosX`, with zero residual across 2,172 placed current `StarSystemBody_C` actors.
- A clean-source parser now extracts original TKU's cooked `/Game/InnerSphereData/MW5_InnerSphereData` directly from the restored original TKU pak. It wrote `reports\tku_editor_first\original_tku_inner_sphere_datatable_rows_20260510.md`, `.json`, and `.csv`, backed by `tools\tku_reference_audit\parse_original_tku_inner_sphere_datatable.py`.
- The original TKU DataTable parse recovered 3,929 rows, 1,091 clustered rows, 69 unique cluster IDs, 103 overlay rows, and 38 constellation rows. Its coordinate span is about X `-1877..1937` and Y `-2004..1912`, projecting to current-level bounds about X `35305..66633` and Y `36020..66538`.
- The DataTable parser now preserves UE4 `FName` numeric suffixes for enum values (`C_8`, `H_0`, etc.), so its derived CSV is current-schema comparable. A prior collapsed `C`/`H` display bug was fixed before import candidates were generated.
- A repair-candidate manifest now exists at `reports\tku_editor_first\tku_editor_repair_candidate_manifest_20260510.md` and `.json`, backed by `tools\tku_reference_audit\plan_tku_editor_repair_candidate.py`. It keeps `build_authorized=false`.
- The manifest found original TKU's legacy overlay/constellation soft paths are mostly not available in current editor loose content, current base game pak, or original TKU pak: 20 unique paths are loose editor assets, 114 are missing from those sources. Treat those old DataTable overlay paths as migration evidence, not assets to restore.
- The manifest also found the legacy TKU `RepairSystem` cluster splits across 32 current CSV cluster targets, while `CareerCluster` maps to current rows with no active CSV cluster. `ClanConflict`, `RepairSystem_Clan`, `RepairSystem_Custom`, and `PirateKingdoms` contain TKU rows absent from the current runtime CSV. Modern cluster repair needs an explicit editor-authored mapping policy before writing assets.
- InnerSphere import candidates now exist at `reports\tku_editor_first\tku_inner_sphere_import_candidates_20260510.md` and `.json`, backed by `tools\tku_reference_audit\build_tku_inner_sphere_import_candidates.py`.
- The import candidate report writes a raw original-TKU current-schema CSV and a safer merged current-plus-TKU-additions CSV. The merged candidate preserves 2,173 current rows, adds 1,801 TKU-only systems, retains 45 current-only rows, and totals 3,974 rows. It is the preferred first editor data candidate, but still does not authorize a build.
- An editor authoring runbook now exists at `reports\tku_editor_first\editor_authoring_runbook_20260510.md` and `.json`. It records the manual MW5 Mod Editor gate, suggested mod target `TKUCompatEditorPatch`, preferred merged DataTable import candidate, current StarMap placement formula, blocked old cooked sources, and package gate.

## Source Of Truth Rules

- For MW5 packaging and mod-framework behavior, prefer `MW5Mercs\Mods\MW5Mercs_Mod_Editor_Guide_(v2.3).pdf`.
- For Unreal Engine concepts, editor mechanics, Blueprints, Actors, Levels, asset references, metadata, and other non-MW5-specific engine behavior, use Epic's official Unreal Engine 4.27 documentation: `https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-4-27-documentation?application_version=4.27&lang=en-US`.
- For specific MW5 asset behavior, prefer direct inspection in the MW5 Mod Editor over pak manifests, guessed inheritance, or runtime symptoms.
- Do not rely on current UE5 documentation for TKU decisions unless the same behavior is confirmed in UE4.27 or in the MW5 Mod Editor.
- If the roadmap, local guesses, third-party tools, or previous build results disagree with MW5 editor evidence or Epic UE4.27 docs, pause and record the discrepancy before building.

## Non-Goals And Safety Rules

- Do not edit or replace the original TKU backup in place.
- Do not edit original TKU paks in place.
- Do not use quarantined blind-build artifacts as source evidence.
- The live `MW5Mercs\Mods\TheKnownUniverse` folder may be used as original TKU evidence only because it was restored from the Nexus build-38 download on 2026-05-10.
- Do not edit `MW5Mercs\Content\Paks\MW5Mercs-zKnownUniverseStarmap.pak`; only rename it temporarily for isolation tests and restore it afterward.
- Do not delete disabled historical paks or rollback artifacts.
- Do not install or download third-party tooling without approval.
- Do not treat a broad vanilla override as success if it removes TKU's starmap value.
- Do not treat title-screen boot as validation.
- Do not build another compatibility pak until an evidence gate below explicitly allows it.
- Keep temporary outputs under `reports\tku_editor_first\`, `tools\tku_reference_audit\`, or another documented staging directory.

## Current Evidence

### Runtime Evidence

- Near-vanilla `modlist.json` with zero enabled mods loaded a new career successfully.
- Near-vanilla `modlist.json` with zero enabled mods plus the loose required TKU override pak loaded a Davion career successfully; the vanilla starmap and mechbay loaded.
- Original `TheKnownUniverse` alone reproduced startup/new-career failure.
- Original TKU crash signature included `EXCEPTION_ACCESS_VIOLATION reading address 0x000000000000004c` and `PCallStackHash = 0039C4B8A7510FAC9074DFC881C752315D75F42F`.
- The same crash signature reproduced with `vonBiomes` disabled, so `vonBiomes` is not the primary/sufficient cause of this fatal career-load crash.
- The loose required override pak is not independently fatal when TKU is disabled.
- The completed runtime split pins the primary fatal source to `TheKnownUniverse.pak`.
- `StarMapActor` / `StarSystemBody` restore attempts produced a separate null access violation at address `0x0000000000000000`.
- Restoring TKU `BaseStarMapBorderActor` produced `Could not find SuperStruct BaseStarMapBorderActor_C to create StarMapActor_2570_C`.
- Build 58 loaded and fixed Steiner/Lyran ownership, but did not restore expanded map width or full non-major territory overlay.
- Build 59 hung after restoring TKU `StarMap.umap` on top of build 58.
- `TKUEvidenceStarmapCompat` hung during Davion career loading with no new crash folder after replacing only TKU `StarMapActor` and `StarSystemBody` with current vanilla class assets.
- A later retry of the same starmap evidence profile failed/terminated without creating a newer crash folder, so that profile is no longer useful for testing.
- TKU `Borders3015` contains `BorderActor` references to `/TheKnownUniverse/2864-01-01/StarMapBorderActor2864-01-01`, unlike current vanilla `Borders3015`, which references `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/StarMapBorderActor3015`.
- TKU `StarMapBorderActor2864-01-01` hard-references `/ModOverride/TheKnownUniverse/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`, matching the previous `BaseStarMapBorderActor_C` failure family.
- `TKUEvidenceStartBorderCompat` reproduced that border-superstruct failure against current vanilla `StarMapActor_2570_C`, so direct cooked border substitution is not a safe patch strategy.
- `TKUEvidenceCorePluginOnly` loaded successfully, proving the root-stripped plugin-content baseline is stable. Its limitation is now proven, not hypothetical: vanilla/current root starmap behavior lacks TKU's expanded map bounds and full non-major overlays.
- `TKUEvidenceBoundsPawn` and `TKUEvidenceCurrentPawnBounds` both failed behaviorally and are disabled. Cooked `StarMapPawn` substitution is now ruled out for bounds work. The next repair gate is editor-authored inspection/recreation or a different current starmap asset path, not another pawn pak.
- Travel, contracts, save, and early starmap interaction were successful in some reduced builds, but those builds bypassed core TKU starmap features.

### Disk Evidence

- Current live TKU folder is restored original build 38 and is the clean TKU source under test.
- Quarantined failed artifacts are outside MW5 loader paths under `codex_quarantine\tku_failed_compat_20260510`.
- Active loose starmap override exists at `MW5Mercs\Content\Paks\MW5Mercs-zKnownUniverseStarmap.pak`.
- Existing reports and scripts live under `reports` and `tools`.
- `reports\tku_editor_first_strategy.md` is now the controlling analysis document.
- `reports\tku_runtime_isolation_20260510.md` records the current runtime isolation matrix.
- `reports\battlefxenhanced_compat_notes.md` and `reports\battlefx_patch_extension_report.md` document BattleFXEnhanced compatibility work that must be included in later stack tests.

### Editor And Reference Evidence

- `reports\tku_editor_first\original_tku_pak_inventory.md` inventories the original unaltered build-38 pak only.
- Original TKU build 38 has 2,709 pak entries, zero path-level `/Game/Campaign/Clusters` assets, and no scanned cooked strings mentioning `MWClusterDataAsset` or `/Game/Campaign/Clusters`.
- Original TKU build 38 also lacks structured package-table imports for `MWClusterDataAsset` in its `StarSystemBody`, while current vanilla `StarSystemBody` imports that class.
- The only cluster-named original TKU asset path is `/Plugins/TheKnownUniverse/Content/Regions/War/CareerModeCustomClusters`.
- Current MW5 editor evidence shows 261 assets under `/Game/Campaign/Clusters`, including 79 `MWClusterDataAsset` assets with `system_ids`, `cluster_faction_asset`, `cluster_overlay`, and `cluster_constellation`.
- `reports\tku_editor_first\cluster_migration_inputs.md` shows current editor runtime data has 824 nonempty cluster rows, 77 unique nonempty cluster IDs, 74 overlay rows, and 31 constellation rows.
- `reports\tku_editor_first\tku_cooked_package_refs.md` confirms the current vanilla starmap class stack imports/exports current cluster-data hooks that original TKU build 38 lacks.
- `reports\tku_editor_first\tku_structured_reference_findings_20260510.md` summarizes the new package-table evidence after the repeated fatal error report.
- `reports\tku_editor_first\tku_evidence_starmap_class_patch_20260510.md` documents the first evidence-gated stabilizer build and its hard-stall runtime result.
- `reports\tku_editor_first\tku_evidence_start_border_patch_20260510.md` documents the next evidence-gated start-border build.
- `reports\tku_editor_first\ue4_starmap_border_path_inspection.md` confirms `StarMapActor_2570_C` and all current vanilla dated border actors depend on the current root `BaseStarMapBorderActor_C`.
- `reports\tku_editor_first\tku_evidence_core_plugin_only_20260510.md` documents the clean-source root-stripped baseline build and why it is now the authorized runtime gate.
- `reports\tku_editor_first\tku_evidence_bounds_pawn_20260510.md` documents the bounds-only pawn patch, its recovered TKU defaults, and the rollback condition.
- `reports\tku_editor_first\tku_evidence_current_pawn_bounds_20260510.md` documents the current-package pawn bounds patch, why the old pawn was ruled out, and the safer serialized-default change.
- The same report found 44 current editor `Place*` region assets with cluster references, and representative assets point directly at `/Game/Campaign/Clusters/*_ClusterAsset`.
- Forty-six current editor cluster IDs are visible in original TKU's cooked `MW5_InnerSphereData` strings, which supports a cluster migration path but does not yet recover the required row mappings.
- The MW5 editor Python stub marks `InnerSphereMapData.cluster`, `cluster_overlay`, and `cluster_constellation` as deprecated in favor of cluster data assets.
- `/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets` exists in the editor and appears designed to migrate `PlaceClusterTOI_ArcAction` and InnerSphereMap data into `MWClusterDataAsset` files.
- The current vanilla `StarMap` level contains 2,172 placed `StarSystemBody_C` actors with vanilla-scale bounds, while editor source JSON contains 3,446 systems. Expanded map support likely needs level/generation work, not only table edits.

### Ruled-Out Hypotheses

- `MW5_TOI_Functions` alone caused the missing Steiner/Lyran ownership issue. Build 56 behaved like build 55 after removing it.
- Legacy `CustomContent` caused the missing Steiner/Lyran ownership issue. Build 57 behaved like build 56 after removing it.
- Root faction/employer assets are harmless. Build 58 fixed Steiner/Lyran ownership by removing all root `/Game` assets.
- TKU `StarMap.umap` can be safely restored once root data conflicts are removed. Build 59 disproved this.
- Replacing only TKU `StarMapActor` and `StarSystemBody` with current vanilla assets is sufficient. The evidence patch disproved this by changing the fatal crash into a hard loading stall.
- Directly reasserting cooked vanilla `BaseStarMapBorderActor`, `Borders3015`, and `AllStarMapBorderChanges` is safe. The start-border evidence patch disproved this by reproducing the `BaseStarMapBorderActor_C` superstruct crash.
- The original TKU pak can remain enabled while we patch around it. The editor evidence disproves this: its root `/Game` `BaseStarMapBorderActor` substitution can invalidate vanilla HoloTable and border children.
- Pak path manifests are enough to reason about Blueprint compatibility. They are not.

## Why The Roadmap Changed

The old roadmap assumed the core problem was stale root assets that could be neutralized by replacing cooked files with vanilla equivalents. That approach made the game more stable, but it also stripped out the TKU systems that likely implement expanded starmap bounds and full territory overlays.

Cooked UE4 assets do not expose enough information through terminal manifests. A `.umap` or `.uasset` can contain parent-class references, Blueprint graphs, construction scripts, serialized object references, material parameter bindings, data-table row schemas, placed actors, and level Blueprint logic. Runtime crashes and hangs proved that path-level asset selection is too coarse.

The better path is to use the MW5 Mod Editor and UE4.27 documentation to inspect or recreate the relevant assets from current-compatible foundations.

## High-Priority Asset Questions

| Asset or group | Question to answer before building |
| --- | --- |
| `/Game/Levels/FrontEnd/StarMap` | Does it hard-reference unsafe TKU starmap classes, dated border actors, level Blueprint logic, or map bounds? |
| `/Game/UI/FrontEnd/Starmap/StarMapActor` | Which current graph/default paths are required for cluster-data and starmap-body interaction, and how can TKU data be routed through current-safe classes? |
| `/Game/UI/FrontEnd/StarMapPawn` | Bounds-only evidence patch is testing whether it controls camera pan limits, map clamps, and zoom behavior. |
| `/Game/UI/FrontEnd/Starmap/StarSystemBody` | Which current `MWClusterDataAsset`, cluster overlay mesh, constellation mesh, ownership display, and faction-color paths are required? |
| `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor` | Why does TKU's serialized class hierarchy fail to find `BaseStarMapBorderActor_C`? |
| TKU dated plugin border assets | Can they be reparented to current vanilla border classes, or must the border data be recreated? |
| `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015` | Is the Davion loading stall caused by TKU redirecting the 3015 start border to an old 2864 TKU plugin actor? |
| `MW5_InnerSphereData`, `EmployerInfoData`, `SystemFactionChanges` | Are TKU rows compatible with the current schema, or do they need to be ported into current tables? |
| `/Game/Campaign/Clusters/*` and `MWClusterDataAsset` | Which modern cluster assets drive non-major overlays, industrial hubs, and cluster factions, and how can TKU's old cluster/overlay data be migrated into this schema? |
| `/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets` | Can this editor utility safely migrate copied/editor-authored TKU data, or should its graph only be used as a migration recipe? |
| `/Plugins/TheKnownUniverse/Content/Regions/War/CareerModeCustomClusters` | Is this old campaign arc data enough to seed modern cluster assets, or is TKU `MW5_InnerSphereData` the better source? |
| Root `/Game/Employers/*` and `/Game/Factions/*` | Which old assets break Steiner/Lyran ownership, and which new factions actually need porting? |
| Faction materials and color data | Are non-major overlays missing because vanilla code ignores TKU colors, because material bindings changed, or because border actors never spawn? |

## Roadmap

## Phase 0: Freeze And Normalize The Work State

### Objective

Stop the live install from drifting while evidence is gathered.

### Tasks

1. Record the current live `TheKnownUniverse` state as restored original Nexus build 38.
2. Preserve build 58 as the last useful runtime baseline in reports, not by blindly reverting the live folder during analysis.
3. Verify the restored original TKU pak and active loose required override pak are not edited in place.
4. Create `reports\tku_editor_first\` for future reference traces and editor notes.
5. Create `tools\tku_reference_audit\` only if new local helper scripts are needed.
6. Record the currently active `modlist.json` before any future runtime test.

### Acceptance Gate

- The restored original TKU pak and active loose required override pak are present and unmodified.
- Build 59 is documented as failed, not used as a gameplay baseline.
- No new pak rebuild has happened.

## Phase 1: Establish Editor And Tooling Evidence

### Objective

Prepare an inspection workflow that can answer asset-reference questions before changing runtime paks.

### Tasks

1. Locate the MW5 Mod Editor install and document its path.
2. Confirm the editor can launch and finish asset discovery.
3. Read the MW5 Mod Editor Guide sections for `Save To Mod`, `ModOverride`, plugin `Content`, existing-mod porting, load order, and custom data tables.
4. Use Epic UE4.27 docs when unsure about Blueprints, Actor references, Level assets, object redirectors, asset metadata, or reference viewers.
5. Confirm which tools are already local:
   - `tools\mw5_pak.py`
   - UnrealPak from the MW5 editor or game toolchain, if present
   - `pypdf`
   - MW5 Mod Editor at `E:\Games\MechWarrior5Editor`
   - FModel at `C:\Program Files\fmodel`
   - UEViewer/umodel at `C:\Program Files\umodel`
   - Blender 5.1 with Unreal PSK/PSA addon at `C:\Program Files\Blender Foundation\Blender 5.1`
   - UAssetAPI/MW5AssetTool at `D:\Downloads\OneDrive\Documents\code\tku-update\tools\MW5AssetTool`
   - UAssetGUI at `C:\Program Files\UassetGUI`
   - UE4SS v3.0.1 dev build extracted from `zDEV-UE4SS_v3.0.1.zip` into `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Binaries\Win64`
6. Use the locally available editor and asset-inspection tools when they can answer reference, cooked-asset, or packaging questions:
   - MW5 Mod Editor for authoritative Blueprint, schema, reference, and mod-authoring evidence
   - FModel and UEViewer/umodel for supporting pak/cooked-asset inspection and reference extraction
   - Blender for mesh/animation import-export or visual inspection when PSK/PSA assets are involved
   - UAssetAPI/MW5AssetTool and UAssetGUI for structured UAsset inspection/comparison where appropriate
   - UE4SS for runtime instrumentation, Lua/mod hooks, and runtime evidence where appropriate
7. List optional tools that might help but still require approval before installation:
   - Unreal asset dump/reference tools compatible with MW5's UE4 version
8. Decide whether original pre-cooked TKU UASSETs exist anywhere outside the backup paks.
9. Maintain a clean-source inventory report for original TKU build 38 and update it only from `MW5Mercs\Mods\TheKnownUniverse`.

### Acceptance Gate

- The editor path and available local tooling are documented.
- The team knows whether there are pre-cooked TKU source assets or only cooked paks.
- The original clean TKU pak inventory exists and is linked from the reference trace.
- No third-party tool has been installed without approval.

## Phase 2: Produce The Reference Trace

### Objective

Identify the actual dependency graph for the starmap, border overlay, map bounds, and faction ownership systems.

### Tasks

1. Inspect current `/Game/Campaign/Clusters` assets and the `MWClusterDataAsset` class in the MW5 Mod Editor.
2. Inspect `/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets` and decide whether it is safe to run on copied/editor-authored data or should only be treated as a migration recipe.
3. Inspect current vanilla `StarMap.umap` and original TKU `StarMap.umap` in the MW5 Mod Editor or an approved asset-inspection setup.
4. Record world settings, level Blueprint references, placed actors, missing class warnings, starmap actor classes, border actor classes, and map movement bounds.
5. Inspect current vanilla and TKU `StarMapActor`.
6. Record parent class, construction script dependencies, BeginPlay logic, territory overlay logic, border actor arrays/maps, material references, and differences around `MouseOverStarSystem` / `SetMouseOverStarSystem`.
7. Inspect current vanilla and TKU `StarMapPawn`.
8. Record input routing, map pan/zoom limits, camera bounds, and starmap transition behavior.
9. Inspect current vanilla and TKU `StarSystemBody`.
10. Record ownership display bindings, owner lookup paths, faction color paths, selected-system UI dependencies, `MWClusterDataAsset` use, and cluster mesh functions.
11. Inspect TKU `BaseStarMapBorderActor` and dated plugin border actors.
12. Record class parents, reparenting feasibility, material bindings, and references to faction/employer assets.
13. Compare vanilla and TKU data schemas for `MW5_InnerSphereData`, `EmployerInfoData`, `SystemFactionChanges`, and `MWClusterDataAsset`.
14. Determine whether TKU's old `Cluster`, `ClusterOverlay`, `ClusterConstellation`, `PlaceCluster`, or `CareerModeCustomClusters` data can seed modern `MWClusterDataAsset` assets.
15. Trace Steiner/Lyran ownership specifically through employer ID, faction ID, display name, row key, asset path, and redirects.
16. Write `reports\tku_editor_first\reference_trace_manifest.md`.
17. Write `reports\tku_editor_first\reference_trace_manifest.json` with machine-readable asset decisions.

### Acceptance Gate

- Every high-priority asset above has an inspected status.
- Each asset is classified as `safe`, `unsafe`, `needs recreation`, `needs reparenting`, `needs schema port`, or `not needed`.
- The cluster overlay system is classified separately from the old border-actor system.
- No build is allowed until this trace exists.

## Phase 3: Choose A Repair Track

### Objective

Pick the smallest repair strategy supported by the reference trace.

### Repair Tracks

- Track A, data-only/plugin-content port: use if vanilla starmap code can consume TKU data once rows, factions, or border definitions are ported into current-compatible schemas.
- Track A1, cluster-data migration: use if non-major overlays can be restored by creating current `MWClusterDataAsset` assets from TKU's old InnerSphere cluster fields or campaign-arc data.
- Track B, editor-authored vanilla substitution: use if expanded bounds or overlay hooks are simple properties or references on current vanilla `StarMapActor`, `StarMapPawn`, `StarSystemBody`, or data assets.
- Track C, reparented TKU border/actor assets: use only if the editor proves TKU classes can be reparented cleanly to current vanilla parents.
- Track D, starmap reconstruction: use if old cooked `StarMap.umap` and starmap Blueprints cannot be safely restored, but their behavior can be rebuilt from inspected references.
- Track E, feature deferral: use if a TKU feature depends on opaque cooked logic that cannot be inspected or recreated safely.

### Decision Rules

- If `StarMap.umap` hard-references unsafe TKU classes, do not restore it directly.
- If data-table schemas differ, port rows into current-compatible data assets rather than restoring old tables wholesale.
- If TKU lacks modern cluster assets, do not keep testing old border actors until the `MWClusterDataAsset` migration path is answered.
- If old root faction/employer assets break Steiner/Lyran ownership, never restore them as a group.
- If non-major overlays require dated border actors, reparent or recreate those actors in the editor before packaging.
- If a feature cannot be explained by reference evidence, defer it rather than gambling with a live pak.

### Acceptance Gate

- A single repair track is selected for the next build.
- The selected track has a written asset list, expected behavior, rollback path, and test checklist.

## Phase 4: Build Only From Evidence

### Objective

Create the first post-strategy build only after the reference trace justifies it.

### Tasks

1. Create a new build rationale document under `reports\tku_editor_first\`.
2. Use the MW5 Mod Editor `Save To Mod` workflow for same-path substitutions.
3. Use plugin `Content` for new TKU data, factions, helper assets, and custom data tables.
4. Avoid cooked TKU replacements unless the editor proves they are safe.
5. Package through the editor when possible.
6. If UnrealPak is used, build from a deterministic response file and include sidecars.
7. Produce a manifest that records source asset, edited asset, mount path, reason, dependency evidence, and rollback file.
8. Do not overwrite original backups.

### Acceptance Gate

- The build can be reproduced from a manifest.
- The manifest cites editor/reference evidence for every changed asset.
- The build has an explicit rollback point.

## Phase 5: Runtime Validation Of The Evidence Build

### Objective

Validate behavior without overclaiming success.

### Test Profile Order

1. Near-vanilla control.
2. TKU evidence build alone.
3. TKU evidence build plus `Coyotesmission`.
4. TKU evidence build plus named local companion mods.
5. TKU evidence build plus `BattleFXEnhanced` and `BattleFXPatch`.
6. Full desired stack with TKU evidence build and BattleFXPatch.

### Mandatory Checks

- Title screen appears without new fatal error.
- New career start reaches starting location selection.
- Starting locations display correctly.
- Career load completes after cinematic.
- Starmap opens from the leopard/hangar UI.
- Starmap pan/zoom covers the intended map width.
- Steiner/Lyran owner data remains correct.
- Non-major faction owners are present where expected.
- Territory overlay renders for the intended faction set.
- Travel works across multiple jumps.
- Conflict zones, arenas, missions, rare mechs, industrial hubs, and contracts generate.
- Save and reload works.
- No new crash folder appears.

### Acceptance Gate

- Test results match the expected behavior from the build rationale.
- Any missing TKU feature is documented as a known limitation, not silently accepted.

## Phase 6: Compatibility Sweep

### Objective

Prove the repaired TKU path does not destabilize the desired local mod stack.

### Named Local Scope

- `ModOptions`
- `BetterMissionChoices`
- `Coyotesmission`
- `PurchaseSalvage`
- `SimpleZoom`
- `BattleFXEnhanced`
- `BattleFXPatch`
- `TheKnownUniverse`
- The post-strategy TKU compatibility build

### Tasks

1. Verify `BattleFXPatch` remains enabled whenever `BattleFXEnhanced` is enabled.
2. Confirm BattleFXPatch reports remain applicable or update them if the TKU build changes mod load order.
3. Test TKU alone before blaming companion mods.
4. Add one compatibility group at a time.
5. Capture crash folder timestamps and logs after each run.
6. If a failure appears, isolate the interaction before changing assets.

### Acceptance Gate

- No return of the original TKU `0x4C` crash.
- No return of known BattleFXEnhanced particle/material crashes covered by `BattleFXPatch`.
- No starmap regression caused by named local mods.

## Phase 7: Full Stack Burn-In

### Objective

Promote the result from "boots once" to "safe enough to play".

### Tasks

1. Run three clean relaunches with the selected full-stack profile.
2. In each run, verify new career or save load, starmap open, travel, contracts, and save/reload.
3. Confirm no new crash folder across the burn-in pass.
4. Confirm the final logs show expected mod and pak mount order.
5. Record performance or loading-screen anomalies separately from hard crashes.

### Acceptance Gate

- Three consecutive clean runs complete without new TKU or BattleFX crash evidence.
- The final limitation list is honest and specific.

## Phase 8: Deployment And Operator Notes

### Deliverables

- Final local TKU compatibility mod or editor-authored patch folder.
- Final packaged pak, if packaging is required.
- Final `mod.json`.
- `reports\tku_editor_first\reference_trace_manifest.md`.
- `reports\tku_editor_first\reference_trace_manifest.json`.
- Build rationale and manifest for every post-strategy build.
- Operator notes covering load order, required companion patches, rollback, and known limitations.

### Deployment Rule

- The patch must be local, self-contained, and reversible.
- It must not require disabling desired mods unless a specific incompatibility is proven and documented.
- It must not hide missing TKU starmap features behind a broad vanilla fallback.

## Build Authorization Gates

- Gate 1: Reference trace exists and classifies high-priority assets.
- Gate 2: Repair track is selected from evidence.
- Gate 3: Build manifest lists every changed asset and why it is safe.
- Gate 4: Rollback path is documented before packaging.
- Gate 5: Runtime test checklist is ready before launch.

No future build should bypass these gates.

## Success Definition

The roadmap is complete only when all of the following are true:

- `TheKnownUniverse` or a locally rebuilt TKU-compatible replacement is enabled.
- Original backups remain preserved.
- The current MW5 build loads a new career cleanly.
- Early starmap gameplay works without the recurring `0x4C` fatal error.
- Steiner/Lyran ownership remains correct.
- Expanded map bounds and territory overlay behavior are either restored or explicitly documented as deferred.
- Named local mods remain usable.
- `BattleFXEnhanced` remains covered by `BattleFXPatch` when enabled.
- The full desired mod profile remains usable, with absent or deferred mods documented.
- The final asset manifest explains why each patched or rebuilt asset is compatible.

## Recommended Implementation Order

1. Freeze and document the restored original TKU build-38 state plus the failed build-59 history.
2. Locate and validate the MW5 Mod Editor workflow.
3. Create `reports\tku_editor_first\`.
4. Produce the starmap and data reference trace.
5. Select repair track A, B, C, D, or E.
6. Create one evidence-backed build manifest.
7. Build through the editor or deterministic packaging only after gates pass.
8. Validate TKU alone.
9. Validate named local mods and BattleFXEnhanced with BattleFXPatch.
10. Validate the full desired stack.
11. Burn in and write final operator notes.

## Immediate Next Step

Do not run another bounds pawn profile. The active safe runtime profile is back to `TKUEvidenceCorePluginOnly` only, and that profile was re-verified on disk after the failed pawn work.

The MW5 editor Python API probes did not expose a safe direct `Create Mod` / `Save To Mod` path. `create_mod_entry` returned successfully in memory but created no disk mod target, so the next work path is: use commandlet Python only for non-mutating inspection and data export, and use the MW5 Mod Editor UI for first editor-authored `Create Mod` / `ModOverride` creation unless a later focused widget/AutomationTool probe proves a safe scripted path.

Continue with evidence-gated inspection of `StarMapActor`, `StarMap` level generation/placement, and the source-to-runtime InnerSphere data import path before authoring another pawn-only bounds patch. In parallel, keep moving the territory-overlay track toward modern `MWClusterDataAsset` migration using the editor utility as evidence, not as an unreviewed mutation.

Expected result if the evidence is right: an editor-authored patch should preserve the starmap open transition. If editor-authored pawn defaults also reproduce first-person hangar view, abandon `StarMapPawn` as the bounds locus and move to `StarMapActor` or level-level bounds inspection. Complete TKU territory overlays remain a separate modern cluster-data migration task.
