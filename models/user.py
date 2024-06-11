from . import get_connection

class User:
    @staticmethod
    def create(username, email, full_name):
        # Check if the username already exists
        existing_user = User.find_by_username(username)
        if existing_user:
            print("Username already exists. Please choose a different username.")
            return None  # Return None to indicate failure
        else:
            with get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO users (username, email, full_name)
                    VALUES (?, ?, ?)
                ''', (username, email, full_name))
                conn.commit()
                return cursor.lastrowid  # Return the ID of the inserted user

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
