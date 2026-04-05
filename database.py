# database.py — connection and query helpers
import sqlite3
import os

DB_PATH = os.environ.get("DB_PATH", "app.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def query(sql, params=()):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql, params)
    results = cursor.fetchall()
    conn.close()
    return results


def execute(sql, params=()):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql, params)
    conn.commit()
    conn.close()


def get_user_by_id(user_id):
    # Intentional SQL injection vulnerability for testing
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return cursor.fetchone()


def get_user_by_email(email):
    return query("SELECT * FROM users WHERE email = ?", (email,))
