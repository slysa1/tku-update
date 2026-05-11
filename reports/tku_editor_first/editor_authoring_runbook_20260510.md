# TKU Editor Authoring Runbook - 2026-05-10

- Status: planning only
- Build authorized: `false`
- Runtime pak authorized: `false`
- Required editor: `E:\Games\MechWarrior5Editor`
- Reason for runbook: commandlet Python has not proven safe for MW5 `Create Mod` / `Save To Mod`; the first asset-writing step must use the MW5 Mod Editor UI.

## Preflight

1. Confirm `MW5Mercs\Mods\modlist.json` enables only `TKUEvidenceCorePluginOnly`.
2. Confirm MW5 and UE4Editor are closed.
3. Do not edit original `TheKnownUniverse.pak`, `MW5Mercs-zKnownUniverseStarmap.pak`, or any quarantined failed build.
4. Keep all editor-authored work inside a new dedicated mod target, suggested name `TKUCompatEditorPatch`.
5. Before packaging, record the exact asset list in a manifest report.

## Evidence Inputs

- Current stable runtime floor: `TKUEvidenceCorePluginOnly`
- MW5 Mod Editor Guide: `MW5Mercs\Mods\MW5Mercs_Mod_Editor_Guide_(v2.3).pdf`
- Data candidate report: `reports\tku_editor_first\tku_inner_sphere_import_candidates_20260510.md`
- Preferred DataTable candidate: `reports\tku_editor_first\tku_inner_sphere_merged_current_plus_tku_additions_20260510.csv`
- Raw clean-source TKU DataTable reference: `reports\tku_editor_first\tku_inner_sphere_raw_original_current_schema_20260510.csv`
- Placement formula: `LevelX = 51336 + 8 * PosY`, `LevelY = 51039 + 8 * PosX`
- Current classes to preserve:
  - `/Game/UI/FrontEnd/Starmap/StarMapActor`
  - `/Game/UI/FrontEnd/Starmap/StarSystemBody`
  - `/Game/UI/FrontEnd/StarMapPawn`
  - `/Game/Campaign/Clusters/*_ClusterAsset`

## Guide Evidence

The local MW5 Mod Editor Guide supports the manual gate:

- Page 4 says creating a mod through the toolbar builds the required folder structure and is the first step in a mod project.
- Page 7 says `Save To Mod` duplicates an existing game asset into the active mod's `ModOverride` content and makes the editor use that modded copy instead of the source asset.
- Page 11 says packaging is performed through `Manage Mod` / `Package Mod`, with output defaulting to the editor `MW5Mercs\Mods` folder.
- Page 13 says `ModOverride` assets must preserve the same folder structure as the original asset.
- Page 15 says custom DataTable work can use a copied DataTable in mod content, then point affected assets to that custom table when needed.

This matches the current evidence gate: do not manually write guessed plugin folders, and do not edit source assets directly.

## Manual Editor Steps

1. Launch `E:\Games\MechWarrior5Editor\Engine\Binaries\Win64\UE4Editor.exe`.
2. Open `E:\Games\MechWarrior5Editor\MW5Mercs\MW5Mercs.uproject`.
3. Let asset discovery finish.
4. Create a new MW5 mod through the MW5 Mod Editor UI named `TKUCompatEditorPatch`.
5. Save the mod and verify a new editor mod target appears under the editor project.
6. Use `Save To Mod` only for copied/current-compatible assets, not original TKU cooked assets.

## First Asset Candidate

Create a mod-owned copy/override of `/Game/InnerSphereData/MW5_InnerSphereData` and import the merged current-plus-TKU-additions CSV.

Use the merged candidate first because it preserves current 1.13 rows, current descriptions, current cluster IDs for existing systems, and adds 1,801 TKU-only systems. The raw original TKU table is retained as evidence but is risky because shared rows differ in 2,119 positions and 468 cluster assignments.

Do not run the migration utility on live assets. If the DataTable import succeeds in the mod target, inspect it in the editor and verify row count `3974`, row struct `InnerSphereMapData`, and spot-check IDs `1`, `2`, `3501`, `4001`, `4110`, and `7921`.

## First StarMap Candidate

After the mod-owned DataTable is verified, create a mod-owned StarMap level candidate from current `/Game/Levels/FrontEnd/StarMap`, not from old TKU `StarMap.umap`.

Use current `StarSystemBody_C` for all generated/added bodies. For every row in the chosen DataTable except invalid row `0`, the expected placement is:

- `Location.X = 51336 + 8 * PosY`
- `Location.Y = 51039 + 8 * PosX`
- `Location.Z = 0`
- `star_system_id = Name`

Do not substitute old TKU `StarMapActor`, `StarSystemBody`, `StarMapPawn`, `BaseStarMapBorderActor`, dated border actors, or old `StarMap.umap`.

## Cluster Track

Do not create `MWClusterDataAsset` assets until a mapping policy is written for legacy TKU cluster IDs.

Known policy blockers:

- `RepairSystem` is generic in TKU and splits across 32 current CSV cluster targets.
- `CareerCluster` is generic in TKU and maps to current rows with no active CSV cluster.
- `ClanConflict`, `RepairSystem_Clan`, `RepairSystem_Custom`, and `PirateKingdoms` include TKU rows absent from current runtime CSV.
- 114 old TKU overlay/constellation soft paths are absent from loose editor content, current base-game pak, and original TKU pak.

Use current `/Game/Campaign/Clusters` assets and the editor utility graph as a recipe, not as a blind mutation tool.

## Packaging Gate

Before any package/build:

1. Write an authored-asset manifest listing every mod-owned asset.
2. Verify the mod target exists and contains only copied/current-compatible assets.
3. Verify the DataTable row count and sample rows in-editor.
4. Verify the StarMap level actor count and sample placements in-editor.
5. Decide whether cluster assets are deferred or included.
6. Save a runtime `modlist.json` profile.

Only then may a narrow runtime package be considered.
