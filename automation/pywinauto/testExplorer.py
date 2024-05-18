import find_pid as find_pid
import pywinauto
import time
process_name = "explorer.exe"

# Find the process ID
pid = find_pid.find_pid(process_name)

if pid :
    app = pywinauto.Application(backend="uia").connect(process=pid)
    main_window = app.top_window()
    main_window.print_control_identifiers()
    pane = main_window.child_window(title="Taskbar")
    
    pywinauto.mouse.right_click(0)
else:
    print("Cant find the process")