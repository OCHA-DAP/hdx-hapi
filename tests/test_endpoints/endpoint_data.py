from datetime import date

endpoint_data = {
    "/api/admin1": {
        "query_parameters": {
            "code": "FoO-001",
            "name": "Province 01",
            "location_code": "FoO",
            "location_name": "Foolandia",
        },
        "expected_fields": [
            "code",
            "name",
            "location_code",
            "location_name"
        ],
    },
    "/api/admin2": {
        "query_parameters": {
            'code': 'FoO-001-A',
            'name': 'District A',
            'admin1_code': 'FOo-001',
            'admin1_name': 'Province 01',
            'location_code': 'FOo',
            'location_name': 'Foolandia',
        },
        "expected_fields": [
            "code",
            "name",
            "admin1_code",
            "admin1_name",
            "location_code",
            "location_name"
        ],
    },
    "/api/age_range": {
        "query_parameters": {
            'code': '10-14'
        },
        "expected_fields": [
            "code",
            "age_min",
            "age_max"
        ],
    },
    "/api/dataset": {
        "query_parameters": {
            'hdx_id': 'c3f001fa-b45b-464c-9460-1ca79fd39b40',
            'title': 'Dataset #1',
            'provider_code': 'Provider01',
            'provider_name': 'Provider #1',
        },
        "expected_fields": [
            "hdx_id",
            "hdx_stub",
            "title",
            "provider_code",
            "provider_name",
            "hdx_link",  # computed field
            "hdx_api_link"  # computed field
        ],
    },
    "/api/gender": {
        "query_parameters": {
            'code': 'F',
            'name': 'female'
        },
        "expected_fields": [
            "code",
            "description"
        ],
    },
    "/api/location": {
        "query_parameters": {
            'code': 'foo',
            'name': 'Foolandia'
        },
        "expected_fields": [
            "code",
            "name"
        ],
    },
    "/api/themes/3W": {
        "query_parameters": {
            'sector_code': 'Shl',
            'dataset_provider_code': 'PROVIDER01',
            'resource_update_date_min': date(2023, 6, 1),
            'resource_update_date_max': date(2023, 6, 2),
            'org_acronym': 'ORG01',
            'org_name': 'Organisation 1',
            'sector_name': 'Emergency Shelter and NFI',
            'location_code': 'foo',
            'location_name': 'Foolandia',
            'admin1_code': 'foo-001',
            'admin1_is_unspecified': False,
            'admin2_code': 'foo-001-xxx',
            'admin2_name': 'Unspecified',
            'admin2_is_unspecified': True,
        },
        "expected_fields": [
            "sector_code",
            "dataset_hdx_stub",
            "resource_hdx_id",
            "org_acronym",
            "org_name",
            "sector_name",
            "location_code",
            "location_name",
            "admin1_code",
            "admin1_name",
            "admin2_code",
            "admin2_name"
        ],
    },
    "/api/org": {
        "query_parameters": {
            'acronym': 'ORG01',
            'name': 'Organisation 1',
            'org_type_description': 'Dono',  # Donor
        },
        "expected_fields": [
            "acronym",
            "name",
            "org_type_code",
            "org_type_description"
        ],
    },
    "/api/org_type": {
        "query_parameters": {
            'code': '431',
            'name': 'national'  # International
        },
        "expected_fields": [
            "code",
            "description"
        ],
    },
    "/api/themes/population": {
        "query_parameters": {
            'gender_code': 'X',
            'age_range_code': '10-14',
            'population': 1000000,
            'dataset_provider_code': 'PROvider01',
            'resource_update_date_min': date(2023, 6, 1),
            'resource_update_date_max': date(2023, 6, 2),
            'location_code': 'fOO',
            'location_name': 'Foolandia',
            'admin1_code': 'FOO-xxx',
            'admin1_is_unspecified': True,
            'admin2_code': 'FOO-xxx-XXX',
            'admin2_name': 'Unspecified',
            'admin2_is_unspecified': True,
        },
        "expected_fields": [
            "gender_code",
            "age_range_code",
            "population",
            "dataset_hdx_stub",
            "resource_hdx_id",
            "location_code",
            "location_name",
            "admin1_code",
            "admin1_name",
            "admin2_code",
            "admin2_name"
        ],
    },
    "/api/resource": {
        "query_parameters": {
            'hdx_id': '90deb235-1bf5-4bae-b231-3393222c2d01',
            'format': 'csv',
            'update_date_min': date(2023, 6, 1),
            'update_date_max': date(2023, 6, 2),
            'is_hxl': True,
            'dataset_hdx_id': 'c3f001fa-b45b-464c-9460-1ca79fd39b40',
            'dataset_title': 'Dataset #1',
            'dataset_provider_code': 'pRoViDeR01',
            'dataset_provider_name': 'Provider #1',
        },
        "expected_fields": [
            "hdx_id",
            "filename",
            "format",
            "update_date",
            "is_hxl",
            "download_url",
            "dataset_hdx_id",
            "dataset_hdx_stub",
            "dataset_title",
            "dataset_provider_code",
            "dataset_provider_name",
            "hdx_link",  # computed field
            "hdx_api_link",  # computed field
            "dataset_hdx_link",  # computed field
            "dataset_hdx_api_link",  # computed field
        ],
    },
    "/api/sector": {
        "query_parameters": {
            'code': 'Pro',
            'name': 'Protect'  # Protection
        },
        "expected_fields": [
            "code",
            "name"
        ],
    },
}
