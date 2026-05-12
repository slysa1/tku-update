param(
    [switch]$Apply,
    [string]$SourcePak = '',
    [string]$StagedPak = '',
    [string]$LivePak = ''
)

$ErrorActionPreference = 'Stop'

$projectRoot = Split-Path -Parent $PSScriptRoot
$script = Join-Path $projectRoot 'tools\tku_reference_audit\build_tku_content_mirror.py'
$argsList = @($script)
if ($Apply) {
    $argsList += '--apply'
}
if ($SourcePak) {
    $argsList += @('--source-pak', $SourcePak)
}
if ($StagedPak) {
    $argsList += @('--staged-pak', $StagedPak)
}
if ($LivePak) {
    $argsList += @('--live-pak', $LivePak)
}

python @argsList
