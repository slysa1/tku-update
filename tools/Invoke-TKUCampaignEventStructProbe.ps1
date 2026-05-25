param(
    [string]$ModName = 'TKUCompatEditorPatch'
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

function Set-TemporaryEnv {
    param(
        [hashtable]$Previous,
        [string]$Name,
        [string]$Value
    )

    if (-not $Previous.ContainsKey($Name)) {
        $Previous[$Name] = [Environment]::GetEnvironmentVariable($Name, 'Process')
    }
    [Environment]::SetEnvironmentVariable($Name, $Value, 'Process')
}

$projectRoot = Split-Path -Parent $PSScriptRoot
$pathConfig = Get-TkuPathConfig
$editorRoot = if ($env:TKU_MW5_EDITOR_ROOT) { $env:TKU_MW5_EDITOR_ROOT } else { $pathConfig.mw5_editor_root }
$cmdPath = Join-Path $editorRoot 'Engine\Binaries\Win64\UE4Editor-Cmd.exe'
$projectPath = Join-Path $editorRoot 'MW5Mercs\MW5Mercs.uproject'
$scriptPath = Join-Path $PSScriptRoot 'tku_reference_audit\ue4_probe_campaign_event_structs.py'

if (-not (Test-Path -LiteralPath $cmdPath)) {
    throw "UE4Editor-Cmd.exe not found: $cmdPath"
}
if (-not (Test-Path -LiteralPath $projectPath)) {
    throw "MW5 editor project not found: $projectPath"
}
if (-not (Test-Path -LiteralPath $scriptPath)) {
    throw "Campaign event struct probe script not found: $scriptPath"
}

$previousEnv = @{}
try {
    Set-TemporaryEnv -Previous $previousEnv -Name 'TKU_PROJECT_ROOT' -Value $projectRoot
    Set-TemporaryEnv -Previous $previousEnv -Name 'TKU_EVENT_STRUCT_MOD_NAME' -Value $ModName

    $scriptForPython = ($scriptPath -replace '\\', '/')
    $scriptArg = "-script=exec(compile(__import__('pathlib').Path('$scriptForPython').read_text(encoding='utf-8'), '$scriptForPython', 'exec'))"
    $arguments = @(
        $projectPath,
        '-run=pythonscript',
        $scriptArg,
        "-DLCName=$ModName",
        '-DLCSubstitutionsContentPath=ModOverride',
        '-basedonreleaseversion=1.0',
        '-unattended',
        '-nop4',
        '-nosplash'
    )

    Write-Host "Launching MW5 Mod Editor campaign event struct probe..."
    Write-Host "  EXE   : $cmdPath"
    Write-Host "  UPROJ : $projectPath"
    Write-Host "  SCRIPT: $scriptPath"
    Write-Host "  MOD   : $ModName"

    & $cmdPath @arguments
    exit $LASTEXITCODE
} finally {
    foreach ($name in $previousEnv.Keys) {
        [Environment]::SetEnvironmentVariable($name, $previousEnv[$name], 'Process')
    }
}
