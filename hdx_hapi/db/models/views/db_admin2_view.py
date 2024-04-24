from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, column_property

from hapi_schema.db_admin2 import view_params_admin2
from hdx_hapi.db.models.views.util.util import view
from hdx_hapi.db.models.base import Base

admin2_view = view(view_params_admin2.name, Base.metadata, view_params_admin2.selectable)


class Admin2View(Base):
    __table__ = admin2_view

    id: Mapped[int] = column_property(admin2_view.c.id)
    admin1_ref: Mapped[int] = column_property(admin2_view.c.admin1_ref)
    code: Mapped[str] = column_property(admin2_view.c.code)
    name: Mapped[str] = column_property(admin2_view.c.name)
    is_unspecified: Mapped[bool] = column_property(admin2_view.c.is_unspecified)
    reference_period_start: Mapped[DateTime] = column_property(admin2_view.c.reference_period_start)
    reference_period_end: Mapped[DateTime] = column_property(admin2_view.c.reference_period_end)
    hapi_updated_date: Mapped[DateTime] = column_property(admin2_view.c.hapi_updated_date)
    hapi_replaced_date: Mapped[DateTime] = column_property(admin2_view.c.hapi_replaced_date)

    admin1_code: Mapped[str] = column_property(admin2_view.c.admin1_code)
    admin1_name: Mapped[str] = column_property(admin2_view.c.admin1_name)
    admin1_is_unspecified: Mapped[bool] = column_property(admin2_view.c.admin1_is_unspecified)
    admin1_reference_period_start: Mapped[DateTime] = column_property(admin2_view.c.admin1_reference_period_start)
    admin1_reference_period_end: Mapped[DateTime] = column_property(admin2_view.c.admin1_reference_period_end)

    location_code: Mapped[str] = column_property(admin2_view.c.location_code)
    location_name: Mapped[str] = column_property(admin2_view.c.location_name)
    location_reference_period_start: Mapped[DateTime] = column_property(admin2_view.c.location_reference_period_start)
    location_reference_period_end: Mapped[DateTime] = column_property(admin2_view.c.location_reference_period_end)
