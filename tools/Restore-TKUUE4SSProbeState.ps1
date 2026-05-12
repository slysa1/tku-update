param(
    [switch]$Apply,
    [string]$ProbeName = 'TKURuntimeProbe',
    [string]$SettingsBackup = 'reports\tku_editor_first\backups\ue4ss_probe_state_20260512-080610\UE4SS-settings.ini',
    [string]$Win64Root = ''
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

$projectRoot = Split-Path -Parent $PSScriptRoot
$pathConfig = Get-TkuPathConfig -ProjectRoot $projectRoot
if (-not $Win64Root) {
    $Win64Root = if ($pathConfig.ue4ss_win64_root) {
        $pathConfig.ue4ss_win64_root
    } else {
        Join-Path $pathConfig.game_root 'MW5Mercs\Binaries\Win64'
    }
}

if (-not [System.IO.Path]::IsPathRooted($SettingsBackup)) {
    $SettingsBackup = Join-Path $projectRoot $SettingsBackup
}

$timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$reportDir = Join-Path $projectRoot 'reports\tku_editor_first'
$backupDir = Join-Path $reportDir "backups\ue4ss_probe_restore_$timestamp"
$settingsPath = Join-Path $Win64Root 'UE4SS-settings.ini'
$modsTxt = Join-Path $Win64Root 'Mods\mods.txt'
$reportPath = Join-Path $reportDir "ue4ss_probe_restore_$timestamp.json"
$reportMdPath = Join-Path $reportDir "ue4ss_probe_restore_$timestamp.md"

$runningProcesses = @(Get-Process | Where-Object { $_.ProcessName -like 'MechWarrior*' })
$safetyFailures = @()
if ($runningProcesses.Count -gt 0) {
    $safetyFailures += "MW5 is still running; close the game before restoring UE4SS settings."
}
if (-not (Test-Path -LiteralPath $settingsPath -PathType Leaf)) {
    $safetyFailures += "UE4SS settings file missing: $settingsPath"
}
if (-not (Test-Path -LiteralPath $SettingsBackup -PathType Leaf)) {
    $safetyFailures += "settings backup missing: $SettingsBackup"
}
if (-not (Test-Path -LiteralPath $modsTxt -PathType Leaf)) {
    $safetyFailures += "UE4SS mods.txt missing: $modsTxt"
}

$actions = @()
if ($safetyFailures.Count -eq 0 -and $Apply) {
    New-Item -ItemType Directory -Force -Path $backupDir | Out-Null
    Copy-Item -LiteralPath $settingsPath -Destination (Join-Path $backupDir 'UE4SS-settings.ini.before-restore')
    Copy-Item -LiteralPath $modsTxt -Destination (Join-Path $backupDir 'mods.txt.before-restore')

    Copy-Item -LiteralPath $SettingsBackup -Destination $settingsPath -Force
    $actions += "restored UE4SS settings from $SettingsBackup"

    $modsText = Get-Content -LiteralPath $modsTxt -Raw
    $pattern = "(?m)^$([regex]::Escape($ProbeName))\s*:\s*\d+\s*$"
    if ($modsText -match $pattern) {
        $modsText = [regex]::Replace($modsText, $pattern, "$ProbeName : 0")
        Set-Content -LiteralPath $modsTxt -Value $modsText -Encoding ASCII
        $actions += "disabled $ProbeName in $modsTxt"
    } else {
        $actions += "$ProbeName entry not present in $modsTxt"
    }
}

$report = [ordered]@{
    generated = (Get-Date).ToString('o')
    apply_requested = [bool]$Apply
    probe_name = $ProbeName
    win64_root = $Win64Root
    settings_path = $settingsPath
    settings_backup = $SettingsBackup
    mods_txt = $modsTxt
    backup_dir = $(if ($Apply) { $backupDir } else { $null })
    safety_failures = $safetyFailures
    actions = $actions
}

New-Item -ItemType Directory -Force -Path $reportDir | Out-Null
$report | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $reportPath -Encoding UTF8

$lines = @(
    "# UE4SS TKU Probe Restore - $timestamp",
    "",
    "- Apply requested: ``$([bool]$Apply)``",
    "- Probe: ``$ProbeName``",
    "- Settings backup: ``$SettingsBackup``",
    "- Settings target: ``$settingsPath``",
    "- mods.txt: ``$modsTxt``",
    "- Backup dir: ``$backupDir``",
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
if ($actions.Count) {
    foreach ($action in $actions) {
        $lines += "- $action"
    }
} else {
    $lines += "- Dry run only; no UE4SS files changed."
}
$lines | Set-Content -LiteralPath $reportMdPath -Encoding UTF8

Write-Host "Wrote $reportPath"
Write-Host "Wrote $reportMdPath"
if ($safetyFailures.Count) {
    exit 1
}
