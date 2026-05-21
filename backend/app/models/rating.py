from datetime import datetime, timezone

from sqlalchemy import CheckConstraint, Index
from sqlmodel import Field, SQLModel

from app.models.enums import Review_status


class Reviews(SQLModel, table=True):
    __tablename__ = "reviews"
    __table_args__ = (
        CheckConstraint("score BETWEEN 1 AND 5", name="ck_reviews_score_between_1_and_5"),
        Index("ix_reviews_series_status_created_at", "series_id", "status", "created_at"),
        Index("ix_reviews_user_id", "user_id"),
    )

    user_id: int = Field(foreign_key="users.id", primary_key=True)
    series_id: int = Field(foreign_key="anime_series.id", primary_key=True)
    score: int = Field(nullable=False)
    content: str | None = None
    status: Review_status = Field(default=Review_status.visible, nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    hidden_at: datetime | None = None
    moderated_by: int | None = Field(default=None, foreign_key="users.id")


Ratings = Reviews
