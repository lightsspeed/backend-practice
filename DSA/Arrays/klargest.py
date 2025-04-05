# Python program to find the k largest elements in the  
# array using min heap

import heapq

# Function to find the k largest elements in the array 
def kLargest(arr, k):
  
    # Create a min-heap with the first k elements
    minH = arr[:k]
    heapq.heapify(minH)
    
    # Traverse the rest of the array
    for x in arr[k:]:
        if x > minH[0]:
            heapq.heapreplace(minH, x)
    
    res = []

    # Min heap will contain only k 
    # largest element
    while minH:
        res.append(heapq.heappop(minH))

    # Reverse the result array, so that all
    # elements are in decreasing order
    res.reverse()

    return res

if __name__ == "__main__":
    arr = [1, 23, 12, 9, 30, 2, 50]
    k = 3
    res = kLargest(arr, k)
    print(" ".join(map(str, res)))



# 🔍 Dry Run for kLargest([1, 23, 12, 9, 30, 2, 50], k=3)
# ✅ Step 1: Create min-heap of first k=3 elements

# arr = [1, 23, 12, 9, 30, 2, 50]
# minH = [1, 23, 12]
# heapq.heapify(minH)  # converts to min-heap → [1, 23, 12]
# minH after heapify → [1, 23, 12]
# (Note: heapq maintains smallest element at index 0)

# 🔁 Step 2: Traverse remaining elements (9, 30, 2, 50)
# x = 9
# → 9 > 1 (min of heap) ✅
# → Replace 1 with 9 → heapreplace(minH, 9)
# minH becomes [9, 23, 12]

# x = 30
# → 30 > 9 ✅
# → Replace 9 with 30 → heapreplace(minH, 30)
# minH becomes [12, 23, 30]

# x = 2
# → 2 < 12 ❌
# → Do nothing

# x = 50
# → 50 > 12 ✅
# → Replace 12 with 50 → heapreplace(minH, 50)
# minH becomes [23, 50, 30]

# 🎯 Step 3: Extract elements from heap
# Heap has 3 largest elements: [23, 50, 30]

# Use heappop():


# res = []
# res.append(23)  → minH: [30, 50]
# res.append(30)  → minH: [50]
# res.append(50)  → minH: []
# res = [23, 30, 50]

# Now reverse it:

# res.reverse() → res = [50, 30, 23]

# ✅ Final Output:

# 50 30 23