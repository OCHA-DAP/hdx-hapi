from datetime import date

endpoint_data = {
    '/api/admin1': {
        'query_parameters': {
            'code': 'FoO-001',
            'name': 'Province 01',
            'location_code': 'FoO',
            'location_name': 'Foolandia',
        },
        'expected_fields': [
            'code',
            'name',
            'location_code',
            'location_name'
        ],
    },
    '/api/admin2': {
        'query_parameters': {
            'code': 'FoO-001-A',
            'name': 'District A',
            'admin1_code': 'FOo-001',
            'admin1_name': 'Province 01',
            'location_code': 'FOo',
            'location_name': 'Foolandia',
        },
        'expected_fields': [
            'code',
            'name',
            'admin1_code',
            'admin1_name',
            'location_code',
            'location_name'
        ],
    },
    '/api/age_range': {
        'query_parameters': {
            'code': '10-14'
        },
        'expected_fields': [
            'code',
            'age_min',
            'age_max'
        ],
    },
    '/api/dataset': {
        'query_parameters': {
            'hdx_id': 'c3f001fa-b45b-464c-9460-1ca79fd39b40',
            'title': 'Dataset #1',
            'hdx_provider_stub': 'Provider01',
            'hdx_provider_name': 'Provider #1',
        },
        'expected_fields': [
            'hdx_id',
            'hdx_stub',
            'title',
            'hdx_provider_stub',
            'hdx_provider_name',
            'hdx_link',  # computed field
            'hdx_api_link'  # computed field
        ],
    },
    '/api/gender': {
        'query_parameters': {
            'code': 'F',
            'name': 'female'
        },
        'expected_fields': [
            'code',
            'description'
        ],
    },
    '/api/location': {
        'query_parameters': {
            'code': 'foo',
            'name': 'Foolandia'
        },
        'expected_fields': [
            'code',
            'name'
        ],
    },
    '/api/themes/3W': {
        'query_parameters': {
            'sector_code': 'Shl',
            'dataset_hdx_provider_stub': 'PROVIDER01',
            'resource_update_date_min': date(2023, 6, 1),
            'resource_update_date_max': date(2023, 6, 2),
            'org_acronym': 'oRG01',
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
        'expected_fields': [
            'sector_code',
            'dataset_hdx_stub',
            'resource_hdx_id',
            'org_acronym',
            'org_name',
            'sector_name',
            'location_code',
            'location_name',
            'reference_period_start',
            'reference_period_end',
            'admin1_code',
            'admin1_name',
            'admin2_code',
            'admin2_name'
        ],
    },
    '/api/org': {
        'query_parameters': {
            'acronym': 'Org01',
            'name': 'Organisation 1',
            'org_type_code': '433',
            'org_type_description': 'Dono',  # Donor
        },
        'expected_fields': [
            'acronym',
            'name',
            'org_type_code',
            'org_type_description'
        ],
    },
    '/api/org_type': {
        'query_parameters': {
            'code': '431',
            'name': 'national'  # International
        },
        'expected_fields': [
            'code',
            'description'
        ],
    },
    '/api/themes/population': {
        'query_parameters': {
            'gender_code': 'X',
            'age_range_code': '10-14',
            'population': 1000000,
            'dataset_hdx_provider_stub': 'PROvider01',
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
        'expected_fields': [
            'gender_code',
            'age_range_code',
            'population',
            'reference_period_start',
            'reference_period_end',
            'dataset_hdx_stub',
            'resource_hdx_id',
            'location_code',
            'location_name',
            'admin1_code',
            'admin1_name',
            'admin2_code',
            'admin2_name'
        ],
    },
    '/api/population_group': {
        'query_parameters': {
            'code': 'refugees',
            'description': 'refugee'  # refugees
        },
        'expected_fields': [
            'code',
            'description'
        ],
    },
    '/api/population_status': {
        'query_parameters': {
            'code': 'inneed',
            'description': 'people'
        },
        'expected_fields': [
            'code',
            'description'
        ],
    },
    '/api/themes/food_security': {
        'query_parameters': {
            'ipc_phase_code': '1',
            'ipc_type_code': 'current',
            'dataset_hdx_provider_stub': 'PROvider01',
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
        'expected_fields': [
            'population_in_phase',
            'population_fraction_in_phase',
            'ipc_phase_code',
            'ipc_phase_name',
            'ipc_type_code',
            'reference_period_start',
            'reference_period_end',
            'dataset_hdx_stub',
            'dataset_hdx_provider_stub',
            'resource_hdx_id',
            'location_code',
            'location_name',
            'admin1_code',
            'admin1_name',
            'admin2_code',
            'admin2_name'
        ],
    },
    '/api/themes/national_risk': {
        'query_parameters': {
            'risk_class': 5,
            'global_rank': 4,
            'overall_risk': 8.1,
            'hazard_exposure_risk': 8.7,
            'vulnerability_risk': 8.5,
            'coping_capacity_risk': 7.1,
            'dataset_hdx_provider_stub': 'pRoViDeR01',
            'resource_update_date_min': date(2023, 6, 1),
            'resource_update_date_max': date(2023, 6, 2),
            # 'sector_name': 'Emergency Shelter and NFI',
            'location_code': 'fOO',
            'location_name': 'Foolandia',
        },
        'expected_fields': [
            'risk_class',
            'global_rank',
            'overall_risk',
            'hazard_exposure_risk',
            'vulnerability_risk',
            'coping_capacity_risk',
            'meta_missing_indicators_pct',
            'meta_avg_recentness_years',
            'reference_period_start',
            'reference_period_end',
            'dataset_hdx_stub',
            'dataset_hdx_provider_stub',
            'resource_hdx_id',
            # "sector_name",
            'location_code',
            'location_name'
        ],
    },
    '/api/themes/humanitarian_needs': {
        'query_parameters': {
            'gender_code': 'm',
            'age_range_code': '0-4',
            'disabled_marker': False,
            'sector_code': 'EDU',
            'sector_name': 'Education',
            'population_group_code': 'refugees',
            'population_status_code': 'inneed',
            'population': 100,
            'dataset_hdx_provider_stub': 'PROvider01',
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
        'expected_fields': [
            'gender_code',
            'age_range_code',
            'disabled_marker',
            'sector_code',
            'population_group_code',
            'population_status_code',
            'population',
            'reference_period_start',
            'reference_period_end',
            'dataset_hdx_stub',
            'dataset_hdx_provider_stub',
            'resource_hdx_id',
            'sector_name',
            'location_code',
            'location_name',
            'admin1_code',
            'admin1_name',
            'admin2_code',
            'admin2_name'
        ],
    },
    '/api/resource': {
        'query_parameters': {
            'hdx_id': '90deb235-1bf5-4bae-b231-3393222c2d01',
            'format': 'csv',
            'update_date_min': date(2023, 6, 1),
            'update_date_max': date(2023, 6, 2),
            'is_hxl': True,
            'dataset_hdx_id': 'c3f001fa-b45b-464c-9460-1ca79fd39b40',
            'dataset_title': 'Dataset #1',
            'dataset_hdx_provider_stub': 'pRoViDeR01',
            'dataset_hdx_provider_name': 'Provider #1',
        },
        'expected_fields': [
            'hdx_id',
            'name',
            'format',
            'update_date',
            'is_hxl',
            'download_url',
            'dataset_hdx_id',
            'dataset_hdx_stub',
            'dataset_title',
            'dataset_hdx_provider_stub',
            'dataset_hdx_provider_name',
            'hdx_link',  # computed field
            'hdx_api_link',  # computed field
            'dataset_hdx_link',  # computed field
            'dataset_hdx_api_link',  # computed field
        ],
    },
    '/api/sector': {
        'query_parameters': {
            'code': 'Pro',
            'name': 'Protect'  # Protection
        },
        'expected_fields': [
            'code',
            'name'
        ],
    },
}
