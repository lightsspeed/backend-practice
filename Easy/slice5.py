# This is slice5.py

# Write a generator function to yield even numbers from 0 to 4.

def even_generator():
    for i in range(0, 5, 2):
        yield i
for num in even_generator():
    print(num)  # Output: 0, 2, 4