# Codex RE Continuation Gate - 2026-05-12

This is a continuation and implementation-gate report for the TKU editor-first recovery track. It consolidates the required 2026-05-10 evidence with the newer 2026-05-12 editor-authored patch, runtime result, and content-mirror evidence.

## Files Read

Required handoff set:

- `README.md`
- `AGENTS.md`
- `TKU_COMPAT_PATCH_ROADMAP.md`
- `reports\tku_editor_first_strategy.md`
- `reports\tku_editor_first\tku_continuation_handoff_20260510.md`
- `reports\tku_runtime_isolation_20260510.md`
- `reports\tku_editor_first\reference_trace_manifest.md`
- `reports\tku_editor_first\tku_repair_track_decision_20260510.md`
- `reports\tku_editor_first\starmap_generation_trace_20260510.md`
- `reports\tku_editor_first\original_tku_inner_sphere_datatable_rows_20260510.md`
- `reports\tku_editor_first\tku_editor_repair_candidate_manifest_20260510.md`
- `reports\tku_editor_first\tku_inner_sphere_import_candidates_20260510.md`
- `reports\tku_editor_first\editor_authoring_runbook_20260510.md`
- `reports\tku_editor_first\editor_mod_target_status_20260510.md`

Newer state/evidence read:

- `config\tku_paths.local.json`
- `config\tku_paths.example.json`
- `tools\tku_project_paths.py`
- `reports\tku_editor_first\known_universe_recovery_report_20260511.md`
- `reports\tku_editor_first\tku_packaged_mod_inspection_20260511.md`
- `reports\tku_editor_first\tku_packaged_mod_inspection_20260511.json`
- `reports\tku_editor_first\ue4_starmap_binding_probe_20260512.md`
- `reports\tku_editor_first\ue4_starmap_binding_probe_20260512.json`
- `reports\tku_editor_first\ue4_starmap_model_probe_20260512.md`
- `reports\tku_editor_first\ue4_starmap_model_probe_20260512.json`
- `reports\tku_editor_first\ue4_initializer_defaults_probe_20260512.md`
- `reports\tku_editor_first\ue4_initializer_defaults_probe_20260512.json`
- `reports\tku_editor_first\ue4_save_assets_to_mod_20260512.md`
- `reports\tku_editor_first\ue4_save_assets_to_mod_20260512.json`
- `reports\tku_editor_first\tku_version_metadata_20260512-092237.md`
- `reports\tku_editor_first\tkucompat_live_test_deploy_20260512-092253.md`
- `reports\tku_editor_first\tku_content_mirror_20260512-092307.md`
- `reports\tku_editor_first\tku_content_mirror_20260512-092307.json`
- Live `MW5Mercs\Mods\modlist.json`
- Live/editor `TKUCompatEditorPatch\mod.json` files

## Accepted Facts

- Original TKU build 38 root `/Game` substitutions are unsafe as a group.
- `TKUEvidenceCorePluginOnly` is the stable floor, but it is feature-incomplete.
- The active live test profile now enables `TKUEvidenceCorePluginOnly` and `TKUCompatEditorPatch`.
- An editor-authored `TKUCompatEditorPatch` exists and has been packaged, deployed, and mirrored into `Content\Paks`.
- The editor-authored `StarMapPawn` override is runtime-proven active: the starmap opens and pans farther than vanilla.
- New-career testing after the pawn repair still showed missing periphery/clan stars and vanilla faction overlays.
- Save-cache is no longer the leading explanation for missing stars.
- The active 8-file content mirror now includes `MW5_InnerSphereData`, `StarSystemGenerator`, `StarMap`, and `StarMapPawn` under a content-root mount matching the legacy loose override style.
- No MW5 or UE4Editor process was running during this verification.

## Ruled-Out Checklist

Do not repeat these paths:

- Broad restoration of original TKU root `/Game` assets.
- Direct cooked substitution of old TKU `StarMap.umap`.
- Direct cooked substitution of old TKU `StarMapActor`.
- Direct cooked substitution of old TKU `StarSystemBody`.
- Direct cooked substitution of old TKU `BaseStarMapBorderActor` or dated border actors.
- Direct cooked substitution of old root faction/employer data as a group.
- Direct cooked old `StarMapPawn` substitution.
- Direct cooked current-package `StarMapPawn` CDO patching.
- Treating title-screen boot as validation.
- Treating pak path manifests as proof of Blueprint/runtime compatibility.
- Blaming `vonBiomes` or the loose required starmap override pak as sufficient causes for the original `0x4C` fatal crash.

Important nuance: the editor-authored `StarMapPawn` override is not the same failed path as the earlier cooked pawn substitutions. The editor-authored pawn override is currently runtime-positive for starmap opening and expanded pan range.

## Dependency Model

Current dependency model for the active patch:

