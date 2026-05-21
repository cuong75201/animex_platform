from datetime import date, datetime, timezone

from sqlalchemy import Index
from sqlmodel import Field, SQLModel

from app.models.enums import Anime_status, Content_access_type


class AnimeSeries(SQLModel, table=True):
    __tablename__ = "anime_series"
    __table_args__ = (
        Index("ix_anime_series_title", "title"),
        Index("ix_anime_series_status", "status"),
        Index("ix_anime_series_access_type", "access_type"),
    )

    id: int | None = Field(default=None, primary_key=True)
    title: str = Field(nullable=False, max_length=255)
    title_other: str | None = Field(default=None, max_length=255)
    description: str | None = None
    status: Anime_status = Field(default=Anime_status.upcoming, nullable=False)
    age_rating: str | None = Field(default=None, max_length=10)
    access_type: Content_access_type = Field(default=Content_access_type.free, nullable=False)
    aired_from: date | None = None
    aired_to: date | None = None
    country: str | None = Field(default=None, max_length=100)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    deleted_at: datetime | None = None
    created_by: int | None = Field(default=None, foreign_key="users.id")
    updated_by: int | None = Field(default=None, foreign_key="users.id")
