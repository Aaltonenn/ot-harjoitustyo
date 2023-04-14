from services.service import Service

Notes = {
    "C": 1,
    "C#": 2,
    "D": 3,
    "D#": 4,
    "E": 5,
    "F": 6,
    "F#": 7,
    "G": 8,
    "G#": 9,
    "A": 10,
    "A#": 11,
    "B": 12,
}

class Determine_chord:
    def determine_chord(self):
        while True:
            print("give 3 notes")
            note1=input()
            note2=input()
            note3=input()

            if note1 == "0" or note2 == 0 or note3 == 0:
                print("ok then")
                break

            if note1 not in Notes or note2 not in Notes or note3 not in Notes:
                print("error notes are not real")
                continue
            Service(note1,note2,note3)