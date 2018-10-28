
from aiohttp import web
import threading
import asyncio
import uvloop
from .middleware import HTTPResponse


def start_server(middleware, port):
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

    async def handle(request):
        response_content = HTTPResponse()
        for plugin in middleware:
            if plugin.threaded:
                threading.Thread(target=plugin.handle, args=(request, response_content)).start()
            else:
                plugin_output = plugin.handle(request, response_content)
                if plugin_output:
                    response_content = plugin_output
        return web.Response(
            body=response_content.body,
            content_type=response_content.content_type,
            status=response_content.status_code)

    app = web.Application()
    app.add_routes([web.route("*", "/{tail:.*}", handle)])

    web.run_app(app, port=port)
