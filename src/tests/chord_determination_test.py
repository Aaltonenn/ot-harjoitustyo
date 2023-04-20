import unittest 
from services.service import ChordDetermination

class TestChord_Determination(unittest.TestCase):
#testaa onko kollme säveltä duurisointu
    def test_is_major_chord(self):
        test = ChordDetermination.chord_determination(self,"B", "D#", "F#")
        self.assertEqual(test, ("B",1))
#testaa onko samat kolme säveltä duurisointu mutta eri järjestyksessä
    def test_second_inversion_major_chord(self):
        test = ChordDetermination.chord_determination(self,"E", "G", "C")
        self.assertEqual(test, ("C",1))
#testaa onko samat kolme säveltä duurisointu mutta vielä eri järjestyksessä
    def test_third_inversion_major_chord(self):
        test = ChordDetermination.chord_determination(self,"G", "C", "E")
        self.assertEqual(test, ("C",1))
#testaa onko samat kolme säveltä duurisointu mutta vielä kerran eri järjestyksessä
    def test_random_order_major_chord(self):
        test = ChordDetermination.chord_determination(self,"C", "G", "E")
        self.assertEqual(test, ("C",1))
#testaa onko kolme säveltä mollisointu
    def test_is_minor_chord(self):
        test = ChordDetermination.chord_determination(self,"B", "D", "F#")
        self.assertEqual(test, ("B",2))
#testaa onko samat kolme säveltä mollisointu, mutta eri järjestyksessä
    def test_second_inversion_minor_chord(self):
        test = ChordDetermination.chord_determination(self,"D#", "G", "C")
        self.assertEqual(test, ("C",2))
#testaa onko samat kolme säveltä mollisointu, mutta eri järjestyksessä
    def test_third_inversion_minor_chord(self):
        test = ChordDetermination.chord_determination(self,"G", "C", "D#")
        self.assertEqual(test, ("C",2))
#testaa onko samat kolme säveltä mollisointu, mutta eri järjestyksessä
    def test_random_order_minor_chord(self):
        test = ChordDetermination.chord_determination(self,"C", "G", "D#")
        self.assertEqual(test, ("C",2))
#testaa toimiiko jos annetut kolme säveltä ei muodosta duuri- eikä mollisointua
    def test_not_major_nor_minor_chord(self):
        test = ChordDetermination.chord_determination(self,"C", "F", "G")
        self.assertEqual(test, "neither")
#testaa jos annetaan jokin sävel jota ei ole olemassa
    def test_given_notes_dont_exist(self):
        test = ChordDetermination.chord_determination(self,"C", "F", "1")
        self.assertEqual(test, "unknown notes")


