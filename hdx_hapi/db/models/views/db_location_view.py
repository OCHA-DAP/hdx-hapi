from sqlalchemy import Boolean, Integer, String, DateTime, text
from sqlalchemy.orm import Mapped, mapped_column
from hdx_hapi.db.models.base import Base


class LocationView(Base):
    __tablename__ = 'location_view'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str] = mapped_column(String(128), nullable=False)
    name: Mapped[str] = mapped_column(String(512), nullable=False)

    reference_period_start: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    reference_period_end: Mapped[DateTime] = mapped_column(DateTime, nullable=True, server_default=text('NULL'))