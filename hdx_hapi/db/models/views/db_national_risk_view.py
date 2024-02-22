from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, column_property
from hapi_schema.db_national_risk import view_params_national_risk

from hdx_hapi.db.models.views.util.util import view
from hdx_hapi.db.models.base import Base


national_risk_view = view(view_params_national_risk.name, Base.metadata, view_params_national_risk.selectable)


class NationalRiskView(Base):
    __table__ = national_risk_view
    
    id: Mapped[int] = column_property(national_risk_view.c.id)

    resource_ref: Mapped[int] = column_property(national_risk_view.c.resource_ref)
    admin2_ref: Mapped[int] = column_property(national_risk_view.c.admin2_ref)

    risk_class: Mapped[int] = column_property(national_risk_view.c.risk_class)
    global_rank: Mapped[int] = column_property(national_risk_view.c.global_rank)
    overall_risk: Mapped[float] = column_property(national_risk_view.c.overall_risk)
    hazard_exposure_risk: Mapped[float] = column_property(national_risk_view.c.hazard_exposure_risk)
    vulnerability_risk: Mapped[float] = column_property(national_risk_view.c.vulnerability_risk)
    coping_capacity_risk: Mapped[float] = column_property(national_risk_view.c.coping_capacity_risk)
    meta_missing_indicators_pct: Mapped[float] = column_property(national_risk_view.c.meta_missing_indicators_pct)
    meta_avg_recentness_years: Mapped[float] = column_property(national_risk_view.c.meta_avg_recentness_years)

    reference_period_start: Mapped[DateTime] = column_property(national_risk_view.c.reference_period_start)
    reference_period_end: Mapped[DateTime] = column_property(national_risk_view.c.reference_period_end)

    source_data: Mapped[str] = column_property(national_risk_view.c.source_data)

    dataset_hdx_id: Mapped[str] = column_property(national_risk_view.c.dataset_hdx_id)
    dataset_hdx_stub: Mapped[str] = column_property(national_risk_view.c.dataset_hdx_stub)
    dataset_title: Mapped[str] = column_property(national_risk_view.c.dataset_title)
    dataset_hdx_provider_stub: Mapped[str] = column_property(national_risk_view.c.dataset_hdx_provider_stub)
    dataset_hdx_provider_name: Mapped[str] = column_property(national_risk_view.c.dataset_hdx_provider_name)

    resource_hdx_id: Mapped[str] = column_property(national_risk_view.c.resource_hdx_id)
    resource_name: Mapped[str] = column_property(national_risk_view.c.resource_name)
    resource_update_date = column_property(national_risk_view.c.resource_update_date)

    # sector_name: Mapped[str] = column_property(national_risk_view.c.sector_name)

    location_code: Mapped[str] = column_property(national_risk_view.c.location_code)
    location_name: Mapped[str] = column_property(national_risk_view.c.location_name)