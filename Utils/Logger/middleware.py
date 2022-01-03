from starlette.requests import Request
from .logging import get_logger

logger = get_logger(__name__)


async def request_logging(request: Request, call_next):
    response = await call_next(request)
    logger.info(f"{request.method} {request.url} {request.client} {response.status_code}")
    return response
