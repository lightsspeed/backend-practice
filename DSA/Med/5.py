# This is 5.py

# Write a function to merge two dictionaries (e.g., {‘a’: 1} and {‘b’: 2}) into one.


def merge_dicts(dict1, dict2):
    merged = dict1.copy()  # Create a copy of the first dictionary
    merged.update(dict2)   # Update with the second dictionary
    return merged

dict1 = {'a': 1}
dict2 = {'b': 2}


merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)  # Output: {'a': 1, 'b': 2}  