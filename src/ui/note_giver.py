from services.service import GiveNotes
class NoteGiver:
    def give_note(self):
        while True:
            rootnote = input("Give a chord's rootnote (for example C) or press 0 to exit").upper()
            if rootnote == "0":
                break
            majorminor = input("Do you want it to be major [1] or minor [2]")
            test=GiveNotes()
            print(test.give_notes(rootnote, majorminor))
        print("going back to main menu")
