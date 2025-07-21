# set is a collection which is unordered, unchangeable, unindexed, and no duplicate values
set_declaration = {1, 2, 3, 4}

# for loop
for x in set_declaration:
    print(x)

# type() function
print(type(set_declaration))

# len() function
print(len(set_declaration))

diff_data_types_sets = {"name", 5.10, 8.5, False}
print(diff_data_types_sets)

# you can add and remove items in a set, but you can't change them.
# you can't access items with the help of indexing

my_set = {5,4,"python", True}
my_set.add(0)

my_another_set = {"java", "selenium"}
my_set.update(my_another_set)
print(my_set)

# remove(item) if item is not found then it will throw an error
my_set.remove(5)

# discard(item) if item is present in the set then it will remove otherwise it won't raise any error like remove
my_set.discard(5)

# pop() method will remove an item randomly

# clear() method will clear the set

# del keyword deletes the set

# union and update will do same thing
my_set = {5,4,"python", True}
my_another_set = {"java", "selenium"}
my_another_set2 = {"java", "selenium", "pytest"}
result = my_set | my_another_set | my_another_set2
# or
result1 = my_set.union(my_another_set, my_another_set2)

# intersection will return new set that contains items that are present in both sets
intersection_ex = {True, False, "new", 3}
intersection_ex1 = {False, 3, "new"}
result2 = intersection_ex & intersection_ex1
print(result2)

# intersection_update() will modify the same set instead of creating a new set

# difference
difference_ex = {'j', 'v', 'h'}
difference_ex_1 = {'t', 'j'}
print(difference_ex - difference_ex_1)

# difference_update()

# symmetric_difference


