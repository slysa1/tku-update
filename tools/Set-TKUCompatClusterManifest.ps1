param(
    [switch]$Apply,
    [string]$ModName = 'TKUCompatEditorPatch',
    [string]$GameVersion = '1.13.378',
    [string]$Description = 'Editor-authored compatibility patch for Known Universe on MW5 1.13.x / DLC7 (Steam/GOG 1.13.378)',
    [int]$DefaultLoadOrder = 95,
    [switch]$IncludePackagedCopies,
    [switch]$IncludeLiveDeployedCopy
)

$ErrorActionPreference = 'Stop'

function Get-TkuPathConfig {
    param([string]$ProjectRoot)

    $configCandidates = @()
    if ($env:TKU_PATHS_CONFIG) {
        $configCandidates += $env:TKU_PATHS_CONFIG
    }
    $configCandidates += @(
        (Join-Path $ProjectRoot 'config\tku_paths.local.json'),
        (Join-Path $ProjectRoot 'config\tku_paths.json'),
        (Join-Path $ProjectRoot 'config\tku_paths.example.json')
    )

    foreach ($candidate in $configCandidates) {
        if (Test-Path -LiteralPath $candidate) {
            return Get-Content -LiteralPath $candidate -Raw | ConvertFrom-Json
        }
    }

    throw "No TKU path config found."
}

function Save-JsonFile {
    param(
        [object]$Value,
        [string]$Path
    )
    $json = $Value | ConvertTo-Json -Depth 30
    Set-Content -LiteralPath $Path -Value $json -Encoding UTF8
}

function Get-SafeBackupName {
    param(
        [string]$Kind,
        [string]$Suffix
    )
    $safeKind = $Kind -replace '[^A-Za-z0-9]+', '-'
    return "$safeKind.$Suffix"
}

$projectRoot = Split-Path -Parent $PSScriptRoot
$pathConfig = Get-TkuPathConfig -ProjectRoot $projectRoot
$editorRoot = if ($env:TKU_MW5_EDITOR_ROOT) { $env:TKU_MW5_EDITOR_ROOT } else { $pathConfig.mw5_editor_root }
$liveModsRoot = if ($env:TKU_LOCAL_MODS_ROOT) { $env:TKU_LOCAL_MODS_ROOT } else { $pathConfig.local_mods_root }

$baseManifestAssets = @(
    '/Game/Campaign/_common/DefaultSystemGenerator.uasset',
    '/Game/DLC1/CareerMode/StartConditions/CareerMode.uasset',
    '/Game/InnerSphereData/MW5_InnerSphereData.uasset',
    '/Game/InnerSphereData/StarSystemGenerator.uasset',
    '/Game/Modes/CampaignMode.uasset',
    '/Game/Modes/MW5GameMode.uasset',
    '/Game/UI/FrontEnd/StarMapPawn.uasset',
    '/Game/Levels/FrontEnd/StarMap.umap'
)

$clusterManifestAssets = @(
    '/Game/Campaign/Clusters/TKU_ClanConflict/ClanConflict.uasset',
    '/Game/Campaign/Clusters/TKU_ClanConflict/TKU_ClanConflict_NoOverlay_ClusterAsset.uasset',
    '/Game/Campaign/Clusters/TKU_ClanConflict_Zones_ClanConf_1/TKU_ClanConflict_Zones_ClanConf_1_ClusterAsset.uasset',
    '/Game/Campaign/Clusters/TKU_ClanConflict_Zones_ClanConf_2/TKU_ClanConflict_Zones_ClanConf_2_ClusterAsset.uasset',
    '/Game/Campaign/Clusters/TKU_ClanConflict_Zones_ClanConf_3/TKU_ClanConflict_Zones_ClanConf_3_ClusterAsset.uasset',
    '/Game/Campaign/Clusters/TKU_ClanConflict_Zones_ClanConf_4/TKU_ClanConflict_Zones_ClanConf_4_ClusterAsset.uasset',
    '/Game/Campaign/Clusters/TKU_RepairSystem_Clan/RepairSystem_Clan.uasset',
    '/Game/Campaign/Clusters/TKU_RepairSystem_Clan/TKU_RepairSystem_Clan_NoOverlay_ClusterAsset.uasset',
    '/Game/Campaign/Clusters/TKU_RepairSystem_Clan_Zones_Clan_Safezone_1/TKU_RepairSystem_Clan_Zones_Clan_Safezone_1_ClusterAsset.uasset',
    '/Game/Campaign/Clusters/TKU_RepairSystem_Clan_Zones_Clan_Safezone_2/TKU_RepairSystem_Clan_Zones_Clan_Safezone_2_ClusterAsset.uasset'
)

