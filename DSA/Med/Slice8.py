# This is 8.py
# How can you use a generator to chain two sequences [1, 2] and [3, 4] into one iterator?

from itertools import chain
gen = chain([1, 2], [3, 4])
print(list(gen))  # Output: [1, 2, 3, 4]