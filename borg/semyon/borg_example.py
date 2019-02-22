from abc import ABC, abstractmethod


class Extractor(ABC):

    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.connection_string = 'old_connection_string'

    def __str__(self):

        return self.connection_string

    @abstractmethod
    def get_data(self, x):
        pass


class Extractor1(Extractor):

    def get_data(self, x):
        return 2.0*x


class Extractor2(Extractor):

    def get_data(self, x):
        return 1.0*x


if __name__ == '__main__':

    ex1 = Extractor1()
    ex2 = Extractor2()

    print('ex1')
    print(ex1.get_data(1.0))
    print(ex1.connection_string)
    print('='*10)

    print('ex2')
    print(ex2.get_data(1.0))
    print(ex2.connection_string)
    print('='*10)


    ex1.connection_string = 'new_connection_string'
    print('ex1: ' + ex1.connection_string)
    print('ex2: ' + ex2.connection_string)