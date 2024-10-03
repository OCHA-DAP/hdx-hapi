from hdx_hapi.config.config import get_config

CONFIG = get_config()

# Location related
DOC_SCOPE_DISCLAIMER = f'Not all data are available for all locations. Learn more about the scope of data coverage in HDX HAPI in the <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}">Overview and Getting Started</a> documentation.'
DOC_LOCATION_ID = 'Filter the response by a location (typically a country), using the unique identifier (id) from the location table associated with each entry.'
DOC_LOCATION_REF = 'Filter the response by a location (typically a country) reference number.'
DOC_LOCATION_CODE = 'Filter the response by a location (typically a country). The location codes use the ISO-3 (ISO 3166 alpha-3) codes.'
DOC_LOCATION_NAME = 'Filter the response by a location (typically a country). The location names are based on the "short name" from the <a href="https://unstats.un.org/unsd/methodology/m49/#fn2">UN M49 Standard</a>.'
DOC_LOCATION_HAS_HRP = 'Filter the response by the has_hrp flag. The has_hrp flag indicates whether a country has a Humanitarian Response Plan.'
DOC_LOCATION_IN_GHO = 'Filter the response by the in_gho flag. The in_gho flag indicates whether a country is in the <a href="https://humanitarianaction.info/">Global Humanitarian Overview</a>.'
DOC_SEE_LOC = 'See the <a href="/docs#/Metadata/get_locations_api_v1_metadata_location_get" target="_blank">location endpoint</a> for details.'
DOC_ADMIN1_ID = 'Filter the response by 1st subnational administrative division, using the unique identifier (id) from the admin1 table associated with each entry.'
DOC_ADMIN1_REF = 'Filter the response by the 1st subnational administrative division reference number.'
DOC_ADMIN1_CODE = 'Filter the response by the 1st subnational administrative divisions. The admin1 codes refer to the p-codes in the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a>.'
DOC_ADMIN1_NAME = 'Filter the response by the 1st subnational administrative divisions. The admin1 names refer to the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a>.'
DOC_SEE_ADMIN1 = 'See the <a href="/docs#/Metadata/get_admin1_api_v1_metadata_admin1_get" target="_blank">admin1 endpoint</a> for details.'
DOC_PROVIDER_ADMIN1_NAME = (
    'Filter the response by the 1st subnational administrative divisions provided by the supplier.'
)
DOC_ADMIN2_ID = 'Filter the response by 2nd subnational administrative division, using the unique identifier (id) from the admin2 table associated with each entry.'
DOC_ADMIN2_REF = 'Filter the response by the 2nd subnational administrative division reference number.'
DOC_ADMIN2_CODE = 'Filter the response by the 2nd subnational administrative divisions. The admin2 codes refer to the p-codes in the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a>.'
DOC_ADMIN2_NAME = 'Filter the response by the 2nd subnational administrative divisions. The admin2 names refer to the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a>.'
DOC_PROVIDER_ADMIN2_NAME = (
    'Filter the response by the 2nd subnational administrative divisions provided by the supplier.'
)
DOC_SEE_ADMIN2 = 'See the <a href="/docs#/Metadata/get_admin2_api_v1_metadata_admin2_get" target="_blank">admin2 endpoint</a> for details.'
DOC_ADMIN_LEVEL_FILTER = 'Filter the response by admin level.'

# HDX Metadata
DOC_HDX_DATASET_ID = 'Filter the response by the dataset ID (dataset_hdx_id), which is a unique and fixed identifier of a Dataset on HDX. A URL in the pattern of `https://data.humdata.org/dataset/[dataset_hdx_id]` will load the dataset page on HDX.'
DOC_HDX_DATASET_STUB = 'Filter the response by the URL-safe name (dataset_hdx_stub) of the dataset as displayed on HDX. This name is unique but can change. A URL in the pattern of `https://data.humdata.org/dataset/[dataset_hdx_stub]` will load the dataset page on HDX.'
DOC_HDX_DATASET_TITLE = 'Filter the response by the title of the dataset as it appears in the HDX interface. This name is not unique and can change.'
DOC_HDX_PROVIDER_STUB = "Filter the response by the URL-safe name of the provider (organization) of the dataset on HDX. A URL in the pattern of `https://data.humdata.org/organization/[hdx_provider_stub]` will load the provider's page on HDX."
DOC_HDX_PROVIDER_NAME = 'Filter the response by the display name of the provider (organization) of the dataset on HDX.'
DOC_HDX_RESOURCE_ID = 'Filter the response by the resource ID, which is a unique and fixed identifier of a resource on HDX. A URL in the pattern of `https://data.humdata.org/dataset/[dataset_hdx_id]/resource/[resource_hdx_id]` will load the resource page on HDX.'
DOC_HDX_RESOURCE_FORMAT = 'Filter the response by the format of the resource on HDX. These are typically file formats (i.e. CSV, XLSX), but can also include APIs and web apps.'
DOC_HDX_RESOURCE_HXL = (
    'Filter the response by whether or not the resource contains <a href="https://hxlstandard.org/">HXL tags</a>.'
)
DOC_HDX_DATASET_IN_RESOURCE_ID = 'Filter the response by the dataset ID (dataset_hdx_id), which is a unique and fixed identifier of a dataset on HDX. A URL in the pattern of `https://data.humdata.org/dataset/[dataset_hdx_id]` will load the dataset page on HDX.'
DOC_HDX_DATASET_IN_RESOURCE_NAME = 'Filter the response by the URL-safe name (dataset_hdx_stub) of the dataset as displayed on HDX. This name is unique but can change. A URL in the pattern of `https://data.humdata.org/dataset/[dataset_hdx_stub]` will load the dataset page on HDX.'
DOC_HDX_PROVIDER_IN_RESOURCE_STUB = "Filter the response by the URL-safe name of the provider (organization) of the dataset on HDX. A URL in the pattern of `https://data.humdata.org/organization/[dataset_hdx_provider_stub]` will load the provider's page on HDX."
DOC_SEE_DATASET = 'See the <a href="/docs#/Metadata/get_datasets_api_v1_metadata_dataset_get" target="_blank">dataset endpoint</a> for details.'

