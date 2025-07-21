# boolean data type can have either True or False
is_married = False
is_eligible_to_vote = True

print(10>9) # True

# almost all the values are True if it has some content

'''
False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
'''

# functions can return True or False
def myFunction() :
  return True

print(myFunction())

if myFunction():
    print("Yes")
else:
    print("Fail")