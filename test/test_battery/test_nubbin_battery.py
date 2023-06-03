from battery.nubbin_battery import NubbinBattery

from datetime import date
import unittest


class TestNubbinBattery(unittest.TestCase):
    """ Test Nubbin battery class
    """

    def test_needs_service_true(self):
        """ test nubbin battery need to be serviced
        """
        current_date = date.fromisoformat("2023-06-03")
        last_service_date = date.fromisoformat("2018-06-03")
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        """ test nubbin battery need to be serviced
        """
        current_date = date.fromisoformat("2023-06-03")
        last_service_date = date.fromisoformat("2021-06-03")
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())


if __name__ == "__main__":
    unittest.main()
