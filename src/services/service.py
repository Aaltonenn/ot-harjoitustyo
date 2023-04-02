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
    "B": 12,
}



class Service:
#Tutkii onko kyseinen sointu duuri tai molli sointu kutsumalla 
#kummallekki luotua metodia
    def chord_recongition(note1,note2,note3):
        if Service.is_major_chord(note1,note2,note3) == True:
            return "this is major chord"
        elif Service.is_minor_chord(note1,note2,note3) == True:
            return "this is minor chord"
        else:
            return "this is not major or minor chord"



    
#tämä metodi tutkii onko annettu sointu duuri(major)sointu.
#tällä hetkellä metodi olettaa että juurisävel on joko c,c#,d,d# tai E
    def is_major_chord(note1,note2,note3):
        #tällä hetkellä ohjelma tutkii
        if Notes[note1] + 4 == Notes[note2] and Notes[note1] + 7 == Notes[note3]:
            return True 
        if Notes[note1] + 4 == Notes[note3] and Notes[note1] + 7 == Notes[note2]:
            return True
        if Notes[note2] + 4 == Notes[note1] and Notes[note2] + 7 == Notes[note3]:
            return True
        if Notes[note2] + 4 == Notes[note3] and Notes[note2] + 7 == Notes[note1]:
            return True
        if Notes[note3] + 4 == Notes[note1] and Notes[note3] + 7 == Notes[note2]:
            return True
        if Notes[note3] + 4 == Notes[note2] and Notes[note3] + 7 == Notes[note1]:
            return True
        return False


#tämä metodi tutkii onko annettu sointu molli(minor)sointu.
#tällä hetkellä metodi olettaa että juurisävel on joko c,c#,d,d# tai E
    def is_minor_chord(note1,note2,note3):
        if Notes[note1] + 3 == Notes[note2] and Notes[note1] + 7 == Notes[note3]:
            return True 
        if Notes[note1] + 3 == Notes[note3] and Notes[note1] + 7 == Notes[note2]:
            return True
        if Notes[note2] + 3 == Notes[note1] and Notes[note2] + 7 == Notes[note3]:
            return True
        if Notes[note2] + 3 == Notes[note3] and Notes[note2] + 7 == Notes[note1]:
            return True
        if Notes[note3] + 3 == Notes[note1] and Notes[note3] + 7 == Notes[note2]:
            return True
        if Notes[note3] + 3 == Notes[note2] and Notes[note3] + 7 == Notes[note1]:
            return True
        return False