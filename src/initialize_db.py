from db_connection import database_connection, test_database_connection

def drop_tables(conn):
    cursor = conn.cursor()
    cursor.execute('drop table if exists users;')
    cursor.execute('drop table if exists passwords;')
    conn.commit()

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            username TEXT,
            password TEXT
    );''')
    conn.commit()

    cursor.execute('''
        CREATE TABLE passwords (
            password_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            username TEXT,
            password TEXT,
            site TEXT,
            user_id REFERENCES users (user_id)
        );''')
    conn.commit()

def insert_root(conn):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES ('root', 'root');")
    conn.commit()

def insert_passwords_for_root(conn):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO passwords (username, password, site, user_id)
        VALUES ('trolli', 'trolli', 'iltalehti.fi', 1);''')
    conn.commit()

    cursor.execute('''
        INSERT INTO passwords (username, password, site, user_id)
        VALUES ('jari', 'aarnio', 'www.pornhub.com', 1);''')
    conn.commit()

def initialize_db():
    conn = database_connection()
    test_conn = test_database_connection()

    drop_tables(conn)
    create_tables(conn)
    insert_root(conn)
    insert_passwords_for_root(conn)

    drop_tables(test_conn)
    create_tables(test_conn)

if __name__ == "__main__":
    initialize_db()
