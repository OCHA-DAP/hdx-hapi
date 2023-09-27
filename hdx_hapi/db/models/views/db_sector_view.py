from sqlalchemy import String, DateTime, text
from sqlalchemy.orm import Mapped, mapped_column
from hdx_hapi.db.models.base import Base


class SectorView(Base):
    __tablename__ = 'sector_view'

    code: Mapped[str] = mapped_column(String(32), primary_key=True)
    name: Mapped[str] = mapped_column(String(512), nullable=False, index=True)
    reference_period_start: Mapped[DateTime] = mapped_column(DateTime, nullable=False, index=True)
    reference_period_end: Mapped[DateTime] = mapped_column(DateTime, nullable=True, server_default=text('NULL'))
