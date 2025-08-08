class Person:

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def get_name(self):
        return self.name

    def __str__(self):
        return f"my name is {self.name} and I'm {self.age} and I'm from {self.address}"

# Object
p1 = Person("guna", 22, "AP")
print(p1.get_name())

# object2
p2 = Person("java", 23, "US")
print(p2)

# deleting attributes
del p1.age

# deleting object
del p2

class Simple:
    pass