import unittest 
from services.service import Service

class TestChord_Recognition(unittest.TestCase):
    def test_is_major_chord(self):
        test = Service.chord_recongition("C", "E", "G")
        self.assertEqual(test, "this is major chord")

    def test_is_minor_chord(self):
        test = Service.chord_recongition("C", "D#", "G")
        self.assertEqual(test, "this is minor chord")

    def test_not_major_nor_minor_chord(self):
        test = Service.chord_recongition("C", "F", "G")
        self.assertEqual(test, "this is not major or minor chord")