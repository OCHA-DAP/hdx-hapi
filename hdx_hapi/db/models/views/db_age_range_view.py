from sqlalchemy.orm import column_property, Mapped
from hapi_schema.db_age_range import view_params_age_range
from hdx_hapi.db.models.views.util.util import view
from hdx_hapi.db.models.base import Base



age_range_view = view(view_params_age_range.name, Base.metadata, view_params_age_range.selectable)

class AgeRangeView(Base):
    __table__ = age_range_view

    code: Mapped[str] = column_property(age_range_view.c.code)
    age_min: Mapped[int] = column_property(age_range_view.c.age_min)
    age_max: Mapped[int] = column_property(age_range_view.c.age_max)