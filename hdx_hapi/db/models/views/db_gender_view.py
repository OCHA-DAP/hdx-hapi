from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from hdx_hapi.db.models import Base


class GenderView(Base):
    __tablename__ = 'gender_view'

    code: Mapped[str] = mapped_column(String(1), primary_key=True)
    description: Mapped[str] = mapped_column(String(256), nullable=False)
