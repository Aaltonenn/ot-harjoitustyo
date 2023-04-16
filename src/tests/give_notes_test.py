import unittest 
from services.service import GiveNotes



class TestGiveNotes(unittest.TestCase):
#testaa mitä tapahtuu jos annettua juurisäveltä ei ole olemassa
    def test_given_rootnote_doesnt_exist(self):
        test = GiveNotes.give_notes(self,5,"1")
        self.assertEqual(test, "rootnote doesnt exist")
    
    def test_not_major_or_minor(self):
        test = GiveNotes.give_notes(self,"C","3")
        self.assertEqual(test, "chord has to be major [1] or minor [2]")

    def test_B_major(self):
        test = GiveNotes.give_notes(self,"B","1")
        self.assertEqual(test, "B major consists of B, D# and F# notes.")

    def test_B_minor(self):
        test = GiveNotes.give_notes(self,"B","2")
        self.assertEqual(test, "B minor consists of B, D and F# notes.")

    def test_C_major(self):
        test = GiveNotes.give_notes(self,"C","1")
        self.assertEqual(test, "C major consists of C, E and G notes.")

    def test_C_minor(self):
        test = GiveNotes.give_notes(self,"C","2")
        self.assertEqual(test, "C minor consists of C, D# and G notes.")
