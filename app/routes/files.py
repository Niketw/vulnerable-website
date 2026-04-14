"""
File upload and download routes.
"""

import os
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse, HTMLResponse

from app.config import UPLOAD_DIR
from app.utils import log_event
from app.templates import upload_page, download_page

router = APIRouter()


# UPLOAD PAGE — serves HTML form
@router.get("/upload", response_class=HTMLResponse)
def upload_form():
    return upload_page()


# FILE UPLOAD — Insecure File Upload (CWE-434)
@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    CWE-434 — Insecure File Upload
    No validation of file extension, MIME type, or content.
    The file is saved directly to the uploads directory using shutil.
    An attacker could upload a malicious executable or web shell.
    """
    destination = os.path.join(UPLOAD_DIR, file.filename)

    with open(destination, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    log_event(f"File uploaded: {file.filename}")
    return {"message": f"File '{file.filename}' uploaded successfully"}


# DOWNLOAD PAGE — serves HTML form
@router.get("/download", response_class=HTMLResponse)
def download_form():
    return download_page()


# FILE DOWNLOAD — Path Traversal (CWE-22)
@router.get("/download/{filename:path}")
def download_file(filename: str):
    """
    CWE-22 — Path Traversal
    The filename from the URL is appended directly to the upload directory
    without sanitizing '../' sequences.  An attacker can read arbitrary
    files on the server, e.g.:
        GET /download/../../etc/passwd
    """
    filepath = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="File not found")

    log_event(f"File downloaded: {filename}")
    return FileResponse(filepath)
