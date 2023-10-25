"""Resource table."""

from hdx_hapi.db.models.base import Base
from sqlalchemy import (
    Boolean,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from hdx_hapi.db.models.db_dataset import DBDataset  # noqa: F401


class DBResource(Base):
    __tablename__ = "resource"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    dataset_ref: Mapped[int] = mapped_column(
        ForeignKey("dataset.id", onupdate="CASCADE", ondelete="CASCADE"),
        nullable=False,
    )
    hdx_id: Mapped[str] = mapped_column(
        String(36), unique=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(256), nullable=False)
    format: Mapped[str] = mapped_column(String(32), nullable=False)
    update_date = mapped_column(DateTime, nullable=False, index=True)
    download_url: Mapped[str] = mapped_column(
        String(1024), nullable=False, unique=True
    )
    is_hxl: Mapped[bool] = mapped_column(Boolean, nullable=False, index=True)

    dataset = relationship("DBDataset")
