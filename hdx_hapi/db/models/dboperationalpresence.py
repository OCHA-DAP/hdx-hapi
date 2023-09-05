"""OperationalPresence table."""
from datetime import datetime

from hdx_hapi.db.models import Base
from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    Text,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from hdx_hapi.db.models.dbadmin2 import DBAdmin2  # noqa: F401
from hdx_hapi.db.models.dborg import DBOrg  # noqa: F401
from hdx_hapi.db.models.dbresource import DBResource  # noqa: F401
from hdx_hapi.db.models.dbsector import DBSector  # noqa: F401


class DBOperationalPresence(Base):
    __tablename__ = "operational_presence"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    resource_ref = mapped_column(
        ForeignKey("resource.id", onupdate="CASCADE", ondelete="CASCADE")
    )
    org_ref = mapped_column(ForeignKey("org.id", onupdate="CASCADE"))
    sector_code = mapped_column(ForeignKey("sector.code", onupdate="CASCADE"))
    admin2_ref: Mapped[int] = mapped_column(
        ForeignKey("admin2.id", onupdate="CASCADE")
    )
    reference_period_start: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, index=True
    )
    reference_period_end: Mapped[datetime] = mapped_column(
        DateTime, nullable=True, server_default=text("NULL")
    )
    source_data: Mapped[str] = mapped_column(Text)

    resource = relationship("DBResource")
    org = relationship("DBOrg")
    sector = relationship("DBSector")
    admin2 = relationship("DBAdmin2")
