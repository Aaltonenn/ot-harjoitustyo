#Nuoteille annetaan numerolliset arvot jotta voidaan laskea
#matemaattisesti ovatko ne duuri tai molli sointuja
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
    "B": 12
}
Reversed = {
    1: "C",
    2: "C#",
    3: "D",
    4: "D#",
    5: "E",
    6: "F",
    7: "F#",
    8: "G",
    9: "G#",
    10: "A",
    11: "A#",
    12: "B"
}


class Service:
    def __init__(self,note1,note2,note3):
        self.list = [Notes[note1], Notes[note2], Notes[note3]]
        self.chord_determination()

#Tutkii onko kyseinen sointu duuri tai molli sointu kutsumalla
#kummallekki luotua metodia
    def chord_determination(self):
        if Service.is_major_chord(self):
            print(f"this is {Reversed[self.rootnote]} major chord")
        if Service.is_minor_chord(self):
            print(f"this is {Reversed[self.rootnote]} minor chord")
        return "this is not major or minor chord"


#tämä metodi tutkii onko annettu sointu duuri(major)sointu.
    def is_major_chord(self):
        i=0
        while i < 3:
            self.list.sort()
            self.rootnote = self.list[0] # pylint: disable=attribute-defined-outside-init
            self.secondnote = self.list[1] # pylint: disable=attribute-defined-outside-init
            self.thirdnote = self.list[2] # pylint: disable=attribute-defined-outside-init
            if (self.rootnote+self.secondnote+self.thirdnote)%3==2:
                if self.rootnote + 4 == self.secondnote and self.rootnote + 7 == self.thirdnote:
                    return True
            self.rootnote += 12
            i+=1
            self.list = [self.rootnote,self.secondnote,self.thirdnote]
        return False


#tämä metodi tutkii onko annettu sointu molli(minor)sointu.
    def is_minor_chord(self):
        i=0
        while i < 3:
            self.list.sort()
            self.rootnote = self.list[0] # pylint: disable=attribute-defined-outside-init
            self.secondnote = self.list[1] # pylint: disable=attribute-defined-outside-init
            self.thirdnote = self.list[2] # pylint: disable=attribute-defined-outside-init
            if (self.rootnote+self.secondnote+self.thirdnote)%3==1:
                if self.rootnote + 3 == self.secondnote and self.rootnote + 7 == self.thirdnote:
                    return True
            self.rootnote += 12
            i+=1
            self.list = [self.rootnote,self.secondnote,self.thirdnote]
        return False
    