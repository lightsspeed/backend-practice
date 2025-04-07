# This is 10.py

# Create a function to check if a tuple is a subset of another tuple.

def is_subset(tup1, tup2):
    return set(tup1).issubset(set(tup2))
print(is_subset((1, 2), (1, 2, 3)))  # Output: True