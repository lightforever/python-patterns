from abc import ABC, abstractmethod


class Builder(ABC):

    @abstractmethod
    def prepare_vectorizer(self) -> object:
        pass

    @abstractmethod
    def prepare_spell_corrector(self) -> object:
        pass

    @abstractmethod
    def prepare_lemmatizer(self) -> object:
        pass

    @abstractmethod
    def prepare_classifier(self) -> object:
        pass


class TextClassifier(object):

    def __init__(self):
        self.pipeline = []

    def make_vectorizer(self):
        self.pipeline.append('BOW vectorizer')

    def make_lemmatizer(self):
        self.pipeline.append('nltk lemmatizer')

    def make_spell_corrector(self):
        self.pipeline.append('pyenchant spell corrector')

    def make_classifier(self):
        self.pipeline.append('linear SVC')


class TextClassifierBuilder(Builder):

    def __init__(self) -> None:

        self.reset_model()

    def reset_model(self):
        self.model = TextClassifier()

    def prepare_vectorizer(self):

        self.model.make_vectorizer()

    def prepare_lemmatizer(self):

        self.model.make_lemmatizer()

    def prepare_spell_corrector(self):

        self.model.make_spell_corrector()

    def prepare_classifier(self):

        self.model.make_classifier()


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

        self._builder.prepare_vectorizer()
        self._builder.prepare_classifier()

    def build_advanced_classifier(self):

        self._builder.prepare_spell_corrector()
        self._builder.prepare_lemmatizer()
        self._builder.prepare_vectorizer()
        self._builder.prepare_classifier()


if __name__=='__main__':

    director = Director()
    builder = TextClassifierBuilder()
    director.builder = builder

    director.build_baseline_classifier()

    print(director.builder.model.pipeline)

    builder.reset_model()

    director.build_advanced_classifier()

    print(director.builder.model.pipeline)


