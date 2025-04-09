# This is slice7.py

# Write a generator function that yields the characters of the string 'hello'.

def char_generator(text):
    for char in text:
        yield char
for c in char_generator('hello'):
    print(c)  # Output: h, e, l, l, o