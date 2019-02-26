class Storage:
    def __init__(self):
        self.__things = {
            'apple': 20,
            'cucumber': 30,
            'baneblade': 1,
        }

    def get_thing(self, name: str):
        if name in self.__things and self.__things[name] > 0:
            self.__things[name] -= 1
            return name.upper()

    def add_to_storage(self, name, amount=1):
        if name not in self.__things:
            self.__things[name] = 0
        self.__things[name] += amount


class Storekeeper:
    def __init__(self, storage: Storage):
        self.__storage = storage

    def get_thing(self, thing_name):
        if thing_name != 'baneblade':
            return self.__storage.get_thing(thing_name)
        else:
            return 'only chosen one can use baneblade'

    def add_to_storage(self, name, amount=1):
        if name == 'baneblade':
            print('Inquisition are notified')
        return self.__storage.add_to_storage(name, amount)


if __name__ == '__main__':
    supplyer = Storekeeper(Storage())

    print(supplyer.get_thing('baneblade'))
    print(supplyer.add_to_storage('baneblade'))
    print(supplyer.get_thing('apple'))
    print(supplyer.get_thing('banana'))
