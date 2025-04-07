# This is Tuple3.py

# Write a program to find the intersection of multiple tuples.


def tuple_intersection(*tuples):
    return tuple(set.intersection(*map(set, tuples)))
print(tuple_intersection((1, 2, 3), (2, 3, 4), (2, 3)))  # Output: (2, 3)