from sqlalchemy import (
    String,
    ForeignKey)

from sqlalchemy.orm import mapped_column

from src.db.base import Base
from src.db.mixins import (
    UUIDMixin,
    TimeStampMixin,
)

class WorkflowInstance(Base, TimeStampMixin, UUIDMixin): 
    __tablename__ = "workflow_instances"

    borrower_id = mapped_column(
        ForeignKey("borrowers.id"),
        nullable=False,
    )

    tenant_id = mapped_column(
        ForeignKey("tenants.id"),
        nullable=False
    )

    workflow_id = mapped_column(
        String,
        nullable=False,
        unique=True
    )

    current_state = mapped_column(
        String,
        nullable=False
    )