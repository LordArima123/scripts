@echo off 

net session >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    call echo You need to run this script as Administrator
    call echo Right click this file, select Run as Administrator
    goto J_END
)
cd %~dp0
call echo Changing Wallpaper
call background.bat
call cd Driver
call echo Installing UltraViewer
call UltraViewer_setup_6.6_en.exe /VERYSILENT /NORESTART
call echo Installing AnyDesk
call AnyDesk.exe --install "C:\Program Files (x86)\AnyDesk" --create-shortcuts --create-desktop-icon --silent
call echo Installing XPrinter
call XPrinter.exe /SILENT /TASKS="desktopicon"
call cd ../
call cd ops-installation
call echo Installing OPS
call installSillent.bat
call cd ../
call cd %~dp0Activate-Windows10
call echo Activating Windows

call script.bat

:J_END

PAUSE