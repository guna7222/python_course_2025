# A list is a collection which is ordered, changeable and allow duplicate values.

fruits = ["apple", "banana", "pineapple", "strawberries", "mango"]
print(fruits)

# accessing items in a list
print(fruits[0])

print(fruits[1:2])

# changing items in a list
fruits[0] = "APPLE"

# looping through list
for x in fruits:
    print(x)

for i in range(len(fruits)):
    print(i, fruits[i])

# while loop
i = 0
while i < len(fruits):
    print(f"Best fruit to have daily {fruits[i]}")  # this {} placeholder can contain variables, operations, functions and modifiers
    i+=1

# list methods
# append(item)
fruits.append("kiwi") # append method appends the item to the end of the list.

# insert(index, item)
fruits.insert(0, "watermelon")

# remove("item") method will remove the specified item if it has more than 1 item then the first occurrence of item will be removed
# if specified item is present then it will throw an error
for x in fruits:
    if "apple".upper() in x:
        fruits.remove('APPLE')


# pop(index) or pop() if you don't specify any index by default last item will be removed
fruits.pop()

# del keyword with index
del fruits[1]

# del fruits (deletes the list)

new_fruits = list(fruits)
print("new fruits", new_fruits)

# clear()
fruits.clear() # removes all the items in a list

# extend(iterable) it can be list, tuple, set, dict
nuts = ["Pista", "groundnuts"]
nuts.extend(new_fruits)
print(nuts)

# sort
nuts.sort() # it will give first preference to capital case
print(nuts)
# if you want to make it as insensitive you can to that with key
nuts.sort(key = str.lower)
print(nuts)

numbers = [1,2,3,4,5]
numbers.sort() # ascending order
print(numbers)
numbers.sort(reverse = True) # descending order
print(numbers)
# reverse() this method will reverse the list
numbers.reverse()
print(numbers)

# copy() list
marks = [90, 98, 99, 56, 38]
# i want new list with same values what ever is there in marks I can simply copy a list
backup_marks = marks.copy()

# another way to copy
backup_marks_2 = list(marks)

# final way to copy
backup_marks_3 = marks[:]

print(backup_marks_3)

# list concatenation
list1 = [1,2,"name"]
list2 = [3,4,6]
list3 = list1+list2
print(list3)

# index("name)

# count(4)
