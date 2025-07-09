# This is 1.py


# Write a generator function that yields Fibonacci numbers up to 10.


def fibonacci():
    a, b = 0, 1
    while a <= 10:
        yield a
        a, b = b, a + b
for num in fibonacci():
    print(num)  # Output: 0, 1, 1, 2, 3, 5, 8