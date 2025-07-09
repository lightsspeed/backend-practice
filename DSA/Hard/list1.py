# This is list1.py

# Write a function to find the k largest elements in a list (e.g., k=2 in [3, 2, 1, 5, 4]).


def find_k_largest_elements(arr, k):
    result = []
    temp = arr.copy()

    for _ in range(k):
        max_val = max(temp)
        result.append(max_val)
        temp.remove(max_val)  # Remove to find next largest

    return result

# Example usage
arr = [3, 2, 1, 5, 4]
k = 2
result = find_k_largest_elements(arr, k)
print("Top", k, "largest:", result)
