from . import get_connection

class Workout:
    @staticmethod
    def create(user_id, type, duration, calories_burned, date):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO workouts (user_id, type, duration, calories_burned, date)
                VALUES (?, ?, ?, ?, ?)
            ''', (user_id, type, duration, calories_burned, date))
            conn.commit()
            return cursor.lastrowid

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
    def find_by_id(workout_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM workouts WHERE id = ?', (workout_id,))
            return cursor.fetchone()

    @staticmethod
    def delete_by_id(workout_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM workouts WHERE id = ?', (workout_id,))
            conn.commit()

    @staticmethod
    def update(workout_id, type=None, duration=None, calories_burned=None, date=None):
        with get_connection() as conn:
            cursor = conn.cursor()
            if type:
                cursor.execute('UPDATE workouts SET type = ? WHERE id = ?', (type, workout_id))
            if duration:
                cursor.execute('UPDATE workouts SET duration = ? WHERE id = ?', (duration, workout_id))
            if calories_burned:
                cursor.execute('UPDATE workouts SET calories_burned = ? WHERE id = ?', (calories_burned, workout_id))
            if date:
                cursor.execute('UPDATE workouts SET date = ? WHERE id = ?', (date, workout_id))
            conn.commit()
