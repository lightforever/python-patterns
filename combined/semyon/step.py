from abc import ABC, abstractmethod


class Step(ABC):

    @abstractmethod
    def prepare(self, X: object, Y: object):
        pass

    @abstractmethod
    def eval(self, X: object):
        pass
