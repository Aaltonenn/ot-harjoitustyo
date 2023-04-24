class SongRepository:
#kappaleiden repositorio, joka vastaa tiedostosta
#löytyvän kappaleiden lukemiesta ja kirjoittamisesta
    def __init__(self, file_path):
        self._file_path = file_path

    def find_all(self):
        return self.read()

    def create(self, artist, song_name, chord_progression):
        songs = self.find_all()
        new_song = [artist,song_name,chord_progression]
        songs.append(new_song)
        self._write(songs)

    def read(self):
        songs = []
        with open(self._file_path) as file:
            for row in file:
                row = row.replace("\n", "")
                parts = row.split(";")
                info = []
                info.append(parts[0])
                info.append(parts[1])
                info.append(parts[2])
                songs.append(info)
        return songs

    def _write(self, songs):
        text=""
        with open(self._file_path, "w") as file:
            for song in songs:
                row = f"{song[0]};{song[1]};{song[2]}\n"
                text+=row
            file.write(text)
