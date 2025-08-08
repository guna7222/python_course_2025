"""
Abstraction: showing only essential details and hiding the implementation is called abstraction

encapsulation: biding variables and methods under single entity is called encapsulation

inheritance: acquiring properties from one class to another class is called inheritance

polymorphism:

class: is an object constructor or a blueprint to create an object
"""

class Employee:

    company = "HP"

    def get_salary(self): # self is object1 (it refers to the current object)
        return 45000

object1 = Employee()
print(object1.company)
print(object1.get_salary())