from engine.willoughby_engine import WilloughbyEngine

import unittest


class TestWilloughbyEngine(unittest.TestCase):
    """ Test Willoughby engine class
    """

    def test_needs_service_true(self):
        """ Test if willoughby engine needs to be serviced
        """
        current_mileage = 70007
        last_service_mileage = 10000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        """ Test if willoughby engine not needs to be serviced
        """
        current_mileage = 70000
        last_service_mileage = 10000
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
