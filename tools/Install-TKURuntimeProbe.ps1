param(
    [switch]$Apply,
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
$backupDir = Join-Path $reportDir "backups\ue4ss_runtime_probe_$timestamp"
$sourceLua = Join-Path $projectRoot 'tools\tku_reference_audit\ue4ss_tku_runtime_probe.lua'
$modsRoot = Join-Path $Win64Root 'Mods'
$modsTxt = Join-Path $modsRoot 'mods.txt'
$probeDir = Join-Path $modsRoot $ProbeName
$probeScriptsDir = Join-Path $probeDir 'Scripts'
$targetLua = Join-Path $probeScriptsDir 'main.lua'
$reportPath = Join-Path $reportDir "ue4ss_runtime_probe_install_$timestamp.json"
$reportMdPath = Join-Path $reportDir "ue4ss_runtime_probe_install_$timestamp.md"

$runningProcesses = @(Get-Process | Where-Object { $_.ProcessName -like 'MechWarrior*' })
$safetyFailures = @()
if ($runningProcesses.Count -gt 0) {
    $safetyFailures += "MW5 is still running; close the game before installing the UE4SS probe."
}
if (-not (Test-Path -LiteralPath $sourceLua -PathType Leaf)) {
    $safetyFailures += "source Lua probe missing: $sourceLua"
}
if (-not (Test-Path -LiteralPath $modsRoot -PathType Container)) {
    $safetyFailures += "UE4SS Mods folder missing: $modsRoot"
}
if (-not (Test-Path -LiteralPath $modsTxt -PathType Leaf)) {
    $safetyFailures += "UE4SS mods.txt missing: $modsTxt"
}

$actions = @()
if ($safetyFailures.Count -eq 0 -and $Apply) {
    New-Item -ItemType Directory -Force -Path $backupDir | Out-Null
    Copy-Item -LiteralPath $modsTxt -Destination (Join-Path $backupDir 'mods.txt')
    if (Test-Path -LiteralPath $probeDir) {
        Copy-Item -LiteralPath $probeDir -Destination (Join-Path $backupDir $ProbeName) -Recurse
    }
    New-Item -ItemType Directory -Force -Path $probeScriptsDir | Out-Null
    Copy-Item -LiteralPath $sourceLua -Destination $targetLua -Force
    $actions += "installed probe Lua to $targetLua"

    $modsText = Get-Content -LiteralPath $modsTxt -Raw
    $pattern = "(?m)^$([regex]::Escape($ProbeName))\s*:\s*\d+\s*$"
    if ($modsText -match $pattern) {
        $modsText = [regex]::Replace($modsText, $pattern, "$ProbeName : 1")
    } else {
        if (-not $modsText.EndsWith("`n")) {
            $modsText += "`r`n"
        }
        $modsText += "$ProbeName : 1`r`n"
    }
    Set-Content -LiteralPath $modsTxt -Value $modsText -Encoding ASCII
    $actions += "enabled $ProbeName in $modsTxt"
}

$report = [ordered]@{
    generated = (Get-Date).ToString('o')
    apply_requested = [bool]$Apply
    probe_name = $ProbeName
    win64_root = $Win64Root
    mods_root = $modsRoot
    target_lua = $targetLua
    mods_txt = $modsTxt
    backup_dir = $(if ($Apply) { $backupDir } else { $null })
    safety_failures = $safetyFailures
    actions = $actions
}

New-Item -ItemType Directory -Force -Path $reportDir | Out-Null
$report | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $reportPath -Encoding UTF8

$lines = @(
    "# UE4SS TKU Runtime Probe Install - $timestamp",
    "",
    "- Apply requested: ``$([bool]$Apply)``",
    "- Probe: ``$ProbeName``",
    "- Target Lua: ``$targetLua``",
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
