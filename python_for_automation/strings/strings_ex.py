# we can represent strings in either single or double quotes
# string is immutable

name = "Guna"
surname = 'raghavaraju'

'''
strings in python are array of bytes representing unicode characters 
'''
print(name[1]) # u

#multiline string
multiline_string = '''
hello
world
'''

# loops
for x in name:
    print(x)

# while loop
i = 0
while i < len(surname):
    print(surname[i])
    i+=1

# len
print(len(surname))

# check specific string is present or not
if "hello" in multiline_string:
    print(True)
else:
    print(False)

# type() function

# slicing
first_name = "python"
print(first_name[1:2])

# negative indexing

print(first_name[:1])
print(first_name[1:])

# modify string
print(first_name.upper())

# lower()
# replace()
# strip()
# split()
# index()
# find()
# capitalize()
# title()
# casefold()
# isupper()
# islower()
# isalnum
# isalpha
# isdigit
# join()-

# f"name {age}" f strings {} placeholder can have variable, operation and functions.

# .format() method

# escape characters
"""
\n
\t
\\
"""

print("hello" , sep="\n", end="")

