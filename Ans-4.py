# Write a python program to create a function that checks whether a passed string is palindrome or not.
def check_palindrome(string):
    # Remove spaces and convert to lowercase
    string = string.replace(" ", "").lower()
    
    # Reverse the string
    reversed_string = string[::-1]
    
    # Check if the original and reversed strings are the same
    if string == reversed_string:
        return True
    else:
        return False

# Example usage
input_string = "Madam Arora teaches malayalam"
if check_palindrome(input_string):
    print(f"The string '{input_string}' is a palindrome.")
else:
    print(f"The string '{input_string}' is not a palindrome.")
