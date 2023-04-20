from ui.gui_main_menu import UI_m
from tkinter import Tk,ttk,constants



class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self.show_gui_main_menu()

    def show_gui_main_menu(self):
        self.hide_current_view()
        self._current_view = UI_m(self._root)
        self._current_view.start()

    def hide_current_view(self):
        if self._current_view != None:
            pass
    



