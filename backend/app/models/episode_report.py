from datetime import datetime, timezone

from sqlalchemy import CheckConstraint, Index
from sqlmodel import Field, SQLModel

from app.models.enums import EpisodeReportReason, ReportStatus


class EpisodeReport(SQLModel, table=True):
    __tablename__ = "episode_reports"
    __table_args__ = (
        CheckConstraint(
            "playback_position_sec IS NULL OR playback_position_sec >= 0",
            name="ck_episode_reports_playback_position_non_negative",
        ),
        Index("ix_episode_reports_status_created_at", "status", "created_at"),
        Index("ix_episode_reports_episode_status_created_at", "episode_id", "status", "created_at"),
        Index("ix_episode_reports_reporter_episode_created_at", "reporter_id", "episode_id", "created_at"),
        Index("ix_episode_reports_reporter_created_at", "reporter_id", "created_at"),
    )

    id: int | None = Field(default=None, primary_key=True)
    reporter_id: int = Field(foreign_key="users.id")
    episode_id: int = Field(foreign_key="episodes.id")
    reason: EpisodeReportReason = Field(nullable=False)
    playback_position_sec: int | None = Field(default=None)
    description: str | None = Field(default=None)
    status: ReportStatus = Field(default=ReportStatus.pending)
    admin_note: str | None = None
    resolved_by: int | None = Field(default=None, foreign_key="users.id")
    resolved_at: datetime | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
