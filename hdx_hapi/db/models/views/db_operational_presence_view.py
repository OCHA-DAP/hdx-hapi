from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, column_property

from hapi_schema.db_operational_presence import view_params_operational_presence

from hdx_hapi.db.models.views.util.util import view
from hdx_hapi.db.models.base import Base

operational_presence_view = \
    view(view_params_operational_presence.name, Base.metadata, view_params_operational_presence.selectable)


class OperationalPresenceView(Base):
    __table__ = operational_presence_view

    id: Mapped[int] = column_property(operational_presence_view.c.id)
    resource_ref: Mapped[int] = column_property(operational_presence_view.c.resource_ref)
    org_ref: Mapped[int] = column_property(operational_presence_view.c.org_ref)
    
    sector_code: Mapped[str] = column_property(operational_presence_view.c.sector_code)
    admin2_ref: Mapped[int] = column_property(operational_presence_view.c.admin2_ref)
    reference_period_start: Mapped[DateTime] = column_property(operational_presence_view.c.reference_period_start)
    reference_period_end: Mapped[DateTime] = column_property(operational_presence_view.c.reference_period_end)
    source_data: Mapped[str] = column_property(operational_presence_view.c.source_data)

    # Additional fields from other tables in the view
    dataset_hdx_id: Mapped[str] = column_property(operational_presence_view.c.dataset_hdx_id)
    dataset_hdx_stub: Mapped[str] = column_property(operational_presence_view.c.dataset_hdx_stub)
    dataset_title: Mapped[str] = column_property(operational_presence_view.c.dataset_title)
    dataset_hdx_provider_stub: Mapped[str] = column_property(operational_presence_view.c.dataset_hdx_provider_stub)
    dataset_hdx_provider_name: Mapped[str] = column_property(operational_presence_view.c.dataset_hdx_provider_name)
    resource_hdx_id: Mapped[str] = column_property(operational_presence_view.c.resource_hdx_id)
    resource_name: Mapped[str] = column_property(operational_presence_view.c.resource_name)
    resource_update_date: Mapped[DateTime] = column_property(operational_presence_view.c.resource_update_date)
    org_acronym: Mapped[str] = column_property(operational_presence_view.c.org_acronym)
    org_name: Mapped[str] = column_property(operational_presence_view.c.org_name)
    org_type_code: Mapped[str] = column_property(operational_presence_view.c.org_type_code)
    org_type_description: Mapped[str] = column_property(operational_presence_view.c.org_type_description)
    sector_name: Mapped[str] = column_property(operational_presence_view.c.sector_name)
    location_code: Mapped[str] = column_property(operational_presence_view.c.location_code)
    location_name: Mapped[str] = column_property(operational_presence_view.c.location_name)
    admin1_code: Mapped[str] = column_property(operational_presence_view.c.admin1_code)
    admin1_name: Mapped[str] = column_property(operational_presence_view.c.admin1_name)
    admin1_is_unspecified: Mapped[bool] = column_property(operational_presence_view.c.admin1_is_unspecified)
    admin2_code: Mapped[str] = column_property(operational_presence_view.c.admin2_code)
    admin2_name: Mapped[str] = column_property(operational_presence_view.c.admin2_name)
    admin2_is_unspecified: Mapped[bool] = column_property(operational_presence_view.c.admin2_is_unspecified)
