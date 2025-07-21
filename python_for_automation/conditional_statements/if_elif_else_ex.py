# control statements or conditional statements

first_name = "guna"
family_name = "raghavaraju"
age = 27

if first_name.lower() == "guna" and age == 27:
    print("Yes, looking for a correct person ")

else:
    print("Not a correct person ")

# elif
num1 = 90
num2 = 95
num3 = 34

if num1 > 50 and num2 < 100:
   print(True)
elif num2 < 100 and num3 > 10:
    print("Yes")
else:
    print(False)

# if you have only one statement.
if num1>50: print(True)

# if you have only one statement to execute
# ternary operator or conditional expression
a = 56
b = 78
print(a) if a> b else print(b)

# pass

if a>b:
    pass
