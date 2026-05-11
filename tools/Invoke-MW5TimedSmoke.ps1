param(
    [Parameter(Mandatory = $true)]
    [string]$Profile,
    [int]$RuntimeSeconds = 90
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
$setProfileScript = Join-Path $PSScriptRoot 'Set-MW5ModProfile.ps1'
$exePath = Join-Path $gameRoot 'MW5Mercs\Binaries\Win64\MechWarrior-Win64-Shipping.exe'
$savedRoot = Join-Path $env:LOCALAPPDATA 'MW5Mercs\Saved'
$configDir = Join-Path $savedRoot 'Config\WindowsNoEditor'
$logDir = Join-Path $savedRoot 'Logs'
$engineIni = Join-Path $configDir 'Engine.ini'
$backupIni = "$engineIni.codex-debug.bak"
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$logFile = Join-Path $logDir "MW5Mercs-smoke-$stamp.log"
$stdoutFile = Join-Path $logDir "MW5Mercs-smoke-stdout-$stamp.log"
$stderrFile = Join-Path $logDir "MW5Mercs-smoke-stderr-$stamp.log"
$crashRoot = Join-Path $savedRoot 'Crashes'
$beforeCrashDirs = @()
if (Test-Path $crashRoot) {
    $beforeCrashDirs = @(Get-ChildItem -LiteralPath $crashRoot -Directory | Select-Object -ExpandProperty Name)
}

if (-not (Test-Path $exePath)) {
    throw "MW5 executable not found: $exePath"
}

& $setProfileScript -Profile $Profile

New-Item -ItemType Directory -Force -Path $configDir | Out-Null
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

$debugBlock = @'
; BEGIN CODEX DEBUG LOGGING
[Core.Log]
Global=Log
LogConfig=Verbose
LogPakFile=Verbose
LogLoad=Verbose
LogStreaming=Verbose
LogLinker=Verbose
LogUObjectGlobals=Verbose
; END CODEX DEBUG LOGGING
'@

$originalEngineIni = ''
if (Test-Path $engineIni) {
    $originalEngineIni = Get-Content $engineIni -Raw
    Set-Content -Path $backupIni -Value $originalEngineIni -NoNewline
}

if ($originalEngineIni -notmatch 'BEGIN CODEX DEBUG LOGGING') {
    $patched = if ([string]::IsNullOrWhiteSpace($originalEngineIni)) {
        $debugBlock
    } else {
        ($originalEngineIni.TrimEnd() + "`r`n`r`n" + $debugBlock)
    }
    Set-Content -Path $engineIni -Value $patched -NoNewline
}

$args = @(
    'MW5Mercs',
    '-log',
    '-stdout',
    '-fileopenlog',
    '-forcelogflush',
    "-ABSLOG=$logFile"
)

$proc = $null
try {
    $proc = Start-Process `
        -FilePath $exePath `
        -ArgumentList $args `
        -WorkingDirectory (Split-Path -Parent $exePath) `
        -RedirectStandardOutput $stdoutFile `
        -RedirectStandardError $stderrFile `
        -PassThru

    Start-Sleep -Seconds $RuntimeSeconds

    if (-not $proc.HasExited) {
        Stop-Process -Id $proc.Id -Force
        $proc.WaitForExit()
    }
} finally {
    if (Test-Path $backupIni) {
        Move-Item -LiteralPath $backupIni -Destination $engineIni -Force
    } elseif (Test-Path $engineIni) {
        $current = Get-Content $engineIni -Raw
        $cleaned = [regex]::Replace(
            $current,
            '(?s)\r?\n?; BEGIN CODEX DEBUG LOGGING.*?; END CODEX DEBUG LOGGING\r?\n?',
            ''
        ).TrimEnd()
        if ($cleaned) {
            Set-Content -Path $engineIni -Value $cleaned -NoNewline
        } else {
            Remove-Item -LiteralPath $engineIni -Force
        }
    }
}

$afterCrashDirs = @()
if (Test-Path $crashRoot) {
    $afterCrashDirs = @(Get-ChildItem -LiteralPath $crashRoot -Directory | Select-Object -ExpandProperty Name)
}
$newCrashDirs = @($afterCrashDirs | Where-Object { $_ -notin $beforeCrashDirs })

Write-Host "Profile: $Profile"
Write-Host "RuntimeSeconds: $RuntimeSeconds"
Write-Host "LogFile: $logFile"
Write-Host "StdoutFile: $stdoutFile"
Write-Host "StderrFile: $stderrFile"
Write-Host "NewCrashDirs: $($newCrashDirs.Count)"
foreach ($dir in $newCrashDirs) {
    Write-Host "  $dir"
}

if (Test-Path $logFile) {
    Write-Host ''
    Write-Host 'Pak-related lines:'
    Select-String -LiteralPath $logFile -Pattern 'KnownUniverse','Pak','Mounted' | Select-Object -Last 80
}
