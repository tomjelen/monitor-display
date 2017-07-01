from collections import namedtuple
import requests

MONITOR_URL = 'http://example.org/status'
MonitorReport = namedtuple("MonitorReport", ["success"])


class MonitorNotAvailableError(Exception):
    pass


def query_status():
    resp = requests.get(MONITOR_URL)

    if resp.status_code == 200:
        return report(resp.json())
    else:
        raise MonitorNotAvailableError('The monitor seems to be dead :(')


def report(monitor_result):
    return MonitorReport(monitor_result['success'])
