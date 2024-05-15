
cd %~dp0
call cd Driver
call echo Opening XPrinter
call start XPrinter.exe
call cd ../
call echo Waiting XPrinter to open
timeout /t 3 /nobreak >nul
call python test.py
PAUSE