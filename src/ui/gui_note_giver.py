from tkinter import Tk, ttk, constants

class NoteGiver:
    def __init__(self, root,handle_give_notes,handle_to_main_menu):
        self._frame = None
        self._root = root
        self._handle_give_notes = handle_give_notes
        self._handle_to_main_menu = handle_to_main_menu
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)
        
    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="To the first box give a rootnote (for example 'C' or 'G#' or 'Ab')\nand into second box do you want the chord to be major [1] or minor [2]")
        self.rootnote_entry = ttk.Entry(master=self._root)
        self.majorminor_entry = ttk.Entry(master=self._root)


        button = ttk.Button(
            master=self._frame,
            text="Enter",
            command=self._handle_give_notes
        )
        
        return_button = ttk.Button(
            master=self._frame,
            text="Return to main menu",
            command=self._handle_to_main_menu
        )
        

        label.pack()
        button.pack()
        return_button.pack()
        self.rootnote_entry.pack()
        self.majorminor_entry.pack()

    def get_rootnote_entry(self):
        return self.rootnote_entry.get()

    def get_majorminor_entry(self):
        return self.majorminor_entry.get()
