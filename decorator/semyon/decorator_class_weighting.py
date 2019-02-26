import typing
import math


class Loss:

    def forward(self, y_true: int, y_pred: float) -> float:
        pass


class CrossEntropy(Loss):

    def forward(self, y_true: int, y_pred: float) -> float:
        loss = y_true * math.log(y_pred) + (1 - y_true) * math.log(1 - y_pred)
        return -loss


class Decorator(Loss):

    def __init__(self, loss: Loss):
        self._loss = loss

    @property
    def loss(self):
        return self._loss

    def forward(self, y_true: int, y_pred: float) -> float:
        return self._loss.forward(y_true, y_pred)


class ClassWeightDecorator(Decorator):

    def __init__(self, loss):
        super().__init__(loss)
        self.class_weights = {
            0: 0.5,
            1: 2
        }

    def forward(self, y_true: int, y_pred: float) -> float:
        pure_loss = super().forward(y_true, y_pred)
        weighted_loss = pure_loss * self.class_weights.get(y_true, 1)
        return weighted_loss


if __name__ == '__main__':

    y_true = [0, 1, 1, 0]
    y_pred = [0.21, 0.77, 0.58, 0.15]

    loss = ClassWeightDecorator(CrossEntropy())

    [print(loss.forward(y,p)) for y,p in zip(y_true, y_pred)]