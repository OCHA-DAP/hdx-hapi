"""Population table."""
from datetime import datetime

from hdx_hapi.db.models.base import Base
from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    Text,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from hdx_hapi.db.models.db_admin2 import DBAdmin2  # noqa: F401
from hdx_hapi.db.models.db_age_range import DBAgeRange  # noqa: F401
from hdx_hapi.db.models.db_gender import DBGender  # noqa: F401
from hdx_hapi.db.models.db_resource import DBResource  # noqa: F401


class DBPopulation(Base):
    __tablename__ = "population"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    resource_ref: Mapped[int] = mapped_column(
        ForeignKey("resource.id", onupdate="CASCADE", ondelete="CASCADE")
    )
    admin2_ref: Mapped[int] = mapped_column(
        ForeignKey("admin2.id", onupdate="CASCADE")
    )
    gender_code: Mapped[str] = mapped_column(
        ForeignKey("gender.code", onupdate="CASCADE")
    )
    age_range_code: Mapped[str] = mapped_column(
        ForeignKey("age_range.code", onupdate="CASCADE")
    )
    population: Mapped[int] = mapped_column(
        Integer, nullable=False, index=True
    )
    reference_period_start: Mapped[datetime] = mapped_column(
        DateTime, nullable=False
    )
    reference_period_end: Mapped[datetime] = mapped_column(
        DateTime, nullable=True, server_default=text("NULL")
    )
    source_data: Mapped[str] = mapped_column(Text)

    resource = relationship("DBResource")
    admin2 = relationship("DBAdmin2")
    age_range = relationship("DBAgeRange")
    gender = relationship("DBGender")
