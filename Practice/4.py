# Sum of Squares of First 10 Positive Integers
# Write a Python program to find the sum of the squares of all numbers from 1 to 10.
# Expected Output: 385
# Tests: Loops, exponentiation, accumulation.☺


sum_of_squares = 0

for i in range(1, 11):
    sum_of_squares += i ** 2
print("Sum of squares from 1 to 10 is:", sum_of_squares)