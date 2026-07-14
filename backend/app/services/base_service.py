"""
Base Service Definition
"""


class BaseService:


    def start(self):
        raise NotImplementedError


    def stop(self):
        raise NotImplementedError
