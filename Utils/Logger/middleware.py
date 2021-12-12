from fastapi import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

from Utils.Logger.logging import get_logger


class LoggingMiddleware(BaseHTTPMiddleware):
    """Logging middleware."""

    def __init__(self, app):
        super().__init__(app)
        self.logger = get_logger(__name__)

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        try:
            response = await call_next(request)
            self.logger.info(f"{request.method} {request.client} | {response.status_code}")
            return response
        except Exception as error:
            self.logger.info(error, exc_info=True)
            raise HTTPException(status_code=500, detail='Fatal error')

