class Mammal:
    def __init__(self, name, mammal_type, sound):
        self.name = name
        self.type = mammal_type
        self.sound = sound
        self.__kingdom = "animals"

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"
 *****************************************************
import unittest
from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    def test_init(self):
        animal = Mammal("Fluffy", "Cat", "Meow")
        self.assertEqual(animal.name, "Fluffy")
        self.assertEqual(animal.type, "Cat")
        self.assertEqual(animal.sound, "Meow")
        self.assertEqual(animal._Mammal__kingdom, "animals")

    def test_make_sound(self):
        mammal = Mammal("Fluffy", "Cat", "Meow")
        res = mammal.make_sound()
        self.assertEqual(res, "Fluffy makes Meow")

    def test_get_kingdom(self):
        mammal = Mammal("Fluffy", "Cat", "Meow")
        res = mammal.get_kingdom()
        self.assertEqual(res, "animals")

    def test_info(self):
        mammal = Mammal("Fluffy", "Cat", "Meow")
        res = mammal.info()
        self.assertEqual(res, "Fluffy is of type Cat")