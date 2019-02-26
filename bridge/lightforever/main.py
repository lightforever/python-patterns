from abc import abstractmethod, ABC

class TextClassifyOptions:
    def __init__(self):
        self.lowercase = False
        self.strip = False
        self.uppercase = False

class TextClassfierInner(ABC):
    @abstractmethod
    def classify(self, text: str, options: TextClassifyOptions)->int:
        pass

class TextClassifierClient(ABC):
    @abstractmethod
    def classify(self, text: str, lowercase: bool)->int:
        pass

class SVMTextClassifierInner(TextClassfierInner):
    def __init__(self, alpha: int, beta: int):
        self.alpha = alpha
        self.beta = beta

    def classify(self, text: str, options: TextClassifyOptions):
        if options.lowercase:
            text = text.lower()
        if options.uppercase:
            text = text.upper()
        if options.strip:
            text = text.strip()

        return (self.alpha+self.beta**2)*len(text)>5

class SVMTextClassifierClient:
    def __init__(self, *args, **kwargs):
        self.clf = SVMTextClassifierInner(*args, **kwargs)

    def classify(self, text: str, lowercase: bool) -> int:
        options = TextClassifyOptions()
        options.lowercase = lowercase
        return self.clf.classify(text, options)

if __name__=='__main__':
    client = SVMTextClassifierClient(alpha=2, beta=3)
    print(client.classify('test text', lowercase=False))