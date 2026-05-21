from datetime import datetime, timezone
from decimal import Decimal

from sqlalchemy import CheckConstraint, Index, Numeric
from sqlmodel import Field, SQLModel

from app.models.enums import Payment_method, Payment_status


class Payments(SQLModel, table=True):
    __tablename__ = "payments"
    __table_args__ = (
        CheckConstraint("amount >= 0", name="ck_payments_amount_non_negative"),
        Index("ix_payments_transaction_code", "transaction_code"),
        Index("ix_payments_gateway_event_id", "gateway_event_id"),
        Index("ix_payments_idempotency_key", "idempotency_key"),
        Index("ix_payments_user_status_created_at", "user_id", "status", "created_at"),
    )

    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id", nullable=False)
    plan_id: int | None = Field(default=None, foreign_key="membership_plans.id")
    transaction_code: str = Field(unique=True, nullable=False, max_length=100)
    gateway_event_id: str | None = Field(default=None, unique=True, max_length=150)
    idempotency_key: str | None = Field(default=None, unique=True, max_length=150)
    payment_method: Payment_method = Field(nullable=False)
    amount: Decimal = Field(sa_type=Numeric(12, 2), nullable=False)
    currency: str = Field(default="VND", nullable=False, max_length=3)
    status: Payment_status = Field(default=Payment_status.pending, nullable=False)
    provider_payload: str | None = None
    paid_at: datetime | None = None
    failed_at: datetime | None = None
    refunded_at: datetime | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
