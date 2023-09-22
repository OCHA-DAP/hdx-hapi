from sqlalchemy import Boolean, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from hdx_hapi.db.models.base import Base


class OperationalPresenceView(Base):
    __tablename__ = 'operational_presence_view'
    # __table_args__ = {'autoload': True, 'autoload_with': 'your_engine'}

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    resource_ref: Mapped[int] = mapped_column(Integer)
    org_ref: Mapped[int] = mapped_column(Integer)
    sector_code: Mapped[str] = mapped_column(String(32))
    admin2_ref: Mapped[int] = mapped_column(Integer)
    reference_period_start: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    reference_period_end: Mapped[DateTime] = mapped_column(DateTime)
    source_data: Mapped[str] = mapped_column(String)

    # Additional fields from other tables in the view
    dataset_hdx_id: Mapped[str] = mapped_column(String(36), nullable=False)
    dataset_hdx_stub: Mapped[str] = mapped_column(String(128), nullable=False)
    dataset_title: Mapped[str] = mapped_column(String(1024), nullable=False)
    dataset_provider_code: Mapped[str] = mapped_column(String(128), nullable=False)
    dataset_provider_name: Mapped[str] = mapped_column(String(512), nullable=False)
    resource_hdx_id: Mapped[str] = mapped_column(String(36), nullable=False)
    resource_filename: Mapped[str] = mapped_column(String(256), nullable=False)
    resource_update_date: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    org_acronym: Mapped[str] = mapped_column(String(32), nullable=False)
    org_name: Mapped[str] = mapped_column(String(512), nullable=False)
    org_type_code: Mapped[str] = mapped_column(String(32), nullable=False)
    org_type_description: Mapped[str] = mapped_column(String(512), nullable=False)
    sector_name: Mapped[str] = mapped_column(String(512), nullable=False)
    location_code: Mapped[str] = mapped_column(String(128), nullable=False)
    location_name: Mapped[str] = mapped_column(String(512), nullable=False)
    admin1_code: Mapped[str] = mapped_column(String(128), nullable=False)
    admin1_name: Mapped[str] = mapped_column(String(512), nullable=False)
    admin1_is_unspecified: Mapped[bool] = mapped_column(Boolean, nullable=False)
    admin2_code: Mapped[str] = mapped_column(String(128), nullable=False)
    admin2_name: Mapped[str] = mapped_column(String(512), nullable=False)
    admin2_is_unspecified: Mapped[bool] = mapped_column(Boolean, nullable=False)
