from tkinter import ttk, constants

class WhatChordsGoWell:
#graafisen käyttöliittymän osa joka vastaa sopivien sointujen palauttamisesta
    def __init__(self, root,handle_what_chords_go_well,handle_to_main_menu):
        self._frame = None
        self._root = root
        self.chord_entry = ttk.Entry(master=self._root)
        self._handle_what_chords_go_well = handle_what_chords_go_well
        self._handle_to_main_menu = handle_to_main_menu
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)
        
    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Give a chord and find out what other chords sounds great with it")

        print_button = ttk.Button(
            master=self._frame,
            text="Print",
            command=self._handle_what_chords_go_well
        )
        
        return_button = ttk.Button(
            master=self._frame,
            text="Return to main menu",
            command=self._handle_to_main_menu
        )
        

        label.pack()
        self.chord_entry.pack()
        print_button.pack()
        return_button.pack()
    

    def get_chord_entry(self):
        return self.chord_entry.get()