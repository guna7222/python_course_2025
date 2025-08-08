import os

if os.path.exists("hello1.txt"):
    os.remove("hello.txt")

else: 
    raise Exception("hello.txt not found")