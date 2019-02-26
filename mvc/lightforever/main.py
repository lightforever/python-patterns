class User:
    def __init__(self, name:str, age: int):
        self.name = name
        self.age = age

class UserView:
    def __init__(self, user: User):
        self.user = user

    def print(self):
        print('UserView.print, our fascinating user:')
        print(f'\tName = {self.user.name} Age = {self.user.age}')

class UserController:
    def create(self, name, age):
        model = User(name, age)
        view = UserView(model)
        view.print()

if __name__=='__main__':
    controlelr = UserController()
    controlelr.create('John', 35)