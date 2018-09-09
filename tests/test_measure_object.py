import unittest
from song_objects import Section, Measure, Beat


class TestMeasure(unittest.TestCase):

    def setUp(self):
        s1 = Section(None, "A")
        self.measure = Measure(s1)

    def test_(self):
        self.assertTrue(False)
