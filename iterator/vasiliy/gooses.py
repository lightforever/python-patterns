from collections import Iterator, Iterable


class Gooses(Iterator):
    def __init__(self):
        self.gooses = [
            'white goose',
            'gray goose'
        ]
        self._pointer = 0

    def __next__(self):
        if self._pointer < len(self.gooses):
            self._pointer += 1
            return self.gooses[self._pointer - 1]
        else:
            raise StopIteration()


class GrandmasGooses(Iterable):
    def __init__(self):
        self.gooses = [
            'white goose',
            'gray goose'
        ]

    def __iter__(self):
        for i in range(len(self.gooses)):
            yield self.gooses[i]


if __name__ == '__main__':
    for goose in Gooses():
        print(goose)

    print('---')

    for goose in GrandmasGooses():
        print(goose)
