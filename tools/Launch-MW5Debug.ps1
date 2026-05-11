param(
    [bool]$Wait = $true,
    [switch]$KeepConfigPatch
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
$exePath = Join-Path $gameRoot 'MW5Mercs\Binaries\Win64\MechWarrior-Win64-Shipping.exe'
$savedRoot = Join-Path $env:LOCALAPPDATA 'MW5Mercs\Saved'
$configDir = Join-Path $savedRoot 'Config\WindowsNoEditor'
$logDir = Join-Path $savedRoot 'Logs'
$engineIni = Join-Path $configDir 'Engine.ini'
$backupIni = "$engineIni.codex-debug.bak"
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$logFile = Join-Path $logDir "MW5Mercs-debug-$stamp.log"
$stdoutFile = Join-Path $logDir "MW5Mercs-stdout-$stamp.log"
$stderrFile = Join-Path $logDir "MW5Mercs-stderr-$stamp.log"

if (-not (Test-Path $exePath)) {
    throw "MW5 executable not found: $exePath"
}

New-Item -ItemType Directory -Force -Path $configDir | Out-Null
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

$debugBlock = @'
; BEGIN CODEX DEBUG LOGGING
[Core.Log]
Global=Log
LogConfig=Verbose
LogStreaming=Verbose
LogLoad=Verbose
LogLinker=Verbose
LogUObjectGlobals=Verbose
LogBlueprint=Verbose
LogSpawn=Verbose
LogPakFile=Verbose
LogRHI=Verbose
LogD3D11RHI=Verbose
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

Write-Host "Launching MW5 with debug logging enabled..."
Write-Host "  EXE : $exePath"
Write-Host "  LOG : $logFile"
Write-Host "  OUT : $stdoutFile"
Write-Host "  ERR : $stderrFile"
Write-Host "  INI : $engineIni"

$proc = $null
try {
    $proc = Start-Process `
        -FilePath $exePath `
        -ArgumentList $args `
        -WorkingDirectory (Split-Path -Parent $exePath) `
        -RedirectStandardOutput $stdoutFile `
        -RedirectStandardError $stderrFile `
        -PassThru
    if ($Wait) {
        Wait-Process -Id $proc.Id
    }
} finally {
    if (-not $KeepConfigPatch) {
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
}

if (Test-Path $logFile) {
    Write-Host ''
    Write-Host 'Last 40 log lines:'
    Get-Content $logFile -Tail 40
} else {
    Write-Warning "No log file was created at $logFile"
}

if (Test-Path $stdoutFile) {
    $stdoutInfo = Get-Item $stdoutFile
    if ($stdoutInfo.Length -gt 0) {
        Write-Host ''
        Write-Host 'Last 40 stdout lines:'
        Get-Content $stdoutFile -Tail 40
    } else {
        Write-Warning "Stdout capture file is empty: $stdoutFile"
    }
}

if (Test-Path $stderrFile) {
    $stderrInfo = Get-Item $stderrFile
    if ($stderrInfo.Length -gt 0) {
        Write-Host ''
        Write-Host 'Last 40 stderr lines:'
        Get-Content $stderrFile -Tail 40
    }
}
