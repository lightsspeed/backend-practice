# This is 5.py

# Write a function to merge two sorted lists into one sorted list.

def merge_sortedArrays(List1, List2):

    return sorted(List1+List2)


print(merge_sortedArrays([1, 2, 5, 3], [7, 6, 4]))