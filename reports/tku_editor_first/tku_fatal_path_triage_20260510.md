# TKU Fatal Career-Load Path Triage - 2026-05-10

## Runtime Pin

- Repro path: Single Player -> New Career -> Davion -> loading screen completes -> fatal error before hangar control.
- Crash signature: `EXCEPTION_ACCESS_VIOLATION reading address 0x000000000000004c`.
- Repeated call-stack hash: `0039C4B8A7510FAC9074DFC881C752315D75F42F`.
- The same crash reproduced with `vonBiomes` disabled.
- The same crash reproduced with only `TheKnownUniverse` enabled and the loose required override pak temporarily disabled.
- With zero enabled mods and the loose required override pak present, Davion career, vanilla starmap, and mechbay loaded successfully.

Conclusion: `TheKnownUniverse.pak` is sufficient to trigger the fatal career-load path. The loose required override pak and `vonBiomes` are not sufficient causes.

## Current Asset Evidence

- TKU `MW5_InnerSphereData` contains the Davion/Haynesville career-start strings and references old border mesh paths under `/Game/Campaign/CampaignArcs/BorderChanges/_common/FactionBorderMeshes/...`.
- TKU `StarMap.umap` hard-references TKU `StarMapActor` and `StarSystemBody` via `/ModOverride/TheKnownUniverse/...` package strings.
- Structured UE4 package-table parsing confirms the loose required override `StarMap.umap` binds to current `/Game/UI/FrontEnd/Starmap/StarMapActor` and `/Game/UI/FrontEnd/Starmap/StarSystemBody`, while TKU's mod-pak `StarMap.umap` binds to `/ModOverride/TheKnownUniverse/...` starmap classes.
- TKU `StarMapActor` references `StarSystemBody`, `MWStarMapBorderActor`, `MWStarMapBorderAsset`, and `MWStarMapModel`.
- TKU `StarSystemBody` references `MWStarSystemBody`, `MWStarMapModel`, and cluster overlay/constellation logic strings.
- Structured UE4 package-table parsing shows current vanilla `StarSystemBody` imports `MWClusterDataAsset` and exports `ResetClusterMeshes`, `GetClusterOverlayMesh`, and `GetClusterConstellationMesh`; original TKU `StarSystemBody` lacks those current cluster-data hooks.
- TKU `BaseStarMapBorderActor` references `MWStarMapBorderActor`.
- Current vanilla editor dump shows the vanilla starmap stack still uses native parents `MWStarMap`, `MWStarMapPawn`, `MWStarSystemBody`, and `MWStarMapBorderActor`.
- Current vanilla `StarMap` is referenced by Leopard and mission-hub area assets, so starmap classes can be touched during career-load, before the player manually opens the starmap.
- Current vanilla editor data uses `/Game/Campaign/Clusters/*_ClusterAsset` `MWClusterDataAsset` assets. Original TKU build 38 has no modern cluster assets.

## Priority Hypotheses

1. TKU's old starmap stack is constructing during career hub load and dereferencing stale or missing data from the old `MW5_InnerSphereData` / border / cluster-overlay model.
2. TKU's old `StarSystemBody` and `StarMapActor` Blueprints predate the current `MWClusterDataAsset` starmap overlay pipeline and are incompatible with current native starmap expectations.
3. TKU's old `MW5_InnerSphereData` schema or references are incompatible with current native starmap code, especially around cluster overlays, border meshes, and modern `MWClusterDataAsset` expectations.
4. TKU's old root `EmployerInfoData`, `SystemFactionChanges`, or root faction/employer assets may create invalid ownership/faction objects during the Davion/Haynesville start, but this is secondary until the starmap/data constructor path is inspected.
5. The crash is not primarily a load-order issue. The same fatal path appears when TKU is the only enabled mod and the loose required override is inactive.

## Immediate Inspection Targets

1. `/Game/Levels/FrontEnd/StarMap`
2. `/Game/UI/FrontEnd/Starmap/StarMapActor`
3. `/Game/UI/FrontEnd/Starmap/StarSystemBody`
4. `/Game/UI/FrontEnd/StarMapPawn`
5. `/Game/InnerSphereData/MW5_InnerSphereData`
6. `/Game/InnerSphereData/Updated/SystemFactionChanges`
7. `/Game/InnerSphereData/Updated/EmployerInfoData`
8. `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
9. `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015`
10. `/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`

## Evidence-Gated Next Step

Do not run another runtime toggle or rebuild yet. The next useful step is to get structured data from the cooked TKU root assets that terminal string scans cannot provide:

- Blueprint parent/class tags and imports for the TKU root starmap classes.
- Default values for TKU `StarMapPawn` bounds and starmap actor references if recoverable.
- Data-table row structure and Davion/Haynesville rows from TKU `MW5_InnerSphereData` / `SystemFactionChanges`.
- Whether TKU cooked assets can be inspected with a local Unreal asset tool without importing them into the editor project.
- Current vanilla `StarMapActor` / `StarSystemBody` graph/default evidence around `MWClusterDataAsset`, cluster mesh creation, and owner/faction display.

Local tooling can now read import/export/package tables structurally, but not Blueprint bytecode or DataTable rows. If editor/tooling cannot recover or recreate those remaining pieces, abandon pak surgery for this stack and recreate the needed starmap/data behavior in the MW5 Mod Editor from current vanilla assets.

## Tooling Status

- MW5 Mod Editor command-line Python inspection works with:
- `UE4Editor-Cmd.exe <project> -run=pythonscript "-script=exec(open(r'<script>').read())" -unattended -nop4 -nosplash`
- `reports\tku_editor_first\ue4_editor_asset_dump.md` is refreshed from the current vanilla editor project.
- `reports\tku_editor_first\tku_crash_surface_scan.md` identifies TKU crash-surface candidates but remains string-only evidence.
- `reports\tku_editor_first\tku_cooked_package_refs.md` adds package-table evidence for imports, exports, native parents, and hard package references.
- `reports\tku_editor_first\tku_structured_reference_findings_20260510.md` summarizes the new evidence and current recommendation.
- No third-party tools have been installed.

## What Not To Do

- Do not make a new compatibility pak from this triage alone.
- Do not restore the disabled load-order shim.
- Do not delete or overwrite original TKU files.
- Do not keep toggling broad groups of cooked assets as a substitute for structured inspection.
