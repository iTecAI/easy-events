from sse_starlette.sse import EventSourceResponse
from starlette.requests import Request
from httpagentparser import detect
import json


async def _flush(request: Request):
    await request.send(
        {
            "type": "http.response.body",
            "body": f": {'.' * 2048 ** 2}\n\n".encode(),
            "more_body": True,
        }
    )

__all__ = ["ASGISourceResponse"]


def ASGISourceResponse(generator, request: Request, **kwargs) -> EventSourceResponse:
    async def _publisher(request: Request):
        ua = detect(request.headers["User-Agent"], fill_none=True)
        try:
            yield json.dumps({"event": None})
            print("flushing")
            if (
                ua["browser"]
                and ua["browser"]["name"]
                and ua["browser"]["name"].lower() == "firefox"
            ):
                # await _flush(request)
                pass
            async for event in generator:
                if not request.is_connected:
                    break
                print("sending", event)
                yield json.dumps(event)
        except Exception as e:
            raise e

    return EventSourceResponse(
        _publisher(request),
        headers={"Cache-Control": "public, max-age=29, no-transform"},
        media_type="text/event-stream;charset=utf-8",
        **kwargs
    )
