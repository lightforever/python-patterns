from abc import abstractmethod, ABC


class Animal(ABC):
    @abstractmethod
    def speak(self)->None:
        pass

    @classmethod
    def factory(cls, animal_type):
        if animal_type == 'cat':
            return Cat()
        return Dog()


class Cat(Animal):
    def speak(self)->None:
        print('Meow')


class Dog(Animal):
    def speak(self)->None:
        print('Bark')


def factory_method(animal_type: str):
    if animal_type == 'cat':
        return Cat()
    return Dog()


class Shelter(ABC):
    @abstractmethod
    def get_one(self)->Animal:
        pass

class CatShelter(ABC):
    def get_one(self)->Animal:
        return Cat()

class DogShelter(ABC):
    def get_one(self)->Animal:
        return Dog()


if __name__ == '__main__':
    cat = factory_method('cat')
    cat.speak()

    dog = factory_method('dog')
    dog.speak()

    cat = Animal.factory('cat')
    cat.speak()

    dog = DogShelter().get_one()
    dog.speak()