# Codex RE State Verification - 2026-05-12

Generated from workspace state on 2026-05-12 Australia/Brisbane. This report is read-only evidence consolidation. No game files, editor assets, paks, modlists, or original TKU artifacts were modified by this verification.

## Repository State

- Workspace: `D:\Downloads\OneDrive\Documents\code\tku-update`
- Branch: `main...origin/main`
- Worktree: dirty before this report was written.
- Pre-existing modified tracked files:
  - `reports/tku_editor_first/known_universe_recovery_report_20260511.md`
  - `reports/tku_editor_first/tku_packaged_mod_inspection_20260511.json`
  - `reports/tku_editor_first/tku_packaged_mod_inspection_20260511.md`
  - `reports/tku_editor_first/tku_packaged_mod_inspection_20260511_TKUCompatEditorPatch_unrealpak_list.txt`
  - `tools/mw5_pak.py`
  - `tools/tku_reference_audit/inspect_tku_packaged_mod.py`
- Pre-existing untracked artifacts include 2026-05-12 reports, backups, staging files, runtime probe helpers, deployment helpers, content mirror helpers, and UE4 commandlet probe outputs under `reports/tku_editor_first/` and `tools/`.

## Config And Paths

`config/tku_paths.local.json` is readable. Every configured path tested exists:

- Game root: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries`
- Local mods root: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Mods`
- Content paks root: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks`
- Steam Workshop root: `E:\SteamLibrary\steamapps\workshop\content\784080`
- MW5 editor root: `E:\Games\MechWarrior5Editor`
- UModel root: `C:\Program Files\umodel`
- FModel root: `C:\Program Files\fmodel`
- Blender root: `C:\Program Files\Blender Foundation\Blender 5.1`
- UAssetAPI/MW5AssetTool root: `D:\Downloads\OneDrive\Documents\code\tku-update\tools\MW5AssetTool`
- UAssetGUI root: `C:\Program Files\UassetGUI`
- UE4SS Win64 root: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Binaries\Win64`
- Configured game version: `1.13.378`

## Active Runtime State

Live `MW5Mercs\Mods\modlist.json` is not the old core-only floor. It currently enables:

- `TKUEvidenceCorePluginOnly`
- `TKUCompatEditorPatch`

No `MW5Mercs-Win64-Shipping`, `MW5Mercs`, `UE4Editor`, or `UE4Editor-Cmd` process was found by the process query. Runtime state should therefore be treated as closed/pending, not mid-test.

Active relevant `Content\Paks` entries:

- `MW5Mercs-WindowsNoEditor.pak`
- `MW5Mercs-zKnownUniverseStarmap.pak`
- `MW5Mercs-zzzzTKUCompatEditorPatch.pak`
- `REQUIRED Override PAK-786-1-0-1713972397.7z`

Relevant hashes:

- Original loose TKU override: `DFAC2CA2E1DEDCD96709A95A778DA1BB55EB02BB87E9E62B7DFC8320DD9F1FCB`
- Active content mirror: `AC3FBAFEE4E4B7F36A65C5EBAC6D8FB3B5DD0D02300674CED702F18983082E13`
- Live deployed `TKUCompatEditorPatch.pak`: `FB5F798061ADFF1DC78A4CD350541E530692C3C681061D639C24107895CB746C`

## Editor And Patch State

The editor project now contains a dedicated compatibility plugin:

- `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins\TKUCompatEditorPatch\TKUCompatEditorPatch.uplugin`

Current mod-owned `ModOverride` assets:

- `ModOverride\InnerSphereData\MW5_InnerSphereData.uasset`
- `ModOverride\InnerSphereData\StarSystemGenerator.uasset`
- `ModOverride\Levels\FrontEnd\StarMap.umap`
- `ModOverride\UI\FrontEnd\StarMapPawn.uasset`

The packaged editor mod under `E:\Games\MechWarrior5Editor\MW5Mercs\Mods\TKUCompatEditorPatch` has corrected package-side `gameVersion: 1.13.378`, but the source plugin `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins\TKUCompatEditorPatch\mod.json` still shows stale editor/source metadata (`gameVersion: 1.13.64`, old description). Treat packaged/live mod metadata as the runtime authority unless the source plugin metadata is intentionally normalized later.

## State Conclusion

The stable documented floor remains `TKUEvidenceCorePluginOnly`, but the active live state is a later isolated test: `TKUEvidenceCorePluginOnly` plus packaged/deployed `TKUCompatEditorPatch`, with an 8-file late-loading content mirror in `Content\Paks`.

No additional build is authorized by this state verification. The next safe action is runtime validation of the already-deployed 8-file content mirror, then log/crash inspection. If that test was already run manually, the missing evidence is the dated runtime result.

## Rollback Notes

Latest mirror rollback from `tku_content_mirror_20260512-092307`:

- Replace `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries\MW5Mercs\Content\Paks\MW5Mercs-zzzzTKUCompatEditorPatch.pak` with `reports\tku_editor_first\backups\content_mirror_20260512-092307\MW5Mercs-zzzzTKUCompatEditorPatch.pak`.

To abandon content-mirror testing entirely, remove only `MW5Mercs-zzzzTKUCompatEditorPatch.pak`; do not touch `MW5Mercs-zKnownUniverseStarmap.pak`.

