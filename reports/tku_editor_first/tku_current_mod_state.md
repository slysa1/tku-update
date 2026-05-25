# TKU Current Mod State

Curated on 2026-05-18 from repo evidence recorded on 2026-05-12, with 2026-05-25 addenda appended for the active DLC7 repair pass. This preserves mod, package, mirror, profile, hash, and rollback information outside the main roadmap so `TKU_COMPAT_PATCH_ROADMAP.md` can stay compact.

This file is a ledger. Use the latest dated section, not the older 2026-05-12 summary, when choosing the current live test state.

## Runtime Target

- Compatibility target: `MW5 v1.13.378`.
- Stable documented floor: `TKUEvidenceCorePluginOnly`.
- Last repo-recorded isolated test profile: `TKUEvidenceCorePluginOnly` plus `TKUCompatEditorPatch`.
- Original loose required override: `MW5Mercs\Content\Paks\MW5Mercs-zKnownUniverseStarmap.pak`, SHA256 `DFAC2CA2E1DEDCD96709A95A778DA1BB55EB02BB87E9E62B7DFC8320DD9F1FCB`.
- Active compat content mirror in the latest verification: `MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak`, SHA256 `158B2C6A203646E6595C761F8B8D310B4792A6C9E6C1A9330D34B81E71D2B405`.
- Live deployed `TKUCompatEditorPatch.pak` in the last verification: SHA256 `FB5F798061ADFF1DC78A4CD350541E530692C3C681061D639C24107895CB746C`.

## Editor Patch

- Editor plugin: `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins\TKUCompatEditorPatch\TKUCompatEditorPatch.uplugin`.
- Editor packaged mod: `E:\Games\MechWarrior5Editor\MW5Mercs\Mods\TKUCompatEditorPatch`.
- Live deployed mod: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch`.
- Last deployed load order: `95`.
- Last deployed package-side `gameVersion`: `1.13.378`.
- Source plugin metadata note: `Plugins\TKUCompatEditorPatch\mod.json` was stale in the 2026-05-12 verification; packaged/live metadata was treated as runtime authority.

## Mod-Owned Assets

The editor project contained these current-compatible `ModOverride` assets in the last verification:

- `ModOverride\InnerSphereData\MW5_InnerSphereData.uasset`.
- `ModOverride\InnerSphereData\StarSystemGenerator.uasset`.
- `ModOverride\Levels\FrontEnd\StarMap.umap`.
- `ModOverride\UI\FrontEnd\StarMapPawn.uasset`.

Known editor-side evidence:

- `MW5_InnerSphereData` override resolves to `/ModOverride/TKUCompatEditorPatch/InnerSphereData/MW5_InnerSphereData` with `3,974` rows.
- `StarSystemGenerator.generate_inner_sphere_data` returns `3,974` systems in the initializer probe.
- `StarMap` override resolves to `/ModOverride/TKUCompatEditorPatch/Levels/FrontEnd/StarMap` with `3,973` `StarSystemBody_C` actors, ID range `1..7921`.
- The placed `StarMapActor` remains the current `/Game/UI/FrontEnd/Starmap/StarMapActor.StarMapActor_C`.
- The editor-authored `StarMapPawn` override is runtime-positive: starmap opens and pans farther than vanilla.

## Latest Deploy

Report: [tkucompat_live_test_deploy_20260512-092253.md](tkucompat_live_test_deploy_20260512-092253.md).

- Apply requested: `True`.
- Source package: `E:\Games\MechWarrior5Editor\MW5Mercs\Mods\TKUCompatEditorPatch`.
- Destination mod: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch`.
- Baseline mod: `TKUEvidenceCorePluginOnly`.
- Live modlist backup: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260512-092253.json`.
- Repo modlist backup: `reports\tku_editor_first\modlist.backup-before-TKUCompatEditorPatch-20260512-092253.json`.
- Destination mod backup: `reports\tku_editor_first\backups\live_mod_before_deploy_TKUCompatEditorPatch_20260512-092253`.
- Test profile: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.profile-TKUCompatEditorPatch-corepatch-20260512-092253.json`.
- Deployed `mod.json` hash: `D44214389A1C8AF11A369793308F88DC9CD5FA3601C245206FF82695A8E52A11`.
- Deployed pak hash: `FB5F798061ADFF1DC78A4CD350541E530692C3C681061D639C24107895CB746C`.
- Live modlist hash after deploy: `9A1B441FD6AE98BF5652F4FEC8253BF59A57635F62A030EEB8A014DCD7E039A4`.

