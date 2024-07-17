"""
This code was generated automatically using src/hapi_schema/utils/hapi_views_code_generator.py
"""

from decimal import Decimal
from sqlalchemy import DateTime
from sqlalchemy.orm import column_property, Mapped
from hdx_hapi.db.models.views.util.util import view
from hdx_hapi.db.models.base import Base
from hapi_schema.db_admin1 import view_params_admin1
from hapi_schema.db_admin2 import view_params_admin2
from hapi_schema.db_conflict_event import view_params_conflict_event
from hapi_schema.db_currency import view_params_currency
from hapi_schema.db_dataset import view_params_dataset
from hapi_schema.db_food_price import view_params_food_price
from hapi_schema.db_food_security import view_params_food_security
from hapi_schema.db_funding import view_params_funding
from hapi_schema.db_humanitarian_needs import view_params_humanitarian_needs
from hapi_schema.db_location import view_params_location
from hapi_schema.db_national_risk import view_params_national_risk
from hapi_schema.db_operational_presence import view_params_operational_presence
from hapi_schema.db_org_type import view_params_org_type
from hapi_schema.db_org import view_params_org
from hapi_schema.db_population import view_params_population
from hapi_schema.db_poverty_rate import view_params_poverty_rate
from hapi_schema.db_refugees import view_params_refugees
from hapi_schema.db_resource import view_params_resource
from hapi_schema.db_sector import view_params_sector
from hapi_schema.db_wfp_commodity import view_params_wfp_commodity
from hapi_schema.db_wfp_market import view_params_wfp_market
from hapi_schema.db_patch import view_params_patch
from hapi_schema.utils.enums import (
    CommodityCategory,
    DisabledMarker,
    EventType,
    IPCPhase,
    IPCType,
    PopulationGroup,
    PopulationStatus,
    PriceFlag,
    PriceType,
    RiskClass,
    Gender,
)

admin1_view = view(view_params_admin1.name, Base.metadata, view_params_admin1.selectable)
admin2_view = view(view_params_admin2.name, Base.metadata, view_params_admin2.selectable)
conflict_event_view = view(view_params_conflict_event.name, Base.metadata, view_params_conflict_event.selectable)
currency_view = view(view_params_currency.name, Base.metadata, view_params_currency.selectable)
dataset_view = view(view_params_dataset.name, Base.metadata, view_params_dataset.selectable)
food_price_view = view(view_params_food_price.name, Base.metadata, view_params_food_price.selectable)
food_security_view = view(view_params_food_security.name, Base.metadata, view_params_food_security.selectable)
funding_view = view(view_params_funding.name, Base.metadata, view_params_funding.selectable)
humanitarian_needs_view = view(
    view_params_humanitarian_needs.name, Base.metadata, view_params_humanitarian_needs.selectable
)
location_view = view(view_params_location.name, Base.metadata, view_params_location.selectable)
national_risk_view = view(view_params_national_risk.name, Base.metadata, view_params_national_risk.selectable)
operational_presence_view = view(
    view_params_operational_presence.name, Base.metadata, view_params_operational_presence.selectable
)
org_type_view = view(view_params_org_type.name, Base.metadata, view_params_org_type.selectable)
org_view = view(view_params_org.name, Base.metadata, view_params_org.selectable)
population_view = view(view_params_population.name, Base.metadata, view_params_population.selectable)
poverty_rate_view = view(view_params_poverty_rate.name, Base.metadata, view_params_poverty_rate.selectable)
refugees_view = view(view_params_refugees.name, Base.metadata, view_params_refugees.selectable)
resource_view = view(view_params_resource.name, Base.metadata, view_params_resource.selectable)
sector_view = view(view_params_sector.name, Base.metadata, view_params_sector.selectable)
wfp_commodity_view = view(view_params_wfp_commodity.name, Base.metadata, view_params_wfp_commodity.selectable)
wfp_market_view = view(view_params_wfp_market.name, Base.metadata, view_params_wfp_market.selectable)
patch_view = view(view_params_patch.name, Base.metadata, view_params_patch.selectable)


