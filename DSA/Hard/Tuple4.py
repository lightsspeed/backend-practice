# This is Tuple4.py

# Create a function to merge k sorted tuples into one sorted tuple.

def merge_k_tuples(tuples):
    return tuple(sorted([x for tup in tuples for x in tup]))
print(merge_k_tuples(((1, 4), (2, 3))))  # Output: (1, 2, 3, 4)