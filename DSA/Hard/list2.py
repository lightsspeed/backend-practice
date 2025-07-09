# This is list2.py

# Implement a function to merge k sorted lists into one sorted list.


def merge_two_lists(l1, l2):
    result = []
    i = j = 0

    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1

    # Add remaining elements
    result.extend(l1[i:])
    result.extend(l2[j:])
    return result


def merge_k_sorted_lists(lists):
    if not lists:
        return []

    while len(lists) > 1:
        merged_lists = []

        # Merge pairs of lists
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else []
            merged_lists.append(merge_two_lists(l1, l2))

        lists = merged_lists

    return lists[0]


# Example usage
lists = [
    [1, 4, 5],
    [1, 3, 4],
    [2, 6]
]

result = merge_k_sorted_lists(lists)
print("Merged sorted list:", result)
