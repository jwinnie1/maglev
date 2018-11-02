from typing import Dict, List, Any
from .middleware import MiddlewarePlugin, HTTPResponse
from urllib.parse import urlparse
import traceback
from termcolor import colored

class RouteHandler():
    data: Any
    prod: bool

    def __init__(self, data, prod):
        self.data = data
        self.prod = prod

    def handle_request(self, request):
        raise NotImplementedError()


RoutingTable = Dict[str, Dict[str, RouteHandler]]


class RouterMiddleware(MiddlewarePlugin):
    threaded = False
    routing_table: RoutingTable = {}

    def __init__(self, plugins: List[RoutingTable]):
        for plugin in plugins:
            self.routing_table = {**self.routing_table, **plugin}

    def handle(self, request, response):
        try:
            return self.routing_table[request.path.rstrip("/")][request.method].handle_request(request)
        except KeyError:
            try:
                return self.routing_table["404"]["ERROR"].handle_request(request)
            except KeyError:
                return HTTPResponse("text/html", "<h1>404: Not Found</h1>", 404)
        except:
            try:
                return self.routing_table["500"]["ERROR"].handle_request(request)
            except KeyError:
                return HTTPResponse("text/html", "<h1>500: Server Error</h1>", 500)
