# models/user.py

from . import get_connection

class User:
    @staticmethod
    def create(username, email, full_name):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO users (username, email, full_name)
                VALUES (?, ?, ?)
            ''', (username, email, full_name))
            conn.commit()

    @staticmethod
    def get_all():
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users')
            return cursor.fetchall()

    @staticmethod
    def find_by_username(username):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
            return cursor.fetchone()

    @staticmethod
    def delete_by_username(username):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM users WHERE username = ?', (username,))
            conn.commit()
