from fastapi import FastAPI

from app import hello
from app import health

app = FastAPI()

app.include_router(hello.router)
app.include_router(health.router)
