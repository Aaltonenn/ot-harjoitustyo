from tkinter import Tk, ttk, constants
from ui.gui_note_giver import NoteGiver



class UI_m:
    def __init__(self, root):
        self._root = root
        self._current_view = None


    def start(self):
        self._show_main_menu()

    def _hide_current_view(self):
        if self._current_view != None:
            self._current_view.destroy()
        self._current_view = None

    def _show_main_menu(self):
        self._hide_current_view()
        self._current_view = MainMenuUI(self._root, self.handle_give_notes, self.handle_determine_chord)
        self._current_view.pack()

    def handle_give_notes(self):
        to_note_giver = NoteGiver(self._root, self.handle_chill)
        to_note_giver.pack()

    def handle_determine_chord(self):
        print("chillisti ja tällee")
    
    def handle_chill(self):
        print("chillutellen")



class MainMenuUI:
    def __init__(self, root, handle_give_notes, handle_determine_chord):
        self._root = root
        self._current_view = None
        self._frame = None
        self.handle_give_notes = handle_give_notes
        self.handle_determine_chord = handle_determine_chord
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="MAIN MENU")
        self._entry = ttk.Entry(master=self._root)

        give_notes_button = ttk.Button(
            master=self._frame,
            text="to give notes",
            command=self.handle_give_notes
        )
        
        determine_chord_button = ttk.Button(
            master=self._frame,
            text="to determine chord",
            command=self.handle_determine_chord
        )


        label.grid(row=1, column=0)
        give_notes_button.grid(row=2, column=0)
        determine_chord_button.grid(row=3, column=0)
