from .settings import (
    PROJECT_NAME,
    VERSION,
    ENVIRONMENT
)


def initialize():

    print("==============================")
    print(f"{PROJECT_NAME}")
    print(f"Version: {VERSION}")
    print(f"Environment: {ENVIRONMENT}")
    print("==============================")

    print("Core services initialized")
