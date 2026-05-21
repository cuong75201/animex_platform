from datetime import time

from sqlmodel import Field, SQLModel

from app.models.enums import weekday as Weekday


class Schedules(SQLModel, table=True):
    __tablename__ = "schedules"

    id: int | None = Field(default=None, primary_key=True)
    anime_release_id: int = Field(foreign_key="anime_releases.id", nullable=False, unique=True)
    weekday: Weekday = Field(nullable=False)
    air_time: time = Field(nullable=False)
