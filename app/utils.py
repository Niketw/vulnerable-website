"""
Utility / helper functions.
"""

from datetime import datetime

from app.config import LOG_FILE


def log_event(message: str):
    """
    CWE-117 — Log Injection
    User input is written directly into the log file with no sanitization.
    An attacker can inject newline characters to forge log entries.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
