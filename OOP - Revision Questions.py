# Example 1
class Person:
    def __init__(self, name, age):
        self.name = name #instance attribute
        self.age = age

    @property
    def age(self):
        return self.age # return self.__age; Recursion

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError
        self.__age = value

    def greet(self):
        return "Hello, I am a human"

#Q1: Would example 1 work? - No. Recursion occurs in "return self.age" (we do not go to @age.setter)./
# Should write "return self.__age" (the same should be for getters and setters) - Encapsulation lecture
#Q2: What is the problem with the code? - Recursion depth
#Q3: self.name in example 1 is... - instance attribute

# Example 2
class Employee(Person):
    min_age = 16 #class attribute
    max_age = 150

    def __init__(self, name, age):
        self.name = name #instance attribute
        self.age = age

    @staticmethod
    def validate_age(value):
        if value < Employee.min_age or \
                value > Employee.max_age:
            raise ValueError()

    def show_min_age(self):
        return self.min_age

#Q4: min_age in example 2 is... - class attribute
#Q5: In example 2, will self.min_age work? - yes, because of the scope searching/
#Local, non-local, Global variables - searches from inside-out - Inheritance lecture
#Q6: You can use @property decorators to only return a single attribute value and not use it for calculations. - False
#We can use a @property to do a calculation, for example, to increase the ID with +=1.
#We use property to define sth. dynamic.
#Q7: We use super()... - to extend the base class functionality
#Q8: Considering example 2, would the following code work?/
# e = Employee("test", 18)
# print(e.validate_age(20)) - yes, it will


# Example 3

class GreetsMixin:
    def greet(self):
        return "Hello!"


class Manager(Person, GreetsMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Q9: Considering example 3, what would this code print/
# e = Manager("test", 18)
#print(e.greet()) - "Hello, I am a human!" - Method resolution order(MRO). Prints 1stly for Person() from example 1


# Example 4

class Card:
    def __init__(self, holder_name):
        self.holder_name = holder_name
        self.__cvv = 5


#Q10: In example 4, the __cvv is... - private attribute (__)
#Q11: Is it possible to change private attribute outside the class in python? - yes.
# c = Card("Test")
# c._Card_cvv = 100
# print(c._Card__cvv) -> "погрозняваме" го и можем да върнем стойността му, но не бива да го правим
#Q12: Considering example 4, is this code working:
# c = Card("Test Holder Name")
# print(c.__cvv) - no, it will raise an error
#Q13: What is "_Card_cvv" - the mangled cvv
#Q14: Considering example 4, would this code work:
# c = Card("Test Holder Name")
# c.card_number = 456678 - yes, because Python is a dynamic language and can create the property.
#Although, we should not do it - monkey patching - dynamic creation of attributes/methods

# Example 5

class ExampleClass:
    my_class_attr = 6

    def __init__(self):
        self.my_instance_attr = 5

    @classmethod
    def get_instance_attr(cls):
        return cls.my_instance_attr

#Q15: Considering example 5, would this code work:
# e = ExampleClass()
# print(e.get_instance_attr()) - no, because of the scope searching


# Example 6
from abc import ABC


class Being(ABC):
    pass

#Q16: In example 6, is the class being an abstract class? - no, it is not, because of #1.
#1. You cannot create an instance from an abstract class
#2. It should have an abstract method and inherit ABC


# Example 7
class India:
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most widely spoken language of India.")

    def type(self):
        print("India is a developing country.")


class USA:
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self):
        print("USA is a developed country.")


obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()

#Q17: Example 7 is example of... - Polymorphism
#Q18: Can we make instances of an abstract class? - no, we can't
#Q19: How do we enforce the classes which inherits an abstract class to implement a certain method? - @abstractmethod decorator
#Q20:Is it possible to see example of inheritance and encapsulation in 1place - yes, we can


