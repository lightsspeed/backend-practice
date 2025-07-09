# This is 1.py

# Write a function to count the occurrences of an item in a tuple.


def count_item(tup, item):
    return tup.count(item)
print(count_item((1, 2, 2, 3), 2))  # Output: 2