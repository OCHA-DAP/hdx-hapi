from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, column_property
from hapi_schema.db_food_security import view_params_food_security

from hdx_hapi.db.models.views.util.util import view
from hdx_hapi.db.models.base import Base


food_security_view = view(view_params_food_security.name, Base.metadata, view_params_food_security.selectable)


class FoodSecurityView(Base):
    __table__ = food_security_view
    
    id: Mapped[int] = column_property(food_security_view.c.id)
    resource_ref: Mapped[int] = column_property(food_security_view.c.resource_ref)
    admin2_ref: Mapped[int] = column_property(food_security_view.c.admin2_ref)
    
    ipc_phase_name: Mapped[str] = column_property(food_security_view.c.ipc_phase_name)
    ipc_phase_code: Mapped[str] = column_property(food_security_view.c.ipc_phase_code)
    ipc_type_code: Mapped[str] = column_property(food_security_view.c.ipc_type_code)
    population_in_phase: Mapped[int] = column_property(food_security_view.c.population_in_phase)
    population_fraction_in_phase: Mapped[float] = column_property(food_security_view.c.population_fraction_in_phase)

    reference_period_start: Mapped[DateTime] = column_property(food_security_view.c.reference_period_start)
    reference_period_end: Mapped[DateTime] = column_property(food_security_view.c.reference_period_end)
    source_data: Mapped[str] = column_property(food_security_view.c.source_data)

    resource_hdx_id: Mapped[str] = column_property(food_security_view.c.resource_hdx_id)
    resource_name: Mapped[str] = column_property(food_security_view.c.resource_name)
    resource_update_date = column_property(food_security_view.c.resource_update_date)

    dataset_hdx_id: Mapped[str] = column_property(food_security_view.c.dataset_hdx_id)
    dataset_hdx_stub: Mapped[str] = column_property(food_security_view.c.dataset_hdx_stub)
    dataset_title: Mapped[str] = column_property(food_security_view.c.dataset_title)
    dataset_hdx_provider_stub: Mapped[str] = column_property(food_security_view.c.dataset_hdx_provider_stub)
    dataset_hdx_provider_name: Mapped[str] = column_property(food_security_view.c.dataset_hdx_provider_name)

    location_code: Mapped[str] = column_property(food_security_view.c.location_code)
    location_name: Mapped[str] = column_property(food_security_view.c.location_name)

    admin1_code: Mapped[str] = column_property(food_security_view.c.admin1_code)
    admin1_name: Mapped[str] = column_property(food_security_view.c.admin1_name)
    admin1_is_unspecified: Mapped[bool] = column_property(food_security_view.c.admin1_is_unspecified)

    admin2_code: Mapped[str] = column_property(food_security_view.c.admin2_code)
    admin2_name: Mapped[str] = column_property(food_security_view.c.admin2_name)
    admin2_is_unspecified: Mapped[bool] = column_property(food_security_view.c.admin2_is_unspecified)