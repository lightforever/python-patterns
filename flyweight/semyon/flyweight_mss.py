import random


class Client:

    def __init__(self):
        self.items_bought = random.randint(1, 100)


class FlyweightCass:

    def __init__(self, cass_type: str):

        assert cass_type in ['express', 'regular']
        self.cass_type = cass_type

    def serve(self, items_left):

        return items_left - 1


class Cass:

    def __init__(self, items_left: int, flyweight_cass: FlyweightCass):
        self.items_left = items_left
        self.flyweight_cass = flyweight_cass

    def serve(self):
        self.items_left = self.flyweight_cass.serve(self.items_left)


class CassFactory:

    def __init__(self):

        self.cass_flyweights = {
            'express': FlyweightCass('express'),
            'regular': FlyweightCass('regular')
        }

    def find_cass(self, client: Client):

        if client.items_bought > 42:
            print('finding regular cass')
            return Cass(client.items_bought, self.cass_flyweights['regular'])
        else:
            print('finding express cass')
            return Cass(client.items_bought, self.cass_flyweights['express'])


if __name__ == '__main__':
    casses = CassFactory()
    busy_casses = []
    for i in range(1000):
        if random.uniform(0, 1) > 0.7:
            client = Client()
            print(f'new client with {client.items_bought} items')
            busy_casses.append(casses.find_cass(client))

        for cass in busy_casses.copy():
            cass.serve()
            if cass.items_left <= 0:
                busy_casses.remove(cass)
                del cass
