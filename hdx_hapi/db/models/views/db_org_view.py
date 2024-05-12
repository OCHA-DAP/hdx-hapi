from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, column_property

from hapi_schema.db_org import view_params_org

from hdx_hapi.db.models.views.util.util import view
from hdx_hapi.db.models.base import Base


org_view = view(view_params_org.name, Base.metadata, view_params_org.selectable)


class OrgView(Base):
    __table__ = org_view

    id: Mapped[int] = column_property(org_view.c.id)
    acronym: Mapped[str] = column_property(org_view.c.acronym)
    name: Mapped[str] = column_property(org_view.c.name)
    org_type_code: Mapped[str] = column_property(org_view.c.org_type_code)
    reference_period_start: Mapped[DateTime] = column_property(org_view.c.reference_period_start)
    reference_period_end: Mapped[DateTime] = column_property(org_view.c.reference_period_end)
    org_type_description: Mapped[str] = column_property(org_view.c.org_type_description)
