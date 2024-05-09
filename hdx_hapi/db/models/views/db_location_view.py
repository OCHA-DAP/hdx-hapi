from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, column_property

from hapi_schema.db_location import view_params_location

from hdx_hapi.db.models.views.util.util import view
from hdx_hapi.db.models.base import Base


location_view = view(view_params_location.name, Base.metadata, view_params_location.selectable)


class LocationView(Base):
    __table__ = location_view

    id: Mapped[int] = column_property(location_view.c.id)
    code: Mapped[str] = column_property(location_view.c.code)
    name: Mapped[str] = column_property(location_view.c.name)

    reference_period_start: Mapped[DateTime] = column_property(location_view.c.reference_period_start)
    reference_period_end: Mapped[DateTime] = column_property(location_view.c.reference_period_end)
    hapi_updated_date: Mapped[DateTime] = column_property(location_view.c.hapi_updated_date)
    hapi_replaced_date: Mapped[DateTime] = column_property(location_view.c.hapi_replaced_date)