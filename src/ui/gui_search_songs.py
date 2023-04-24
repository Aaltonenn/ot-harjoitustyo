from tkinter import ttk, constants

class SearchSongs:
#graafisen käyttöliittymän osa joka vastaa tiedostossa olevien kappaleiden lukemisesta
    def __init__(self, root,handle_search_songs,handle_to_main_menu):
        self._frame = None
        self._root = root
        self._handle_search_songs = handle_search_songs
        self._handle_to_main_menu = handle_to_main_menu
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)
        
    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Would you like to print a list of songs and their chord progressions")

        print_button = ttk.Button(
            master=self._frame,
            text="Print",
            command=self._handle_search_songs
        )
        
        return_button = ttk.Button(
            master=self._frame,
            text="Return to main menu",
            command=self._handle_to_main_menu
        )
        

        label.pack()
        print_button.pack()
        return_button.pack()
    