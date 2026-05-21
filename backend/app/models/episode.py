from datetime import datetime, timezone

from sqlalchemy import BigInteger, CheckConstraint, Column, Index, UniqueConstraint
from sqlmodel import Field, SQLModel

from app.models.enums import Episode_access_type, Episode_status


class Episodes(SQLModel, table=True):
    __tablename__ = "episodes"
    __table_args__ = (
        UniqueConstraint("anime_release_id", "episode_num", name="uq_episodes_release_episode_num"),
        CheckConstraint("episode_num > 0", name="ck_episodes_episode_num_positive"),
        CheckConstraint("duration IS NULL OR duration >= 0", name="ck_episodes_duration_non_negative"),
        Index("ix_episodes_anime_release_id", "anime_release_id"),
        Index("ix_episodes_release_at", "release_at"),
        Index("ix_episodes_status", "status"),
        Index("ix_episodes_access_type", "access_type"),
    )

    id: int | None = Field(default=None, primary_key=True)
    anime_release_id: int = Field(nullable=False, foreign_key="anime_releases.id")
    episode_num: int = Field(nullable=False)
    title: str | None = Field(default=None, max_length=255)
    description: str | None = None
    video_key: str = Field(nullable=False, max_length=500)
    duration: int | None = None
    size_bytes: int | None = Field(default=None, sa_column=Column(BigInteger))
    release_at: datetime | None = None
    access_type: Episode_access_type = Field(default=Episode_access_type.inherit, nullable=False)
    status: Episode_status = Field(default=Episode_status.processing)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    deleted_at: datetime | None = None
