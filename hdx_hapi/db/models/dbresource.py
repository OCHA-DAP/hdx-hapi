"""Resource table."""

from hdx_hapi.db.models import Base
from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship


class DBResource(Base):
    __tablename__ = "resource"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    dataset_ref: Mapped[int] = mapped_column(
        ForeignKey("dataset.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
    code: Mapped[str] = mapped_column(String(128), nullable=False)
    filename: Mapped[str] = mapped_column(String(256), nullable=False)
    format: Mapped[str] = mapped_column(String(32), nullable=False)
    update_date = mapped_column(DateTime, nullable=False, index=True)
    is_hxl: Mapped[bool] = mapped_column(Boolean, nullable=False, index=True)

    dataset = relationship("DBDataset")
