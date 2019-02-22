from abc import ABC, abstractmethod
from uuid import uuid4
import random


class BaseEngine(ABC):
    def __init__(self, serial_number):
        self.serial_number = serial_number

    @property
    @abstractmethod
    def fuel_type(self):
        pass

    @abstractmethod
    def start(self):
        print('Engine started')

    @abstractmethod
    def stop(self):
        print('Engine stopped')

    @abstractmethod
    def accelerate(self, rpm=2000):
        print(f'rpm = {rpm}')


class ElectricEngine(BaseEngine):
    def __init__(self, serial_number, max_rpm):
        super().__init__(serial_number)
        self.max_rpm = max_rpm

    @property
    def fuel_type(self):
        return 'electricity'

    def start(self):
        return super().start()

    def stop(self):
        return super().stop()

    def accelerate(self, rpm=500):
        if rpm > self.max_rpm:
            raise ValueError('Too high rpm. Engine could be damaged.')
        return super().accelerate(rpm)


class GASEngine(BaseEngine):
    def __init__(self, serial_number):
        super().__init__(serial_number)

    @property
    def fuel_type(self):
        return 'gas'

    def start(self):
        return super().start()

    def stop(self):
        return super().stop()

    def accelerate(self, rpm=4500):
        return super().accelerate(rpm)


class AbstractEngineFactory:
    def __call__(self, engine_type='electric'):
        if engine_type == 'electric':
            return ElectricEngineFactory(ElectricEngine)
        else:
            return GASEngineFactory(GASEngine)


class ElectricEngineFactory:
    def __init__(self, engine_class):
        self.__engine_class = engine_class

    def __call__(self, serial_number=None):
        return self.__engine_class(serial_number or uuid4(), max_rpm=2500)


class GASEngineFactory:
    def __init__(self, engine_class):
        self.__engine_class = engine_class

    def __call__(self, serial_number=None):
        return self.__engine_class(serial_number or uuid4())


if __name__ == '__main__':
    abstract_engine_factory = AbstractEngineFactory()

    engines = []
    engine_types = ['electric', 'gas']

    for i in range(10):
        engine_factory = abstract_engine_factory(random.choice(engine_types))
        engines.append(engine_factory())

    for engine in engines:
        print(f'{engine.fuel_type} engine {engine.serial_number}')
        engine.start()
        try:
            engine.accelerate(8000)
        except ValueError as e:
            print(e)
        engine.stop()
        print('----------------')
