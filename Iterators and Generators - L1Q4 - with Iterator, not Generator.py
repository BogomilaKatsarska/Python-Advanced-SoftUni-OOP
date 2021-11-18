class squares_iter:
    def __init__(self, end):
        self.end = end
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        temp = self.start
        self.start += 1
        return temp ** 2


for el in squares_iter(5):
    print(el)

