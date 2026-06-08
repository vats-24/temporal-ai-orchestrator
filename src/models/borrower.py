from sqlalchemy import (
    String,
    Float,
    ForeignKey,
)

from sqlalchemy.orm import mapped_column

from src.db.base import Base
from src.db.mixins import (
    TimestampMixin,
    UUIDMixin,
)

class Borrower(Base,TimestampMixin, UUIDMixin):
    __tablename__ = "borrowers"

    full_name = mapped_column(
        String,
        nullable=False
    )

    phone = mapped_column(
        String,
        nullable=False
    )

    loan_amount = mapped_column(
        Float,
        nullable=False
    )

    tenant_id = mapped_column(
        ForeignKey("tenants.id"),
        nullable=False
    )