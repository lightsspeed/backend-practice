# This is Slice10.py

# In a debugging scenario, a generator def gen(): for i in range(5): yield i; print(i) prints unexpected values. Explain and fix it.


def gen():
    for i in range(5):
        yield i
for val in gen():
    print(val)  # Output: 0, 1, 2, 3, 4