# ============================================================
# Cursor Config Auto-Sync
# Called by Windows Scheduled Task. Never prompts; never hangs.
# ============================================================

$ErrorActionPreference = 'Continue'
$repo    = "$env:USERPROFILE\.cursor"
$logFile = Join-Path $repo '.sync.log'

# Hard-disable any interactive prompt git might attempt under a
# non-interactive session (Scheduled Task with -WindowStyle Hidden).
$env:GIT_TERMINAL_PROMPT = '0'
$env:GCM_INTERACTIVE     = 'never'

function Write-Log {
    param([string]$Message, [string]$Level = 'INFO')
    $ts = Get-Date -Format 'yyyy-MM-dd HH:mm:ss'
    "[$ts] [$Level] $Message" | Out-File -Append -Encoding utf8 $logFile
}

function Trim-Log {
    if (-not (Test-Path $logFile)) { return }
    $lines = Get-Content $logFile -Encoding utf8
    if ($lines.Count -gt 1000) {
        $lines[-800..-1] | Set-Content $logFile -Encoding utf8
    }
}

try {
    Set-Location $repo

    $status = git status --porcelain 2>&1
    $hasLocalChanges = $false
    if ($LASTEXITCODE -ne 0) {
        Write-Log "git status failed: $status" 'ERROR'
        return
    }
    if ($status) { $hasLocalChanges = $true }

    if ($hasLocalChanges) {
        $fileCount = ($status | Measure-Object).Count
        $timestamp = Get-Date -Format 'yyyy-MM-dd HH:mm'

        $addOutput = git add -A 2>&1
        if ($LASTEXITCODE -ne 0) {
            Write-Log "git add failed: $addOutput" 'ERROR'
            return
        }

        $commitOutput = git commit -m "auto-sync: $timestamp ($fileCount files)" 2>&1
        if ($LASTEXITCODE -ne 0) {
            Write-Log "git commit failed: $commitOutput" 'ERROR'
            return
        }
        Write-Log "committed $fileCount changed file(s)"
    }

    $unpushed = git log 'origin/main..HEAD' --oneline 2>&1
    if ($LASTEXITCODE -ne 0) {
        Write-Log "git log origin/main..HEAD failed: $unpushed" 'ERROR'
        return
    }

    if ($unpushed) {
        Write-Log "push start: $(($unpushed | Measure-Object).Count) commit(s) ahead of origin"
        $pushOutput = git push origin main 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Log "push success"
        } else {
            $oneLine = ($pushOutput -join ' | ').Substring(0, [Math]::Min(400, ($pushOutput -join ' | ').Length))
            Write-Log "push failed (exit $LASTEXITCODE): $oneLine" 'ERROR'
        }
    }

    Trim-Log
} catch {
    Write-Log "exception: $_" 'ERROR'
}
