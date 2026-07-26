from sqlalchemy import String
from sqlalchemy.orm import mapped_column


from src.db.base import Base
from src.db.mixins import (TimeStampMixin, UUIDMixin)

class Tenant(Base, TimeStampMixin, UUIDMixin):
    __tablename__ = "tenants"

    name = mapped_column(
        String,
        nullable=False,
        unique=True,
    )