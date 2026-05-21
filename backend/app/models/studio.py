from datetime import datetime, timezone

from sqlalchemy import Index
from sqlmodel import Field, SQLModel


class Studios(SQLModel, table=True):
    __tablename__ = "studios"
    __table_args__ = (
        Index("ix_studios_slug", "slug"),
    )

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(unique=True, nullable=False, max_length=255)
    slug: str = Field(unique=True, nullable=False, max_length=255)
    founded: int | None = None
    website: str | None = Field(default=None, max_length=500)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    deleted_at: datetime | None = None
