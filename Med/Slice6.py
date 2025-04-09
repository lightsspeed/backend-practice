# This is 6.py

# How would you use a generator to create an infinite sequence of odd numbers starting from 1?

def odd_generator():
    n = 1
    while True:
        yield n
        n += 2
gen = odd_generator()
for _ in range(5):
    print(next(gen))  # Output: 1, 3, 5, 7, 9


    