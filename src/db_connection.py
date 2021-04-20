import sqlite3

conn = sqlite3.connect("db.py")

def database_connection():
    return conn
