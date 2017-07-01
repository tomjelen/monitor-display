# pylint: disable=C0103
import unittest
from unittest import mock
from unittest.mock import patch
from unittest.mock import ANY
import requests_mock
import app
import monitor
import display


class AppTests(unittest.TestCase):

    @requests_mock.mock()
    def test_displays_happy_monitor(self, fake_requests):
        fake_requests.get('http://example.org/status',
                          json={'success': True},
                          status_code=200)

        fake_display = mock.Mock(spec=display)

        app.display_current_monitor_status(monitor, fake_display)
        fake_display.show_success.assert_called_with()

    @requests_mock.mock()
    def test_displays_monitor_errors(self, fake_requests):
        fake_requests.get('http://example.org/status',
                          json={'success': False},
                          status_code=200)

        fake_display = mock.Mock(spec=display)

        app.display_current_monitor_status(monitor, fake_display)
        fake_display.show_failure.assert_called_with()

    @requests_mock.mock()
    @patch('time.sleep', return_value=None)  # Instant sleeps
    def test_displays_error_when_monitor_is_dead(self, fake_requests, fake_sleep):
        fake_requests.get('http://example.org/status',
                          json={'a': 'b'},
                          status_code=500)

        fake_display = mock.Mock(spec=display)

        app.display_current_monitor_status(monitor, fake_display)
        fake_display.show_general_failure.assert_called_with(ANY)

    @requests_mock.mock()
    @patch('time.sleep', return_value=None)  # Instant sleeps
    def test_will_retry_on_monitor_failure(self, fake_requests, fake_sleep):
        fake_requests.get('http://example.org/status',
                          json={'a': 'b'},
                          status_code=500)

        fake_display = mock.Mock(spec=display)

        app.display_current_monitor_status(monitor, fake_display)
        self.assertGreater(fake_requests.call_count, 1)


if __name__ == '__main__':
    unittest.main()
