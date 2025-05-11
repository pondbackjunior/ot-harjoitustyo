import tkinter as tk
import re

TAGS = {
    "bold": "b",
    "italic": "i",
    "underline": "u",
    "dim": "",
    "h1": "h1",
    "h2": "h2",
    "h3": "h3",
    "h4": "h4",
    "h5": "h5"
}


class VisualEditor:
    def __init__(self, root, textarea):
        self._root = root
        self._textarea = textarea

    def on_key_release(self, event=None):  # pylint: disable=unused-argument
        """Called when a key is released. Updates the visualization of the HTML."""
        html = self._textarea.get("1.0", "end-1c")
        self.visualize_html(html)

    def visualize_html(self, html):
        """
        Visualizes the HTML in the textarea by applying tags to the text.
        First it removes all previous tags and then applies new ones based on the HTML content.
        """
        for tag in TAGS:
            self._textarea.tag_remove(tag, "1.0", tk.END)

        pattern = re.finditer(r"(</?!?([a-zA-Z0-9]+\s?(.*?))>)|([^<>]+)", html)
        index = 0
        tag_stack = []

        for match in pattern:
            tag, tag_type, _, text = match.groups()

            if tag:
                tag_start = f"1.0 + {index} chars"
                tag_end = f"1.0 + {index + len(tag)} chars"
                self._textarea.tag_add("dim", tag_start, tag_end)

                if tag_type not in TAGS.values():
                    index += len(tag)
                    continue

                if not tag.startswith("</"):
                    tag_stack.append((tag_type, index + len(tag)))
                else:
                    for i in range(len(tag_stack) - 1, -1, -1):
                        if tag_stack[i][0] == tag_type:
                            _, open_pos = tag_stack.pop(i)
                            start = f"1.0 + {open_pos} chars"
                            end = f"1.0 + {index} chars"
                            for style, tag_name in TAGS.items():
                                if tag_type == tag_name:
                                    self._textarea.tag_add(style, start, end)
                                    break
                            break
                index += len(tag)
            elif text:
                index += len(text)
