# This is 1.py

# Write a function to implement binary search on a sorted list (e.g., [1, 3, 5, 7, 9]) to find the index of 7.


def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found

print(binary_search([1, 3, 5, 7, 9], 7))  # Output: 3 (index of 7 in the list)
print(binary_search([1, 3, 5, 7, 9], 4))  # Output: -1 (4 is not in the list)