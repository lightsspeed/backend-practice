# This is slice6.py

# What happens when you iterate over a generator multiple times?

# Answer: It can only be iterated once; subsequent iterations yield nothing; e.g., g = (x for x in [1, 2]); list(g); list(g) outputs [].