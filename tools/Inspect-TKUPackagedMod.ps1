param(
    [string]$ModName = 'TKUCompatEditorPatch',
    [string]$PackageRoot = '',
    [string]$ModDir = '',
    [string]$UnrealPak = ''
)

$ErrorActionPreference = 'Stop'

$projectRoot = Split-Path -Parent $PSScriptRoot
$scriptPath = Join-Path $PSScriptRoot 'tku_reference_audit\inspect_tku_packaged_mod.py'

if (-not (Test-Path -LiteralPath $scriptPath)) {
    throw "Packaged mod inspection script not found: $scriptPath"
}

$arguments = @($scriptPath, '--mod-name', $ModName)
if ($PackageRoot) {
    $arguments += @('--package-root', $PackageRoot)
}
if ($ModDir) {
    $arguments += @('--mod-dir', $ModDir)
}
if ($UnrealPak) {
    $arguments += @('--unrealpak', $UnrealPak)
}

$previousProjectRoot = [Environment]::GetEnvironmentVariable('TKU_PROJECT_ROOT', 'Process')
try {
    [Environment]::SetEnvironmentVariable('TKU_PROJECT_ROOT', $projectRoot, 'Process')
    python @arguments
    exit $LASTEXITCODE
} finally {
    [Environment]::SetEnvironmentVariable('TKU_PROJECT_ROOT', $previousProjectRoot, 'Process')
}
