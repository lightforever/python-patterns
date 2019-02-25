import random


class Cass:

    def __init__(self, number):

        self.number = number
        self.work_time = 5

    def serve(self):

        self.work_time -= 1


class CassesPool:

    def __init__(self, n_casses):
        self.casses = [Cass(i) for i in range(n_casses)]

    def assign_cass(self):
        cass = self.casses.pop(0)
        print(f'cass {cass.number} assigned')
        return cass

    def release_cass(self, cass: Cass):
        print(f'cass {cass.number} released')
        self.casses.append(cass)

    def __len__(self):
        return len(self.casses)



if __name__ == '__main__':
    available_casses =  CassesPool(15)
    busy_casses = []
    for i in range(100):
        new_client = random.uniform(0, 1) > 0.8
        if new_client:
            if len(available_casses)<1:
                print('no casses available. client waiting')
                continue
            else:
                busy_casses.append(available_casses.assign_cass())
        for cass in busy_casses.copy():
            cass.serve()
            if cass.work_time == 0:
                busy_casses.remove(cass)
                available_casses.release_cass(cass)
