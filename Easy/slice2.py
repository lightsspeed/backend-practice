# This is slice2.py

# Write a simple generator function that yields numbers from 1 to 3.

def number_generator():
    yield 1
    yield 2
    yield 3
for num in number_generator():
    print(num)  # Output: 1, 2, 3