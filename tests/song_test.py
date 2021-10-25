import unittest
from classes.songs import Songs

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Songs("Forest Swords", "Panic")

    def test_song_has_artist(self):
        self.assertEqual("Forest Swords", self.song.artist_name)

    def test_song_has_name(self):
        self.assertEqual("Panic", self.song.song_name)
