import unittest 
from services.service import GiveNotes



class TestGiveNotes(unittest.TestCase):
#testaa mitä tapahtuu jos annettua juurisäveltä ei ole olemassa
    def test_given_rootnote_doesnt_exist(self):
        test = GiveNotes.give_notes(self,5,"1")
        self.assertEqual(test, "rootnote doesnt exist")

    def test_B_major(self):
        test = GiveNotes.give_notes(self,"B","1")
        self.assertEqual(test, ("B","D#","F#"))

    def test_B_minor(self):
        test = GiveNotes.give_notes(self,"B","2")
        self.assertEqual(test, ("B","D","F#"))

    def test_C_major(self):
        test = GiveNotes.give_notes(self,"C","1")
        self.assertEqual(test, ("C","E","G"))

    def test_C_minor(self):
        test = GiveNotes.give_notes(self,"C","2")
        self.assertEqual(test, ("C","D#","G"))
