from collections import namedtuple
import time
import requests

MONITOR_URL = 'https://242v7ngehg.execute-api.eu-west-1.amazonaws.com/Prod/status'
MonitorReport = namedtuple("MonitorReport", ["success"])

class MonitorNotAvailableError(Exception):
    pass

def query_status(retry_attempts=0):
    resp = requests.get(MONITOR_URL)
    if resp.status_code == 200:
        return report(resp.json())
    else:
        # back off if the server is throwing errors
        if retry_attempts < 5:
            time.sleep(5 * retry_attempts)
            retry_attempts += 1
            return query_status(retry_attempts)
        else:
            raise MonitorNotAvailableError()


def report(monitor_result):
    return MonitorReport(monitor_result['success'])
