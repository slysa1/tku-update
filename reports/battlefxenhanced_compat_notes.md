# BattleFXEnhanced Compatibility Notes

## Safe Changes Added

- Generated optional BattleFX-enabled profiles:
  - [modlist.profile-single-knownuniverse-battlefx-compat-20260506.json](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Mods/modlist.profile-single-knownuniverse-battlefx-compat-20260506.json>)
  - [modlist.profile-named-local-battlefx-compat-20260506.json](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Mods/modlist.profile-named-local-battlefx-compat-20260506.json>)
  - [modlist.profile-full-stack-tku-battlefx-compat-20260506.json](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Mods/modlist.profile-full-stack-tku-battlefx-compat-20260506.json>)
- Kept the active `modlist.json` on the safer non-BattleFX profile:
  [modlist.profile-full-stack-with-tku-compat-20260506.json](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Mods/modlist.profile-full-stack-with-tku-compat-20260506.json>)
- Added an extension report for the BattleFX patch:
  [battlefx_patch_extension_report.md](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/reports/battlefx_patch_extension_report.md>)

## What The Analysis Found

- `BattleFXPatch` already overrides 45 high-risk BattleFX assets.
- Two leftover BattleFX-only asset paths still do not have exact modern vanilla counterparts in `MW5Mercs-WindowsNoEditor.pak`:
  - `/Game/Objects/Projectiles/Missile/Particles/Missile_Impact_Dirt_PCL`
  - `/Game/Objects/_common/Effects/ExplosionsMegaPack/Particles/Volataile/Explosion_Mech_Alt`
- Because there is no exact current-game source file at those paths, they were **not** force-patched with renamed substitute assets. That would be risky and could create package-name mismatches.

## Smoke Result

- The full-stack profile with `BattleFXEnhanced + BattleFXPatch + TheKnownUniverseCompatPatch` booted for 90 seconds without creating a new crash directory.

This confirms startup compatibility only. It does **not** prove combat-effect stability.

## Recommended Use

If you want to try BattleFX safely, switch to:

- [modlist.profile-full-stack-tku-battlefx-compat-20260506.json](</E:/SteamLibrary/steamapps/common/MechWarrior 5 Mercenaries/MW5Mercs/Mods/modlist.profile-full-stack-tku-battlefx-compat-20260506.json>)

Then validate in-game with real effect triggers:

1. Enter combat.
2. Fire PPC, large laser, gauss, and missiles.
3. Watch for any new crash folder under `%LOCALAPPDATA%\MW5Mercs\Saved\Crashes`.

If you want the safest default, stay on the current non-BattleFX full-stack profile.
