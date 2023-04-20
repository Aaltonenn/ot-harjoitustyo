from tkinter import Tk, ttk, constants

class NoteGiver:
    def __init__(self, root,chill):
        print("täällä käytiin")
        self._frame = None
        self._root = root
        self.chill = chill
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        label = ttk.Label(master=self._frame, text="in note giver ui")
        self._entry = ttk.Entry(master=self._root)

        button = ttk.Button(
            master=self._frame,
            text="call chillutellen",
            command=self.chill
        )
        

        label.grid(row=0, column=0)
        button.grid(row=1, column=0)


