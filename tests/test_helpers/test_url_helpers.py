import logging
from pydantic import HttpUrl, TypeAdapter
from hdx_hapi.config.config import get_config
from hdx_hapi.endpoints.models.hdx_metadata import DatasetResponse
from hdx_hapi.services.hdx_url_logic import get_dataset_url, get_dataset_api_url


log = logging.getLogger(__name__)

config = get_config()


def test_helper_get_dataset_url():
    log.info('started test_helper_get_dataset_url')

    dataset_id = 'test-dataset'

    AdaptedTypeURL = TypeAdapter(HttpUrl)
    expected_link = AdaptedTypeURL.validate_strings(f'https://data.humdata.org/dataset/{dataset_id}')

    dataset_url = get_dataset_url(dataset_id=dataset_id)

    assert dataset_url == expected_link

    dataset_view = DatasetResponse(
        dataset_hdx_id=dataset_id,
        dataset_hdx_stub=dataset_id,
        dataset_hdx_title='Test Dataset #1',
        hdx_provider_stub='test-provider',
        hdx_provider_name='Test Provider',
    )

    assert dataset_view.hdx_link == expected_link


def test_helper_get_dataset_api_url():
    log.info('started test_helper_get_dataset_api_url')

    dataset_id = 'test-api-dataset'

    AdaptedTypeURL = TypeAdapter(HttpUrl)
    expected_link = AdaptedTypeURL.validate_strings(f'https://data.humdata.org/api/action/package_show?id={dataset_id}')

    dataset_api_url = get_dataset_api_url(dataset_id=dataset_id)

    assert dataset_api_url == expected_link

    dataset_view = DatasetResponse(
        dataset_hdx_id=dataset_id,
        dataset_hdx_stub=dataset_id,
        dataset_hdx_title='Test Dataset #2',
        hdx_provider_stub='test-provider2',
        hdx_provider_name='Test Provider 2',
    )

    assert dataset_view.hdx_api_link == expected_link


# def test_helper_get_organization_url():
#     log.info('started test_helper_get_organization_url')

#     org_id = 'test-organization'
#     expected_link = HttpUrl(url='https://data.humdata.org/organization/%s' % (org_id))

#     org_url = get_organization_url(org_id=org_id)

#     assert org_url == expected_link

#     org_view = OrgResponse(
#         acronym=org_id,
#         name='Test Org',
#         org_type_code='Test Org Type Code',
#         org_type_description='Test Org Type Description'
#     )

#     assert org_view.hdx_link == expected_link
