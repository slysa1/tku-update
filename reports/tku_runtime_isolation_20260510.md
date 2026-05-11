# TKU Runtime Isolation Notes - 2026-05-10

## Purpose

Track runtime evidence for the current original-TKU compatibility investigation. This file is intentionally separate from rebuild reports so we do not confuse observed behavior with proposed fixes.

## Active Source Discipline

- Original TKU mod folder under test: `MW5Mercs\Mods\TheKnownUniverse`
- Original TKU pak: `MW5Mercs\Mods\TheKnownUniverse\Paks\TheKnownUniverse.pak`
- Required loose TKU override pak: `MW5Mercs\Content\Paks\MW5Mercs-zKnownUniverseStarmap.pak`
- Failed load-order shim is disabled and preserved as: `MW5Mercs\Mods\TheKnownUniverse\Paks\zzzz_MW5Mercs-zKnownUniverseStarmap.loadorder-test.pak.disabled-20260510`
- No original pak has been edited or overwritten.

## Crash Signature Under TKU

- Repro path: Single Player -> New Career -> Davion -> loading screen completes -> fatal error before actual gameplay.
- Error: `Unhandled Exception: EXCEPTION_ACCESS_VIOLATION reading address 0x000000000000004c`
- Repeated call-stack hash: `0039C4B8A7510FAC9074DFC881C752315D75F42F`
- Representative crash folders:
- `C:\Users\dogpe\AppData\Local\MW5Mercs\Saved\Crashes\UE4CC-Windows-0C87C32F4B3D2BD810D0ED9B9F8FDB25_0000`
- `C:\Users\dogpe\AppData\Local\MW5Mercs\Saved\Crashes\UE4CC-Windows-4D810CEE44C0036A63EC3EB0A4A0F5EA_0000`
- The crash remains identical with `vonBiomes` disabled, so `vonBiomes` is not sufficient to explain this fatal career-load crash.

## Isolation Results

| Test | Active mods | Loose required override pak | Result | Interpretation |
| --- | --- | --- | --- | --- |
| Intended stack without `vonBiomes` | TKU, ModOptions, YAML family, MW5 Compatibility Pack | Present | Same fatal crash after Davion loading screen | `vonBiomes` table override is not the primary/sufficient cause of this crash |
| Override-only baseline | No enabled mods | Present | Davion career loaded successfully; vanilla starmap and mechbay loaded | Required loose override pak does not appear fatal by itself |
| TKU-only, loose override disabled | `TheKnownUniverse` only | Disabled during test | Same fatal crash after Davion loading screen | `TheKnownUniverse.pak` is sufficient to trigger the fatal crash |
| Evidence starmap class patch | `TheKnownUniverse`, `TKUEvidenceStarmapCompat` | Present | Davion career start reached the loading screen and then hard-stalled with no new crash folder; later retry terminated/crashed without creating a newer crash folder than `10/05/2026 7:51:50 PM`; patch was disabled and rollback profile saved as `MW5Mercs\Mods\modlist.profile-tku-only-after-starmap-evidence-crash-20260510.json` | Replacing only old TKU `StarMapActor` / `StarSystemBody` changes the failure mode, so the stale starmap class stack is implicated, but the remaining TKU root asset mix is still inconsistent and this evidence patch is not viable |
| Evidence start-border patch | `TheKnownUniverse`, `TKUEvidenceStarmapCompat`, `TKUEvidenceStartBorderCompat` | Present | Crashed after 34 seconds with `Could not find SuperStruct BaseStarMapBorderActor_C to create StarMapActor_2570_C`; hash `6B39ADBEAC4A925A9AA74C71905744CB2C6A6097` | Direct vanilla cooked border overrides are unsafe; the border path needs editor-authored/reparented reconstruction or removal of unsafe TKU root border overrides |
| Evidence core plugin-only baseline | `TKUEvidenceCorePluginOnly` only | Present | Loaded successfully; starmap opened; map remained bounded by vanilla limits; territory overlay looked vanilla/incomplete and missed minor powers | Confirms the root-stripped TKU plugin-content baseline is stable, but also confirms expanded bounds and full TKU overlay are not restored by plugin content alone |
| Evidence bounds pawn patch | `TKUEvidenceCorePluginOnly`, `TKUEvidenceBoundsPawn` | Present | Career loaded, but pressing the starmap button entered first-person hangar view instead of opening the starmap | Old cooked TKU `StarMapPawn` is not a safe direct restore despite matching native parent/import-export shape; disabled |
| Evidence current pawn bounds patch | `TKUEvidenceCorePluginOnly`, `TKUEvidenceCurrentPawnBounds` | Present | Career loaded, but pressing the starmap button again entered first-person hangar view instead of opening the starmap | Even current-package cooked `StarMapPawn` substitution is unsafe for this setup; bounds must move to editor-authored asset workflow or another asset path |

