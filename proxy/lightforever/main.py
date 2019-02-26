from abc import ABC, abstractmethod

class BaseWitch(ABC):
    @abstractmethod
    def predict(self) -> str:
        pass

    @abstractmethod
    def curse(self, enemy: str) -> str:
        pass

class Witch(BaseWitch):
    def __init__(self):
        self.asked_count = 1
        self.ask_message = 'Ask me a bit more'

    def predict(self)->str:
        self.asked_count += 1
        if self.asked_count % 3 == 0:
            return 'There is a war between you and nearby kingdom next week'
        return self.ask_message

    def curse(self, enemy: str)->str:
        self.asked_count += 1
        if self.asked_count % 3 == 0:
            return f'Let {enemy} become a hare'
        return self.ask_message

class WitchProxy(BaseWitch):
    def __init__(self, witch):
        self.witch = witch

    def predict(self) -> str:
        while True:
            pred = self.witch.predict()
            if pred!=self.witch.ask_message:
                return pred

    def curse(self, enemy)->str:
        while True:
            answer = self.witch.curse(enemy)
            if answer != self.witch.ask_message:
                return answer

class King:
    def __init__(self, witch: BaseWitch):
        self.witch = witch

    def ask_predict(self):
        pred = self.witch.predict()
        print(f'King asked the witch about a prediction')
        print(f'\tThe prediction is: {pred}')

    def ask_curse(self, enemy):
        curse = self.witch.curse(enemy)
        print(f'King asked the witch to curse an enemy {enemy}')
        print(f'\tThe curse is: {curse}')

if __name__=='__main__':
    witch = Witch()
    witch_proxy = WitchProxy(witch)
    king = King(witch_proxy)
    king.ask_predict()
    king.ask_curse('Bolton')
    king.ask_curse('Jeremy')