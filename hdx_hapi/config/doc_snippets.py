from hdx_hapi.config.config import get_config

CONFIG = get_config()

DOC_ADMIN1_REF = 'Filter the response by the 1st subnational administrative reference number. The admin1 reference is intended as a stable identifier which will not change if, for example, admin1 name changes'
DOC_ADMIN1_CODE = 'Filter the response by the 1st subnational administrative divisions. The admin1 codes refer to the p-codes in the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a>.'
DOC_ADMIN1_NAME = 'Filter the response by the 1st subnational administrative divisions. The admin1 names refer to the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a>.'
DOC_ADMIN2_REF = 'Filter the response by the 2nd subnational administrative reference number. The admin2 reference is intended as a stable identifier which will not change if, for example, admin2 name changes'
DOC_ADMIN2_CODE = 'Filter the response by the 2nd subnational administrative divisions. The admin2 codes refer to the p-codes in the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a>.'
DOC_ADMIN2_NAME = 'Filter the response by the 2nd subnational administrative divisions. The admin2 names refer to the <a href="https://data.humdata.org/dashboards/cod?">Common Operational Datasets</a>.'
DOC_AGE_RANGE_SUMMARY = 'Get the list of age ranges used for disaggregating population data'
DOC_AGE_RANGE = 'Filter the response by the age range. These are expressed as [start age]-[end age]. The end age is assumed to be inclusive, though that is not always explicit in the source data.'
DOC_GENDER_SUMMARY = 'Get the list of gender codes used for disaggregating population data'
DOC_GENDER_CODE = 'Filter the response by the gender code.'
DOC_GENDER = 'Filter the response by the gender. f (female), m (male), x (non-binary), u (unspecified), o (other) and all (a sum over all genders)'
DOC_GENDER_DESCRIPTION = 'Filter the response by the gender description.'
DOC_HDX_DATASET_ID = 'Filter the response by the dataset ID (hdx_id), which is a unique and fixed identifier of a Dataset on HDX. A URL in the pattern of `https://data.humdata.org/dataset/[hdx_id]` will load the dataset page on HDX.'
DOC_HDX_DATASET_NAME = 'Filter the response by the URL-safe name (hdx_stub) of the dataset as displayed on HDX. This name is unique but can change. A URL in the pattern of `https://data.humdata.org/dataset/[hdx_stub]` will load the dataset page on HDX.'
DOC_HDX_DATASET_TITLE = 'Filter the response by the title of the dataset as it appears in the HDX interface. This name is not unique and can change.'
DOC_HDX_PROVIDER_STUB = "Filter the response by the code of the provider (organization) of the dataset on HDX. A URL in the pattern of `https://data.humdata.org/organization/[hdx_provider_stub]` will load the provider's page on HDX."
DOC_HDX_PROVIDER_NAME = 'Filter the response by the display name of the provider (organization) of the dataset on HDX.'
DOC_HDX_RESOURCE_ID = 'Filter the response by the resource ID (hdx_id), which is a unique and fixed identifier of a resource on HDX. A URL in the pattern of `https://data.humdata.org/dataset/[dataset_hdx_id]/resource/[hdx_id]` will load the resource page on HDX.'
DOC_HDX_RESOURCE_FORMAT = 'Filter the response by the format of the resource on HDX. These are typically file formats (i.e. CSV, XLSX), but can also include APIs and web apps.'
DOC_HDX_RESOURCE_HXL = (
    'Filter the response by whether or not the resource contains <a href="https://hxlstandard.org/">HXL tags</a>.'
)
DOC_HDX_DATASET_IN_RESOURCE_ID = 'Filter the response by the dataset ID (dataset_hdx_id), which is a unique and fixed identifier of a dataset on HDX. A URL in the pattern of `https://data.humdata.org/dataset/[dataset_hdx_id]` will load the dataset page on HDX. '
DOC_HDX_DATASET_IN_RESOURCE_NAME = 'Filter the response by the URL-safe name (dataset_hdx_stub) of the dataset as displayed on HDX. This name is unique but can change. A URL in the pattern of `https://data.humdata.org/dataset/[dataset_hdx_stub]` will load the dataset page on HDX.'
DOC_HDX_PROVIDER_IN_RESOURCE_STUB = "Filter the response by the code of the provider (organization) of the dataset on HDX. A URL in the pattern of `https://data.humdata.org/organization/[dataset_hdx_provider_stub]` will load the provider's page on HDX."
DOC_LOCATION_REF = 'Filter the response by a location (typically a country) reference number. The location reference is intended as a stable identifier which will not change if, for example location name changes'
DOC_LOCATION_CODE = 'Filter the response by a location (typically a country). The location codes use the ISO-3 (ISO 3166 alpha-3) codes.'
DOC_LOCATION_NAME = 'Filter the response by a location (typically a country). The location names are based on the "short name" from the <a href="https://unstats.un.org/unsd/methodology/m49/#fn2">UN M49 Standard</a>.'
DOC_ORG_ACRONYM = 'Filter the response by the standard acronym used to represent the organization. When data is brought into the HDX HAPI database, an attempt is made to standardize the acronyms.'
DOC_ORG_NAME = 'Filter the response by the standard name used to represent the organization. When data is brought into the HDX HAPI database, an attempt is made to standardize the acronyms.'
DOC_ORG_TYPE_CODE = 'Filter the response by the organization type code.'
DOC_ORG_TYPE_DESCRIPTION = 'Filter the response by the organization type description.'
DOC_SCOPE_DISCLAIMER = f'Not all data are available for all locations. Learn more about the scope of data coverage in HDX HAPI in the <a href="{CONFIG.HAPI_READTHEDOCS_OVERVIEW_URL}">Overview and Getting Started</a> documentation.'
DOC_SECTOR_CODE = 'Filter the response by the sector code.'
DOC_SECTOR_NAME = 'Filter the response by the sector name.'
DOC_UPDATE_DATE_MIN = 'Min date of update date, e.g. 2020-01-01 or 2020-01-01T00:00:00'
DOC_UPDATE_DATE_MAX = 'Max date of update date, e.g. 2020-01-01 or 2020-01-01T00:00:00'
DOC_HAPI_UPDATED_DATE_MIN = 'Min date of HDX HAPI updated date, e.g. 2020-01-01 or 2020-01-01T00:00:00'
DOC_HAPI_UPDATED_DATE_MAX = 'Max date of HDX HAPI updated date, e.g. 2020-01-01 or 2020-01-01T00:00:00'
DOC_HAPI_REPLACED_DATE_MIN = 'Min date of HDX HAPI replaced date, e.g. 2020-01-01 or 2020-01-01T00:00:00'
DOC_HAPI_REPLACED_DATE_MAX = 'Max date of HDX HAPI replaced date, e.g. 2020-01-01 or 2020-01-01T00:00:00'

DOC_SEE_ADMIN1 = 'See the <a href="/docs#/Metadata/get_admin1_api_v1_metadata_admin1_get" target="_blank">admin1 endpoint</a> for details.'
DOC_SEE_ADMIN2 = 'See the <a href="/docs#/Metadata/get_admin2_api_v1_metadata_admin2_get" target="_blank">admin2 endpoint</a> for details.'
DOC_SEE_DATASET = 'See the <a href="/docs#/Metadata/get_datasets_api_v1_metadata_dataset_get" target="_blank">dataset endpoint</a> for details.'
DOC_SEE_LOC = 'See the <a href="/docs#/Metadata/get_locations_api_v1_metadata_location_get" target="_blank">location endpoint</a> for details.'
DOC_SEE_ORG_TYPE = 'See the <a href="/docs#/Metadata/get_org_types_api_v1_metadata_org_type_get" target="_blank">org type endpoint</a> for details.'

DOC_CURRENCY_CODE = 'Filter the response by the currency code.'
