# Write a python program to create a function that takes a number as a parameter and checks if the number is prime or not.
def check_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    return True

# Example usage
num = 17

if check_prime(num):
    print(f"The number {num} is prime.")
else:
    print(f"The number {num} is not prime.")
