import math
import sys
import random
# import my_module
import platform as os
from my_module import this_dict
# external module
import requests

print(math.sqrt(16))
print(sys.version)
print(random.randrange(1, 25))

'''
The module can contain functions, as already described, but also variables of all types 
(arrays, dictionaries, objects etc):
'''

# my own module
# print(my_module.is_eligible_to_vote(19))

# External module
request = requests.get("https://w3schools.com")
print(request.status_code)

print(os.system())
print(dir(os))  # it will list all the available functions and variables
print(dir(requests))

name = this_dict["name"]
print(name)