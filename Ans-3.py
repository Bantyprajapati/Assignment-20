# Write a python program to create a function that prints the even numbers from a given list.
def print_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    for number in even_numbers:
        print(number)

# Example usage
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Even numbers:")
print_even_numbers(my_list)
