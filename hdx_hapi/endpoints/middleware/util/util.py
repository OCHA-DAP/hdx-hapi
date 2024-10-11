import logging
import hashlib
import time
import ua_parser.user_agent_parser as useragent
from typing import Optional, Tuple, List
from urllib.parse import parse_qs, urlparse, unquote
from fastapi import Request, Response

from hdx_hapi.config.config import get_config


logger = logging.getLogger(__name__)

_CONFIG = get_config()


async def track_api_call(request: Request, response: Response):
    is_nginx_verify_request = getattr(request.state, 'is_nginx_verify_request', False)

    if is_nginx_verify_request:
        endpoint, query_params_keys, output_format, admin_level, current_url = _parse_nginx_header(request)
    else:
        endpoint, query_params_keys, output_format, admin_level, current_url = _parse_fastapi_request(request)

    app_name = getattr(request.state, 'app_name', None)
    user_agent_string = request.headers.get('user-agent', '')
    ip_address = request.headers.get('x-forwarded-for', '')
    response_code = response.status_code

    distinct_id = HashCodeGenerator({'ip': ip_address, 'ua': user_agent_string}).compute_hash()
    event_time = time.time()

    ua_os, ua_browser, ua_browser_version = _parse_user_agent(user_agent_string)

    mixpanel_dict = {
        'endpoint path': endpoint,
        'query params': query_params_keys,
        'time': event_time,
        'app name': app_name,
        'identifier verification': is_nginx_verify_request,
        'output format': output_format,
        'admin level': admin_level,
        'server side': True,
        'response code': response_code,
        'user agent': user_agent_string,
        'ip': ip_address,
        '$os': ua_os,
        '$browser': ua_browser,
        '$browser_version': ua_browser_version,
        '$current_url': current_url,
    }
    await send_mixpanel_event('hapi api call', distinct_id, mixpanel_dict)


async def track_page_view(request: Request, response: Response):
    is_nginx_verify_request = getattr(request.state, 'is_nginx_verify_request', False)

    if is_nginx_verify_request:
        _, _, _, _, current_url = _parse_nginx_header(request)
    else:
        _, _, _, _, current_url = _parse_fastapi_request(request)

    user_agent_string = request.headers.get('user-agent', '')
    ip_address = request.headers.get('x-forwarded-for', '')
    response_code = response.status_code

    distinct_id = HashCodeGenerator({'ip': ip_address, 'ua': user_agent_string}).compute_hash()
    event_time = time.time()

    ua_os, ua_browser, ua_browser_version = _parse_user_agent(user_agent_string)

    page_view_dict = {
        'page title': 'HDX HAPI - OpenAPI Docs',
        'time': event_time,
        'identifier verification': is_nginx_verify_request,
        'server side': True,
        'response code': response_code,
        'user agent': user_agent_string,
        'ip': ip_address,
        '$os': ua_os,
        '$browser': ua_browser,
        '$browser_version': ua_browser_version,
        '$current_url': current_url,
    }
    await send_mixpanel_event('hapi openapi docs view', distinct_id, page_view_dict)


async def send_mixpanel_event(event_name: str, distinct_id: str, event_data: dict):
    _CONFIG.MIXPANEL.track(distinct_id, event_name, event_data)  # pyright: ignore[reportOptionalMemberAccess]


def extract_path_identifier_and_query_params(original_url: str) -> Tuple[str, Optional[str], dict]:
    """
    Extract the path, app_identifier and query parameters from the Nginx header.
    Args:
        original_url: The original URL from the Nginx header
    Returns:
        Tuple of path, app_identifier and query parameters
    """

    parsed_url = urlparse(original_url)
    path = parsed_url.path
    query_params = parse_qs(parsed_url.query)
    app_identifier = query_params.get('app_identifier', [None])[0]
    return path, app_identifier, query_params


def _parse_fastapi_request(request: Request) -> Tuple[str, List[str], str, str, str]:
    """
    Parse the FastAPI request to extract data needed for analytics.

    Args:
        request: The FastAPI request object

    Returns:
        Tuple containing endpoint, query_params_keys, output_format, admin_level and current_url
    """
    app_identifier = request.query_params.get('app_identifier', '')
    endpoint = request.url.path

    query_params_keys = list(request.query_params.keys())
    output_format = request.query_params.get('output_format', '')
    admin_level = request.query_params.get('admin_level', '')
    email_address = request.query_params.get('email', '')

    current_url = unquote(str(request.url))

    if app_identifier:
        current_url = current_url.replace(app_identifier, 'unavailable')
    if email_address:
        current_url = current_url.replace(email_address, 'unavailable')

    return endpoint, query_params_keys, output_format, admin_level, current_url


def _parse_nginx_header(request: Request) -> Tuple[str, List[str], str, str, str]:
    """
    Parse nginx headers to extract data needed for analytics.

    Args:
        request: The FastAPI request object.

    Returns:
        Tuple containing endpoint, query_params_keys, output_format, admin_level and current_url
    """
    original_uri_from_nginx = request.headers.get('X-Original-URI')
    assert original_uri_from_nginx is not None
    endpoint, app_identifier, query_params = extract_path_identifier_and_query_params(original_uri_from_nginx)

    query_params_keys = list(query_params.keys())
    output_format = query_params.get('output_format', [''])[0]
    admin_level = query_params.get('admin_level', [''])[0]
    email_address = query_params.get('email', [''])[0]

    protocol = request.headers.get('x-forwarded-proto', '')
    host = request.headers.get('x-forwarded-host', '')
    current_url = unquote(f'{protocol}://{host}{original_uri_from_nginx}')

    if app_identifier:
        current_url = current_url.replace(app_identifier, 'unavailable')
    if email_address:
        current_url = current_url.replace(email_address, 'unavailable')

    return endpoint, query_params_keys, output_format, admin_level, current_url


def _parse_user_agent(user_agent: str) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """
    Parse the user agent string to extract the operating system, browser, and browser version.

    Args:
        user_agent: The user agent string to be parsed

    Returns:
        A tuple containing the operating system, browser, and browser version
    """
    ua_dict = useragent.Parse(user_agent)
    ua_os = ua_dict.get('os', {}).get('family')
    ua_browser = ua_dict.get('user_agent', {}).get('family')
    ua_browser_version = ua_dict.get('user_agent', {}).get('major')

    return ua_os, ua_browser, ua_browser_version


class HashCodeGenerator(object):
    """
    Works only on simple dictionaries (not nested). At least the specified fields need to not be nested.
    """

    def __init__(self, src_dict, field_list=None):
        if not field_list and src_dict:
            field_list = list(src_dict.keys())

        assert field_list is not None
        field_list.sort()
        try:
            self.__inner_string = ''
            if field_list and src_dict:
                for field in field_list:
                    self.__inner_string += '{}-{},'.format(field, src_dict.get(field))
            else:
                raise Exception('Either field list or source dict are null')
        except Exception:
            raise Exception('Exception while trying to generate hash code')

    def compute_hash(self):
        hash_builder = hashlib.md5()
        hash_builder.update(self.__inner_string.encode())
        hash_code = hash_builder.hexdigest()
        logger.debug('Generated code for {} is {}'.format(self.__inner_string, hash_code))
        return hash_code
