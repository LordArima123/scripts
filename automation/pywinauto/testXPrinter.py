import psutil
from pywinauto import Application
import time
def find_pid_by_name(process_name):
    for proc in psutil.process_iter(['pid', 'name']):
        if proc.info['name'] == process_name:
            return proc.info['pid']
    return None

process_name = "XPrinter.tmp"

# Find the process ID
pid = find_pid_by_name(process_name)

if pid:
    # Connect to the application by its process ID
    app = Application(backend="uia").connect(process=pid)
    main_window = app.top_window()
    # main_window['CheckBox'].wait("enabled").click_input()
    main_window.print_control_identifiers()
    main_window['I accept the agreementRadioButton'].click()
    main_window['Next'].click()
    
    main_window['Next'].click()
    
    main_window.print_control_identifiers()
    checkbox = main_window['CheckBox']
    checkbox.click_input()
    main_window['Next'].click()
    main_window['Install'].click()
    main_window['Finish'].click()
    
    
else:
    print(f"No running process found with the name {process_name}")