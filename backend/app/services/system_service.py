from .base_service import BaseService


class SystemService(BaseService):


    def start(self):

        print("System service started")


    def stop(self):

        print("System service stopped")
