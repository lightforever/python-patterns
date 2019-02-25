import typing
from nltk import WordPunctTokenizer
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegressionCV

from .step import Step


class BasicTokenizer(Step):

    def eval(self, X: typing.List[str]) -> typing.List[str]:
        return X.split(' ')


class NLTKTokenizer(Step):

    def __init__(self):
        self.wp = WordPunctTokenizer()

    def eval(self, X: typing.List[str]) -> typing.List[str]:

        return self.wp.tokenize(X)


class Normalizer(Step):

    def eval(self, X: typing.List[str]) -> typing.List[str]:

        xn = [re.sub('[^a-z0-9 ]', '', doc.lower()) for doc in X]
        return xn


class BOWVectorizer(Step):

    def __init__(self):
        self.bow = CountVectorizer(max_features=5000)

    def prepare(self, X: object, Y: object):
        self.bow.fit(X)

    def eval(self, X: typing.List[str]) -> typing.List[str]:

        return self.bow.transform(X)


class Classifier(Step):

    def __init__(self):

        self._model = LogisticRegressionCV(class_weight='balanced')

    def prepare(self, X: object, Y: object):

        self._model.fit(X, Y)

        return self

    def eval(self, X: typing.List[str]) -> list:

        return self._model.predict(X)


class StepsPipeline(Step):

    def __init__(self, steps: typing.List[Step]):
        self.steps = steps

    def prepare(self, X: object, Y: object = None):
        [step.prepare(X, Y) for step in self.steps]
        return self

    def eval(self, X: object):
        xn = X
        for step in self.steps:
            xn = step.eval(xn)
        return xn
