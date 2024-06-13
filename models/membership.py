# models/membership.py

from . import get_connection

class Membership:
    @staticmethod
    def create_table():
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS memberships (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    plan TEXT,
                    start_date TEXT,
                    end_date TEXT,
                    FOREIGN KEY (user_id) REFERENCES users (id)
                )
            ''')
            conn.commit()

    @staticmethod
    def create(user_id, plan, start_date, end_date):
        Membership.create_table()  # Ensure the table exists
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO memberships (user_id, plan, start_date, end_date)
                VALUES (?, ?, ?, ?)
            ''', (user_id, plan, start_date, end_date))
            conn.commit()

    @staticmethod
    def get_all():
        Membership.create_table()  # Ensure the table exists
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM memberships')
            return cursor.fetchall()

    @staticmethod
    def find_by_user_id(user_id):
        Membership.create_table()  # Ensure the table exists
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM memberships WHERE user_id = ?', (user_id,))
            return cursor.fetchone()

    @staticmethod
    def delete_by_user_id(user_id):
        Membership.create_table()  # Ensure the table exists
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM memberships WHERE user_id = ?', (user_id,))
            conn.commit()

    @staticmethod
    def update(membership_id, plan=None, start_date=None, end_date=None):
        with get_connection() as conn:
            cursor = conn.cursor()
            if plan:
                cursor.execute('UPDATE memberships SET plan = ? WHERE id = ?', (plan, membership_id))
            if start_date:
                cursor.execute('UPDATE memberships SET start_date = ? WHERE id = ?', (start_date, membership_id))
            if end_date:
                cursor.execute('UPDATE memberships SET end_date = ? WHERE id = ?', (end_date, membership_id))
            conn.commit()

