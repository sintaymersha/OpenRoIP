"""
Custom exceptions for OpenRoIP.
"""


class OpenRoIPError(Exception):
    """Base exception for all OpenRoIP errors."""
    pass


class BridgeError(OpenRoIPError):
    """Generic bridge-related error."""
    pass


class RadioNotConnectedError(BridgeError):
    """Raised when a radio operation is attempted while disconnected."""
    pass


class DriverLoadError(BridgeError):
    """Raised when a radio driver cannot be loaded."""
    pass


class InvalidRadioStateError(BridgeError):
    """Raised when an invalid radio state transition is attempted."""
    pass