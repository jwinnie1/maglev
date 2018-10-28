from .middleware import HTTPResponse
from mako.lookup import TemplateLookup
from .routing import RouteHandler, RoutingTable
from pathlib import Path
from termcolor import colored


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

def index_route(idx: RoutingTable, lookup: TemplateLookup, path: Path, url_root: str = ""):
    for page in path.iterdir():
        if page.suffix == ".mako":
            if page.stem.startswith("_"):
                continue
            if page.stem == "404":
                if url_root == "":
                    idx["404"] = {
                        "ERROR": ErrorRouteHandler(lookup.get_template(page.name), 404)
                    }
                else:
                    print(colored("warn", "red") + ": 404 page cannot be in a subdirectory")
                    continue
            elif page.stem == "index":
                idx[url_root.rstrip("/")] = {
                    "GET": PageRouteHandler(lookup.get_template(str(path.absolute().relative_to(Path(lookup.directories[0]))) + "/" + page.name))
                }
            else:
                idx[url_root + page.stem] = {
                    "GET": PageRouteHandler(lookup.get_template(str(path.absolute().relative_to(Path(lookup.directories[0]))) + "/" + page.name))
                }
        elif page.is_dir():
            index_route(idx, lookup, page, "/" + page.name + "/") # Recursion!

def routing_plugin_pages(pages_path: Path) -> RoutingTable:
    output = {}
    lookup = TemplateLookup(
        directories=[pages_path.absolute()],
        module_directory=pages_path.parent / ".cache" / "pages",
    )
    index_route(output, lookup, pages_path)
    return output
