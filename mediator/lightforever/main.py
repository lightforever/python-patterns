class WindowManger:
    def __init__(self):
        self.windows = []
        self.parents = {}

    def print_parents(self) -> None:
        print('-' * 7)
        for key, value in self.parents.items():
            print(f'Parent: {value.name} Child: {key.name}')
        print('-' * 7)

    def set_parent(self, child, parent: str) -> None:
        if not any(w.name == parent for w in self.windows):
            raise Exception(f'No window with name = {parent}')

        if any(w for w in self.windows if w.name == parent):
            parent_win = next(w for w in self.windows if w.name == parent)
            if parent_win in self.parents and self.parents[parent_win] == child:
                del self.parents[parent_win]

        self.parents[child] = next(w for w in self.windows if w.name == parent)


class Window:
    def __init__(self, name: str, manager: WindowManger):
        self.name = name
        self.manager = manager

    def set_parent(self, name: str):
        self.manager.set_parent(self, name)

    def __hash__(self):
        return self.name.__hash__()

    def __eq__(self, other):
        return other.name == self.name


if __name__ == '__main__':
    manager = WindowManger()
    win1 = Window('win1', manager)
    win2 = Window('win2', manager)
    manager.windows.extend([win1, win2])

    win1.set_parent('win2')
    manager.print_parents()
    win2.set_parent('win1')
    manager.print_parents()
