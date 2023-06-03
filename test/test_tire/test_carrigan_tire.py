from tire.carrigan_tire import CarriganTire

import unittest


class TestCarriganTire(unittest.TestCase):
    """ Test Carrigan tire class method
    """

    def test_needs_service_true(self):
        """ Test if carrigan tire need to be serviced
        """
        wears = [0.5, 0.2, 0.4, 0.9]
        tire = CarriganTire(wears)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        """ Test if carrigan tire not need to be serviced
        """
        wears = [0.5, 0.2, 0.4, 0.1]
        tire = CarriganTire(wears)
        self.assertFalse(tire.needs_service())
