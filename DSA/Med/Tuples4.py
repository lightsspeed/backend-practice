# This is 4.py


# Create a function to merge multiple tuples into one.

def merge_tuples(*tuples):
    return tuple(x for tup in tuples for x in tup)
print(merge_tuples((1, 2), (3, 4)))  # Output: (1, 2, 3, 4)