- `MW5GameMode` and `CampaignMode` default `default_inner_sphere_class` point to `/Game/InnerSphereData/StarSystemGenerator.StarSystemGenerator_C`.
- The `TKUCompatEditorPatch` override of `StarSystemGenerator` is editor-visible and callable.
- `StarSystemGenerator.generate_inner_sphere_data` returns 3,974 systems in the initializer probe.
- The `MW5_InnerSphereData` override resolves to `/ModOverride/TKUCompatEditorPatch/InnerSphereData/MW5_InnerSphereData` with 3,974 rows.
- The `StarMap` override resolves to `/ModOverride/TKUCompatEditorPatch/Levels/FrontEnd/StarMap` with 3,973 `StarSystemBody_C` actors, ID range `1..7921`.
- The placed `StarMapActor` in that level still uses current `/Game/UI/FrontEnd/Starmap/StarMapActor.StarMapActor_C`.
- `StarMapSceneManager` references that current `StarMapActor_C` and current `/Game/UI/FrontEnd/StarMapPawn.StarMapPawn_C`.
- `StarMapActor.star_system_body_look_up` is empty in editor/CDO probes; that is expected to be runtime-populated and is not by itself a failure.
- A freshly constructed transient `MWStarMapModel` returns empty arrays and zeroed `StarSystemInfo`; that proves uninitialized native models are not useful as standalone evidence.

## Package Reference Trace

Active root package providers for the target assets:

| Provider | Mount | Relevant entries |
| --- | --- | --- |
| Base game pak | `../../../` | `MW5_InnerSphereData`, `StarSystemGenerator`, `StarMap`, `StarMapPawn` |
| Original loose TKU override | `../../../MW5Mercs/Content/` | `MW5_InnerSphereData`, `StarMap` |
| Active TKU compat content mirror | `../../../MW5Mercs/Content/` | `MW5_InnerSphereData`, `StarSystemGenerator`, `StarMap`, `StarMapPawn` |
| Deployed mod pak | mod package | `MW5_InnerSphereData`, `StarSystemGenerator`, `StarMap`, `StarMapPawn`, asset registry |

The latest content mirror SHA256 is `AC3FBAFEE4E4B7F36A65C5EBAC6D8FB3B5DD0D02300674CED702F18983082E13` and contains eight expected files. This mirror was created before this report; this report does not authorize a new build.

## Missing And Stale References

No new missing hard asset reference was found in the 2026-05-12 editor probes; the recorded `errors` arrays are empty for the binding/model probes.

Remaining missing/blocked evidence:

- No runtime result is recorded yet for the latest 8-file mirror containing `StarSystemGenerator`.
- UE4SS runtime instrumentation is currently blocked by signature scanning failure (`FText::FText(FString&&)` missing and PS scan timeout), so it is not a usable next discriminator without separate UE4SS repair.
- 114 legacy TKU overlay/constellation soft paths remain absent from loose editor content, current base-game pak, and original TKU pak; they are migration clues, not restoration candidates.
- There is still no current-schema `MWClusterDataAsset` migration policy for generic TKU `RepairSystem` and `CareerCluster`, or for `ClanConflict`, `RepairSystem_Clan`, `RepairSystem_Custom`, and `PirateKingdoms`.
- The source plugin `Plugins\TKUCompatEditorPatch\mod.json` has stale editor/source metadata, while packaged/live metadata has been corrected.

## Current-vs-TKU Schema Comparison

- Current runtime/editor DataTable: 2,173 rows.
- Original TKU DataTable parse: 3,929 rows.
- Merged current-plus-TKU-additions DataTable: 3,974 rows.
- Merged candidate preserves current rows and adds 1,801 TKU-only rows.
- Original TKU coordinate span projects through the current formula to approximately level X `35305..66633` and level Y `36020..66538`.
- Current vanilla level has 2,172 placed `StarSystemBody_C` actors.
- Current editor-authored TKUCompat level has 3,973 placed `StarSystemBody_C` actors.
- Current placement formula remains: `LevelX = 51336 + 8 * PosY`; `LevelY = 51039 + 8 * PosX`.
- Raw original TKU import remains risky because shared rows differ heavily in positions and 468 cluster assignments.
- No TKU enum values were missing from observed current enum value sets after the parser suffix fix.

## Evidence-Only Assets

Treat these as evidence, not safe restoration candidates:

- Original cooked TKU `StarMap.umap`.
- Original cooked TKU `StarMapActor`.
- Original cooked TKU `StarSystemBody`.
- Original cooked TKU `StarMapPawn`.
- Original cooked TKU `BaseStarMapBorderActor` and dated border actor chain.
- Original cooked root faction/employer data as a group.
- Legacy TKU overlay/constellation mesh paths, especially the 114 unavailable paths.
- Quarantined blind-build artifacts.
- UE4SS probe output from the failed 2026-05-12 attempt.

