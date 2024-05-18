import psutil
from pywinauto import Application
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
    app = Application().connect(process=pid)

    print(pid)
    print(app)
else:
    print(f"No running process found with the name {process_name}")