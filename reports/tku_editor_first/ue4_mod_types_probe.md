# UE4 MW5 Mod Types Probe

- Generated: `2026-05-10T11:34:59.185236+00:00`
- Method: non-mutating `UE4Editor-Cmd -run=pythonscript` introspection.
- Safety: did not call `set_active_mod`, `create_mod_entry`, `package_mod`, `save_asset`, `duplicate_asset`, or any asset-writing API.

## Decision

Editor Python exposes MW5 mod metadata structs and read-only mod utilities. It exposes MWModEditorWidget.package_mod(args), but no direct module-level CreateMod, SaveToMod, or SaveTo symbol was found by this probe.

- Can create a complete MW5 mod via direct Python API: `False`
- Can package via Python without a UI widget instance: `False`
- Package API appears to require `MWModEditorWidget.package_mod(args)`: `True`
- Manual editor UI required for safe `Create Mod` / `Save To Mod` until a widget workflow is proven: `True`

## Runtime State

- `workspace`: `E:\SteamLibrary\steamapps\common\MechWarrior 5 Mercenaries`
- `editor_root`: `E:\Games\MechWarrior5Editor`
- `project`: `E:\Games\MechWarrior5Editor\MW5Mercs\MW5Mercs.uproject`
- `stub_path`: `E:\Games\MechWarrior5Editor\MW5Mercs\Intermediate\PythonStub\unreal.py`

## Matching Unreal Symbols

### `MWModPluginInfo`
- `MWModPluginInfo`

### `ModPackageArgs`
- `ModPackageArgs`

### `ModPackage`
- `ModPackageArgs`

### `MWMod`
- `MWModEditorWidget`
- `MWModPluginInfo`
- `MWModUtils`

### `ModPlugin`
- `MWModPluginInfo`

### `PackageMod`
- None found

### `CreateMod`
- None found

### `SaveToMod`
- None found

### `SaveTo`
- None found

## Exact Type Summaries

### `MWModPluginInfo`
- Exists: `True`
- Public member count: `20`

### `ModPackageArgs`
- Exists: `True`
- Public member count: `13`

### `MWModUtils`
- Exists: `True`
- Public member count: `41`

### `MWModEditorWidget`
- Exists: `True`
- Public member count: `196`

### `ModInfo`
- Exists: `True`
- Public member count: `20`

### `ModList`
- Exists: `True`
- Public member count: `10`

### `ModListEntry`
- Exists: `True`
- Public member count: `12`

### `ModStatus`
- Exists: `True`
- Public member count: `9`

### `ModPlatform`
- Exists: `True`
- Public member count: `9`

### `ModConflict`
- Exists: `True`
- Public member count: `11`

### `PublishedModVisibility`
- Exists: `True`
- Public member count: `7`

## Struct Constructor Samples

### `MWModPluginInfo_default`
- Constructed: `True`
- `mod_name`: ``
- `plugin_path`: ``
- `version_name`: ``
- `friendly_name`: ``
- `description`: ``
- `category`: ``
- `created_by`: ``
- `created_by_url`: ``
- `docs_url`: ``
- `marketplace_url`: ``
- `support_url`: ``
- `engine_version`: ``

### `MWModPluginInfo_sample`
- Constructed: `True`
- `mod_name`: `__TKUProbeNoCreate__`
- `plugin_path`: `__NoDiskPath__`
- `version_name`: `0.0-probe`
- `friendly_name`: `TKU Probe No Create`
- `description`: `Non-mutating constructor sample`
- `category`: `Probe`
- `created_by`: `Codex`
- `created_by_url`: ``
- `docs_url`: ``
- `marketplace_url`: ``
- `support_url`: ``
- `engine_version`: `4.27`

### `ModPackageArgs_default`
- Constructed: `True`
- `mod_name`: ``
- `skip_packaging`: `False`
- `output_to_folder`: `False`
- `publish_to_steam`: `False`
- `steam_visibility`: ``

### `ModPackageArgs_sample`
- Constructed: `True`
- `mod_name`: `__TKUProbeNoPackage__`
- `skip_packaging`: `True`
- `output_to_folder`: `True`
- `publish_to_steam`: `False`
- `steam_visibility`: `Private`

## Safe MWModUtils Calls

