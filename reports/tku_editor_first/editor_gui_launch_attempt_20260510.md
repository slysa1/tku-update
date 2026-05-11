# MW5 Mod Editor GUI Launch Attempt - 2026-05-10

- Goal: open the MW5 Mod Editor GUI for the first safe `Create Mod` step.
- Project: `E:\Games\MechWarrior5Editor\MW5Mercs\MW5Mercs.uproject`
- Safety: no assets, paks, mod files, or modlists were intentionally modified.

## Attempt 1: Direct UE4Editor Launch

- Command path: `E:\Games\MechWarrior5Editor\Engine\Binaries\Win64\UE4Editor.exe`
- Result: process `41600` launched and responded.
- Evidence from log:
  - Generated Python stub at `E:\Games\MechWarrior5Editor\MW5Mercs\Intermediate\PythonStub\unreal.py`.
  - Asset discovery completed.
  - Shader compilation progressed to `1` remaining.
- Blocking observation:
  - `MainWindowHandle` remained `0`.
  - No usable top-level editor window was exposed to this Codex session.
  - No `TKUCompatEditorPatch` mod or plugin target appeared.
- Cleanup: process `41600` was stopped after the launch stayed invisible/headless.

## Attempt 2: Explorer/Uproject Association

- Command path: `explorer.exe` with the `.uproject` path.
- Result: command returned, but no `UE4Editor` process appeared after the check interval.

## Decision

The first safe MW5 editor `Create Mod` gate still requires a manual interactive editor launch/action by the user. The target to create is:

- Mod name: `TKUCompatEditorPatch`

After that target exists, continue with:

1. Inspect the created `Mods` and `Plugins` filesystem deltas.
2. Confirm the active editor mod metadata.
3. Use the editor `Save To Mod` path or a controlled mod-owned Python import path for `/Game/InnerSphereData/MW5_InnerSphereData`.
4. Do not package until the imported row count and sample rows verify cleanly.

Build authorized: `false`.
