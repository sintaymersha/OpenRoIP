from .settings import (
    PROJECT_NAME,
    VERSION,
    ENVIRONMENT,
)

from app.core.application import service_manager

from app.services.system_service import SystemService
from app.services.radio_service import RadioService
from app.services.audio_service import AudioService
from app.services.radio_discovery import RadioDiscoveryService
from app.services.bridge_service import BridgeService


def initialize():

    print("==============================")
    print(PROJECT_NAME)
    print(f"Version: {VERSION}")
    print(f"Environment: {ENVIRONMENT}")
    print("==============================")

    service_manager.register("system", SystemService())
    service_manager.register("radio", RadioService())
    service_manager.register("audio", AudioService())
    service_manager.register("radio_discovery", RadioDiscoveryService())
    service_manager.register("bridge", BridgeService())

    service_manager.start_all()

    print("Core services initialized")