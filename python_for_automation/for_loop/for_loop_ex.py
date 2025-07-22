# for loop is used to iterate over a sequence

programming_languages = ["python", "java", "go", "c", ".NET", "JS"]
for x in programming_languages:
    if x == "python":
        print(f"most famous programming language {x}")

    print(x)

# looping through a string
bike = "Yamaha"
for x in bike:
    print(x)

# continue keyword is used to skip the current iteration and continues with another iteration.
# break keyword is used to break out a loop

for x in bike:
    if x == "m":
        break
    print(x + " test")

# range(1, 12, increment)
for i in range(1, 12, 2):
    print(i)
else:
    print("out of for loop")

# pass keyword