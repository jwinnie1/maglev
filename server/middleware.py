from typing import Any
from termcolor import colored


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
    mode = "minimal_colorized"

    def handle(self, request, response):
        if self.mode == "dump":
            print(request.__dict__, response.__dict__)
        elif self.mode == "minimal":
            print(f"{request.method} {request.rel_url} => {response.status_code}")
        elif self.mode == "minimal_colorized":
            if response.status_code == 404:
                status = colored(response.status_code, "red")
            else:
                status = colored(response.status_code, "green")
            print(f"{request.method} {request.rel_url} => {status}")
        else:
            print(colored("warn", "red") + f": logger mode '{self.mode}' not valid")
