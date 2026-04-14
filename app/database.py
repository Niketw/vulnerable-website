"""
Database initialization and connection helpers.
"""

import sqlite3

from app.config import DATABASE


def get_db():
    """Return a new database connection with Row factory."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """
    Create tables and seed default data.
    Passwords are stored in PLAIN TEXT (CWE-256) — intentional vulnerability.
    """
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'student'
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            full_name TEXT,
            email TEXT,
            grade TEXT
        )
    """)

    # Insert default users — passwords stored in PLAIN TEXT (CWE-256)
    try:
        cursor.execute(
            "INSERT INTO users (username, password, role) VALUES ('admin', 'admin123', 'admin')"
        )
        cursor.execute(
            "INSERT INTO users (username, password, role) VALUES ('student1', 'pass123', 'student')"
        )
        cursor.execute(
            "INSERT INTO student_data (username, full_name, email, grade) VALUES ('student1', 'Alice Johnson', 'alice@school.edu', 'A')"
        )
    except sqlite3.IntegrityError:
        pass  # Users already exist

    conn.commit()
    conn.close()
