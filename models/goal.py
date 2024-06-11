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
    def delete_by_id(goal_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM goals WHERE id = ?', (goal_id,))
            conn.commit()
