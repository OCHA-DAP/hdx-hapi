"""OrgType table."""

from hdx_hapi.db.models import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column


class DBOrgType(Base):
    __tablename__ = "org_type"

    code: Mapped[str] = mapped_column(String(32), primary_key=True)
    description: Mapped[str] = mapped_column(String(512), nullable=False)
