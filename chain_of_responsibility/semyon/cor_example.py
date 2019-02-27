from abc import ABC, abstractmethod
import random


class Aircraft:

    def __init__(self):

        self.engines_status = random.uniform(0, 1) > 0.2
        self.chassis_status = random.uniform(0, 1) > 0.2
        self.fuel_status = random.uniform(0, 1) > 0.2
        self.wings_status = random.uniform(0, 1) > 0.2


class Checker(ABC):

    @abstractmethod
    def set_next(self, next_checker):
        pass

    @abstractmethod
    def check(self, value: Aircraft):
        pass


class GenericChecker(Checker):

    _next = None

    def set_next(self, next_checker: Checker):
        self._next = next_checker

    @abstractmethod
    def check(self, value: Aircraft):
        if self._next is not None:
            return self._next.check(value)
        else:
            return None


class EngineChecker(GenericChecker):

    def check(self, value: Aircraft):

        if not value.engines_status:
            return 'engine fail'
        else:
            super().check(value)


class ChassisChecker(GenericChecker):

    def check(self, value: Aircraft):

        if not value.chassis_status:
            return 'chassis fail'
        else:
            super().check(value)


class FuelChecker(GenericChecker):

    def check(self, value: Aircraft):

        if not value.chassis_status:
            return 'fuel fail'
        else:
            super().check(value)


class WingsChecker(GenericChecker):

    def check(self, value: Aircraft):

        if not value.chassis_status:
            return 'wings fail'
        else:
            super().check(value)


if __name__ == '__main__':

    check_order = [EngineChecker(), ChassisChecker(), WingsChecker(), FuelChecker()]
    aircraft = Aircraft()

    for i, checker in enumerate(check_order[:-1]):
        checker.set_next(check_order[i+1])

    for checker in check_order:
        res = checker.check(aircraft)
        if res is not None:
            print(res)
            break
