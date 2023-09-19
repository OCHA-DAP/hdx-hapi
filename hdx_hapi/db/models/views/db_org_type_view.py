from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from hdx_hapi.db.models import Base


class OrgTypeView(Base):
    __tablename__ = 'org_type_view'

    code: Mapped[str] = mapped_column(String(32), primary_key=True)
    description: Mapped[str] = mapped_column(String(512), nullable=False)
