# This is 3.py

# Write a program to check if a given string (e.g., "radar") is a palindrome.

def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False