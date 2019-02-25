class Being:
    def move(self):
        pass

    def say(self):
        pass


class Snake:
    def creep(self):
        print('snake creeps')

    def hiss(self):
        print('snake hisses')

class Human:
    def go(self):
        print('human goes')

    def speak(self):
        print('human speaks')

class BeingAdapter:
    _initialized = False

    def __init__(self, being, **adapter_funcs):
        self.being = being

        for key, value in adapter_funcs.items():
            setattr(self.being, key, getattr(being, value))

        for key in list(Being.__dict__):
            if not key.startswith('__'):
                if not hasattr(self.being, key):
                    raise Exception(f'{key} has not been adapted for Being class')

        self._initialized = True

    def __getattr__(self, item):
        if self._initialized:
            return getattr(self.being, item)
        return getattr(self, item)

    def __setattr__(self, instance, value):
        if self._initialized:
            setattr(self.being, instance, value)
        else:
            super().__setattr__(instance, value)

if __name__=='__main__':
    snake = Snake()
    human = Human()

    being_snake = BeingAdapter(snake, move='creep', say='hiss')
    being_snake.say()
    being_snake.move()