from battery.spindler_battery import SpindlerBattery

from datetime import date
import unittest


class TestSpindlerBattery(unittest.TestCase):
    """ Test Spindler battery class
    """

    def test_needs_service_true(self):
        """ test spindler battery need to be serviced
        """
        current_date = date.fromisoformat("2023-06-03")
        last_service_date = date.fromisoformat("2019-06-03")
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        """ test spindler battery not need to be serviced
        """
        current_date = date.fromisoformat("2023-06-03")
        last_service_date = date.fromisoformat("2021-06-03")
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())
