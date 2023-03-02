from functools import reduce


def multiply_list(lst):
    return reduce(lambda x, y: x * y, lst)


my_list = [1, 2, 3, 4, 5]
result = multiply_list(my_list)
print(result)