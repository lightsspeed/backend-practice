# This is Slice3.py

# A generator function def count(): for i in range(5): yield i stops after one iteration. Debug and explain why.

def count():
    for i in range(5):
        yield i
gen = count()
print(list(gen))  # Output: [0, 1, 2, 3, 4]