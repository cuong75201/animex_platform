from datetime import datetime, timezone

from sqlalchemy import Index
from sqlmodel import Field, SQLModel


class Favorites(SQLModel, table=True):
    __tablename__ = "favorites"
    __table_args__ = (
        Index("ix_favorites_user_created_at", "user_id", "created_at"),
        Index("ix_favorites_series_id", "series_id"),
    )

    user_id: int = Field(foreign_key="users.id", primary_key=True)
    series_id: int = Field(foreign_key="anime_series.id", primary_key=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
