from services.service import ChordDetermination

class DetermineChord:
    def determine_chord(self):
        while True:
            print("Give 3 notes - or press 0 if you want to exit to main menu")
            note1=input().upper()
            if note1 == "0":
                print("Going back to main menu")
                break
            note2=input().upper()
            note3=input().upper()

            test=ChordDetermination()
            print(test.chord_determination(note1,note2,note3))
