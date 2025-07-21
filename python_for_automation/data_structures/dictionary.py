# dictionary is a collection which is ordered, changeable and doesn't allow duplicate keys
employees = {
    "name" : "guna",
    "age" : 26,
    "height" : 5.10,
    "is_married" : False,
    # "is_married" : True  # this will override above value
}
print(employees)

old_employees = {"years_of_exp": 25, "marks_scored": [12, 34], "names": {
    "first_name": "Guna"
}, "years_of_exp_2": 45}
print(old_employees["years_of_exp"])
print(old_employees["names"]["first_name"])

# we can also use get(key) method
x = old_employees.get("years_of_exp")
print(x)

print(old_employees.keys())

# values() method will return a list with dict values

# items()

for x in old_employees: # keys will be printed
    print(x)

for i in old_employees:
    print(old_employees[i]) # all the values will be printed one by one

for ii in old_employees.values():
    print(ii) # all the values will be printed one by one

for ii in old_employees.keys(): # all the keys will be printed one by one
    print(ii)


# items()
for x, j in old_employees.items():
    print(f"key: {x} - value: {j}")

# copy() method

# Nested dict
cars = {
    "santo" : {
        "modal" : 1989,
        "type": "petrol"
    },
    "bmw" : {
        "modal" : 1989,
        "type": "petrol",
        "fast" : 250
    }
}
print(f"hey Guna {cars["bmw"]["fast"]}")
dict1 = {
    "name" : "prabhas",
    "age" : 26
}

dict2 = {
    "name" : "guna",
    "age" : 27
}

my_dict = {
    "dict1" : dict1,
    "dict2" : dict2
}

print(my_dict)

for x, y in my_dict.items():
    print(x)

    for j in y:
        print(j, y[j])


cars1 = {
    "santo" : {
        "modal" : 1989,
        "type": "petrol"
    },
    "bmw" : {
        "modal" : 1989,
        "type": "petrol",
        "fast" : 250
    }
}

for x, j in cars1.items():
    print(x)

    for y in j:
        print(y, j[y])