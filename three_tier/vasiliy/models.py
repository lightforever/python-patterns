from three_tier.vasiliy.datastorage import CatDataSource
from typing import List


class Cat:
    def __init__(self, pk, first_name, last_name):
        self.pk = pk
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def all(cls) -> List['Cat']:
        return [Cat(*result) for result in CatDataSource().execute('get all cats')]

    def meow(self):
        print(f'{self.first_name} {self.last_name} said "meow"')
