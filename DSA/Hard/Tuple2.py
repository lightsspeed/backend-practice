# This is Tuple2.py

# Implement a function to rotate a tuple by k positions to the right.


def rotate_tuple(tup, k):
    k = k % len(tup)
    return tup[-k:] + tup[:-k]
print(rotate_tuple((1, 2, 3, 4), 2))  # Output: (3, 4, 1, 2)