class Admin1View(Base):
    __table__ = admin1_view
    id: Mapped[int] = column_property(admin1_view.c.id)
    location_ref: Mapped[int] = column_property(admin1_view.c.location_ref)
    code: Mapped[str] = column_property(admin1_view.c.code)
    name: Mapped[str] = column_property(admin1_view.c.name)
    is_unspecified: Mapped[bool] = column_property(admin1_view.c.is_unspecified)
    from_cods: Mapped[bool] = column_property(admin1_view.c.from_cods)
    reference_period_start: Mapped[DateTime] = column_property(admin1_view.c.reference_period_start)
    reference_period_end: Mapped[DateTime] = column_property(admin1_view.c.reference_period_end)
    location_code: Mapped[str] = column_property(admin1_view.c.location_code)
    location_name: Mapped[str] = column_property(admin1_view.c.location_name)


class Admin2View(Base):
    __table__ = admin2_view
    id: Mapped[int] = column_property(admin2_view.c.id)
    admin1_ref: Mapped[int] = column_property(admin2_view.c.admin1_ref)
    code: Mapped[str] = column_property(admin2_view.c.code)
    name: Mapped[str] = column_property(admin2_view.c.name)
    is_unspecified: Mapped[bool] = column_property(admin2_view.c.is_unspecified)
    from_cods: Mapped[bool] = column_property(admin2_view.c.from_cods)
    reference_period_start: Mapped[DateTime] = column_property(admin2_view.c.reference_period_start)
    reference_period_end: Mapped[DateTime] = column_property(admin2_view.c.reference_period_end)
    admin1_code: Mapped[str] = column_property(admin2_view.c.admin1_code)
    admin1_name: Mapped[str] = column_property(admin2_view.c.admin1_name)
    admin1_is_unspecified: Mapped[bool] = column_property(admin2_view.c.admin1_is_unspecified)
    location_ref: Mapped[int] = column_property(admin2_view.c.location_ref)
    location_code: Mapped[str] = column_property(admin2_view.c.location_code)
    location_name: Mapped[str] = column_property(admin2_view.c.location_name)


class ConflictEventView(Base):
    __table__ = conflict_event_view
    resource_hdx_id: Mapped[str] = column_property(conflict_event_view.c.resource_hdx_id)
    admin2_ref: Mapped[int] = column_property(conflict_event_view.c.admin2_ref)
    event_type: Mapped[EventType] = column_property(conflict_event_view.c.event_type)
    events: Mapped[int] = column_property(conflict_event_view.c.events)
    fatalities: Mapped[int] = column_property(conflict_event_view.c.fatalities)
    reference_period_start: Mapped[DateTime] = column_property(conflict_event_view.c.reference_period_start)
    reference_period_end: Mapped[DateTime] = column_property(conflict_event_view.c.reference_period_end)
    location_code: Mapped[str] = column_property(conflict_event_view.c.location_code)
    location_name: Mapped[str] = column_property(conflict_event_view.c.location_name)
    has_hrp: Mapped[bool] = column_property(location_view.c.has_hrp)
    in_gho: Mapped[bool] = column_property(location_view.c.in_gho)
    admin1_code: Mapped[str] = column_property(conflict_event_view.c.admin1_code)
    admin1_name: Mapped[str] = column_property(conflict_event_view.c.admin1_name)
    admin1_is_unspecified: Mapped[bool] = column_property(conflict_event_view.c.admin1_is_unspecified)
    location_ref: Mapped[int] = column_property(conflict_event_view.c.location_ref)
    admin2_code: Mapped[str] = column_property(conflict_event_view.c.admin2_code)
    admin2_name: Mapped[str] = column_property(conflict_event_view.c.admin2_name)
    admin2_is_unspecified: Mapped[bool] = column_property(conflict_event_view.c.admin2_is_unspecified)
    admin1_ref: Mapped[int] = column_property(conflict_event_view.c.admin1_ref)


class CurrencyView(Base):
    __table__ = currency_view
    code: Mapped[str] = column_property(currency_view.c.code)
    name: Mapped[str] = column_property(currency_view.c.name)


class DatasetView(Base):
    __table__ = dataset_view
    dataset_hdx_id: Mapped[str] = column_property(dataset_view.c.hdx_id)
    dataset_hdx_stub: Mapped[str] = column_property(dataset_view.c.hdx_stub)
    dataset_hdx_title: Mapped[str] = column_property(dataset_view.c.title)
    hdx_provider_stub: Mapped[str] = column_property(dataset_view.c.hdx_provider_stub)
    hdx_provider_name: Mapped[str] = column_property(dataset_view.c.hdx_provider_name)


