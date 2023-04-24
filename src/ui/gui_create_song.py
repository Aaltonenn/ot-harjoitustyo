from tkinter import ttk, constants

class CreateSong:
#Graafisen käyttäliittymän osa joka vastaa uusien kappaleiden luomiesta ja kirjoittamisesta tiedostoon
    def __init__(self, root,handle_create_song,handle_to_main_menu):
        self._frame = None
        self._root = root
        self._handle_create_song = handle_create_song
        self._handle_to_main_menu = handle_to_main_menu
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)
        
    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="To the first box write the name of the artist\nTo the second box write the name of the song\nTo the third box write down the chord progression (just a string)")
        self.artist_entry = ttk.Entry(master=self._root)
        self.song_name_entry = ttk.Entry(master=self._root)
        self.chord_progression_entry = ttk.Entry(master=self._root)
        

        print_button = ttk.Button(
            master=self._frame,
            text="Create the song",
            command=self._handle_create_song
        )
        
        return_button = ttk.Button(
            master=self._frame,
            text="Return to main menu",
            command=self._handle_to_main_menu
        )
        

        label.pack()
        self.artist_entry.pack()
        self.song_name_entry.pack()
        self.chord_progression_entry.pack()
        print_button.pack()
        return_button.pack()

    def get_artist_entry(self):
        return self.artist_entry.get()

    def get_song_name_entry(self):
        return self.song_name_entry.get()

    def get_chord_progression_entry(self):
        return self.chord_progression_entry.get()

    