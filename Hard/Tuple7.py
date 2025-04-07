# This is Tuple7.py

# Write a program to partition a tuple around a pivot value.


def partition_tuple(tup, pivot):
    left = tuple(x for x in tup if x <= pivot)
    right = tuple(x for x in tup if x > pivot)
    return left + right
print(partition_tuple((3, 1, 4, 2), 2))  # Output: (1, 2, 3, 4)