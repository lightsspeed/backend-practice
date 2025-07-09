# This is Slice6.py

# A generator def gen(): yield from range(3) raises a TypeError. Debug and fix it with proper iteration.

def gen():
    yield from range(3)  # Correct usage
for val in gen():
    print(val)  # Output: 0, 1, 2