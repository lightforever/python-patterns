import typing
import re
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report


class Data:

    def __init__(self, csv_path: str, data_col: str, target_col: str):

        self.csv_path = csv_path
        #
        self.data_col = data_col
        self.target_col = target_col
        self.type = None
        self.reviews = None
        self.labels = None

    def load_data(self):
        df = pd.read_csv(self.csv_path, usecols=['type', self.data_col, self.target_col], encoding='ISO-8859-1').sample(50000)
        self.type = df['type']
        self.reviews = df[self.data_col]
        self.labels = df[self.target_col]


    def clean_data(self, docs:typing.Union[None, typing.List[str]]=None):
        if not isinstance(docs,list):
            self.reviews = self.reviews.apply(lambda x: re.sub('[^a-z0-9 ]', '', x.lower()))
        else:
            return [re.sub('[^a-z0-9 ]', '', d.lower()) for d in docs]

    def get_dataset(self, cut_unsup=False):
        if not cut_unsup:
            X_train = self.reviews[self.type=='train']
            y_train = self.labels[self.type == 'train']

            X_test = self.reviews[self.type=='test']
            y_test = self.labels[self.type == 'test']

        else:
            X_train = self.reviews[(self.type =='train') & (self.labels != 'train')]
            y_train = self.labels[self.type == 'train']

            X_test = self.reviews[self.type=='test']
            y_test = self.labels[self.type == 'test']

        return {
            'X_train': X_train,
            'y_train': y_train,
            'X_test': X_test,
            'y_test': y_test
        }


class Model:

    def __init__(self):
        self.model = Pipeline(steps=[
            ('vectorizer', TfidfVectorizer(stop_words='english',max_features=5000)),
            ('classifier', LinearSVC(class_weight='balanced'))
        ])

    def train(self, data_dict:dict):
        self.model.fit(data_dict['X_train'], data_dict['y_train'])


    def predict(self, docs: typing.List[str]):
        return self.model.predict(docs)

    def get_metrics(self, data_dict):
        X_test = data_dict['X_test']
        y_test = data_dict['y_test']

        y_test_pred = self.model.predict(X_test)

        print(classification_report(y_test,y_test_pred))


class Presentation:

    def __init__(self, model):

        self.model = model

    def analyze_reviews(self, docs):
        try:
            predictions = self.model.predict(docs)
            stats = sum([1 if 'pos' in pred else 0 for pred in predictions])
            print(f'{stats} from {len(docs)} reviews are positive')
        except Exception:
            print('model is invalid')



if __name__ == '__main__':

    data = Data(csv_path='data/imdb/imdb_master.csv', data_col='review', target_col='label')
    model = Model()
    data.load_data()
    data.clean_data()
    data_dict = data.get_dataset()
    model.train(data_dict)
    model.get_metrics(data_dict)

    presentation = Presentation(model)

    presentation.analyze_reviews(data_dict['X_test'])