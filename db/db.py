import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db/database.db")
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
        
    def set_user_subscribed(self, user_id: int) -> bool:
        try:
            self.cursor.execute(
                "UPDATE user SET status = ? WHERE id = ?",
                ("subscribed", user_id)
            )
            self.connection.commit()
            return self.cursor.rowcount > 0
        except sqlite3.Error:
            return False