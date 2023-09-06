from sqlalchemy import Boolean, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from hdx_hapi.db.models import Base


class DatasetView(Base):
    __tablename__ = 'dataset_view'
    # __table_args__ = {'autoload': True, 'autoload_with': 'your_engine'}
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str] = mapped_column(String(128), nullable=False)
    title: Mapped[str] = mapped_column(String(1024), nullable=False)
    provider_code: Mapped[str] = mapped_column(String(128), nullable=False)
    provider_name: Mapped[str] = mapped_column(String(512), nullable=False)
    hdx_link: Mapped[str] = mapped_column(String(512), nullable=False)
    api_link: Mapped[str] = mapped_column(String(1024), nullable=False)
