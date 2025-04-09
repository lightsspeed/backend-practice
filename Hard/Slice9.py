# This is Slice9.py

# Write a generator that yields the power set of a list [1, 2] (all possible subsets).


def power_set(items):
    if not items:
        yield set()
        return
    for item in power_set(items[1:]):
        yield set(item)
        yield set(item) | {items[0]}
for subset in power_set([1, 2]):
    print(subset)  # Output: set(), {1}, {2}, {1, 2}