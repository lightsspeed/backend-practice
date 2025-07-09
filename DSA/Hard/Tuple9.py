# This is Tuple9.py

# Write a program to find the difference between two tuples.


def tuple_difference(tup1, tup2):
    return tuple(set(tup1) - set(tup2))
print(tuple_difference((1, 2, 3), (2, 3)))  # Output: (1,)