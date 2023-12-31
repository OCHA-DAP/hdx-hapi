"""Admin2 table."""
from datetime import datetime

from hdx_hapi.db.models.base import Base
from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from hdx_hapi.db.models.db_admin1 import DBAdmin1  # noqa: F401


class DBAdmin2(Base):
    __tablename__ = "admin2"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    admin1_ref: Mapped[int] = mapped_column(
        ForeignKey("admin1.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
    code: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(512), nullable=False)
    is_unspecified: Mapped[bool] = mapped_column(
        Boolean, server_default=text("FALSE")
    )
    reference_period_start: Mapped[datetime] = mapped_column(
        DateTime, nullable=False
    )
    reference_period_end: Mapped[datetime] = mapped_column(
        DateTime, nullable=True, server_default=text("NULL")
    )

    admin1 = relationship("DBAdmin1")
