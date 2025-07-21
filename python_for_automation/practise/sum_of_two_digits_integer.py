# check weather sum of two digits are integer

# def sum_of_two_digits_are_integer(num1, num2):
#     sum_of_num1_and_num2 = num1 + num2
#     if isinstance(sum_of_num1_and_num2, int):
#         return True
#     else:
#         return False
#
# print(sum_of_two_digits_are_integer(12, 34))

#
values = 54
origin_value = values
sum_of_digits = 0
i = 0
while values > i:
    last_value = values%10
    sum_of_digits+=last_value
    values//=10 # values = values // 10

print(sum_of_digits)