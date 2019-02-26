import weakref


class FlyweightMeta(type):
    def __new__(mcls, name, bases, dict_):
        dict_['_registry'] = weakref.WeakValueDictionary()
        return super().__new__(mcls, name, bases, dict_)

    def __call__(cls, *args, **kwargs):
        key = cls.serialize_args(cls, args, kwargs)

        obj = cls._registry.get(key)
        if obj is None:
            obj = super().__call__(*args, **kwargs)
            cls._registry[key] = obj

        return obj


    @staticmethod
    def serialize_args(cls, args, kwargs):
        serialized = []
        serialized.extend(args)
        serialized.extend([str(kwargs), cls.__name__])
        return tuple(serialized)


class File(metaclass=FlyweightMeta):
    def __init__(self, path, opts):
        self.path = path
        self.opts = opts

    def __str__(self):
        return f'<file: {self.path} {self.opts}>'


if __name__ == '__main__':
    file1 = File('path', 'w+')
    file2 = File('path', 'w+')
    file3 = File('path', 'wb+')
    file4 = File('path', 'wb+')

    print(id(file1), id(file2), id(file3), id(file4))
