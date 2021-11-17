class custom_range:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        temp = self.current
        self.current += 1
        return temp

one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)
