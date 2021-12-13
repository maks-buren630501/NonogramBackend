from fastapi import FastAPI, HTTPException

from Utils.Logger.middleware import LoggingMiddleware

app = FastAPI()

app.add_middleware(LoggingMiddleware)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/{dividend}/{divisor}")
async def division(dividend: int, divisor: int):
    try:
        return {"result": f"{round(dividend / divisor, 2)}"}
    except ZeroDivisionError:
        raise HTTPException(detail="ZeroDivisionError", status_code=500)
