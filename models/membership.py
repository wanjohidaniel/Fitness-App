# models/membership.py

from . import get_connection

class Membership:
    @staticmethod
    def get_all():
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM memberships')
            return cursor.fetchall()

    @staticmethod
    def find_by_user_id(user_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM memberships WHERE user_id = ?', (user_id,))
            return cursor.fetchone()
