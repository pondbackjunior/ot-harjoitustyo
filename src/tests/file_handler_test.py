import unittest
from unittest.mock import patch, mock_open, MagicMock
import tkinter as tk
from utils.file_handler import FileHandler


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.textarea = MagicMock()
        self.file_handler = FileHandler(self.root, self.textarea)

    @patch("tkinter.filedialog.askopenfilename", return_value="test.html")
    @patch("builtins.open", new_callable=mock_open, read_data="<h1>Hello world</h1>")
    def test_open_file(self, mock_open_file, _):
        self.file_handler.open_file(from_device=True)
        mock_open_file.assert_called_with("test.html", "r", encoding="utf-8")
        self.textarea.delete.assert_called_with("1.0", tk.END)
        self.textarea.insert.assert_called_with("1.0", "<h1>Hello world</h1>")

    def test_new_file(self):
        self.file_handler._current_file = "test.html"
        self.file_handler.new_file()
        self.assertIsNone(self.file_handler._current_file)
        self.textarea.delete.assert_called_with("1.0", tk.END)

    @patch("tkinter.messagebox.showinfo")
    @patch("builtins.open", new_callable=mock_open)
    def test_save_file_override(self, mock_open_file, mock_messagebox):
        self.file_handler._current_file = "test.html"
        self.file_handler._textarea.get = MagicMock(
            return_value="<h1>Hello hello</h1>")
        self.file_handler.save_file()
        mock_open_file.assert_called_with("test.html", "w", encoding="utf-8")
        mock_open_file().write.assert_called_with("<h1>Hello hello</h1>")
        mock_messagebox.assert_called_with("Success", "File saved.")

    @patch("tkinter.filedialog.asksaveasfilename", return_value="test.html")
    @patch("tkinter.messagebox.showinfo")
    @patch("builtins.open", new_callable=mock_open)
    def test_save_file_createnew(self, mock_open_file, mock_messagebox, _):
        self.file_handler._current_file = None
        self.file_handler._textarea.get = MagicMock(
            return_value="<h1>Hello test</h1>")
        self.file_handler.save_file()
        mock_open_file.assert_called_with("test.html", "w", encoding="utf-8")
        mock_open_file().write.assert_called_with("<h1>Hello test</h1>")
        mock_messagebox.assert_called_with("Success", "File saved.")
