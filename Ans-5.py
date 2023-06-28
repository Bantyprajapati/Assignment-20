# Write a python program to create a function to find the Min of three numbers.
def find_min(num1, num2, num3):
    return min(num1, num2, num3)

# Test the function
a = 10
b = 5
c = 8
minimum = find_min(a, b, c)
print("The minimum value is:", minimum)
