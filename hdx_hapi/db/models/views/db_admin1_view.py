from sqlalchemy import Boolean, Integer, String, DateTime, text
from sqlalchemy.orm import Mapped, mapped_column
from hdx_hapi.db.models.base import Base


class Admin1View(Base):
    __tablename__ = 'admin1_view'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    location_ref: Mapped[int] = mapped_column(Integer, nullable=False)
    code: Mapped[str] = mapped_column(String(128), nullable=False)
    name: Mapped[str] = mapped_column(String(512), nullable=False)
    is_unspecified: Mapped[bool] = mapped_column(Boolean, server_default=text('FALSE'))

    reference_period_start: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    reference_period_end: Mapped[DateTime] = mapped_column(DateTime, nullable=True, server_default=text('NULL'))

    location_code: Mapped[str] = mapped_column(String(128), nullable=False)
    location_name: Mapped[str] = mapped_column(String(512), nullable=False)
    location_reference_period_start: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    location_reference_period_end: Mapped[DateTime] = mapped_column(DateTime, nullable=True, server_default=text('NULL'))