### `get_mods_install_path`
- OK: `True`
  E:/Games/MechWarrior5Editor/MW5Mercs/Mods/

### `get_mod_plugin_names`
- OK: `True`
  []

### `get_active_mod_plugin`
- OK: `True`
  {
    "repr": "<Struct 'MWModPluginInfo' (0x0000022187F22200) {mod_name: \"\", plugin_path: \"\", version_name: \"\", friendly_name: \"\", description: \"\", category: \"\", created_by: \"\", created_by_url: \"\", docs_url: \"\", marketplace_url: \"\", support_url: \"\", engine_version: \"\"}>",
    "python_type": "MWModPluginInfo"
  }

### `get_active_mod_entry`
- OK: `True`
  {
    "repr": "<Struct 'ModListEntry' (0x0000022187F21240) {mod_name: \"\", info: {display_name: \"\", version: \"\", build_number: 0, description: \"\", author: \"\", author_url: \"\", default_load_order: 0.000000, game_version: \"\", manifest: , steam_published_file_id: 0, steam_last_submitted_build_number: 0, steam_mod_visibility: Private}, status: {enabled: False}, origin: None}>",
    "python_type": "ModListEntry"
  }

### `get_mod_platform`
- OK: `True`
  {
    "repr": "<ModPlatform.NONE: 0>",
    "python_type": "ModPlatform"
  }

### `get_mod_list(False)`
- OK: `True`
  []

### `get_mod_list(True)`
- OK: `True`
  []

### `get_enabled_mod_list`
- OK: `True`
  []

### `get_running_mods`
- OK: `True`
  []

### `get_mod_status_list`
- OK: `True`
  {
    "repr": "<Struct 'ModList' (0x0000022192D253C0) {game_version: \"1.13.64\", mod_status: ()}>",
    "python_type": "ModList"
  }

## Editor Widget Probe

- `MWModEditorWidget` exists: `True`
- `package_mod` member present: `True`
- Constructor attempt constructed: `False`
- Constructor error: `Exception: MWModEditorWidget: Class 'MWModEditorWidget' is abstract`

## Editor Utility Asset Matches

### `/Game/UI/Editor`
- Exists: `True`
- Asset count: `9`
- `/Game/UI/Editor/Mods/ManageMod_Checkmark_64x_ICN.ManageMod_Checkmark_64x_ICN`
- `/Game/UI/Editor/Mods/ManageMod_XMark_64x_ICN.ManageMod_XMark_64x_ICN`
- `/Game/UI/Editor/Mods/ManageModEditorWidget.ManageModEditorWidget`