$activeCareerSourceManifestAssets = @(
    '/Game/DLC1/CareerMode/StartConditions/CareerMode_Davion_Start.uasset',
    '/Game/DLC1/CareerMode/StartConditions/CareerMode_Davion_Start_Tutorial.uasset',
    '/Game/DLC1/CareerMode/StartConditions/CareerMode_FRR_Start.uasset',
    '/Game/DLC1/CareerMode/StartConditions/CareerMode_FRR_Start_Tutorial.uasset',
    '/Game/DLC1/CareerMode/StartConditions/CareerMode_Kurita_Start.uasset',
    '/Game/DLC1/CareerMode/StartConditions/CareerMode_Kurita_Start_Tutorial.uasset',
    '/Game/DLC1/CareerMode/StartConditions/CareerMode_Liao_Start.uasset',
    '/Game/DLC1/CareerMode/StartConditions/CareerMode_Liao_Start_Tutorial.uasset',
    '/Game/DLC1/CareerMode/StartConditions/CareerMode_Marik_Start.uasset',
    '/Game/DLC1/CareerMode/StartConditions/CareerMode_Marik_Start_Tutorial.uasset',
    '/Game/DLC1/CareerMode/StartConditions/CareerMode_Steiner_Start.uasset',
    '/Game/DLC1/CareerMode/StartConditions/CareerMode_Steiner_Start_Tutorial.uasset',
    '/Game/DLC1/CareerMode/StartConditions/CareerMode_Start.uasset',
    '/Game/DLC1/CareerMode/StartConditions/FRR_CareerMode_Start.uasset',
    '/Game/DLC1/CareerMode/CareerModeCoreCampaign.uasset',
    '/Game/DLC1/CareerMode/StartConditions/Arcs/CareerModeClusters.uasset',
    '/Game/DLC1/CareerMode/StartConditions/Arcs/CareerMode_SafeZones.uasset'
)

$activeClusterDiagnosticManifestAssets = @(
    '/Game/DLC1/CareerMode/Clusters/Rasalhague_7_10/Rasalhague_7_10_ClusterAsset.uasset'
)

$targets = @(
    [ordered]@{
        kind = 'editor source mod.json'
        path = Join-Path $editorRoot "MW5Mercs\Plugins\$ModName\mod.json"
    }
)

if ($IncludePackagedCopies) {
    $targets += @(
        [ordered]@{
            kind = 'editor package root mod.json'
            path = Join-Path $editorRoot "MW5Mercs\Mods\$ModName\mod.json"
        },
        [ordered]@{
            kind = 'editor package copy mod.json'
            path = Join-Path $editorRoot "MW5Mercs\Mods\$ModName\$ModName\mod.json"
        },
        [ordered]@{
            kind = 'editor nested package copy mod.json'
            path = Join-Path $editorRoot "MW5Mercs\Mods\$ModName\$ModName\$ModName\mod.json"
        }
    )
}

if ($IncludeLiveDeployedCopy) {
    $targets += [ordered]@{
        kind = 'live deployed mod.json'
        path = Join-Path $liveModsRoot "$ModName\mod.json"
    }
}

$timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$reportDir = Join-Path $projectRoot 'reports\tku_editor_first'
$backupDir = Join-Path $reportDir "backups\cluster_manifest_$timestamp"
$reportPath = Join-Path $reportDir "tku_cluster_manifest_$timestamp.json"
$reportMdPath = Join-Path $reportDir "tku_cluster_manifest_$timestamp.md"
$changes = @()

