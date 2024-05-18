@echo off
:: Check for admin rights
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting administrative privileges...
    powershell -Command "Start-Process '%~0' -Verb RunAs"
    exit /b
)
cd %~dp0
call cd python
call echo installing Python 3.12
call python-3.12.3-amd64.exe /quiet InstallAllUsers=1 PrependPath=1
timeout /t 5 /nobreak >nul
call cd ../
echo Changing file
call installpip.bat
goto J_END


:J_Loop
call %0
:J_END
PAUSE