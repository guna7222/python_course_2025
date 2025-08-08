
# file = open('hello.txt) line 2 and 3 are same by default mode will be rt
# for binary files like images use rb, for text file use rt
file = open("hello.txt", 'r')

reading_file = file.read()
print(reading_file)


# with statement
with open("hello.txt", 'r') as f:
    print(f.read(5))
    print(f.readline())
file.close()

with open("hello.txt", 'r') as f:
    for x in f:
        print(x.upper())