# Time periods
DOC_UPDATE_DATE_MIN = 'Minimum date that datasets was last updated, e.g. 2020-01-01 or 2020-01-01T00:00:00'
DOC_UPDATE_DATE_MAX = 'Maximum date that datasets was last updated, e.g. 2020-01-01 or 2020-01-01T00:00:00'
# DOC_HAPI_UPDATED_DATE_MIN = 'Min date of HDX HAPI updated date, e.g. 2020-01-01 or 2020-01-01T00:00:00'
# DOC_HAPI_UPDATED_DATE_MAX = 'Max date of HDX HAPI updated date, e.g. 2020-01-01 or 2020-01-01T00:00:00'
# DOC_HAPI_REPLACED_DATE_MIN = 'Min date of HDX HAPI replaced date, e.g. 2020-01-01 or 2020-01-01T00:00:00'
# DOC_HAPI_REPLACED_DATE_MAX = 'Max date of HDX HAPI replaced date, e.g. 2020-01-01 or 2020-01-01T00:00:00'
DOC_REFERENCE_PERIOD_START = 'The start date for which the data are applicable'
DOC_REFERENCE_PERIOD_END = 'The end date for which the data are applicable'

# Enumerations
DOC_COMMODITY_CATEGORY = f'Filter the response by the food group that the commodity belongs to, available values are described <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/enums/#commodity-category">here.</a>'
DOC_DISABLED_MARKER = f'Filter the response by the presence of disability disaggregation data, available values are described <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/enums/#disabled-marker">here.</a>'
DOC_ACLED_EVENT_TYPE = f'Filter the response by the ACLED event-type categories (non-mutually exclusive), available values are described <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/enums/#event-type">here.</a>'
DOC_GENDER = f'Filter the response by the gender, available values are described <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/enums/#gender">here.</a>'
DOC_IPC_PHASE = f'Filter the response by the IPC phase, available values are described <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/enums/#ipc-code">here.</a>'
DOC_IPC_TYPE = f'Filter the response by the IPC type, available values are described <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/enums/#ipc-type">here.</a>'
DOC_POPULATION_GROUP = f'Filter the response by the population group, available values are described <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/enums/#population-group">here.</a>'
DOC_POPULATION_STATUS = f'Filter the response by the population status, available values are described <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/enums/#population-status">here.</a>'
DOC_PRICE_FLAG = f'Filter the response by the pre-processing characteristics of food prices, available values are described <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/enums/#price-flag">here.</a>'
DOC_PRICE_TYPE = f'Filter the response by the point in the supply chain at which the price is determined, available values are described <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/enums/#price-type">here.</a>'
DOC_RISK_CLASS = f'Filter the response by the INFORM risk class, available values are described <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}data_usage_guides/enums/#risk-class">here.</a>'

# Humanitarian Response metadata

DOC_ORG_ACRONYM = 'Filter the response by the standard acronym used to represent the organization. When data is brought into the HDX HAPI database, an attempt is made to standardize the acronyms.'
DOC_ORG_NAME = 'Filter the response by the standard name used to represent the organization. When data is brought into the HDX HAPI database, an attempt is made to standardize the acronyms.'
DOC_ORG_TYPE_CODE = 'Filter the response by the organization type code.'
DOC_ORG_TYPE_DESCRIPTION = 'Filter the response by the organization type description.'
DOC_SECTOR_CODE = 'Filter the response by the sector code.'
DOC_SECTOR_NAME = 'Filter the response by the sector name.'
DOC_SEE_ORG_TYPE = 'See the <a href="/docs#/Metadata/get_org_types_api_v1_metadata_org_type_get" target="_blank">org type endpoint</a> for details.'


DOC_AGE_RANGE = 'Filter the response by the age range. These are expressed as [start age]-[end age], or [start age]+ for an age range starting at [start age] or above. The end age is assumed to be inclusive, though that is not always explicit in the source data.'
# Endpoints - Food prices
DOC_CURRENCY_CODE = 'Filter the response by the currency code.'


def truncate_query_description(query_description) -> str:
    # This function converts a query doc string which typically starts with `Filter the response by...`
    # to a doc string suitable to describe
    response_description = query_description.replace('Filter the response by ', '')
    # response_description = response_description.capitalize()
    if response_description.startswith('the'):
        response_description = 'The' + response_description[3:]
    if response_description.startswith('a'):
        response_description = 'A' + response_description[1:]
    return response_description
