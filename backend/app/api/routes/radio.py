from fastapi import APIRouter, HTTPException

from app.core.application import service_manager

router = APIRouter(
    prefix="/radio",
    tags=["Radio"],
)


def get_radio_service():
    """
    Retrieve the RadioService instance from the Service Manager.
    """
    radio_service = service_manager.get_service("radio")

    if radio_service is None:
        raise HTTPException(
            status_code=503,
            detail="Radio service not available",
        )

    return radio_service


@router.get("/status")
def status():
    return get_radio_service().get_status()


@router.post("/connect")
def connect():
    get_radio_service().connect("Virtual Radio")
    return {"message": "Radio connected"}


@router.post("/disconnect")
def disconnect():
    get_radio_service().disconnect()
    return {"message": "Radio disconnected"}


@router.post("/ptt/on")
def ptt_on():
    get_radio_service().ptt_on()
    return {"message": "PTT enabled"}


@router.post("/ptt/off")
def ptt_off():
    get_radio_service().ptt_off()
    return {"message": "PTT disabled"}


@router.post("/tx/on")
def tx_on():
    get_radio_service().set_transmitting(True)
    return {"message": "Transmission started"}


@router.post("/tx/off")
def tx_off():
    get_radio_service().set_transmitting(False)
    return {"message": "Transmission stopped"}


@router.post("/rx/on")
def rx_on():
    get_radio_service().set_receiving(True)
    return {"message": "Reception started"}


@router.post("/rx/off")
def rx_off():
    get_radio_service().set_receiving(False)
    return {"message": "Reception stopped"}