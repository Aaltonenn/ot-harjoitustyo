from ui.determine_chord import DetermineChord
from ui.note_giver import NoteGiver

class UI:
    def start(self):
        while True:
            command = int(input("What would you like to do? \n Know what notes go into a chord? (press 1) \n  or \n Give 3 notes and find out if they make a chord? (press 2) \n  or\n Exit (press 0)"))
            if command == 1:
                note_giver_ui = NoteGiver()
                note_giver_ui.give_note()
            if command == 2:           
                print("Going into chord determination section:")
                determine_ui = DetermineChord()
                determine_ui.determine_chord()
            if command == 0:
                break
        print("Turning off...")
                