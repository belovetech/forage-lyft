from engine.sternman_engine import SternmanEngine
import unittest


class TestSternmanEngine(unittest.TestCase):
    """ Test Sternman engine class
    """

    def test_needs_service_true(self):
        """ Test if Sternman engine needs to be serviced
        """
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        """ Test if Sternman engine not needs to be serviced
        """
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())
