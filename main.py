from fastapi import FastAPI

from Utils.Logger.middleware import LoggingMiddleware

app = FastAPI()

app.add_middleware(LoggingMiddleware)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
