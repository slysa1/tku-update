# TKU Repair Track Decision - 2026-05-10

## Scope

This decision follows the focused non-mutating MW5 Mod Editor probes:

- `reports\tku_editor_first\ue4_mod_types_probe.md`
- `reports\tku_editor_first\ue4_starmap_bounds_clusters_probe.md`

No runtime pak was built. No original TKU pak, loose TKU starmap pak, or game asset was edited.

## Verified State

- Live `MW5Mercs\Mods\modlist.json` still enables only `TKUEvidenceCorePluginOnly`.
- No MW5 or MW5 Mod Editor process was running after the commandlet probes completed.
- The stable runtime floor remains root-stripped TKU plugin content only.

## API Gate

Editor commandlet Python is approved for non-mutating inspection and data export only.

The focused API probe found `MWModPluginInfo`, `ModPackageArgs`, `MWModUtils`, and `MWModEditorWidget.package_mod(args)`, but no direct module-level `CreateMod`, `SaveToMod`, `SaveTo`, or `PackageMod` symbol. `MWModEditorWidget` is abstract from commandlet construction, and no active mod plugin was visible to the commandlet.

Decision: first safe `Create Mod` and `Save To Mod` authoring must use the MW5 Mod Editor UI unless a later focused widget-spawn or AutomationTool workflow proves a scripted path.

## Bounds Track

Selected next bounds track: Track B2, inspect and reconstruct through current `StarMapActor`, `StarMap` level generation/placement, and source-to-runtime InnerSphere data import before authoring another pawn-only patch.

Evidence:

- Current `/Game/Levels/FrontEnd/StarMap` has 2,182 actors, including 2,172 `StarSystemBody_C` actors.
- Current runtime CSV has 2,173 rows with vanilla-scale coordinates.
- Editor source JSON has 3,446 systems with much wider coordinates.
- Current `StarMapPawn` still exposes the known vanilla pan/zoom defaults, but previous cooked pawn substitutions broke starmap opening.

Decision: do not build another pawn-only bounds patch next. Expanded TKU map support likely requires level/body generation or data import work in addition to camera bounds.

## Overlay Track

Selected next overlay track: Track A1, migrate or recreate current-schema `MWClusterDataAsset` territory data.

Evidence:

- Current editor project has 79 `MWClusterDataAsset` assets.
- Those assets contain 815 system memberships, 74 overlay meshes, and 31 constellation meshes.
- `EUW_MigratePlaceClusterTOIsToClusterAssets` depends on `PlaceClusterToi` assets and `/Game/InnerSphereData/MW5_InnerSphereData`.
- Original TKU build 38 has no modern `/Game/Campaign/Clusters` assets, so old cooked border or overlay restoration is not the correct first repair path.

Decision: inspect the migration utility graph in the editor UI before running it. Treat it as a recipe until its write targets, rename behavior, and source assumptions are understood.

## Build Gate

No new build is authorized yet.

Next evidence tasks:

1. Inspect `EUW_MigratePlaceClusterTOIsToClusterAssets` graph in the MW5 Mod Editor UI without running it.
2. Trace source-to-runtime import for `MW5_InnerSphereData.json` / `.csv` and the placed `StarSystemBody_C` generation path.
3. Inspect current `StarMapActor` graph/defaults around star body lookup, cluster material use, border mesh generation, and data-table reads.
4. Only after those inspections, choose a narrowly scoped editor-authored `ModOverride` candidate and write a build manifest before packaging.
