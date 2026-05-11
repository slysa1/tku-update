param(
    [switch]$Apply,
    [string]$ModName = 'TKUCompatEditorPatch',
    [string]$GameVersion = '1.13.378',
    [string]$Description = 'Editor-authored compatibility patch for Known Universe on MW5 1.13.x / DLC7 (Steam/GOG 1.13.378)',
    [switch]$IncludeEditorPlugin,
    [switch]$ForceEditorPlugin
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
    $json = $Value | ConvertTo-Json -Depth 20
    Set-Content -LiteralPath $Path -Value $json -Encoding UTF8
}

function Add-Change {
    param(
        [string]$Kind,
        [string]$Path,
        [object]$Before,
        [object]$After,
        [string]$Status
    )
    $script:changes += [ordered]@{
        kind = $Kind
        path = $Path
        before = $Before
        after = $After
        status = $Status
    }
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
$timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$reportDir = Join-Path $projectRoot 'reports\tku_editor_first'
$reportPath = Join-Path $reportDir "tku_version_metadata_$timestamp.json"
$reportMdPath = Join-Path $reportDir "tku_version_metadata_$timestamp.md"
$backupDir = Join-Path $reportDir "backups\version_metadata_$timestamp"
$changes = @()

$targets = @(
    @{
        kind = 'editor packaged mod.json'
        path = Join-Path $editorRoot "MW5Mercs\Mods\$ModName\mod.json"
    },
    @{
        kind = 'live deployed mod.json'
        path = Join-Path $liveModsRoot "$ModName\mod.json"
    }
)

foreach ($target in $targets) {
    $path = $target.path
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        Add-Change -Kind $target.kind -Path $path -Before $null -After $null -Status 'missing'
        continue
    }

    $json = Get-Content -LiteralPath $path -Raw | ConvertFrom-Json
    $before = [ordered]@{
        description = $json.description
        gameVersion = $json.gameVersion
    }
    $json.description = $Description
    $json.gameVersion = $GameVersion
    $after = [ordered]@{
        description = $json.description
        gameVersion = $json.gameVersion
    }

    if ($Apply) {
        New-Item -ItemType Directory -Force -Path $backupDir | Out-Null
        Copy-Item -LiteralPath $path -Destination (Join-Path $backupDir (Get-SafeBackupName -Kind $target.kind -Suffix 'mod.json'))
        Save-JsonFile -Value $json -Path $path
    }
    Add-Change -Kind $target.kind -Path $path -Before $before -After $after -Status $(if ($Apply) { 'updated' } else { 'planned' })
}

$liveModlist = Join-Path $liveModsRoot 'modlist.json'
if (Test-Path -LiteralPath $liveModlist -PathType Leaf) {
    $json = Get-Content -LiteralPath $liveModlist -Raw | ConvertFrom-Json
    $before = [ordered]@{ gameVersion = $json.gameVersion }
    $json.gameVersion = $GameVersion
    $after = [ordered]@{ gameVersion = $json.gameVersion }
    if ($Apply) {
        New-Item -ItemType Directory -Force -Path $backupDir | Out-Null
        Copy-Item -LiteralPath $liveModlist -Destination (Join-Path $backupDir 'live.modlist.json')
        Save-JsonFile -Value $json -Path $liveModlist
    }
    Add-Change -Kind 'live modlist' -Path $liveModlist -Before $before -After $after -Status $(if ($Apply) { 'updated' } else { 'planned' })
} else {
    Add-Change -Kind 'live modlist' -Path $liveModlist -Before $null -After $null -Status 'missing'
}

$editorPlugin = Join-Path $editorRoot "MW5Mercs\Plugins\$ModName\$ModName.uplugin"
if ($IncludeEditorPlugin) {
    $editorRunning = @(Get-Process | Where-Object { $_.ProcessName -eq 'UE4Editor' }).Count -gt 0
    if ($editorRunning -and -not $ForceEditorPlugin) {
        Add-Change -Kind 'editor plugin descriptor' -Path $editorPlugin -Before $null -After $null -Status 'skipped: UE4Editor is running'
    } elseif (Test-Path -LiteralPath $editorPlugin -PathType Leaf) {
        $json = Get-Content -LiteralPath $editorPlugin -Raw | ConvertFrom-Json
        $before = [ordered]@{ Description = $json.Description }
        $json.Description = $Description
        $after = [ordered]@{ Description = $json.Description }
        if ($Apply) {
            New-Item -ItemType Directory -Force -Path $backupDir | Out-Null
            Copy-Item -LiteralPath $editorPlugin -Destination (Join-Path $backupDir "$ModName.uplugin")
            Save-JsonFile -Value $json -Path $editorPlugin
        }
        Add-Change -Kind 'editor plugin descriptor' -Path $editorPlugin -Before $before -After $after -Status $(if ($Apply) { 'updated' } else { 'planned' })
    } else {
        Add-Change -Kind 'editor plugin descriptor' -Path $editorPlugin -Before $null -After $null -Status 'missing'
    }
}

$report = [ordered]@{
    generated = (Get-Date).ToString('o')
    apply_requested = [bool]$Apply
    mod_name = $ModName
    target_game_version = $GameVersion
    target_description = $Description
    backup_dir = $(if ($Apply) { $backupDir } else { $null })
    changes = $changes
}

New-Item -ItemType Directory -Force -Path $reportDir | Out-Null
$report | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $reportPath -Encoding UTF8

$lines = @(
    "# TKU Version Metadata - $timestamp",
    "",
    "- Apply requested: ``$([bool]$Apply)``",
    "- Mod name: ``$ModName``",
    "- Target game version: ``$GameVersion``",
    "- Target description: ``$Description``",
    "- Backup dir: ``$backupDir``",
    "",
    "## Changes",
    ""
)
foreach ($change in $changes) {
    $lines += "- $($change.kind): ``$($change.status)`` - ``$($change.path)``"
}
$lines | Set-Content -LiteralPath $reportMdPath -Encoding UTF8

Write-Host "Wrote $reportPath"
Write-Host "Wrote $reportMdPath"
