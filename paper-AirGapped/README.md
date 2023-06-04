# Labz

## Read content in powershell
$content = Get-Content -Path "c:\Users\Public\file.txt"
$binary_s = $binaryString = $fileContent | ForEach-Object { [System.Convert]::ToString($_, 2).PadLeft(8, '0') }
