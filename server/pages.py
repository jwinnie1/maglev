from .middleware import HTTPResponse
from mako.lookup import TemplateLookup
from mako import exceptions
from .routing import RouteHandler, RoutingTable
from pathlib import Path
from termcolor import colored


class PageRouteHandler(RouteHandler):
    def handle_request(self, request):
        try:
            return HTTPResponse(
                "text/html",
                self.data.render(request=request),
                200
            )
        except:
            if self.prod:
                raise
            else:
                return HTTPResponse(
                    "text/html",
                    exceptions.html_error_template().render(),
                    500
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

def index_route(idx: RoutingTable,
                lookup: TemplateLookup,
                path: Path,
                prod: bool,
                url_root: str = ""):
    for page in path.iterdir():
        if page.suffix == ".mako":
            if page.stem.startswith("_"):
                continue
            if page.stem in ["404", "500"]:
                if url_root == "":
                    idx[page.stem] = {
                        "ERROR": ErrorRouteHandler(lookup.get_template(page.name), int(page.stem))
                    }
                else:
                    print(colored("warn", "red") + ": Error pages cannot be in a subdirectory")
                    continue
            elif page.stem == "index":
                idx[url_root.rstrip("/")] = {
                    "GET": PageRouteHandler(
                            lookup.get_template(
                                str(
                                    path.absolute().relative_to(
                                        Path(lookup.directories[0])
                                    )
                                ) + "/" + page.name),
                            prod
                        )
                }
            else:
                idx[("/" if url_root == "" else url_root) + page.stem] = {
                    "GET": PageRouteHandler(
                            lookup.get_template(
                                str(
                                    path.absolute().relative_to(
                                        Path(lookup.directories[0])
                                    )
                                ) + "/" + page.name),
                            prod
                        )
                }
        elif page.is_dir():
            index_route(idx, lookup, page, prod, "/" + page.name + "/") # Recursion!

def routing_plugin_pages(pages_path: Path, prod: bool) -> RoutingTable:
    output = {}
    lookup = TemplateLookup(
        directories=[pages_path.absolute()],
        module_directory=pages_path.parent / ".cache" / "pages",
    )
    index_route(output, lookup, pages_path, prod)
    return output
