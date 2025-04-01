import tkinter as tk
from tkinter import filedialog, messagebox

class FileHandler:
	def __init__(self, root, textarea):
		self._root = root
		self._textarea = textarea
		self._current_file = None

	def open_file(self):
		"""Opens an existing html file and places into textarea"""
		file = filedialog.askopenfilename(filetypes=[("HTML files", "*.html")])
		if file:
			self._current_file = file
			with open(file, "r", encoding="utf-8") as f:
				data = f.read()
			self._textarea.delete("1.0", tk.END)
			self._textarea.insert("1.0", data)

	def new_file(self):
		"""Erases content and resets file"""
		self._current_file = None
		self._textarea.delete("1.0", tk.END)

	def save_file(self):
		"""Saves the file into the device"""
		if self._current_file:
			# The file we're working with already exists, so we overwrite it
			with open(self._current_file, "w", encoding="utf-8") as file:
				file.write(self._textarea.get("1.0", tk.END))
			messagebox.showinfo("Success", "File saved.")
		else:
			# We don't have a file yet, so we create one
			file = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html")])
			if file:
				self._current_file = file
				self.save_file()