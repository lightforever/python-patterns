from abc import ABC, abstractmethod
from typing import List

class AriphmeticOperation(ABC):
    @abstractmethod
    def execute(self)->float:
        pass

class IdentityOperation(AriphmeticOperation):
    def __init__(self, value: float):
        self.value = value

    def execute(self):
        return self.value

class SumOperation(AriphmeticOperation):
    def __init__(self, *operands: List[AriphmeticOperation]):
        self.operands = operands

    def execute(self):
        return sum(o.execute() for o in self.operands)

class MultiplyOperation(AriphmeticOperation):
    def __init__(self, *operands: List[AriphmeticOperation]):
        self.operands = operands

    def execute(self):
        if len(self.operands)==0:
            return 0

        res = self.operands[0].execute()
        for i in range(1, len(self.operands)):
            res *= self.operands[i].execute()

        return res

if __name__ == '__main__':
    val1 = IdentityOperation(1)
    val2 = IdentityOperation(2)

    print('val1', val1.execute(), 'val2', val2.execute())

    s = SumOperation(val1, val2)
    print('SumOperation', s.execute())

    m = MultiplyOperation(s, val2)
    print('MultiplyOperation', m.execute())
