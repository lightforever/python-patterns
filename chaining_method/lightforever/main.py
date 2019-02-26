class DataFrame:
    def __init__(self):
        self.columns = ['a', 'b', 'c']
        self.data = [
            {'a': 10, 'b': 20, 'c':30},
            {'a': 5, 'b': 10, 'c': 30}
        ]
        self.index = 'a'

    def set_index(self, col):
        assert col in self.columns, 'Column is not in column list'
        self.index = col
        return self

    def slice(self, min_index, max_index):
        self.data = self.data[min_index:max_index]
        return self

if __name__=='__main__':
    df = DataFrame().slice(1, 3).set_index('b')
    print(df.data)
    print(df.index)