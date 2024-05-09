from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, column_property

from hapi_schema.db_resource import view_params_resource

from hdx_hapi.db.models.views.util.util import view
from hdx_hapi.db.models.base import Base


resource_view = view(view_params_resource.name, Base.metadata, view_params_resource.selectable)


class ResourceView(Base):
    __table__ = resource_view
    
    id: Mapped[int] = column_property(resource_view.c.id)
    dataset_ref: Mapped[int] = column_property(resource_view.c.dataset_ref)
    hdx_id: Mapped[str] = column_property(resource_view.c.hdx_id)
    name: Mapped[str] = column_property(resource_view.c.name)
    format: Mapped[str] = column_property(resource_view.c.format)
    update_date = column_property(resource_view.c.update_date)
    is_hxl: Mapped[bool] = column_property(resource_view.c.is_hxl)
    download_url: Mapped[str] = column_property(resource_view.c.download_url)
    hapi_updated_date: Mapped[DateTime] = column_property(resource_view.c.hapi_updated_date)
    hapi_replaced_date: Mapped[DateTime] = column_property(resource_view.c.hapi_replaced_date)

    dataset_hdx_id: Mapped[str] = column_property(resource_view.c.dataset_hdx_id)
    dataset_hdx_stub: Mapped[str] = column_property(resource_view.c.dataset_hdx_stub)
    dataset_title: Mapped[str] = column_property(resource_view.c.dataset_title)

    dataset_hdx_provider_stub: Mapped[str] = column_property(resource_view.c.dataset_hdx_provider_stub)
    dataset_hdx_provider_name: Mapped[str] = column_property(resource_view.c.dataset_hdx_provider_name)
    