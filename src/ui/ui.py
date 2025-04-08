import tkinter as tk
from tkinter import ttk
from utils.file_handler import FileHandler
from editors.main import EditorMain


class UI:
    def __init__(self, root):
        self._root = root
        self._textarea = tk.Text(master=self._root, wrap="word")
        self._file_handler = FileHandler(self._root, self._textarea)
        self._main_editor = EditorMain(self._root, self._textarea)
        self._edit_mode = tk.StringVar(value="source")

    def start(self):
        open_file_button = ttk.Button(
            master=self._root, text="Open", command=self._file_handler.open_file)
        new_file_button = ttk.Button(
            master=self._root, text="New file", command=self._file_handler.new_file)
        save_file_button = ttk.Button(
            master=self._root, text="Save", command=self._file_handler.save_file, style="info.TButton")
        self.source_button = ttk.Radiobutton(
            master=self._root, text="Source", value="source",
              variable=self._edit_mode, command=self.switch_editor,
              style="customsource.TButton")
        self.visual_button = ttk.Radiobutton(
            master=self._root, text="Visual", value="visual",
              variable=self._edit_mode, command=self.switch_editor,
              style="customvisual.TButton")

        open_file_button.place(relx=0.075, rely=0.1, anchor="center")
        new_file_button.place(relx=0.175, rely=0.1, anchor="center")
        save_file_button.place(relx=0.275, rely=0.1, anchor="center")
        self.source_button.place(relx=0.925, rely=0.1, anchor="center")
        self.visual_button.place(relx=0.825, rely=0.1, anchor="center")

        self._textarea.place(relx=0.5, rely=0.55,
                             anchor="center", width=1200, height=590)
        
        self.toolbar = ttk.Frame(self._root, width=30)
        self.toolbar.pack_propagate(False)
        ttk.Button(self.toolbar, text="𝐁", command=lambda: self._main_editor.insert_tag("b")).pack(pady=2, fill="x")
        ttk.Button(self.toolbar, text="𝘐", command=lambda: self._main_editor.insert_tag("i")).pack(pady=2, fill="x")
        ttk.Button(self.toolbar, text="𝐔", command=lambda: self._main_editor.insert_tag("u")).pack(pady=2, fill="x")
        ttk.Button(self.toolbar, text="H1", command=lambda: self._main_editor.insert_tag("h1")).pack(pady=2, fill="x")
        
        ttk.Style().configure("customsource.TButton", indicatoron=False)
        ttk.Style().configure("customvisual.TButton", indicatoron=False)
        self.switch_editor()
    
    def switch_editor(self):
        current = self._edit_mode.get()
        if current == "source":
            ttk.Style().configure("customsource.TButton", background="#b09646")
            ttk.Style().configure("customvisual.TButton", background="#e6c35a")
            self.toolbar.pack_forget()
        else:
            ttk.Style().configure("customvisual.TButton", background="#b09646")
            ttk.Style().configure("customsource.TButton", background="#e6c35a")
            self.toolbar.pack(side="left", fill="y", pady=100)
