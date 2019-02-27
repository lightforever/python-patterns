

class ImageClassifier:

    def __init__(self, model_type: str):

        _models_dict = {
            'logit': self.logistic_regression_predict,
            'svm': self.svm_predict,
            'net': self.cnn_predict
        }
        self.classifier_fn = _models_dict.get(model_type, self.unknown_model)

    @staticmethod
    def unknown_model():
        raise NotImplementedError('model specified is not implemented')

    @staticmethod
    def logistic_regression_predict():
        print('logistic regression predicting')

    @staticmethod
    def svm_predict():
        print('svm predicting')

    @staticmethod
    def cnn_predict():
        print('conv net predicting')


if __name__ == '__main__':
    imageClassifier1 = ImageClassifier('net')
    imageClassifier1.classifier_fn()

    imageClassifier2 = ImageClassifier('bayes')
    imageClassifier2.classifier_fn()