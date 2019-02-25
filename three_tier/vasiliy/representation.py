from three_tier.vasiliy.models import Cat


class UI:
    @staticmethod
    def pprint(cat: Cat):
        print(f'----{cat.first_name} {cat.last_name}----')

    @staticmethod
    def show_food_to(cat: Cat):
        cat.meow()


if __name__ == '__main__':
    cats = Cat.all()

    for cat in cats:
        UI.pprint(cat)
        UI.show_food_to(cat)
