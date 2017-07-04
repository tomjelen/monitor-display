import time
import monitor
from monitor import MonitorNotAvailableError
import display


def display_current_monitor_status(monitor, display):
    try:
        report = monitor.query_status()

        if report.success['status'] == 1:
            display.show_success()
        elif report.success['status'] == 0:
            # Implemented status 0 
            # for handle cases where Travis kick out us
            display.show_warning()
        else:
            display.show_failure()

    except MonitorNotAvailableError:
        display.show_general_failure('The monitor seems to be dead :(')


if __name__ == '__main__':
    display.init()
    
    while True:
        display_current_monitor_status(monitor, display)
        # Travis API suck! 
        # Kick us out for a while if we 
        # do more tha 1 request per minute
        time.sleep(60) 
