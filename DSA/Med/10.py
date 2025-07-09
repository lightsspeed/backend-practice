# This is 10.py

# Create a program to sort a list of tuples based on the second element (e.g., [(1, 5), (2, 2), (3, 8)]).



tuples_list = [(1, 5), (2, 2), (3, 8)]
sorted_list = sorted(tuples_list, key=lambda x: x[1])
print(sorted_list)  # Output: [(2, 2), (1, 5), (3, 8)]