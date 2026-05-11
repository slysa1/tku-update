# Editor InnerSphere Source Analysis

This report inspects source-style data included with the MW5 Mod Editor. It does not modify editor or game assets.

## Counts

- `inner_sphere_json_rows`: 3446
- `source_employer_rows`: 143
- `source_system_faction_rows`: 3158
- `runtime_inner_sphere_csv_rows`: 2173

## Coordinate Ranges

- `inner_sphere_json`: X -1875.9410400390625 to 1935.8389892578125, Y -1919.68896484375 to 1910.759033203125
- `runtime_inner_sphere_csv`: X -517.0 to 685.0, Y -524.0 to 552.0

## Parse Notes

- `SystemFactionChanges.json`: {'encoding': 'utf-16-le', 'line_ending_repair': "replace b'\\r\\n\\x00' with b'\\n\\x00'", 'repair_bytes_removed': 57002}
- `MW5_InnerSphereData.csv`: parsed as UTF-16

## Term Counts

- `Clan`: {'inner_json_count': 10, 'employer_count': 24, 'system_faction_count': 37, 'runtime_inner_csv_count': 0}
- `Lyran`: {'inner_json_count': 0, 'employer_count': 2, 'system_faction_count': 0, 'runtime_inner_csv_count': 41}
- `Steiner`: {'inner_json_count': 0, 'employer_count': 0, 'system_faction_count': 0, 'runtime_inner_csv_count': 33}
- `ComStar`: {'inner_json_count': 1, 'employer_count': 1, 'system_faction_count': 0, 'runtime_inner_csv_count': 1}
- `FederatedCommonwealth`: {'inner_json_count': 0, 'employer_count': 2, 'system_faction_count': 0, 'runtime_inner_csv_count': 0}
- `Wolf`: {'inner_json_count': 2, 'employer_count': 3, 'system_faction_count': 2, 'runtime_inner_csv_count': 0}

## Top Faction Codes In Source SystemFactionChanges

- `FC`: 1055
- `FS`: 1000
- `IND`: 915
- `LA`: 867
- `ABN`: 837
- `DC`: 803
- `FWL`: 721
- `CC`: 645
- `RWR`: 404
- `TH`: 402
- `PIND`: 283
- `TA`: 172
- `OA`: 166
- `TC`: 149
- `MOC`: 105
- `FRR`: 84
- `FoS`: 75
- `AG`: 69
- `FWLR`: 65
- `CCom`: 64
- `DA`: 64
- `HL`: 58
- `TamP`: 50
- `SSUP`: 48
- `SIS`: 36
- `TGU`: 35
- `CLAN`: 34
- `SIMA`: 30
- `PD`: 26
- `TFR`: 23
- `PoR`: 21
- `MCM`: 19
- `CF`: 19
- `OC`: 19
- `NC`: 18
- `MH`: 17
- `SIC`: 17
- `AXP`: 13
- `CIH`: 12
- `CJF`: 12

## Key Samples

### `inner_json_clan`

- `{"Name": "45", "StarSystemName": "Albion (Clan)", "PosX": -50.19599914550781, "PosY": 1790.72705078125, "SystemStatus": "Normal"}`
- `{"Name": "133", "StarSystemName": "Arcadia (Clan)", "PosX": -115.55699920654297, "PosY": 1607.54296875, "SystemStatus": "Normal"}`
- `{"Name": "165", "StarSystemName": "Atreus (Clan)", "PosX": 71.78199768066406, "PosY": 1732.8289794921875, "SystemStatus": "Normal"}`
- `{"Name": "512", "StarSystemName": "Dagda (Clan)", "PosX": -132.16799926757812, "PosY": 1602.5989990234375, "SystemStatus": "Normal"}`
- `{"Name": "1438", "StarSystemName": "Niles (Clan)", "PosX": 118.96499633789062, "PosY": 1705.4139404296875, "SystemStatus": "Normal"}`
- `{"Name": "1785", "StarSystemName": "Sheridan (Clan)", "PosX": 125.91400146484375, "PosY": 1792.81396484375, "SystemStatus": "Normal"}`
- `{"Name": "1970", "StarSystemName": "Tiber (Clan)", "PosX": 89.48500061035156, "PosY": 1875.31298828125, "SystemStatus": "Normal"}`
- `{"Name": "2167", "StarSystemName": "York (Clan)", "PosX": -70.86299896240234, "PosY": 1805.593994140625, "SystemStatus": "Normal"}`

### `source_employer_clan`

- `{"Short": "CB", "Employer": "(Id=\"MWEmployerAsset:ClanBurrock\")"}`
- `{"Short": "CBS", "Employer": "(Id=\"MWEmployerAsset:ClanBloodSpirit\")"}`
- `{"Short": "CCC", "Employer": "(Id=\"MWEmployerAsset:ClanCloudCobra\")"}`
- `{"Short": "CCO", "Employer": "(Id=\"MWEmployerAsset:ClanCoyote\")"}`
- `{"Short": "CDS", "Employer": "(Id=\"MWEmployerAsset:ClanDiamondShark\")"}`
- `{"Short": "CFM", "Employer": "(Id=\"MWEmployerAsset:ClanFireMandrill\")"}`
- `{"Short": "CGB", "Employer": "(Id=\"MWEmployerAsset:ClanGhostBear\")"}`
- `{"Short": "CGS", "Employer": "(Id=\"MWEmployerAsset:ClanGoliathScorpion\")"}`

### `source_employer_lyran`

- `{"Short": "LA", "Employer": "(Id=\"MWEmployerAsset:LyranAlliance\")"}`
- `{"Short": "LC", "Employer": "(Id=\"MWEmployerAsset:LyranCommonwealth\")"}`

### `system_faction_clan`

- `{"Name": "Albion(Clan)", "Primary": "Albion (Clan)", "FactionChange": [{"Date": "2786-08-24", "Faction": "SLIE"}, {"Date": "2802-06-11", "Faction": "CB"}, {"Date": "2821-01-01", "Faction": "CB"}]}`
- `{"Name": "Arcadia(Clan)", "Primary": "Arcadia (Clan)", "FactionChange": [{"Date": "2786-08-24", "Faction": "SLIE"}, {"Date": "2802-06-11", "Faction": "CGB,CSA,CSV"}, {"Date": "2821-01-01", "Faction": "IND"}, {"Date": "2822-01-01", "Faction": "CLAN"}]}`
- `{"Name": "Atreus(Clan)", "Primary": "Atreus (Clan)", "FactionChange": [{"Date": "2802-06-11", "Faction": "CFM,CIH"}, {"Date": "2900-01-01", "Faction": "CSJ,CFM,CIH"}, {"Date": "3025-01-01", "Faction": "CLAN"}]}`
- `{"Name": "Babylon", "Primary": "Babylon", "FactionChange": [{"Date": "2786-08-24", "Faction": "SLIE"}, {"Date": "2802-06-11", "Faction": "CCO,CCC,CDS,CIH"}, {"Date": "2864-01-01", "Faction": "CLAN"}]}`
- `{"Name": "Barcella", "Primary": "Barcella", "FactionChange": [{"Date": "2802-06-11", "Faction": "CNC"}, {"Date": "2821-01-01", "Faction": "CNC"}, {"Date": "3000-01-01", "Faction": "CNC,CIH,CJF"}, {"Date": "3025-01-01", "Faction": "CLAN"}]}`
