param(
    [Parameter(Mandatory = $true)]
    [string]$Profile
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

    throw "No TKU path config found. Expected config\tku_paths.local.json or TKU_PATHS_CONFIG."
}

$pathConfig = Get-TkuPathConfig
$gameRoot = if ($env:TKU_GAME_ROOT) { $env:TKU_GAME_ROOT } else { $pathConfig.game_root }
$modsRoot = if ($env:TKU_LOCAL_MODS_ROOT) {
    $env:TKU_LOCAL_MODS_ROOT
} elseif ($pathConfig.local_mods_root) {
    $pathConfig.local_mods_root
} else {
    Join-Path $gameRoot 'MW5Mercs\Mods'
}
$activePath = Join-Path $modsRoot 'modlist.json'
$profilePath = if ([IO.Path]::IsPathRooted($Profile)) {
    $Profile
} else {
    Join-Path $modsRoot $Profile
}

if (-not (Test-Path $profilePath)) {
    throw "Profile not found: $profilePath"
}

Copy-Item -LiteralPath $profilePath -Destination $activePath -Force

$json = Get-Content $activePath -Raw | ConvertFrom-Json
$enabled = @($json.modStatus.PSObject.Properties | Where-Object { $_.Value.bEnabled -eq $true } | Select-Object -ExpandProperty Name)

Write-Host "Applied profile: $profilePath"
Write-Host "Enabled mods: $($enabled.Count)"
if ($enabled.Count -gt 0) {
    $enabled | ForEach-Object { Write-Host "  $_" }
}
