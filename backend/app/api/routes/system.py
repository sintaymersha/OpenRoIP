from fastapi import APIRouter

from app.core.application import service_manager

router = APIRouter(
    prefix="/system",
    tags=["System"],
)


@router.get("/status")
def status():
    return service_manager.get_status()