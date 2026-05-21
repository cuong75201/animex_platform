from datetime import datetime, timezone

from sqlalchemy import CheckConstraint, Index, UniqueConstraint
from sqlmodel import Field, SQLModel


class WatchHistory(SQLModel, table=True):
    __tablename__ = "watch_history"
    __table_args__ = (
        UniqueConstraint("user_id", "episode_id", name="uq_watch_history_user_episode"),
        CheckConstraint("progress_sec >= 0", name="ck_watch_history_progress_non_negative"),
        Index("ix_watch_history_user_watched_at", "user_id", "watched_at"),
        Index("ix_watch_history_episode_id", "episode_id"),
    )

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", nullable=False)
    episode_id: int = Field(foreign_key="episodes.id", nullable=False)
    progress_sec: int = Field(default=0)
    completed: bool = Field(default=False, nullable=False)
    watched_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
