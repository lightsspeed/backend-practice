# This is list4.py

# Create a function to rotate a list by k positions to the left.


def rotate_left(lst, k):
    k = k % len(lst)  # Handle k larger than list length
    return lst[k:] + lst[:k]
print(rotate_left([1, 2, 3, 4], 2))  # Output: [3, 4, 1, 2]