# pylint: disable=C0103
import unittest
from unittest import mock
import app
import display

class AppTests(unittest.TestCase):

    def test_displays_happy_monitor(self):
        fake_display = mock.Mock(spec=display)
        app.display_current_monitor_status(fake_display)
        fake_display.show_success.assert_called_with()

    def test_displays_monitor_errors(self):
        pass

    def test_displays_error_when_monitor_is_dead(self):
        pass

    def test_will_retry_on_monitor_faliure(self):
        pass


if __name__ == '__main__':
    unittest.main()
