from functools import wraps


def printable(upper=False):
    def inner(func, *args, **kwargs):
        @wraps(func)
        def inner2(*args, **kwargs):
            res = func(*args, **kwargs)
            log = f'{func.__name__} result = {res}'
            print(log.upper() if upper else log)

        return inner2

    return inner


@printable(upper=True)
def prod(a: int, b: int):
    return a * b


class Base:
    children = []

    @staticmethod
    def register(include):
        def inner(cls):
            if include:
                Base.children.append(cls)

        return inner

    @classmethod
    def show_children(cls):
        print('Children:')
        for c in cls.children:
            print(f'\t{c.__name__}')


@Base.register(include=True)
class Advanced(Base):
    pass


@Base.register(include=False)
class Advanced2(Base):
    pass


if __name__ == '__main__':
    prod(2, 5)

    Base.show_children()
