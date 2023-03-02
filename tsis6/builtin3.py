def is_palindrome(string):
    
    string = ''.join(char.lower() for char in string if char.isalnum())
    
    
    return string == string[::-1]

# Example usage
my_string = "A man, a plan, a canal: Panama"
result = is_palindrome(my_string)
print(result)