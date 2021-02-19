from fastapi import APIRouter

router = APIRouter()


@router.get("/health/alive")
async def alive():
    return {"status": "I'm not dead!"}


@router.get("/health/ready")
async def ready():
    return {"status": "Ready"}
