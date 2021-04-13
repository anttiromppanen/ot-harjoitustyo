from db_connection import database_connection

def drop_tables(conn):
    cursor = conn.cursor()
    cursor.execute('drop table if exists users;')
    conn.commit()

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE users (
        id integer primary key autoincrement not null,
        username text,
        password text
    );''')
    conn.commit()

def insert_root(conn):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES ('root', 'root');")
    conn.commit()

def initialize_db():
    conn = database_connection()

    drop_tables(conn)
    create_tables(conn)
    insert_root(conn)

if __name__ == "__main__":
    initialize_db()