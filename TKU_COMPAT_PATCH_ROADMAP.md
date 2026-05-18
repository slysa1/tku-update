# The Known Universe Compatibility Roadmap

## Goal

Deliver a local compatibility path for `TheKnownUniverse` (`TKU`) on `MW5 v1.13.378` that is stable for new-career start, early starmap use, travel, contracts, saving, and the user's desired mod stack.

This file is intentionally a compact decision dashboard. Detailed mod/package state lives in [reports/tku_editor_first/tku_current_mod_state.md](reports/tku_editor_first/tku_current_mod_state.md), and historical evidence stays in the linked reports.

## Current State

- Strategy: editor-first repair, not blind cooked-pak restoration. See [reports/tku_editor_first_strategy.md](reports/tku_editor_first_strategy.md).
- Clean TKU evidence source: restored original Nexus build 38; original TKU paks and loose required override must remain unedited.
- Stable floor: `TKUEvidenceCorePluginOnly` loads career and opens the starmap, but it keeps vanilla-width map behavior and incomplete/vanilla territory overlays.
- Active repo-recorded test state: `TKUEvidenceCorePluginOnly` plus packaged `TKUCompatEditorPatch`, with a late-loading content mirror. Details and hashes are in [reports/tku_editor_first/tku_current_mod_state.md](reports/tku_editor_first/tku_current_mod_state.md).
- Runtime-positive patch evidence: editor-authored `StarMapPawn` opens the starmap and pans farther than vanilla.
- Remaining blocker: TKU-added periphery/clan stars and non-major faction overlays are not yet proven restored.
- Next safe action: runtime-validate the already-deployed 8-file content mirror, then inspect logs/crash timestamps. Do not build a new patch before that result is recorded.

## What Is Proven

- The loose required TKU starmap override pak is not fatal by itself.
- The original `TheKnownUniverse.pak` is sufficient to reproduce the repeated `0x4C` new-career fatal crash.
- Original TKU build 38 predates the current `MWClusterDataAsset` overlay pipeline.
- Old cooked root `/Game` starmap, border, and base-class substitutions are unsafe as a group.
- Broad vanilla fallback can make the game load while bypassing core TKU starmap value.
- Editor-authored current-parent assets are safer than direct cooked TKU substitutions.
- Save-cache is no longer the leading explanation for missing stars after the pawn repair.

## Do Not Repeat

- Do not directly restore old cooked TKU `StarMap.umap`, `StarMapActor`, `StarSystemBody`, `StarMapPawn`, `BaseStarMapBorderActor`, dated border actors, or old root faction/employer assets.
- Do not treat title-screen boot as validation.
- Do not treat pak path manifests as proof of Blueprint/runtime compatibility.
- Do not blame `vonBiomes` or the loose starmap override as sufficient causes for the original crash.
- Do not edit original TKU paks, the original loose required override, quarantined failed builds, or rollback artifacts in place.
- Do not use source-side `Plugins\TKUCompatEditorPatch\mod.json` as the authority for `gameVersion` or load order; it was stale in the 2026-05-12 verification, while packaged/live metadata was corrected.

## Working Hypothesis

The active editor-authored patch is mounting at least the `StarMapPawn` override, but visible star population still depends on either root package precedence or a current runtime data path beyond the authored DataTable/map package. Territory overlays are a separate current-schema cluster migration problem.

## Next Gate

1. Launch MW5 with the isolated test profile: `TKUEvidenceCorePluginOnly` and `TKUCompatEditorPatch`.
2. Confirm the content mirror `MW5Mercs-zzzzTKUCompatEditorPatch.pak` is active and the original `MW5Mercs-zKnownUniverseStarmap.pak` is untouched.
3. Start a fresh career, open the starmap, pan beyond vanilla bounds, and check whether TKU-added periphery/clan stars appear.
4. Exit after the result is clear and inspect logs/crash timestamps.
5. Record the result in `reports/tku_editor_first/`.

Decision after the gate:

