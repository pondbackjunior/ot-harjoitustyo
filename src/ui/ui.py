import tkinter as tk
from tkinter import ttk
from utils.file_handler import FileHandler

class UI:
	def __init__(self, root):
		self._root = root
		self._textarea = tk.Text(master=self._root, wrap="word")
		self._file_handler = FileHandler(self._root, self._textarea)

	def start(self):
		open_file_button = ttk.Button(master=self._root, text="Open file", command=self._file_handler.open_file)
		new_file_button = ttk.Button(master=self._root, text="New file", command=self._file_handler.new_file)
		save_file_button = ttk.Button(master=self._root, text="Save file", command=self._file_handler.save_file)

		open_file_button.place(relx=0.3, rely=0.1, anchor="center")
		new_file_button.place(relx=0.5, rely=0.1, anchor="center")
		save_file_button.place(relx=0.7, rely=0.1, anchor="center")

		self._textarea.place(relx=0.5, rely=0.55, anchor="center", width=600, height=350)