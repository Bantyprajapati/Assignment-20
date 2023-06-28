# Write a python program to create a function to check whether a string is an anagram or not.
def is_anagram(str1, str2):
    # Convert the strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Remove any whitespace from the strings
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    # Sort the characters in both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    # Check if the sorted strings are equal
    return sorted_str1 == sorted_str2

# Test the function
input_str1 = "listen"
input_str2 = "silent"
if is_anagram(input_str1, input_str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
