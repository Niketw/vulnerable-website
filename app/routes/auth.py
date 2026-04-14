"""
Authentication routes.
"""

from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse

from app.database import get_db
from app.models import LoginRequest
from app.utils import log_event
from app.templates import login_page

router = APIRouter()


# LOGIN PAGE — serves HTML form
@router.get("/login", response_class=HTMLResponse)
def login_form():
    return login_page()


# LOGIN — SQL Injection (CWE-89) & Broken Authentication
@router.post("/login")
def login(creds: LoginRequest):
    """
    CWE-89 — SQL Injection
    The query is built via string concatenation, so input like:
        username: ' OR 1=1 --
        password: anything
    will bypass authentication entirely.

    Passwords are also compared in plain text (no hashing).
    """
    log_event(f"Login attempt for user: {creds.username}")

    conn = get_db()
    query = (
        "SELECT * FROM users WHERE username = '"
        + creds.username
        + "' AND password = '"
        + creds.password
        + "'"
    )
    user = conn.execute(query).fetchone()
    conn.close()

    if user:
        log_event(f"Login SUCCESS for user: {creds.username}")
        return {
            "message": "Login successful",
            "user": {
                "id": user["id"],
                "username": user["username"],
                "role": user["role"],
            },
        }

    log_event(f"Login FAILED for user: {creds.username}")
    raise HTTPException(status_code=401, detail="Invalid credentials")
