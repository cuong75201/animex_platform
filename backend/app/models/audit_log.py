from datetime import datetime, timezone

from sqlalchemy import Index
from sqlmodel import Field, SQLModel

from app.models.enums import Audit_action


class AuditLogs(SQLModel, table=True):
    __tablename__ = "audit_logs"
    __table_args__ = (
        Index("ix_audit_logs_actor_created_at", "actor_id", "created_at"),
        Index("ix_audit_logs_action_created_at", "action", "created_at"),
        Index("ix_audit_logs_target", "target_type", "target_id"),
    )

    id: int | None = Field(default=None, primary_key=True)
    actor_id: int | None = Field(default=None, foreign_key="users.id")
    action: Audit_action = Field(nullable=False)
    target_type: str | None = Field(default=None, max_length=50)
    target_id: int | None = None
    ip_address: str | None = Field(default=None, max_length=45)
    user_agent: str | None = Field(default=None, max_length=500)
    metadata_json: str | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
