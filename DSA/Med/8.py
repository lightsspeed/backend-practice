# Use a while loop to print the Fibonacci sequence up to the 10th number.

a, b = 0, 1
count = 0
while count < 10:
    print(a, end=" ")
    a, b = b, a + b
    count += 1  # Output: 0 1 1 2 3 5 8 13 21 34