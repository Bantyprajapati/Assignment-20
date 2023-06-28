# Write a python program to create a function to check whether a string is a pangram or not.
import string

def is_pangram(string):
    # Convert the string to lowercase
    string = string.lower()

    # Create a set of all lowercase alphabets
    alphabets = set(string.ascii_lowercase)

    # Remove any punctuation and spaces from the string
    cleaned_string = ''.join(char for char in string if char.isalpha())

    # Check if the cleaned string contains all the alphabets
    return set(cleaned_string) == alphabets

# Test the function
input_string = "The quick brown fox jumps over the lazy dog"
if is_pangram(input_string):
    print("The string is a pangram.")
else:
    print("The string is not a pangram.")
