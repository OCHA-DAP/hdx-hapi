from sqlalchemy import Integer, String, DateTime, text
from sqlalchemy.orm import Mapped, mapped_column
from hdx_hapi.db.models.base import Base


class OrgView(Base):
    __tablename__ = 'org_view'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # hdx_link: Mapped[str] = mapped_column(String(1024), nullable=False)
    acronym: Mapped[str] = mapped_column(String(32), nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(512), nullable=False)
    org_type_code: Mapped[str] = mapped_column(String(32), nullable=False)
    reference_period_start: Mapped[DateTime] = mapped_column(DateTime, nullable=False, index=True)
    reference_period_end: Mapped[DateTime] = mapped_column(DateTime, nullable=True, server_default=text('NULL'))
    org_type_description: Mapped[str] = mapped_column(String(512), nullable=False)
