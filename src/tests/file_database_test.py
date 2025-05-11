import unittest
import sqlite3
from time import sleep
import pytest
from utils.file_database import FileDatabase


class MemoryFileDatabase(FileDatabase):
    def __init__(self):
        super().__init__()
        self.conn = sqlite3.connect(":memory:")


class TestFileDatabase(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def setup_db(self, monkeypatch):
        # Override the FileDatabase to use an in-memory database
        class InMemoryFileDatabase(FileDatabase):
            def __init__(self):
                self.conn = sqlite3.connect(":memory:")

        self.db = InMemoryFileDatabase()
        self.db.set_up()
        yield
        self.db.conn.close()

    def test_add_file_and_get_all_files(self):
        self.db.add_file("Test", "text here", "/path/to/file.html")
        results = self.db.get_all_files()
        assert len(results) == 1
        assert results[0][1] == "Test"
        assert results[0][2] == "text here"
        assert results[0][3] == "/path/to/file.html"

    def test_add_file_replaces_existing(self):
        self.db.add_file("Test1", "Text A", "/path/to/file.html")
        self.db.add_file("Test2", "Text B", "/path/to/file.html")
        results = self.db.get_all_files()
        assert len(results) == 1
        assert results[0][1] == "Test2"
        assert results[0][2] == "Text B"

    def test_add_and_remove_file(self):
        self.db.add_file("Test1", "Text A", "/path/to/file.html")
        self.db.remove_file("/path/to/file.html")
        results = self.db.get_all_files()
        assert results == []

    def test_reset_drops_table(self):
        self.db.add_file("Test", "text here", "/path/to/file.html")
        self.db.reset()
        self.db.set_up()
        results = self.db.get_all_files()
        assert results == []

    def test_get_five_newest_files_above_limit(self):
        print("Wait 5s for loop...")
        for i in range(7):
            self.db.add_file(f"File{i}", f"Text {i}", f"/file{i}.html")
            sleep(1)  # Sleeping to get new timestamps

        newest = self.db.get_five_newest_files()
        assert len(newest) == 5
        names = [row[1] for row in newest]
        assert names == ["File6", "File5", "File4", "File3", "File2"]

    def test_get_five_newest_files_with_few_entries(self):
        self.db.add_file("testfile", "stuff", "/file.html")
        result = self.db.get_five_newest_files()
        assert len(result) == 1
        assert result[0][1] == "testfile"
