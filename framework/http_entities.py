class HTTPEntity:

    def __init__(self, headers, body):
        self.headers = headers
        self.body = body


class Request(HTTPEntity):

    def __init__(self, verb, path, parameters, headers, body):
        self.verb = verb
        self.path = path
        self.parameters = parameters
        super().__init__(headers, body)


class Response(HTTPEntity):

    def __init__(self, status, headers, body):
        self.status = status
        super().__init__(headers, body)
