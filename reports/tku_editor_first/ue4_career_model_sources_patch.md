# UE4 Career Model Sources Patch

- Generated: `2026-05-24T17:35:39.727387+00:00`
- Apply requested: `True`
- InnerSphere class: `/ModOverride/TKUCompatEditorPatch/InnerSphereData/StarSystemGenerator.StarSystemGenerator_C`
- Campaign generator target: `/ModOverride/TKUCompatEditorPatch/Campaign/_common/DefaultSystemGenerator`
- Scope: MW5GameMode, CampaignMode, and DLC1 CareerMode class defaults.

## Safety

- No safety failures.

## Result

- Attempted: `True`
- Applied: `True`
- Saved: `True`
- Reason: `None`

## Assets

### `/ModOverride/TKUCompatEditorPatch/Campaign/_common/DefaultSystemGenerator`
- Source: `/Game/Campaign/_common/DefaultSystemGenerator`
- File: `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins\TKUCompatEditorPatch\ModOverride\Campaign\_common\DefaultSystemGenerator.uasset`
- Saved: `True`

### `/ModOverride/TKUCompatEditorPatch/Modes/MW5GameMode`
- Source: `/Game/Modes/MW5GameMode`
- File: `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins\TKUCompatEditorPatch\ModOverride\Modes\MW5GameMode.uasset`
- Saved: `True`
- Backup: `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\backups\TKUCompatEditorPatch_career_model_sources_patch\ModOverride\Modes\MW5GameMode.uasset`
- DefaultInnerSphereClass: `/ModOverride/TKUCompatEditorPatch/InnerSphereData/StarSystemGenerator.StarSystemGenerator_C`
- CampaignSystemGeneratorClass: `/ModOverride/TKUCompatEditorPatch/Campaign/_common/DefaultSystemGenerator.DefaultSystemGenerator_C`

### `/ModOverride/TKUCompatEditorPatch/Modes/CampaignMode`
- Source: `/Game/Modes/CampaignMode`
- File: `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins\TKUCompatEditorPatch\ModOverride\Modes\CampaignMode.uasset`
- Saved: `True`
- Backup: `D:\Downloads\OneDrive\Documents\code\tku-update\reports\tku_editor_first\backups\TKUCompatEditorPatch_career_model_sources_patch\ModOverride\Modes\CampaignMode.uasset`
- DefaultInnerSphereClass: `/ModOverride/TKUCompatEditorPatch/InnerSphereData/StarSystemGenerator.StarSystemGenerator_C`
- CampaignSystemGeneratorClass: `/ModOverride/TKUCompatEditorPatch/Campaign/_common/DefaultSystemGenerator.DefaultSystemGenerator_C`

### `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/CareerMode`
- Source: `/Game/DLC1/CareerMode/StartConditions/CareerMode`
- File: `E:\Games\MechWarrior5Editor\MW5Mercs\Plugins\TKUCompatEditorPatch\ModOverride\DLC1\CareerMode\StartConditions\CareerMode.uasset`
- Saved: `True`
- DefaultInnerSphereClass: `/ModOverride/TKUCompatEditorPatch/InnerSphereData/StarSystemGenerator.StarSystemGenerator_C`
- CampaignSystemGeneratorClass: `/ModOverride/TKUCompatEditorPatch/Campaign/_common/DefaultSystemGenerator.DefaultSystemGenerator_C`

## Before/After

### `/Game/Modes/MW5GameMode`
- Target: `/ModOverride/TKUCompatEditorPatch/Modes/MW5GameMode`
- Before DefaultInnerSphereClass: `/ModOverride/TKUCompatEditorPatch/InnerSphereData/StarSystemGenerator.StarSystemGenerator_C`
- Before CampaignSystemGeneratorClass: `/Game/Campaign/_common/DefaultSystemGenerator.DefaultSystemGenerator_C`
- After DefaultInnerSphereClass: `/ModOverride/TKUCompatEditorPatch/InnerSphereData/StarSystemGenerator.StarSystemGenerator_C`
- After CampaignSystemGeneratorClass: `/ModOverride/TKUCompatEditorPatch/Campaign/_common/DefaultSystemGenerator.DefaultSystemGenerator_C`
### `/Game/Modes/CampaignMode`
- Target: `/ModOverride/TKUCompatEditorPatch/Modes/CampaignMode`
- Before DefaultInnerSphereClass: `/ModOverride/TKUCompatEditorPatch/InnerSphereData/StarSystemGenerator.StarSystemGenerator_C`
- Before CampaignSystemGeneratorClass: `/Game/Campaign/_common/DefaultSystemGenerator.DefaultSystemGenerator_C`
- After DefaultInnerSphereClass: `/ModOverride/TKUCompatEditorPatch/InnerSphereData/StarSystemGenerator.StarSystemGenerator_C`
- After CampaignSystemGeneratorClass: `/ModOverride/TKUCompatEditorPatch/Campaign/_common/DefaultSystemGenerator.DefaultSystemGenerator_C`
### `/Game/DLC1/CareerMode/StartConditions/CareerMode`
- Target: `/ModOverride/TKUCompatEditorPatch/DLC1/CareerMode/StartConditions/CareerMode`
- Before DefaultInnerSphereClass: `/ModOverride/TKUCompatEditorPatch/InnerSphereData/StarSystemGenerator.StarSystemGenerator_C`
- Before CampaignSystemGeneratorClass: `/Game/Campaign/_common/DefaultSystemGenerator.DefaultSystemGenerator_C`
- After DefaultInnerSphereClass: `/ModOverride/TKUCompatEditorPatch/InnerSphereData/StarSystemGenerator.StarSystemGenerator_C`
- After CampaignSystemGeneratorClass: `/ModOverride/TKUCompatEditorPatch/Campaign/_common/DefaultSystemGenerator.DefaultSystemGenerator_C`