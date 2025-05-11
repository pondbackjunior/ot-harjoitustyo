import tkinter as tk


class EditorMain:
    def __init__(self, root, textarea):
        self._root = root
        self._textarea = textarea

        # Keyboard shortcuts
        self._textarea.bind(
            "<Control-b>", lambda _: (self.insert_tag("b"), "break")[1])  # Bold
        self._textarea.bind(
            "<Control-i>", lambda _: (self.insert_tag("i"), "break")[1])  # Italic
        self._textarea.bind(
            "<Control-u>", lambda _: (self.insert_tag("u"), "break")[1])  # Underline
        self._textarea.bind("<Control-a>", lambda _: (
            self._textarea.tag_add("sel", "1.0", "end-1c"), "break")[1])  # Select all
        self._textarea.bind("<Control-z>", self.undo)  # Undo
        self._textarea.bind("<Control-Shift-Z>", self.redo)  # Redo
        self._textarea.bind("<Button-1>", lambda _: self._textarea.tag_remove(
            "highlight", "1.0", tk.END))  # Remove highlights from search
        # Auto indent on Enter
        self._textarea.bind("<Return>", self.auto_indent)

        # Configuring tags for styling
        self._textarea.tag_configure(
            "bold", font=("TkDefaultFont", 10, "bold"))
        self._textarea.tag_configure(
            "italic", font=("TkDefaultFont", 10, "italic"))
        self._textarea.tag_configure(
            "underline", font=("TkDefaultFont", 10, "underline"))
        self._textarea.tag_configure("dim", foreground="#AAAAAA")
        self._textarea.tag_configure("h1", font=("TkDefaultFont", 20, "bold"))
        self._textarea.tag_configure("h2", font=("TkDefaultFont", 18, "bold"))
        self._textarea.tag_configure("h3", font=("TkDefaultFont", 16, "bold"))
        self._textarea.tag_configure("h4", font=("TkDefaultFont", 14, "bold"))
        self._textarea.tag_configure("h5", font=("TkDefaultFont", 12, "bold"))
        self._textarea.tag_configure("highlight", background="yellow")

    def insert_tag(self, tag):
        """
        Inserts an html tag around the selected text.
        If there is no selected text, it inserts the tag at the cursor's position.
        """
        self._textarea.focus_set()
        try:
            start = self._textarea.index("sel.first")
            end = self._textarea.index("sel.last")
            selection = self._textarea.get(start, end)

            self._textarea.delete(start, end)
            self._textarea.insert(start, f"<{tag}>{selection}</{tag}>")
        except tk.TclError:
            # There was no selected text, so we simply enter the tags.
            # In this case, we also place the cursor between the tags.
            cursor = self._textarea.index("insert")
            self._textarea.insert(cursor, f"<{tag}></{tag}>")

            cursor_index = f'{cursor}+{len(f"<{tag}>")}c'
            self._textarea.mark_set("insert", cursor_index)

    def undo(self, event=None):  # pylint: disable=unused-argument
        try:
            self._textarea.edit_undo()
        except tk.TclError:
            pass
        return "break"

    def redo(self, event=None):  # pylint: disable=unused-argument
        try:
            self._textarea.edit_redo()
        except tk.TclError:
            pass
        return "break"

    def search(self, search_term):
        """
        Searches for a term in the textarea and highlights all occurrences.
        If the term is empty, it removes all highlights.
        """
        self._textarea.tag_remove("highlight", "1.0", tk.END)
        if not search_term:
            return

        start = "1.0"
        while True:
            pos = self._textarea.search(search_term, start, stopindex=tk.END)
            if not pos:
                break
            end = f"{pos}+{len(search_term)}c"
            self._textarea.tag_add("highlight", pos, end)
            start = end

    def replace_one(self, search_term, replace_term):
        """
        Replaces the first occurrence of a search term with a replacement term.
        If the search term is empty, it does nothing.
        """
        if not search_term:
            return

        pos = self._textarea.search(search_term, "1.0", stopindex=tk.END)
        if pos:
            end = f"{pos}+{len(search_term)}c"
            self._textarea.delete(pos, end)
            self._textarea.insert(pos, replace_term)

    def replace_all(self, search_term, replace_term):
        """
        Replaces all occurrences of a search term with a replacement term.
        If the search term is empty, it does nothing.
        """
        self._textarea.tag_remove("highlight", "1.0", tk.END)
        if not search_term:
            return

        start = "1.0"
        while True:
            pos = self._textarea.search(search_term, start, stopindex=tk.END)
            if not pos:
                break
            end = f"{pos}+{len(search_term)}c"
            self._textarea.delete(pos, end)
            self._textarea.insert(pos, replace_term)

    def auto_indent(self, event=None):  # pylint: disable=unused-argument
        """
        Automatically indents the new line based on the indentation of the current line.
        """
        line_index = self._textarea.index("insert linestart")
        current_line = self._textarea.get(line_index, f"{line_index} lineend")

        indent = ""
        for char in current_line:
            if char in (" ", "\t"):
                indent += char
            else:
                break

        self._textarea.insert("insert", f"\n{indent}")
        return "break"
