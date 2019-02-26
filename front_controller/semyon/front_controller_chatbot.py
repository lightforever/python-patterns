from abc import ABC, abstractmethod
import typing
import random


class BaseResponce(ABC):

    _patterns = []

    @staticmethod
    @abstractmethod
    def get_responce() -> str:
        pass

    def match_fn(self, message: str) -> bool:
        return any([p in message for p in self._patterns])


class UnknownResponce(BaseResponce):

    @staticmethod
    def get_responce():
        responces = [
            'I don\'t know what you mean. I\'m kind of dumb yet.',
            'Could you come back later?',
            'dunno, lol'
        ]
        return random.choice(responces)


class ScheduleResponce(BaseResponce):

    _patterns = [
        'schedule',
        'timetable',
        'upcoming games',
        'games today'
    ]

    @staticmethod
    def get_responce():
        responces = [
            'Sure ',
            'You got it ',
            'Here it is ',
            'With pleasure '
        ]
        return random.choice(responces) + 'https://stats.nba.com/schedule/'


class Dispather:

    def __init__(self, responces: list):
        self.responces = [r() for r in responces]

    def dispatch(self, message: str):

        definedResponce = UnknownResponce()

        for resp in self.responces:
            if resp.match_fn(message):
                definedResponce = resp

        print(definedResponce.get_responce())


class Handler:

    def process_message(self, message: str) -> typing.Union[str, None]:
        if len(message)<4:
            return 'The message looks noninformative, could you please reformulate it'
        else:
            return None


if __name__ == '__main__':

    dispatcher = Dispather(BaseResponce.__subclasses__())
    handler = Handler()

    mes = ''

    while True:
        mes = input()
        if mes == 'q':
            break

        processed = handler.process_message(mes)

        if isinstance(processed, str):
            print(processed)
        else:
            resp = dispatcher.dispatch(mes)
            print(resp)
