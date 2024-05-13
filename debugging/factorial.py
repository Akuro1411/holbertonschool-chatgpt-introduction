#!/usr/bin/python3
import sys

def factorial(n):
    # Handling edge cases
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0:
        return 1
    
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    return result

# Checking if the user has provided the command-line argument
if len(sys.argv) != 2:
    print("Usage: python3 script.py <number>")
    sys.exit(1)

# Validating if the provided argument is an integer
try:
    number = int(sys.argv[1])
except ValueError:
    print("Please provide a valid integer")
    sys.exit(1)

# Calculating and printing the factorial
f = factorial(number)
print(f)

