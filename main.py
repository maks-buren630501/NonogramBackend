from fastapi import FastAPI
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware

from Application.Core.router import RouteExceptionHandler
from Application.Core.settings import APP
from Application.Core.Logger.middleware import request_logging
from Application.Authentication.urls import authentication_router
from Application.User.urls import user_router

app = FastAPI(
    debug=APP.DEBUG,
    title=f"{APP.APP_NAME} {APP.APP_VERSION}",
    middleware=[Middleware(BaseHTTPMiddleware, dispatch=request_logging)],
    routes=[*authentication_router.routes, *user_router.routes]
)

app.router.route_class = RouteExceptionHandler


@app.get("/")
async def root():
    return {"message": "Hello World"}
