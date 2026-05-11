# TKU Structured Reference Findings - 2026-05-10

## Purpose

Record the first non-string, package-table evidence for the repeated TKU Davion career-load fatal error.

This report was produced after the user reported another fatal error. No new runtime toggles or rebuilds were performed. The latest crash context still matched the known TKU-only `0x4C` crash signature, and the live `modlist.json` remained the safe all-disabled control profile.

## New Tooling

- Added read-only package parser: `tools\tku_reference_audit\parse_ue4_package_refs.py`
- Generated structured report: `reports\tku_editor_first\tku_cooked_package_refs.md`
- Generated machine-readable report: `reports\tku_editor_first\tku_cooked_package_refs.json`

The parser reads UE4 cooked package summaries, name maps, import maps, export maps, native parent references, and hard package references from `.uasset` / `.umap` files inside the original paks. It does not decode Blueprint bytecode or DataTable row payloads.

## Key Findings

### 1. The safe loose override and the unsafe TKU mod map do not bind to the same starmap class packages

- `MW5Mercs-zKnownUniverseStarmap.pak` `/Game/Levels/FrontEnd/StarMap.umap` hard-references current vanilla `/Game/UI/FrontEnd/Starmap/StarMapActor` and `/Game/UI/FrontEnd/Starmap/StarSystemBody`.
- `TheKnownUniverse.pak` `/Game/Levels/FrontEnd/StarMap.umap` hard-references `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarMapActor` and `/ModOverride/TheKnownUniverse/UI/FrontEnd/Starmap/StarSystemBody`.
- This explains why the loose override can be safe alone, while enabling TKU reintroduces the fatal path through TKU's old starmap classes.

### 2. TKU `StarSystemBody` is structurally older than current vanilla

- Current vanilla `StarSystemBody` imports `/Script/MechWarrior.MWClusterDataAsset`.
- Original TKU `StarSystemBody` does not import `MWClusterDataAsset`.
- Current vanilla `StarSystemBody` exports `ResetClusterMeshes`, `GetClusterOverlayMesh`, and `GetClusterConstellationMesh`.
- Original TKU `StarSystemBody` lacks those exports.

Interpretation: TKU build 38 predates the current cluster-data overlay pipeline. The missing non-major overlays are likely not recoverable by restoring old cooked border actors alone.

### 3. TKU `StarMapActor` is also older and bound to TKU package paths

- Both current vanilla and TKU `StarMapActor` inherit from native `MWStarMap`.
- TKU `StarMapActor` hard-references TKU `StarSystemBody` through `/ModOverride/TheKnownUniverse/...`.
- Current vanilla `StarMapActor` references current `/Game/...` starmap assets and imports current native functions such as `/Script/MechWarrior.MWStarMap.MouseOverStarSystem`.
- TKU exports `MouseOverStarSystem` and `OnMouseOverStarSystem__DelegateSignature`; current vanilla exports `SetMouseOverStarSystem` instead.

Interpretation: the fatal crash is likely not a simple missing native parent. It is more likely stale Blueprint graph/default behavior or stale class interaction with current native starmap and cluster systems.

### 4. `StarMapPawn` is not the immediate fatal suspect

- Current vanilla and original TKU `StarMapPawn` have matching import/export structure and both inherit from `MWStarMapPawn`.
- It may still control expanded map pan/zoom bounds, but it is not the strongest crash candidate from package-table evidence.

### 5. `BaseStarMapBorderActor` is a later overlay risk, not the first fatal target

- Current vanilla and TKU `BaseStarMapBorderActor` both inherit from `MWStarMapBorderActor`.
- TKU adds an `AddDepthStencil` export that vanilla does not have.
- Previous mixed restores produced a `Could not find SuperStruct BaseStarMapBorderActor_C` failure, so old border actors remain unsafe unless recreated or reparented in the editor.

## Updated Asset Classification

| Asset | Classification | Reason |
| --- | --- | --- |
| `/Game/Levels/FrontEnd/StarMap` from loose override | Conditionally safe evidence | It binds to current `/Game/...` starmap classes and passed the override-only Davion career load. |
| `/Game/Levels/FrontEnd/StarMap` from TKU mod pak | Unsafe direct restore | It binds to `/ModOverride/TheKnownUniverse/...` starmap classes and TKU-only reproduces the fatal. |
| `/Game/UI/FrontEnd/Starmap/StarMapActor` from TKU | Unsafe old class stack | It binds to TKU `StarSystemBody` and diverges from current vanilla function/import shape. |
| `/Game/UI/FrontEnd/Starmap/StarSystemBody` from TKU | Unsafe old class stack | It lacks current `MWClusterDataAsset` import and cluster-mesh exports. |
| `/Game/UI/FrontEnd/StarMapPawn` from TKU | Needs property inspection | Import/export structure matches vanilla; bounds defaults may still be useful. |
| `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor` from TKU | Unsafe until editor-authored | Parent exists, but prior mixed restores failed and TKU has extra graph/export behavior. |
| `MW5_InnerSphereData`, `SystemFactionChanges`, `EmployerInfoData` | Needs row/schema inspection | Package-table structure is not enough; rows must be inspected or exported with editor/asset tooling. |
| `/Game/Campaign/Clusters/*` | Needs recreation/migration | Current vanilla uses `MWClusterDataAsset`; original TKU has no modern cluster assets. |

## Evidence-Gated Next Step

Do not run another broad runtime toggle. The next justified action is to inspect or recreate a current-compatible starmap class path:

1. Use the MW5 Mod Editor to inspect current vanilla `StarMapActor` and `StarSystemBody` defaults/graphs related to cluster assets, overlays, and star-system body creation.
2. Inspect `StarMapPawn` defaults for pan/zoom bounds and compare against TKU strings/defaults if recoverable.
3. Inspect the cluster migration utility and representative `MWClusterDataAsset` assets.
4. If editor evidence confirms that current vanilla starmap classes can consume wide StarMap and migrated cluster data, authorize a minimal evidence build that neutralizes TKU's old starmap classes while keeping or recreating TKU data through current schemas.

## What This Rules Out

- The fatal error is not primarily `vonBiomes`.
- The fatal error is not the loose required override pak by itself.
- The fatal error is not explained by a missing native parent class on `StarMapActor`, `StarSystemBody`, or `StarMapPawn`; the native parents still exist.
- Restoring TKU's old starmap Blueprint classes is not a viable first fix.
- Restoring old border actors before cluster/data migration is not evidence-backed.

## First Concrete Recommendation

Open the MW5 Mod Editor evidence path next, not the game runtime: inspect current vanilla `StarSystemBody`, `StarMapActor`, `StarMapPawn`, representative `MWClusterDataAsset` assets, and `EUW_MigratePlaceClusterTOIsToClusterAssets`. The first build should be a current-schema starmap/cluster migration build, not another old-asset restore.
