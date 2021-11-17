class reverse_iter:

    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        while not self.iterable:
            raise StopIteration
        temp = self.iterable.pop()
        return temp


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
