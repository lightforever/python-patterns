from abc import ABC, abstractmethod
import numpy as np


class Embedding(ABC):

    @abstractmethod
    def get_word_vector(self, word: str) -> np.ndarray:
        pass


class EmbeddingModel(Embedding):

    def __init__(self, model_path):
        self.model = self.load_model(model_path)

    @staticmethod
    def load_model(model_path: str):
        print('model loaded')
        return {'': np.zeros(300)}

    def get_word_vector(self, word: str) -> np.ndarray:
        return self.model.get(word, np.ones(300))


class Proxy(Embedding):

    def __init__(self, embedding: Embedding):
        self._model = embedding

    def check_word(self, word: str) -> bool:
        return ' ' not in word

    def get_word_vector(self, word: str):

        if self.check_word(word):
            return self._model.get_word_vector(word)
        else:
            raise ValueError('more than one word found!')


if __name__ == '__main__':

    embedding = EmbeddingModel('')
    proxy = Proxy(embedding)

    print(proxy.get_word_vector('Hello'))

    try:
        proxy.get_word_vector('The Emperor protects')
    except ValueError as e:
        print(e)
