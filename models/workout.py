from . import get_connection

class Workout:
    @staticmethod
    def create(user_id, date, type, duration, calories_burned):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO workouts (user_id, date, type, duration, calories_burned)
                VALUES (?, ?, ?, ?, ?)
            ''', (user_id, date, type, duration, calories_burned))
            conn.commit()

    @staticmethod
    def get_all():
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM workouts')
            return cursor.fetchall()

    @staticmethod
    def find_by_user_id(user_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM workouts WHERE user_id = ?', (user_id,))
            return cursor.fetchall()

    @staticmethod
    def delete_by_id(workout_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM workouts WHERE id = ?', (workout_id,))
            conn.commit()
