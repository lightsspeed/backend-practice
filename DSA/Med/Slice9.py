# This is 9.py
# Write a generator function that yields the factorial of numbers from 1 to 5.


def factorial_generator():
    def fact(n):
        if n == 0: return 1
        return n * fact(n - 1)
    for i in range(1, 6):
        yield fact(i)
for f in factorial_generator():
    print(f)  # Output: 1, 2, 6, 24, 120