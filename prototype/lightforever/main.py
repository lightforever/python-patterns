from abc import ABC, abstractmethod


class Prototype(ABC):
    _objects = dict()

    def clone(self):
        obj = self.__class__()
        obj.__dict__ = self.__dict__.copy()
        return obj

    @abstractmethod
    def key(self) -> str:
        pass

    @classmethod
    def register(cls, obj) -> None:
        cls._objects[obj.key()] = obj

    @classmethod
    def create(cls, key:str=None, **kwargs):
        if key is not None and key in cls._objects:
            obj = cls._objects[key].clone()
        else:
            obj = cls()

        obj.__dict__.update(kwargs)
        return obj

    def __repr__(self):
        return ' '.join([f'{k}={v}' for k, v in self.__dict__.items() if not k.startswith('__')])

class Car(Prototype):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def key(self):
        if 'type' in self.__dict__:
            return self.__dict__['type']
        return str(id)

if __name__ == '__main__':
   car = Car(type='BMW', speed=10, color='green')
   print(car)
   Car.register(car)

   car2 = Car.create('BMW', speed=20)
   car3 = Car.create(type='Toyoto', speed=20)
   print(car)
   print(car2)
   print(car3)