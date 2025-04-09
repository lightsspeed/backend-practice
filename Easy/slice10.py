# This is slice10.py

# What is the advantage of using generators for large datasets?


# Answer: Generators save memory by yielding one item at a time instead of storing all data; e.g., (x for x in range(1000000)) vs. list(range(1000000)).