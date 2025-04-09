# This is Slice4.py

# Write a generator that yields the running sum of a list [1, 2, 3, 4] as it iterates.


def running_sum(numbers):
    total = 0
    for num in numbers:
        total += num
        yield total
for s in running_sum([1, 2, 3, 4]):
    print(s)  # Output: 1, 3, 6, 10