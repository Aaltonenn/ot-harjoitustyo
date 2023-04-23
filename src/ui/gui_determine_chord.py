from tkinter import Tk, ttk, constants

class DetermineChord:
    def __init__(self, root,handle_determine_chord,handle_to_main_menu):
        self._frame = None
        self._root = root
        self._handle_determine_chord = handle_determine_chord
        self._handle_to_main_menu = handle_to_main_menu
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)
        
    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="Give 3 notes (for example 'C', 'E' and 'G')\nand I will tell you if that makes a chord")
        self.first_entry = ttk.Entry(master=self._root)
        self.second_entry = ttk.Entry(master=self._root)
        self.third_entry = ttk.Entry(master=self._root)


        button = ttk.Button(
            master=self._frame,
            text="Enter",
            command=self._handle_determine_chord
        )
        
        return_button = ttk.Button(
            master=self._frame,
            text="Return to main menu",
            command=self._handle_to_main_menu
        )
        

        label.pack()
        self.first_entry.pack()
        self.second_entry.pack()
        self.third_entry.pack()
        button.pack()
        return_button.pack()

    
    def get_first_entry(self):
        return self.first_entry.get()

    def get_second_entry(self):
        return self.second_entry.get()
    
    def get_third_entry(self):
        return self.third_entry.get()