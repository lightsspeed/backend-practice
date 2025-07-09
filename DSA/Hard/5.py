# This is 5.py

# Write a function to check if two strings are anagrams (e.g., "listen" and "silent") using a dictionary.


def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    char_count = {}
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
    for char in str2:
        char_count[char] = char_count.get(char, 0) - 1
        if char_count[char] == 0:
            del char_count[char]
    return len(char_count) == 0
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False



#dry run above code
# str1 = "listen"   # str2 = "silent"
# char_count = {}   # Initialize an empty dictionary to count characters
# for char in str1: # Iterate through each character in str1
#     char_count[char] = char_count.get(char, 0) + 1    # Increment the count of the character in the dictionary
# # After this loop, char_count will be {'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1}
# for char in str2: # Iterate through each character in str2
#     char_count[char] = char_count.get(char, 0) - 1    # Decrement the count of the character in the dictionary
#     # If the count becomes 0, remove the character from the dictionary
#     if char_count[char] == 0:
#         del char_count[char]
# # After this loop, char_count will be empty if str1 and str2 are anagrams
# # If char_count is empty, it means str1 and str2 are anagrams
# # If char_count is not empty, it means str1 and str2 are not anagrams
# return len(char_count) == 0  # Return True if char_count is empty, False otherwise
# print(are_anagrams("listen", "silent"))  # Output: True   
# print(are_anagrams("hello", "world"))    # Output: False
# # Output: True
# # Output: False