class FoodPriceView(Base):
    __table__ = food_price_view
    resource_hdx_id: Mapped[str] = column_property(food_price_view.c.resource_hdx_id)
    market_code: Mapped[str] = column_property(food_price_view.c.market_code)
    commodity_code: Mapped[str] = column_property(food_price_view.c.commodity_code)
    currency_code: Mapped[str] = column_property(food_price_view.c.currency_code)
    unit: Mapped[str] = column_property(food_price_view.c.unit)
    price_flag: Mapped[PriceFlag] = column_property(food_price_view.c.price_flag)
    price_type: Mapped[PriceType] = column_property(food_price_view.c.price_type)
    price: Mapped[Decimal] = column_property(food_price_view.c.price)
    reference_period_start: Mapped[DateTime] = column_property(food_price_view.c.reference_period_start)
    reference_period_end: Mapped[DateTime] = column_property(food_price_view.c.reference_period_end)
    admin2_ref: Mapped[int] = column_property(food_price_view.c.admin2_ref)
    market_name: Mapped[str] = column_property(food_price_view.c.market_name)
    lat: Mapped[float] = column_property(food_price_view.c.lat)
    lon: Mapped[float] = column_property(food_price_view.c.lon)
    commodity_category: Mapped[CommodityCategory] = column_property(food_price_view.c.commodity_category)
    commodity_name: Mapped[str] = column_property(food_price_view.c.commodity_name)
    location_code: Mapped[str] = column_property(food_price_view.c.location_code)
    location_name: Mapped[str] = column_property(food_price_view.c.location_name)
    location_ref: Mapped[int] = column_property(food_price_view.c.location_ref)
    has_hrp: Mapped[bool] = column_property(location_view.c.has_hrp)
    in_gho: Mapped[bool] = column_property(location_view.c.in_gho)
    admin1_code: Mapped[str] = column_property(food_price_view.c.admin1_code)
    admin1_name: Mapped[str] = column_property(food_price_view.c.admin1_name)
    admin1_is_unspecified: Mapped[bool] = column_property(food_price_view.c.admin1_is_unspecified)
    admin1_ref: Mapped[int] = column_property(food_price_view.c.admin1_ref)
    admin2_code: Mapped[str] = column_property(food_price_view.c.admin2_code)
    admin2_name: Mapped[str] = column_property(food_price_view.c.admin2_name)
    admin2_is_unspecified: Mapped[bool] = column_property(food_price_view.c.admin2_is_unspecified)


class FoodSecurityView(Base):
    __table__ = food_security_view
    resource_hdx_id: Mapped[str] = column_property(food_security_view.c.resource_hdx_id)
    admin2_ref: Mapped[int] = column_property(food_security_view.c.admin2_ref)
    ipc_phase: Mapped[IPCPhase] = column_property(food_security_view.c.ipc_phase)
    ipc_type: Mapped[IPCType] = column_property(food_security_view.c.ipc_type)
    population_in_phase: Mapped[int] = column_property(food_security_view.c.population_in_phase)
    population_fraction_in_phase: Mapped[float] = column_property(food_security_view.c.population_fraction_in_phase)
    reference_period_start: Mapped[DateTime] = column_property(food_security_view.c.reference_period_start)
    reference_period_end: Mapped[DateTime] = column_property(food_security_view.c.reference_period_end)
    location_code: Mapped[str] = column_property(food_security_view.c.location_code)
    location_name: Mapped[str] = column_property(food_security_view.c.location_name)
    has_hrp: Mapped[bool] = column_property(location_view.c.has_hrp)
    in_gho: Mapped[bool] = column_property(location_view.c.in_gho)
    admin1_code: Mapped[str] = column_property(food_security_view.c.admin1_code)
    admin1_name: Mapped[str] = column_property(food_security_view.c.admin1_name)
    admin1_is_unspecified: Mapped[bool] = column_property(food_security_view.c.admin1_is_unspecified)
    location_ref: Mapped[int] = column_property(food_security_view.c.location_ref)
    admin2_code: Mapped[str] = column_property(food_security_view.c.admin2_code)
    admin2_name: Mapped[str] = column_property(food_security_view.c.admin2_name)
    admin2_is_unspecified: Mapped[bool] = column_property(food_security_view.c.admin2_is_unspecified)
    admin1_ref: Mapped[int] = column_property(food_security_view.c.admin1_ref)


