from tkinter import Tk
from ui.ui import UI
from utils.file_database import FileDatabase


def main():
    window = Tk()
    window.geometry("1340x740")
    window.title("HTML editor")

    database = FileDatabase()
    database.set_up()
    all_files = database.get_all_files()
    five_newest_files = database.get_five_newest_files()

    ui_view = UI(window, all_files, five_newest_files)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
