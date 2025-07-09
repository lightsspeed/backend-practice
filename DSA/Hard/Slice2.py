# This is Slice2.py

# Write a generator function that yields palindromic numbers up to 100 (e.g., 11, 22).


def palindrome_generator():
    for i in range(1, 101):
        if str(i) == str(i)[::-1]:
            yield i
for p in palindrome_generator():
    print(p)  # Output: 1, 2, 3, ..., 99