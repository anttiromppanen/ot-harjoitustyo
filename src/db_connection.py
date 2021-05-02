import sqlite3

conn = sqlite3.connect("db.py")
test_conn = sqlite3.connect("test_db.py")

def database_connection():
    return conn

def test_database_connection():
    return test_conn