class FundingView(Base):
    __table__ = funding_view
    resource_hdx_id: Mapped[str] = column_property(funding_view.c.resource_hdx_id)
    appeal_code: Mapped[str] = column_property(funding_view.c.appeal_code)
    location_ref: Mapped[int] = column_property(funding_view.c.location_ref)
    appeal_name: Mapped[str] = column_property(funding_view.c.appeal_name)
    appeal_type: Mapped[str] = column_property(funding_view.c.appeal_type)
    requirements_usd: Mapped[Decimal] = column_property(funding_view.c.requirements_usd)
    funding_usd: Mapped[Decimal] = column_property(funding_view.c.funding_usd)
    funding_pct: Mapped[Decimal] = column_property(funding_view.c.funding_pct)
    reference_period_start: Mapped[DateTime] = column_property(funding_view.c.reference_period_start)
    reference_period_end: Mapped[DateTime] = column_property(funding_view.c.reference_period_end)
    location_code: Mapped[str] = column_property(funding_view.c.location_code)
    location_name: Mapped[str] = column_property(funding_view.c.location_name)
    has_hrp: Mapped[bool] = column_property(location_view.c.has_hrp)
    in_gho: Mapped[bool] = column_property(location_view.c.in_gho)


class HumanitarianNeedsView(Base):
    __table__ = humanitarian_needs_view
    resource_hdx_id: Mapped[str] = column_property(humanitarian_needs_view.c.resource_hdx_id)
    admin2_ref: Mapped[int] = column_property(humanitarian_needs_view.c.admin2_ref)
    gender: Mapped[Gender] = column_property(humanitarian_needs_view.c.gender)
    age_range: Mapped[str] = column_property(humanitarian_needs_view.c.age_range)
    min_age: Mapped[int] = column_property(humanitarian_needs_view.c.min_age)
    max_age: Mapped[int] = column_property(humanitarian_needs_view.c.max_age)
    sector_code: Mapped[str] = column_property(humanitarian_needs_view.c.sector_code)
    population_group: Mapped[PopulationGroup] = column_property(humanitarian_needs_view.c.population_group)
    population_status: Mapped[PopulationStatus] = column_property(humanitarian_needs_view.c.population_status)
    disabled_marker: Mapped[DisabledMarker] = column_property(humanitarian_needs_view.c.disabled_marker)
    population: Mapped[int] = column_property(humanitarian_needs_view.c.population)
    reference_period_start: Mapped[DateTime] = column_property(humanitarian_needs_view.c.reference_period_start)
    reference_period_end: Mapped[DateTime] = column_property(humanitarian_needs_view.c.reference_period_end)
    sector_name: Mapped[str] = column_property(humanitarian_needs_view.c.sector_name)
    location_code: Mapped[str] = column_property(humanitarian_needs_view.c.location_code)
    location_name: Mapped[str] = column_property(humanitarian_needs_view.c.location_name)
    location_ref: Mapped[int] = column_property(humanitarian_needs_view.c.location_ref)
    has_hrp: Mapped[bool] = column_property(location_view.c.has_hrp)
    in_gho: Mapped[bool] = column_property(location_view.c.in_gho)
    admin1_code: Mapped[str] = column_property(humanitarian_needs_view.c.admin1_code)
    admin1_name: Mapped[str] = column_property(humanitarian_needs_view.c.admin1_name)
    admin1_is_unspecified: Mapped[bool] = column_property(humanitarian_needs_view.c.admin1_is_unspecified)
    admin2_code: Mapped[str] = column_property(humanitarian_needs_view.c.admin2_code)
    admin2_name: Mapped[str] = column_property(humanitarian_needs_view.c.admin2_name)
    admin2_is_unspecified: Mapped[bool] = column_property(humanitarian_needs_view.c.admin2_is_unspecified)
    admin1_ref: Mapped[int] = column_property(humanitarian_needs_view.c.admin1_ref)


class LocationView(Base):
    __table__ = location_view
    id: Mapped[int] = column_property(location_view.c.id)
    code: Mapped[str] = column_property(location_view.c.code)
    name: Mapped[str] = column_property(location_view.c.name)
    from_cods: Mapped[bool] = column_property(location_view.c.from_cods)
    has_hrp: Mapped[bool] = column_property(location_view.c.has_hrp)
    in_gho: Mapped[bool] = column_property(location_view.c.in_gho)
    reference_period_start: Mapped[DateTime] = column_property(location_view.c.reference_period_start)
    reference_period_end: Mapped[DateTime] = column_property(location_view.c.reference_period_end)


