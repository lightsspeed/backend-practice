# This is 1.py

# Write a function to find the factorial of a number (e.g., 5) using a loop.


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial(5))  # Output: 120