### `/Game/UI`
- Exists: `True`
- Asset count: `3842`
- `/Game/UI/_common/Textures/Icons/Sensors/Vision_Mode_ICN_48px.Vision_Mode_ICN_48px`
- `/Game/UI/_common/Textures/Icons/Sensors/Vision_Mode_Night_ICN_48px.Vision_Mode_Night_ICN_48px`
- `/Game/UI/_common/Textures/Icons/Sensors/Vision_Mode_Thermal_ICN_48px.Vision_Mode_Thermal_ICN_48px`
- `/Game/UI/_common/Textures/Icons/Sensors/Vision_Mode_Zoom_ICN_48px.Vision_Mode_Zoom_ICN_48px`
- `/Game/UI/BattleGrid/Textures/StoryMissions/A1M1_AmmoDump.A1M1_AmmoDump`
- `/Game/UI/Editor/Mods/ManageMod_Checkmark_64x_ICN.ManageMod_Checkmark_64x_ICN`
- `/Game/UI/Editor/Mods/ManageMod_XMark_64x_ICN.ManageMod_XMark_64x_ICN`
- `/Game/UI/Editor/Mods/ManageModEditorWidget.ManageModEditorWidget`
- `/Game/UI/FrontEnd/Codex/Entries/MechLab/ViewModes_CodexEntry.ViewModes_CodexEntry`
- `/Game/UI/FrontEnd/Components/SaveMechDialogBox.SaveMechDialogBox`
- `/Game/UI/FrontEnd/Marketplace/ESortMode.ESortMode`
- `/Game/UI/FrontEnd/Mods/Assets/DetailsArrow.DetailsArrow`
- `/Game/UI/FrontEnd/Mods/Assets/EGSLogo_Default_ICN.EGSLogo_Default_ICN`
- `/Game/UI/FrontEnd/Mods/Assets/EGSLogo_Hovered_ICN.EGSLogo_Hovered_ICN`
- `/Game/UI/FrontEnd/Mods/Assets/EmptyCheckbox.EmptyCheckbox`
- `/Game/UI/FrontEnd/Mods/Assets/expand_window_icon.expand_window_icon`
- `/Game/UI/FrontEnd/Mods/Assets/FilledCheckbox.FilledCheckbox`
- `/Game/UI/FrontEnd/Mods/Assets/ModDetailsFrame.ModDetailsFrame`
- `/Game/UI/FrontEnd/Mods/Assets/ModFrame.ModFrame`
- `/Game/UI/FrontEnd/Mods/Assets/SteamIconOnly-Inverted.SteamIconOnly-Inverted`
- `/Game/UI/FrontEnd/Mods/Assets/SteamIconOnly.SteamIconOnly`
- `/Game/UI/FrontEnd/Mods/Assets/SteamWorkShop_Default_ICN.SteamWorkShop_Default_ICN`
- `/Game/UI/FrontEnd/Mods/Assets/SteamWorkshop_Hovered_ICN.SteamWorkshop_Hovered_ICN`
- `/Game/UI/FrontEnd/Mods/Assets/TabbedFolder-Inverted.TabbedFolder-Inverted`
- `/Game/UI/FrontEnd/Mods/Assets/TabbedFolder.TabbedFolder`
- `/Game/UI/FrontEnd/Mods/ModConflictDetails.ModConflictDetails`
- `/Game/UI/FrontEnd/Mods/ModScreenEntry.ModScreenEntry`
- `/Game/UI/FrontEnd/Mods/ModsScreen.ModsScreen`
- `/Game/UI/SaveLoad/LoadScreen/CampaignComponentDisplayData.CampaignComponentDisplayData`
- `/Game/UI/SaveLoad/LoadScreen/CampaignDLCLockComponent.CampaignDLCLockComponent`
- `/Game/UI/SaveLoad/LoadScreen/CampaignDLCToolTip.CampaignDLCToolTip`
- `/Game/UI/SaveLoad/LoadScreen/CampaignDLCToolTipItem.CampaignDLCToolTipItem`
- `/Game/UI/SaveLoad/LoadScreen/CampaignLockDisplayData.CampaignLockDisplayData`
- `/Game/UI/SaveLoad/LoadScreen/ImportSaveScreen.ImportSaveScreen`
- `/Game/UI/SaveLoad/LoadScreen/LoadActionComponent.LoadActionComponent`
- `/Game/UI/SaveLoad/LoadScreen/LoadCampaignList_Wireframe.LoadCampaignList_Wireframe`
- `/Game/UI/SaveLoad/LoadScreen/LoadGameCampaignList.LoadGameCampaignList`
- `/Game/UI/SaveLoad/LoadScreen/LoadGameSaveList.LoadGameSaveList`
- `/Game/UI/SaveLoad/LoadScreen/LoadGameScreen.LoadGameScreen`
- `/Game/UI/SaveLoad/LoadScreen/LoadSaveList_Wireframe.LoadSaveList_Wireframe`
- `/Game/UI/SaveLoad/LoadScreen/LoadScreenCampaignComponent.LoadScreenCampaignComponent`
- `/Game/UI/SaveLoad/LoadScreen/LoadScreenSaveComponent.LoadScreenSaveComponent`
- `/Game/UI/SaveLoad/LoadScreen/NewCampaign_Wireframe.NewCampaign_Wireframe`
- `/Game/UI/SaveLoad/LoadScreen/SaveLoadDialog.SaveLoadDialog`
- `/Game/UI/SaveLoad/SaveLoadButton.SaveLoadButton`
- `/Game/UI/SaveLoad/SaveScreen/SaveActionComponent.SaveActionComponent`
- `/Game/UI/SaveLoad/SaveScreen/SaveActionState.SaveActionState`
- `/Game/UI/SaveLoad/SaveScreen/SaveGameScreen.SaveGameScreen`
- `/Game/UI/Textures/GenericButtons_Icons/FE_ModUpdateAlert_ICN_32PX.FE_ModUpdateAlert_ICN_32PX`

### `/Game/Editor`
- Exists: `False`
