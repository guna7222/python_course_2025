# variables are containers for storing data values
# in python the variables are created the moment when you assign a value to it.

a = 5
age = 27 # int
name = "Guna" # string

# type casting
abc = str(43)
print(type(abc)) # class 'str'

# single line comments
"""
multiline comments
"""

'''
A variable can have a short name (like x and y) or a more descriptive name (age, car_name, total_volume).

Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.
'''

# legal variable names
_n24s = '23' # legal
gu___34_g = 34 # legal

print(gu___34_g, "legal")

# illegal variable names
'''
$he4 = 4
4gun = 45
etc.,
'''

# camel case
myVar = "each word expect first starts with capital letters"

# pascal case
MyVar = "each word starts with Capital letters"

# snake case
my_var = "snake case"

# assigning multiple values to multiple variables
af,b,c = 10, 11, 12

# assigning 1 value to multiple variables
h = j = i = 454

# unpack a collection
fruits = ["apple", "banana"]
first_fruit, second_fruit = fruits
print(first_fruit, second_fruit)

# global variables
'''
global:-  the variables that are declared outside of a function then that is called as global variable

local variable:- a variable that is declared inside a method then that is called as local variable
'''

names = "global"
def my_function():
    print(names)

my_function()

# another example of local vs global variable
user_age = 34

def age_checker():
    user_age = 34 # local variable
    print(user_age) # since local variable is available, it will give first preference to local variable

print(user_age) # this global variable name remains the same.

# global keyword
# you can make local variable as global variable with global keyword
def present():
    global language
    language = "programming"
present()
print(language)