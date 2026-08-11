import re

from pydantic import EmailStr, field_validator
from sqlmodel import Field, SQLModel

from app.models.enums import User_Role, User_gender, User_status


class UserUpdate(SQLModel):
    username: str | None = Field(default=None, min_length=3, max_length=100)
    email: EmailStr | None = None
    password: str | None = Field(default=None, min_length=8, max_length=128)
    full_name: str | None = Field(default=None, max_length=150)
    description: str | None = Field(default=None, max_length=500)
    gender: User_gender | None = None
    role: User_Role | None = None
    status: User_status | None = None

    