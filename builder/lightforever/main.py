class Shop:
    def __init__(self):
        self._build()

    def _create_goods(self)->None:
        self.goods = ['good1', 'good2']

    def _rent_building(self)->None:
        self.building = 'Western Yahoo 2/3, New York city'

    def _hire_employees(self):
        self.employees = ['John', 'Jenny']

    def _build(self):
        self._create_goods()
        self._rent_building()
        self._hire_employees()

if __name__=='__main__':
    shop = Shop()
    print('Shop employees: ', ' '.join(shop.employees))
    print('Shop Building: ', shop.building)
    print('Shop goods: ', ' '.join(shop.goods))