import sqlite3

DB_PATH = "sales.db"

def get_connection():
    return sqlite3.connect(DB_PATH)
