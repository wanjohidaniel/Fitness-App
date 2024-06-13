# models/goal.py

from . import get_connection

class Goal:
    @staticmethod
    def create(user_id, description, target_date):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO goals (user_id, description, target_date)
                VALUES (?, ?, ?)
            ''', (user_id, description, target_date))
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def get_all():
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM goals')
            return cursor.fetchall()

    @staticmethod
    def find_by_user_id(user_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM goals WHERE user_id = ?', (user_id,))
            return cursor.fetchall()

    @staticmethod
    def find_by_id(goal_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM goals WHERE id = ?', (goal_id,))
            return cursor.fetchone()

    @staticmethod
    def delete_by_id(goal_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM goals WHERE id = ?', (goal_id,))
            conn.commit()

    @staticmethod
    def update(goal_id, description=None, target_date=None):
        with get_connection() as conn:
            cursor = conn.cursor()
            if description:
                cursor.execute('UPDATE goals SET description = ? WHERE id = ?', (description, goal_id))
            if target_date:
                cursor.execute('UPDATE goals SET target_date = ? WHERE id = ?', (target_date, goal_id))
            conn.commit()

