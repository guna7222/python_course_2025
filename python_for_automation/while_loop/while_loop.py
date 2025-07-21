# with while loop we can execute a set of statements as long as the condition is true

a = 0

while a < 10:
    print(a)
    a+=1

# break

num1 = 45
while num1<50:
    print(num1)
    if num1 == 47:
        break
    num1+=1

# continue keyword
num2 = 50
while num1<100:
    print(num1)
    if num1 == 47:
        break
    num1+=1