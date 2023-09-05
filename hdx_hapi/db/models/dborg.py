"""Org table."""
from datetime import datetime

from hdx_hapi.db.models import Base
from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    String,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from hdx_hapi.db.models.dborgtype import DBOrgType

class DBOrg(Base):
    __tablename__ = "org"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    hdx_link: Mapped[str] = mapped_column(String(1024), nullable=False)
    acronym = mapped_column(String(32), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(512), nullable=False)
    org_type_code: Mapped[str] = mapped_column(
        ForeignKey("org_type.code", onupdate="CASCADE", ondelete="CASCADE")
    )
    reference_period_start: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, index=True
    )
    reference_period_end: Mapped[datetime] = mapped_column(
        DateTime, nullable=True, server_default=text("NULL")
    )

    org_type = relationship("DBOrgType")
