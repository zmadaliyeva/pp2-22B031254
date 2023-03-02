def all_true(tuple_val):
    return all(tuple_val)

# Example usage
my_tuple1 = (True, True, True, True)
result1 = all_true(my_tuple1)
print(result1)  

my_tuple2 = (True, False, True, True)
result2 = all_true(my_tuple2)
print(result2)