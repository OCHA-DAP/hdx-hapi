"""Gender table."""

from hdx_hapi.db.models.base import Base
from sqlalchemy import CHAR, String
from sqlalchemy.orm import Mapped, mapped_column


class DBGender(Base):
    __tablename__ = "gender"

    code: Mapped[str] = mapped_column(CHAR(1), primary_key=True)
    description: Mapped[str] = mapped_column(String(256))
