# This is 5.py
# Write a generator function that yields pairs of numbers from two lists [1, 2] and [3, 4].


def pair_generator(list1, list2):
    for i in range(min(len(list1), len(list2))):
        yield (list1[i], list2[i])
for pair in pair_generator([1, 2], [3, 4]):
    print(pair)  # Output: (1, 3), (2, 4)