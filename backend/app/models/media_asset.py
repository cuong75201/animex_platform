from datetime import datetime, timezone

from sqlalchemy import BigInteger, CheckConstraint, Column, Index
from sqlmodel import Field, SQLModel

from app.models.enums import Media_purpose, Media_status


class MediaAssets(SQLModel, table=True):
    __tablename__ = "media_assets"
    __table_args__ = (
        CheckConstraint(
            "((CASE WHEN user_id IS NOT NULL THEN 1 ELSE 0 END) + "
            "(CASE WHEN series_id IS NOT NULL THEN 1 ELSE 0 END) + "
            "(CASE WHEN episode_id IS NOT NULL THEN 1 ELSE 0 END)) = 1",
            name="ck_media_assets_exactly_one_owner",
        ),
        CheckConstraint("width IS NULL OR width > 0", name="ck_media_assets_width_positive"),
        CheckConstraint("height IS NULL OR height > 0", name="ck_media_assets_height_positive"),
        CheckConstraint("size_bytes IS NULL OR size_bytes >= 0", name="ck_media_assets_size_non_negative"),
        Index("ix_media_assets_user_purpose", "user_id", "purpose", "status"),
        Index("ix_media_assets_series_purpose", "series_id", "purpose", "status"),
        Index("ix_media_assets_episode_purpose", "episode_id", "purpose", "status"),
        Index("ix_media_assets_storage_key", "storage_key"),
    )

    id: int | None = Field(default=None, primary_key=True)
    user_id: int | None = Field(default=None, foreign_key="users.id")
    series_id: int | None = Field(default=None, foreign_key="anime_series.id")
    episode_id: int | None = Field(default=None, foreign_key="episodes.id")
    purpose: Media_purpose = Field(nullable=False)
    storage_key: str = Field(nullable=False, unique=True, max_length=500)
    mime_type: str | None = Field(default=None, max_length=100)
    width: int | None = None
    height: int | None = None
    size_bytes: int | None = Field(default=None, sa_column=Column(BigInteger))
    alt_text: str | None = Field(default=None, max_length=255)
    status: Media_status = Field(default=Media_status.active, nullable=False)
    created_by: int | None = Field(default=None, foreign_key="users.id")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    deleted_at: datetime | None = None
