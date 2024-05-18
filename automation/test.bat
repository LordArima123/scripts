
cd %~dp0

call cd Driver
call echo Opening XPrinter
call start XPrinter.exe
call cd ../
call echo Waiting XPrinter to open
timeout /t 5 /nobreak >nul
call python testXPrinter.py
 PAUSE