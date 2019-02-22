import pandas as pd
import numpy as np

class FeatureFactory(object):

    def __init__(self, feature_factory=None):

        self.feature_factory = feature_factory

    def extract(self):

        extractor = self.feature_factory()

        return extractor.extract(csv_path='data/house_prices/train.csv')


class CategoricalFE(object):

    def extract(self, csv_path):
        col = pd.read_csv(csv_path, usecols=['GrLivArea']).values.squeeze()
        return col / np.max(col)


class ContiniousFE(object):

    def extract(self, csv_path):
        col = pd.read_csv(csv_path, usecols=['BsmtFinType1'])
        ohe = pd.get_dummies(col).values
        return ohe


if __name__ == "__main__":

    ff = FeatureFactory(CategoricalFE)
    print(ff.extract())
    ff.feature_factory = ContiniousFE
    print(ff.extract())