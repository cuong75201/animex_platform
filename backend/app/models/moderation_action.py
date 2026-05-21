from datetime import datetime, timezone

from sqlalchemy import Index
from sqlmodel import Field, SQLModel

from app.models.enums import Moderation_action_type


class ModerationActions(SQLModel, table=True):
    __tablename__ = "moderation_actions"
    __table_args__ = (
        Index("ix_moderation_actions_moderator_created_at", "moderator_id", "created_at"),
        Index("ix_moderation_actions_target", "target_type", "target_id"),
    )

    id: int | None = Field(default=None, primary_key=True)
    moderator_id: int = Field(foreign_key="users.id", nullable=False)
    action_type: Moderation_action_type = Field(nullable=False)
    target_type: str = Field(nullable=False, max_length=50)
    target_id: int = Field(nullable=False)
    reason: str | None = None
    note: str | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
