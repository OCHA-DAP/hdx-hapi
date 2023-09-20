import pytest
import logging
from hdx_hapi.config.config import CONFIG, get_config
from hdx_hapi.processing.helpers import Context, get_dataset_url, get_dataset_api_url, get_organization_url

from main import app

log = logging.getLogger(__name__)

config = get_config()
context = Context(config=config)

def test_helper_get_dataset_url():
    log.info('started test_helper_get_dataset_url')

    dataset_id = 'test-dataset'
    dataset_url = get_dataset_url(context=context, dataset_id=dataset_id)

    assert dataset_url == 'https://data.humdata.org/dataset/%s' % (dataset_id)

def test_helper_get_dataset_api_url():
    log.info('started test_helper_get_dataset_api_url')

    dataset_id = 'test-api-dataset'
    dataset_url = get_dataset_api_url(context=context, dataset_id=dataset_id)

    assert dataset_url == 'https://data.humdata.org/api/action/package_show?id=%s' % (dataset_id)

def test_helper_get_organization_url():
    log.info('started test_helper_get_organization_url')

    org_id = 'test-organization'
    dataset_url = get_organization_url(context=context, org_id=org_id)

    assert dataset_url == 'https://data.humdata.org/organization/%s' % (org_id)
