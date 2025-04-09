# This is 10.py


# How would you use a generator to yield numbers divisible by 3 from a range of 1 to 15?

def divisible_by_three():
    for i in range(1, 16):
        if i % 3 == 0:
            yield i
for num in divisible_by_three():
    print(num)  # Output: 3, 6, 9, 12, 15