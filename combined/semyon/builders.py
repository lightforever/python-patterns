from abc import ABC, abstractmethod
from .steps import *
import pandas as pd


class Builder(ABC):

    @abstractmethod
    def make_preprocessing(self, steps: list) -> object:
        pass

    @abstractmethod
    def make_model(self) -> object:
        pass

    @abstractmethod
    def load_data(self, csv_path: str, col_x: str, col_y: str) -> object:
        pass


class TextClassifier(object):

    def __init__(self):
        self._preprocessing = None
        self.data = dict()
        self._model = None

    @property
    def preprocessing(self):
        return self._preprocessing

    @preprocessing.setter
    def preprocessing(self, model: StepsPipeline):
        self._preprocessing = model

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model: Step):
        self._model = model

    def prepare(self):
        self.preprocessing = self.preprocessing.prepare(self.data['X'])
        self.data['Xn'] = self.preprocessing.eval(self.data['X'])
        self.model.prepare(self.data['Xn'], self.data['Y'])

    def eval(self, X: typing.List[str]) -> list:
        xn = self.preprocessing.eval(X)
        return self.model.eval(xn)


class StepFactory:

    @abstractmethod
    def create_step(self, *args):
        pass


class PreprocessingStepFactory(StepFactory):

    def __init__(self):

        self.preprocessors = {
            'BOWVectorizer': BOWVectorizer,
            'NLTKtokenizer': NLTKTokenizer,
            'BasicTokenizer': BasicTokenizer,
            'Normalizer': Normalizer
        }

    def create_step(self, type: str):

        if type in self.preprocessors:
            return self.preprocessors[type]()
        else:
            raise ValueError('invalid preprocessor type')


class ClassifierFactory(StepFactory):

    def __init__(self):

        self.classifiers = {
            'logistic regression': Classifier
        }

    def create_step(self, type: str):

        if type in self.classifiers:
            return self.classifiers[type]()
        else:
            raise ValueError('invalid classifier type')


class TextClassifierBuilder(Builder):

    def __init__(self) -> None:

        self.classifier = None
        self.reset_model()
        self.preprocessingFactory = PreprocessingStepFactory()
        self.classifierFactory = ClassifierFactory()

    def reset_model(self):
        self.classifier = TextClassifier()

    def make_preprocessing(self, steps: list):

        self.classifier.preprocessing = StepsPipeline([self.preprocessingFactory.create_step(step) for step in steps])

    def make_model(self):

        self.classifier.model = self.classifierFactory.create_step('logistic regression')

    def load_data(self, csv_path: str, col_x: str, col_y: str):

        df = pd.read_csv(csv_path, usecols=['type', col_x, col_y], encoding='ISO-8859-1')#.sample(1000)
        df = df[df['type'] == 'train']
        self.classifier.data['X'] = df[col_x].values.tolist()
        self.classifier.data['Y'] = df[col_y].values.tolist()



class Director:

    def __init__(self):

        self._builder = None


    @property
    def builder(self) -> TextClassifierBuilder:

        return self._builder

    @builder.setter
    def builder(self, builder:TextClassifierBuilder) -> None:

        self._builder = builder


    def build_baseline_classifier(self):

        self.builder.load_data('data/imdb/imdb_master.csv', 'review', 'label')
        steps = ['BOWVectorizer']
        self.builder.make_preprocessing(steps)
        self.builder.make_model()
        self.builder.classifier.prepare()


    def build_advanced_classifier(self):

        self.builder.load_data('data/imdb/imdb_master.csv', 'review', 'label')
        steps = ['Normalizer', 'BOWVectorizer']
        self.builder.make_preprocessing(steps)
        self.builder.make_model()
        self.builder.classifier.prepare()
