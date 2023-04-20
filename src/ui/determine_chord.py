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
            if type(test.chord_determination(note1,note2,note3)) == tuple:
                if test.chord_determination(note1,note2,note3)[1] == 1:
                    print(f"That is a {test.chord_determination(note1,note2,note3)[0]} major chord")
                if test.chord_determination(note1,note2,note3)[1] == 2:
                    print(f"That is a {test.chord_determination(note1,note2,note3)[0]} minor chord")
            if test.chord_determination(note1,note2,note3) == "unknonw notes":
                print("The notes you gave are unknown. Please try these for example 'C', 'E', 'G'")
            if test.chord_determination(note1,note2,note3) == "neither":
                print("The notes you gave don't make a major or minor chord")
                    