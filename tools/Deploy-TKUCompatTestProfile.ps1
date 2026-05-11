param(
    [switch]$Apply,
    [string]$ModName = 'TKUCompatEditorPatch',
    [string]$BaselineModName = 'TKUEvidenceCorePluginOnly',
    [int]$LoadOrder = 95,
    [string]$GameVersion = '1.13.378',
    [string]$SourcePackageDir = '',
    [string]$LiveModsRoot = ''
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

function Get-FileSha256 {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        return $null
    }
    return (Get-FileHash -Algorithm SHA256 -LiteralPath $Path).Hash
}

function Save-JsonFile {
    param(
        [object]$Value,
        [string]$Path
    )
    $json = $Value | ConvertTo-Json -Depth 20
    Set-Content -LiteralPath $Path -Value $json -Encoding UTF8
}

$projectRoot = Split-Path -Parent $PSScriptRoot
$pathConfig = Get-TkuPathConfig -ProjectRoot $projectRoot
$editorRoot = if ($env:TKU_MW5_EDITOR_ROOT) { $env:TKU_MW5_EDITOR_ROOT } else { $pathConfig.mw5_editor_root }
if (-not $SourcePackageDir) {
    $SourcePackageDir = Join-Path $editorRoot "MW5Mercs\Mods\$ModName"
}
if (-not $LiveModsRoot) {
    $LiveModsRoot = $pathConfig.local_mods_root
}

$timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$reportDir = Join-Path $projectRoot 'reports\tku_editor_first'
$reportPath = Join-Path $reportDir "tkucompat_live_test_deploy_$timestamp.json"
$reportMdPath = Join-Path $reportDir "tkucompat_live_test_deploy_$timestamp.md"
$liveModlist = Join-Path $LiveModsRoot 'modlist.json'
$liveBackup = Join-Path $LiveModsRoot "modlist.backup-before-$ModName-$timestamp.json"
$repoBackup = Join-Path $reportDir "modlist.backup-before-$ModName-$timestamp.json"
$profilePath = Join-Path $LiveModsRoot "modlist.profile-$ModName-corepatch-$timestamp.json"
$destModDir = Join-Path $LiveModsRoot $ModName
$destModJson = Join-Path $destModDir 'mod.json'
$baselineModDir = Join-Path $LiveModsRoot $BaselineModName

$sourceExists = Test-Path -LiteralPath $SourcePackageDir -PathType Container
$destExistsBefore = Test-Path -LiteralPath $destModDir
$liveModlistExists = Test-Path -LiteralPath $liveModlist -PathType Leaf
$baselineExists = Test-Path -LiteralPath $baselineModDir -PathType Container

$safetyFailures = @()
if (-not $sourceExists) {
    $safetyFailures += "source packaged mod folder missing: $SourcePackageDir"
}
if (-not $liveModlistExists) {
    $safetyFailures += "live modlist missing: $liveModlist"
}
if (-not $baselineExists) {
    $safetyFailures += "baseline mod folder missing: $baselineModDir"
}
if ($destExistsBefore) {
    $safetyFailures += "destination mod folder already exists; refusing to overwrite: $destModDir"
}

$currentModlist = $null
$gameVersion = $GameVersion
$gameVersionSource = 'parameter/default'
if ([string]::IsNullOrWhiteSpace($gameVersion)) {
    $gameVersion = '1.13.378'
    $gameVersionSource = 'fallback'
}
if ($liveModlistExists) {
    $currentModlist = Get-Content -LiteralPath $liveModlist -Raw | ConvertFrom-Json
    if (-not $PSBoundParameters.ContainsKey('GameVersion') -and $currentModlist.gameVersion -and [string]$currentModlist.gameVersion -eq $gameVersion) {
        $gameVersion = [string]$currentModlist.gameVersion
        $gameVersionSource = 'live modlist'
    }
}

$report = [ordered]@{
    generated = (Get-Date).ToString('o')
    apply_requested = [bool]$Apply
    mod_name = $ModName
    baseline_mod_name = $BaselineModName
    source_package_dir = $SourcePackageDir
    live_mods_root = $LiveModsRoot
    destination_mod_dir = $destModDir
    load_order = $LoadOrder
    game_version = $gameVersion
    game_version_source = $gameVersionSource
    live_modlist = $liveModlist
    live_modlist_backup = $liveBackup
    repo_modlist_backup = $repoBackup
    profile_path = $profilePath
    safety_failures = $safetyFailures
    actions = @()
    hashes = [ordered]@{}
}