foreach ($target in $targets) {
    $path = $target.path
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        $changes += [ordered]@{
            kind = $target.kind
            path = $path
            status = 'missing'
        }
        continue
    }

    $json = Get-Content -LiteralPath $path -Raw | ConvertFrom-Json
    $beforeManifest = @($json.manifest)
    $manifest = [System.Collections.Generic.List[string]]::new()
    foreach ($entry in $beforeManifest) {
        if (-not [string]::IsNullOrWhiteSpace([string]$entry) -and -not $manifest.Contains([string]$entry)) {
            $manifest.Add([string]$entry)
        }
    }

    $requiredManifest = @($baseManifestAssets + $clusterManifestAssets + $activeCareerSourceManifestAssets + $activeClusterDiagnosticManifestAssets)
    $added = @()
    foreach ($entry in $requiredManifest) {
        if (-not $manifest.Contains($entry)) {
            $manifest.Add($entry)
            $added += $entry
        }
    }

    $before = [ordered]@{
        description = $json.description
        gameVersion = $json.gameVersion
        defaultLoadOrder = $json.defaultLoadOrder
        manifestCount = $beforeManifest.Count
        clusterManifestCount = @($beforeManifest | Where-Object { $_ -like '/Game/Campaign/Clusters/TKU_*' }).Count
        activeCareerSourceManifestCount = @($beforeManifest | Where-Object { $activeCareerSourceManifestAssets -contains $_ }).Count
        activeClusterDiagnosticManifestCount = @($beforeManifest | Where-Object { $activeClusterDiagnosticManifestAssets -contains $_ }).Count
    }

    $json.description = $Description
    $json.gameVersion = $GameVersion
    $json.defaultLoadOrder = $DefaultLoadOrder
    $json.manifest = @($manifest)

    $after = [ordered]@{
        description = $json.description
        gameVersion = $json.gameVersion
        defaultLoadOrder = $json.defaultLoadOrder
        manifestCount = @($json.manifest).Count
        clusterManifestCount = @($json.manifest | Where-Object { $_ -like '/Game/Campaign/Clusters/TKU_*' }).Count
        activeCareerSourceManifestCount = @($json.manifest | Where-Object { $activeCareerSourceManifestAssets -contains $_ }).Count
        activeClusterDiagnosticManifestCount = @($json.manifest | Where-Object { $activeClusterDiagnosticManifestAssets -contains $_ }).Count
    }

    if ($Apply) {
        New-Item -ItemType Directory -Force -Path $backupDir | Out-Null
        Copy-Item -LiteralPath $path -Destination (Join-Path $backupDir (Get-SafeBackupName -Kind $target.kind -Suffix 'mod.json'))
        Save-JsonFile -Value $json -Path $path
    }

    $changes += [ordered]@{
        kind = $target.kind
        path = $path
        status = $(if ($Apply) { 'updated' } else { 'planned' })
        before = $before
        after = $after
        addedManifestEntries = $added
    }
}

$report = [ordered]@{
    generated = (Get-Date).ToString('o')
    apply_requested = [bool]$Apply
    mod_name = $ModName
    target_game_version = $GameVersion
    target_description = $Description
    default_load_order = $DefaultLoadOrder
    required_cluster_manifest_assets = $clusterManifestAssets
    required_active_career_source_manifest_assets = $activeCareerSourceManifestAssets
    required_active_cluster_diagnostic_manifest_assets = $activeClusterDiagnosticManifestAssets
    backup_dir = $(if ($Apply) { $backupDir } else { $null })
    changes = $changes
}

New-Item -ItemType Directory -Force -Path $reportDir | Out-Null
$report | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath $reportPath -Encoding UTF8

$lines = @(
    "# TKU Cluster Manifest - $timestamp",
    "",
    "- Apply requested: ``$([bool]$Apply)``",
    "- Mod name: ``$ModName``",
    "- Target game version: ``$GameVersion``",
    "- Default load order: ``$DefaultLoadOrder``",
    "- Backup dir: ``$backupDir``",
    "",
    "## Changes",
    ""
)

foreach ($change in $changes) {
    $lines += "- $($change.kind): ``$($change.status)`` - ``$($change.path)``"
    if ($change.before -and $change.after) {
        $lines += "  - Manifest count: ``$($change.before.manifestCount)`` -> ``$($change.after.manifestCount)``"
        $lines += "  - TKU cluster entries: ``$($change.before.clusterManifestCount)`` -> ``$($change.after.clusterManifestCount)``"
        $lines += "  - Active career source entries: ``$($change.before.activeCareerSourceManifestCount)`` -> ``$($change.after.activeCareerSourceManifestCount)``"
        $lines += "  - Active cluster diagnostic entries: ``$($change.before.activeClusterDiagnosticManifestCount)`` -> ``$($change.after.activeClusterDiagnosticManifestCount)``"
        $lines += "  - Added entries: ``$(@($change.addedManifestEntries).Count)``"
    }
}

$lines += ""
$lines += "## Required Cluster Assets"
$lines += ""
foreach ($entry in $clusterManifestAssets) {
    $lines += "- ``$entry``"
}

$lines += ""
$lines += "## Required Active Career Source Assets"
$lines += ""
foreach ($entry in $activeCareerSourceManifestAssets) {
    $lines += "- ``$entry``"
}

$lines += ""
$lines += "## Required Active Cluster Diagnostic Assets"
$lines += ""
foreach ($entry in $activeClusterDiagnosticManifestAssets) {
    $lines += "- ``$entry``"
}

$lines | Set-Content -LiteralPath $reportMdPath -Encoding UTF8

Write-Host "Wrote $reportPath"
Write-Host "Wrote $reportMdPath"
