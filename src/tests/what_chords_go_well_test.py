import unittest 
from services.service import ChordsGoWell

class TestChord_Determination(unittest.TestCase):
    def test_c(self):
        test = ChordsGoWell.chords_go_well(self,"c")
        self.assertEqual(test, ("C" ,['D', 'E', 'F', 'G', 'A', 'B']))

    def test_d(self):
        test = ChordsGoWell.chords_go_well(self,"d")
        self.assertEqual(test, ("D" ,['E', 'F#', 'G', 'A', 'B', 'C#']))

    def test_e(self):
        test = ChordsGoWell.chords_go_well(self,"e")
        self.assertEqual(test, ("E" ,['F#', 'G#', 'A', 'B', 'C#', 'D#']))

    def test_f(self):
        test = ChordsGoWell.chords_go_well(self,"f")
        self.assertEqual(test, ("F" ,['G', 'A', 'A#', 'C', 'D', 'E']))

    def test_g(self):
        test = ChordsGoWell.chords_go_well(self,"g")
        self.assertEqual(test, ("G" ,['A', 'B', 'C', 'D', 'E', 'F#']))

    def test_a(self):
        test = ChordsGoWell.chords_go_well(self,"a")
        self.assertEqual(test, ("A" ,['B', 'C#', 'D', 'E', 'F#', 'G#']))

    def test_b(self):
        test = ChordsGoWell.chords_go_well(self,"b")
        self.assertEqual(test, ("B" ,['C#', 'D#', 'E', 'F#', 'G#', 'A#']))

    def test_q(self):
        test = ChordsGoWell.chords_go_well(self,"q")
        self.assertEqual(test, (''))
