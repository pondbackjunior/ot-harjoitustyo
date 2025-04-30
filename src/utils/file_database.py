import sqlite3
import os


class FileDatabase:
    def __init__(self):
        os.makedirs("src/data", exist_ok=True)
        self.conn = sqlite3.connect("src/data/files.db")

    def reset(self):
        cur = self.conn.cursor()
        cur.execute("DROP TABLE IF EXISTS Files")
        self.conn.commit()

    def set_up(self):
        cur = self.conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Files (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                content TEXT,
                full_path TEXT UNIQUE NOT NULL,
                modified_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def add_file(self, name, content, full_path):
        cur = self.conn.cursor()
        cur.execute("INSERT OR REPLACE INTO Files (name, content, full_path) VALUES (?, ?, ?)",
                    (name, content, full_path))
        self.conn.commit()

    def get_all_files(self, order_by="ORDER BY modified_at DESC"):
        cur = self.conn.cursor()
        cur.execute(f"SELECT * FROM Files {order_by}")
        return cur.fetchall()

    def get_five_newest_files(self):
        """Gets fives newest files to be used in the quick Open menu"""
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM Files ORDER BY modified_at DESC LIMIT 5")
        return cur.fetchall()
