from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, column_property

from hapi_schema.db_sector import view_params_sector

from hdx_hapi.db.models.views.util.util import view
from hdx_hapi.db.models.base import Base


sector_view = view(view_params_sector.name, Base.metadata, view_params_sector.selectable)


class SectorView(Base):
    __table__ = sector_view

    code: Mapped[str] = column_property(sector_view.c.code)
    name: Mapped[str] = column_property(sector_view.c.name)
