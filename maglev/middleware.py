from typing import Any


class HTTPResponse:
    content_type: str
    body: Any
    status_code: int

    def __init__(self, content_type=None, body=None, status_code=None):
        if content_type:
            self.content_type = content_type
        if body:
            self.body = body
        if status_code:
            self.status_code = status_code


class MiddlewarePlugin:
    threaded: bool

    def handle(self, request, response: HTTPResponse):
        raise NotImplementedError()


class LoggerMiddleware(MiddlewarePlugin):
    threaded = True

    def handle(self, request, response):
        print(f"{request.method} {request.rel_url} => {response.status_code}")
