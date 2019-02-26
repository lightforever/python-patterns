from typing import Dict, List

class Store:
    def __init__(self):
        self.data = [
            {'name': 'John', 'age': 38},
            {'name': 'Janny', 'age': 45},
            {'name': 'Bill', 'age': 25},
        ]

    def query(self, min_age: int, max_age: int)->Dict[str, object]:
        return [row for row in self.data if min_age<=row['age']<=max_age]

class BuisnessLogic:
    def __init__(self, store: Store):
        self.store = store

    def get_old(self)->List[Dict]:
        return self.store.query(35, 100)

    def get_young(self)->List[Dict]:
        return self.store.query(0, 35)

class Ui:
    def __init__(self, logic: BuisnessLogic):
        self.logic = logic

    def show_old(self)->None:
        print('Old People:')
        print('---')

        for man in self.logic.get_old():
            print(f'\tName = {man["name"]} Age = {man["age"]}')

        print('---')
        print()

    def show_young(self)->None:
        print('Young People:')
        print('---')

        for man in self.logic.get_young():
            print(f'\tName = {man["name"]} Age = {man["age"]}')

        print('---')
        print()

if __name__=='__main__':
    store = Store()
    logic = BuisnessLogic(store)
    ui = Ui(logic)

    ui.show_old()
    ui.show_young()