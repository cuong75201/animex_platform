from datetime import datetime, timezone

from sqlalchemy import CheckConstraint, Index, UniqueConstraint, text
from sqlmodel import Field, SQLModel

from app.models.enums import Membership_status


class UserMemberships(SQLModel, table=True):
    __tablename__ = "user_memberships"
    __table_args__ = (
        CheckConstraint("end_at > start_at", name="ck_user_memberships_end_after_start"),
        UniqueConstraint("payment_id", name="uq_user_memberships_payment_id"),
        Index("ix_user_memberships_user_status_end_at", "user_id", "status", "end_at"),
        Index("ix_user_memberships_payment_id", "payment_id"),
        Index(
            "uq_user_memberships_one_active_per_user",
            "user_id",
            unique=True,
            postgresql_where=text("status = 'active'"),
        ),
    )

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", nullable=False)
    plan_id: int = Field(foreign_key="membership_plans.id", nullable=False)
    payment_id: int | None = Field(default=None, foreign_key="payments.id")
    status: Membership_status = Field(default=Membership_status.pending, nullable=False)
    start_at: datetime = Field(nullable=False)
    end_at: datetime = Field(nullable=False)
    activated_at: datetime | None = None
    cancelled_at: datetime | None = None
    expired_at: datetime | None = None
    refunded_at: datetime | None = None
    auto_renew: bool = Field(default=False, nullable=False)
    cancel_at_period_end: bool = Field(default=False, nullable=False)
    grace_until: datetime | None = None
    renewed_from_id: int | None = Field(default=None, foreign_key="user_memberships.id")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
