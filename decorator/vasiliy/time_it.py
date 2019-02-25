from time import sleep
from datetime import datetime
from functools import wraps


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()

        result = func(*args, **kwargs)

        stop = datetime.now()

        print(f'execution of {func.__name__} took {stop - start}.')

        return result
    return wrapper


@time_it
def do_something_slow():
    sleep(3)


if __name__ == '__main__':
    do_something_slow()