if ($safetyFailures.Count -eq 0 -and $Apply) {
    New-Item -ItemType Directory -Force -Path $reportDir | Out-Null
    Copy-Item -LiteralPath $liveModlist -Destination $liveBackup
    Copy-Item -LiteralPath $liveModlist -Destination $repoBackup
    $report.actions += "backed up live modlist to $liveBackup"
    $report.actions += "backed up live modlist to $repoBackup"

    Copy-Item -LiteralPath $SourcePackageDir -Destination $destModDir -Recurse
    $report.actions += "copied packaged mod to $destModDir"

    $modJson = Get-Content -LiteralPath $destModJson -Raw | ConvertFrom-Json
    $modJson.defaultLoadOrder = $LoadOrder
    $modJson.gameVersion = $gameVersion
    Save-JsonFile -Value $modJson -Path $destModJson
    $report.actions += "updated deployed $ModName mod.json defaultLoadOrder=$LoadOrder gameVersion=$gameVersion"

    $testModlist = [ordered]@{
        gameVersion = $gameVersion
        modStatus = [ordered]@{
            $BaselineModName = @{ bEnabled = $true }
            $ModName = @{ bEnabled = $true }
        }
    }
    Save-JsonFile -Value $testModlist -Path $profilePath
    Save-JsonFile -Value $testModlist -Path $liveModlist
    $report.actions += "wrote isolated test profile $profilePath"
    $report.actions += "activated isolated test profile in $liveModlist"
}

if (Test-Path -LiteralPath $destModDir -PathType Container) {
    $report.hashes.deployed_mod_json = Get-FileSha256 -Path $destModJson
    $pakPath = Join-Path $destModDir "Paks\$ModName.pak"
    $report.hashes.deployed_pak = Get-FileSha256 -Path $pakPath
}
$report.hashes.source_mod_json = Get-FileSha256 -Path (Join-Path $SourcePackageDir 'mod.json')
$report.hashes.source_pak = Get-FileSha256 -Path (Join-Path $SourcePackageDir "Paks\$ModName.pak")
$report.hashes.live_modlist = Get-FileSha256 -Path $liveModlist

New-Item -ItemType Directory -Force -Path $reportDir | Out-Null
$report | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $reportPath -Encoding UTF8

$lines = @(
    "# TKU Compat Live Test Deploy - $timestamp",
    "",
    "- Apply requested: ``$([bool]$Apply)``",
    "- Source package: ``$SourcePackageDir``",
    "- Destination mod: ``$destModDir``",
    "- Baseline mod: ``$BaselineModName``",
    "- Load order: ``$LoadOrder``",
    "- Game version: ``$gameVersion``",
    "- Game version source: ``$gameVersionSource``",
    "- Live modlist backup: ``$liveBackup``",
    "- Repo modlist backup: ``$repoBackup``",
    "- Test profile: ``$profilePath``",
    "",
    "## Safety",
    ""
)
if ($safetyFailures.Count) {
    foreach ($failure in $safetyFailures) {
        $lines += "- FAIL: $failure"
    }
} else {
    $lines += "- No safety failures."
}
$lines += ""
$lines += "## Actions"
$lines += ""
if ($report.actions.Count) {
    foreach ($action in $report.actions) {
        $lines += "- $action"
    }
} else {
    $lines += "- Dry run only; no live files changed."
}
$lines += ""
$lines += "## Hashes"
$lines += ""
foreach ($key in $report.hashes.Keys) {
    $lines += "- ${key}: ``$($report.hashes[$key])``"
}
$lines += ""
$lines += "## Rollback"
$lines += ""
$lines += "To restore the previous live modlist, copy ``$liveBackup`` back to ``$liveModlist``."
$lines | Set-Content -LiteralPath $reportMdPath -Encoding UTF8

Write-Host "Wrote $reportPath"
Write-Host "Wrote $reportMdPath"
if ($safetyFailures.Count) {
    exit 1
}
