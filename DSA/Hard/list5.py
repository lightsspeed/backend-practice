# This is list5.py

# Write a program to find the median of a list using the quickselect algorithm.



def quickselect(arr, k):
    if not arr:
        return None
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    if k < len(left):
        return quickselect(left, k)
    elif k < len(left) + len(equal):
        return pivot
    else:
        return quickselect(right, k - len(left) - len(equal))
def find_median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (quickselect(lst, n//2 - 1) + quickselect(lst, n//2)) / 2
    return quickselect(lst, n//2)
print(find_median([3, 1, 4, 2]))  # Output: 2.5