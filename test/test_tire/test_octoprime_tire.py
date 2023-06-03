from tire.octoprime_tire import OctoprimeTire

import unittest


class TestOctoprimeTire(unittest.TestCase):
    """ Test OctoprimeTire tire class method
    """

    def test_needs_service_true(self):
        """ Test if OctoprimeTire tire need to be serviced
        """
        wears = [0.8, 0.9, 0.7, 0.9]
        tire = OctoprimeTire(wears)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        """ Test if OctoprimeTire tire not need to be serviced
        """
        wears = [0.5, 0.2, 0.4, 0.1]
        tire = OctoprimeTire(wears)
        self.assertFalse(tire.needs_service())
