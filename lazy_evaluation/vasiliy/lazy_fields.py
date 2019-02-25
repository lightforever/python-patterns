import math


class SquaredRootOfFive:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        raise AttributeError()

    def __get__(self, instance, owner):
        if not hasattr(self, 'sqrt_5'):
            print(f'---lazy calculations of {self.name}---')
            self.sqrt_5 = math.sqrt(5)

        return self.sqrt_5


class Constants:
    square_root_of_five = SquaredRootOfFive()
    pi = math.pi


if __name__ == '__main__':
    constants = Constants()

    print(constants.square_root_of_five)
    print('cashed value', constants.square_root_of_five)

    constants.square_root_of_five = 10


