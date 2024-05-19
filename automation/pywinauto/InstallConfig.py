import find_pid as find_pid
from pywinauto import Application
import time
process_name = "XPrinter Driver V7.77.exe"

# Find the process ID
pid = find_pid.find_pid(process_name)

if pid :
    app = Application(backend="uia").connect(process=pid)
    main_window = app.top_window()
    main_window.print_control_identifiers()
    main_window['USB'].click()
    main_window['XP80C'].click()
    main_window['Install Now'].click()
    time.sleep(1)
    main_window["No"].click()
else:
    print("Cant find the process")