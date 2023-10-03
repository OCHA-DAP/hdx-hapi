import logging
from pydantic import HttpUrl
from dataclasses import dataclass
from hdx_hapi.config.config import Config

logger = logging.getLogger(__name__)

from hdx_hapi.config.config import get_config

CONFIG = get_config()

def get_dataset_url(dataset_id: str) -> HttpUrl:
    """Creates the full HDX URL for a dataset
    
    Args:
        context (Context): 
        dataset_id (str): Dataset id or name
    Returns:
        str: HDX URL for the specified dataset
    """    
    domain = CONFIG.HDX_DOMAIN
    dataset_url = CONFIG.HDX_DATASET_URL
    if not domain:
        logger.warning('HDX_DOMAIN environment variable is not set.')

    url=dataset_url.format(domain=domain, dataset_id=dataset_id)
    return HttpUrl(url=url)

def get_dataset_api_url(dataset_id: str) -> HttpUrl:
    """Creates the full HDX API URL for a dataset
    
    Args:
        context (Context): 
        dataset_id (str): Dataset id or name
    Returns:
        str: HDX API URL for the specified dataset (package_show)
    """    
    domain = CONFIG.HDX_DOMAIN
    dataset_api_url = CONFIG.HDX_DATASET_API_URL
    if not domain:
        logger.warning('HDX_DOMAIN environment variable is not set.')

    url=dataset_api_url.format(domain=domain, dataset_id=dataset_id)
    return HttpUrl(url=url)


def get_resource_url(dataset_id: str, resource_id: str) -> HttpUrl:
    """Creates the full HDX URL for a dataset
    
    Args:
        context (Context): 
        dataset_id (str): Dataset id or name
    Returns:
        str: HDX URL for the specified dataset
    """    
    domain = CONFIG.HDX_DOMAIN
    resource_url = CONFIG.HDX_RESOURCE_URL
    if not domain:
        logger.warning('HDX_DOMAIN environment variable is not set.')

    url=resource_url.format(domain=domain, dataset_id=dataset_id, resource_id=resource_id)
    return HttpUrl(url=url)

def get_resource_api_url(resource_id: str) -> HttpUrl:
    """Creates the full HDX API URL for a dataset
    
    Args:
        context (Context): 
        dataset_id (str): Dataset id or name
    Returns:
        str: HDX API URL for the specified dataset (package_show)
    """    
    domain = CONFIG.HDX_DOMAIN
    resource_api_url = CONFIG.HDX_RESOURCE_API_URL
    if not domain:
        logger.warning('HDX_DOMAIN environment variable is not set.')

    url=resource_api_url.format(domain=domain, resource_id=resource_id)
    return HttpUrl(url=url)


def get_organization_url(org_id: str) -> HttpUrl:
    """Creates the full HDX URL for an organization

    Args:
        context (Context): 
        org_id (str): Organization id or name

    Returns:
        str: HDX URL for the specified organization
    """    
    domain = CONFIG.HDX_DOMAIN
    organization_url = CONFIG.HDX_ORGANIZATION_URL
    if not domain:
        logger.warning('HDX_DOMAIN environment variable is not set.')
        
    url = organization_url.format(domain=domain, org_id=org_id)
    return HttpUrl(url=url)