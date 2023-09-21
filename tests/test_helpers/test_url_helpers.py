import pytest
import logging
from hdx_hapi.config.config import CONFIG, get_config
from hdx_hapi.endpoints.models.dataset_view import DatasetViewPydantic
from hdx_hapi.endpoints.models.org_view import OrgViewPydantic
from hdx_hapi.services.hdx_url_logic import get_dataset_url, get_dataset_api_url, get_organization_url

from datetime import date

from main import app

log = logging.getLogger(__name__)

config = get_config()

def test_helper_get_dataset_url():
    log.info('started test_helper_get_dataset_url')

    dataset_id = 'test-dataset'
    excepted_link = 'https://data.humdata.org/dataset/%s/' % (dataset_id)

    dataset_url = get_dataset_url(dataset_id=dataset_id)

    assert dataset_url == excepted_link

    dataset_view = DatasetViewPydantic(
        hdx_id=dataset_id,
        hdx_stub=dataset_id,
        title='Test Dataset #1',
        provider_code='test-provider',
        provider_name='Test Provider'
    )

    assert dataset_view.hdx_link == excepted_link

def test_helper_get_dataset_api_url():
    log.info('started test_helper_get_dataset_api_url')

    dataset_id = 'test-api-dataset'
    excepted_link = 'https://data.humdata.org/api/action/package_show?id=%s' % (dataset_id)

    dataset_api_url = get_dataset_api_url(dataset_id=dataset_id)

    assert dataset_api_url == excepted_link

    dataset_view = DatasetViewPydantic(
        hdx_id=dataset_id,
        hdx_stub=dataset_id,
        title='Test Dataset #2',
        provider_code='test-provider2',
        provider_name='Test Provider 2'
    )

    assert dataset_view.api_link == excepted_link

def test_helper_get_organization_url():
    log.info('started test_helper_get_organization_url')

    org_id = 'test-organization'
    excepted_link = 'https://data.humdata.org/organization/%s' % (org_id)

    org_url = get_organization_url(org_id=org_id)

    assert org_url == excepted_link

    org_view = OrgViewPydantic(
        acronym=org_id,
        name='Test Dataset',
        reference_period_start=date(2000, 1, 1),
        reference_period_end=None
    )

    assert org_view.hdx_link == excepted_link
