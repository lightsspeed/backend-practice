# This is 6.py


# Use a list comprehension to create a tuple of even numbers from 1 to 6.


even_tuple = tuple(x for x in range(1, 7) if x % 2 == 0)
print(even_tuple)  # Output: (2, 4, 6)