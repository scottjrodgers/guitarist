import unittest
from song_objects import Song, Section


class TestSongObject(unittest.TestCase):

    def setUp(self):
        self.song = Song(title="This is my Test Song", by="Scott J. Rodgers",
                         tuning=['C2', 'G2', 'C3', 'G3', 'C4', 'E4'])
        section_a1 = Section(self.song, "A1")
        section_b1 = Section(self.song, "B1")
        section_a2 = Section(self.song, "A2")
        self.song.repeat_section("B1")
        section_a3 = Section(self.song, "A3")

    def test_song_title(self):
        self.assertEqual(self.song.title, "This is my Test Song")

    def test_song_writer(self):
        self.assertEqual(self.song.by, "Scott J. Rodgers")

    def test_song_tuning(self):
        self.assertEqual(self.song.tuning, ['C2', 'G2', 'C3', 'G3', 'C4', 'E4'])

    def test_sections_dictionary(self):
        self.assertTrue("A1" in self.song.sections)
        self.assertTrue("B1" in self.song.sections)
        self.assertTrue("A2" in self.song.sections)
        self.assertFalse("B2" in self.song.sections)
        self.assertTrue("A3" in self.song.sections)

    def test_sections_list(self):
        self.assertEqual(self.song.section_sequence, ['A1', 'B1', 'A2', 'B1', 'A3'])
