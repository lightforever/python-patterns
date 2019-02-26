from abc import ABC, abstractmethod


class CommandLoop:
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)
        return self

    def run(self):
        while self.commands:
            command = self.commands.pop()
            command.execute()


class Command(ABC):
    def __init__(self, target):
        self.target = target

    @abstractmethod
    def execute(self):
        pass


class PrintHelloCommand(Command):
    def execute(self):
        self.target.print_hello()


class CongratulateCommand(Command):
    def __init__(self, target, name):
        super().__init__(target)
        self.name = name

    def execute(self):
        self.target.congratulate(self.name)


class RadioStation:
    def congratulate(self, name):
        print(f'We congratulate {name}')


class TVChannel:
    def print_hello(self):
        print('Hello everyone')


class AdvertisementBoard:
    def print_hello(self):
        print('Hello only guys who paid for our service')


if __name__ == '__main__':
    loop = CommandLoop()
    radio_station = RadioStation()
    tv = TVChannel()
    board = AdvertisementBoard()

    loop.add_command(PrintHelloCommand(tv))
    loop.add_command(PrintHelloCommand(board))
    loop.add_command(CongratulateCommand(radio_station, 'Rick'))

    loop.run()
