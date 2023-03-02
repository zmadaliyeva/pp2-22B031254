def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    return upper_count, lower_count


my_string = "Hello World!"
result = count_upper_lower(my_string)
print(f"Uppercase count: {result[0]}, Lowercase count: {result[1]}")