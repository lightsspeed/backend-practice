# This is 9.py

# Write a program to find the second largest number in a list.



def find_second_largest(numbers):
    if len(numbers) < 2:
        return "List must have at least two elements."

    largest = second_largest = float('-inf')

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest if second_largest != float('-inf') else "No second largest number found."

# Example usage:
nums = [12, 45, 9, 74, 30, 74]
result = find_second_largest(nums)
print("Second largest number is:", result)
