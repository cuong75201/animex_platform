from datetime import datetime, timezone
from decimal import Decimal

from sqlalchemy import CheckConstraint, Index, Numeric
from sqlmodel import Field, SQLModel

from app.models.enums import Plan_status


class MembershipPlans(SQLModel, table=True):
    __tablename__ = "membership_plans"
    __table_args__ = (
        CheckConstraint("price >= 0", name="ck_membership_plans_price_non_negative"),
        CheckConstraint("duration_days >= 0", name="ck_membership_plans_duration_non_negative"),
        Index("ix_membership_plans_status", "status"),
    )

    id: int | None = Field(default=None, primary_key=True)
    code: str = Field(unique=True, nullable=False, max_length=50)
    name: str = Field(unique=True, nullable=False, max_length=100)
    price: Decimal = Field(sa_type=Numeric(12, 2), nullable=False)
    duration_days: int = Field(nullable=False)
    description: str | None = None
    status: Plan_status = Field(default=Plan_status.active, nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
