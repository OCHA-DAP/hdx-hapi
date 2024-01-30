from sqlalchemy.orm import Mapped, column_property

from hapi_schema.db_gender import view_params_gender

from hdx_hapi.db.models.views.util.util import view
from hdx_hapi.db.models.base import Base


gender_view = view(view_params_gender.name, Base.metadata, view_params_gender.selectable)


class GenderView(Base):
    __table__ = gender_view

    code: Mapped[str] = column_property(gender_view.c.code)
    description: Mapped[str] = column_property(gender_view.c.description)
