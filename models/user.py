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
            return cursor.lastrowid

    @staticmethod
    def generate_unique_user_id():
        while True:
            user_id = random.randint(1000, 9999)
            if not User.find_by_id(user_id):
                return user_id

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
    def find_by_id(user_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
            return cursor.fetchone()

    @staticmethod
    def delete_by_username(username):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM users WHERE username = ?', (username,))
            conn.commit()

    @staticmethod
    def delete_by_id(user_id):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
            conn.commit()

    @staticmethod
    def update(user_id, email=None, full_name=None):
        with get_connection() as conn:
            cursor = conn.cursor()
            if email:
                cursor.execute('UPDATE users SET email = ? WHERE id = ?', (email, user_id))
            if full_name:
                cursor.execute('UPDATE users SET full_name = ? WHERE id = ?', (full_name, user_id))
            conn.commit()

