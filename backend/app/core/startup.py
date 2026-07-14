from .settings import (
    PROJECT_NAME,
    VERSION,
    ENVIRONMENT
)

from app.services.service_manager import ServiceManager
from app.services.system_service import SystemService



def initialize():

    print("==============================")
    print(PROJECT_NAME)
    print(f"Version: {VERSION}")
    print(f"Environment: {ENVIRONMENT}")
    print("==============================")


    manager = ServiceManager()

    manager.register(SystemService())


    manager.start_all()


    print("Core services initialized")