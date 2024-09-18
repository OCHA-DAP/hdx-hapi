# ruff: noqa
import os

USE_VAT = os.getenv('HAPI_USE_VAT', 'False').lower() == 'true'

if not USE_VAT:
    from hdx_hapi.db.models.views.all_views import (
        LocationView,
        Admin1View,
        Admin2View,
        ConflictEventView,
        DatasetView,
        ResourceView,
        OrgTypeView,
        OrgView,
        SectorView,
        OperationalPresenceView,
        NationalRiskView,
        PopulationView,
        HumanitarianNeedsView,
        PovertyRateView,
        WfpCommodityView,
        WfpMarketView,
        CurrencyView,
        FoodPriceView,
        FoodSecurityView,
        FundingView,
        RefugeesView,
        AvailabilityView,
        IdpsView,
        ReturneesView,
    )
else:
    from hapi_schema.db_views_as_tables import (
        DBLocationVAT as LocationView,
        DBAdmin1VAT as Admin1View,
        DBAdmin2VAT as Admin2View,
        DBConflictEventVAT as ConflictEventView,
        DBDatasetVAT as DatasetView,
        DBResourceVAT as ResourceView,
        DBOrgTypeVAT as OrgTypeView,
        DBOrgVAT as OrgView,
        DBSectorVAT as SectorView,
        DBOperationalPresenceVAT as OperationalPresenceView,
        DBNationalRiskVAT as NationalRiskView,
        DBPopulationVAT as PopulationView,
        DBHumanitarianNeedsVAT as HumanitarianNeedsView,
        DBPovertyRateVAT as PovertyRateView,
        DBWfpCommodityVAT as WfpCommodityView,
        DBWfpMarketVAT as WfpMarketView,
        DBCurrencyVAT as CurrencyView,
        DBFoodPriceVAT as FoodPriceView,
        DBFoodSecurityVAT as FoodSecurityView,
        DBFundingVAT as FundingView,
        DBRefugeesVAT as RefugeesView,
        DBAvailabilityVAT as AvailabilityView,
        DBIDPsVAT as IdpsView,
        DBReturneesVAT as ReturneesView,
    )
