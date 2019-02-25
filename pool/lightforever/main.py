from time import sleep
from queue import Queue
from typing import List
from threading import Thread

class Car:
    def __init__(self, name: str):
        self.name = name

    def drive_to(self, location: str)->None:
        sleep(1)

class CarPool:
    def __init__(self, cars: List[Car]):
        self.queue = Queue()
        for car in cars:
            self.queue.put(car)

    def get_car(self)->Car:
        return self.queue.get()

    def put_car(self, car:Car)->None:
        self.queue.put(car)

class UserTravel(Thread):
    def __init__(self, user: str, pool: CarPool, location: str):
        self.user = user
        self.pool = pool
        self.car = self.pool.get_car()
        self.location = location

        super(UserTravel, self).__init__()

    def run(self):
        self.car.drive_to(self.location)
        print(f'User = {self.user}, Car {self.car.name} at the {self.location}')
        self.release_car()

    def release_car(self)->None:
        if self.car is not None:
            self.pool.put_car(self.car)

if __name__=='__main__':
    cars = [Car('BMW'), Car('Toyoto'), Car('Mersedes')]
    pool = CarPool(cars)
    user_locations = [('John', 'Washington'), ('Smith', 'Mayami'), ('Steve', 'Brunks'), ('Ben', 'Hollywood')]
    for user, location in user_locations:
        user_travel = UserTravel(user, pool, location)
        user_travel.start()