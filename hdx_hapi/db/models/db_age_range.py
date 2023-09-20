"""Resource table."""

from hdx_hapi.db.models.base import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class DBAgeRange(Base):
    __tablename__ = "age_range"

    code: Mapped[str] = mapped_column(String(32), primary_key=True)
    age_min: Mapped[int] = mapped_column(Integer, nullable=False)
    age_max: Mapped[int] = mapped_column(Integer, nullable=True)
