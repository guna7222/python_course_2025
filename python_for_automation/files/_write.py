with open("hello.txt", 'a') as file:
    file.write("appending data to the txt file and")

# opening file
with open("hello.txt", 'r') as file:
    print(file.read())

# 'w' will override the existing content if file is available (it will also create a file if file doesn't exit's)

# 'x' will create a new file if the file doesn't exit's otherwise it will throw an error

# 'a' will also create a file if file doesn't exit's if exit's will append the data