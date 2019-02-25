from abc import ABC, abstractmethod
from typing import List, Tuple


class AbstractDataSource(ABC):
    @abstractmethod
    def execute(self, query) -> List[Tuple[int, str, str]]:
        pass


class CatDataSource(AbstractDataSource):
    def execute(self, query):
        return [
            (1, 'Cat', 'Tom'),
            (2, 'Kitty', 'Purry'),
        ]
