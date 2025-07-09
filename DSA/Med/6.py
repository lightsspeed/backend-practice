# This is 6.py

# Create a program to find the largest number in a list (e.g., [3, 1, 4, 1, 5]) without using max().


numbers = [3, 1, 40, 1, 5]
largest = numbers[0]  # Assume the first number is the largest

for number in numbers:
    if number > largest:
        largest = number  # Update largest if current number is greater

print(largest)  # Output: 40