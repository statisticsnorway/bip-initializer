from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from jinja2 import Environment, FileSystemLoader
import json

router = APIRouter()


# Define the API schema
class HRValues(BaseModel):
    name: str
    namespace: str
    flux_image_tag_pattern: Optional[str] = "glob:main-*"
    cluster: str
    billingproject: str
    image_repository: str
    image_tag: str
    # Required in ssb-chart but default values defined
    apptype: str = "backend"
    exposed: bool = False
    authentication: bool = True
    port: Optional[int] = 80

    class Config:
        schema_extra = {
            "example": {
                "name": "myapp",
                "namespace": "stratus",
                "flux_image_tag_pattern": "glob:main-*",
                "cluster": "staging-bip-app",
                "billingproject": "ssb-stratus",
                "image_repository": "eu.gcr.io/prod-bip/ssb/stratus/myapp",
                "image_tag": "master-imagescan-f5130c78fbcc54fc038d7e0e28cde35da8e791f6",
                "port": 8080,
                "apptype": "backend",
                "exposed": False,
                "authentication": True,
            }
        }


@router.post("/api/v1/generate")
async def generate(hrvalues: HRValues):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("helmrelease.j2")
    generated_hr = template.render(hrvalues)
    return json.loads(generated_hr)
