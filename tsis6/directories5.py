def write_list_to_file(filename, lst):
    with open(filename, 'w') as file:
        for item in lst:
            file.write("%s\n" % item)

# Example usage
filename = "example.txt"
my_list = ["apple", "banana", "cherry"]
write_list_to_file(filename, my_list)
print("List written to file", filename)