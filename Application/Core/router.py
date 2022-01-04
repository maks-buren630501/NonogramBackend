from typing import Callable

from fastapi import HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.routing import APIRoute
from starlette.requests import Request
from starlette.responses import Response

from Application.Core.Logger.logging import get_logger


logger = get_logger(__name__)


class RouteExceptionHandler(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            try:
                response = await original_route_handler(request)
                return response
            except Exception as exc:
                if isinstance(exc, (HTTPException, RequestValidationError)):
                    raise exc
                logger.error(exc_info=True, msg=f"{request.method} {request.client}")
                raise HTTPException(status_code=500, detail="Fatal error")

        return custom_route_handler
