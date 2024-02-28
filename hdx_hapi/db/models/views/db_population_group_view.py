from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, column_property

from hapi_schema.db_population_group import view_params_population_group

from hdx_hapi.db.models.views.util.util import view
from hdx_hapi.db.models.base import Base


population_group_view = view(view_params_population_group.name, Base.metadata, view_params_population_group.selectable)


class PopulationGroupView(Base):
    __table__ = population_group_view

    code: Mapped[str] = column_property(population_group_view.c.code)
    description: Mapped[str] = column_property(population_group_view.c.description)
