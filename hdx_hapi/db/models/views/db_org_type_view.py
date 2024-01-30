from sqlalchemy.orm import Mapped, column_property

from hapi_schema.db_org_type import view_params_org_type

from hdx_hapi.db.models.views.util.util import view
from hdx_hapi.db.models.base import Base


org_type_view = view(view_params_org_type.name, Base.metadata, view_params_org_type.selectable)


class OrgTypeView(Base):
    __table__ = org_type_view

    code: Mapped[str] = column_property(org_type_view.c.code)
    description: Mapped[str] = column_property(org_type_view.c.description)
