from fastapi import APIRouter, Request
from pydantic import BaseModel
from typing import Optional
from jinja2 import Environment, FileSystemLoader
import json

router = APIRouter()


class HRValues(BaseModel):
    name: str
    namespace: str
    cluster: str
    billingproject: str
    image_repository: str
    image_tag: str
    # Required in ssb-chart but default values defined
    apptype = "backend"
    exposed = False
    port: Optional[int] = 80


@router.post("/api/1/generate")
async def generate_handler(hrvalues: HRValues):
    env = Environment(
        loader=FileSystemLoader('templates')
    )
    template = env.get_template('helmrelease.j2')
    generated_hr = template.render(hrvalues)
    return json.loads(generated_hr)
