# This is slice9.py

# Write a generator function to yield squares of numbers from 1 to 3.

def square_generator():
    for i in range(1, 4):
        yield i * i
for sq in square_generator():
    print(sq)  # Output: 1, 4, 9