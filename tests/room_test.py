import unittest
from classes.rooms import Rooms
from classes.guests import Guests
from classes.songs import Songs

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Rooms(1)
        self.guests = Guests("Sam")
        self.songs = Songs("Forest Swords", "Panic")

    def test_room_has_number(self):
        self.assertEqual(1, self.room.room_no)

    def test_guest_added_to_room(self):
        guest = self.guests
        self.room.check_in(guest)
        self.assertEqual("Sam", self.room.guests[0])

    def test_guest_leaves_room(self):
        guest = self.guests
        self.room.check_in(guest)
        self.room.check_out(guest)
        self.assertEqual([], self.room.guests)

    def test_song_added_to_room(self):
        song = self.songs
        self.room.add_song(song)
        self.assertEqual("Forest Swords", self.room.songs[0])
