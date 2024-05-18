echo Try installing pip pakages

call "C:\Program Files\Python312\Scripts\pip" install pyautogui pillow

IF %ERRORLEVEL% NEQ 0 (
    call echo loop
   
    call %0
)
echo Running scripts
call test.bat
