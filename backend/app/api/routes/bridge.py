from fastapi import APIRouter, HTTPException

from app.core.application import service_manager


router = APIRouter(
    prefix="/bridge",
    tags=["Bridge"],
)


def get_bridge_service():

    bridge_service = service_manager.get_service("bridge")

    if bridge_service is None:
        raise HTTPException(
            status_code=503,
            detail="Bridge service unavailable",
        )

    return bridge_service


@router.get("/status")
def bridge_status():
    """
    Get bridge status.
    """

    return get_bridge_service().get_status()


@router.post("/connect")
def connect_bridge():
    """
    Connect bridge.
    """

    get_bridge_service().connect()

    return {
        "status": "Bridge connected"
    }


@router.post("/disconnect")
def disconnect_bridge():
    """
    Disconnect bridge.
    """

    get_bridge_service().disconnect()

    return {
        "status": "Bridge disconnected"
    }


@router.post("/start")
def start_bridge():
    """
    Start bridge operation.
    """

    get_bridge_service().start_bridge()

    return {
        "status": "Bridge started"
    }


@router.post("/stop")
def stop_bridge():
    """
    Stop bridge operation.
    """

    get_bridge_service().stop_bridge()

    return {
        "status": "Bridge stopped"
    }


@router.post("/ptt/on")
def ptt_on():

    get_bridge_service().ptt_on()

    return {
        "status": "PTT ON"
    }


@router.post("/ptt/off")
def ptt_off():

    get_bridge_service().ptt_off()

    return {
        "status": "PTT OFF"
    }