from time import sleep

class Student:
    def __init__(self, name: str, clever_level: int):
        self.name = name
        self.clever_level = clever_level

    def __repr__(self):
        return f'Name = {self.name} Clever level = {self.clever_level}'

    def score_subject(self, index:int):
        sleep(0.1)
        return self.clever_level

    @property
    def score(self)->int:
        return sum(self.score_subject(i) for i in range(10))

if __name__=='__main__':
    student = Student('James', 5)
    print(student, 'Score =', student.score)

    student = Student('John', 3)
    print(student, 'Score =', student.score)