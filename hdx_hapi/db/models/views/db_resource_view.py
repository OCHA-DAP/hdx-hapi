from sqlalchemy import Boolean, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from hdx_hapi.db.models.base import Base


class ResourceView(Base):
    __tablename__ = 'resource_view'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    dataset_ref: Mapped[int] = mapped_column(Integer, nullable=False)
    hdx_id: Mapped[str] = mapped_column(String(36), nullable=False)
    filename: Mapped[str] = mapped_column(String(256), nullable=False)
    format: Mapped[str] = mapped_column(String(32), nullable=False)
    update_date = mapped_column(DateTime, nullable=False)
    is_hxl: Mapped[bool] = mapped_column(Boolean, nullable=False)
    download_url: Mapped[str] = mapped_column(String(1024), nullable=False)

    dataset_hdx_id: Mapped[str] = mapped_column(String(36), nullable=False)
    dataset_hdx_stub: Mapped[str] = mapped_column(String(128), nullable=False)

    dataset_title: Mapped[str] = mapped_column(String(1024), nullable=False)
    dataset_provider_code: Mapped[str] = mapped_column(String(128), nullable=False)
    dataset_provider_name: Mapped[str] = mapped_column(String(512), nullable=False)
    