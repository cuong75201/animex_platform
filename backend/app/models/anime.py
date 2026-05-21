from datetime import datetime, timezone

from sqlalchemy import CheckConstraint, Index
from sqlmodel import Field, SQLModel

from app.models.enums import Anime_status, Content_access_type


class AnimeReleases(SQLModel, table=True):
    __tablename__ = "anime_releases"
    __table_args__ = (
        CheckConstraint("release_year IS NULL OR release_year >= 1900", name="ck_anime_releases_release_year"),
        Index("ix_anime_releases_slug", "slug"),
        Index("ix_anime_releases_series_id", "series_id"),
        Index("ix_anime_releases_broadcast_season_id", "broadcast_season_id"),
        Index("ix_anime_releases_status", "status"),
        Index("ix_anime_releases_access_type", "access_type"),
    )

    id: int | None = Field(default=None, primary_key=True)
    series_id: int = Field(foreign_key="anime_series.id", nullable=False)
    broadcast_season_id: int | None = Field(default=None, foreign_key="broadcast_seasons.id")
    release_title: str | None = Field(default=None, max_length=255)
    description: str | None = None
    slug: str = Field(unique=True, nullable=False, max_length=255)
    trailer_url: str | None = Field(default=None, max_length=500)
    release_year: int | None = None
    release_number: int | None = None
    release_type: str = Field(default="season", nullable=False, max_length=50)
    duration: int | None = None
    age_rating: str | None = Field(default=None, max_length=10)
    status: Anime_status = Field(default=Anime_status.upcoming, nullable=False)
    access_type: Content_access_type = Field(default=Content_access_type.free, nullable=False)
    total_episodes: int | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    deleted_at: datetime | None = None


Animes = AnimeReleases
