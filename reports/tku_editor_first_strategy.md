# TKU Editor-First Compatibility Strategy

## Purpose

This document replaces the previous black-box rebuild loop with an evidence-first workflow for TheKnownUniverse (TKU) compatibility. The next phase should not toggle cooked assets in and out of paks until we have traced the relevant asset references in the MW5 Mod Editor or equivalent Unreal asset tooling.

The working assumption is now conservative: TKU's missing functionality is probably not recoverable by path-level pak surgery alone. The starmap behavior, faction territory overlay, expanded map bounds, and several faction ownership paths appear to be controlled by cooked maps, Blueprint classes, data tables, and material bindings whose internal references are not visible from terminal manifests.

## Current Disk State

- Workspace: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries`
- Live mod folder: `MW5Mercs\Mods\TheKnownUniverse`
- Current live TKU build: original Nexus build 38, restored on 2026-05-10.
- Original unaltered TKU source for evidence: `MW5Mercs\Mods\TheKnownUniverse`.
- Source discipline: use restored build-38 TKU files for evidence. Use quarantined blind-build artifacts only to document failed history.
- Quarantine root for failed blind-build artifacts: `codex_quarantine\tku_failed_compat_20260510`.
- Active loose required starmap override: `MW5Mercs\Content\Paks\MW5Mercs-zKnownUniverseStarmap.pak`.
- Disabled load-order shim: `MW5Mercs\Mods\TheKnownUniverse\Paks\zzzz_MW5Mercs-zKnownUniverseStarmap.loadorder-test.pak.disabled-20260510`.
- Current live TKU pak contents: original root `/Game` overrides plus `/Plugins/TheKnownUniverse` content.
- Last useful baseline from testing: build 58, plugin-only with zero root `/Game` assets.
- MW5 Mod Editor Guide is present at `MW5Mercs\Mods\MW5Mercs_Mod_Editor_Guide_(v2.3).pdf`.
- The guide was parsed with `pypdf` after it became available locally. The most relevant sections are "Creating a Substitution Mod", "Porting your existing Mod into the new Mod framework", "Changing the Load Order", and "Using Custom Data Tables".

No original backup should be edited. No disabled content pak should be deleted. Future outputs should stay under documented staging/report directories.

## Known Facts

- Original TKU crashes near startup in the modern install with `EXCEPTION_ACCESS_VIOLATION reading address 0x000000000000004c`.
- Current restored original TKU reproduces the same `0x4C` crash after Single Player -> New Career -> Davion -> loading screen completion.
- The `0x4C` crash reproduced with `vonBiomes` disabled, so `vonBiomes` is not sufficient to explain the fatal career-load crash.
- With zero enabled mods and the loose required override pak still present, a Davion career loaded successfully and the vanilla starmap and mechbay opened.
- Therefore the loose required override pak is not independently fatal; the current fatal source is TKU's mod pak content or its interaction with the loose override.
- TKU-only with the loose required override pak temporarily disabled reproduced the same `0x4C` crash and call-stack hash. This pins the primary fatal source to `TheKnownUniverse.pak`.
- Earlier `StarMapActor` / `StarSystemBody` restore attempts produced a different null access violation, `EXCEPTION_ACCESS_VIOLATION reading address 0x0000000000000000`.
- Restoring TKU `BaseStarMapBorderActor` caused a hard class load failure: `Could not find SuperStruct BaseStarMapBorderActor_C to create StarMapActor_2570_C`.
- Build 43, a conservative vanilla-root rescue, loaded into career and allowed starmap use, travel, contracts, saving, and exiting, but displayed only a dot map with missing territory overlay and incomplete ownership.
- Build 55/56/57 all showed similar results: major powers and ComStar territory overlay could appear, but Steiner/Lyran ownership was missing.
- Build 56 removed TKU `MW5_TOI_Functions` with no meaningful improvement, so that library is not the primary cause of the Steiner ownership issue.
- Build 57 removed legacy `CustomContent` with no meaningful improvement, so legacy `CustomContent` is not the primary cause of the Steiner ownership issue.
- Build 58 removed all root `/Game` assets and kept only TKU plugin content. This fixed Steiner/Lyran system ownership, but the map stayed vanilla-width and the territory overlay was still limited to the vanilla major powers plus ComStar.
- Build 59 added TKU `/Game/Levels/FrontEnd/StarMap` back on top of the plugin-only baseline and hung on the loading screen.
- The original TKU pak has substantial root `/Game` content, including starmap map/actor/pawn/body assets, faction/employer assets, data tables, border change assets, and faction materials.
- The plugin-only baseline proves that some TKU plugin data can coexist with the modern game, but it does not prove that vanilla starmap code consumes all TKU territory/bounds data.
- A clean-pak inventory of original TKU build 38 found 2,709 entries, zero `/Game/Campaign/Clusters` assets, and no scanned cooked strings mentioning `MWClusterDataAsset` or `/Game/Campaign/Clusters`.
- The only cluster-named original TKU path is `/Plugins/TheKnownUniverse/Content/Regions/War/CareerModeCustomClusters`, which references `PlaceClanConflict` and `PlaceCustomConflict`; it is not a modern cluster overlay asset set.
- The current MW5 editor project contains 261 assets under `/Game/Campaign/Clusters`, including 79 `MWClusterDataAsset` assets with `system_ids`, `cluster_faction_asset`, `cluster_overlay`, and `cluster_constellation` properties.
- Current editor runtime `MW5_InnerSphereData.csv` has 824 nonempty cluster rows, 77 unique nonempty cluster IDs, 74 cluster-overlay rows, and 31 cluster-constellation rows.
- Current editor `CampaignArcs/Regions` contains 44 `Place*` assets with cluster references. Representative assets point directly at `/Game/Campaign/Clusters/*_ClusterAsset` and expose `ClusterDataAsset` / `ClusterDataAssetId` strings.
- Forty-six current editor cluster IDs appear in original TKU's cooked `MW5_InnerSphereData` strings, including `LyranStrongholds`, `SteinerBorder`, `SteinerMarikBorder`, `TaurianCorridor`, and `OutworldsBorder`.
- Original TKU cooked strings prove old cluster IDs and mesh references are present, but they do not provide safe row-to-cluster mappings. That mapping needs editor/tool-level export before asset creation.
- The MW5 editor Python stub marks `InnerSphereMapData.cluster`, `cluster_overlay`, and `cluster_constellation` as deprecated and says those values should now be referenced from a `ClusterDataAsset`.
- The editor contains `/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets`, whose embedded text says it migrates `PlaceClusterTOI_ArcAction` and InnerSphereMap data into a `MWClusterDataAsset` file.
- The current vanilla editor `StarMap` level loads with 2,172 placed `StarSystemBody_C` actors inside vanilla-scale bounds. That supports the user's observation that the map remains bounded to vanilla width when the old TKU map is not used.

## Ruled-Out Hypotheses

- `MW5_TOI_Functions` alone causes the Steiner/Lyran ownership failure. Build 56 behaved like build 55 after removing it.
- Legacy `CustomContent` causes the Steiner/Lyran ownership failure. Build 57 behaved like build 56 after removing it.
- Root faction/employer assets are harmless. Build 58 fixed Steiner/Lyran ownership by removing all root `/Game` assets.
- TKU `StarMap.umap` can be safely restored once root data conflicts are removed. Build 59 disproved this by hanging on load.
- A successful title-screen boot is sufficient validation. Multiple failures only appeared after new career start, cinematic skip, loading, or opening the starmap.
- Pak mount order or path selection alone explains the issue. Same-name repacks and content-pak override variants changed symptoms but did not restore full functionality.
- `vonBiomes` alone explains the current fatal career-load crash. The same `0x4C` call-stack hash reproduced with `vonBiomes` disabled.
- The loose required override pak alone explains the current fatal career-load crash. It loaded a Davion career successfully with no enabled mods.
- The loose required override pak is required to reproduce the fatal career-load crash. TKU-only without that pak reproduced the same crash.
- Directly restoring old cooked Blueprint classes is safe without inspecting their parent classes, graph references, and construction-time dependencies.

## Why The Previous Approach Was Weak

- It treated cooked UE4 assets like swappable source modules. Pak manifests reveal paths, not internal Blueprint graphs, serialized object references, construction scripts, class parents, material bindings, or data-table schemas.
- It did not follow the guide's recommended porting path for old mods. The guide explicitly says existing work should be ported from pre-cooked UASSETs copied from the project folder structure, not from PAK files or cooking target output.
- Crash logs from the shipping game lack enough symbols to identify the failing property or graph node. A null access violation or load hang can identify a symptom class, but not the exact broken serialized reference.
- Map-level assets are especially opaque from the terminal. `StarMap.umap` can contain placed actors, level Blueprint logic, world settings, camera bounds, hard references to old classes, and references to dated plugin border actors.
- Several tests mixed two goals: preventing crashes and preserving TKU features. The crash-prevention path increasingly replaced TKU root assets with vanilla assets, which stabilized the game but also removed the custom map behavior we were trying to recover.
- Build scripts encoded the current guess more than a reproducible experimental ledger. Reports captured outcomes, but the live script constants moved forward, making it easy to keep testing from a failed state.
- Output symptoms were used as proxies for asset dependencies. That is not reliable when cooked Blueprints can fail because of hidden parent-class, function-signature, property-layout, or object-path mismatches.
- Broad vanilla fallback can hide the real incompatibility. It can make the game load while silently bypassing the TKU systems that implement expanded bounds or non-vanilla territory rendering.

## Guide-Backed Constraints

- The editor creates two mod content areas: `ModOverride` for modified versions of existing game assets and `<ModName> Content` for new assets.
- Substitution assets belong in `ModOverride` and must preserve the same folder structure as the original game asset.
- New assets belong in the mod's plugin `Content` folder, not in `ModOverride`.
- The guide's recommended porting workflow requires pre-cooked UASSETs from the original project layout. It specifically rejects using PAK files or cooking target folders as the source for a real port.
- The guide's basic legacy-port path, which wraps an existing PAK inside a v2 mod container, can make a mod visible to the in-game mod manager but does not make cooked assets editable, modern-schema-compatible, or internally safe.
- The guide recommends avoiding shared source table conflicts by making custom data tables as new mod content and pointing override assets at those tables. This supports a data-port strategy over whole-table replacement.
- Load order can be changed in `mod.json`, but the guide treats it as ordering behavior, not as a fix for broken Blueprint inheritance or schema drift.

## Source Of Truth Hierarchy

- First source of truth for TKU behavior: observed MW5 runtime behavior from documented builds and crash logs.
- First source of truth for MW5 mod packaging: `MW5Mercs\Mods\MW5Mercs_Mod_Editor_Guide_(v2.3).pdf`.
- First source of truth for specific MW5 assets: direct inspection in the MW5 Mod Editor, especially Blueprint parents, level references, data-table schemas, material bindings, and packaging output.
- Source of truth when unsure about Unreal Engine concepts or editor mechanics: Epic's official Unreal Engine 4.27 documentation, starting with `https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-4-27-documentation?application_version=4.27&lang=en-US`.
- Version guardrail: MW5 is UE4-era, so prefer version-matched UE4.27 documentation over current UE5 documentation. When MW5-specific behavior differs from generic UE4.27 behavior, prefer direct MW5 Mod Editor evidence and the MW5 Mod Editor Guide.

## Likely Remaining Causes

- Expanded map width and access to clan homeworlds likely depend on TKU `StarMap.umap`, `StarMapActor`, `StarMapPawn`, `StarSystemBody`, placed map actors, camera movement bounds, or starmap UI clamp values.
- Non-major faction territory overlay now appears especially likely to depend on porting TKU's old InnerSphere cluster/overlay data into current `/Game/Campaign/Clusters` `MWClusterDataAsset` assets. Original TKU lacks those modern assets entirely.
- TKU dated plugin border assets, custom border actor classes, faction color materials, material parameter bindings, and `StarMapActor` logic may still matter, but they should be investigated after the cluster-asset schema gap is traced.
- Plugin-only success with limited overlay suggests the TKU plugin assets can mount, but the modern vanilla starmap shell does not fully consume TKU's custom border/rendering data.
- Old root faction/employer assets likely conflict with the current MW5 schema or identifiers. The strongest evidence is that removing all root `/Game` assets fixed Steiner/Lyran ownership.
- The `BaseStarMapBorderActor_C` fatal error indicates a class inheritance or serialized parent mismatch. Restoring only part of that hierarchy is unsafe.
- The `StarMap.umap` loading hang suggests the map contains hard references to unsafe TKU starmap classes, missing parent classes, dated border actors, or graph logic that blocks during construction or BeginPlay.
- Expanded clan-world access probably requires both data and level work: current editor source JSON has 3,446 systems, but the loaded vanilla `StarMap` level has 2,172 placed system actors and vanilla-scale bounds.

## Recommended Editor And Tooling Workflow

- Freeze the rebuild loop. Do not produce another compatibility pak until there is a reference-trace report for the assets being changed.
- Treat build 58 as the last useful runtime baseline and build 59 as a failed experimental state. Do not use build 59 for feature conclusions except to mark TKU `StarMap.umap` unsafe as a blind restore.
- Use the MW5 Mod Editor as the primary source of truth for Blueprint parents, references, level contents, data table schemas, and material bindings.
- Follow the guide's substitution model: create modern editor-authored overrides with `Save To Mod` or equivalent editor workflow, rather than copying cooked substitutes out of a pak.
- Follow the guide's new-asset model: port new factions, custom tables, and helper assets into plugin `Content`, then point modern override assets at them.
- Treat the guide's "basic approach" for old PAKs as a packaging compatibility wrapper only. It is not a repair workflow for TKU's cooked starmap classes.
- Use local pak tooling only for inventory and packaging verification. `tools\mw5_pak.py` is useful for path counts and manifests, but it cannot answer Blueprint compatibility questions.
- Use UnrealPak, if available locally, only to list or extract known assets into a contained staging area after a clear manifest exists.
- Use the available MW5 Mod Editor at `E:\Games\MechWarrior5Editor` as the primary inspection and authoring environment whenever editor evidence is needed.
- Use the available FModel install at `C:\Program Files\fmodel` and UEViewer/umodel install at `C:\Program Files\umodel` when cooked-asset, pak, export, string, or reference inspection would speed up the evidence trail.
- Use the available Blender 5.1 install at `C:\Program Files\Blender Foundation\Blender 5.1`, with the Unreal PSK/PSA addon installed, for mesh/animation import-export or visual inspection when appropriate.
- Use the available UAssetAPI/MW5AssetTool at `D:\Downloads\OneDrive\Documents\code\tku-update\tools\MW5AssetTool` and UAssetGUI at `C:\Program Files\UassetGUI` for structured UAsset inspection/comparison where appropriate.
- UE4SS v3.0.1 dev build from `zDEV-UE4SS_v3.0.1.zip` is extracted in `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Binaries\Win64`; use it where runtime instrumentation, Lua/mod hooks, or runtime evidence would help.
- If third-party inspection or runtime tools are used, treat their output as supporting evidence unless the workflow has been separately validated. The decisive fixes should still be made by recreating or reparenting assets in the editor where possible.
- Additional Unreal asset dump/reference tools still require approval before installation.

## Assets Requiring Editor-Level Inspection First

- `/Game/Levels/FrontEnd/StarMap`
- `/Game/UI/FrontEnd/Starmap/StarMapActor`
- `/Game/UI/FrontEnd/StarMapPawn`
- `/Game/UI/FrontEnd/Starmap/StarSystemBody`
- `/Game/Campaign/CampaignArcs/BorderChanges/_common/BaseStarMapBorderActor`
- `/Game/Campaign/CampaignArcs/BorderChanges/AllStarMapBorderChanges`
- `/Game/Campaign/CampaignArcs/BorderChanges/3015_GameStart/Borders3015`
- `/Game/InnerSphereData/MW5_InnerSphereData`
- `/Game/InnerSphereData/Updated/EmployerInfoData`
- `/Game/InnerSphereData/Updated/SystemFactionChanges`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/Faction_MTL`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionBorder_MTL`
- `/Game/UI/FrontEnd/Starmap/Materials/Factions/FactionColours_MTF`
- `/Game/Campaign/Clusters/*`, especially `MWClusterDataAsset` examples for Lyran, Steiner-Kurita, Taurian, Outworlds, industrial hubs, and non-major overlays.
- `/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets`
- `/Plugins/TheKnownUniverse/Content/Regions/War/CareerModeCustomClusters`
- Root `/Game/Employers/*` and `/Game/Factions/*` assets from TKU, especially anything identifying Steiner/Lyran Commonwealth.
- TKU plugin dated border assets under `/Plugins/TheKnownUniverse/Content`, including `StarMapBorderActor*`, `StarMapBordersUpdate_Action_*`, year assets, and faction-related data assets.

## Exact Next Inspection Steps

1. Create or identify a clean editor-side TKU compatibility mod workspace. Keep original backups outside the active editing path.
2. Use the guide's `Save To Mod` substitution workflow for current vanilla assets that need changes. Do not start by importing cooked TKU replacements over current assets.
3. Place genuinely new TKU assets, custom data tables, and helper assets in plugin `Content`, matching the guide's new-asset workflow.
4. Inspect current `/Game/Campaign/Clusters` assets and the `MWClusterDataAsset` class first. Record required properties, primary-asset registration, package naming, faction asset references, overlay meshes, constellation meshes, and system ID sets.
5. Inspect `/Game/UI/Editor/Utils/EUW_MigratePlaceClusterTOIsToClusterAssets`. Determine whether it can be run safely on copied/editor-authored data, or whether its graph should be used only as a recipe for our own migration script.
6. Inspect `StarMap.umap`. Record world settings, level Blueprint references, placed actor classes, missing-class warnings, camera/pan bounds, starmap UI references, placed `StarSystemBody_C` generation assumptions, and hard references to TKU starmap classes.
7. Inspect `StarMapActor`. Record parent class, construction script dependencies, BeginPlay logic, territory overlay generation paths, border actor arrays/maps, faction material references, cluster-asset lookup paths, and references to `BaseStarMapBorderActor_C` or `StarSystemBody`.
8. Inspect `StarMapPawn` and `StarSystemBody`. Record map movement bounds, input routing, selected-system display bindings, ownership display logic, cluster overlay mesh logic, and references to root faction/employer assets.
9. Inspect `BaseStarMapBorderActor` and dated plugin border actors. Confirm whether they can be reparented to current vanilla classes or whether their logic must be recreated using current vanilla border formats.
10. Compare TKU and current vanilla data schemas for `MW5_InnerSphereData`, `EmployerInfoData`, `SystemFactionChanges`, and `MWClusterDataAsset`. Record changed columns, row keys, asset reference fields, and faction/employer identifier differences.
11. Specifically trace why old root faction/employer assets break Steiner/Lyran ownership. Check display name, internal ID, enum/string owner key, employer asset path, faction asset path, and any redirects.
12. Save findings into `reports\tku_editor_first\reference_trace_manifest.md` plus a machine-readable `reference_trace_manifest.json`.
13. Only then choose a rebuild path based on the decision tree below.

## Decision Tree For The Next Phase

- If `StarMap.umap` has hard references to unsafe TKU `StarMapActor`, `StarMapPawn`, `StarSystemBody`, `BaseStarMapBorderActor`, or dated border actor classes, do not restore the cooked map directly. Recreate a modern-compatible map or level override in the editor.
- If expanded map bounds are controlled by simple properties on vanilla-compatible `StarMapActor` or `StarMapPawn`, create an editor-authored substitution based on the current vanilla asset with only the bounds changed.
- If expanded map bounds are controlled by `StarMap.umap` placed actors or level Blueprint logic, recreate those pieces in an editor-authored modern map instead of repacking the old cooked map.
- If clan homeworlds exist only in TKU `MW5_InnerSphereData` and the current schema differs, port rows into a current-schema data asset. Do not restore the old table as a whole.
- If TKU cluster/overlay data exists only as deprecated `InnerSphereMapData` fields or old `PlaceCluster`/campaign-arc assets, recreate it as current `MWClusterDataAsset` assets before testing old border actors.
- If a data-table change is needed, prefer the guide-backed custom table pattern: create a new plugin-content table and point a modern override asset at it, instead of replacing shared vanilla source tables blindly.
- If non-major overlays require dated TKU border actors that can be reparented cleanly to the current vanilla border base class, rebuild those assets in the editor and package them as a minimal compatibility patch.
- If dated TKU border actors cannot be reparented because graph logic or parent APIs changed, recreate border definitions using the current vanilla border actor/data format.
- If old root faction/employer assets break Steiner/Lyran because of schema or identifier drift, never restore them as a group. Port only the new factions required by TKU into current-schema assets.
- If editor inspection cannot recover enough graph detail, use approved asset inspection tools for reference extraction. If references remain opaque, abandon cooked pak surgery for the starmap stack and rebuild the needed functionality manually in the editor.
- If a future rebuild is justified, require a pre-build evidence package with exact assets changed, dependency graph evidence, expected visible behavior, rollback path, and a test checklist.

## Risks And Rollback Points

- Build 59 is not a stable baseline. It should be treated as failed because it hung on load after adding TKU `StarMap.umap`.
- Build 58 is the best known stable TKU-only baseline, but it is feature-incomplete.
- Restored original TKU pak `MW5Mercs\Mods\TheKnownUniverse\Paks\TheKnownUniverse.pak` must not be edited in place.
- Active loose required override `MW5Mercs\Content\Paks\MW5Mercs-zKnownUniverseStarmap.pak` may be renamed only for reversible isolation and must be restored afterward.
- Quarantined blind-build artifacts under `codex_quarantine\tku_failed_compat_20260510` must not be used as clean source evidence.
- Disabled historical content paks in `MW5Mercs\Content\Paks` should remain untouched unless a deliberate rollback plan says otherwise.
- Future temporary outputs should be contained under `reports\tku_editor_first\`, `tools\tku_reference_audit\`, or a clearly named staging directory.
- Future build scripts should write a manifest and rationale for each build number. Do not silently mutate constants and overwrite the same live pak without preserving the reasoning.

## What Not To Do Next

- Do not run another blind rebuild because a symptom suggests a likely asset.
- Do not restore TKU `StarMap.umap`, `StarMapActor`, `StarMapPawn`, `StarSystemBody`, or `BaseStarMapBorderActor` without reference graph evidence.
- Do not restore root faction/employer assets as a broad group.
- Do not use the guide's basic PAK-container approach as evidence that the contents are compatible. It only makes an old PAK load through the mod manager.
- Do not call plugin-only behavior "full TKU compatibility"; it is a stable baseline, not the target feature set.
- Do not rely on title-screen boot as validation.
- Do not install or download third-party tooling without approval.
- Do not use broad vanilla overrides and treat the result as a compatibility fix if the TKU starmap features are bypassed.

## Recommended First Concrete Action

Move directly to editor/tool inspection of `TheKnownUniverse.pak`, focused on TKU root starmap classes, border actors, root data assets, and game-start plugin/campaign assets. Do not perform another runtime toggle or rebuild until the inspection explains which asset group can crash immediately after a Davion career load.
