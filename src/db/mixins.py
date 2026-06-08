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
        
    )