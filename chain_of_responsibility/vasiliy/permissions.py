from abc import ABC, abstractmethod


class User:
    def __init__(self, roles):
        self.roles = roles


class AbstractPermission(ABC):
    def __init__(self, successor=None):
        self.successor = successor

    def __call__(self, user: User):
        res = self.check_permission(user)
        if res is False:
            return 'successfully failed'

        if self.successor is not None:
            return self.successor(user)

        return True

    def check_permission(self, user: User):
        return self.role in user.roles

    @property
    @abstractmethod
    def role(self):
        pass


class Writer(AbstractPermission):
    @property
    def role(self):
        return 'writer'


class Seller(AbstractPermission):
    @property
    def role(self):
        return 'seller'


class Owner(AbstractPermission):
    @property
    def role(self):
        return 'owner'


if __name__ == '__main__':
    all_constraints = Seller(Owner(Writer()))
    weaker_constraints = Writer(Seller())
    user = User(['writer', 'seller'])

    print(all_constraints(user))
    print(weaker_constraints(user))
