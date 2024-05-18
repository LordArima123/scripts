
cd %~dp0
call echo Opening XPrinter
call cd "C:\XINYE POS Printer Driver\XPrinter Driver V7.77"
call start "" "XPrinter Driver V7.77.exe"

call echo Waiting XPrinter to open
cd %~dp0pywinauto
timeout /t 5 /nobreak >nul
call python InstallConfig.py
 PAUSE