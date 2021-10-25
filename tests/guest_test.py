import unittest
from classes.guests import Guests

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guests("Sam")

    def test_guest_has_name(self):
        self.assertEqual("Sam", self.guest.guest_name)