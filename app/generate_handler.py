from fastapi import APIRouter, Request
from pydantic import BaseModel
from typing import Optional
from fastapi.templating import Jinja2Templates

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
async def generate_handler(request: Request, hrvalues: HRValues):
    templates = Jinja2Templates(directory="templates")
    generated_hr = templates.TemplateResponse(
        "helmrelease.j2", {"request": request, "values": hrvalues}
    )
    return generated_hr
    # Sjekk for gyldig verdier??
    # Kall metode generate og send med variabler i HRValues
    # Returner det metoden sender tilbake
