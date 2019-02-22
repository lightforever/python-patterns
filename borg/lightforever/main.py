class Car:
    __shared_dict = {}

    def __init__(self):
        self.__dict__ = Car.__shared_dict
        self.speed = 0


class Track(Car):
    pass

class CarSingle:
    __instance = None
    def __init__(self):
        if self.__instance is not None:
            raise Exception('CarSingle is already constructed')

    @staticmethod
    def get_instance():
        if CarSingle.__instance is None:
            CarSingle.__instance = CarSingle()
        return CarSingle.__instance


class TrackSingle(Car):
    __instance = None
    @staticmethod
    def get_instance():
        if TrackSingle.__instance is None:
            TrackSingle.__instance = TrackSingle()
        return TrackSingle.__instance

if __name__=='__main__':
    car = Car()
    track = Track()

    car.speed = 10
    print(car.speed)
    print(track.speed)

    print(id(car))
    print(id(track))

    car_single = CarSingle.get_instance()
    car_single2 = CarSingle.get_instance()

    car_single.speed = 20
    print(car_single.speed)
    print(car_single.speed)

    print(id(car_single))
    print(id(car_single2))

    track = TrackSingle.get_instance()
    print(id(track)!=id(car_single))