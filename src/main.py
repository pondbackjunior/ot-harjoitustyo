from tkinter import Tk
from ui.ui import UI

def main():
    window = Tk()
    window.geometry("640x480")
    window.title("HTML editor")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()

if __name__ == "__main__":
    main()