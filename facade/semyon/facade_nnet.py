from abc import ABC, abstractmethod
import typing


class NetBlock(ABC):

    @abstractmethod
    def forward(self):
        pass

    @abstractmethod
    def backward(self):
        pass


class ConvLayer(NetBlock):

    def forward(self):
        print('conv forward')

    def backward(self):
        print('conv backward')


class DenseLayer(NetBlock):

    def forward(self):
        print('dense forward')

    def backward(self):
        print('dense backward')


class PoolLayer(NetBlock):

    def forward(self):
        print('pool forward')

    def backward(self):
        print('pool backward')


class CrossEntropy(NetBlock):

    def forward(self):
        print('cross entropy computed')

    def backward(self):
        print('loss gradient computed')

def create_layer(type: str) -> NetBlock:
    types = {
        'conv': ConvLayer,
        'pool': PoolLayer,
        'dense': DenseLayer,
        'crossentropy': CrossEntropy
    }
    assert type in types

    return types[type]()


class Net(NetBlock):

    def __init__(self, layers: typing.List[str], loss: str):

        self.layers = [create_layer(l) for l in layers]
        self.loss = create_layer(loss)

    def forward(self):
        for layer in self.layers:
            layer.forward()
        self.loss.forward()

    def backward(self):
        self.loss.backward()
        for layer in self.layers[::-1]:
            layer.backward()

    def infer(self):
        for layer in self.layers:
            layer.forward()
        print('predictions obtained!')


class Facade:

    def __init__(self):

        self.net = None

    def build_cat_classifier(self):
        net_structure = [
            'conv',
            'conv',
            'conv',
            'pool',
            'dense',
            'dense'
        ]
        loss = 'crossentropy'
        net = Net(net_structure, loss)

        for epoch in range(42):
            net.forward()
            net.backward()

        self.net = net

    def make_prediction(self):
        self.net.infer()



if __name__ == '__main__':

    facade = Facade()
    facade.build_cat_classifier()
    facade.make_prediction()