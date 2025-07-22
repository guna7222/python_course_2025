# Lambda function is called anonymous function and inline function
# A function can take any number of arguments but can have only 1 expression

# lambda arguments : expression

var = lambda a, b: a * b
value = var(2,2)
print(value)

def myFunction(n):
    return lambda a : a*n

another = myFunction(5)
result = another(5)
print(result)