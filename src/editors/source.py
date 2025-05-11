import tkinter as tk
import re
from editors.visual import TAGS


class SourceEditor:
    def __init__(self, root, textarea):
        self._root = root
        self._textarea = textarea

        # Configuring tags for syntax highlighting
        self._textarea.tag_configure(
            "tag_bracket", foreground="#6969e0")
        self._textarea.tag_configure(
            "tag_name", foreground="#0000FF")

    def on_key_release(self, event=None):  # pylint: disable=unused-argument
        """Called when a key is released. Updates the syntax highlighting"""
        html = self._textarea.get("1.0", "end-1c")
        self.highlight_syntax(html)

    def highlight_syntax(self, html):
        """
        Highlights the syntax of the HTML in the textarea by applying tags to the text.
        First it removes all previous tags and then applies new ones based on the HTML content.
        """
        for tag in TAGS:
            self._textarea.tag_remove(tag, "1.0", tk.END)

        pattern = re.finditer(r"(</?!?([a-zA-Z0-9]+)([^<>]*)>)|([^<>]+)", html)
        index = 0

        for match in pattern:
            full_tag, tag_name, _, text = match.groups()
            # Third one would be the attributes, but we don't consider them

            if full_tag:
                bracket_start = f"1.0 + {index} chars"
                bracket_end = f"1.0 + {index + 1} chars"
                self._textarea.tag_add(
                    "tag_bracket", bracket_start, bracket_end)

                tagname_start = f"1.0 + {index + 1} chars"
                tagname_end = f"1.0 + {index + 1 + len(tag_name)} chars"
                self._textarea.tag_add("tag_name", tagname_start, tagname_end)

                rest_end = f"1.0 + {index + len(full_tag) - 1} chars"
                self._textarea.tag_add("tag_bracket", tagname_end, rest_end)

                closing = f"1.0 + {index + len(full_tag) - 1} chars"
                closing_end = f"1.0 + {index + len(full_tag)} chars"
                self._textarea.tag_add("tag_bracket", closing, closing_end)

                index += len(full_tag)

            elif text:
                index += len(text)
