# Write a python program to create a function and print a list where the values are square of numbers between 1 and 30.
def square_numbers(start, end):
    squares = [num**2 for num in range(start, end+1)]
    return squares

# Generate the list of squares
start_num = 1
end_num = 30
squares_list = square_numbers(start_num, end_num)

# Print the list of squares
print("List of squares:")
print(squares_list)
