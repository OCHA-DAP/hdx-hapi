from sqlalchemy import Boolean, Integer, String, DateTime, Text, text
from sqlalchemy.orm import Mapped, mapped_column
from hdx_hapi.db.models.base import Base


class PopulationView(Base):
    __tablename__ = 'population_view'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    resource_ref: Mapped[int] = mapped_column(Integer, nullable=False)
    admin2_ref: Mapped[int] = mapped_column(Integer, nullable=False)
    gender_code: Mapped[str] = mapped_column(String(1), nullable=True)
    age_range_code: Mapped[str] = mapped_column(String(32), nullable=True)
    population: Mapped[int] = mapped_column(Integer, nullable=False, index=True)
    reference_period_start: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    reference_period_end: Mapped[DateTime] = mapped_column(DateTime, nullable=True, server_default=text('NULL'))
    source_data: Mapped[str] = mapped_column(Text, nullable=True)

    resource_hdx_id: Mapped[str] = mapped_column(String(36), nullable=False)
    resource_name: Mapped[str] = mapped_column(String(256), nullable=False)
    resource_update_date = mapped_column(DateTime, nullable=False)

    dataset_hdx_id: Mapped[str] = mapped_column(String(36), unique=True, nullable=False)
    dataset_hdx_stub: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    dataset_title: Mapped[str] = mapped_column(String(1024), nullable=False)
    dataset_provider_code: Mapped[str] = mapped_column(String(128), nullable=False)
    dataset_provider_name: Mapped[str] = mapped_column(String(512), nullable=False)

    location_code: Mapped[str] = mapped_column(String(128), nullable=False)
    location_name: Mapped[str] = mapped_column(String(512), nullable=False)

    admin1_code: Mapped[str] = mapped_column(String(128), nullable=False)
    admin1_name: Mapped[str] = mapped_column(String(512), nullable=False)
    admin1_is_unspecified: Mapped[bool] = mapped_column(Boolean, server_default=text('FALSE'))

    admin2_code: Mapped[str] = mapped_column(String(128), nullable=False)
    admin2_name: Mapped[str] = mapped_column(String(512), nullable=False)
    admin2_is_unspecified: Mapped[bool] = mapped_column(Boolean, server_default=text('FALSE'))