class NationalRiskView(Base):
    __table__ = national_risk_view
    resource_hdx_id: Mapped[str] = column_property(national_risk_view.c.resource_hdx_id)
    location_ref: Mapped[int] = column_property(national_risk_view.c.location_ref)
    risk_class: Mapped[RiskClass] = column_property(national_risk_view.c.risk_class)
    global_rank: Mapped[int] = column_property(national_risk_view.c.global_rank)
    overall_risk: Mapped[float] = column_property(national_risk_view.c.overall_risk)
    hazard_exposure_risk: Mapped[float] = column_property(national_risk_view.c.hazard_exposure_risk)
    vulnerability_risk: Mapped[float] = column_property(national_risk_view.c.vulnerability_risk)
    coping_capacity_risk: Mapped[float] = column_property(national_risk_view.c.coping_capacity_risk)
    meta_missing_indicators_pct: Mapped[float] = column_property(national_risk_view.c.meta_missing_indicators_pct)
    meta_avg_recentness_years: Mapped[float] = column_property(national_risk_view.c.meta_avg_recentness_years)
    reference_period_start: Mapped[DateTime] = column_property(national_risk_view.c.reference_period_start)
    reference_period_end: Mapped[DateTime] = column_property(national_risk_view.c.reference_period_end)
    location_code: Mapped[str] = column_property(national_risk_view.c.location_code)
    location_name: Mapped[str] = column_property(national_risk_view.c.location_name)
    has_hrp: Mapped[bool] = column_property(location_view.c.has_hrp)
    in_gho: Mapped[bool] = column_property(location_view.c.in_gho)


class OperationalPresenceView(Base):
    __table__ = operational_presence_view
    resource_hdx_id: Mapped[str] = column_property(operational_presence_view.c.resource_hdx_id)
    admin2_ref: Mapped[int] = column_property(operational_presence_view.c.admin2_ref)
    org_acronym: Mapped[str] = column_property(operational_presence_view.c.org_acronym)
    org_name: Mapped[str] = column_property(operational_presence_view.c.org_name)
    sector_code: Mapped[str] = column_property(operational_presence_view.c.sector_code)
    reference_period_start: Mapped[DateTime] = column_property(operational_presence_view.c.reference_period_start)
    reference_period_end: Mapped[DateTime] = column_property(operational_presence_view.c.reference_period_end)
    org_type_code: Mapped[str] = column_property(operational_presence_view.c.org_type_code)
    org_type_description: Mapped[str] = column_property(operational_presence_view.c.org_type_description)
    sector_name: Mapped[str] = column_property(operational_presence_view.c.sector_name)
    location_code: Mapped[str] = column_property(operational_presence_view.c.location_code)
    location_name: Mapped[str] = column_property(operational_presence_view.c.location_name)
    has_hrp: Mapped[bool] = column_property(location_view.c.has_hrp)
    in_gho: Mapped[bool] = column_property(location_view.c.in_gho)
    admin1_code: Mapped[str] = column_property(operational_presence_view.c.admin1_code)
    admin1_name: Mapped[str] = column_property(operational_presence_view.c.admin1_name)
    admin1_is_unspecified: Mapped[bool] = column_property(operational_presence_view.c.admin1_is_unspecified)
    location_ref: Mapped[int] = column_property(operational_presence_view.c.location_ref)
    admin2_code: Mapped[str] = column_property(operational_presence_view.c.admin2_code)
    admin2_name: Mapped[str] = column_property(operational_presence_view.c.admin2_name)
    admin2_is_unspecified: Mapped[bool] = column_property(operational_presence_view.c.admin2_is_unspecified)
    admin1_ref: Mapped[int] = column_property(operational_presence_view.c.admin1_ref)


class OrgTypeView(Base):
    __table__ = org_type_view
    code: Mapped[str] = column_property(org_type_view.c.code)
    description: Mapped[str] = column_property(org_type_view.c.description)


class OrgView(Base):
    __table__ = org_view
    acronym: Mapped[str] = column_property(org_view.c.acronym)
    name: Mapped[str] = column_property(org_view.c.name)
    org_type_code: Mapped[str] = column_property(org_view.c.org_type_code)
    org_type_description: Mapped[str] = column_property(org_view.c.org_type_description)


