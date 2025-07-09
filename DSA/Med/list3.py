# This is 3.py

# Remove all occurrences of a specific value (e.g., 2) from a list.

num = [1, 1, 6, 5, 8, 8, 1]


nums = [x for x in num if x != 1]

print(nums)

def remove_values(num):

    result = []

    for i in num:
        if i != 1:
            result.append(i)
    return result


num = [1, 1, 6, 5, 8, 8, 1]

print(remove_values(num))    



