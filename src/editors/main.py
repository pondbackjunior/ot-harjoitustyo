import tkinter as tk

class EditorMain:
    def __init__(self, root, textarea):
        self._root = root
        self._textarea = textarea

        # Keyboard shortcuts
        self._textarea.bind("<Control-b>", lambda _: self.insert_tag("b"))
        self._textarea.bind("<Control-i>", lambda _: self.insert_tag("i"))
        self._textarea.bind("<Control-u>", lambda _: self.insert_tag("u"))
        self._textarea.bind("<Control-a>", self.select_all)

    def insert_tag(self, tag):
        """Inserts an html tag around the selected text"""
        self._textarea.focus_set()
        try:
            start = self._textarea.index("sel.first")
            end = self._textarea.index("sel.last")
            selection = self._textarea.get(start, end)

            self._textarea.delete(start, end)
            self._textarea.insert(start, f"<{tag}>{selection}</{tag}>")
        except tk.TclError:
            # There was no selected text, so we simply enter the tags
            cursor = self._textarea.index("insert")
            self._textarea.insert(cursor, f"<{tag}></{tag}>")

    def select_all(self, event=None): # pylint: disable=unused-argument
        # event=None is required by tkinter, otherwise we get TypeError: EditorMain.select_all() takes 1 positional argument but 2 were given
        # Therefore we use pylint disable.
        self._textarea.tag_add("sel", "1.0", "end-1c")
        return "break"
    