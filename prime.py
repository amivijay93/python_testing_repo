import math


def is_prime(num):
    # Prime numbers must be greater than 1
    if num <= 1:
        return False

    # Check for divisors from 2 up to the square root of num
    # int(math.sqrt(num)) + 1 ensures the square root itself is checked
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False  # If a divisor is found, it's not prime

    return True  # No divisors found, it is prime


# Example usage
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")