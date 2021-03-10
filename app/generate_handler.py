from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional

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
    serviceaccount_create: Optional[bool] = True


@router.post("/api/1/generate")
async def generate_handler(hrvalues: HRValues):
    # Kall metode generate og send med variabler i HRValues
    # Returner det metoden sender tilbake
    return hrvalues
