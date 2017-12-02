import json

from framework.http_entities import Response
from framework.framework import route_mapping

# this is needed for uwsgi to correctly connect to the module
from framework.framework import application
# and this is for the "unused import statement" warning not to show up
application = application


def root(request):
    template = 'Your query parameters are:\n{}'

    parameters = request.parameters
    json_parameters = json.dumps(parameters, indent=4)
    response_body = template.format(json_parameters)

    headers = {
        'content-type': 'text/html',
        'content-length': str(len(response_body)),
    }
    return Response('200 OK', headers, response_body)


def echo(request):
    return Response('200 OK', request.headers, request.body)


route_mapping['/'] = root
route_mapping['/echo'] = echo
