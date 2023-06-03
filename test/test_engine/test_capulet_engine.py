from engine.capulet_engine import CapuletEngine

import unittest


class TestCapulateEngine(unittest.TestCase):
    """ Test Capulate engine class
    """

    def test_needs_service_true(self):
        """ Test if capulate engine needs to be serviced
        """
        current_mileage = 40004
        last_service_mileage = 10000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        """ Test if capulate engine not needs to be serviced
        """
        current_mileage = 40000
        last_service_mileage = 10000
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
