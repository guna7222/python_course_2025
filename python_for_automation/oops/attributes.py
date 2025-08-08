class MyClass:
    class_attribute = 1

    def __init__(self, address):
        #self.class_attribute = class_attribute
        self.address = address


# object
p1 = MyClass("hyd")
print(p1.class_attribute)