. C:\Users\thiba\google_drive\music\dev\scripts\powershell\libs\VirtualDesktop.ps1

Start-Sleep 10  # waiting for loop midi & pycharm launch

vdesk on:4 run:C:\Users\thiba\AppData\Local\Microsoft\WindowsApps\wt.exe --maximized -p "Protocol0 System midi server"

Start-Sleep 5

Get-Desktop 1 | Switch-Desktop
