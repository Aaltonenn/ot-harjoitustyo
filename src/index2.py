from tkinter import Tk
from ui.gui import UI


def main():
    window = Tk()
    window.title("Sointu ohjelma")
    ui_view = UI(window)
    ui_view.start()
    
    window.mainloop()


if __name__ == "__main__":
    main()