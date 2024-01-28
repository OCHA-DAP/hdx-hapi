from sqlalchemy.orm import Mapped, column_property

from hapi_schema.db_dataset import view_params_dataset

from hdx_hapi.db.models.base import Base
from hdx_hapi.db.models.views.util.util import view

dataset_view = view(view_params_dataset.name, Base.metadata, view_params_dataset.selectable)


class DatasetView(Base):
    __table__ = dataset_view
    
    id: Mapped[int] = column_property(dataset_view.c.id)
    hdx_id: Mapped[str] = column_property(dataset_view.c.hdx_id)
    hdx_stub: Mapped[str] = column_property(dataset_view.c.hdx_stub)
    title: Mapped[str] = column_property(dataset_view.c.title)
    hdx_provider_stub: Mapped[str] = column_property(dataset_view.c.hdx_provider_stub)
    hdx_provider_name: Mapped[str] = column_property(dataset_view.c.hdx_provider_name)
