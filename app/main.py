from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app import hello
from app import health

app = FastAPI()

app.include_router(hello.router)
app.include_router(health.router)


Instrumentator().instrument(app).expose(app)
