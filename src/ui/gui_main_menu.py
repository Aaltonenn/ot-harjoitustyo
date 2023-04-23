from tkinter import Tk, ttk, constants, StringVar
from ui.gui_note_giver import NoteGiver
from ui.gui_determine_chord import DetermineChord
from services.service import GiveNotes, ChordDetermination
import time


class UI_m:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_main_menu()

    def _hide_current_view(self):
        if self._current_view != None:
            self._current_view.destroy()
        try:
            self._current_view.rootnote_entry.destroy()
            self._current_view.majorminor_entry.destroy()
        except AttributeError:
            pass
        try:
            self._current_view.first_entry.destroy()
            self._current_view.second_entry.destroy()
            self._current_view.third_entry.destroy()
        except AttributeError:
            pass
        self._current_view = None

    def _show_main_menu(self):
        self._hide_current_view()
        self._current_view = MainMenuUI(self._root, self.handle_to_give_notes, self.handle_to_determine_chord)
        self._current_view.pack()

    def handle_to_give_notes(self):
        self._hide_current_view()
        self._current_view = NoteGiver(self._root, self.handle_give_notes, self.handle_to_main_menu)
        self._current_view.pack()

    def handle_to_determine_chord(self):
        self._hide_current_view()
        self._current_view = DetermineChord(self._root, self.handle_determine_chord, self.handle_to_main_menu)
        self._current_view.pack()

    def handle_determine_chord(self):
        note1=self._current_view.get_first_entry().upper()
        note2=self._current_view.get_second_entry().upper()
        note3=self._current_view.get_third_entry().upper()
        test=ChordDetermination()
        if type(test.chord_determination(note1,note2,note3)) == tuple:
            if test.chord_determination(note1,note2,note3)[1] == 1:
                print(f"That is a {test.chord_determination(note1,note2,note3)[0]} major chord")
            if test.chord_determination(note1,note2,note3)[1] == 2:
                print(f"That is a {test.chord_determination(note1,note2,note3)[0]} minor chord")
        if test.chord_determination(note1,note2,note3) == "unknonw notes":
            print("The notes you gave are unknown. Please try these for example 'C', 'E', 'G'")
        print("chillisti ja tällee")
        if test.chord_determination(note1,note2,note3) == "neither":
            print("The notes you gave don't make a major or minor chord")

    def handle_give_notes(self):
        rootnote=self._current_view.get_rootnote_entry()
        rootnote=rootnote.upper()
        majorminor=self._current_view.get_majorminor_entry()
        
        test=GiveNotes()
        if test.give_notes(rootnote, majorminor) == "rootnote doesnt exist":
                print("Given rootnote doesn't exist. Try giving 'C' for example")
        if majorminor not in ("1","2"):
            print("chord has to be major [1] or minor [2]")

        if type(test.give_notes(rootnote, majorminor)) == tuple:
            notes = (test.give_notes(rootnote, majorminor))             
            if len(rootnote) == 2 and rootnote[1] == "B":
                rootnote = rootnote[0] + "b"
            if majorminor == "1":
                print(f"{rootnote} major consits of {notes[0]}, {notes[1]} and {notes[2]}")
            if majorminor == "2":
                print(f"{rootnote} minor consits of {notes[0]}, {notes[1]} and {notes[2]}")
        
    def handle_to_main_menu(self):
        self._show_main_menu()



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

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="MAIN MENU\nWhat would you like to do?")

        give_notes_button = ttk.Button(
            master=self._frame,
            text="Give a chord and find out what notes it's made from",
            command=self.handle_give_notes
        )
        
        determine_chord_button = ttk.Button(
            master=self._frame,
            text="Give 3 notes and find out does it make a major or minor chord",
            command=self.handle_determine_chord
        )


        label.grid(row=1, column=0)
        give_notes_button.grid(row=2, column=0)
        determine_chord_button.grid(row=3, column=0)
