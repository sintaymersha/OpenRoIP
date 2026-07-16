"""
Driver Loader for OpenRoIP.

Responsible for loading and returning the appropriate
radio driver implementation.
"""

from app.radio.virtual_radio import VirtualRadio


class DriverLoader:
    """Loads radio driver implementations."""

    @staticmethod
    def load(driver_name: str = "virtual"):
        """
        Load and return the requested radio driver.
        """

        if driver_name == "virtual":
            return VirtualRadio()

        raise ValueError(f"Unsupported driver: {driver_name}")