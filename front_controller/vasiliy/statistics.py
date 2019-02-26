from abc import ABC, abstractmethod


class AbstractStatistics(ABC):
    @staticmethod
    @abstractmethod
    def get_statistics(data):
        pass


class ImageStatistics(AbstractStatistics):
    @staticmethod
    def get_statistics(image):
        return 'some image statistics'


class CategoricalDataStatistics(AbstractStatistics):
    @staticmethod
    def get_statistics(cat_data):
        return 'some qualitative statistics'


class QuantitativeDataStatistics(AbstractStatistics):
    @staticmethod
    def get_statistics(quantitative_data):
        return 'some quantitative statistics'


class AbstractData(ABC):
    @property
    @abstractmethod
    def data_type(self):
        pass

    @property
    @abstractmethod
    def data(self):
        pass


class ImageData(AbstractData):
    @property
    def data_type(self):
        return 'image'

    @property
    def data(self):
        return 'image data'


class CatData(AbstractData):
    @property
    def data_type(self):
        return 'categorical'

    @property
    def data(self):
        return 'categorical data'


class QuantitativeData(AbstractData):
    @property
    def data_type(self):
        return 'quantitative'

    @property
    def data(self):
        return 'quantitative data'


class StatisticsDispatcher:
    def __init__(self):
        self._registry = {}

    def register(self, statistics_getter: AbstractStatistics, data_type: str):
        self._registry[data_type] = statistics_getter

    def dispatch(self, data: AbstractData):
        if data.data_type in self._registry:
            return self._registry[data.data_type].get_statistics(data)
        raise ValueError(f'There is no registered statistics getters for data type {data.data_type}')


if __name__ == '__main__':
    dispatcher = StatisticsDispatcher()
    dispatcher.register(ImageStatistics(), 'image')
    dispatcher.register(CategoricalDataStatistics(), 'categorical')
    dispatcher.register(QuantitativeDataStatistics(), 'quantitative')

    data = [QuantitativeData(), CatData(), ImageData()]
    print(list(map(dispatcher.dispatch, data)))
