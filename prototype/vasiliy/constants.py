class Prototype:
    def clone(self, **kwargs):
        new_instance = self.__class__()
        new_instance.__dict__.update(**kwargs)
        return new_instance


class Constants(Prototype):
    def __init__(self):
        self.e = 2.718281828


if __name__ == '__main__':
    original = Constants()
    constants_created_using_prototype = original.clone(pi=3.14)

    print(id(original), id(constants_created_using_prototype))
    print(constants_created_using_prototype.e)
    print(constants_created_using_prototype.pi)
