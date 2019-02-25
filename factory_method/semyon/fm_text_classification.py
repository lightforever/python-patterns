from abc import ABC, abstractmethod
import typing
from nltk import WordPunctTokenizer
import re
from sklearn.feature_extraction.text import CountVectorizer

class Step(ABC):

    @abstractmethod
    def prepare(self, X: object):
        pass

    @abstractmethod
    def eval(self, X: object):
        pass


class BasicTokenizer(Step):

    def prepare(self, X: str):
        pass

    def eval(self, X: str) -> typing.List[str]:
        return X.split(' ')


class NLTKTokenizer(Step):

    def __init__(self):
        self.wp = WordPunctTokenizer()

    def prepare(self, X: object):
        pass

    def eval(self, X: str) -> typing.List[str]:

        return self.wp.tokenize(X)


class Normalizer(Step):

    def prepare(self, X: object):
        pass

    def eval(self, X: str) -> str:
        xn = re.sub('[^a-z0-9 ]', '', X.lower())
        return xn


class BOWVectorizer(Step):

    def __init__(self):
        self.bow = CountVectorizer()

    def prepare(self, X: str):
        self.bow.fit(X)

    def eval(self, X:str):

        return self.bow.transform(X)


def step_factory(cls:Step) -> Step:

    return cls()


def pipeline(X:str, steps:typing.List):
    res = X
    for step in steps:
        step_instance = step_factory(step)
        res = step_instance.eval(res)
    return res

if __name__ == '__main__':
    steps = [
        Normalizer,
        BasicTokenizer
    ]

    text = 'The Emperor protects!'

    print(pipeline(text, steps))