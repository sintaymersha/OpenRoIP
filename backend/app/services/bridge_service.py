"""
Bridge Service
"""

from .base_service import BaseService
from app.bridge.bridge_manager import BridgeManager


class BridgeService(BaseService):

    def __init__(self):
        self.bridge = BridgeManager()

    def start(self):
        print("Starting Bridge Service...")
        self.bridge.initialize()

    def stop(self):
        print("Stopping Bridge Service...")
        self.bridge.shutdown()
