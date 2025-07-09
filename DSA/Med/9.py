# This is 9.py

# Write a function to count the number of vowels in a string (e.g., "hello world").


def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
print(count_vowels("hello world"))  # Output: 3