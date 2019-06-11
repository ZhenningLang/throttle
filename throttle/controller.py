"""
Speed controller

Only master node will manage a controller object
"""
import logging
import random


class AbstractController:

    def registry(self, key: str, params: dict) -> bool:
        raise NotImplementedError()

    def admit(self, key: str) -> bool:
        raise NotImplementedError()


class AverageController(AbstractController):

    def __init__(self):
        self.records = []

    def registry(self, key: str, params: dict) -> bool:
        pass

    def admit(self, key: str) -> bool:
        pass


class MockController(AbstractController):

    def registry(self, key: str, params: dict) -> bool:
        ret = random.random() < 0.5
        logging.info(f'In {self.__class__}.registry, key: {key}, params: {params}, ret: {ret}')
        return ret

    def admit(self, key: str) -> bool:
        ret = random.random() < 0.5
        logging.info(f'In {self.__class__}.admit, key: {key}, ret: {ret}')
        return ret
