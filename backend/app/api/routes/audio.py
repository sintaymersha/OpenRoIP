from fastapi import APIRouter, HTTPException

from app.core.application import service_manager


router = APIRouter(
    prefix="/audio",
    tags=["Audio"],
)


def get_audio_service():
    audio_service = service_manager.get_service("audio")

    if audio_service is None:
        raise HTTPException(
            status_code=503,
            detail="Audio service unavailable",
        )

    return audio_service


@router.get("/status")
def audio_status():
    """
    Get current audio status.
    """
    return get_audio_service().get_status()


@router.post("/rx/start")
def start_rx():
    """
    Start audio input.
    """
    get_audio_service().start_rx()

    return {"status": "RX audio started"}


@router.post("/rx/stop")
def stop_rx():
    """
    Stop audio input.
    """
    get_audio_service().stop_rx()

    return {"status": "RX audio stopped"}


@router.post("/tx/start")
def start_tx():
    """
    Start audio output.
    """
    get_audio_service().start_tx()

    return {"status": "TX audio started"}


@router.post("/tx/stop")
def stop_tx():
    """
    Stop audio output.
    """
    get_audio_service().stop_tx()

    return {"status": "TX audio stopped"}