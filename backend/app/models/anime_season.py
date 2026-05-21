from sqlalchemy import Index, UniqueConstraint
from sqlmodel import Field, SQLModel

from app.models.enums import Season_name


class BroadcastSeasons(SQLModel, table=True):
    __tablename__ = "broadcast_seasons"
    __table_args__ = (
        UniqueConstraint("name", "year", name="uq_broadcast_seasons_name_year"),
        Index("ix_broadcast_seasons_slug", "slug"),
    )

    id: int | None = Field(default=None, primary_key=True)
    name: Season_name = Field(nullable=False)
    year: int = Field(nullable=False)
    slug: str = Field(unique=True, nullable=False, max_length=100)


AnimeSeasons = BroadcastSeasons
