from sqlalchemy import (
    String,
    ForeignKey,
)

from sqlalchemy.orm import mapped_column    

from src.db.base import Base
from src.db.mixins import (
    UUIDMixin,
    TimeStampMixin,
)

class AuditLog(Base, TimeStampMixin, UUIDMixin):
    __tablename__ = "audit_logs"

    tenant_id = mapped_column(
        ForeignKey("tenants.id"),
        nullable=False,
    )


    actor_id = mapped_column(
        ForeignKey("users.id"),
        nullable=True
    )

    action = mapped_column(
        String,
        nullable=False
    )

    resource_type = mapped_column(
        String,
        nullable=False
    )

    resource_id = mapped_column(
        String,
        nullable=False
    )

    correlation_id = mapped_column(
        String,
        nullable=True
    )