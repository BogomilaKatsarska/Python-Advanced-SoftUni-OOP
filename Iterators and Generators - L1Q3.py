class vowels:
    def __init__(self, text):
        self.text = text
        self.start = 0
        self.all_vowels = "AEOUIYaeouiy"
        self.vowels_list = [el for el in self.text if el in self.all_vowels]
        self.end = len(self.vowels_list)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        index = self.start
        self.start += 1
        return self.vowels_list[index]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