class PopulationView(Base):
    __table__ = population_view
    resource_hdx_id: Mapped[str] = column_property(population_view.c.resource_hdx_id)
    admin2_ref: Mapped[int] = column_property(population_view.c.admin2_ref)
    gender: Mapped[Gender] = column_property(population_view.c.gender)
    age_range: Mapped[str] = column_property(population_view.c.age_range)
    min_age: Mapped[int] = column_property(population_view.c.min_age)
    max_age: Mapped[int] = column_property(population_view.c.max_age)
    population: Mapped[int] = column_property(population_view.c.population)
    reference_period_start: Mapped[DateTime] = column_property(population_view.c.reference_period_start)
    reference_period_end: Mapped[DateTime] = column_property(population_view.c.reference_period_end)
    location_code: Mapped[str] = column_property(population_view.c.location_code)
    location_name: Mapped[str] = column_property(population_view.c.location_name)
    has_hrp: Mapped[bool] = column_property(location_view.c.has_hrp)
    in_gho: Mapped[bool] = column_property(location_view.c.in_gho)
    admin1_code: Mapped[str] = column_property(population_view.c.admin1_code)
    admin1_name: Mapped[str] = column_property(population_view.c.admin1_name)
    admin1_is_unspecified: Mapped[bool] = column_property(population_view.c.admin1_is_unspecified)
    location_ref: Mapped[int] = column_property(population_view.c.location_ref)
    admin2_code: Mapped[str] = column_property(population_view.c.admin2_code)
    admin2_name: Mapped[str] = column_property(population_view.c.admin2_name)
    admin2_is_unspecified: Mapped[bool] = column_property(population_view.c.admin2_is_unspecified)
    admin1_ref: Mapped[int] = column_property(population_view.c.admin1_ref)


class PovertyRateView(Base):
    __table__ = poverty_rate_view
    resource_hdx_id: Mapped[str] = column_property(poverty_rate_view.c.resource_hdx_id)
    admin1_ref: Mapped[int] = column_property(poverty_rate_view.c.admin1_ref)
    admin1_name: Mapped[str] = column_property(poverty_rate_view.c.admin1_name)
    mpi: Mapped[float] = column_property(poverty_rate_view.c.mpi)
    headcount_ratio: Mapped[float] = column_property(poverty_rate_view.c.headcount_ratio)
    intensity_of_deprivation: Mapped[float] = column_property(poverty_rate_view.c.intensity_of_deprivation)
    vulnerable_to_poverty: Mapped[float] = column_property(poverty_rate_view.c.vulnerable_to_poverty)
    in_severe_poverty: Mapped[float] = column_property(poverty_rate_view.c.in_severe_poverty)
    reference_period_start: Mapped[DateTime] = column_property(poverty_rate_view.c.reference_period_start)
    reference_period_end: Mapped[DateTime] = column_property(poverty_rate_view.c.reference_period_end)
    location_code: Mapped[str] = column_property(poverty_rate_view.c.location_code)
    location_name: Mapped[str] = column_property(poverty_rate_view.c.location_name)
    admin1_code: Mapped[str] = column_property(poverty_rate_view.c.admin1_code)
    admin1_is_unspecified: Mapped[bool] = column_property(poverty_rate_view.c.admin1_is_unspecified)
    location_ref: Mapped[int] = column_property(poverty_rate_view.c.location_ref)


class RefugeesView(Base):
    __table__ = refugees_view
    resource_hdx_id: Mapped[str] = column_property(refugees_view.c.resource_hdx_id)
    origin_location_ref: Mapped[int] = column_property(refugees_view.c.origin_location_ref)
    asylum_location_ref: Mapped[int] = column_property(refugees_view.c.asylum_location_ref)
    population_group: Mapped[PopulationGroup] = column_property(refugees_view.c.population_group)
    gender: Mapped[Gender] = column_property(refugees_view.c.gender)
    age_range: Mapped[str] = column_property(refugees_view.c.age_range)
    min_age: Mapped[int] = column_property(refugees_view.c.min_age)
    max_age: Mapped[int] = column_property(refugees_view.c.max_age)
    population: Mapped[int] = column_property(refugees_view.c.population)
    reference_period_start: Mapped[DateTime] = column_property(refugees_view.c.reference_period_start)
    reference_period_end: Mapped[DateTime] = column_property(refugees_view.c.reference_period_end)
    origin_location_code: Mapped[str] = column_property(refugees_view.c.origin_location_code)
    origin_location_name: Mapped[str] = column_property(refugees_view.c.origin_location_name)
    asylum_location_code: Mapped[str] = column_property(refugees_view.c.asylum_location_code)
    asylum_location_name: Mapped[str] = column_property(refugees_view.c.asylum_location_name)


