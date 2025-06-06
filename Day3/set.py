from typing import Tuple

def find_common_and_unique(list1: list, list2: list) -> Tuple[list, list]:
    set1, set2 = set(list1), set(list2)
    common = list(set1 & set2)  # Intersection
    unique = list(set1 ^ set2)  # Symmetric difference
    return common, unique

# Test cases
if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    common, unique = find_common_and_unique(list1, list2)
    print(f"Common elements: {common}")  # Output: Common elements: [4, 5]
    print(f"Unique elements: {unique}")  # Output: Unique elements: [1, 2, 3, 6, 7, 8]
    print(find_common_and_unique([], [1, 2]))  # Output: ([], [1, 2])