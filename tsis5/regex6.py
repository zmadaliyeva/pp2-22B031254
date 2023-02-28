import re

text = 'Python Exercises, PHP exercises.'
print(re.sub("[ ,.]", ":", text))