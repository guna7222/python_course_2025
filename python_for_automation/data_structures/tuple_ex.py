# tuple is a collection, which is ordered, unchangeable (immutable) and allow duplicate values.

# defining tuple

current_trends = ("genai", "deepfake", "natural processing language")
print(current_trends)

# tuple with 1 item
tuple_with_single_item = ("item1",)

# len() function
print(len(tuple_with_single_item))

# different data types in tuple
diff_data_types = (1, 2.5, True, "world")
print(diff_data_types)

# type function to know the data type of the variable
print(type(diff_data_types))

# tuple constructor
tuple_constructor = tuple(("Guna", 27, 1998))
print(tuple_constructor)

# range of index
range_of_index = tuple(current_trends)
print(range_of_index[1:2])

# check specific item exits in the tuple or not
for x in range_of_index:
    if "genai" in x:
        print(True)
    else:
        print(False)
else:
    print("finally out of for loop")

# converting tuple to list and converting back list to tuple
tuple_ex = (1,2,34,5)
print(tuple_ex)
list_ex = list(tuple_ex)
list_ex[1] = "guna"
tuple_ex = tuple(list_ex)
print(tuple_ex)

# unpack tuples
unpacking_tuples = (1,2,3,4)
a,b,c,d = unpacking_tuples
print(a,b,c,d)

# unpacking another example
unpacking_more_values = (1,2,3,4,5,6,7,9)
*more_values,one,two,three = unpacking_more_values  # *more_values returns a list
print(more_values, one, two, three)

# join tuples using + operator

# methods
'''
count(item) - counts how many times specified values has occured. 
index(item) - returns index of specified item
'''
