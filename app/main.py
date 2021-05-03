from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app import hello
from app import health
from app import generate

app = FastAPI(
    title="BIP Initializer",
    description="API docs for the BIP Initializer backend.\n"
    + "Endpoint /api/v1/schema will render the models json-schema.",
    version="0.2.0",
)

app.include_router(hello.router)
app.include_router(health.router)
app.include_router(generate.router)


Instrumentator().instrument(app).expose(app)
