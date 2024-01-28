from sqlalchemy import Boolean, Integer, String, DateTime, text
from sqlalchemy.orm import column_property, Mapped

from hapi_schema.db_admin1 import view_params_admin1

from hdx_hapi.db.models.views.util.util import view
from hdx_hapi.db.models.base import Base


admin1_view = view(view_params_admin1.name, Base.metadata, view_params_admin1.selectable)

class Admin1View(Base):
    __table__ = admin1_view

    id: Mapped[int] = column_property(admin1_view.c.id)
    location_ref: Mapped[int] = column_property(admin1_view.c.location_ref)
    code: Mapped[str] = column_property(admin1_view.c.code)
    name: Mapped[str] = column_property(admin1_view.c.name)
    is_unspecified: Mapped[bool] = column_property(admin1_view.c.is_unspecified)

    reference_period_start: Mapped[DateTime] = column_property(admin1_view.c.reference_period_start)
    reference_period_end: Mapped[DateTime] = column_property(admin1_view.c.reference_period_end)

    location_code: Mapped[str] = column_property(admin1_view.c.location_code)
    location_name: Mapped[str] = column_property(admin1_view.c.location_name)
    location_reference_period_start: Mapped[DateTime] = column_property(admin1_view.c.location_reference_period_start)
    location_reference_period_end: Mapped[DateTime] = column_property(admin1_view.c.location_reference_period_end)
