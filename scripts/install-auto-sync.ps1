# ============================================================
# One-time installer: registers auto-sync.ps1 as a Windows
# Scheduled Task that runs every 15 minutes under the current
# user. Does not require admin rights.
#
# Run:
#   powershell -NoProfile -ExecutionPolicy Bypass -File `
#     "$env:USERPROFILE\.cursor\scripts\install-auto-sync.ps1"
# Uninstall:
#   Unregister-ScheduledTask -TaskName CursorConfigAutoSync -Confirm:$false
# ============================================================

$taskName    = 'CursorConfigAutoSync'
$scriptPath  = Join-Path $env:USERPROFILE '.cursor\scripts\auto-sync.ps1'
$intervalMin = 120

if (-not (Test-Path $scriptPath)) {
    Write-Error "Sync script not found: $scriptPath"
    exit 1
}

$existing = Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
if ($existing) {
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
    Write-Host "Removed existing task $taskName, re-registering..."
}

$action = New-ScheduledTaskAction `
    -Execute 'powershell.exe' `
    -Argument "-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$scriptPath`""

$triggerTime = New-ScheduledTaskTrigger `
    -Once -At (Get-Date).AddSeconds(30) `
    -RepetitionInterval (New-TimeSpan -Minutes $intervalMin) `
    -RepetitionDuration ([TimeSpan]::FromDays(3650))

$triggerLogon = New-ScheduledTaskTrigger -AtLogOn

$trigger = @($triggerTime, $triggerLogon)

$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -MultipleInstances IgnoreNew `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 10)

Register-ScheduledTask `
    -TaskName $taskName `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -Description "Auto-sync %USERPROFILE%\.cursor to GitHub at a regular interval." `
    -RunLevel Limited | Out-Null

Write-Host ""
$intervalHuman = if ($intervalMin -lt 60) { "$intervalMin minutes" } else { "$($intervalMin / 60) hours" }
Write-Host "[OK] Registered scheduled task: $taskName"
Write-Host "  - Runs every $intervalHuman"
Write-Host "  - Also runs at user logon"
Write-Host "  - Log file: %USERPROFILE%\.cursor\.sync.log"
Write-Host ""
Write-Host "Run once manually to test:"
Write-Host "  Start-ScheduledTask -TaskName $taskName"
Write-Host ""
Write-Host "Tail log:"
Write-Host '  Get-Content "$env:USERPROFILE\.cursor\.sync.log" -Tail 20'
Write-Host ""
Write-Host "Uninstall:"
Write-Host '  Unregister-ScheduledTask -TaskName CursorConfigAutoSync -Confirm:$false'
