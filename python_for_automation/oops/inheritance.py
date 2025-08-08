class Parent:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_and_last_name(self):
        return f"{self.first_name} {self.last_name}"

x = Parent("guna", "sekhar")
print(x.first_name)

class Child(Parent):
    pass

ch = Child("paths", "python")
print(ch.first_name)