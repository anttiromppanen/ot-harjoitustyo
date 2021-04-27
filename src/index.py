from tkinter import Tk
from ui.ui import UI
from initialize_db import initialize_db


def main():
    window = Tk()
    window.title("Zero salt rounds")
    window.geometry("1200x800")

    # remove when register is working
    initialize_db()

    ui = UI(window)
    ui.start()
    window.mainloop()


if __name__ == "__main__":
    main()
