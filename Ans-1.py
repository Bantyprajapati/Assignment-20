# Write a python program to create a function that takes a list and returns a new list with the original list's unique elements.
def get_unique_elements(lst):
    unique_lst = list(set(lst))
    return unique_lst

# Example usage
my_list = [1, 2, 3, 4, 3, 2, 5, 6, 5, 4]
result = get_unique_elements(my_list)
print("Original List:", my_list)
print("Unique Elements List:", result)