- If TKU-added stars appear, root package precedence plus `StarSystemGenerator` mirroring is confirmed; move next to Track A1 `MWClusterDataAsset` migration.
- If stars remain missing, inspect runtime `StarMapActor`, `StarSystemGenerator`, and live `MWStarMapModel` initialization rather than rebuilding the same DataTable/map assets again.
- If the starmap misroutes, hangs, or crashes, roll back the content mirror and compare against the editor-authored pawn-positive runtime result.

## Active Tracks

- Track B2, editor-authored star population and bounds repair: active. Editor-authored pawn bounds work is runtime-positive; DataTable/map/generator runtime source remains unresolved.
- Track A1, current-schema cluster overlay migration: pending. Needs current-schema `MWClusterDataAsset` mapping policy for TKU legacy clusters such as `RepairSystem`, `CareerCluster`, `ClanConflict`, `RepairSystem_Clan`, `RepairSystem_Custom`, and `PirateKingdoms`.
- Desired mod-stack validation: pending until TKU-only/editor-authored gates pass. Named scope includes `ModOptions`, `BetterMissionChoices`, `Coyotesmission`, `PurchaseSalvage`, `SimpleZoom`, `BattleFXEnhanced`, `BattleFXPatch`, TKU, and the compatibility patch.

## Safety Rules

- Keep the original TKU build 38 folder and paks as evidence, not mutation targets.
- Keep failed blind-build artifacts in `codex_quarantine/tku_failed_compat_20260510`.
- Use MW5 Mod Editor `Save To Mod` / `ModOverride` for same-path game-asset substitutions.
- Use plugin `Content` for new TKU data, helper assets, factions, and custom tables.
- Package only from a written asset manifest and preserve rollback before live deployment.
- Validate new career, starmap open, pan/zoom, ownership, overlays, travel, contracts, save/reload, and crash-folder timestamps before claiming success.

## Success Definition

The roadmap is complete only when:

- TKU or a locally rebuilt TKU-compatible replacement is enabled.
- Original backups remain preserved.
- New career start and early starmap gameplay work without the recurring `0x4C` fatal crash.
- Steiner/Lyran ownership remains correct.
- Expanded map bounds and territory overlay behavior are restored or explicitly documented as deferred.
- The named local mod stack remains usable, including `BattleFXEnhanced` with `BattleFXPatch`.
- The final asset manifest explains why each patched or rebuilt asset is compatible.

## Evidence Index

- Current mod/package/deploy state: [reports/tku_editor_first/tku_current_mod_state.md](reports/tku_editor_first/tku_current_mod_state.md).
- Latest continuation gate: [reports/tku_editor_first/codex_re_continuation_gate_20260512.md](reports/tku_editor_first/codex_re_continuation_gate_20260512.md).
- Latest state verification: [reports/tku_editor_first/codex_re_state_verification_20260512.md](reports/tku_editor_first/codex_re_state_verification_20260512.md).
- Runtime isolation matrix: [reports/tku_runtime_isolation_20260510.md](reports/tku_runtime_isolation_20260510.md).
- Editor-first strategy: [reports/tku_editor_first_strategy.md](reports/tku_editor_first_strategy.md).
- Repair candidate manifest: [reports/tku_editor_first/tku_editor_repair_candidate_manifest_20260510.md](reports/tku_editor_first/tku_editor_repair_candidate_manifest_20260510.md).
- Import candidates: [reports/tku_editor_first/tku_inner_sphere_import_candidates_20260510.md](reports/tku_editor_first/tku_inner_sphere_import_candidates_20260510.md).
- Packaged mod inspection: [reports/tku_editor_first/tku_packaged_mod_inspection_20260511.md](reports/tku_editor_first/tku_packaged_mod_inspection_20260511.md).
- Latest live deploy report: [reports/tku_editor_first/tkucompat_live_test_deploy_20260512-092253.md](reports/tku_editor_first/tkucompat_live_test_deploy_20260512-092253.md).
- Latest content mirror report: [reports/tku_editor_first/tku_content_mirror_20260512-092307.md](reports/tku_editor_first/tku_content_mirror_20260512-092307.md).
