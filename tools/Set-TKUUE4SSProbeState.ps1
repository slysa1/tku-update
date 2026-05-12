param(
    [switch]$Apply,
    [ValidateSet('enabled', 'disabled')]
    [string]$ProbeState = 'enabled',
    [int]$EngineMajorVersion = 4,
    [int]$EngineMinorVersion = 27,
    [string]$ProbeName = 'TKURuntimeProbe',
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

function Set-IniValue {
    param(
        [string[]]$Lines,
        [string]$Section,
        [string]$Key,
        [string]$Value
    )
    $out = New-Object System.Collections.Generic.List[string]
    $inSection = $false
    $sectionSeen = $false
    $keySet = $false

    foreach ($line in $Lines) {
        if ($line -match '^\s*\[(.+?)\]\s*$') {
            if ($inSection -and -not $keySet) {
                $out.Add("$Key = $Value")
                $keySet = $true
            }
            $inSection = ($Matches[1] -eq $Section)
            if ($inSection) {
                $sectionSeen = $true
            }
            $out.Add($line)
            continue
        }

        if ($inSection -and $line -match "^\s*$([regex]::Escape($Key))\s*=") {
            $out.Add("$Key = $Value")
            $keySet = $true
        } else {
            $out.Add($line)
        }
    }

    if (-not $sectionSeen) {
        $out.Add("")
        $out.Add("[$Section]")
        $out.Add("$Key = $Value")
    } elseif ($inSection -and -not $keySet) {
        $out.Add("$Key = $Value")
    }

    return $out.ToArray()
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

$timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$reportDir = Join-Path $projectRoot 'reports\tku_editor_first'
$backupDir = Join-Path $reportDir "backups\ue4ss_probe_state_$timestamp"
$settingsPath = Join-Path $Win64Root 'UE4SS-settings.ini'
$modsTxt = Join-Path $Win64Root 'Mods\mods.txt'
$reportPath = Join-Path $reportDir "ue4ss_probe_state_$timestamp.json"
$reportMdPath = Join-Path $reportDir "ue4ss_probe_state_$timestamp.md"

$runningProcesses = @(Get-Process | Where-Object { $_.ProcessName -like 'MechWarrior*' })
$safetyFailures = @()
if ($runningProcesses.Count -gt 0) {
    $safetyFailures += "MW5 is still running; close the game before changing UE4SS settings."
}
if (-not (Test-Path -LiteralPath $settingsPath -PathType Leaf)) {
    $safetyFailures += "UE4SS settings file missing: $settingsPath"
}
if (-not (Test-Path -LiteralPath $modsTxt -PathType Leaf)) {
    $safetyFailures += "UE4SS mods.txt missing: $modsTxt"
}

$actions = @()
if ($safetyFailures.Count -eq 0 -and $Apply) {
    New-Item -ItemType Directory -Force -Path $backupDir | Out-Null
    Copy-Item -LiteralPath $settingsPath -Destination (Join-Path $backupDir 'UE4SS-settings.ini')
    Copy-Item -LiteralPath $modsTxt -Destination (Join-Path $backupDir 'mods.txt')

    $lines = Get-Content -LiteralPath $settingsPath
    $lines = Set-IniValue -Lines $lines -Section 'EngineVersionOverride' -Key 'MajorVersion' -Value ([string]$EngineMajorVersion)
    $lines = Set-IniValue -Lines $lines -Section 'EngineVersionOverride' -Key 'MinorVersion' -Value ([string]$EngineMinorVersion)
    Set-Content -LiteralPath $settingsPath -Value $lines -Encoding ASCII
    $actions += "set EngineVersionOverride to $EngineMajorVersion.$EngineMinorVersion in $settingsPath"

    $modsText = Get-Content -LiteralPath $modsTxt -Raw
    $enabledValue = if ($ProbeState -eq 'enabled') { '1' } else { '0' }
    $pattern = "(?m)^$([regex]::Escape($ProbeName))\s*:\s*\d+\s*$"
    if ($modsText -match $pattern) {
        $modsText = [regex]::Replace($modsText, $pattern, "$ProbeName : $enabledValue")
    } elseif ($ProbeState -eq 'enabled') {
        if (-not $modsText.EndsWith("`n")) {
            $modsText += "`r`n"
        }
        $modsText += "$ProbeName : 1`r`n"
    }
    Set-Content -LiteralPath $modsTxt -Value $modsText -Encoding ASCII
    $actions += "set $ProbeName to $ProbeState in $modsTxt"
}

$report = [ordered]@{
    generated = (Get-Date).ToString('o')
    apply_requested = [bool]$Apply
    probe_name = $ProbeName
    probe_state = $ProbeState
    engine_major_version = $EngineMajorVersion
    engine_minor_version = $EngineMinorVersion
    settings_path = $settingsPath
    mods_txt = $modsTxt
    backup_dir = $(if ($Apply) { $backupDir } else { $null })
    safety_failures = $safetyFailures
    actions = $actions
}

New-Item -ItemType Directory -Force -Path $reportDir | Out-Null
$report | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $reportPath -Encoding UTF8

$lines = @(
    "# UE4SS TKU Probe State - $timestamp",
    "",
    "- Apply requested: ``$([bool]$Apply)``",
    "- Probe: ``$ProbeName`` -> ``$ProbeState``",
    "- Engine override: ``$EngineMajorVersion.$EngineMinorVersion``",
    "- Settings: ``$settingsPath``",
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
