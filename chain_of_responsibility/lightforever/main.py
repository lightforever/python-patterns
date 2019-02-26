from abc import ABC, abstractproperty, abstractmethod


class Being(ABC):
    @abstractproperty
    @property
    def type(self):
        pass


class Elf(Being):
    @property
    def type(self):
        return 'Elf'


class Dwarf(Being):
    @property
    def type(self):
        return 'Dwarf'


class Human(Being):
    @property
    def type(self):
        return 'Human'


class Handler(ABC):
    def __init__(self):
        self.successor = None

    def __or__(self, other):
        other.successor = self
        return other

    @abstractmethod
    def is_valid(self, t):
        pass

    def process(self, being: Being):
        if self.is_valid(being.type):
            print(f'{type(self).__name__} processing {being.type}')
        elif self.successor is not None:
            self.successor.process(being)


class ElfHandler(Handler):
    def is_valid(self, t):
        return t == 'Elf'


class DwarfHandler(Handler):
    def is_valid(self, t):
        return t == 'Dwarf'


class DefaultHandler(Handler):
    def is_valid(self, t):
        return True


if __name__ == '__main__':
    beings = [Human(), Dwarf(), Elf()]
    handler = DefaultHandler()| DwarfHandler() | ElfHandler()
    for being in beings:
        handler.process(being)
