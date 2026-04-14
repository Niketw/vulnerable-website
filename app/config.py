"""
Application configuration and constants.
"""

import os

DATABASE = "students.db"
UPLOAD_DIR = "uploads"
LOG_FILE = "app.log"

os.makedirs(UPLOAD_DIR, exist_ok=True)
