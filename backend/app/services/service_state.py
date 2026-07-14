from enum import Enum


class ServiceState(Enum):

    STOPPED = "stopped"

    STARTING = "starting"

    RUNNING = "running"

    FAILED = "failed"
