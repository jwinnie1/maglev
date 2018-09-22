from .middleware import HTTPResponse
from mako.lookup import TemplateLookup
from .routing import RouteHandler, RoutingTable
from pathlib import Path


class PageRouteHandler(RouteHandler):
    def handle_request(self, request):
        return HTTPResponse(
            "text/html",
            self.data.render(request=request),
            200
        )


class ErrorRouteHandler(RouteHandler):
    def __init__(self, data, code):
        self.data = data
        self.code = code

    def handle_request(self, request):
        return HTTPResponse(
            "text/html",
            self.data.render(request=request),
            self.code
        )


def routing_plugin_pages(pages_path: Path) -> RoutingTable:
    output = {}
    lookup = TemplateLookup(
        directories=[pages_path.absolute()],
        module_directory=pages_path.parent / ".cache" / "pages",
    )
    for page in pages_path.iterdir():
        if page.suffix == ".mako":
            if page.stem.startswith("_"):
                continue
            if page.stem == "404":
                output["404"] = {
                    "ERROR": ErrorRouteHandler(lookup.get_template(page.name), 404)
                }
            elif page.stem == "index":
                output["/"] = {
                    "GET": PageRouteHandler(lookup.get_template(page.name))
                }
            else:
                output["/" + page.stem] = {
                    "GET": PageRouteHandler(lookup.get_template(page.name))
                }
    return output