## Latest Content Mirror

Report: [tku_content_mirror_20260512-092307.md](tku_content_mirror_20260512-092307.md).

Purpose: late-load a `Content\Paks` mirror of the editor-authored compat package so root `/Game` assets can win over the legacy loose TKU starmap pak during a controlled runtime test.

- Apply requested: `True`.
- Source pak: `E:\Games\MechWarrior5Editor\MW5Mercs\Mods\TKUCompatEditorPatch\Paks\TKUCompatEditorPatch.pak`.
- Staged mirror pak: `reports\tku_editor_first\staging\MW5Mercs-zzzzTKUCompatEditorPatch-20260512-092307.pak`.
- Live mirror pak: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak`.
- Mirror pak SHA256: `AC3FBAFEE4E4B7F36A65C5EBAC6D8FB3B5DD0D02300674CED702F18983082E13`.
- Files mirrored: `8`.
- Backup of prior live mirror: `reports\tku_editor_first\backups\content_mirror_20260512-092307\MW5Mercs-zzzzTKUCompatEditorPatch.pak`.

Root package providers for the target assets in the continuation gate:

| Provider | Mount | Relevant entries |
| --- | --- | --- |
| Base game pak | `../../../` | `MW5_InnerSphereData`, `StarSystemGenerator`, `StarMap`, `StarMapPawn` |
| Original loose TKU override | `../../../MW5Mercs/Content/` | `MW5_InnerSphereData`, `StarMap` |
| Active TKU compat content mirror | `../../../MW5Mercs/Content/` | `MW5_InnerSphereData`, `StarSystemGenerator`, `StarMap`, `StarMapPawn` |
| Deployed mod pak | mod package | `MW5_InnerSphereData`, `StarSystemGenerator`, `StarMap`, `StarMapPawn`, asset registry |

## Runtime Result Ledger

- `TKUEvidenceCorePluginOnly` loaded career and opened the starmap, but remained vanilla-width with incomplete/vanilla overlays.
- Editor-authored `TKUCompatEditorPatch` before the latest mirror was runtime-safe in the isolated baseline stack.
- After the editor-authored pawn repair, the starmap opened and panned farther than vanilla.
- A new-career test after the pawn repair still showed missing periphery/clan-area stars and vanilla faction overlays.
- The latest 8-file content mirror containing `StarSystemGenerator` had no recorded runtime result in the repo evidence as of the 2026-05-12 continuation gate.
- 2026-05-25 post-career-source test: career and starmap loaded, panning remained extended, Taurian/Magistracy space may have had more stars, but clan stars were still missing and faction overlay remained vanilla.
- Package inspection after that test proved the clan cluster assets were not cooked into the package, so that result did not validate the new cluster data.
- The current live package now contains the TKU clan cluster/faction assets; the next runtime test is the first valid cluster-asset runtime check.

## Rollback Notes

Do not touch original TKU paks.

- Restore prior live modlist from `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260512-092253.json`.
- Restore prior deployed mod folder from `reports\tku_editor_first\backups\live_mod_before_deploy_TKUCompatEditorPatch_20260512-092253`.
- Restore prior content mirror from `reports\tku_editor_first\backups\content_mirror_20260512-092307\MW5Mercs-zzzzTKUCompatEditorPatch.pak`.
- To abandon content-mirror testing, remove only `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak`.
- Leave `MW5Mercs-zKnownUniverseStarmap.pak` untouched unless a separately documented reversible isolation test renames and restores it.

## Evidence Sources

- [codex_re_continuation_gate_20260512.md](codex_re_continuation_gate_20260512.md).
- [codex_re_state_verification_20260512.md](codex_re_state_verification_20260512.md).
- [tkucompat_live_test_deploy_20260512-092253.md](tkucompat_live_test_deploy_20260512-092253.md).
- [tku_content_mirror_20260512-092307.md](tku_content_mirror_20260512-092307.md).
- [tku_packaged_mod_inspection_20260511.md](tku_packaged_mod_inspection_20260511.md).
- [ue4_starmap_binding_probe_20260512.md](ue4_starmap_binding_probe_20260512.md).
- [ue4_starmap_model_probe_20260512.md](ue4_starmap_model_probe_20260512.md).
- [ue4_initializer_defaults_probe_20260512.md](ue4_initializer_defaults_probe_20260512.md).

## 2026-05-25 Live Update

This section supersedes the 2026-05-12 "latest deploy" values for the current isolated test state.

### Runtime Target

- Compatibility target remains `MW5 v1.13.378`.
- Active live profile: `TKUEvidenceCorePluginOnly` plus `TKUCompatEditorPatch`.
- Active live modlist: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.json`.
- Isolated profile report: `reports\tku_editor_first\tkucompat_live_test_deploy_20260525-122425.md`.
- Live modlist backup: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\modlist.backup-before-TKUCompatEditorPatch-20260525-122425.json`.
- Prior deployed mod backup: `reports\tku_editor_first\backups\live_mod_before_deploy_TKUCompatEditorPatch_20260525-122425`.

### Applied Editor Patch

- Patch report: `reports\tku_editor_first\ue4_career_model_sources_patch.md`.
- Added mod-owned `/Game/Campaign/_common/DefaultSystemGenerator` override.
- Added mod-owned `/Game/DLC1/CareerMode/StartConditions/CareerMode` override.
- Updated mod-owned `MW5GameMode`, `CampaignMode`, and DLC1 `CareerMode` defaults:
  - `DefaultInnerSphereClass`: `/ModOverride/TKUCompatEditorPatch/InnerSphereData/StarSystemGenerator.StarSystemGenerator_C`.
  - `CampaignSystemGeneratorClass`: `/ModOverride/TKUCompatEditorPatch/Campaign/_common/DefaultSystemGenerator.DefaultSystemGenerator_C`.
- Added current-schema TKU clan cluster/faction assets:
  - Patch report: `reports\tku_editor_first\ue4_tku_clan_cluster_assets_patch.md`.
  - Manifest sync report: `reports\tku_editor_first\tku_cluster_manifest_20260525-043107.md`.
  - The source manifest now includes 10 `/Game/Campaign/Clusters/TKU_*` assets so the MW5 Mod Editor cook includes them.
  - Overlay meshes are current-schema placeholders for this diagnostic pass; final-authentic TKU clan overlay art is still a separate restoration task.

### Packaged And Deployed Assets

- Valid source package was the newest nested editor output:
  - `E:\Games\MechWarrior5Editor\MW5Mercs\Mods\TKUCompatEditorPatch\TKUCompatEditorPatch\TKUCompatEditorPatch`.
- Deployed live mod:
  - `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods\TKUCompatEditorPatch`.
- Deployed pak SHA256: `7B9EA432C7624E4AE045F90D5E4C81F91A744F94F285A75B57232BA12C0A6C4E`.
- Live `mod.json` build number: `6`.
- Live `mod.json` load order: `95`.
- Live `mod.json` game version: `1.13.378`.
- Live package inspection report: `reports\tku_editor_first\tku_packaged_mod_inspection_20260511.md`.
- Live package inspection safety failures: none.
- `UnrealPak -List` confirmed all expected fragments, including:
  - `Content/Campaign/_common/DefaultSystemGenerator.uasset/.uexp`.
  - `Content/DLC1/CareerMode/StartConditions/CareerMode.uasset/.uexp`.
  - `Content/InnerSphereData/MW5_InnerSphereData.uasset/.uexp`.
  - `Content/InnerSphereData/StarSystemGenerator.uasset/.uexp`.
  - `Content/Modes/CampaignMode.uasset/.uexp`.
  - `Content/Modes/MW5GameMode.uasset/.uexp`.
  - `Content/UI/FrontEnd/StarMapPawn.uasset/.uexp`.
  - `Content/Levels/FrontEnd/StarMap.umap/.uexp`.
  - `Content/Campaign/Clusters/TKU_ClanConflict/*.uasset/.uexp`.
  - `Content/Campaign/Clusters/TKU_RepairSystem_Clan/*.uasset/.uexp`.

### Current Test

- MW5 was launched against the cluster-cooked package.
- Runtime result: career mode loaded, the starmap opened, extended panning remained active, and existing stars appear to carry TKU ownership data such as Oberon Confederation.
- Runtime result still failing: visible base starmap and faction overlay look vanilla; TKU/clan stars are missing.
- Latest save scan: `reports\tku_editor_first\mw5_save_starmap_scan_20260525-131101.md`.
- Save evidence: latest test save still used `MWStartConditionsAsset:CareerMode_Davion_Start`; scanned `MWStarMapModel` data did not include the TKU/clan sample IDs.

### Active Career Source Surface

- Patch report: `reports\tku_editor_first\ue4_active_career_sources_patch.md`.
- Added 17 current-schema active career source assets to the editor plugin `ModOverride` folder:
  - 12 direct DLC1 career start-condition assets.
  - `CareerMode_Start`, `FRR_CareerMode_Start`, `CareerModeCoreCampaign`, `CareerModeClusters`, and `CareerMode_SafeZones`.
- Manifest sync report: `reports\tku_editor_first\tku_cluster_manifest_20260525-132824.md`.
- Editor source manifest now has 35 entries, including 17 active career source entries and the existing 10 TKU cluster entries.
- Source-file check found 0 missing files for the source manifest.
- Verification probe: `reports\tku_editor_first\ue4_campaign_model_sources_probe.md`.
- Probe evidence: `/Game/DLC1/CareerMode/StartConditions/CareerMode_Davion_Start`, `CareerMode_Start`, `CareerModeCoreCampaign`, `CareerModeClusters`, and `CareerMode_SafeZones` now resolve through `/ModOverride/TKUCompatEditorPatch`.
- Known limitation: the active source copies still contain vanilla border and warzone action content. They are now packageable and editable, but the runtime star-generation root cause is not yet proven fixed.

### Next Package Test

- Package `TKUCompatEditorPatch` again in the MW5 Mod Editor.
- Use the newest nested package output from `E:\Games\MechWarrior5Editor\MW5Mercs\Mods\TKUCompatEditorPatch\TKUCompatEditorPatch\TKUCompatEditorPatch`.
- Deploy it to the live isolated profile.
- Run a fresh career starmap test, preferably from a fresh slot.
- If clan stars are still absent, the strongest remaining hypothesis is that runtime `MWStarMapModel` generation is bypassing the patched generator/table path; overlay restoration then remains a separate campaign border/warzone action patch task.

### Active Cluster Diagnostic

- Cross-agent review recommended a narrow active-cluster diagnostic before broad DLC7/career-arc mutation.
- Applied diagnostic patch report: `reports\tku_editor_first\ue4_active_cluster_diagnostic_patch.md`.
- Manifest report: `reports\tku_editor_first\tku_cluster_manifest_20260525-162032.md`.
- Diagnostic target: `/Game/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset.uasset`.
- Diagnostic IDs appended to the mod-owned override: `4088`, `4089`, `4090`.
- Editor source manifest now has 36 entries and includes the diagnostic active cluster asset.
- Package inspection confirmed `Content/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset.uasset/.uexp` in build 8.
- Live deployment report: `reports\tku_editor_first\tkucompat_live_test_deploy_20260525-163735.md`.
- Runtime result: career and starmap loaded, but the user reported the map looked the same as the previous run.
- Save scan report: `reports\tku_editor_first\mw5_save_starmap_scan_20260525-164145.md`.
- Save scan result: IDs `4088`, `4089`, and `4090` still do not appear in the latest `StarMapModel` segment.
- Correction: follow-up scan `reports\tku_editor_first\mw5_save_starmap_scan_20260525-164254.md` also found zero `StarMapModel` occurrences for the original Rasalhague cluster member IDs, so this save scanner does not serialize full cluster membership. The visual result is still negative, but the ID scan is not a definitive cluster-data proof.
- Current next target: map the active career arc/action graph and determine whether placement actions, `ClusterDataAssetId`, or campaign event triggers need patching rather than only `MWClusterDataAsset.system_ids`.

### Active Action Probe And Current Content Mirror

- Cross-agent follow-up fixes were applied to `tools\tku_reference_audit\ue4_probe_active_campaign_actions.py` and `tools\Invoke-TKUActiveCampaignActionsProbe.ps1`.
- Active action probe report: `reports\tku_editor_first\ue4_active_campaign_actions_probe.md`.
- Probe result: `800` assets inspected, `252` ArcAction Blueprints found, `47` PlaceCluster-like actions, `212` cluster references, and only `1` mod-owned active cluster reference.
- Confirmed mod-owned active reference: `/Game/DLC1/CareerMode/Warzones/Rasalhauge_Clusters/PlaceRasalhague_ArcAction_7_10` points to the mod-owned `Rasalhague_7_10_ClusterAsset`.
- Confirmed limitation: packaged TKU clan clusters are not yet wired into active placement roots, so faction overlay restoration remains unresolved.
- Content mirror builder was patched to select the newest available `TKUCompatEditorPatch.pak`; the old behavior could choose the stale 2026-05-12 editor pak.
- Content isolation script now supports targeted `-Target CompatMirror` or `-Target LegacyStarmap` operations.
- Current active compat mirror: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak`.
- Current active compat mirror SHA256: `4414AC6DA60FD9D04E5BCB9098E0D716A689912AF4C484288AD54680537860DC`.
- Current mirror report: `reports\tku_editor_first\tku_content_mirror_20260525-171114.md`.
- Current mirror isolation status: `reports\tku_editor_first\tku_content_pak_isolation_20260525-171148.md`.
- Legacy `MW5Mercs-zKnownUniverseStarmap.pak` remains disabled.
- Next HITL test: close the MW5 Mod Editor, launch MW5, create a new/fresh career, open the starmap, check for clan stars and faction overlay changes, save, then scan the latest save.

### Fresh Content Mirror Runtime Result

- Runtime result with the active content mirror: no visible change from the previous run.
- User-visible failure remains: clan/TKU stars absent and faction overlay still vanilla.
- Save scan report: `reports\tku_editor_first\mw5_save_starmap_scan_20260525-190333.md`.
- Latest scanned campaign: `House Davion`, start condition `MWStartConditionsAsset:CareerMode_Davion_Start`, DLC tags `DLC1` through `DLC7`.
- Latest save: `37C711E141C90274851105B37CBC3707.sav`, timestamp `2026-05-25T19:00:06`.
- `StarMapModel` sample-id occurrences remain zero for `4088`, `4089`, `4090`, `4110`, and `7921`.
- Direct binary string scan found no `Strana Mechty`, `Strana`, `Babylon`, `Huntress`, `Clan`, `Oberon`, or `TKU_ClanConflict` strings in the latest saves.
- The same saves still contain `TaurianConcordat`, `MagistracyOfCanopus`, and `Rasalhague_7_10_ClusterAsset`.
- Live mirror package evidence remains valid: `UnrealPak -List` shows mount `../../../MW5Mercs/Content/` and all eight expected root starmap/data files.
- Current conclusion: fresh content-root mirror deployment is not sufficient. Continue on active campaign/starmap initialization and placement-action wiring.

### All-Game Content Mirror

- Reason for change: the previous active content mirror contained only the 8 starmap-core files, while the current editor-authored `TKUCompatEditorPatch.pak` also contains game mode, career source, campaign arc, and TKU cluster assets under root `/Game` paths.
- Tool patch: `tools\tku_reference_audit\build_tku_content_mirror.py` now supports `--scope starmap-core` and `--scope all-game`.
- Dry-run report: `reports\tku_editor_first\tku_content_mirror_20260525-193027.md`.
- Applied report: `reports\tku_editor_first\tku_content_mirror_20260525-193109.md`.
- Applied scope: `all-game`.
- Live mirror pak: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak`.
- Live mirror SHA256: `158B2C6A203646E6595C761F8B8D310B4792A6C9E6C1A9330D34B81E71D2B405`.
- Live mirror entries: `72`, all under `/Game`.
- Confirmed live entries include:
  - `/Game/Modes/CampaignMode.uasset`.
  - `/Game/Modes/MW5GameMode.uasset`.
  - `/Game/DLC1/CareerMode/CareerModeCoreCampaign.uasset`.
  - `/Game/Campaign/Clusters/TKU_ClanConflict/TKU_ClanConflict_NoOverlay_ClusterAsset.uasset`.
  - `/Game/Levels/FrontEnd/StarMap.umap`.
- Rollback: replace the live mirror with `reports\tku_editor_first\backups\content_mirror_20260525-193109\MW5Mercs-zzzzTKUCompatEditorPatch.pak`.
- Next HITL test: launch MW5 from a closed state, start a fresh career, open the starmap, check TKU/clan stars, faction overlay, map centering, and extended panning, then save once for the next scan.
