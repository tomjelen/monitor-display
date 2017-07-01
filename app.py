"""

def displayCurrentMonitorStatus(monitor, leds):
    try
        report = monitor.query_status()
        leds.show(report)
    except
        leds.show_general_failure()




if __name__ == '__main__':
  leds.init()

  While:
    displayCurrentMonitorStatus(monitor, leds)
    time.sleep(10)

"""
