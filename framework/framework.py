from .http_entities import Request


import os
PYCHARM_DEBUG_ENV = 'PYCHARM_DEBUG'
if PYCHARM_DEBUG_ENV in os.environ and os.environ[PYCHARM_DEBUG_ENV] == 'True':
    from . import debug
    debug.set_debug_environment()


route_mapping = {}


def application(environ, start_response):
    verb = environ['REQUEST_METHOD']
    path = environ['PATH_INFO']
    parameters = get_parameters(environ['QUERY_STRING'])
    headers = get_headers(environ)

    content_length = int(environ.get('CONTENT_LENGTH', 0))
    body = environ['wsgi.input'].read(content_length)

    request = Request(verb, path, parameters, headers, body)

    response = route_mapping[path](request)

    prepared_headers = list(response.headers.items())

    start_response(response.status, prepared_headers)
    return prepare_body(response.body)


def get_parameters(query_string):
    params_dict = {}
    for pair in query_string.split('&'):
        if not pair:
            continue

        key, value = tuple(pair.split('='))
        params_dict[key] = value

    return params_dict


def get_headers(environ):
    headers = {k[5:].lower(): v for k, v in environ.items() if k.startswith('HTTP_')}
    headers['content_type'] = get_content_type(environ)
    headers['content_length'] = get_content_length(environ)

    return headers


def get_content_length(environ):
    content_type_key = 'CONTENT_LENGTH'
    return get_standard_header(content_type_key, environ)


def get_content_type(environ):
    content_type_key = 'CONTENT_TYPE'
    return get_standard_header(content_type_key, environ)


def get_standard_header(content_type_key, environ):
    if content_type_key not in environ.keys():
        return None
    return environ[content_type_key]


def prepare_body(body):
    if isinstance(body, str):
        return [body.encode()]
    if isinstance(body, bytes):
        return body
