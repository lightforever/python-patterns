from functools import wraps
from copy import deepcopy


def use_prototype(cls):
    class_builder = cls.__new__

    @wraps(class_builder)
    def new(_cls, *args, **kwargs):
        proto = class_builder(cls)
        saved_dict = deepcopy(proto.__dict__)

        @wraps(class_builder)
        def _new(_cls_, *args, **kwargs):
            proto.__dict__ = saved_dict
            return proto

        cls.__new__ = staticmethod(_new)

        return proto

    cls.__new__ = staticmethod(new)

    return cls


@use_prototype
class BaseConstants:
    @staticmethod
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)

        instance.pi = cls.calc_pi()
        instance.e = cls.calc_e()

        return instance

    @staticmethod
    def calc_pi():
        print('pi calculated')
        return 3.14

    @staticmethod
    def calc_e():
        print('e calculated')
        return 2.718281828


@use_prototype
class CustomConstants(BaseConstants):
    @staticmethod
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)

        instance.custom_constant = cls.calc_custom_constant()

        return instance

    @staticmethod
    def calc_custom_constant():
        print('custom constant calculated')
        return 5.45


if __name__ == '__main__':
    print('main')

    cc = CustomConstants()
    print(cc.pi)
    print(cc.e)
    print(cc.custom_constant)
    print('---')

    base_c = BaseConstants()
    print(base_c.pi)
    print(base_c.e)
    print('---')

    cc.e = 'new value'
    print(cc.e)

    cc2 = CustomConstants()
    print(cc.pi)
    print(cc.e, '# value of prototype has not changed')
    print(cc.custom_constant)
