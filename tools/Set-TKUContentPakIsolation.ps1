param(
    [ValidateSet('Status', 'Isolate', 'Restore')]
    [string]$Mode = 'Status',
    [switch]$Apply
)

$ErrorActionPreference = 'Stop'

function Get-TkuPathConfig {
    $projectRoot = Split-Path -Parent $PSScriptRoot
    $configCandidates = @()
    if ($env:TKU_PATHS_CONFIG) {
        $configCandidates += $env:TKU_PATHS_CONFIG
    }
    $configCandidates += @(
        (Join-Path $projectRoot 'config\tku_paths.local.json'),
        (Join-Path $projectRoot 'config\tku_paths.json'),
        (Join-Path $projectRoot 'config\tku_paths.example.json')
    )

    foreach ($candidate in $configCandidates) {
        if (Test-Path -LiteralPath $candidate) {
            return Get-Content -LiteralPath $candidate -Raw | ConvertFrom-Json
        }
    }

    throw "No TKU path config found."
}

function Get-Sha256 {
    param([string]$Path)
    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        return $null
    }
    return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash
}

function Assert-UnderRoot {
    param(
        [string]$Root,
        [string]$Path
    )
    $resolvedRoot = [System.IO.Path]::GetFullPath($Root).TrimEnd('\') + '\'
    $resolvedPath = [System.IO.Path]::GetFullPath($Path)
    if (-not $resolvedPath.StartsWith($resolvedRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Refusing to operate outside content pak root: $Path"
    }
}

$projectRoot = Split-Path -Parent $PSScriptRoot
$pathConfig = Get-TkuPathConfig
$contentPaksRoot = $pathConfig.content_paks_root
$reportDir = Join-Path $projectRoot 'reports\tku_editor_first'
$timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$reportJson = Join-Path $reportDir "tku_content_pak_isolation_$timestamp.json"
$reportMd = Join-Path $reportDir "tku_content_pak_isolation_$timestamp.md"
$suffix = '.disabled-by-tku-isolation'

$targets = @(
    [pscustomobject]@{
        Name = 'MW5Mercs-zzzzTKUCompatEditorPatch.pak'
        Reason = 'Disable the ad hoc loose content mirror whose packaged assets still contain ModOverride internal paths.'
    },
    [pscustomobject]@{
        Name = 'MW5Mercs-zKnownUniverseStarmap.pak'
        Reason = 'Disable the legacy loose root override for a reversible mod-folder-only isolation test.'
    }
)

if (-not (Test-Path -LiteralPath $contentPaksRoot -PathType Container)) {
    throw "Content pak root not found: $contentPaksRoot"
}

New-Item -ItemType Directory -Path $reportDir -Force | Out-Null

$actions = @()
$safetyFailures = @()
$targetReports = @()

foreach ($target in $targets) {
    $activePath = Join-Path $contentPaksRoot $target.Name
    $disabledPath = "$activePath$suffix"
    Assert-UnderRoot -Root $contentPaksRoot -Path $activePath
    Assert-UnderRoot -Root $contentPaksRoot -Path $disabledPath

    $activeExists = Test-Path -LiteralPath $activePath -PathType Leaf
    $disabledExists = Test-Path -LiteralPath $disabledPath -PathType Leaf
    $targetReport = [ordered]@{
        name = $target.Name
        reason = $target.Reason
        active_path = $activePath
        disabled_path = $disabledPath
        active_exists_before = $activeExists
        disabled_exists_before = $disabledExists
        active_sha256_before = Get-Sha256 -Path $activePath
        disabled_sha256_before = Get-Sha256 -Path $disabledPath
    }

    if ($Mode -eq 'Isolate') {
        if ($activeExists -and $disabledExists) {
            $safetyFailures += "Both active and disabled files exist for $($target.Name); refusing to guess."
        } elseif ($activeExists) {
            if ($Apply) {
                Move-Item -LiteralPath $activePath -Destination $disabledPath
                $actions += "disabled $($target.Name)"
            } else {
                $actions += "would disable $($target.Name)"
            }
        } elseif ($disabledExists) {
            $actions += "$($target.Name) already disabled"
        } else {
            $actions += "$($target.Name) absent"
        }
    } elseif ($Mode -eq 'Restore') {
        if ($activeExists -and $disabledExists) {
            $safetyFailures += "Both active and disabled files exist for $($target.Name); refusing to guess."
        } elseif ($disabledExists) {
            if ($Apply) {
                Move-Item -LiteralPath $disabledPath -Destination $activePath
                $actions += "restored $($target.Name)"
            } else {
                $actions += "would restore $($target.Name)"
            }
        } elseif ($activeExists) {
            $actions += "$($target.Name) already active"
        } else {
            $actions += "$($target.Name) absent"
        }
    } else {
        $actions += "status checked for $($target.Name)"
    }

    $targetReport.active_exists_after = Test-Path -LiteralPath $activePath -PathType Leaf
    $targetReport.disabled_exists_after = Test-Path -LiteralPath $disabledPath -PathType Leaf
    $targetReport.active_sha256_after = Get-Sha256 -Path $activePath
    $targetReport.disabled_sha256_after = Get-Sha256 -Path $disabledPath
    $targetReports += $targetReport
}

$report = [ordered]@{
    timestamp = $timestamp
    generated_utc = (Get-Date).ToUniversalTime().ToString('o')
    mode = $Mode
    apply_requested = [bool]$Apply
    content_paks_root = $contentPaksRoot
    suffix = $suffix
    safety_failures = $safetyFailures
    actions = $actions
    targets = $targetReports
}

$report | ConvertTo-Json -Depth 8 | Set-Content -LiteralPath $reportJson -Encoding UTF8

$lines = @(
    "# TKU Content Pak Isolation - $timestamp",
    "",
    "- Mode: ``$Mode``",
    "- Apply requested: ``$([bool]$Apply)``",
    "- Safety: renames only; no pak contents are modified.",
    "- Restore command: ``.\tools\Set-TKUContentPakIsolation.ps1 -Mode Restore -Apply``",
    "",
    "## Actions"
)
foreach ($action in $actions) {
    $lines += "- $action"
}
if ($safetyFailures.Count -gt 0) {
    $lines += ""
    $lines += "## Safety Failures"
    foreach ($failure in $safetyFailures) {
        $lines += "- $failure"
    }
}
$lines += ""
$lines += "## Targets"
foreach ($targetReport in $targetReports) {
    $lines += "- ``$($targetReport.name)`` active before ``$($targetReport.active_exists_before)`` after ``$($targetReport.active_exists_after)`` disabled before ``$($targetReport.disabled_exists_before)`` after ``$($targetReport.disabled_exists_after)``"
}
$lines | Set-Content -LiteralPath $reportMd -Encoding UTF8

Write-Host $reportJson
Write-Host $reportMd

if ($safetyFailures.Count -gt 0) {
    exit 1
}
