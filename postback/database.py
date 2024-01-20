import sqlite3

from config import DB_PATH


def create_tables_if_not_exist():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()

        # Создаём таблицу регистраций
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS one_win_registrations (
            one_win_id INTEGER PRIMARY KEY,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        '''
        cursor.execute(create_table_query)

        # Создаём таблицу депозитов
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS one_win_deposits (
            one_win_id INTEGER,
            amount FLOAT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        '''
        cursor.execute(create_table_query)

        conn.commit()


def save_registration(sub_id: int, one_win_id: int):
    with sqlite3.connect('имя_базы_данных.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO one_win_registrations VALUES (?, ?);', (sub_id, one_win_id))
        conn.commit()


def save_deposit(sub_id: int, one_win_id, amount: float):
    with sqlite3.connect('имя_базы_данных.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO one_win_deposits VALUES (?, ?, ?);', (sub_id, one_win_id, amount))
        conn.commit()
