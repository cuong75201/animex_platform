from datetime import datetime, timezone

from sqlalchemy import Index
from sqlmodel import Field, SQLModel

from app.models.enums import Notification_ref_type, Notification_type


class Notifications(SQLModel, table=True):
    __tablename__ = "notifications"
    __table_args__ = (
        Index("ix_notifications_user_read_created_at", "user_id", "is_read", "created_at"),
    )

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", nullable=False)
    type: Notification_type = Field(nullable=False)
    title: str | None = Field(default=None, max_length=255)
    content: str | None = None
    is_read: bool = Field(default=False)
    ref_type: Notification_ref_type | None = None
    ref_id: int | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    read_at: datetime | None = None
