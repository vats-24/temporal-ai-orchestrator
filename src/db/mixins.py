import uuid

from datetime import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import UUID

class TimeStampMixin:
    created_at = mapped_column(
        DateTime,
        default=datetime.now()
    )

    updated_at = mapped_column(
        DateTime,
        default=datetime.now(),
        onupdate=datetime.now()
    )

class UUIDMixin:
    id = mapped_column(
        UUID(as_uuid=True),
    primary_key=True,
    default=uuid.uuid4
    )