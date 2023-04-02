class UI:
    def start(self):
        while True:
            print("give 3 notes")
            note1=int(input())
            note2=int(input())
            note3=int(input())
            if note1==0 or note2 == 0 or note3 == 0:
                print("ok then")
                break
            print(note1, note2, note3)