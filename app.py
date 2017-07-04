import time
import monitor
from monitor import MonitorNotAvailableError
import display

def display_current_monitor_status(monitor, display):
    try:
        report = monitor.query_status()

        if report.success:
            display.show_success()
        else:
            display.show_failure()

    except MonitorNotAvailableError:
        display.show_general_failure('The monitor seems to be dead :(')


if __name__ == '__main__':
    display.init()
    
    while True:
        display_current_monitor_status(monitor, display)
        time.sleep(10) 
