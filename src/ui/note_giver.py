from services.service import GiveNotes
class NoteGiver:
#tekstikäyttöliittymän osa joka vastaa sointujen etsimisestä

#sovelluslogiikka löytyy service.Givenotes
    def give_note(self):
        while True:
            rootnote = input("Give a chord's rootnote (for example C) or press 0 to exit").upper()
            if rootnote == "0":
                break
            majorminor = input("Do you want it to be major [1] or minor [2]")
            if majorminor not in ("1","2"):
                print("chord has to be major [1] or minor [2]")
                continue
            test=GiveNotes()
            if type(test.give_notes(rootnote, majorminor)) == tuple:
                notes = (test.give_notes(rootnote, majorminor))
                if majorminor == "1":
                    print(f" {rootnote} major consits of {notes[0]}, {notes[1]} and {notes[2]}")
                if majorminor == "2":
                    print(f" {rootnote} minor consits of {notes[0]}, {notes[1]} and {notes[2]}")
            if test.give_notes(rootnote, majorminor) == "rootnote doesnt exist":
                print(" Given rootnote doesn't exist. Try giving 'C' for example")
        
        print("going back to main menu")
