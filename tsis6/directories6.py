import string

for letter in string.ascii_uppercase:
    filename = letter + ".txt"
    with open(filename, 'w') as file:
        file.write("This is file " + letter)
    print(filename, "created")