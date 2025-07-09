# Sum of First 20 Fibonacci NumbersWrite a Python program to calculate the sum of the first 20 numbers in the Fibonacci sequence (starting with 0, 1).Expected Output: 10946Tests: Loops, maintaining sequence state, accumulation.☺


#
# Initialize the first two Fibonacci numbers
fibonacci_1 = 0
fibonacci_2 = 1
sum_of_fibonacci = fibonacci_1 + fibonacci_2
# Number of Fibonacci numbers to sum
n = 20
# Calculate the sum of the first 20 Fibonacci numbers
for i in range(2, n):
    next_fibonacci = fibonacci_1 + fibonacci_2
    print(next_fibonacci, end=", ")
    sum_of_fibonacci += next_fibonacci
    # Print the next Fibonacci number
    print(next_fibonacci, end=", ")
    # Print the sum so far
    print("Sum so far:", sum_of_fibonacci)
    # Update the previous two Fibonacci numbers
    fibonacci_1 = fibonacci_2

    fibonacci_2 = next_fibonacci
# Print the last Fibonacci number
print(next_fibonacci, end=", ")
# Print the result
print("Sum of the first 20 Fibonacci numbers is:", sum_of_fibonacci)