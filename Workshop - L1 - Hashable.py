class HashTable:
    def __init__(self): # по примерите виждаме, че не трябва да ни се подават параметри при инициализацията
        self.max_capacity = 4 #dictionary-то в началото може да държи 4 key-value pairs
        self.__keys = [None] * self.max_capacity #създаваме лист 1 за key
        self.__values = [None] * self.max_capacity # създаваме лист 2 за pairs

    @property
    def length(self):
        return self.max_capacity

    def __setitem__(self, key, value):
        """Set a key/value pair.
        If the key does not exist as an element in the list,
        then ValueError is raised and we must wet the new one.
        If it does exist then we update the current element in the list."""
        if len([el for el in self.__keys if el is not None]) == self.max_capacity:
            self.__resize()
        try:
            index = self.__keys.index(key)
            self.__values[index] = value
            return
        except ValueError:
            index = self.get_available_index(key)
            self.__keys[index] = key
            self.__value[index] = value

    def __getitem__(self, key):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            raise KeyError("Key is not in dict")

    def __len__(self):
        return len([el for el in self.__keys if el is not None])

    def __resize(self): #метод, който увеличава дължината на листовете
        self.__keys = self.__keys + [None] * self.max_capacity
        self.__values = self.__values + [None] * self.max_capacity
        self.max_capacity *= 2

    def __check_index(self, index):
        if index == len(self.__keys):
            return self.__check_index(0)
        if self.__keys[index] is None:
            return index
        #We have collision - take the linear approach here
        return self.__check_index(index+1)

    def get_available_index(self, key): #трябва да се погрижи за колизията
        index = self.hash(key)
        available_index = self.__check_index(index)
        # We have collision
        return available_index

    def hash(self, key):
        index = sum([ord(char) for char in key]) % self.max_capacity
        return index

    def get(self, key, default=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return default


#collision = Collision detection is the computational problem of detecting the intersection of two or more objects.
# когато един от индексите се презаписва от друг и така губим първия
#1.linear approach for collision: изчисляваш индекеса и, ако видиш, че там има елемент, продължаваш към следващия индекс, докато не намерим такъв свободен
#2. quadratic approach for collision: там трябва да "прескачаме" през 4 индекса. Той е по-бърз от линейния, но не е толкова щадящ от гледна точка на памет
#3. random approach for collision: избираме рандом индекси

table = HashTable()

table["name"] = "Peter" #трябва да накараме този синтаксис да може да работи като key-values
# __setitem__ dunder method [] == "set item"
table["age"] = 25

print(table)
print(table.get("name"))
print(table["age"]) #implement get item dunder method __getitem__
print(len(table))

# 1.	Overview
# Create a HashTable class that should have the needed functionality for a hash table, such as:
# •	hash(key: str) - a function that should figure out where to store the key-value pair
# •	add(key: str, value: any) - adds a new key-value pair usign the hash function
# •	get(key: str) - returns the value corresponding to the given key
# •	additional "magic" methods, that will make the code in the example work correctrly
# The HashTable should have an attribute called array of type: list, where all the values will be stored. Upon initialization the default length of the array should be 4. After each addition of an element if the HashTable gets too populated, double the length of the array and re-add the existing data.
# You are not allowed to inherit any classes. Feel free to implement your own functionality (and unit tests) or to write the methods by yourself.