## Stale Or Contradictory Docs

- `TKU_COMPAT_PATCH_ROADMAP.md`, `tku_continuation_handoff_20260510.md`, and `reference_trace_manifest.md` are stale where they say active `modlist.json` enables only `TKUEvidenceCorePluginOnly`.
- `editor_authoring_runbook_20260510.md` is stale where it says manual Create Mod is still the first gate; `TKUCompatEditorPatch` now exists.
- `editor_mod_target_status_20260510.md` contradicts itself: it says the dedicated compatibility mod exists and manual Create Mod is not required, but its next gate text still says to create it.
- `known_universe_recovery_report_20260511.md` has older intermediate next-step text, but its later 2026-05-12 sections supersede that.
- Packaged/live metadata was corrected to `1.13.378`, while the source plugin `mod.json` remains stale.

## Implementation Gate

Additional build authorization: `false`.

Reason:

- The already-deployed 8-file mirror has not yet been runtime-validated in the repo evidence.
- The star-population failure after the earlier pawn repair was not solved by proof of editor-side DataTable/level correctness alone.
- The overlay track still lacks a current-schema cluster mapping policy.

Runtime validation of the existing active test state is authorized, provided rollback is preserved first.

Expected active test state:

- Enabled mods: `TKUEvidenceCorePluginOnly`, `TKUCompatEditorPatch`.
- Active loose original override: `MW5Mercs-zKnownUniverseStarmap.pak` remains present and unmodified.
- Active compat content mirror: `MW5Mercs-zzzzTKUCompatEditorPatch.pak`, SHA256 `AC3FBAFEE4E4B7F36A65C5EBAC6D8FB3B5DD0D02300674CED702F18983082E13`.

## Runtime Test Plan

Minimum next test:

1. Launch MW5 with no editor process running.
2. Confirm only `TKUEvidenceCorePluginOnly` and `TKUCompatEditorPatch` are enabled.
3. Start a fresh career.
4. Open the starmap from the hangar UI.
5. Confirm there is no first-person-hangar misroute.
6. Pan beyond vanilla bounds.
7. Check whether TKU-added periphery/clan-area stars appear.
8. Check whether the core star density matches the 3,973 placed-body expectation more closely than vanilla.
9. Check whether overlay remains vanilla; this is expected until Track A1 cluster migration.
10. Exit and inspect logs/crash timestamps.

Decision after test:

- If stars appear, root package precedence plus `StarSystemGenerator` mirroring is confirmed; next design gate becomes Track A1 `MWClusterDataAsset` migration.
- If stars remain missing, package precedence is not sufficient; next evidence target is runtime `StarMapActor`/`StarSystemGenerator` initialization and the live `MWStarMapModel` data source, not another DataTable or map rebuild.
- If the starmap misroutes or crashes, rollback immediately and compare against the editor-authored pawn-positive runtime result.

## Rollback

Do not touch original TKU paks.

Rollback options:

- Latest mirror rollback: restore `reports\tku_editor_first\backups\content_mirror_20260512-092307\MW5Mercs-zzzzTKUCompatEditorPatch.pak` over the live mirror.
- Full content-mirror rollback: remove only `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak`.
- Deployed mod rollback: use `reports\tku_editor_first\backups\live_mod_before_deploy_TKUCompatEditorPatch_20260512-092253` for the deployed mod folder if needed.
- The original loose `MW5Mercs-zKnownUniverseStarmap.pak` must remain untouched unless a separate reversible isolation test explicitly records a rename/restore.

## Commands Run

Representative verification commands run in this continuation:

- `Get-Location; git status --short --branch`
- `Get-ChildItem -Force`
- `Get-ChildItem -Path reports\tku_editor_first -Force`
- `Get-Content -Raw` for all required handoff files listed above.
- `Get-Content -Raw config\tku_paths.local.json`
- `Get-Content -Raw tools\tku_project_paths.py`
- Path existence check via PowerShell `Test-Path` over `config\tku_paths.local.json`.
- `Get-Content -Raw "E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.json"`
- `Get-Process -Name MW5Mercs-Win64-Shipping,MW5Mercs,UE4Editor,UE4Editor-Cmd -ErrorAction SilentlyContinue | Select-Object ProcessName,Id,Path`
- `Get-ChildItem` over live mods, editor plugin, editor packaged mod, and content paks.
- `Get-FileHash -Algorithm SHA256` for the active loose TKU override, active content mirror, and packaged/deployed `TKUCompatEditorPatch.pak`.
- Python JSON summary commands over `ue4_starmap_model_probe_20260512.json`, `ue4_starmap_binding_probe_20260512.json`, `ue4_initializer_defaults_probe_20260512.json`, `tku_packaged_mod_inspection_20260511.json`, and `tku_content_mirror_20260512-092307.json`.

