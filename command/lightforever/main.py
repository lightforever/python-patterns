from functools import partial
from typing import Callable


def log(message: str) -> None:
    print(message)


def process(func: Callable[[], bool], failture_log: Callable[[str], None], success_log: Callable[[str], None]):
    if func():
        success_log()
    else:
        failture_log()


if __name__ == '__main__':
    func = lambda: False
    func2 = lambda: True

    success = partial(log, message='Success')
    fail = partial(log, message='Fail')

    print(f'func processing')
    process(func, fail, success)
    print(f'func2 processing')
    process(func2, fail, success)
