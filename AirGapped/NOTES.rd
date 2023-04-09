PS C:\Users\rocco> [console]::CapsLock
False
PS C:\Users\rocco> [console]::CapsLock
True
PS C:\Users\rocco> $wash = New-Object -ComObject WScrips.Shell
New-Object : Recupero della class factory COM per il componente con CLSID
{00000000-0000-0000-0000-000000000000} non riuscito a causa del seguente errore: 80040154
Interfaccia non registrata. (Eccezione da HRESULT: 0x80040154 (REGDB_E_CLASSNOTREG)).
In riga:1 car:9
+ $wash = New-Object -ComObject WScrips.Shell
+         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : ResourceUnavailable: (:) [New-Object], COMException
    + FullyQualifiedErrorId : NoCOMClassIdentified,Microsoft.PowerShell.Commands.NewObjectCommand

PS C:\Users\rocco> $wash = New-Object -ComObject WScript.Shell
PS C:\Users\rocco> $wash.SendKeys('{CAPSLOCK}')
PS C:\Users\rocco> $wash.SendKeys('{CAPSLOCK}')