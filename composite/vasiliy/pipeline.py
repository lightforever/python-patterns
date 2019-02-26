from abc import ABC, abstractmethod
from numbers import Number
from collections import OrderedDict


class Estimator(ABC):
    @abstractmethod
    def fit(self, x, y) -> 'Estimator':
        pass

    @abstractmethod
    def predict(self, x) -> Number:
        pass


class PCA(Estimator):
    def fit(self, x, y):
        print('PCA fit')
        return self

    def predict(self, x):
        print('PCA predict')
        return 0


class RidgeRegression(Estimator):
    def fit(self, x, y) -> 'Estimator':
        print('ridge regression fit')
        return self

    def predict(self, x) -> Number:
        print('ridge regression predict')
        return 0


class Pipeline(Estimator):
    def __init__(self, estimators: OrderedDict):
        self.pipeline = estimators

    def fit(self, x, y):
        for stage, estimator in self.pipeline.items():
            print(f'fitting {stage}...')
            estimator.fit(x, y)
            x = estimator.predict(x)
        return self

    def predict(self, x):
        for stage, estimator in self.pipeline.items():
            print(f'predicting {stage} ...')
            x = estimator.predict(x)
        return x


if __name__ == '__main__':
    pipeline = Pipeline(OrderedDict([
        ('dim. reduction', PCA()),
        ('ridge regression', RidgeRegression()),
    ]))

    pipeline.fit(0, 0)
    pipeline.predict(0)
