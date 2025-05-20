import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("base.db")
        self.cursor = self.connection.cursor()

    def is_user_exists(self, user_id: int) -> bool:
        self.cursor.execute('SELECT 1 FROM user WHERE id = ?', (user_id,))
        return bool(self.cursor.fetchone())

    def add_user(self, user_id: int, username: str) -> bool:
        try:
            self.cursor.execute('''
                INSERT INTO user (id, username)
                VALUES (?, ?)
            ''', (user_id, username))
            self.connection.commit()
            return True
        except sqlite3.IntegrityError:
            return False