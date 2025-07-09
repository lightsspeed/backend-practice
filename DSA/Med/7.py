# This is 7.py

# Write a program to remove duplicates from a list (e.g., [1, 2, 2, 3, 4, 4]) using a set.


numbers = [1, 2, 2, 3, 4, 4]
unique_numbers = set(numbers)  # Convert list to set to remove duplicates

print(list(unique_numbers))  # Convert back to list and print

# Output: [1, 2, 3, 4]


#remmove duplicates from a list without using set
numbers = [1, 2, 2, 3, 4, 4]
unique_numbers = []  # Initialize an empty list to store unique numbers

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)  # Add to the list if not already present
    
print(unique_numbers)  # Output: [1, 2, 3, 4]