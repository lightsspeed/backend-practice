# This is 10.py


# Create a program to split a list into two halves.


def split_list_in_half(lst):
    mid = len(lst) // 2
    first_half = lst[:mid]
    second_half = lst[mid:]
    return first_half, second_half

# Example usage
original_list = [1, 2, 3, 4, 5, 6, 7]
first, second = split_list_in_half(original_list)

print("First half:", first)
print("Second half:", second)
