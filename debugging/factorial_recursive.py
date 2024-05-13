#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Check if the user has provided the command-line argument
if len(sys.argv) != 2:
    print("Usage: python3 script.py <number>")
    sys.exit(1)

# Validate if the provided argument is an integer
try:
    number = int(sys.argv[1])
except ValueError:
    print("Please provide a valid integer.")
    sys.exit(1)

# Calculate and print the factorial
f = factorial(number)
print(f)

