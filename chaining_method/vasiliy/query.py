class Query:
    def __init__(self):
        self.query = ''

    def select(self, *args):
        self.query += 'SELECT ' + ', '.join(map(str, args))
        return self

    def join(self, *args):
        self.query += ' JOIN ' + ', '.join(map(str, args))
        return self

    def filter(self, *args):
        self.query += ' WHERE ' + ', '.join(map(str, args))
        return self

    def execute(self):
        print(self.query)


if __name__ == '__main__':
    Query().select('apple', 'banana').join('fruits').join('citruses').filter('apple is red').execute()
