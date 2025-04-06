def merge_sort(arr):
    if len(arr) > 1:
        # Step 1: Divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Step 2: Recursively sort both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Step 3: Merge the two halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements from left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements from right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Test case
arr = [13,5,1,19,9]
merge_sort(arr)
print(arr)
