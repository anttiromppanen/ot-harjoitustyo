from db_connection import database_connection, test_database_connection

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            username TEXT,
            password TEXT
    );''')
    conn.commit()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            password_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            username TEXT,
            password TEXT,
            site TEXT,
            user_id REFERENCES users (user_id)
        );''')
    conn.commit()

def initialize_db():
    conn = database_connection()
    test_conn = test_database_connection()

    create_tables(conn)
    create_tables(test_conn)

if __name__ == "__main__":
    initialize_db()
