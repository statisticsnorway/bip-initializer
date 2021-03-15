from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app import hello
from app import health
from app import generate

app = FastAPI()

app.include_router(hello.router)
app.include_router(health.router)
app.include_router(generate.router)


Instrumentator().instrument(app).expose(app)
