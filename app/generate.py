from fastapi import APIRouter
from pydantic import BaseModel, constr, conint
from typing import Optional
from jinja2 import Environment, FileSystemLoader
import json

router = APIRouter()

# Defining qualified/legal character format that can be used
# Inspired by this: https://github.com/kubernetes/kubernetes/blob/master/staging/src/k8s.io/apimachinery/pkg/util/validation/validation.go and this
# https://docs.docker.com/engine/reference/commandline/tag/
# All regex expressions below are tested using https://regexr.com
qnameCharFmt = "^[A-Za-z]([-A-Za-z0-9]*[A-Za-z0-9])?$"
qnameExtCharFmt = "[-A-Za-z0-9_.*/]"
qurlFmt = "(https?:\/\/)?(www\.)?[a-zA-Z0-9]+([-a-zA-Z0-9.]{1,254}[A-Za-z0-9])?\.[a-zA-Z0-9()]{1,6}([\/][-a-zA-Z0-9_]+)*[\/]?"
qImageTagFmt = "[a-zA-Z0-9][-a-zA-Z0-9._*]*"
qFluxImageTagFmt = "^(glob|regex|semver):" + qImageTagFmt
qApptype = "^(frontend|backend)$"


class HRValues(BaseModel):
    """Define the API schema. Any values that we define a default
    value for becomes optional in the request call.
    """

    name: constr(min_length=1, max_length=63, regex=qnameCharFmt)
    namespace: constr(min_length=1, max_length=63, regex=qnameCharFmt)
    flux_image_tag_pattern: constr(
        min_length=1, max_length=128, regex=qFluxImageTagFmt
    ) = "glob:main-*"
    cluster: constr(min_length=1, max_length=63, regex=qnameCharFmt)
    billingproject: constr(min_length=1, max_length=63, regex=qnameCharFmt)
    image_repository: constr(regex=qurlFmt)
    image_tag: constr(min_length=1, max_length=128, regex=qImageTagFmt)
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
    """ Generate valid HelmRelease from input """
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("helmrelease.j2")
    generated_hr = template.render(hrvalues)
    return json.loads(generated_hr)


@router.get("/api/v1/schema")
async def schema():
    """ Expose schema definition for the model """
    return json.dumps(HRValues.schema(), indent=2)
