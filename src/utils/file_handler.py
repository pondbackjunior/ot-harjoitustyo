import tkinter as tk
from tkinter import filedialog, messagebox
from utils.file_database import FileDatabase


class FileHandler:
    def __init__(self, root, textarea):
        self._root = root
        self._textarea = textarea
        self._current_file = None
        self._database = FileDatabase()

        # Keyboard shortcuts
        self._textarea.bind(
            "<Control-o>", lambda _: (self.open_file(from_device=True), "break")[1])
        self._textarea.bind(
            "<Control-n>", lambda _: (self.new_file(), "break")[1])
        self._textarea.bind(
            "<Control-s>", lambda _: (self.save_file(), "break")[1])

    def open_file(self, file=None, from_device=False):
        """Opens an existing html file and places into textarea"""
        if from_device:
            file = filedialog.askopenfilename(
                filetypes=[("HTML files", "*.html")])
        if file:
            self._current_file = file
            with open(file, "r", encoding="utf-8") as f:
                data = f.read()
            self._textarea.delete("1.0", tk.END)
            self._textarea.insert("1.0", data)
            self._root.title(f"HTML editor - {file}")

    def new_file(self):
        """Erases content and resets file"""
        self._current_file = None
        self._textarea.delete("1.0", tk.END)
        self._root.title("HTML editor")

    def save_file(self):
        """Saves the file into the device"""
        if self._current_file:
            # The file we're working with already exists, so we overwrite it
            with open(self._current_file, "w", encoding="utf-8") as file:
                file.write(self._textarea.get("1.0", tk.END))
            # Save the file in the database
            file_name = self._current_file.split("/")[-1]
            file_content = self._textarea.get("1.0", tk.END)
            self._database.add_file(
                file_name, file_content, self._current_file)

            messagebox.showinfo("Success", "File saved.")
            self._root.title(f"HTML editor - {self._current_file}")
        else:
            # We don't have a file yet, so we create one
            file = filedialog.asksaveasfilename(defaultextension=".html",
                                                filetypes=[("HTML files", "*.html")])
            if file:
                self._current_file = file
                self.save_file()
