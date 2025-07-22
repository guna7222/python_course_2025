# a function is a block of a code which will execute when a function is being called.
# def keyword is used to create a function

def find_average(*num1):  # tuple of arguments
    tuple_of_arguments = num1
    sum1 = 0
    length_of_arguments = len(tuple_of_arguments)
    for x in tuple_of_arguments:
        sum1+=x
    average = sum1/length_of_arguments
    return average

# calling a function
print(find_average(1,2,2))

# key value
def user_details(first_name, last_name):
    full_name = first_name + last_name
    return full_name

user_details(last_name="Raghavaraju", first_name="Guna sekhar")


# default arguments
def default_parameter(num1, num2, values = 45): # value is the default argument
    print(values + num1, num2)

default_parameter(46, 45)   # here we are passing only 2 arguments
# if you pass another argument then values variable value will be changed


# Arbitrary with **
def examples(**ex):
    print(ex)
    if ex["language"] == "telugu":
        return "perfect match"
    else:
        return "Not a perfect match"

output = examples(name="guna", age= 34, height = 6, language="telugu".lower())
print(output)

# passing list to the arguments
def list_example(collection):
    for x in collection:
        print(x)

list_values = [12,34,56,87]
list_example(list_values)

# pass
def pass_function():
    pass
