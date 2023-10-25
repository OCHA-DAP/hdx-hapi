from sqlalchemy import Boolean, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from hdx_hapi.db.models.base import Base


class DatasetView(Base):
    __tablename__ = 'dataset_view'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    hdx_id: Mapped[str] = mapped_column(String(36), unique=True, nullable=False)
    hdx_stub: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    title: Mapped[str] = mapped_column(String(1024), nullable=False)
    hdx_provider_stub: Mapped[str] = mapped_column(String(128), nullable=False)
    hdx_provider_name: Mapped[str] = mapped_column(String(512), nullable=False)
