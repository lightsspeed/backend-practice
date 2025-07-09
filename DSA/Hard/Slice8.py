# This is Slice8.py

# A generator function def infinite(): while True: yield x fails with NameError. Debug and fix it.


def infinite():
    x = 0
    while True:
        yield x
        x += 1
gen = infinite()
for _ in range(3):
    print(next(gen))  # Output: 0, 1, 2