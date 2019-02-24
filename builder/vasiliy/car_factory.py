class Car:
    def __init__(self):
        self.serial_number = 'some number'

        self.init_body()
        self.init_engine()
        self.init_other_things()

    def init_engine(self):
        self.engine = 'some engine'

    def init_body(self):
        self.body = 'some body'

    def init_other_things(self):
        pass


if __name__ == '__main__':
    car = Car()
    print(car.body, car.engine)
