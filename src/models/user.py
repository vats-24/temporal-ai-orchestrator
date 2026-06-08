from sqlalchemy import (
    String,
    ForeignKey,
)

from sqlalchemy.orm import mapped_column

from src.db.base import Base
from src.db.mixins import (
    UUIDMixin,
    TimestampMixin,
)

class User(Base, TimestampMixin, UUIDMixin):
    __tablename__ = "users"

    email = mapped_column(
        String,
        nullable=False,
        unique=True,
    )

    hashed_password = mapped_column(
        String,
        nullable=False,
    )

    role = mapped_column(
        String,
        nullable=False,
    )

    tenant_id = mapped_column(
        ForeignKey("tenants.id"),
        nullable=False,
    )