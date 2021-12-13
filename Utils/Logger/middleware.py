import traceback
from typing import Callable

from fastapi.routing import APIRoute, HTTPException, RequestValidationError
from starlette.requests import Request
from starlette.responses import Response

from Utils.Logger.logging import get_logger

logger = get_logger(__name__)


class LoggingRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            try:
                response = await original_route_handler(request)
                logger.info(f"{request.method} {request.client} | {response.status_code} {response.body.decode()}")
                return response
            except Exception as exc:
                logger.error(f"{request.method} {request.client} | {exc} {traceback.format_exc()}")
                if isinstance(exc, (HTTPException, RequestValidationError)):
                    raise exc
                raise HTTPException(status_code=500, detail="Fatal error")

        return custom_route_handler
