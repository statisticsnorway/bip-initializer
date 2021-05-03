from fastapi import APIRouter
from pydantic import BaseModel
from jinja2 import Environment, FileSystemLoader
import json

router = APIRouter()


# Define the API schema. Any values that we define a default
# value for becomes optional in the request call.
class HRValues(BaseModel):
    name: str
    namespace: str
    flux_image_tag_pattern: str = "glob:main-*"
    cluster: str
    billingproject: str
    image_repository: str
    image_tag: str
    apptype: str = "backend"
    exposed: bool = False
    authentication: bool = True
    port: int = 8080
    health_probes: bool = True
    metrics: bool = True

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
                "health_probes": True,
                "metrics": True,
            }
        }


@router.post("/api/v1/generate")
async def generate(hrvalues: HRValues):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("helmrelease.j2")
    generated_hr = template.render(hrvalues)
    return json.loads(generated_hr)
