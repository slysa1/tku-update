# TKU Current Mod State

Curated on 2026-05-18 from repo evidence recorded on 2026-05-12. This preserves mod, package, mirror, profile, hash, and rollback information outside the main roadmap so `TKU_COMPAT_PATCH_ROADMAP.md` can stay compact.

This file is a ledger, not a fresh live verification. If the game or editor has been touched since the 2026-05-12 reports, verify the live paths before acting.

## Runtime Target

- Compatibility target: `MW5 v1.13.378`.
- Stable documented floor: `TKUEvidenceCorePluginOnly`.
- Last repo-recorded isolated test profile: `TKUEvidenceCorePluginOnly` plus `TKUCompatEditorPatch`.
- Original loose required override: `MW5Mercs\Content\Paks\MW5Mercs-zKnownUniverseStarmap.pak`, SHA256 `DFAC2CA2E1DEDCD96709A95A778DA1BB55EB02BB87E9E62B7DFC8320DD9F1FCB`.
- Active compat content mirror in the last verification: `MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak`, SHA256 `AC3FBAFEE4E4B7F36A65C5EBAC6D8FB3B5DD0D02300674CED702F18983082E13`.
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
