from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def accelerate(self, rpm=400):
        pass


class Vehicle(ABC):
    def __init__(self, engine: Engine):
        self.engine = engine

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def accelerate(self, rpm):
        self.engine.accelerate(rpm)


class Ford(Vehicle):
    def __init__(self, engine: Engine, family):
        super().__init__(engine)
        self.family = family

    def start(self):
        print(f'ford {self.family} started')

    def stop(self):
        print(f'ford {self.family} stopped')


class V12(Engine):
    def accelerate(self, rpm=4000):
        print(f'V12 accelerated to {rpm} rpm')


class V8(Engine):
    def accelerate(self, rpm=4000):
        print(f'V8 accelerated to {rpm} rpm')


if __name__ == '__main__':
    ford_mustang = Ford(V12(), 'mustang')
    ford_mustang.start()
    ford_mustang.accelerate(5400)
    ford_mustang.stop()

    print('-'*7)

    ford_fiesta = Ford(V8(), 'fiesta')
    ford_fiesta.start()
    ford_fiesta.accelerate(3200)
    ford_fiesta.stop()
