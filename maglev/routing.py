from typing import Dict, List
from .middleware import MiddlewarePlugin, HTTPResponse
from urllib.parse import urlparse

class RouteHandler():
    def __init__(self, data):
        self.data = data

    def handle_request(self, request):
        raise NotImplementedError()


RoutingTable = Dict[str, Dict[str, RouteHandler]]


class RouterMiddleware(MiddlewarePlugin):
    threaded = False
    routing_table: RoutingTable = {}

    def __init__(self, plugins: List[RoutingTable]):
        for plugin in plugins:
            self.routing_table = {**self.routing_table, **plugin}
        print(self.routing_table)

    def handle(self, request, response):
        try:
            return self.routing_table[request.path.rstrip("/")][request.method].handle_request(request)
        except KeyError:
            try:
                return self.routing_table["404"]["ERROR"].handle_request(request)
            except KeyError:
                return HTTPResponse("text/html", "<h1>404: Not Found</h1>", 404)
