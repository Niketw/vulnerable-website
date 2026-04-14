"""
Pydantic request/response models.
"""

from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str


class RoleUpdate(BaseModel):
    username: str
    role: str
