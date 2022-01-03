from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware

from Utils.Core.router import RouteExceptionHandler
from Utils.Core.settings import APP
from Utils.Logger.middleware import request_logging

app = FastAPI(
    debug=APP.DEBUG,
    title=f"{APP.APP_NAME} {APP.APP_VERSION}",
    middleware=[Middleware(BaseHTTPMiddleware, dispatch=request_logging)]
)

app.router.route_class = RouteExceptionHandler


@app.get("/")
async def root():
    return {"message": "Hello World"}


