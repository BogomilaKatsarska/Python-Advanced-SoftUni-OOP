class Book:
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages

# book = Book("My Book", "Me", 200)
# print(book.name)
# print(book.author)
# print(book.pages)


# "self" се самоизвиква - в нашия пример е "book".
# Функция, която е дефинирана в класа, се нарича метод
# A class is used to create individual instance of an object.