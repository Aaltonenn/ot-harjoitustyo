from ui.gui_main_menu import GUI

class UI:
#luokka vastaa GRAAFISENkäyttöliittymän avaamisesta
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self.show_gui_main_menu()

    def show_gui_main_menu(self):
        self.hide_current_view()
        self._current_view = GUI(self._root)
        self._current_view.start()

    def hide_current_view(self):
        if self._current_view != None:
            pass
    



