import unittest
from song_objects import Song, Section, Measure, NotationString


class TestSectionObject(unittest.TestCase):

    def setUp(self):
        song = Song("Title", "by")
        self.section = Section(song, "Section A")

    def test_section_name(self):
        self.assertEqual(self.section.name, "Section A")

    def test_section_correct_in_song(self):
        self.assertTrue(self.section.name in self.section.song.sections)
        self.assertEqual(len(self.section.song.section_sequence), 1)
        self.assertEqual(self.section.song.section_sequence[0], "Section A")

    def test_strings_exist(self):
        self.assertEqual(len(self.section.strings), 7)
        for i in range(7):
            self.assertEqual(type(self.section.strings[i]), NotationString)

    def test_add_measure(self):
        # Starts out as empty list
        self.assertEqual(len(self.section.measures), 0)

        # add a fake "Measure 1"
        self.section.add_measure("Measure_1")
        self.assertEqual(len(self.section.measures), 1)
        self.assertEqual(self.section.measures[0], "Measure_1")

        # add a fake "Measure 1"
        self.section.add_measure("Measure_2")
        self.assertEqual(len(self.section.measures), 2)
        self.assertEqual(self.section.measures[1], "Measure_2")

    def test_last_measure(self):
        # Starts out as none
        self.assertTrue(self.section.last_measure() is None)

        # Once we add a measure we get that measure back
        m1 = Measure(self.section)
        self.assertTrue(self.section.last_measure() is m1)

        # Adding a second measure, it gives us the second one
        m2 = Measure(self.section)
        self.assertTrue(self.section.last_measure() is m2)
