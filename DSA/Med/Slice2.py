# This is 2.py
# How would you use a generator expression to filter even numbers from a range of 0 to 9?

even_gen = (x for x in range(10) if x % 2 == 0)
print(list(even_gen))  # Output: [0, 2, 4, 6, 8]