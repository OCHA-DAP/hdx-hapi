from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, column_property

from hapi_schema.db_population_status import view_params_population_status

from hdx_hapi.db.models.views.util.util import view
from hdx_hapi.db.models.base import Base


population_status_view = view(view_params_population_status.name, Base.metadata, view_params_population_status.selectable)


class PopulationStatusView(Base):
    __table__ = population_status_view

    code: Mapped[str] = column_property(population_status_view.c.code)
    description: Mapped[str] = column_property(population_status_view.c.description)