class ResourceView(Base):
    __table__ = resource_view
    resource_hdx_id: Mapped[str] = column_property(resource_view.c.hdx_id)
    dataset_hdx_id: Mapped[str] = column_property(resource_view.c.dataset_hdx_id)
    name: Mapped[str] = column_property(resource_view.c.name)
    format: Mapped[str] = column_property(resource_view.c.format)
    update_date: Mapped[DateTime] = column_property(resource_view.c.update_date)
    is_hxl: Mapped[bool] = column_property(resource_view.c.is_hxl)
    download_url: Mapped[str] = column_property(resource_view.c.download_url)
    hapi_updated_date: Mapped[DateTime] = column_property(resource_view.c.hapi_updated_date)
    dataset_hdx_stub: Mapped[str] = column_property(resource_view.c.dataset_hdx_stub)
    dataset_hdx_title: Mapped[str] = column_property(resource_view.c.dataset_title)
    dataset_hdx_provider_stub: Mapped[str] = column_property(resource_view.c.dataset_hdx_provider_stub)
    dataset_hdx_provider_name: Mapped[str] = column_property(resource_view.c.dataset_hdx_provider_name)


class SectorView(Base):
    __table__ = sector_view
    code: Mapped[str] = column_property(sector_view.c.code)
    name: Mapped[str] = column_property(sector_view.c.name)


class WfpCommodityView(Base):
    __table__ = wfp_commodity_view
    code: Mapped[str] = column_property(wfp_commodity_view.c.code)
    category: Mapped[CommodityCategory] = column_property(wfp_commodity_view.c.category)
    name: Mapped[str] = column_property(wfp_commodity_view.c.name)


class WfpMarketView(Base):
    __table__ = wfp_market_view
    code: Mapped[str] = column_property(wfp_market_view.c.code)
    admin2_ref: Mapped[int] = column_property(wfp_market_view.c.admin2_ref)
    name: Mapped[str] = column_property(wfp_market_view.c.name)
    lat: Mapped[float] = column_property(wfp_market_view.c.lat)
    lon: Mapped[float] = column_property(wfp_market_view.c.lon)
    location_code: Mapped[str] = column_property(wfp_market_view.c.location_code)
    location_name: Mapped[str] = column_property(wfp_market_view.c.location_name)
    admin1_code: Mapped[str] = column_property(wfp_market_view.c.admin1_code)
    admin1_name: Mapped[str] = column_property(wfp_market_view.c.admin1_name)
    admin1_is_unspecified: Mapped[bool] = column_property(wfp_market_view.c.admin1_is_unspecified)
    location_ref: Mapped[int] = column_property(wfp_market_view.c.location_ref)
    admin2_code: Mapped[str] = column_property(wfp_market_view.c.admin2_code)
    admin2_name: Mapped[str] = column_property(wfp_market_view.c.admin2_name)
    admin2_is_unspecified: Mapped[bool] = column_property(wfp_market_view.c.admin2_is_unspecified)
    admin1_ref: Mapped[int] = column_property(wfp_market_view.c.admin1_ref)


class PatchView(Base):
    __table__ = patch_view
    id: Mapped[int] = column_property(patch_view.c.id)
    patch_sequence_number: Mapped[int] = column_property(patch_view.c.patch_sequence_number)
    commit_hash: Mapped[str] = column_property(patch_view.c.commit_hash)
    commit_date: Mapped[DateTime] = column_property(patch_view.c.commit_date)
    patch_path: Mapped[str] = column_property(patch_view.c.patch_path)
    patch_permalink_url: Mapped[str] = column_property(patch_view.c.patch_permalink_url)
    patch_target: Mapped[str] = column_property(patch_view.c.patch_target)
    patch_hash: Mapped[str] = column_property(patch_view.c.patch_hash)
    state: Mapped[str] = column_property(patch_view.c.state)
    execution_date: Mapped[DateTime] = column_property(patch_view.c.execution_date)
