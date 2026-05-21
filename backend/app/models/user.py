from datetime import datetime, timezone

from sqlalchemy import Index
from pydantic import EmailStr
from sqlmodel import Field, SQLModel

from app.models.enums import User_Role, User_gender, User_status


class User(SQLModel, table=True):
    __tablename__ = "users"
    __table_args__ = (
        Index("ix_users_email", "email"),
        Index("ix_users_username", "username"),
        Index("ix_users_status", "status"),
    )

    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True, nullable=False, max_length=100)
    email: EmailStr = Field(unique=True, nullable=False, max_length=255)
    password_hash: str = Field(nullable=False, max_length=255)
    gender: User_gender | None = None
    role: User_Role = Field(default=User_Role.user, nullable=False)
    status: User_status = Field(default=User_status.email_unverified, nullable=False)
    last_login_at: datetime | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    deleted_at: datetime | None = None
