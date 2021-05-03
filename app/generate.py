from fastapi import APIRouter
from pydantic import BaseModel, constr, conint
from typing import Optional
from jinja2 import Environment, FileSystemLoader
import json

router = APIRouter()

# Defining qualified/legal character format that can be used
qnameCharFmt = "^[A-Za-z]([-A-Za-z0-9]*[A-Za-z0-9])?$"
qnameExtCharFmt = "[-A-Za-z0-9_.*/]"
qurlFmt = "(https?:\/\/)?(www\.)?[a-zA-Z0-9]+([-a-zA-Z0-9.]{1,254}[A-Za-z0-9])?\.[a-zA-Z0-9()]{1,6}([\/][-a-zA-Z0-9_]+)*[\/]?"
qImageTagFmt = "[a-zA-Z0-9][-a-zA-Z0-9._*]*"
qFluxImageTagFmt = "^(glob|regex|semver):" + qImageTagFmt
qApptype = "^(frontend|backend)$"

# Define the API schema. Any values that we define a default
# value for becomes optional in the request call.
class HRValues(BaseModel):
    name: constr(regex=qnameCharFmt, min_length=1, max_length=63)
    namespace: constr(regex=qnameCharFmt, min_length=1, max_length=63)
    flux_image_tag_pattern: constr(
        regex=qFluxImageTagFmt, min_length=1, max_length=128
    ) = "glob:main-*"
    cluster: constr(regex=qnameCharFmt, min_length=1, max_length=63)
    billingproject: constr(regex=qnameCharFmt, min_length=1, max_length=63)
    image_repository: constr(regex=qurlFmt)
    image_tag: constr(regex=qImageTagFmt, min_length=1, max_length=128)
    apptype: constr(regex=qApptype) = "backend"
    exposed: bool = False
    authentication: bool = True
    port: conint(ge=1024, le=65535) = 8080
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


@router.get("/api/v1/schema")
async def schema():
    return json.dumps(HRValues.schema(), indent=2)
