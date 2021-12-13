from fastapi import FastAPI

from Utils.Logger.middleware import LoggingRoute

app = FastAPI()

app.router.route_class = LoggingRoute


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/{dividend}/{divisor}")
async def division(dividend: int, divisor: int):
    return {"result": f"{round(dividend / divisor, 2)}"}

