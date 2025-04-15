import tkinter as tk
from tkinter import ttk
from utils.file_handler import FileHandler
from editors.main import EditorMain


class UI:
    def __init__(self, root, all_files, five_newest_files):
        self._root = root
        self._textarea = tk.Text(master=self._root, wrap="word", undo=True)
        self._file_handler = FileHandler(self._root, self._textarea)
        self._main_editor = EditorMain(self._root, self._textarea)
        self._edit_mode = tk.StringVar(value="source")
        self._all_files = all_files
        self._five_newest_files = five_newest_files

    def start(self):
        self.setup_buttons()
        self.setup_textarea()
        self.setup_toolbar()
        self.setup_style()
        self.switch_editor()

    def setup_buttons(self):
        """Sets up the top row buttons"""
        # Defines buttons
        open_file_button = ttk.Menubutton(
            master=self._root, text="Open...")
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

        # Place buttons
        open_file_button.place(relx=0.09, rely=0.1, anchor="center")
        new_file_button.place(relx=0.19, rely=0.1, anchor="center")
        save_file_button.place(relx=0.29, rely=0.1, anchor="center")
        self.source_button.place(relx=0.91, rely=0.1, anchor="center")
        self.visual_button.place(relx=0.81, rely=0.1, anchor="center")

        # Setup menu for the Open button
        open_menu = tk.Menu(open_file_button, tearoff=0)
        for file in self._five_newest_files:
            open_menu.add_command(
                label=file[1], command=lambda f=file[3]: self._file_handler.open_file(file=f))
        open_menu.add_command(label="All files...",
                              command=self.all_files_popup)
        open_menu.add_command(
            label="Select file...", command=lambda: self._file_handler.open_file(from_device=True))
        open_file_button["menu"] = open_menu

    def setup_textarea(self):
        self._textarea.place(relx=0.5, rely=0.55,
                             anchor="center", width=1200, height=590)

    def setup_toolbar(self):
        self.toolbar = ttk.Frame(self._root, width=65)
        self.toolbar.pack_propagate(False)
        ttk.Button(self.toolbar, text="𝐁", command=lambda: self._main_editor.insert_tag(
            "b")).pack(pady=2, fill="x")
        ttk.Button(self.toolbar, text="𝘐", command=lambda: self._main_editor.insert_tag(
            "i")).pack(pady=2, fill="x")
        ttk.Button(self.toolbar, text="𝐔", command=lambda: self._main_editor.insert_tag(
            "u")).pack(pady=2, fill="x")
        heading_button = ttk.Menubutton(self.toolbar, text="H.")
        heading_button.pack(pady=2, fill="x")

        heading_menu = tk.Menu(heading_button, tearoff=0)
        for i in range(1, 6):
            heading_menu.add_command(
                label=f"Heading {i}", command=lambda h=i: self._main_editor.insert_tag(f"h{h}"))
        heading_button["menu"] = heading_menu

    def setup_style(self):
        ttk.Style().configure("customsource.TButton", indicatoron=False)
        ttk.Style().configure("customvisual.TButton", indicatoron=False)

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

    def all_files_popup(self):
        """Sets up the popup for opening the list of all files"""
        popup = tk.Toplevel(self._root)
        popup.title("Select a file")
        popup.geometry("300x400")
        popup.resizable(False, False)
        popup.grab_set()

        listbox = tk.Listbox(popup)
        listbox.pack(fill="both", expand=True, padx=10, pady=10)

        for file in self._all_files:
            listbox.insert("end", file[1])

        # Double click to open
        listbox.bind("<Double-1>", lambda e: on_select())

        def on_select():
            index = listbox.curselection()
            if index:
                selected_file = self._all_files[index[0]]
                self._file_handler.open_file(file=selected_file[3])
                popup.destroy()
