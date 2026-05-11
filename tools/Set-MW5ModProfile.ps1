param(
    [Parameter(Mandatory = $true)]
    [string]$Profile
)

$ErrorActionPreference = 'Stop'

$modsRoot = Join-Path (Split-Path -Parent $PSScriptRoot) 'MW5Mercs\Mods'
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