## Current Evidence-Based Conclusion

The required loose `MW5Mercs-zKnownUniverseStarmap.pak` can coexist with the base game through a Davion career load. The fatal crash appears when TKU's mod pak content is enabled, and TKU's mod pak is sufficient to reproduce the same `0x4C` call-stack hash without the loose required override pak.

The first evidence starmap-class patch changed the repeated fatal crash into a hard loading stall with no new crash folder. That is a useful distinction: it supports the hypothesis that the old TKU starmap class stack is on the fatal path, but it does not authorize a broad vanilla override as a final fix. The active next target is the compatibility boundary between current `StarMapActor` / `StarSystemBody` and the still-active TKU root assets: `StarMapPawn`, dated border assets, faction materials, root faction/employer data, `SystemFactionChanges`, `EmployerInfoData`, and `MW5_TOI_Functions`.

A later retry of the same starmap evidence profile also failed/terminated without producing a newer crash folder. That makes the profile operationally useless for more testing, so `TKUEvidenceStarmapCompat` was disabled.

The follow-up start-border evidence patch failed with the known `BaseStarMapBorderActor_C` superstruct error, this time while creating vanilla `StarMapActor_2570_C`. That narrows the conclusion: cooked pak substitution of border assets is itself unsafe. The border side must be inspected and rebuilt/reparented in the editor, or excluded until the current-schema cluster/overlay path is reconstructed.

Editor inspection then confirmed the border crash mechanism: `StarMapActor_2570_C` is parented to current `/Game/.../BaseStarMapBorderActor_C`, and vanilla dated border actors share that parent. A clean-source `TKUEvidenceCorePluginOnly` baseline was built from original TKU build 38 with all root `/Game` substitutions removed. The runtime gate succeeded: the career and starmap loaded, but the starmap still used vanilla bounds and the territory overlay remained incomplete/vanilla-looking.

Both pawn-substitution bounds tests failed behaviorally: the old TKU pawn and the current-package CDO patch both allowed career load but caused the starmap button to enter first-person hangar view. That failure is useful because it proves package-table compatibility and readable CDO defaults are not enough for cooked `StarMapPawn` surgery. Bounds work must move to an editor-authored asset workflow or to a different inspected starmap asset path. Overlay work remains a separate modern `MWClusterDataAsset` migration problem.

## Completed Reversible Isolation

1. Exit MW5 cleanly.
2. Temporarily rename `MW5Mercs\Content\Paks\MW5Mercs-zKnownUniverseStarmap.pak` to `MW5Mercs-zKnownUniverseStarmap.pak.disabled-20260510`.
3. Enable only `TheKnownUniverse` in `modlist.json`.
4. Launch and reproduce Single Player -> New Career -> Davion.
5. Restore the loose pak immediately after the test.

Result: the same fatal crash reproduced, and the loose required override pak was restored afterward.

## Decision Meaning

- The primary fatal path is inside `TheKnownUniverse.pak`.
- The loose required override pak remains relevant for intended TKU starmap behavior, but it is not required for this fatal career-load crash.
- The evidence patch result makes the next target narrower than "all TKU content": cooked `StarMapPawn` substitution is ruled out; territory overlay needs current-schema cluster data.
- The start-border patch result rules out direct cooked vanilla reassertion of `BaseStarMapBorderActor` as a safe fix.

## What Not To Do

- Do not rebuild or repack TKU from this result alone.
- Do not restore the disabled load-order shim.
- Do not delete the loose required override pak.
- Do not re-enable `vonBiomes` until the TKU-only crash path is isolated.
- Do not iterate more starmap-class paks until the remaining active root asset mix has been traced.
- Do not re-enable `TKUEvidenceStartBorderCompat`; it reproduced the `BaseStarMapBorderActor_C` superstruct failure.
- Do not treat a successful bounds patch as an overlay fix; missing minor-power territory is still a data/cluster migration task.
- Do not re-enable `TKUEvidenceBoundsPawn`; it broke the starmap button into first-person hangar view.
- Do not re-enable `TKUEvidenceCurrentPawnBounds`; it reproduced the same starmap-button failure.
