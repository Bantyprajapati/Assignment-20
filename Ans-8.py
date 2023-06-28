# Write a python program to create a function that accepts a string and calculate the number of upper case letters and lower case letters.
def count_letters(string):
    uppercase_count = 0
    lowercase_count = 0

    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count

# Test the function
input_string = "Hello World"
upper, lower = count_letters(input_string)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
