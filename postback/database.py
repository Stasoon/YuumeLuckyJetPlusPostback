import sqlite3
from datetime import datetime

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
            id INTEGER PRIMARY KEY,
            one_win_id INTEGER,
            amount FLOAT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        '''
        cursor.execute(create_table_query)

        conn.commit()


def save_registration(one_win_id: int):
    current_datetime = datetime.now()

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO one_win_registrations VALUES (?, ?);', (one_win_id, current_datetime))
        conn.commit()


def save_deposit(one_win_id, amount: float):
    current_datetime = datetime.now()

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO one_win_deposits (one_win_id, amount, timestamp) VALUES (?, ?, ?);',
            (one_win_id, amount, current_datetime)
        )
        conn.commit()
