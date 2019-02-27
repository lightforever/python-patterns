from copy import deepcopy


class Estimator:
    def __init__(self):
        self.weights = [0.1]*10
        self.bias = [0.1]*10

    def train_epoch(self):
        for i in range(len(self.weights)):
            self.weights[i] += 0.01

        for i in range(len(self.bias)):
            self.bias[i] += 0.01

        return self

    def save(self) -> 'State':
        return State(deepcopy(self.weights), deepcopy(self.bias))

    def resume(self, state: 'State'):
        self.weights = state.weights
        self.bias = state.bias
        return self


class State:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias


if __name__ == '__main__':
    # instead of caretaker
    estimator = Estimator()

    estimator.train_epoch().train_epoch()

    state = estimator.save()

    restored_estimator = Estimator().resume(state)

    print(restored_estimator.weights)
    print(restored_estimator.bias)




