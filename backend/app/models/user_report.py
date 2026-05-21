from datetime import datetime, timezone

from sqlalchemy import CheckConstraint, Index, UniqueConstraint
from sqlmodel import Field, SQLModel

from app.models.enums import ReportStatus, UserReportReason


class UserReport(SQLModel, table=True):
    __tablename__ = "user_reports"
    __table_args__ = (
        UniqueConstraint("reporter_id", "accused_id", name="uq_user_report"),
        CheckConstraint("reporter_id <> accused_id", name="ck_user_reports_no_self_report"),
        Index("ix_user_reports_status_created_at", "status", "created_at"),
        Index("ix_user_reports_accused_id", "accused_id"),
    )

    id: int | None = Field(default=None, primary_key=True)
    reporter_id: int = Field(foreign_key="users.id")
    accused_id: int = Field(foreign_key="users.id")
    reason: UserReportReason = Field(nullable=False)
    description: str | None = Field(default=None)
    status: ReportStatus = Field(default=ReportStatus.pending)
    admin_note: str | None = None
    resolved_by: int | None = Field(default=None, foreign_key="users.id")
    resolved_at: datetime | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
