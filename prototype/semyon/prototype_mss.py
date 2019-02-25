import random


class QueuePrototype:

    _status = 'free'
    worktime = 5

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, s: str):
        if s == 'busy':
            self._status = s

    @status.getter
    def status(self) -> str:
        if self._status =='busy':
            self.worktime -= 1
            if self.worktime == 0:
                self._status = 'closed'
        return self._status

    def clone(self, **attrs):

        obj = self.__class__()
        obj.__dict__.update(attrs)
        return obj


class CashierDispatcher(object):

    def __init__(self):
        self._queues = {}

    def get_opened_queues(self):

        return self._queues

    def open_queue(self, name, obj):

        self._queues[name] = obj

    def close_queue(self, name):

        del self._queues[name]


if __name__ == '__main__':

    k = 0
    firstcash = QueuePrototype()
    dispatcher = CashierDispatcher()
    dispatcher.open_queue(f'queue_{k}', firstcash)

    for i in range(100):
        newclient = random.uniform(0, 1) > 0.7
        if newclient:
            k += 1
            for n, q in dispatcher.get_opened_queues().copy().items():
                if q.status == 'free':
                    q.status = 'busy'
                elif q.status == 'closed':
                    dispatcher.close_queue(n)
                    print(f'Касса {n} закрыта!')
            else:
                dispatcher.open_queue(f'queue_{k}', firstcash.clone())
                print(f'Сободная касса #{k}')
