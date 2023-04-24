import os
from repositories.song_repository import SongRepository
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
    "DB": 2,
    "EB": 4,
    "FB": 5,
    "GB": 7,
    "AB": 9,
    "BB": 11,
    "CB": 12,
    "B#": 1,
    "E#": 6
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


class ChordDetermination:

#Tutkii onko kyseinen sointu duuri tai molli sointu kutsumalla
#kummallekki luotua metodia
    def chord_determination(self,note1,note2,note3):
        if note1 not in Notes or note2 not in Notes or note3 not in Notes:
            return "unknown notes"
        is_major = ChordDetermination.is_major_chord(self,note1,note2,note3)
        if is_major is not False:
            return (Reversed[is_major],1)
        is_minor = ChordDetermination.is_minor_chord(self,note1,note2,note3)
        if is_minor is not False:
            return (Reversed[is_minor],2)
        return "neither"


#tämä metodi tutkii onko annettu sointu duuri(major)sointu.
    def is_major_chord(self,note1,note2,note3):
        list_of_notes = [Notes[note1], Notes[note2], Notes[note3]]
        i=0
        while i < 3:
            list_of_notes.sort()
            rootnote = list_of_notes[0]
            secondnote = list_of_notes[1]
            thirdnote = list_of_notes[2]
            if (rootnote+secondnote+thirdnote)%3==2:
                if rootnote + 4 == secondnote and rootnote + 7 == thirdnote:
                    return rootnote
            rootnote += 12
            i+=1
            list_of_notes = [rootnote,secondnote,thirdnote]
        return False


#tämä metodi tutkii onko annettu sointu molli(minor)sointu.
    def is_minor_chord(self,note1,note2,note3):
        list_of_notes = [Notes[note1], Notes[note2], Notes[note3]]
        i=0
        while i < 3:
            list_of_notes.sort()
            rootnote = list_of_notes[0]
            secondnote = list_of_notes[1]
            thirdnote = list_of_notes[2]
            if (rootnote+secondnote+thirdnote)%3==1:
                if rootnote + 3 == secondnote and rootnote + 7 == thirdnote:
                    return rootnote
            rootnote += 12
            i+=1
            list_of_notes = [rootnote,secondnote,thirdnote]
        return False

class GiveNotes:
#kertoo mistä sävelistä käyttäjän antama duuri/mollisointu koostuu
    def give_notes(self, rootnote, majorminor):
        if rootnote not in Notes:
            return "rootnote doesnt exist"
        if majorminor == "1":
            numbers = [Notes[rootnote], Notes[rootnote]+4, Notes[rootnote]+7]
            if numbers[1]>12:
                numbers[1] = numbers[1]-12
            if numbers[2]>12:
                numbers[2] = numbers[2]-12
            notes = [Reversed[numbers[0]],Reversed[numbers[1]],Reversed[numbers[2]]]
            return (notes[0],notes[1],notes[2])
        numbers = [Notes[rootnote], Notes[rootnote]+3, Notes[rootnote]+7]
        if numbers[1]>12:
            numbers[1] = numbers[1]-12
        if numbers[2]>12:
            numbers[2] = numbers[2]-12
        notes = [Reversed[numbers[0]],Reversed[numbers[1]],Reversed[numbers[2]]]
        return (notes[0],notes[1],notes[2])

class SongSearcher:
#etsii kaikki tiedostoon tallennetut kappaleet
    def search_songs(self):
        dirname = os.path.dirname(__file__)
        song_repository = SongRepository(os.path.join(dirname, "..", "..", "data", "songs.csv"))
        for song in song_repository.read():
            print(f"{song[0]},  {song[1]},  {song[2]}")

class SongCreater:
#luo tiedostoon uuden kappaleen, kappaleet voi lukea SongSearcherilla
    def create_song(artist, song_name, chord_progression):
        dirname = os.path.dirname(__file__)
        song_repository = SongRepository(os.path.join(dirname, "..", "..", "data","songs.csv"))
        song_repository.create(artist, song_name, chord_progression)
        print("Your song has been created - Here is the new list of all songs")
        for song in song_repository.read():
            print(f"{song[0]},  {song[1]},  {song[2]}")
