@echo off 
cd %~dp0
call reg.exe add "HKCU\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d "%~dp0background.jpg" /f

call rundll32.exe user32.dll, UpdatePerUserSystemParameters
