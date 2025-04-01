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
    def test_open_file(self, mock_open_file, mock_dialog):
        self.file_handler.open_file()
        mock_open_file.assert_called_with("test.html", "r", encoding="utf-8")
        self.textarea.delete.assert_called_with("1.0", tk.END)
        self.textarea.insert.assert_called_with("1.0", "<h1>Hello world</h1>")