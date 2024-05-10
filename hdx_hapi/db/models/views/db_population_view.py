from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, column_property
from hapi_schema.db_population import view_params_population

from hdx_hapi.db.models.views.util.util import view
from hdx_hapi.db.models.base import Base


population_view = view(view_params_population.name, Base.metadata, view_params_population.selectable)


class PopulationView(Base):
    __table__ = population_view

    id: Mapped[int] = column_property(population_view.c.id)
    resource_ref: Mapped[int] = column_property(population_view.c.resource_ref)
    admin2_ref: Mapped[int] = column_property(population_view.c.admin2_ref)
    gender_code: Mapped[str] = column_property(population_view.c.gender_code)
    age_range_code: Mapped[str] = column_property(population_view.c.age_range_code)

    population: Mapped[int] = column_property(population_view.c.population)
    reference_period_start: Mapped[DateTime] = column_property(population_view.c.reference_period_start)
    reference_period_end: Mapped[DateTime] = column_property(population_view.c.reference_period_end)
    source_data: Mapped[str] = column_property(population_view.c.source_data)

    resource_hdx_id: Mapped[str] = column_property(population_view.c.resource_hdx_id)
    resource_name: Mapped[str] = column_property(population_view.c.resource_name)
    resource_update_date = column_property(population_view.c.resource_update_date)
    hapi_updated_date: Mapped[DateTime] = column_property(population_view.c.hapi_updated_date)
    hapi_replaced_date: Mapped[DateTime] = column_property(population_view.c.hapi_replaced_date)

    dataset_hdx_id: Mapped[str] = column_property(population_view.c.dataset_hdx_id)
    dataset_hdx_stub: Mapped[str] = column_property(population_view.c.dataset_hdx_stub)
    dataset_title: Mapped[str] = column_property(population_view.c.dataset_title)
    dataset_hdx_provider_stub: Mapped[str] = column_property(population_view.c.dataset_hdx_provider_stub)
    dataset_hdx_provider_name: Mapped[str] = column_property(population_view.c.dataset_hdx_provider_name)

    location_code: Mapped[str] = column_property(population_view.c.location_code)
    location_name: Mapped[str] = column_property(population_view.c.location_name)

    admin1_code: Mapped[str] = column_property(population_view.c.admin1_code)
    admin1_name: Mapped[str] = column_property(population_view.c.admin1_name)
    admin1_is_unspecified: Mapped[bool] = column_property(population_view.c.admin1_is_unspecified)
    location_ref: Mapped[int] = column_property(population_view.c.location_ref)

    admin2_code: Mapped[str] = column_property(population_view.c.admin2_code)
    admin2_name: Mapped[str] = column_property(population_view.c.admin2_name)
    admin2_is_unspecified: Mapped[bool] = column_property(population_view.c.admin2_is_unspecified)
    admin1_ref: Mapped[int] = column_property(population_view.c.admin1_ref)
