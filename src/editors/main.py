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

    # Pylint's disable unused-argument is used because the event argument is required (otherwise it runs into an error), but we don't use it.
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
