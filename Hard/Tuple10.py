# This is Tuple10.py

# Implement a function to check if a tuple is a palindrome.

def is_tuple_palindrome(tup):
    return tup == tup[::-1]
print(is_tuple_palindrome((1, 2, 2, 1)))  # Output: True