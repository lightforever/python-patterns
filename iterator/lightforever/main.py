class Records:
    def __init__(self):
        self.data = [0, 1, 2, 3]

    def __iter__(self):
        for i in self.data:
            yield i

if __name__=='__main__':
    records = Records()
    for r in records:
        print(r)