from abc import ABC, abstractmethod
from numbers import Number
from typing import Iterable


class BaseEstimator(ABC):
    @abstractmethod
    def fit(self, x, y) -> 'BaseEstimator':
        pass

    @abstractmethod
    def predict(self, x) -> Iterable[Number]:
        pass


class CustomEstimator:
    def __init__(self):
        self.field = 'field_value'

    def learn(self, x, y):
        print('Estimator was learnt')
        return self

    def get_prediction(self, x) -> Iterable[Number]:
        print('Prediction was made')
        return [0, 0, 0, 0]

    def print_hello(self):
        print('hello')


def grid_search_cv(estimator: BaseEstimator, initial_guess: Iterable[Number]) -> Iterable[Number]:
    print(f'Hyperparameters were found: {initial_guess}')
    return estimator


class Adapter:
    def __init__(self, adaptee, **mapping):
        self.__adaptee = adaptee
        self.__mapping = mapping

    def __getattr__(self, item):
        if item in self.__mapping:
            return self.__mapping[item]
        return getattr(self.__adaptee, item)


if __name__ == '__main__':
    estimator = CustomEstimator()
    adapted = Adapter(estimator, fit=estimator.learn, predict=estimator.get_prediction)
    grid_search_cv(adapted, [0, 0, 0])
    print(adapted.fit(1, 2))
    print(adapted.predict(2))
    adapted.print_hello()
