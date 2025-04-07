# This is Tuple5.py

# Write a program to find the median of a tuple using the quickselect algorithm.


def quickselect(tup, k):
    if not tup:
        return None
    pivot = tup[len(tup)//2]
    left = tuple(x for x in tup if x < pivot)
    equal = tuple(x for x in tup if x == pivot)
    right = tuple(x for x in tup if x > pivot)
    if k < len(left):
        return quickselect(left, k)
    elif k < len(left) + len(equal):
        return pivot
    else:
        return quickselect(right, k - len(left) - len(equal))
def find_median(tup):
    n = len(tup)
    if n % 2 == 0:
        return (quickselect(tup, n//2 - 1) + quickselect(tup, n//2)) / 2
    return quickselect(tup, n//2)
print(find_median((3, 1, 4, 2)))  # Output: 2.5